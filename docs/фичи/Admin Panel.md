---
updated: 2026-04-27
---

# Admin Panel

Отдельное React-приложение в директории `admin/`. Развёрнуто на Railway.

**Production URL:** https://admin-production-1563.up.railway.app

## Технологии

- React + TypeScript + Vite
- React Router v6
- Собственный `authStore` (Zustand)
- `admin/Dockerfile` — отдельный образ Python 3.12-slim

## Страницы

| Путь          | Компонент        | Назначение                              |
|---------------|------------------|-----------------------------------------|
| `/`           | `Dashboard`      | Метрики: пользователи, курсы, платежи   |
| `/users`      | `UsersPage`      | Список пользователей, поиск, блокировка |
| `/courses`    | `CoursesPage`    | Управление курсами, статус, публикация  |
| `/moderation` | `ModerationPage` | Модерация контента и отзывов            |
| `/payments`   | `PaymentsPage`   | История платежей                        |
| `/sprints`    | `SprintsPage`    | Создание и завершение [[Спринты|спринтов]]|
| `/ai-course`  | `AICoursePage`   | AI-генерация курсов                     |
| `/login`      | `LoginPage`      | Вход для администратора (role=admin)    |

## Layout

Сайдбар (260 px) + основная область. Иконки из lucide-react. Активный пункт меню выделяется акцентным цветом. В шапке отображается имя администратора.

## AI-генерация курсов (`/ai-course`)

Форма отправляет `multipart/form-data` на `POST /api/ai/generate-course`:
- `topic` — тема курса (обязательно)
- `prompt` — дополнительный контекст
- `language` — язык курса (ru/en/…)
- `difficulty` — beginner / intermediate / advanced
- `sections_count` — количество секций (по умолчанию 5)
- `files[]` — загружаемые файлы с материалами (необязательно)

Ответ содержит `course_id`, `title`, `sections_count`, `lessons_count`.

## Защита маршрутов

`ProtectedRoute` проверяет токен через `authStore.hydrate()`. Незалогиненные пользователи перенаправляются на `/login`.

## Связанные страницы

- [[Спринты|Спринты]] — управление спринтами через `/sprints`
- [[Курсы и шаги|Курсы и шаги]] — AI-генерация и публикация курсов
- [[Production|Production]] — деплой на Railway
