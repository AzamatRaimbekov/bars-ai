"""Seed: Claude Code Mastery course — learn to use Claude Code CLI."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSE_TITLE = "Claude Code Mastery"
COURSE_DESC = (
    "Полный курс по Claude Code — AI-ассистенту для разработчиков от Anthropic. "
    "Научитесь использовать CLI для написания кода, отладки, рефакторинга, "
    "работы с git, настройки MCP-серверов и создания автоматизаций."
)

SECTIONS = [
    # ===== SECTION 1 =====
    {
        "title": "Введение в Claude Code",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое Claude Code",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Claude Code — AI в терминале", "markdown": "## Что такое Claude Code?\n\nClaude Code — это CLI-инструмент от Anthropic, который позволяет использовать Claude прямо в терминале для:\n\n- Написания и редактирования кода\n- Отладки ошибок\n- Рефакторинга\n- Работы с git (коммиты, PR)\n- Поиска по кодовой базе\n- Запуска команд в shell\n\n### Ключевые особенности:\n- **Agentic** — Claude сам решает какие файлы читать, какие инструменты использовать\n- **Контекст проекта** — понимает структуру вашего проекта через CLAUDE.md\n- **Безопасность** — спрашивает разрешение перед опасными действиями\n- **MCP** — расширяется через Model Context Protocol серверы"},
                    {"type": "quiz", "question": "Что такое Claude Code?", "options": [{"id": "a", "text": "CLI-инструмент для использования Claude AI в терминале", "correct": True}, {"id": "b", "text": "Визуальный редактор кода", "correct": False}, {"id": "c", "text": "Плагин для VS Code", "correct": False}, {"id": "d", "text": "Языки программирования", "correct": False}]},
                    {"type": "true-false", "statement": "Claude Code работает только в браузере и не имеет CLI-интерфейса.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Claude Code", "back": "CLI-инструмент от Anthropic для agentic-разработки прямо в терминале"}, {"front": "Agentic", "back": "Claude сам выбирает какие инструменты использовать, какие файлы читать и как решить задачу"}, {"front": "CLAUDE.md", "back": "Файл конфигурации проекта — инструкции, стиль кода, архитектура, которые Claude читает автоматически"}, {"front": "MCP", "back": "Model Context Protocol — протокол для подключения внешних инструментов (GitHub, Figma, БД и др.)"}]},
                    {"type": "matching", "pairs": [{"left": "Claude Code", "right": "CLI для AI-разработки"}, {"left": "CLAUDE.md", "right": "Файл с инструкциями для Claude"}, {"left": "MCP", "right": "Протокол расширений"}, {"left": "/help", "right": "Slash-команда для справки"}]}
                ],
            },
            {
                "t": "Установка и настройка",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Установка Claude Code", "markdown": "## Установка\n\n### Требования:\n- Node.js 18+\n- npm или yarn\n- API-ключ Anthropic или подписка Claude\n\n### Установка:\n```bash\nnpm install -g @anthropic-ai/claude-code\n```\n\n### Первый запуск:\n```bash\ncd your-project\nclaude\n```\n\nClaude автоматически:\n1. Определит тип проекта\n2. Прочитает CLAUDE.md если есть\n3. Проанализирует структуру файлов\n4. Будет готов к работе\n\n### Аутентификация:\nПри первом запуске Claude попросит войти через браузер или ввести API-ключ."},
                    {"type": "terminal-sim", "prompt": "Установите Claude Code глобально через npm", "expectedCommand": "npm install -g @anthropic-ai/claude-code", "output": "added 1 package in 3.2s\n\n1 package is looking for funding\n  run `npm fund` for details", "hint": "Используйте npm install с флагом -g для глобальной установки"},
                    {"type": "terminal-sim", "prompt": "Запустите Claude Code в текущей директории", "expectedCommand": "claude", "output": "╭──────────────────────────────────────╮\n│  Claude Code v1.0.0                  │\n│  Type your request or /help          │\n╰──────────────────────────────────────╯\n\n>", "hint": "Просто введите имя команды"},
                    {"type": "quiz", "question": "Какая минимальная версия Node.js требуется для Claude Code?", "options": [{"id": "a", "text": "Node.js 18+", "correct": True}, {"id": "b", "text": "Node.js 12+", "correct": False}, {"id": "c", "text": "Node.js 20+", "correct": False}, {"id": "d", "text": "Node.js не нужен", "correct": False}]},
                    {"type": "drag-order", "items": ["Установить Node.js 18+", "Выполнить npm install -g @anthropic-ai/claude-code", "Перейти в директорию проекта", "Запустить claude", "Пройти аутентификацию"]},
                    {"type": "true-false", "statement": "Claude Code можно использовать без API-ключа или подписки.", "correct": False}
                ],
            },
            {
                "t": "Интерфейс и навигация",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Как работать с Claude Code", "markdown": "## Интерфейс Claude Code\n\n### Режимы ввода:\n- **Однострочный** — просто печатайте и нажмите Enter\n- **Многострочный** — Shift+Enter для новой строки\n- **Slash-команды** — начинаются с `/`\n\n### Основные slash-команды:\n- `/help` — справка\n- `/clear` — очистить контекст\n- `/compact` — сжать историю\n- `/cost` — показать потраченные токены\n- `/model` — сменить модель\n- `/permissions` — управление разрешениями\n\n### Горячие клавиши:\n- `Escape` — отменить текущее действие\n- `Ctrl+C` — прервать выполнение\n- `Tab` — автодополнение файлов\n- `↑/↓` — история команд"},
                    {"type": "terminal-sim", "prompt": "Посмотрите справку по доступным командам", "expectedCommand": "/help", "output": "Available commands:\n  /help       - Show this help\n  /clear      - Clear conversation\n  /compact    - Compact history\n  /cost       - Show token usage\n  /model      - Switch model\n  /permissions - Manage permissions", "hint": "Slash-команда для справки"},
                    {"type": "matching", "pairs": [{"left": "/clear", "right": "Очистить контекст диалога"}, {"left": "/compact", "right": "Сжать историю для экономии токенов"}, {"left": "/cost", "right": "Показать потраченные токены"}, {"left": "/model", "right": "Сменить модель Claude"}, {"left": "Escape", "right": "Отменить текущее действие"}]},
                    {"type": "multi-select", "question": "Какие из этих slash-команд существуют в Claude Code? (выберите все правильные)", "options": [{"id": "a", "text": "/help", "correct": True}, {"id": "b", "text": "/clear", "correct": True}, {"id": "c", "text": "/deploy", "correct": False}, {"id": "d", "text": "/compact", "correct": True}, {"id": "e", "text": "/build", "correct": False}, {"id": "f", "text": "/cost", "correct": True}]},
                    {"type": "quiz", "question": "Как отменить текущее действие Claude?", "options": [{"id": "a", "text": "Нажать Escape", "correct": True}, {"id": "b", "text": "Написать /stop", "correct": False}, {"id": "c", "text": "Закрыть терминал", "correct": False}, {"id": "d", "text": "Нажать Ctrl+Z", "correct": False}]}
                ],
            },
        ],
    },
    # ===== SECTION 2 =====
    {
        "title": "Работа с кодом",
        "pos": 1,
        "lessons": [
            {
                "t": "Написание кода с Claude",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Промпты для написания кода", "markdown": "## Как писать код с Claude Code\n\n### Принципы хороших промптов:\n1. **Будьте конкретны** — «Создай React-компонент Button с вариантами primary и secondary» вместо «Сделай кнопку»\n2. **Указывайте контекст** — «В файле src/components/» или «Используя существующую дизайн-систему»\n3. **Описывайте поведение** — «При клике вызывает onClick, при disabled — серый и некликабельный»\n\n### Примеры промптов:\n```\nСоздай функцию validateEmail которая проверяет email по RFC 5322\n```\n```\nДобавь тёмную тему в приложение, используя CSS переменные\n```\n```\nНапиши unit-тест для функции calculateTotal в src/utils/cart.ts\n```"},
                    {"type": "conversation-sim", "scenario": "Вы хотите создать React-компонент модального окна.", "messages": [{"role": "user", "text": "Нужен модальный компонент"}], "choices": [{"id": "a", "text": "Создай React-компонент Modal с props: open, onClose, title, children. Использовать портал, анимацию fade-in, закрытие по Escape и клику на оверлей.", "correct": True, "feedback": "Отличный промпт! Конкретный, с описанием поведения и всех нужных props."}, {"id": "b", "text": "Сделай модалку", "correct": False, "feedback": "Слишком размыто. Claude не знает какие props нужны, как анимировать, как закрывать."}, {"id": "c", "text": "Напиши весь код для модального окна на JavaScript без фреймворков", "correct": False, "feedback": "Вы в React-проекте, зачем без фреймворков? И нет деталей о поведении."}]},
                    {"type": "category-sort", "categories": ["Хороший промпт", "Плохой промпт"], "items": [{"text": "Создай функцию validateEmail по RFC 5322", "category": "Хороший промпт"}, {"text": "Сделай валидацию", "category": "Плохой промпт"}, {"text": "Добавь тесты для CartService, покрой edge cases: пустая корзина, отрицательное количество", "category": "Хороший промпт"}, {"text": "Напиши тесты", "category": "Плохой промпт"}, {"text": "В файле src/api/auth.ts добавь refresh token логику с ротацией", "category": "Хороший промпт"}, {"text": "Почини авторизацию", "category": "Плохой промпт"}]},
                    {"type": "snippet-order", "instruction": "Соберите хороший промпт для Claude Code", "fragments": ["Создай React-компонент", "SearchInput", "с debounce 300ms,", "иконкой поиска из lucide-react,", "и очисткой по кнопке X"]},
                    {"type": "true-false", "statement": "Claude Code может создавать новые файлы и редактировать существующие без вашего подтверждения.", "correct": False}
                ],
            },
            {
                "t": "Отладка и исправление ошибок",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Debugging с Claude Code", "markdown": "## Отладка с Claude Code\n\n### Как сообщить об ошибке:\n\n**Способ 1: Вставить ошибку**\n```\nУ меня ошибка: TypeError: Cannot read properties of undefined (reading 'map')\nв файле src/components/UserList.tsx:42\n```\n\n**Способ 2: Попросить запустить**\n```\nЗапусти npm test и исправь все ошибки\n```\n\n**Способ 3: Описать поведение**\n```\nКнопка Submit не работает на странице /register — при клике ничего не происходит\n```\n\n### Claude умеет:\n- Читать stack trace и находить root cause\n- Запускать тесты и чинить падающие\n- Анализировать логи\n- Проверять типы TypeScript\n- Искать похожие баги в кодовой базе"},
                    {"type": "conversation-sim", "scenario": "У вас падает тест в CI. Вы хотите попросить Claude разобраться.", "messages": [], "choices": [{"id": "a", "text": "Запусти npm test, найди падающие тесты, проанализируй причину и исправь", "correct": True, "feedback": "Claude сам запустит тесты, прочитает вывод, найдёт файлы и исправит."}, {"id": "b", "text": "Почему тесты падают?", "correct": False, "feedback": "Без запуска тестов Claude может только гадать. Лучше попросить его запустить и проанализировать."}, {"id": "c", "text": "Удали все падающие тесты", "correct": False, "feedback": "Это не решение проблемы, а её маскировка!"}]},
                    {"type": "terminal-sim", "prompt": "Попросите Claude запустить тесты и исправить ошибки", "expectedCommand": "запусти npm test и исправь все падающие тесты", "output": "I'll run the tests first to see what's failing.\n\n> npm test\n\nFAIL src/utils/__tests__/cart.test.ts\n  ● calculateTotal › should handle empty cart\n\nLet me fix this...\n\n[Edit] src/utils/cart.ts - Fixed edge case for empty array\n\n> npm test\n\nAll tests passed ✓", "hint": "Попросите Claude сделать два действия: запустить и исправить"},
                    {"type": "quiz", "question": "Какой способ сообщить Claude об ошибке самый эффективный?", "options": [{"id": "a", "text": "Вставить полный stack trace с указанием файла и строки", "correct": True}, {"id": "b", "text": "Сказать 'Что-то не работает'", "correct": False}, {"id": "c", "text": "Отправить скриншот ошибки", "correct": False}, {"id": "d", "text": "Описать ошибку на английском", "correct": False}]},
                    {"type": "highlight-text", "instruction": "Выделите элементы, которые полезно включить в сообщение об ошибке для Claude", "segments": [{"text": "TypeError: Cannot read properties of undefined", "correct": True}, {"text": "Я думаю это из-за React", "correct": False}, {"text": "в файле src/components/UserList.tsx:42", "correct": True}, {"text": "Помогите пожалуйста", "correct": False}, {"text": "при рендере списка пользователей из API", "correct": True}, {"text": "Может перезагрузить комп?", "correct": False}]}
                ],
            },
            {
                "t": "Рефакторинг кода",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Рефакторинг с Claude", "markdown": "## Рефакторинг с Claude Code\n\n### Типы рефакторинга:\n- **Извлечение** — вынести логику в отдельную функцию/компонент\n- **Переименование** — изменить имена для ясности\n- **Упрощение** — убрать дублирование, упростить условия\n- **Типизация** — добавить TypeScript типы\n- **Модернизация** — обновить до новых API (React hooks, etc.)\n\n### Примеры промптов:\n```\nРазбей файл src/utils/helpers.ts на отдельные модули по ответственности\n```\n```\nПеределай класс UserService в функциональный стиль с хуками\n```\n```\nДобавь строгую TypeScript типизацию в src/api/\n```"},
                    {"type": "quiz", "question": "Что лучше всего попросить при рефакторинге большого файла?", "options": [{"id": "a", "text": "Разбить файл на модули по ответственности", "correct": True}, {"id": "b", "text": "Переписать всё с нуля", "correct": False}, {"id": "c", "text": "Добавить комментарии", "correct": False}, {"id": "d", "text": "Сжать весь код в одну строку", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Извлечение", "right": "Вынести логику в отдельную функцию"}, {"left": "Переименование", "right": "Улучшить имена переменных и функций"}, {"left": "Типизация", "right": "Добавить TypeScript интерфейсы"}, {"left": "Модернизация", "right": "Обновить class-компоненты до hooks"}]},
                    {"type": "snippet-order", "instruction": "Соберите промпт для рефакторинга", "fragments": ["Разбей", "UserService.ts", "на отдельные модули:", "auth, profile, settings.", "Сохрани все существующие тесты рабочими."]},
                    {"type": "true-false", "statement": "При рефакторинге Claude автоматически обновляет все импорты в других файлах.", "correct": True}
                ],
            },
        ],
    },
    # ===== SECTION 3 =====
    {
        "title": "CLAUDE.md и конфигурация",
        "pos": 2,
        "lessons": [
            {
                "t": "Создание CLAUDE.md",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "CLAUDE.md — мозг проекта", "markdown": "## CLAUDE.md\n\nCLAUDE.md — файл в корне проекта, который Claude читает автоматически при каждом запуске.\n\n### Что включать:\n- **Стек проекта** — языки, фреймворки, версии\n- **Структура** — основные директории и их назначение\n- **Код-стайл** — правила именования, форматирования\n- **Команды** — как запускать, тестировать, деплоить\n- **Ограничения** — что НЕ делать\n\n### Пример:\n```markdown\n# Project: PathMind\n\n## Tech Stack\n- Frontend: React 19 + TypeScript + Tailwind v4\n- Backend: FastAPI + PostgreSQL\n- State: Zustand\n\n## Commands\n- `npm run dev` — start dev server\n- `npm run build` — production build\n- `cd backend && uvicorn app.main:app` — start API\n\n## Code Style\n- Use functional components with hooks\n- Prefer named exports\n- Russian comments for business logic\n```"},
                    {"type": "snippet-order", "instruction": "Соберите правильную структуру CLAUDE.md", "fragments": ["# Project: MyApp", "## Tech Stack", "- React 18 + TypeScript", "## Commands", "- npm run dev — start dev", "## Code Style", "- Use functional components"]},
                    {"type": "quiz", "question": "Когда Claude читает CLAUDE.md?", "options": [{"id": "a", "text": "Автоматически при каждом запуске в директории с этим файлом", "correct": True}, {"id": "b", "text": "Только когда вы явно попросите", "correct": False}, {"id": "c", "text": "Раз в неделю", "correct": False}, {"id": "d", "text": "Никогда — это просто документация", "correct": False}]},
                    {"type": "multi-select", "question": "Что полезно включить в CLAUDE.md? (выберите все правильные)", "options": [{"id": "a", "text": "Стек технологий проекта", "correct": True}, {"id": "b", "text": "Пароли и API-ключи", "correct": False}, {"id": "c", "text": "Команды для запуска и тестирования", "correct": True}, {"id": "d", "text": "Правила код-стайла", "correct": True}, {"id": "e", "text": "Личные заметки разработчика", "correct": False}, {"id": "f", "text": "Структура директорий", "correct": True}]},
                    {"type": "category-sort", "categories": ["Включить в CLAUDE.md", "НЕ включать"], "items": [{"text": "Стек: React + TypeScript", "category": "Включить в CLAUDE.md"}, {"text": "API_KEY=sk-ant-...", "category": "НЕ включать"}, {"text": "npm run dev — запуск", "category": "Включить в CLAUDE.md"}, {"text": "Пароль от базы данных", "category": "НЕ включать"}, {"text": "Используй named exports", "category": "Включить в CLAUDE.md"}, {"text": "TODO: починить баг #123", "category": "НЕ включать"}]},
                    {"type": "true-false", "statement": "CLAUDE.md должен содержать API-ключи для удобства Claude.", "correct": False}
                ],
            },
            {
                "t": "Настройки и разрешения",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Система разрешений", "markdown": "## Разрешения в Claude Code\n\n### Уровни разрешений:\n- **Чтение файлов** — всегда разрешено\n- **Редактирование файлов** — требует подтверждения (можно автоматизировать)\n- **Запуск команд** — требует подтверждения для небольших команд\n- **Опасные операции** — git push, rm -rf, всегда спрашивает\n\n### Настройка через /permissions:\n```\n/permissions\n```\n\nМожно разрешить автоматически:\n- `npm test` — запуск тестов без подтверждения\n- `Edit` — редактирование без подтверждения\n\n### settings.json:\nГлобальные настройки хранятся в `~/.claude/settings.json`\nПроектные — в `.claude/settings.json`"},
                    {"type": "terminal-sim", "prompt": "Откройте меню настройки разрешений", "expectedCommand": "/permissions", "output": "Permission settings:\n\n  File reads:     ✅ Always allowed\n  File edits:     ⚠️  Ask each time\n  Shell commands: ⚠️  Ask each time\n  Git operations: 🔒 Always ask\n\n  Type a tool name to toggle auto-allow.", "hint": "Используйте slash-команду для разрешений"},
                    {"type": "quiz", "question": "Какая операция ВСЕГДА требует подтверждения пользователя?", "options": [{"id": "a", "text": "git push и другие опасные операции", "correct": True}, {"id": "b", "text": "Чтение файлов", "correct": False}, {"id": "c", "text": "Поиск по файлам", "correct": False}, {"id": "d", "text": "Показ справки", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Чтение файлов", "right": "Всегда разрешено"}, {"left": "Редактирование", "right": "По умолчанию спрашивает"}, {"left": "Shell-команды", "right": "По умолчанию спрашивает"}, {"left": "git push", "right": "Всегда спрашивает"}]},
                    {"type": "true-false", "statement": "Claude Code может выполнить git push --force без подтверждения, если так настроить.", "correct": False}
                ],
            },
        ],
    },
    # ===== SECTION 4 =====
    {
        "title": "Git и командная работа",
        "pos": 3,
        "lessons": [
            {
                "t": "Коммиты и PR с Claude",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Git-операции", "markdown": "## Git с Claude Code\n\n### Автоматические коммиты:\n```\nЗакоммить изменения с осмысленным сообщением\n```\nClaude проанализирует diff, напишет commit message и создаст коммит.\n\n### Создание PR:\n```\nСоздай PR с описанием всех изменений\n```\nClaude создаст PR через `gh` CLI с заголовком и описанием.\n\n### Code Review:\n```\nСделай ревью PR #42\n```\nClaude прочитает diff, оставит комментарии.\n\n### Важно:\n- Claude НИКОГДА не делает force push\n- Всегда создаёт новый коммит (не amend)\n- Спрашивает перед push в remote"},
                    {"type": "terminal-sim", "prompt": "Попросите Claude создать коммит", "expectedCommand": "закоммить изменения", "output": "I'll analyze the changes and create a commit.\n\n> git diff --staged\n\nChanges:\n- Modified src/components/Button.tsx (added hover animation)\n- Created src/components/Modal.tsx (new component)\n\n> git commit -m \"feat: add hover animation to Button, create Modal component\"\n\n[main abc1234] feat: add hover animation to Button, create Modal component\n 2 files changed, 48 insertions(+)", "hint": "Попросите Claude закоммитить"},
                    {"type": "quiz", "question": "Что Claude делает перед созданием коммита?", "options": [{"id": "a", "text": "Анализирует diff и пишет осмысленное сообщение", "correct": True}, {"id": "b", "text": "Коммитит с пустым сообщением", "correct": False}, {"id": "c", "text": "Спрашивает у вас текст сообщения", "correct": False}, {"id": "d", "text": "Пушит сразу в main", "correct": False}]},
                    {"type": "multi-select", "question": "Какие git-операции Claude делает безопасно? (выберите все)", "options": [{"id": "a", "text": "Создание нового коммита", "correct": True}, {"id": "b", "text": "Создание PR через gh", "correct": True}, {"id": "c", "text": "Force push", "correct": False}, {"id": "d", "text": "Анализ diff", "correct": True}, {"id": "e", "text": "Amend последнего коммита без спроса", "correct": False}]},
                    {"type": "true-false", "statement": "Claude Code может сделать git push --force без предупреждения.", "correct": False},
                    {"type": "drag-order", "items": ["Внести изменения в код", "Попросить Claude закоммитить", "Claude анализирует diff", "Claude пишет commit message", "Claude создаёт коммит", "Попросить Claude создать PR"]}
                ],
            },
            {
                "t": "Работа с ветками",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Ветки и worktrees", "markdown": "## Ветки и Git Worktrees\n\n### Создание веток:\n```\nСоздай ветку feature/auth и начни работу над авторизацией\n```\n\n### Git Worktrees:\nClaude может создавать изолированные рабочие деревья для параллельной работы:\n```\nСоздай worktree для фичи payment в отдельной директории\n```\n\nWorktree позволяет:\n- Работать над несколькими фичами одновременно\n- Не терять незакоммиченные изменения\n- Запускать тесты в изоляции\n\n### Merge:\n```\nСмерджи ветку feature/auth в main, разреши конфликты\n```\nClaude разрешит конфликты интеллектуально, а не просто выбрав одну сторону."},
                    {"type": "quiz", "question": "Что такое Git Worktree?", "options": [{"id": "a", "text": "Изолированная копия репозитория для параллельной работы", "correct": True}, {"id": "b", "text": "Визуализация git-дерева", "correct": False}, {"id": "c", "text": "Способ сохранения стешей", "correct": False}, {"id": "d", "text": "Аналог git stash", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Worktree", "right": "Изолированная копия для параллельной работы"}, {"left": "Branch", "right": "Ветка разработки"}, {"left": "Merge", "right": "Объединение веток"}, {"left": "Conflict resolution", "right": "Claude разрешает конфликты интеллектуально"}]},
                    {"type": "true-false", "statement": "Claude всегда выбирает одну сторону при разрешении конфликтов, не пытаясь объединить изменения.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Git Worktree", "back": "Изолированная рабочая копия репозитория. Позволяет работать над разными ветками одновременно без stash."}, {"front": "Conflict Resolution", "back": "Claude анализирует оба варианта и создаёт объединённое решение, а не просто выбирает одну сторону."}]}
                ],
            },
        ],
    },
    # ===== SECTION 5 =====
    {
        "title": "MCP и расширения",
        "pos": 4,
        "lessons": [
            {
                "t": "Model Context Protocol",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Что такое MCP", "markdown": "## MCP — Model Context Protocol\n\nMCP позволяет подключать внешние инструменты к Claude Code.\n\n### Популярные MCP-серверы:\n- **GitHub** — работа с issues, PR, actions\n- **Figma** — чтение дизайнов и генерация кода\n- **PostgreSQL** — прямые запросы к базе\n- **Sentry** — анализ ошибок в продакшене\n- **Slack** — отправка сообщений\n\n### Настройка в settings.json:\n```json\n{\n  \"mcpServers\": {\n    \"github\": {\n      \"command\": \"npx\",\n      \"args\": [\"@anthropic-ai/mcp-github\"]\n    }\n  }\n}\n```\n\n### Использование:\nПосле подключения Claude автоматически получает доступ к инструментам MCP-сервера."},
                    {"type": "quiz", "question": "Что такое MCP в контексте Claude Code?", "options": [{"id": "a", "text": "Model Context Protocol — протокол подключения внешних инструментов", "correct": True}, {"id": "b", "text": "Main Control Panel — панель управления", "correct": False}, {"id": "c", "text": "Multi-Channel Processing — многоканальная обработка", "correct": False}, {"id": "d", "text": "Memory Cache Protocol — протокол кэширования", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "MCP GitHub", "right": "Работа с issues и PR"}, {"left": "MCP Figma", "right": "Чтение дизайнов"}, {"left": "MCP PostgreSQL", "right": "Запросы к базе данных"}, {"left": "MCP Sentry", "right": "Анализ ошибок продакшена"}]},
                    {"type": "multi-select", "question": "Какие MCP-серверы существуют? (выберите все правильные)", "options": [{"id": "a", "text": "GitHub", "correct": True}, {"id": "b", "text": "Figma", "correct": True}, {"id": "c", "text": "Instagram", "correct": False}, {"id": "d", "text": "PostgreSQL", "correct": True}, {"id": "e", "text": "TikTok", "correct": False}]},
                    {"type": "true-false", "statement": "MCP-серверы нужно устанавливать и настраивать вручную в settings.json.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "MCP", "back": "Model Context Protocol — открытый протокол от Anthropic для подключения внешних инструментов к AI-моделям"}, {"front": "MCP Server", "back": "Сервер, который предоставляет инструменты (tools) и ресурсы (resources) по протоколу MCP"}, {"front": "mcpServers в settings.json", "back": "Секция конфигурации Claude Code, где указываются подключённые MCP-серверы с командой запуска и аргументами"}]}
                ],
            },
        ],
    },
    # ===== SECTION 6 =====
    {
        "title": "Продвинутые техники",
        "pos": 5,
        "lessons": [
            {
                "t": "Эффективные промпты",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Prompt Engineering для Claude Code", "markdown": "## Продвинутые промпты\n\n### Техника «Шаг за шагом»:\n```\nСначала проанализируй текущую архитектуру auth-модуля,\nзатем предложи план рефакторинга,\nи только после моего одобрения начинай реализацию\n```\n\n### Техника «Ограничения»:\n```\nДобавь валидацию форм БЕЗ внешних библиотек,\nиспользуя только нативные API браузера\n```\n\n### Техника «Контекст файлов»:\n```\nПосмотри src/types/user.ts и обнови все компоненты,\nкоторые используют устаревший тип UserProfile\n```\n\n### Техника «Итерация»:\n```\nОтлично, но сделай кнопки крупнее и добавь hover-анимацию\n```"},
                    {"type": "conversation-sim", "scenario": "Вы хотите рефакторить auth-модуль, но сначала нужен план.", "messages": [], "choices": [{"id": "a", "text": "Проанализируй архитектуру auth-модуля в src/auth/. Составь план рефакторинга с указанием файлов и изменений. Не начинай реализацию без моего одобрения.", "correct": True, "feedback": "Идеально! Пошаговый подход с явным запретом на действия до одобрения."}, {"id": "b", "text": "Рефакторни auth", "correct": False, "feedback": "Слишком размыто. Claude начнёт менять код без плана — рискованно."}, {"id": "c", "text": "Покажи все файлы в src/auth/", "correct": False, "feedback": "Это только чтение файлов, а не планирование рефакторинга."}]},
                    {"type": "highlight-text", "instruction": "Выделите элементы хорошего промпта", "segments": [{"text": "Сначала проанализируй", "correct": True}, {"text": "потом сделай", "correct": False}, {"text": "текущую архитектуру auth-модуля,", "correct": True}, {"text": "затем предложи план,", "correct": True}, {"text": "сделай побыстрее", "correct": False}, {"text": "и только после моего одобрения начинай", "correct": True}]},
                    {"type": "category-sort", "categories": ["Эффективная техника", "Неэффективная техника"], "items": [{"text": "Пошаговый план с чекпоинтами", "category": "Эффективная техника"}, {"text": "Один огромный промпт на всё сразу", "category": "Неэффективная техника"}, {"text": "Указание ограничений и файлов", "category": "Эффективная техника"}, {"text": "Размытые формулировки типа 'сделай лучше'", "category": "Неэффективная техника"}, {"text": "Итерация: одобрение → следующий шаг", "category": "Эффективная техника"}, {"text": "Копирование огромного файла в промпт", "category": "Неэффективная техника"}]},
                    {"type": "snippet-order", "instruction": "Соберите пошаговый промпт", "fragments": ["Проанализируй", "все API-эндпоинты в src/api/,", "найди дублирование логики,", "составь план рефакторинга,", "дождись моего одобрения."]}
                ],
            },
            {
                "t": "Итоговый экзамен",
                "xp": 30,
                "steps": [
                    {"type": "quiz", "question": "Как установить Claude Code?", "options": [{"id": "a", "text": "npm install -g @anthropic-ai/claude-code", "correct": True}, {"id": "b", "text": "pip install claude-code", "correct": False}, {"id": "c", "text": "brew install claude", "correct": False}, {"id": "d", "text": "apt-get install claude-code", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "CLAUDE.md", "right": "Инструкции для Claude о проекте"}, {"left": "/compact", "right": "Сжатие истории диалога"}, {"left": "MCP", "right": "Подключение внешних инструментов"}, {"left": "Worktree", "right": "Изолированная копия репозитория"}, {"left": "/permissions", "right": "Управление разрешениями"}]},
                    {"type": "terminal-sim", "prompt": "Очистите контекст диалога", "expectedCommand": "/clear", "output": "Conversation cleared. Context reset.", "hint": "Используйте slash-команду для очистки"},
                    {"type": "multi-select", "question": "Что Claude Code делает автоматически? (выберите все)", "options": [{"id": "a", "text": "Читает CLAUDE.md при запуске", "correct": True}, {"id": "b", "text": "Анализирует структуру проекта", "correct": True}, {"id": "c", "text": "Пушит код в main", "correct": False}, {"id": "d", "text": "Спрашивает перед опасными операциями", "correct": True}, {"id": "e", "text": "Удаляет ненужные файлы", "correct": False}]},
                    {"type": "category-sort", "categories": ["Безопасно", "Требует подтверждения", "Запрещено"], "items": [{"text": "Чтение файлов", "category": "Безопасно"}, {"text": "Редактирование кода", "category": "Требует подтверждения"}, {"text": "git push --force", "category": "Запрещено"}, {"text": "Запуск npm test", "category": "Требует подтверждения"}, {"text": "Поиск по коду", "category": "Безопасно"}, {"text": "rm -rf /", "category": "Запрещено"}]},
                    {"type": "true-false", "statement": "CLAUDE.md должен храниться в корне проекта и коммититься в git.", "correct": True},
                    {"type": "type-answer", "question": "Какая slash-команда показывает потраченные токены?", "acceptedAnswers": ["/cost", "cost"]}
                ],
            },
        ],
    },
]


async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == COURSE_TITLE))
        if existing.scalar_one_or_none():
            print(f"Course '{COURSE_TITLE}' already exists — skipping.")
            return

        author_result = await db.execute(select(User).limit(1))
        author = author_result.scalar_one_or_none()
        if not author:
            print("No users found.")
            return

        course = Course(
            title=COURSE_TITLE,
            slug="claude-code-mastery-" + uuid.uuid4().hex[:4],
            description=COURSE_DESC,
            author_id=author.id,
            category="Other",
            difficulty="Intermediate",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()

        nodes, edges = [], []
        lesson_counter = 0
        total_lessons = 0

        for sec_data in SECTIONS:
            section = CourseSection(course_id=course.id, title=sec_data["title"], position=sec_data["pos"])
            db.add(section)
            await db.flush()

            for li, les_data in enumerate(sec_data["lessons"]):
                lesson = CourseLesson(
                    section_id=section.id, title=les_data["t"], position=li,
                    content_type="interactive", content_markdown="",
                    xp_reward=les_data["xp"], steps=les_data["steps"],
                )
                db.add(lesson)
                await db.flush()

                row = lesson_counter // 5
                col_idx = lesson_counter % 5
                x = SNAKE_X[col_idx] * CANVAS_W
                y = V_PAD + row * ROW_H
                nodes.append({"id": str(lesson.id), "x": x, "y": y})
                if lesson_counter > 0:
                    edges.append({"id": f"e-{lesson_counter}", "source": nodes[-2]["id"], "target": nodes[-1]["id"]})
                lesson_counter += 1
                total_lessons += 1

        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created course '{COURSE_TITLE}': {len(SECTIONS)} sections, {total_lessons} lessons.")
        print("Seed complete!")


if __name__ == "__main__":
    asyncio.run(main())
