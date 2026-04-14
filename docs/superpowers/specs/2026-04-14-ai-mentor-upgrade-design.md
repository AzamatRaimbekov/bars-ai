# AI Mentor Upgrade — Design Spec

**Date:** 2026-04-14

---

## Overview

Доработка AI ментора: добавление памяти и контекста, интерактивных упражнений, анализа прогресса с рекомендациями, и голосовых уроков. Модульная архитектура из 4 компонентов.

## Архитектура

Ментор-оркестратор объединяет 4 модуля. Перед каждым ответом:
1. Memory Module формирует контекст (история + профиль знаний + прогресс)
2. Progress Advisor добавляет данные о прогрессе и рекомендации
3. Оркестратор решает: обычный ответ, упражнение, рекомендация или голосовой урок
4. Claude генерирует ответ с контекстом всех модулей

```
User → Mentor Page → Orchestrator
                        ├→ Memory Module (контекст + профиль)
                        ├→ Exercise Engine (задачи + проверка)
                        ├→ Progress Advisor (рекомендации + план)
                        └→ Voice Lesson Engine (голосовые уроки)
                              ↓
                        Claude API → Response
```

---

## Модуль 1: Memory Module

### Новые таблицы

**mentor_sessions:**
| Field | Type | Description |
|-------|------|-------------|
| id | UUID PK | |
| user_id | UUID FK→users | |
| direction | String | frontend/english/callcenter/cib |
| title | String | Автогенерируемое название сессии |
| created_at | DateTime | |
| updated_at | DateTime | |

**mentor_messages:**
| Field | Type | Description |
|-------|------|-------------|
| id | UUID PK | |
| session_id | UUID FK→mentor_sessions | CASCADE delete |
| role | String | user/assistant |
| content | Text | Текст сообщения |
| created_at | DateTime | |

**knowledge_profiles:**
| Field | Type | Description |
|-------|------|-------------|
| id | UUID PK | |
| user_id | UUID FK→users | UNIQUE per user+direction |
| direction | String | |
| strengths | JSON | ["тема1", "тема2"] |
| weaknesses | JSON | ["тема3", "тема4"] |
| notes | JSON | Свободные заметки Claude о студенте |
| updated_at | DateTime | |

### Логика

1. При входе на /mentor — загрузить последнюю сессию или создать новую
2. Каждое сообщение → сохранить в mentor_messages
3. Каждые 10 сообщений → Claude анализирует диалог, обновляет knowledge_profile
4. Контекст для запроса = последние 20 сообщений + сводка knowledge_profile + прогресс курсов

### API

- `GET /api/mentor/sessions` — список сессий пользователя
- `POST /api/mentor/sessions` — создать новую сессию
- `GET /api/mentor/sessions/{id}/messages` — история (пагинация: limit/offset)
- `DELETE /api/mentor/sessions/{id}` — удалить сессию
- `GET /api/mentor/profile` — профиль знаний

### Обновлённый chat endpoint

`POST /api/mentor/chat` заменяет старый `/api/ai/chat`:
```json
Request: {
  "session_id": "uuid",
  "content": "текст сообщения"
}
Response: {
  "content": "ответ ментора",
  "session_id": "uuid",
  "message_id": "uuid"
}
```

Оркестратор автоматически:
- Сохраняет оба сообщения в БД
- Подтягивает контекст из Memory Module
- Обновляет knowledge_profile если нужно

---

## Модуль 2: Exercise Engine

### Типы упражнений

1. **Вопрос-ответ** — все направления. Ментор задаёт вопрос, студент отвечает, Claude оценивает.
2. **Код** — только frontend. Ментор даёт задачу, студент пишет код в чате, Claude проверяет корректность.
3. **Ролевые сценарии** — все направления. Ментор играет роль (клиент, тимлид, собеседующий), студент тренируется в диалоге.

### Как работает

Ментор сам решает когда дать упражнение на основе контекста:
- После объяснения темы → вопрос-ответ для проверки
- Если студент попросил практику → код или сценарий
- Если в knowledge_profile есть слабость → целевое упражнение

Упражнения НЕ отдельный UI — они часть обычного чата. Claude генерирует упражнение как обычное сообщение с особой структурой, фронтенд распознаёт по маркерам.

### Маркеры в ответе Claude

Claude оборачивает упражнения в специальные блоки:
```
[EXERCISE:qa]
Вопрос: Что такое замыкание в JavaScript?
[/EXERCISE]

[EXERCISE:code]
Задача: Напиши функцию debounce(fn, delay)
[/EXERCISE]

[EXERCISE:roleplay]
Сценарий: Ты — junior разработчик на code review. Я — senior. Защити свой PR.
[/EXERCISE]

[EXERCISE_RESULT]
Оценка: 8/10
Feedback: Хорошо объяснил замыкание, но забыл упомянуть лексическое окружение.
[/EXERCISE_RESULT]
```

Фронтенд парсит маркеры и рендерит:
- `[EXERCISE:code]` → блок с подсветкой синтаксиса и кнопкой "Отправить код"
- `[EXERCISE:qa]` → обычный текст
- `[EXERCISE:roleplay]` → индикатор "Ролевая игра активна"
- `[EXERCISE_RESULT]` → карточка с оценкой и feedback

