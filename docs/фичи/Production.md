---
updated: 2026-04-27
---

# Production

## URL

| Сервис      | URL                                                  |
|-------------|------------------------------------------------------|
| Приложение  | https://barsai-production.up.railway.app (основной) |
| Admin Panel | https://admin-production-1563.up.railway.app         |

## Деплой: Railway

Оба сервиса развёрнуты на [Railway](https://railway.app) с автодеплоем из ветки `main` на GitHub. При каждом пуше Railway пересобирает Docker-образ и перезапускает контейнер.

## Dockerfile (основное приложение)

Многоэтапная сборка (`/Dockerfile`):

**Stage 1 — frontend** (node:20-slim):
1. `npm ci --legacy-peer-deps`
2. `npm run build` → артефакт `/app/dist`

**Stage 2 — backend** (python:3.12-slim):
1. `pip install -r requirements.txt`
2. Копируется код бэкенда (`backend/`)
3. Копируется фронтенд из Stage 1 в `/app/static`
4. Порт: `3847` (переопределяется через `$PORT`)
5. Healthcheck: `GET /api/health` каждые 30 с, 5 попыток, старт через 300 с

**CMD:**
```sh
python create_tables.py && (python seed_all.py &) && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-3847}
```
Сид запускается фоново, чтобы не блокировать старт сервера.

## Admin Dockerfile

`admin/Dockerfile` — отдельный образ python:3.12-slim. Запускает `alembic upgrade head` перед стартом uvicorn.

## .railwayignore

Файлы, исключённые из контекста сборки:

```
node_modules, backend/venv, __pycache__, .git, .github, .claude,
.superpowers, .zed, .playwright-mcp, docs, dist, *.pyc,
*.tsbuildinfo, .env, .DS_Store, landing-*.png, hero-*.png, mobile-*.png
```

Папка `docs/` исключена — документация не попадает в образ.

## Переменные окружения

Задаются через Railway Variables. Основные ключи описаны в [[../бэкенд/Конфигурация|Конфигурация]]:
`DATABASE_URL`, `REDIS_URL`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `SECRET_KEY`.

## Связанные страницы

- [[../бэкенд/Конфигурация|Конфигурация]] — переменные окружения
- [[Admin Panel|Admin Panel]] — URL и структура админки
- [[../гайды/Деплой|Деплой]] — пошаговый гайд по деплою
