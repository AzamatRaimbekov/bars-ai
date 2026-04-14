# Community Sprints & Trophy System — Design Spec

**Date:** 2026-04-14

---

## Overview

Система кубков (трофеев) за достижения + 3-недельные спринты с денежными призами. Лидерборд спринта, админ-панель для управления, автоматическое начисление кубков за действия на платформе.

## Кубки — Таблица начислений

| Действие | Кубков | action code |
|----------|--------|-------------|
| Пройти урок | 1 | lesson_complete |
| Пройти все уроки секции | 3 | section_complete |
| Пройти курс полностью | 10 | course_complete |
| Выиграть баттл (Popping) | 5 | battle_win |
| Pose-check ≥90% | 2 | pose_check_90 |
| Streak 7 дней | 3 | streak_7 |
| Streak 30 дней | 10 | streak_30 |
| Первый курс записан | 1 | first_enroll |
| Daily quest выполнен | 1 | daily_quest |

## Спринт — Механика

- **Длительность:** 21 день (3 недели)
- **Автостарт:** если нет активного спринта, система создаёт новый автоматически
- **Админ:** может создать кастомный спринт (свои даты, название, призы) или закрыть текущий досрочно
- **Закрытие:** при закрытии фиксируется лидерборд, определяются победители
- **Статусы:** draft → active → completed | cancelled

### Призы по умолчанию
- 1 место: $100 + 50% от суммы купленных курсов за период спринта
- 2 место: $50
- 3 место: $10

Призы хранятся в JSON поле спринта, админ может изменить при создании.

---

## Новые таблицы

### sprints

| Field | Type | Description |
|-------|------|-------------|
| id | UUID PK | |
| title | String(200) | "Спринт #5" или кастомное название |
| start_date | DateTime | Начало спринта |
| end_date | DateTime | Конец спринта (start + 21 день) |
| status | String(20) | draft / active / completed / cancelled |
| prizes | JSON | [{"place":1,"amount":100,"currency":"USD","bonus":"50% от курсов"},{"place":2,"amount":50},{"place":3,"amount":10}] |
| created_by | UUID FK→users | Кто создал (null для автоматических) |
| closed_by | UUID FK→users | Кто закрыл (null если автоматически) |
| winners | JSON | null до закрытия, потом [{user_id, place, trophies, prize}] |
| created_at | DateTime | |

### trophy_events

| Field | Type | Description |
|-------|------|-------------|
| id | UUID PK | |
| user_id | UUID FK→users | |
| sprint_id | UUID FK→sprints, nullable | null если нет активного спринта |
| action | String(30) | lesson_complete, battle_win, streak_7... |
| trophies | Integer | Количество начисленных кубков |
| metadata | JSON | Доп. данные: {lesson_id, course_id, ...} |
| created_at | DateTime | |

---

## Backend — Новые файлы

### backend/app/models/sprint.py
Модели Sprint и TrophyEvent.

### backend/app/services/trophy_service.py
Логика начисления кубков:
- `award_trophies(db, user_id, action, metadata)` — создаёт TrophyEvent, находит активный спринт
- `get_user_trophies(db, user_id, sprint_id=None)` — сумма кубков пользователя
- `get_sprint_leaderboard(db, sprint_id, limit=50)` — топ пользователей по кубкам

### backend/app/services/sprint_service.py
Управление спринтами:
- `get_active_sprint(db)` — текущий активный спринт (или создать автоматически)
- `create_sprint(db, title, start_date, end_date, prizes, created_by)` — создание кастомного
- `close_sprint(db, sprint_id, closed_by)` — закрытие, фиксация победителей
- `auto_create_sprint(db)` — автосоздание если нет активного

### backend/app/routers/sprint.py
Публичные эндпоинты:
- `GET /api/sprints/active` — текущий спринт
- `GET /api/sprints/active/leaderboard` — лидерборд текущего спринта
- `GET /api/sprints/history` — история спринтов
- `GET /api/sprints/my-trophies` — мои кубки (общие + за текущий спринт)