### Сохранение результатов

Результаты упражнений → обновление knowledge_profile:
- Правильный ответ → добавить в strengths
- Неправильный → добавить в weaknesses

---

## Модуль 3: Progress Advisor

### Данные

Читает из существующих таблиц:
- `progress.completed_lessons` — пройденные уроки
- `progress.completed_nodes` — пройденные узлы roadmap
- `progress.xp` — общий XP
- `course_enrollments` — записи на курсы
- `knowledge_profiles` — слабые стороны из ментора

### Логика рекомендаций

1. Собрать пройденные уроки по курсам пользователя
2. Найти непройденные уроки, отсортировать по приоритету:
   - Уроки по слабым сторонам из knowledge_profile (высший приоритет)
   - Следующий непройденный урок в sequence (обычный приоритет)
3. Сформировать план на неделю: 3-5 рекомендованных уроков с обоснованием

### API

`GET /api/mentor/recommendations`:
```json
Response: {
  "weekly_plan": [
    {
      "lesson_id": "uuid",
      "lesson_title": "CSS Grid Layout",
      "course_title": "Frontend Development",
      "reason": "У тебя пробел в CSS Grid — ты ошибся на 3 вопросах по этой теме",
      "priority": "high"
    }
  ],
  "stats": {
    "completed_percentage": 45,
    "strong_topics": ["HTML basics", "JavaScript variables"],
    "weak_topics": ["CSS Grid", "React hooks"]
  }
}
```

### Интеграция с чатом

Ментор может:
- Предложить урок: "Я вижу у тебя пробел в CSS Grid. Давай пройдём [этот урок](/courses/{id}/learn/{lesson_id})?"
- Ссылка ведёт прямо на урок в курсе
- После прохождения урока → прогресс обновляется → рекомендации пересчитываются

---

## Модуль 4: Voice Lesson Engine

### Структура голосового урока

Мини-урок 5-10 минут, 5 фаз:
1. **Введение** (30 сек) — "Сегодня разберём тему X. Это важно потому что..."
2. **Объяснение** (2-3 мин) — Основной материал, примеры
3. **Проверка** (1-2 мин) — 2-3 вопроса студенту
4. **Практика** (2-3 мин) — Упражнение или сценарий
5. **Итог** (30 сек) — Резюме + что учить дальше

### Адаптивный темп

- Студент отвечает верно → ускорить, перейти к сложнее
- Студент отвечает неверно → замедлить, объяснить проще, дать ещё пример
- Студент говорит "не понимаю" → переформулировать, дать аналогию

### Стейт машина

```
IDLE → INTRO → EXPLAIN → CHECK → PRACTICE → SUMMARY → IDLE
         ↑__________________________|  (если не понял — назад)
```

### Frontend

Новый компонент `VoiceLessonMode` поверх существующего `VoiceModeOverlay`:
- Отображает текущую фазу урока (прогресс-бар)
- Показывает тему урока
- Кнопки: "Пауза", "Повтори", "Дальше"

### API

`POST /api/mentor/voice-lesson`:
```json
Request: {
  "session_id": "uuid",
  "action": "start" | "next" | "repeat" | "answer",
  "topic": "CSS Grid",  // только для start
  "content": "ответ студента"  // только для answer
}
Response: {
  "phase": "intro" | "explain" | "check" | "practice" | "summary",
  "content": "текст для озвучки",
  "exercise": null | { "type": "qa", "question": "..." },
  "progress": 0.2,  // 0-1 прогресс урока
  "is_complete": false
}
```

---

## Изменения на фронтенде

### Страница Mentor.tsx — обновления

1. Боковая панель с историей сессий (список сессий, создание новой)
2. Парсинг маркеров упражнений в сообщениях
3. Карточка рекомендаций сверху чата ("Рекомендуем пройти...")
4. Кнопка "Голосовой урок" для запуска структурированного урока
5. Индикатор фазы голосового урока

### Новые компоненты

- `SessionList` — список сессий в sidebar
- `ExerciseBlock` — рендер упражнений (qa, code, roleplay)
- `ExerciseResult` — карточка результата
- `RecommendationCard` — рекомендация урока
- `VoiceLessonMode` — UI голосового урока

### Обновлённые хуки

- `useChat` → работает с session_id, сохраняет в БД
- `useMentorSessions` — новый хук для CRUD сессий
- `useRecommendations` — загрузка рекомендаций
- `useVoiceLesson` — стейт машина голосового урока

---

## Миграция БД

Alembic миграция добавляет 3 таблицы:
- `mentor_sessions`
- `mentor_messages`
- `knowledge_profiles`

Старый эндпоинт `/api/ai/chat` остаётся для обратной совместимости. Новый `/api/mentor/chat` используется ментором.

---

## Не входит в скоуп

- Стриминг ответов (отдельная задача)
- Кастомные менторы (создание пользователем)
- Офлайн-режим
- Мониторинг стоимости API
