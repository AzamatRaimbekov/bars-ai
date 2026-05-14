---
description: Chronological log of wiki changes. Append-only.
---

# Wiki Log

## [2026-05-12] fix | Prod auth 500 + landing language switcher

- Backend: добавил отсутствующие `ALTER TABLE ADD COLUMN IF NOT EXISTS` в `backend/create_tables.py` для `users.organization_id`, `users.is_superadmin`, `courses.organization_id` — Railway-деплой через root `Dockerfile` не запускал alembic, поэтому B2B Phase 1 колонки не создавались и `SELECT` падал. Параллельно создана Alembic-миграция `b1a2c3d4e5f6_add_b2b_saas_phase1_schema.py` для `backend/Dockerfile`-пути.
- Frontend: заменил группу из 4 кнопок-переключателей языка в `LandingNav` на нативный `<select>` — на мобильном навбар больше не переполняется. Обновлены [[фичи/Landing i18n]] и [[фронтенд/Компоненты]].
- Mentor: вернул `lg:flex-row` основному контейнеру `src/pages/Mentor.tsx` — коммит `bad632e` (mobile-fullscreen фикс) случайно сменил layout на `flex-col` для всех брейкпоинтов, из-за чего на десктопе сайдбар сессий стакался поверх чата вместо левой колонки.

## [2026-05-14] ingest | Kids AI course

- Добавлен курс `seed_ai_kids.py` — «ИИ для детей — приключение с роботом Барсбеком» (7+). 7 секций, 23 урока, 106 шагов, 425 XP. Категория AI, Beginner. Минимум текста, упор на видео и игровые шаги: `quiz`, `true-false`, `multi-select`, `drag-order`, `matching`, `category-sort`, `flashcards`. Зарегистрирован в `seed_all.py`. Темы: что такое ИИ, где он живёт, как учится, ИИ-художник, голосовые помощники, ИИ в играх, безопасность.

## [2026-04-27] init | Wiki restructured to LLM Wiki pattern
- Converted existing docs to LLM Wiki pattern with index.md and log.md
- Added feature pages: Геймификация, Спринты, Курсы и шаги, Онбординг, AI Менторство, Admin Panel, Landing i18n, Production
- Updated CLAUDE.md with wiki schema (ingest, query, lint workflows)
- Existing pages preserved and cross-referenced

## [2026-04-27] ingest | Multi-language landing
- Added Landing i18n page documenting 4-language support (RU/EN/KY/UZ)
- Updated Компоненты page with language switcher in LandingNav

## [2026-04-27] ingest | Hero video background
- Updated HeroSection with mascot video as full-screen background
- Fixed .railwayignore to allow PNG/JPG images on production

## [2026-04-27] ingest | Web Speech API for pronunciation
- Replaced OpenAI Whisper with browser Web Speech API
- No API key needed, works in Chrome/Edge/Safari

## [2026-04-27] ingest | AI course generator with file upload
- Added prompt field and file upload (PDF/Word/Excel) to admin AI generator
- Backend extracts text from uploaded files for Claude context

## [2026-04-27] ingest | Currency change KZT to USD
- Replaced all тенге references with dollars across frontend and seeds

## [2026-04-27] fix | Database migrations
- Added missing columns: onboarding_complete, assessment_context, tags
- Backfilled tags for all courses based on category mapping
- Fixed course list 500 error (tags schema allowing None)

## [2026-05-04] ingest | B2B SaaS Phase 1
- Added B2B SaaS feature page documenting multi-tenant architecture
- Updated Модели page with 7 new B2B models (Organization, Department, Role, InviteLink, etc.)
- Updated База данных page with all new model descriptions and User/Course B2B columns
- Updated Аутентификация page with JWT B2B extension, CurrentUser dependency, RBAC permissions
- Updated index.md with B2B SaaS entry

## [2026-05-03] ingest | Contributor guide
- Added root `AGENTS.md` with repo-specific contributor workflow and commands
- Updated project structure wiki to reference the new guide and nested compiler subproject
