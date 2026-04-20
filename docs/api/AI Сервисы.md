# AI Сервисы

## Интеграция

PathMind использует **Claude API** через OpenAI-совместимый SDK (`openai` Python package).

Ключ: `ANTHROPIC_API_KEY` (обязательный), `OPENAI_API_KEY` (опциональный).

## Сервисы

### AI Service (`ai_service.py`)
- Генерация учебного контента
- Эндпоинт: `POST /api/ai/generate`

### Mentor Service (`mentor_service.py`)
- Персональный AI-ментор для каждого пользователя
- Контекст чата сохраняется в БД (модель `Mentor`)
- Эндпоинт: `POST /api/mentor/chat`

## Фронтенд

### Чат-интерфейс (`src/components/chat/`)
- Компоненты чата с AI-ментором
- Поддержка markdown-ответов

### Симулятор (`src/components/simulator/`)
- Симуляция собеседований с AI
- Store: `simulatorStore.ts`

---

См. также: [[Аутентификация]], [[Сервисы]]
