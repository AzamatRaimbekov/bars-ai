# AI Сервисы — Barsbek

## Интеграция

Bars AI использует **Claude API** (Anthropic) напрямую через HTTP (`httpx`).

Модель: `claude-sonnet-4-20250514`
Ключ: `ANTHROPIC_API_KEY` (обязательный)

## Barsbek — AI-ассистент

**Barsbek** — единый AI-ассистент платформы Bars AI. Дружелюбный, поддерживающий, знающий. Говорит как мудрый старший брат, который искренне хочет чтобы студент добился успеха.

### Специализации (по направлениям)

| Направление | Специализация |
|---|---|
| frontend | HTML, CSS, JS, React, TypeScript |
| english | Vocabulary, grammar, pronunciation (A1-C2) |
| callcenter | Обслуживание клиентов, скрипты, конфликты |
| cib | Финансы, банковские операции, Excel, интервью |
| programming | Python, алгоритмы, структуры данных |
| design | UI/UX, типографика, цвет, Figma |
| marketing | SMM, таргет, копирайтинг, аналитика |
| languages | Любой язык — погружение, мнемоника, культура |

### Промпт-система

Базовый промпт (`BARSBEK_BASE`) + специализация по направлению.

```python
# backend/app/services/ai_service.py
BARSBEK_BASE = """You are Barsbek — the AI learning assistant of Bars AI platform..."""
MENTOR_PROMPTS = {
    "frontend": f"{BARSBEK_BASE}\n\nYour specialty is Frontend...",
    ...
}
```

## Сервисы

### AI Service (`ai_service.py`)
- `chat()` — чат с Barsbek
- `assess()` — оценка уровня студента
- `tip()` — совет дня (кэшируется в Redis на 24ч)
- `score()` — оценка ответа на собеседовании

### Mentor Service (`mentor_service.py`)
- Контекст чата сохраняется в БД (модель `MentorSession`, `MentorMessage`)
- Голосовой режим (Voice Lessons)
- Рекомендации по обучению
- Эндпоинт: `POST /api/mentor/chat`

## Фронтенд

### Чат-интерфейс (`src/components/chat/`)
- ChatWindow, MessageBubble, VoiceModeOverlay

### Страница Ментора (`src/pages/Mentor.tsx`)
- Чат с Barsbek
- Голосовой режим
- История сессий
- Рекомендации по обучению

### Симулятор (`src/components/simulator/`)
- Симуляция собеседований
- Store: `simulatorStore.ts`

---

См. также: [[Аутентификация]], [[Сервисы]], [[Компоненты]]
