# Bars AI — Платформа обучения

## Документация

Проект использует Obsidian vault в `docs/` для документации. При изменении структурных файлов (роутеры, модели, страницы, сторы, сервисы, компоненты) — обновляй соответствующие .md файлы в docs/.

Маппинг файлов → документации:
- `backend/app/routers/*` → `docs/архитектура/Структура проекта.md`, `docs/api/API Обзор.md`
- `backend/app/models/*` → `docs/бэкенд/Модели.md`, `docs/архитектура/База данных.md`
- `backend/app/services/*` → `docs/бэкенд/Сервисы.md`
- `src/pages/*`, `src/App.tsx` → `docs/фронтенд/Роутинг.md`
- `src/store/*` → `docs/фронтенд/Сторы.md`
- `src/components/*` → `docs/фронтенд/Компоненты.md`
- `src/lib/pyodideWorker.ts`, `src/hooks/usePyodide.ts`, `src/components/courses/steps/PythonCodingStep.tsx` → `docs/фронтенд/Python Coding.md`
- `backend/app/config.py` → `docs/бэкенд/Конфигурация.md`

Используй `[[вики-линки]]` для связей между заметками.