### backend/app/routers/admin.py
Админ-эндпоинты (только для суперадмина):
- `GET /api/admin/sprints` — все спринты
- `POST /api/admin/sprints` — создать спринт
- `POST /api/admin/sprints/{id}/close` — закрыть спринт
- `POST /api/admin/sprints/{id}/cancel` — отменить спринт
- `GET /api/admin/users` — все пользователи
- `GET /api/admin/stats` — статистика платформы

### Защита админ-эндпоинтов
Новое поле `role` в модели User: "user" (по умолчанию) или "admin".
Dependency `get_admin_user_id` — проверяет role == "admin".

---

## Интеграция с существующими сервисами

Хуки начисления кубков добавляются в:

1. **progress_service.py** → `complete_lesson()` — после успешного завершения урока:
   ```python
   await trophy_service.award_trophies(db, user_id, "lesson_complete", {"lesson_id": str(lesson_id)})
   ```

2. **course_service.py** → `complete_lesson()` — проверить, если все уроки секции/курса пройдены:
   ```python
   # Если вся секция пройдена
   await trophy_service.award_trophies(db, user_id, "section_complete", {"section_id": ...})
   # Если весь курс пройден
   await trophy_service.award_trophies(db, user_id, "course_complete", {"course_id": ...})
   ```

3. **progress_service.py** → `update_streak()` — при streak 7 и 30:
   ```python
   if new_streak == 7:
       await trophy_service.award_trophies(db, user_id, "streak_7")
   if new_streak == 30:
       await trophy_service.award_trophies(db, user_id, "streak_30")
   ```

4. **CourseStepPlayer (frontend)** → при battle_win, pose_check_90:
   - Фронтенд вызывает новый эндпоинт `POST /api/sprints/trophy` с action и metadata

---

## Frontend — Новые файлы

### Страницы
- `src/pages/Sprint.tsx` — публичная страница спринта (лидерборд, таймер, мои кубки)
- `src/pages/Admin.tsx` — админ-панель

### Компоненты
- `src/components/sprint/SprintBanner.tsx` — баннер на Dashboard "Спринт идёт! 12 дней"
- `src/components/sprint/SprintLeaderboard.tsx` — таблица лидеров с местами и кубками
- `src/components/sprint/TrophyCounter.tsx` — виджет 🏆 в TopBar
- `src/components/sprint/PrizeCard.tsx` — карточка приза (1-2-3 место)
- `src/components/admin/SprintManager.tsx` — CRUD спринтов в админке
- `src/components/admin/UsersList.tsx` — список пользователей
- `src/components/admin/PlatformStats.tsx` — статистика

### Сервисы/хуки
- `src/services/sprintApi.ts` — API клиент для спринтов и кубков
- `src/hooks/useActiveSprint.ts` — загрузка текущего спринта
- `src/hooks/useSprintLeaderboard.ts` — лидерборд

### Интеграция
- `TopBar.tsx` — добавить TrophyCounter (🏆 125)
- `Dashboard.tsx` — добавить SprintBanner
- `App.tsx` — добавить роуты /sprint и /admin

---

## Админ-панель UI

Страница `/admin` с табами:

**Таб "Спринты":**
- Текущий активный спринт: название, даты, обратный отсчёт, лидерборд
- Кнопка "Закрыть спринт" (подтверждение) → фиксирует победителей
- Кнопка "Создать новый спринт" → форма: название, даты, призы
- История прошлых спринтов с победителями

**Таб "Пользователи":**
- Таблица: имя, email, кубков за спринт, кубков всего, курсов пройдено, XP
- Фильтр/поиск

**Таб "Статистика":**
- Всего пользователей
- Активных за неделю
- Курсов пройдено
- Кубков выдано
- Доход от курсов за период спринта

---

## Роутинг и защита

```
/sprint — публичная (авторизованные пользователи)
/admin — только role="admin"
```

AdminGuard в App.tsx:
```typescript
function AdminGuard({ children }) {
  const { user } = useAuthStore()
  if (user?.role !== 'admin') return <Navigate to="/dashboard" />
  return children
}
```

---

## Не входит в скоуп

- Реальная платёжная интеграция (Stripe, PayPal) — выплаты пока ручные
- Push-уведомления о спринте
- Командные спринты (пока только индивидуальные)
