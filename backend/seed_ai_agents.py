"""Seed: AI-агенты — построй своего автономного помощника."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "AI-агенты — построй своего автономного помощника"
DESC = (
    "От chatbot к автономному агенту: архитектура agent loop, tool use, "
    "память, MCP, browser automation. Финальный проект — агент, который "
    "сам выполняет многошаговые задачи. Для разработчиков."
)

def info(t, m): return {"type": "info", "title": t, "markdown": m}
def video(t, u): return {"type": "video", "title": t, "url": u}
def tf(s, c): return {"type": "true-false", "statement": s, "correct": c}
def quiz(q, opts): return {"type": "quiz", "question": q, "options": [{"id": chr(97+i), "text": t, "correct": ok} for i, (t, ok) in enumerate(opts)]}
def multi(q, opts): return {"type": "multi-select", "question": q, "options": [{"id": chr(97+i), "text": t, "correct": ok} for i, (t, ok) in enumerate(opts)]}
def order(items): return {"type": "drag-order", "items": items}
def match(pairs): return {"type": "matching", "pairs": [{"left": l, "right": r} for l, r in pairs]}
def cards(pairs): return {"type": "flashcards", "cards": [{"front": f, "back": b} for f, b in pairs]}
def sort_items(cats): return {"type": "category-sort", "categories": [{"name": n, "items": items} for n, items in cats]}


S = [
    {
        "title": "Что такое AI-агент",
        "pos": 0,
        "lessons": [
            {
                "t": "Chatbot vs RAG vs Agent",
                "xp": 20,
                "steps": [
                    info("Три уровня", "## Эволюция\n\n**1. Chatbot** — LLM + история сообщений. Знает только то, что в обучении.\n\n**2. RAG (Retrieval-Augmented)** — Chatbot + векторный поиск по базе документов. Может ответить про твои внутренние данные.\n\n**3. Agent** — Chatbot + **инструменты** + **цикл рассуждения**. LLM сама решает, какой tool вызвать, смотрит результат, делает следующий шаг.\n\n### Ключевое отличие агента\nАгент **сам планирует и выполняет** многошаговую задачу. Chatbot отвечает на вопрос — агент **делает дело**."),
                    match([
                        ("Chatbot", "LLM + история, без внешних данных"),
                        ("RAG", "Chatbot + векторный поиск по документам"),
                        ("Agent", "LLM + tools + цикл рассуждения, многошаговые задачи"),
                    ]),
                    quiz("Что главное в агенте, чего нет в chatbot?", [
                        ("Большая модель", False),
                        ("Цикл: думать → вызвать tool → смотреть результат → продолжать", True),
                        ("Голосовой интерфейс", False),
                        ("Память между сессиями", False),
                    ]),
                    multi("Какие задачи подходят для агента?", [
                        ("Запланировать встречу: найти слоты в календаре, написать всем", True),
                        ("Исследовать тему — погуглить, скачать PDF, суммаризовать", True),
                        ("Ответить на один простой вопрос", False),
                        ("Заполнить отчёт по данным из 3 систем", True),
                    ]),
                ],
            },
            {
                "t": "Agent loop: основа всего",
                "xp": 25,
                "steps": [
                    info("Цикл рассуждения", "## ReAct loop\n\n```\nUSER: «Найди дешёвый билет в Стамбул на следующую неделю»\n\nLLM думает:\n  ходка 1: «Мне нужны даты — спрошу или возьму следующую неделю»\n  → call: search_flights(from='Москва', to='Стамбул', date='2026-05-21..28')\n\nTool возвращает: 12 рейсов\n\nLLM думает:\n  ходка 2: «Отсортирую по цене, возьму топ-3»\n  → call: sort_and_filter(...)\n\nTool возвращает: 3 рейса\n\nLLM думает:\n  ходка 3: «Готово — отвечу пользователю»\n  → return final answer\n```\n\n### Ключевые компоненты\n1. **System prompt** — описание роли и доступных tools\n2. **Tools** — функции, которые LLM может вызвать\n3. **Loop** — повторяется пока LLM не решит «finished»\n4. **Stop conditions** — лимит ходок, бюджет токенов, явное завершение"),
                    order([
                        "LLM получает задачу + список tools",
                        "LLM рассуждает (think) и решает: вызвать tool или ответить",
                        "Если tool — приложение исполняет, передаёт результат обратно",
                        "LLM смотрит результат, рассуждает дальше",
                        "Цикл до stop condition или final answer",
                    ]),
                    multi("Что обязательно для безопасного agent loop?", [
                        ("Лимит на количество ходок (например, 20)", True),
                        ("Бюджет токенов", True),
                        ("Возможность пользователю прервать", True),
                        ("Бесконечный цикл без лимитов", False),
                    ]),
                    tf("Agent loop повторяется, пока LLM сама не решит завершить или не сработает stop condition.", True),
                ],
            },
            {
                "t": "Frameworks: Anthropic SDK, OpenAI Agents, LangGraph",
                "xp": 20,
                "steps": [
                    info("С чего начать", "## Главные опции 2026\n\n### Anthropic Agent SDK (Python/TypeScript)\nОфициальный SDK от Anthropic. Тонкий, понятный. Tool use, MCP-интеграция из коробки. **Рекомендую новичкам.**\n\n### OpenAI Agents SDK\nОт OpenAI. Похоже по идеологии. Хорошо для GPT-моделей.\n\n### LangGraph (LangChain)\nГраф-based. Для сложных multi-agent сценариев. Steeper learning curve.\n\n### CrewAI\nИгровая абстракция: «роли», «команды». Быстро прототипировать.\n\n### Свой код\nИногда самое быстрое — написать loop в 100 строках без фреймворка."),
                    match([
                        ("Anthropic Agent SDK", "Простой, официальный, рекомендуют для старта"),
                        ("OpenAI Agents", "Аналог от OpenAI"),
                        ("LangGraph", "Граф-based, для сложных multi-agent"),
                        ("CrewAI", "Роли + команды, быстрый прототип"),
                    ]),
                    quiz("С чего лучше начать первый агент?", [
                        ("Сразу LangGraph + Kubernetes", False),
                        ("Anthropic SDK или OpenAI SDK + Python скрипт", True),
                        ("Без кода вообще", False),
                    ]),
                    tf("Часто проще написать свой 100-строчный loop, чем учить тяжёлый фреймворк.", True),
                ],
            },
        ],
    },
    {
        "title": "Tools: руки агента",
        "pos": 1,
        "lessons": [
            {
                "t": "Анатомия tool",
                "xp": 25,
                "steps": [
                    info("Schema + handler", "## Что такое tool для LLM\n\nКаждый tool = пара:\n1. **Schema** — описание в JSON: имя, описание, параметры с типами\n2. **Handler** — функция в твоём коде, которая исполняется\n\n### Пример (Anthropic SDK, Python)\n```python\nfrom anthropic import Anthropic\n\ntools = [{\n    \"name\": \"get_weather\",\n    \"description\": \"Get current weather for a city\",\n    \"input_schema\": {\n        \"type\": \"object\",\n        \"properties\": {\n            \"city\": {\"type\": \"string\", \"description\": \"City name\"},\n            \"unit\": {\"type\": \"string\", \"enum\": [\"celsius\", \"fahrenheit\"]}\n        },\n        \"required\": [\"city\"]\n    }\n}]\n```\n\n### Главное\n- **Description** — LLM выбирает tool по описанию. Пиши подробно!\n- **Schema** — Pydantic / JSON Schema валидируется автоматически\n- **Handler** возвращает строку или JSON-объект, который LLM получает следующей ходкой"),
                    multi("Что нужно для хорошего tool?", [
                        ("Понятное name", True),
                        ("Подробный description — LLM выбирает по нему", True),
                        ("Чёткая input schema", True),
                        ("Возвращаемый тип, понятный LLM (строка / JSON)", True),
                        ("Случайные имена параметров", False),
                    ]),
                    quiz("По чему LLM выбирает, какой tool вызвать?", [
                        ("По имени tool", False),
                        ("По description (главное) + schema", True),
                        ("Случайно", False),
                        ("По алфавиту", False),
                    ]),
                    tf("Чем подробнее description у tool, тем точнее LLM его вызывает.", True),
                ],
            },
            {
                "t": "Tool use loop в коде",
                "xp": 30,
                "steps": [
                    info("Полный код агента", "## Минимальный агент на Anthropic SDK\n\n```python\nfrom anthropic import Anthropic\n\nclient = Anthropic()\n\ndef run_agent(user_message, tools, handlers, max_iters=10):\n    messages = [{\"role\": \"user\", \"content\": user_message}]\n    for _ in range(max_iters):\n        resp = client.messages.create(\n            model=\"claude-sonnet-4-6\",\n            max_tokens=2048,\n            tools=tools,\n            messages=messages,\n        )\n        # Если LLM решила вызвать tool\n        if resp.stop_reason == \"tool_use\":\n            messages.append({\"role\": \"assistant\", \"content\": resp.content})\n            tool_results = []\n            for block in resp.content:\n                if block.type == \"tool_use\":\n                    result = handlers[block.name](**block.input)\n                    tool_results.append({\n                        \"type\": \"tool_result\",\n                        \"tool_use_id\": block.id,\n                        \"content\": str(result),\n                    })\n            messages.append({\"role\": \"user\", \"content\": tool_results})\n        else:\n            return resp.content[0].text\n    return \"Hit iteration limit\"\n```"),
                    order([
                        "Отправить сообщения + tools в LLM",
                        "Проверить stop_reason",
                        "Если tool_use — вызвать handler, добавить результат в messages",
                        "Если end_turn — вернуть финальный текст",
                        "Лимит на итерации (защита от бесконечного цикла)",
                    ]),
                    multi("Что должен делать loop?", [
                        ("Иметь max_iters лимит", True),
                        ("Передавать ВСЮ историю сообщений каждую итерацию", True),
                        ("Сохранять tool_use_id для связи запрос-результат", True),
                        ("Игнорировать stop_reason — всегда продолжать", False),
                    ]),
                    quiz("Что значит stop_reason='tool_use'?", [
                        ("LLM закончила работу", False),
                        ("LLM хочет вызвать инструмент, ждёт результат", True),
                        ("Ошибка", False),
                        ("Превышен лимит токенов", False),
                    ]),
                ],
            },
            {
                "t": "Browser automation, computer use",
                "xp": 25,
                "steps": [
                    info("Агент в браузере", "## Browser Use / Computer Use\n\n**Anthropic Computer Use** (2024+) — LLM может **видеть скриншот экрана** и решать: кликнуть, напечатать, прокрутить.\n\n**Browser Use** (open-source) — то же, но только в браузере, через Playwright.\n\n### Сценарии\n- Заказать пиццу через сайт\n- Заполнить форму на госуслугах\n- Парсить сайты без API\n- Тестирование UI\n\n### Минимальный пример (Browser Use)\n```python\nfrom browser_use import Agent\nfrom langchain_anthropic import ChatAnthropic\n\nagent = Agent(\n    task=\"Найди дешёвый рейс Москва-Стамбул на 21 мая\",\n    llm=ChatAnthropic(model=\"claude-sonnet-4-6\"),\n)\nresult = await agent.run()\n```\n\n### Ограничения\n- **Медленно** (каждый клик = новый screenshot + LLM-вызов)\n- **Дорого** (много токенов на скриншоты)\n- **Хрупко** (UI меняется → агент путается)\n- **Опасно** — может случайно купить, отправить, удалить"),
                    multi("Когда стоит использовать browser automation агента?", [
                        ("Сайт без API", True),
                        ("Прототип / разовая задача", True),
                        ("Тестирование UI", True),
                        ("Высоконагруженный production-парсер (1M запросов/день)", False),
                    ]),
                    tf("Browser automation агент медленнее и дороже, чем прямой API.", True),
                    quiz("Главное ограничение browser-агента?", [
                        ("Не понимает русский", False),
                        ("Хрупкость: UI поменялся — агент сломался", True),
                        ("Не может кликать", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Память и контекст",
        "pos": 2,
        "lessons": [
            {
                "t": "Краткосрочная vs долгосрочная память",
                "xp": 20,
                "steps": [
                    info("Два разных уровня", "## Память\n\n### Краткосрочная (in-context)\nЭто **история текущей беседы** в самом промпте. Ограничена context window (Claude Sonnet 4.6 — 200K-1M токенов).\n\nЛимит = упёрся в стену. Когда диалог длинный, нужно **summarize** старые сообщения.\n\n### Долгосрочная (vector DB / database)\nПомнит **между сессиями**.\n- Профиль пользователя (имя, предпочтения)\n- Прошлые задачи и результаты\n- Knowledge base\n\nХранится в Postgres / Pinecone / Weaviate / SQLite + ручной index.\n\n### Паттерн agentic memory\n```\nперед каждым запросом:\n  1. Достать релевантные воспоминания из БД\n  2. Вставить в system prompt\n  3. Получить ответ\n  4. Сохранить новые факты в БД\n```"),
                    match([
                        ("In-context", "История диалога в самом промпте"),
                        ("Long-term", "Хранится в БД, переживает сессии"),
                        ("Summarize", "Сжимать старые сообщения когда упёрся в context"),
                        ("Vector DB", "Семантический поиск релевантных воспоминаний"),
                    ]),
                    multi("Где хранить долгосрочную память?", [
                        ("PostgreSQL", True),
                        ("Pinecone / Weaviate (vector DB)", True),
                        ("Локальный SQLite + индекс", True),
                        ("В самом коде агента как константы", False),
                    ]),
                    tf("Краткосрочная память помещается в context window, долгосрочная — нет.", True),
                ],
            },
            {
                "t": "MCP как стандартный коннектор",
                "xp": 20,
                "steps": [
                    info("Когда есть MCP", "## MCP + Agents\n\nMCP (Model Context Protocol) даёт твоему агенту готовые tools от внешних серверов. **Не пиши tools для GitHub/Slack/Jira с нуля** — подключи MCP-серверы.\n\n### Минус: ещё не везде есть\n### Плюс: переиспользование, безопасность, обновления вендора\n\n### Пример\n```python\nfrom mcp.client.stdio import stdio_client, StdioServerParameters\n\n# Подключаем готовый GitHub MCP\nparams = StdioServerParameters(\n    command=\"npx\", args=[\"-y\", \"@modelcontextprotocol/server-github\"]\n)\nasync with stdio_client(params) as (read, write):\n    async with ClientSession(read, write) as session:\n        await session.initialize()\n        # Все tools GitHub автоматически доступны\n        result = await session.call_tool(\"create_issue\", {...})\n```\n\nСм. подробный курс по MCP в каталоге."),
                    multi("Что даёт MCP агенту?", [
                        ("Готовые tools (GitHub, Slack, Jira) без переписывания", True),
                        ("Стандарт — один сервер работает в Claude Desktop и в кастомном агенте", True),
                        ("Авто-обновление вендором", True),
                        ("Замену вашего бизнес-кода", False),
                    ]),
                    quiz("Когда лучше использовать MCP-сервер вместо своего tool?", [
                        ("Интеграция с популярной системой (GitHub, Slack)", True),
                        ("Вызов внутренней секретной БД компании", False),
                        ("Тривиальное действие в 2 строки кода", False),
                    ]),
                ],
            },
            {
                "t": "Sub-agents и оркестрация",
                "xp": 25,
                "steps": [
                    info("Разделяй и властвуй", "## Sub-agents\n\nСложную задачу делишь на **под-задачи** для отдельных агентов с разными ролями:\n\n```\nMain Agent: «Сделай отчёт о продажах за квартал»\n  ├─ Researcher: соберёт данные из CRM и БД\n  ├─ Analyst: посчитает тренды, найдёт аномалии\n  ├─ Writer: оформит в красивый отчёт\n  └─ Reviewer: проверит на ошибки\n```\n\n### Зачем\n1. **Изоляция контекста** — каждый агент видит только свой контекст\n2. **Специализация** — разные system prompts под разные роли\n3. **Параллелизм** — могут работать одновременно\n4. **Качество** — критик-агент находит ошибки writer-агента\n\n### Когда НЕ нужно\n- Простая задача в 2-3 шага — overhead не стоит\n- Latency-критичные задачи — sub-agents добавляют ходки\n\n### Anthropic Sub-agent SDK\nВ Claude Code и Agent SDK есть готовый паттерн sub-agents."),
                    multi("Когда оправдан multi-agent дизайн?", [
                        ("Сложная multi-step задача с разными ролями", True),
                        ("Нужна параллельная работа", True),
                        ("Критик/ревьюер должен проверять writer", True),
                        ("Простой single-step запрос", False),
                    ]),
                    tf("Sub-agents добавляют сложность и latency — не делай их без необходимости.", True),
                    quiz("Что главное преимущество sub-agents?", [
                        ("Дешевле", False),
                        ("Изоляция контекста + специализация по ролям", True),
                        ("Faster always", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Production и финальный проект",
        "pos": 3,
        "lessons": [
            {
                "t": "Безопасность агента",
                "xp": 25,
                "steps": [
                    info("Что может пойти не так", "## Топ-рисков\n\n### 1. Prompt injection\nЗлоумышленник вкладывает инструкции в данные, которые агент читает (email, web page, документ). LLM может «послушаться».\n\n**Защита:**\n- Чёткая граница «данные» vs «инструкции»\n- Не давай тулы для критичных действий без подтверждения\n\n### 2. Бесконечные циклы / runaway\nАгент зацикливается, жжёт токены.\n\n**Защита:** `max_iters`, budget на токены, watchdog.\n\n### 3. Tool misuse\nАгент удалил не то, отправил не туда.\n\n**Защита:**\n- **Human-in-the-loop** для деструктивных операций (delete, send, pay)\n- **Read-only** где возможно\n- **Сэндбоксинг** окружения\n- **Audit log** всех вызовов tools\n\n### 4. Утечка данных\nАгент случайно постит секрет в публичный канал.\n\n**Защита:** валидация на исходящих сообщениях, redaction токенов."),
                    match([
                        ("Prompt injection", "Атакующий вшил инструкции в данные"),
                        ("Runaway loop", "Бесконечный цикл, жжёт токены"),
                        ("Tool misuse", "Удалил/отправил не то"),
                        ("Data leak", "Слил секрет в публичный канал"),
                    ]),
                    multi("Что обязательно для production-агента?", [
                        ("max_iters лимит", True),
                        ("Human-in-the-loop для деструктивных действий", True),
                        ("Audit log всех вызовов", True),
                        ("Полная автономия без надзора", False),
                    ]),
                    tf("Деструктивные действия (delete, send money) должны требовать подтверждения человека.", True),
                ],
            },
            {
                "t": "Мониторинг и оптимизация",
                "xp": 20,
                "steps": [
                    info("Метрики агента", "## Что мерить\n\n### Качество\n- **Success rate** — % задач завершённых корректно (нужен ground truth)\n- **Hallucinations** — % фактических ошибок\n- **Tool error rate** — % неудачных вызовов tools\n\n### Стоимость\n- **Tokens per task** — сколько в среднем тратит\n- **API cost per task** — в долларах\n- **Iterations per task** — сколько ходок\n\n### Latency\n- **Time to first action** — как быстро начал делать\n- **Total task time**\n\n### Инструменты\n- **LangSmith / Helicone** — observability для LLM-приложений\n- **OpenTelemetry traces** — для self-hosted\n- **Свой логгер** — простой DB-таблица events\n\n### Дешевле\nКаждая ходка = вызов LLM = деньги. Оптимизация:\n- **Caching prompts** (Anthropic prompt caching)\n- **Меньше iterations** через лучшие промпты\n- **Routing** простых задач на Haiku вместо Sonnet"),
                    multi("Какие метрики агента стоит мерить?", [
                        ("Success rate", True),
                        ("Стоимость на задачу", True),
                        ("Количество ходок", True),
                        ("Цвет интерфейса", False),
                    ]),
                    quiz("Главный способ снизить стоимость агента?", [
                        ("Включить prompt caching", True),
                        ("Увеличить max_iters", False),
                        ("Поменять цвет логотипа", False),
                    ]),
                    tf("Дешёвый Haiku может справиться с простыми задачами агента вместо Sonnet — экономит деньги.", True),
                ],
            },
            {
                "t": "Финал: агент-секретарь",
                "xp": 35,
                "steps": [
                    info("Твой проект", "## Задача\n\nПостроить **агента-секретаря**: на вход почта/мессенджеры — он сам приоритизирует, отвечает на простые, эскалирует сложное.\n\n### Архитектура\n```\n[Email/Slack input] → [Agent loop]\n  ├─ tool: read_inbox()\n  ├─ tool: classify(message) → urgent | normal | spam\n  ├─ tool: draft_reply(message, context)\n  ├─ tool: send_reply(message_id, body)  ← требует подтверждения!\n  ├─ tool: escalate_to_user(message)\n  └─ tool: schedule_meeting(participants, when)\n```\n\n### Чек-лист\n- [ ] Tool descriptions ясные\n- [ ] max_iters = 20\n- [ ] send_reply требует human approval\n- [ ] Все действия — в audit log\n- [ ] Prompt caching включён\n- [ ] Тесты на edge cases (spam, прикреплённые файлы, тред)\n- [ ] Метрики: success rate, токены/задача"),
                    order([
                        "Tools и schemas",
                        "Agent loop с max_iters",
                        "Human-in-the-loop для send/delete",
                        "Audit log",
                        "Тесты на edge cases",
                        "Prompt caching",
                        "Мониторинг (LangSmith / Helicone)",
                    ]),
                    multi("Что должно быть в production-агенте-секретаре?", [
                        ("Подтверждение перед отправкой ответа", True),
                        ("Лимит на стоимость в день", True),
                        ("Audit log", True),
                        ("Полная автономия отправки чему угодно", False),
                    ]),
                    cards([
                        ("Agent loop", "Цикл: думать → tool → результат → продолжать"),
                        ("max_iters", "Лимит на ходки — спасает от runaway"),
                        ("Human-in-the-loop", "Подтверждение для деструктивных действий"),
                        ("Prompt caching", "Кеш system prompt'а — большая экономия токенов"),
                        ("Sub-agents", "Разделение сложной задачи между специализированными агентами"),
                    ]),
                    tf("Production-агент без audit log — это плохая идея.", True),
                ],
            },
        ],
    },
]


async def main():
    async with async_session() as db:
        if (await db.execute(select(Course).where(Course.title == T))).scalar_one_or_none():
            print(f"'{T}' already exists — skipping.")
            return
        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author:
            print("No users.")
            return
        course = Course(
            title=T, slug="ai-agents-" + uuid.uuid4().hex[:4], description=DESC,
            author_id=author.id, category="AI", difficulty="Intermediate",
            price=0, currency="USD", status="published",
            tags=["AI", "Agents", "Programming", "Anthropic"],
        )
        db.add(course); await db.flush()
        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(course_id=course.id, title=sd["title"], position=sd["pos"])
            db.add(sec); await db.flush()
            for li, ld in enumerate(sd["lessons"]):
                les = CourseLesson(section_id=sec.id, title=ld["t"], position=li,
                                   content_type="interactive", content_markdown="",
                                   xp_reward=ld["xp"], steps=ld["steps"])
                db.add(les); await db.flush()
                r, c = lc // 5, lc % 5
                x, y = SNAKE_X[c] * CANVAS_W, V_PAD + r * ROW_H
                nodes.append({"id": str(les.id), "x": x, "y": y})
                if lc > 0:
                    edges.append({"id": f"e-{lc}", "source": nodes[-2]["id"], "target": nodes[-1]["id"]})
                lc += 1; tl += 1
        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
