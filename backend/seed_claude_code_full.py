"""Seed: Claude Code — полный курс по всем фичам. 10 sections, 40+ lessons."""
import asyncio, uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90
T = "Claude Code — Полный курс"

S = [
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 1: Начало работы
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Начало работы", "pos": 0, "lessons": [
    {"t": "Что такое Claude Code", "xp": 15, "steps": [
      {"type":"info","title":"Claude Code — AI-ассистент в терминале","markdown":"## Что такое Claude Code?\n\nClaude Code — это agentic CLI-инструмент от Anthropic. Он живёт в вашем терминале, понимает вашу кодовую базу и помогает писать код быстрее.\n\n### Ключевые возможности:\n- **Чтение и редактирование файлов** — Claude сам находит нужные файлы\n- **Запуск команд** — npm test, git commit, любые shell-команды\n- **Поиск по коду** — grep, glob, анализ зависимостей\n- **Git-операции** — коммиты, PR, ревью, конфликты\n- **MCP** — подключение внешних инструментов (GitHub, Figma, БД)\n- **Мультимодальность** — понимает скриншоты и изображения\n\n### Модели:\n- **Claude Opus 4** — самая мощная, для сложных задач\n- **Claude Sonnet 4** — баланс скорости и качества\n- **Claude Haiku** — быстрая, для простых задач"},
      {"type":"quiz","question":"Какой тип инструмента представляет собой Claude Code?","options":[{"id":"a","text":"Agentic CLI для разработки в терминале","correct":True},{"id":"b","text":"Веб-приложение для код-ревью","correct":False},{"id":"c","text":"IDE-плагин","correct":False},{"id":"d","text":"Компилятор","correct":False}]},
      {"type":"matching","pairs":[{"left":"Claude Opus 4","right":"Самая мощная модель для сложных задач"},{"left":"Claude Sonnet 4","right":"Баланс скорости и качества"},{"left":"Claude Haiku","right":"Быстрая для простых задач"},{"left":"MCP","right":"Подключение внешних инструментов"},{"left":"Agentic","right":"Сам выбирает инструменты и стратегию"}]},
      {"type":"flashcards","cards":[{"front":"Agentic","back":"Claude сам решает какие файлы читать, какие инструменты использовать, в каком порядке действовать. Ему не нужны пошаговые инструкции."},{"front":"CLI","back":"Command Line Interface — интерфейс командной строки. Claude Code работает в терминале, а не в браузере."},{"front":"MCP","back":"Model Context Protocol — протокол от Anthropic для подключения внешних инструментов и данных к Claude."},{"front":"Context Window","back":"Окно контекста — объём информации, которую Claude может помнить за один сеанс. До 200K токенов."}]},
      {"type":"true-false","statement":"Claude Code работает только в VS Code и не поддерживает обычный терминал.","correct":False}
    ]},
    {"t": "Установка и первый запуск", "xp": 20, "steps": [
      {"type":"info","title":"Установка Claude Code","markdown":"## Установка\n\n### Требования:\n- Node.js 18+ (рекомендуется 20+)\n- macOS, Linux или Windows (через WSL2)\n\n### Установка:\n```bash\nnpm install -g @anthropic-ai/claude-code\n```\n\n### Запуск:\n```bash\ncd ~/my-project\nclaude\n```\n\n### CLI-флаги запуска:\n- `claude` — интерактивный режим\n- `claude -c` — продолжить последнюю сессию\n- `claude -p \"prompt\"` — выполнить запрос без интерактива\n- `claude --model sonnet` — выбрать модель\n- `claude --verbose` — подробный вывод\n\n### Первый запуск:\n1. Claude предложит аутентификацию через браузер\n2. Автоматически определит тип проекта\n3. Прочитает CLAUDE.md если есть\n4. Готов к работе!"},
      {"type":"terminal-sim","prompt":"Установите Claude Code глобально","expectedCommand":"npm install -g @anthropic-ai/claude-code","output":"added 1 package in 4.1s","hint":"Используйте npm install с флагом -g"},
      {"type":"terminal-sim","prompt":"Запустите Claude Code в текущей директории","expectedCommand":"claude","output":"╭─────────────────────────────────╮\n│  Claude Code v1.2.0             │\n│  /help for commands             │\n╰─────────────────────────────────╯\n\n>","hint":"Просто введите claude"},
      {"type":"terminal-sim","prompt":"Продолжите последнюю сессию Claude Code","expectedCommand":"claude -c","output":"Resuming session: \"Fix auth module\" (2 hours ago)\n\n>","hint":"Флаг -c для continue"},
      {"type":"multi-select","question":"Какие CLI-флаги поддерживает Claude Code?","options":[{"id":"a","text":"-c для продолжения сессии","correct":True},{"id":"b","text":"-p для промпта без интерактива","correct":True},{"id":"c","text":"--model для выбора модели","correct":True},{"id":"d","text":"--deploy для деплоя","correct":False},{"id":"e","text":"--verbose для подробного вывода","correct":True}]},
      {"type":"drag-order","items":["Установить Node.js 18+","npm install -g @anthropic-ai/claude-code","Перейти в директорию проекта (cd)","Запустить claude","Аутентифицироваться через браузер","Начать работу"]}
    ]},
    {"t": "Интерфейс и ввод", "xp": 20, "steps": [
      {"type":"info","title":"Как вводить текст","markdown":"## Режимы ввода\n\n### Однострочный:\nПросто печатаете и Enter.\n\n### Многострочный:\n- **Shift+Enter** — новая строка\n- **Вставка** — многострочный текст автоматически\n\n### Горячие клавиши:\n| Клавиша | Действие |\n|---------|----------|\n| `Escape` | Отмена текущего действия |\n| `Ctrl+C` | Прерывание выполнения |\n| `Tab` | Автодополнение файлов |\n| `↑` / `↓` | История команд |\n| `Shift+Tab` | Переключение модели |\n\n### Специальные вводы:\n- Перетащите файл в терминал — путь вставится автоматически\n- Вставьте изображение — Claude проанализирует его\n- Вставьте URL — Claude прочитает содержимое"},
      {"type":"matching","pairs":[{"left":"Escape","right":"Отмена текущего действия"},{"left":"Ctrl+C","right":"Прерывание выполнения"},{"left":"Tab","right":"Автодополнение файлов"},{"left":"↑ / ↓","right":"История команд"},{"left":"Shift+Enter","right":"Новая строка"}]},
      {"type":"quiz","question":"Как переключить модель прямо во время ввода?","options":[{"id":"a","text":"Shift+Tab","correct":True},{"id":"b","text":"Ctrl+M","correct":False},{"id":"c","text":"Alt+S","correct":False},{"id":"d","text":"F5","correct":False}]},
      {"type":"true-false","statement":"Claude Code может анализировать изображения, вставленные в терминал.","correct":True},
      {"type":"category-sort","categories":["Поддерживается","Не поддерживается"],"items":[{"text":"Перетаскивание файлов в терминал","category":"Поддерживается"},{"text":"Вставка изображений","category":"Поддерживается"},{"text":"Голосовой ввод","category":"Не поддерживается"},{"text":"Автодополнение файлов (Tab)","category":"Поддерживается"},{"text":"Drag & Drop из браузера","category":"Не поддерживается"},{"text":"Вставка URL для анализа","category":"Поддерживается"}]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 2: Slash-команды
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Slash-команды", "pos": 1, "lessons": [
    {"t": "Основные команды", "xp": 25, "steps": [
      {"type":"info","title":"Все slash-команды","markdown":"## Slash-команды Claude Code\n\nВведите `/` чтобы увидеть все доступные команды.\n\n### Управление сессией:\n- `/clear` — очистить контекст диалога\n- `/compact` — сжать историю (экономит токены)\n- `/resume` — продолжить прошлую сессию\n- `/rename` — переименовать сессию\n\n### Настройки:\n- `/config` — открыть настройки\n- `/model` — сменить модель\n- `/permissions` — управление разрешениями\n- `/login` / `/logout` — аутентификация\n\n### Инструменты:\n- `/cost` — показать потраченные токены\n- `/doctor` — диагностика проблем\n- `/status` — информация о сессии\n- `/help` — справка\n\n### Кастомные:\n- `/commit` — создать коммит\n- Любые пользовательские slash-команды через skills"},
      {"type":"terminal-sim","prompt":"Очистите контекст диалога","expectedCommand":"/clear","output":"Conversation cleared.","hint":"Slash-команда для очистки"},
      {"type":"terminal-sim","prompt":"Посмотрите сколько токенов потрачено","expectedCommand":"/cost","output":"Session cost:\n  Input tokens:  45,231\n  Output tokens: 12,847\n  Total cost:    $0.42","hint":"Slash-команда для стоимости"},
      {"type":"terminal-sim","prompt":"Запустите диагностику Claude Code","expectedCommand":"/doctor","output":"Running diagnostics...\n\n✅ Node.js v20.11.0\n✅ Claude Code v1.2.0 (latest)\n✅ Authentication: valid\n✅ API connection: OK\n✅ MCP servers: 2 configured\n\nAll checks passed!","hint":"Slash-команда для диагностики"},
      {"type":"multi-select","question":"Какие slash-команды управляют сессией?","options":[{"id":"a","text":"/clear","correct":True},{"id":"b","text":"/compact","correct":True},{"id":"c","text":"/resume","correct":True},{"id":"d","text":"/deploy","correct":False},{"id":"e","text":"/rename","correct":True},{"id":"f","text":"/build","correct":False}]},
      {"type":"matching","pairs":[{"left":"/clear","right":"Очистить контекст"},{"left":"/compact","right":"Сжать историю для экономии"},{"left":"/cost","right":"Показать потраченные токены"},{"left":"/doctor","right":"Диагностика проблем"},{"left":"/model","right":"Сменить модель Claude"},{"left":"/permissions","right":"Управление разрешениями"}]}
    ]},
    {"t": "Compact и управление контекстом", "xp": 20, "steps": [
      {"type":"info","title":"Управление контекстом","markdown":"## Контекст и /compact\n\n### Зачем нужен /compact?\nУ Claude ограниченное окно контекста. Когда диалог долгий, старые сообщения автоматически сжимаются. `/compact` делает это явно.\n\n### Использование:\n```\n/compact\n```\nСожмёт всю историю в краткое резюме.\n\n```\n/compact сфокусируйся на auth-модуле\n```\nСожмёт с акцентом на указанной теме.\n\n### Когда использовать:\n- Диалог стал длинным (50+ сообщений)\n- Переключаетесь на другую задачу\n- Claude начинает «забывать» ранние инструкции\n\n### Auto-compact:\nClaude автоматически сжимает контекст когда приближается к лимиту. Но ручной /compact даёт лучший результат."},
      {"type":"terminal-sim","prompt":"Сожмите историю с фокусом на auth","expectedCommand":"/compact сфокусируйся на auth-модуле","output":"Compacting conversation...\n\nPrevious context (47 messages) summarized:\n- Working on auth module refactoring\n- JWT tokens implemented\n- Refresh token rotation pending\n\nContext reduced from 45K to 3K tokens.","hint":"Используйте /compact с описанием фокуса"},
      {"type":"quiz","question":"Когда лучше всего использовать /compact?","options":[{"id":"a","text":"Когда диалог стал длинным и Claude забывает контекст","correct":True},{"id":"b","text":"После каждого сообщения","correct":False},{"id":"c","text":"Только при ошибках","correct":False},{"id":"d","text":"Никогда — это вредно","correct":False}]},
      {"type":"true-false","statement":"Claude автоматически сжимает контекст когда приближается к лимиту окна.","correct":True},
      {"type":"fill-blank","text":"Команда ___ сжимает историю диалога. Можно указать ___ на конкретной теме для лучшего результата.","answers":["/compact","фокус"]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 3: CLAUDE.md и настройки
  # ═══════════════════════════════════════════════════════════════════
  {"title": "CLAUDE.md и конфигурация", "pos": 2, "lessons": [
    {"t": "CLAUDE.md — инструкции для Claude", "xp": 25, "steps": [
      {"type":"info","title":"CLAUDE.md","markdown":"## CLAUDE.md — мозг проекта\n\nClaude автоматически читает CLAUDE.md при запуске.\n\n### Уровни:\n- **Корень проекта** `./CLAUDE.md` — проектные инструкции\n- **Домашняя директория** `~/.claude/CLAUDE.md` — глобальные инструкции\n- **Поддиректории** `src/CLAUDE.md` — инструкции для конкретной папки\n\n### Что включать:\n```markdown\n# Project: MyApp\n\n## Tech Stack\n- React 19 + TypeScript 5.5\n- Tailwind CSS v4\n- FastAPI backend\n\n## Commands\n- npm run dev — dev server\n- npm test — run tests\n- npm run build — production build\n\n## Architecture\n- src/components/ — React components\n- src/services/ — API layer\n- src/store/ — Zustand stores\n\n## Code Style\n- Functional components with hooks\n- Named exports (not default)\n- Comments in Russian\n\n## Rules\n- NEVER modify .env files\n- Always run tests before committing\n- Use conventional commits\n```"},
      {"type":"snippet-order","instruction":"Соберите структуру CLAUDE.md","fragments":["# Project: MyApp","## Tech Stack","- React 19 + TypeScript","## Commands","- npm run dev — dev server","## Code Style","- Named exports","## Rules","- NEVER modify .env files"]},
      {"type":"category-sort","categories":["Включить в CLAUDE.md","НЕ включать"],"items":[{"text":"Стек технологий","category":"Включить в CLAUDE.md"},{"text":"API-ключи и пароли","category":"НЕ включать"},{"text":"Команды запуска/тестирования","category":"Включить в CLAUDE.md"},{"text":"Правила код-стайла","category":"Включить в CLAUDE.md"},{"text":"Номера кредитных карт","category":"НЕ включать"},{"text":"Архитектура проекта","category":"Включить в CLAUDE.md"},{"text":"Личные заметки","category":"НЕ включать"},{"text":"Запреты (что НЕ делать)","category":"Включить в CLAUDE.md"}]},
      {"type":"quiz","question":"Где Claude ищет CLAUDE.md?","options":[{"id":"a","text":"В корне проекта, в поддиректориях и в ~/.claude/","correct":True},{"id":"b","text":"Только в корне проекта","correct":False},{"id":"c","text":"Только если попросить","correct":False},{"id":"d","text":"В /etc/claude/","correct":False}]},
      {"type":"multi-select","question":"Какие секции полезны в CLAUDE.md?","options":[{"id":"a","text":"Tech Stack","correct":True},{"id":"b","text":"Commands","correct":True},{"id":"c","text":"Passwords","correct":False},{"id":"d","text":"Code Style","correct":True},{"id":"e","text":"Architecture","correct":True},{"id":"f","text":"Personal diary","correct":False}]},
      {"type":"true-false","statement":"CLAUDE.md в поддиректории переопределяет корневой для файлов в той папке.","correct":True}
    ]},
    {"t": "Settings и конфигурация", "xp": 20, "steps": [
      {"type":"info","title":"Система настроек","markdown":"## Settings.json\n\n### Уровни настроек:\n1. **Глобальные** — `~/.claude/settings.json`\n2. **Проектные** — `.claude/settings.json` (коммитится в git)\n3. **Локальные** — `.claude/settings.local.json` (НЕ коммитится)\n\n### Основные настройки:\n```json\n{\n  \"permissions\": {\n    \"allow\": [\"Bash(npm test)\", \"Bash(npm run lint)\", \"Edit\"],\n    \"deny\": [\"Bash(rm -rf)\"]\n  },\n  \"env\": {\n    \"ANTHROPIC_MODEL\": \"claude-sonnet-4-20250514\"\n  },\n  \"hooks\": {\n    \"postToolUse\": [{\n      \"matcher\": \"Edit\",\n      \"command\": \"npm run lint --fix ${file}\"\n    }]\n  }\n}\n```\n\n### Приоритет:\nLocal > Project > Global"},
      {"type":"matching","pairs":[{"left":"~/.claude/settings.json","right":"Глобальные настройки"},{"left":".claude/settings.json","right":"Проектные (в git)"},{"left":".claude/settings.local.json","right":"Локальные (не в git)"},{"left":"permissions.allow","right":"Авторазрешения"},{"left":"hooks","right":"Автоматические действия"}]},
      {"type":"quiz","question":"Какой файл настроек НЕ коммитится в git?","options":[{"id":"a","text":"settings.local.json","correct":True},{"id":"b","text":"settings.json","correct":False},{"id":"c","text":"CLAUDE.md","correct":False},{"id":"d","text":"Все коммитятся","correct":False}]},
      {"type":"drag-order","items":["Global (~/.claude/settings.json)","Project (.claude/settings.json)","Local (.claude/settings.local.json)"]},
      {"type":"true-false","statement":"Локальные настройки имеют высший приоритет над проектными и глобальными.","correct":True}
    ]},
    {"t": "Система разрешений", "xp": 25, "steps": [
      {"type":"info","title":"Permissions","markdown":"## Система разрешений\n\n### Уровни:\n- **Чтение** — всегда разрешено\n- **Редактирование** — по умолчанию спрашивает\n- **Shell-команды** — по умолчанию спрашивает\n- **Опасные операции** — ВСЕГДА спрашивает\n\n### Настройка auto-allow:\n```json\n{\n  \"permissions\": {\n    \"allow\": [\n      \"Edit\",\n      \"Bash(npm test)\",\n      \"Bash(npm run *)\",\n      \"Bash(git status)\",\n      \"Bash(git diff)\"\n    ],\n    \"deny\": [\n      \"Bash(rm -rf *)\",\n      \"Bash(git push --force)\"\n    ]\n  }\n}\n```\n\n### Через /permissions:\nМожно настроить интерактивно прямо в сессии.\n\n### Важно:\n- `git push --force` **никогда** не авторазрешается\n- `rm -rf /` **никогда** не авторазрешается\n- Удаление файлов всегда спрашивает подтверждение"},
      {"type":"terminal-sim","prompt":"Откройте настройки разрешений","expectedCommand":"/permissions","output":"Permission settings:\n\n  Allow list:\n    ✅ Edit\n    ✅ Bash(npm test)\n    ✅ Bash(npm run *)\n\n  Deny list:\n    🚫 Bash(rm -rf *)\n    🚫 Bash(git push --force)\n\n  Type a pattern to add/remove.","hint":"/permissions"},
      {"type":"category-sort","categories":["Можно авторазрешить","Нельзя авторразрешить"],"items":[{"text":"Edit (редактирование файлов)","category":"Можно авторазрешить"},{"text":"Bash(npm test)","category":"Можно авторазрешить"},{"text":"git push --force","category":"Нельзя авторразрешить"},{"text":"Bash(git status)","category":"Можно авторазрешить"},{"text":"rm -rf /","category":"Нельзя авторразрешить"},{"text":"Bash(npm run lint)","category":"Можно авторазрешить"}]},
      {"type":"quiz","question":"Какую операцию НЕВОЗМОЖНО авторазрешить?","options":[{"id":"a","text":"git push --force","correct":True},{"id":"b","text":"npm test","correct":False},{"id":"c","text":"Редактирование файлов","correct":False},{"id":"d","text":"git status","correct":False}]},
      {"type":"true-false","statement":"Можно разрешить шаблон Bash(npm run *) для всех npm-скриптов.","correct":True}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 4: Работа с кодом
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Работа с кодом", "pos": 3, "lessons": [
    {"t": "Написание кода", "xp": 25, "steps": [
      {"type":"info","title":"Промпты для кода","markdown":"## Написание кода с Claude\n\n### Принципы промптов:\n1. **Конкретность** — указывайте файл, функцию, поведение\n2. **Контекст** — ссылайтесь на существующие файлы\n3. **Ограничения** — что НЕ делать\n4. **Примеры** — покажите желаемый результат\n\n### Хорошие промпты:\n```\nСоздай компонент SearchInput в src/components/ui/\nс debounce 300ms, иконкой поиска из lucide-react,\nпо стилю как существующий Input.tsx\n```\n\n### Claude умеет:\n- Создавать новые файлы\n- Редактировать существующие (через Edit tool)\n- Искать код по паттернам (Grep, Glob)\n- Понимать зависимости между файлами\n- Обновлять импорты автоматически"},
      {"type":"conversation-sim","scenario":"Вы хотите создать API-клиент для работы с пользователями.","messages":[],"choices":[{"id":"a","text":"Создай сервис UserService в src/services/userApi.ts. Методы: getAll, getById, create, update, delete. Используй существующий apiFetch из src/services/api.ts. Типы возьми из src/types/user.ts.","correct":True,"feedback":"Отлично! Конкретный файл, методы, ссылки на существующий код."},{"id":"b","text":"Сделай API для юзеров","correct":False,"feedback":"Слишком размыто — где создать? какие методы? какие типы?"},{"id":"c","text":"Напиши fetch-запросы","correct":False,"feedback":"Нет структуры — Claude не знает куда положить код и какие endpoints использовать."}]},
      {"type":"highlight-text","instruction":"Выделите элементы хорошего промпта","segments":[{"text":"Создай компонент SearchInput","correct":True},{"text":"сделай что-нибудь","correct":False},{"text":"в src/components/ui/","correct":True},{"text":"где-нибудь","correct":False},{"text":"с debounce 300ms,","correct":True},{"text":"по стилю как существующий Input.tsx","correct":True}]},
      {"type":"snippet-order","instruction":"Соберите хороший промпт","fragments":["Создай хук useDebounce","в src/hooks/useDebounce.ts,","с типизацией generic <T>,","задержка по умолчанию 300ms,","добавь unit-тест."]},
      {"type":"true-false","statement":"Claude Code может обновлять импорты в других файлах при рефакторинге.","correct":True}
    ]},
    {"t": "Отладка и тестирование", "xp": 25, "steps": [
      {"type":"info","title":"Debug и тесты","markdown":"## Отладка\n\n### 3 способа сообщить об ошибке:\n\n**1. Вставить stack trace:**\n```\nОшибка: TypeError: Cannot read property 'map' of undefined\nat UserList (src/components/UserList.tsx:42)\n```\n\n**2. Попросить запустить:**\n```\nЗапусти npm test и исправь все падающие тесты\n```\n\n**3. Описать поведение:**\n```\nКнопка «Отправить» на /register не реагирует на клик\n```\n\n## Тестирование\n\n### Claude может:\n- Написать тесты для существующего кода\n- Запустить тесты и починить падающие\n- Добавить edge cases\n- Сделать TDD — сначала тест, потом реализация\n\n### Промпт:\n```\nНапиши тесты для CartService: пустая корзина,\nдублирование товаров, отрицательное количество,\nмаксимальная сумма. Используй Vitest.\n```"},
      {"type":"terminal-sim","prompt":"Попросите Claude запустить тесты и исправить ошибки","expectedCommand":"запусти npm test и исправь падающие тесты","output":"Running tests...\n\n> npm test\n\n❌ FAIL src/utils/cart.test.ts (3 failures)\n\nAnalyzing failures...\nFixed: empty cart edge case\nFixed: negative quantity validation\nFixed: overflow check\n\n✅ All 24 tests passing","hint":"Попросите запустить И исправить"},
      {"type":"category-sort","categories":["Хороший способ","Плохой способ"],"items":[{"text":"Вставить полный stack trace","category":"Хороший способ"},{"text":"Написать 'не работает'","category":"Плохой способ"},{"text":"Указать файл и строку ошибки","category":"Хороший способ"},{"text":"Отправить скриншот без контекста","category":"Плохой способ"},{"text":"Описать ожидаемое vs фактическое поведение","category":"Хороший способ"},{"text":"Сказать 'почини всё'","category":"Плохой способ"}]},
      {"type":"quiz","question":"Какой подход к тестированию поддерживает Claude?","options":[{"id":"a","text":"Все: написание, запуск, исправление, TDD","correct":True},{"id":"b","text":"Только написание тестов","correct":False},{"id":"c","text":"Только запуск тестов","correct":False},{"id":"d","text":"Claude не работает с тестами","correct":False}]},
      {"type":"true-false","statement":"Claude может использовать TDD-подход: сначала написать тест, потом реализацию.","correct":True}
    ]},
    {"t": "Рефакторинг", "xp": 20, "steps": [
      {"type":"info","title":"Рефакторинг с Claude","markdown":"## Рефакторинг\n\n### Типы рефакторинга:\n- **Декомпозиция** — разбить большой файл на модули\n- **Типизация** — добавить TypeScript типы\n- **Модернизация** — class → hooks, callbacks → async/await\n- **Оптимизация** — убрать дублирование, упростить логику\n\n### Лучшие практики:\n1. Попросите **план** перед рефакторингом\n2. Указывайте **что сохранить** (API, тесты)\n3. Делайте **маленькими шагами** с проверкой\n4. Используйте **Plan Mode** для сложных рефакторингов\n\n### Plan Mode:\n```\nshift+tab → Plan mode\n\nПроанализируй auth-модуль и составь план рефакторинга.\nНе начинай реализацию без моего одобрения.\n```"},
      {"type":"conversation-sim","scenario":"Файл utils.ts вырос до 800 строк и стал неуправляемым.","messages":[],"choices":[{"id":"a","text":"Проанализируй src/utils.ts, сгруппируй функции по ответственности, предложи план разбиения на отдельные модули. Покажи план — не начинай без одобрения.","correct":True,"feedback":"Правильно! Сначала план, потом действие."},{"id":"b","text":"Перепиши utils.ts","correct":False,"feedback":"Нет плана — Claude может разбить не так, как вы хотите."},{"id":"c","text":"Удали utils.ts и начни заново","correct":False,"feedback":"Потеряете рабочий код! Рефакторинг ≠ переписывание."}]},
      {"type":"matching","pairs":[{"left":"Декомпозиция","right":"Разбить файл на модули"},{"left":"Типизация","right":"Добавить TypeScript интерфейсы"},{"left":"Модернизация","right":"Class → hooks, callbacks → async"},{"left":"Plan Mode","right":"Сначала план, потом реализация"}]},
      {"type":"drag-order","items":["Попросить Claude проанализировать файл","Получить план рефакторинга","Одобрить или скорректировать план","Claude выполняет рефакторинг","Проверить что тесты проходят","Закоммитить результат"]},
      {"type":"true-false","statement":"При рефакторинге лучше попросить Claude сделать всё за один раз, без промежуточных проверок.","correct":False}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 5: Git-интеграция
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Git и командная работа", "pos": 4, "lessons": [
    {"t": "Коммиты и PR", "xp": 25, "steps": [
      {"type":"info","title":"Git с Claude","markdown":"## Git-операции\n\n### Коммиты:\n```\nЗакоммить все изменения\n```\nClaude:\n1. Запустит `git diff`\n2. Проанализирует изменения\n3. Напишет осмысленный commit message\n4. Создаст коммит\n\n### Pull Requests:\n```\nСоздай PR с описанием\n```\nClaude через `gh` CLI создаст PR с:\n- Заголовком (до 70 символов)\n- Описанием изменений\n- Test plan\n\n### Правила безопасности Claude:\n- ❌ Никогда не делает `git push --force`\n- ❌ Никогда не amend без запроса\n- ❌ Никогда не пушит без подтверждения\n- ✅ Всегда создаёт НОВЫЙ коммит\n- ✅ Спрашивает перед push"},
      {"type":"terminal-sim","prompt":"Попросите Claude закоммитить изменения","expectedCommand":"закоммить изменения","output":"Analyzing changes...\n\n> git diff --staged\n\n  Modified: src/components/Button.tsx\n  Created: src/hooks/useDebounce.ts\n\n> git commit -m \"feat: add useDebounce hook, update Button hover animation\"\n\n[main a1b2c3d] feat: add useDebounce hook, update Button hover animation\n 2 files changed, 34 insertions(+), 2 deletions(-)","hint":"Попросите закоммитить"},
      {"type":"multi-select","question":"Какие git-операции Claude НИКОГДА не делает без спроса?","options":[{"id":"a","text":"git push (любой)","correct":True},{"id":"b","text":"git push --force","correct":True},{"id":"c","text":"git diff","correct":False},{"id":"d","text":"git amend","correct":True},{"id":"e","text":"git status","correct":False}]},
      {"type":"quiz","question":"Что Claude делает при создании коммита?","options":[{"id":"a","text":"Анализирует diff и пишет осмысленное сообщение","correct":True},{"id":"b","text":"Коммитит с сообщением 'update'","correct":False},{"id":"c","text":"Спрашивает у вас текст сообщения","correct":False},{"id":"d","text":"Amend-ит последний коммит","correct":False}]},
      {"type":"true-false","statement":"Claude Code использует conventional commits формат по умолчанию.","correct":True}
    ]},
    {"t": "Worktrees и ветки", "xp": 20, "steps": [
      {"type":"info","title":"Git Worktrees","markdown":"## Git Worktrees\n\nWorktree — изолированная копия репозитория для параллельной работы.\n\n### Зачем:\n- Работа над фичей без потери текущих изменений\n- Параллельный запуск тестов\n- Изоляция экспериментов\n\n### Как Claude использует:\nClaude может создать worktree для подзадачи, выполнить работу в изоляции, и вернуть результат.\n\n### Sub-agents:\nClaude может запускать sub-агентов в отдельных worktrees для параллельной работы:\n```\nЗапусти параллельно:\n1. Рефакторинг auth-модуля\n2. Написание тестов для cart-модуля\n```\n\nКаждый sub-agent работает в своём worktree и не мешает другим."},
      {"type":"quiz","question":"Что такое Git Worktree?","options":[{"id":"a","text":"Изолированная копия репозитория для параллельной работы","correct":True},{"id":"b","text":"Визуализация git-дерева","correct":False},{"id":"c","text":"Аналог git branch","correct":False},{"id":"d","text":"Инструмент для merge","correct":False}]},
      {"type":"matching","pairs":[{"left":"Worktree","right":"Изолированная копия для параллельной работы"},{"left":"Sub-agent","right":"Дочерний агент для подзадачи"},{"left":"Parallel execution","right":"Несколько задач одновременно"},{"left":"Conflict resolution","right":"Claude объединяет изменения интеллектуально"}]},
      {"type":"true-false","statement":"Sub-agents в Claude Code могут работать параллельно в разных worktrees.","correct":True},
      {"type":"flashcards","cards":[{"front":"Git Worktree","back":"Позволяет иметь несколько рабочих копий одного репозитория. Каждая на своей ветке."},{"front":"Sub-agent","back":"Дочерний процесс Claude, выполняющий подзадачу автономно. Может работать в изоляции."},{"front":"Parallel dispatch","back":"Запуск нескольких sub-agents одновременно для независимых задач."}]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 6: MCP — Model Context Protocol
  # ═══════════════════════════════════════════════════════════════════
  {"title": "MCP и расширения", "pos": 5, "lessons": [
    {"t": "Что такое MCP", "xp": 25, "steps": [
      {"type":"info","title":"Model Context Protocol","markdown":"## MCP — расширения Claude Code\n\nMCP (Model Context Protocol) — открытый протокол от Anthropic для подключения внешних инструментов.\n\n### Что даёт MCP:\n- **Tools** — инструменты, которые Claude может вызывать\n- **Resources** — данные, которые Claude может читать\n- **Prompts** — шаблоны промптов\n\n### Популярные серверы:\n- **GitHub MCP** — issues, PRs, actions, repos\n- **Figma MCP** — чтение дизайнов, генерация кода\n- **PostgreSQL MCP** — SQL-запросы к базе\n- **Sentry MCP** — анализ ошибок продакшена\n- **Slack MCP** — чтение/отправка сообщений\n- **Linear MCP** — задачи и проекты\n- **Firebase MCP** — управление проектами Firebase\n\n### Настройка в settings.json:\n```json\n{\n  \"mcpServers\": {\n    \"github\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@anthropic-ai/mcp-server-github\"],\n      \"env\": { \"GITHUB_TOKEN\": \"ghp_...\" }\n    }\n  }\n}\n```"},
      {"type":"matching","pairs":[{"left":"GitHub MCP","right":"Issues, PRs, Actions"},{"left":"Figma MCP","right":"Чтение дизайнов"},{"left":"PostgreSQL MCP","right":"SQL-запросы к базе"},{"left":"Sentry MCP","right":"Ошибки продакшена"},{"left":"Slack MCP","right":"Сообщения команды"},{"left":"Linear MCP","right":"Задачи и проекты"}]},
      {"type":"quiz","question":"Что такое MCP?","options":[{"id":"a","text":"Model Context Protocol — протокол подключения внешних инструментов","correct":True},{"id":"b","text":"Master Control Panel","correct":False},{"id":"c","text":"Multi-Channel Processing","correct":False},{"id":"d","text":"Micro Component Platform","correct":False}]},
      {"type":"multi-select","question":"Что MCP-сервер может предоставить Claude?","options":[{"id":"a","text":"Tools (инструменты)","correct":True},{"id":"b","text":"Resources (данные)","correct":True},{"id":"c","text":"Prompts (шаблоны)","correct":True},{"id":"d","text":"GPU для обучения","correct":False}]},
      {"type":"true-false","statement":"MCP-серверы настраиваются в файле settings.json.","correct":True},
      {"type":"category-sort","categories":["MCP-сервер существует","Не существует"],"items":[{"text":"GitHub","category":"MCP-сервер существует"},{"text":"Figma","category":"MCP-сервер существует"},{"text":"TikTok","category":"Не существует"},{"text":"PostgreSQL","category":"MCP-сервер существует"},{"text":"Instagram","category":"Не существует"},{"text":"Sentry","category":"MCP-сервер существует"},{"text":"Firebase","category":"MCP-сервер существует"}]}
    ]},
    {"t": "Настройка MCP-серверов", "xp": 20, "steps": [
      {"type":"info","title":"Подключение MCP","markdown":"## Как подключить MCP-сервер\n\n### Шаг 1: Найти сервер\nОфициальные серверы: `@anthropic-ai/mcp-server-*`\nСообщество: npm, GitHub\n\n### Шаг 2: Добавить в settings.json\n```json\n{\n  \"mcpServers\": {\n    \"имя-сервера\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@пакет/имя\"],\n      \"env\": {\n        \"API_KEY\": \"ваш-ключ\"\n      }\n    }\n  }\n}\n```\n\n### Шаг 3: Перезапустить Claude\nMCP-серверы загружаются при старте.\n\n### Шаг 4: Использовать\nClaude автоматически видит инструменты MCP:\n```\nПокажи открытые issues в репозитории myapp\n```"},
      {"type":"drag-order","items":["Найти нужный MCP-сервер","Добавить конфигурацию в settings.json","Указать env-переменные (токены, ключи)","Перезапустить Claude Code","Claude автоматически подключит инструменты","Использовать в промптах"]},
      {"type":"quiz","question":"Когда загружаются MCP-серверы?","options":[{"id":"a","text":"При старте Claude Code","correct":True},{"id":"b","text":"При каждом промпте","correct":False},{"id":"c","text":"По запросу /mcp","correct":False},{"id":"d","text":"Автоматически из npm","correct":False}]},
      {"type":"fill-blank","text":"MCP-серверы настраиваются в секции ___ файла ___. Для каждого сервера указывается ___ запуска и ___ окружения.","answers":["mcpServers","settings.json","command","env"]},
      {"type":"true-false","statement":"После добавления MCP-сервера нужно перезапустить Claude Code.","correct":True}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 7: Hooks и автоматизация
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Hooks и автоматизация", "pos": 6, "lessons": [
    {"t": "Система Hooks", "xp": 25, "steps": [
      {"type":"info","title":"Hooks — автоматические действия","markdown":"## Hooks в Claude Code\n\nHooks — это shell-команды, которые выполняются автоматически при определённых событиях.\n\n### Типы событий:\n- **preToolUse** — перед использованием инструмента\n- **postToolUse** — после использования инструмента\n- **notification** — при уведомлениях Claude\n- **stop** — когда Claude завершает ответ\n\n### Примеры:\n\n**Линтер после редактирования:**\n```json\n{\n  \"hooks\": {\n    \"postToolUse\": [{\n      \"matcher\": \"Edit\",\n      \"command\": \"npx eslint --fix ${file}\"\n    }]\n  }\n}\n```\n\n**Форматирование после сохранения:**\n```json\n{\n  \"hooks\": {\n    \"postToolUse\": [{\n      \"matcher\": \"Write\",\n      \"command\": \"npx prettier --write ${file}\"\n    }]\n  }\n}\n```"},
      {"type":"matching","pairs":[{"left":"preToolUse","right":"Перед использованием инструмента"},{"left":"postToolUse","right":"После использования инструмента"},{"left":"notification","right":"При уведомлениях"},{"left":"stop","right":"Когда Claude завершает ответ"},{"left":"matcher","right":"Фильтр: какой инструмент отслеживать"}]},
      {"type":"quiz","question":"Какой hook запускает линтер после каждого редактирования файла?","options":[{"id":"a","text":"postToolUse с matcher: Edit","correct":True},{"id":"b","text":"preToolUse с matcher: Lint","correct":False},{"id":"c","text":"notification с matcher: Edit","correct":False},{"id":"d","text":"Hooks не поддерживают линтинг","correct":False}]},
      {"type":"true-false","statement":"Hooks могут блокировать действие Claude, если вернут ненулевой код выхода.","correct":True},
      {"type":"flashcards","cards":[{"front":"Hook","back":"Shell-команда, автоматически выполняемая при событии Claude Code. Настраивается в settings.json."},{"front":"matcher","back":"Фильтр в hook — определяет к какому инструменту применяется hook (Edit, Write, Bash и т.д.)"},{"front":"preToolUse","back":"Hook перед действием. Может заблокировать действие (exit code != 0)."},{"front":"postToolUse","back":"Hook после действия. Полезен для линтинга, форматирования, уведомлений."}]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 8: IDE интеграции
  # ═══════════════════════════════════════════════════════════════════
  {"title": "IDE-интеграции", "pos": 7, "lessons": [
    {"t": "VS Code и JetBrains", "xp": 20, "steps": [
      {"type":"info","title":"Claude Code в IDE","markdown":"## IDE-интеграции\n\n### VS Code:\nClaude Code встраивается в VS Code как терминал и как расширение:\n- Открыть через Command Palette: `Claude: Open`\n- Inline-подсказки при редактировании\n- Статусная строка с информацией о сессии\n\n### JetBrains (IntelliJ, WebStorm, PyCharm):\n- Поддержка через встроенный терминал\n- Claude читает проект через стандартные инструменты\n\n### Terminal-first:\nClaude Code изначально разработан для терминала. IDE-интеграции — это обёртки над CLI.\n\n### Преимущества CLI:\n- Работает везде: локально, SSH, CI/CD\n- Не зависит от конкретной IDE\n- Полный контроль через настройки\n- Быстрее запускается"},
      {"type":"quiz","question":"Для какой IDE есть нативное расширение Claude Code?","options":[{"id":"a","text":"VS Code","correct":True},{"id":"b","text":"Sublime Text","correct":False},{"id":"c","text":"Vim","correct":False},{"id":"d","text":"Atom","correct":False}]},
      {"type":"true-false","statement":"Claude Code работает только в VS Code и не поддерживает обычный терминал.","correct":False},
      {"type":"category-sort","categories":["Преимущество CLI","Преимущество IDE"],"items":[{"text":"Работает через SSH","category":"Преимущество CLI"},{"text":"Визуальный diff","category":"Преимущество IDE"},{"text":"Работает в CI/CD","category":"Преимущество CLI"},{"text":"Inline-подсказки","category":"Преимущество IDE"},{"text":"Не зависит от IDE","category":"Преимущество CLI"},{"text":"Интеграция с редактором","category":"Преимущество IDE"}]},
      {"type":"matching","pairs":[{"left":"VS Code","right":"Нативное расширение + терминал"},{"left":"JetBrains","right":"Через встроенный терминал"},{"left":"SSH","right":"CLI работает удалённо"},{"left":"CI/CD","right":"Headless-режим для автоматизации"}]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 9: Продвинутые техники
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Продвинутые техники", "pos": 8, "lessons": [
    {"t": "Plan Mode и Extended Thinking", "xp": 25, "steps": [
      {"type":"info","title":"Режимы работы Claude","markdown":"## Plan Mode\n\nPlan Mode — режим, в котором Claude ТОЛЬКО планирует, не выполняя действий.\n\n### Как активировать:\n- `Shift+Tab` → переключить на Plan mode\n- Или написать: «Составь план, не начинай реализацию»\n\n### Когда использовать:\n- Сложный рефакторинг\n- Новая фича с неясной архитектурой\n- Когда хотите одобрить подход перед началом\n\n## Extended Thinking\n\nClaude может «думать вслух» — показывать ход рассуждений перед ответом.\n\n### Модели:\n- **Claude Opus** — extended thinking включён по умолчанию\n- **Claude Sonnet** — можно включить через настройки\n\n## Headless/CI Mode\n\n```bash\nclaude -p \"Исправь все eslint-ошибки\" --allowedTools Edit,Bash\n```\n\nЗапуск без интерактива для CI/CD пайплайнов."},
      {"type":"quiz","question":"Как активировать Plan Mode?","options":[{"id":"a","text":"Shift+Tab или попросить составить план","correct":True},{"id":"b","text":"Ctrl+P","correct":False},{"id":"c","text":"/plan","correct":False},{"id":"d","text":"Plan Mode не существует","correct":False}]},
      {"type":"matching","pairs":[{"left":"Plan Mode","right":"Только планирование, без действий"},{"left":"Extended Thinking","right":"Claude показывает ход рассуждений"},{"left":"Headless Mode","right":"Без интерактива, для CI/CD"},{"left":"claude -p","right":"Одноразовый промпт без сессии"}]},
      {"type":"terminal-sim","prompt":"Запустите Claude в headless-режиме для исправления линт-ошибок","expectedCommand":"claude -p \"исправь все eslint ошибки\" --allowedTools Edit,Bash","output":"Processing...\n\nFound 12 eslint errors across 5 files.\n\nFixed:\n  src/utils/helpers.ts: 4 errors\n  src/components/Card.tsx: 3 errors\n  src/hooks/useAuth.ts: 5 errors\n\nAll eslint errors resolved.","hint":"Используйте claude -p с --allowedTools"},
      {"type":"true-false","statement":"Headless-режим позволяет запускать Claude Code в CI/CD пайплайнах.","correct":True},
      {"type":"flashcards","cards":[{"front":"Plan Mode","back":"Режим планирования: Claude анализирует задачу, составляет план, но НЕ выполняет действия до одобрения."},{"front":"Extended Thinking","back":"Claude показывает процесс размышления перед ответом. Помогает понять логику решений."},{"front":"Headless Mode","back":"claude -p 'prompt' — выполняет задачу без интерактива. Для CI/CD, скриптов, автоматизации."},{"front":"--allowedTools","back":"Флаг для headless-режима: какие инструменты разрешить без подтверждения (Edit, Bash, etc.)"}]}
    ]},
    {"t": "Память и сессии", "xp": 20, "steps": [
      {"type":"info","title":"Memory и Sessions","markdown":"## Система памяти\n\nClaude Code может сохранять информацию между сессиями через файловую систему памяти.\n\n### Память хранится в:\n`~/.claude/projects/<project>/memory/`\n\n### Типы памяти:\n- **user** — информация о вас (роль, предпочтения)\n- **feedback** — ваши коррекции поведения Claude\n- **project** — контекст проекта (дедлайны, решения)\n- **reference** — ссылки на внешние ресурсы\n\n### Сессии:\n- `/resume` — вернуться к прошлой сессии\n- `claude -c` — продолжить последнюю\n- `/rename` — переименовать текущую\n\n### MEMORY.md:\nИндексный файл, связывающий все файлы памяти.\nClaude автоматически его читает."},
      {"type":"matching","pairs":[{"left":"user memory","right":"Роль, предпочтения, экспертиза"},{"left":"feedback memory","right":"Коррекции: «не делай так, делай этак»"},{"left":"project memory","right":"Контекст: дедлайны, решения, инциденты"},{"left":"reference memory","right":"Ссылки на внешние системы"},{"left":"MEMORY.md","right":"Индекс всех файлов памяти"}]},
      {"type":"quiz","question":"Где Claude Code хранит память?","options":[{"id":"a","text":"В файловой системе: ~/.claude/projects/<project>/memory/","correct":True},{"id":"b","text":"В облаке Anthropic","correct":False},{"id":"c","text":"В localStorage браузера","correct":False},{"id":"d","text":"Claude не имеет памяти","correct":False}]},
      {"type":"multi-select","question":"Какие типы памяти поддерживает Claude Code?","options":[{"id":"a","text":"user — о пользователе","correct":True},{"id":"b","text":"feedback — коррекции поведения","correct":True},{"id":"c","text":"project — контекст проекта","correct":True},{"id":"d","text":"reference — внешние ссылки","correct":True},{"id":"e","text":"cache — кэш ответов","correct":False}]},
      {"type":"true-false","statement":"Claude может запоминать ваши предпочтения между сессиями.","correct":True}
    ]},
    {"t": "Sub-agents и параллельная работа", "xp": 25, "steps": [
      {"type":"info","title":"Sub-agents","markdown":"## Параллельная работа с Sub-agents\n\nClaude Code может запускать sub-агентов — дочерние процессы для параллельного выполнения задач.\n\n### Как это работает:\n1. Claude получает задачу с несколькими независимыми подзадачами\n2. Запускает sub-agent для каждой\n3. Каждый работает в изоляции (опционально — в worktree)\n4. Результаты собираются и объединяются\n\n### Пример:\n```\nПараллельно:\n1. Добавь тесты для UserService\n2. Рефакторни CartService \n3. Обнови документацию API\n```\n\n### Типы sub-agents:\n- **Explore** — быстрый поиск по кодовой базе\n- **Plan** — планирование архитектуры\n- **General** — выполнение любых задач\n\n### Background agents:\nМожно запустить агента в фоне и получить результат позже."},
      {"type":"quiz","question":"Когда Claude запускает sub-agents?","options":[{"id":"a","text":"Когда задача содержит несколько независимых подзадач","correct":True},{"id":"b","text":"Всегда при каждом запросе","correct":False},{"id":"c","text":"Только при ошибках","correct":False},{"id":"d","text":"Sub-agents не существуют","correct":False}]},
      {"type":"matching","pairs":[{"left":"Explore agent","right":"Быстрый поиск по коду"},{"left":"Plan agent","right":"Планирование архитектуры"},{"left":"General agent","right":"Любые задачи"},{"left":"Background agent","right":"Работа в фоне"},{"left":"Worktree isolation","right":"Каждый агент в своей копии репо"}]},
      {"type":"true-false","statement":"Sub-agents могут работать параллельно, каждый в своём git worktree.","correct":True},
      {"type":"category-sort","categories":["Подходит для параллельной работы","Нужна последовательность"],"items":[{"text":"Тесты + документация + линтинг","category":"Подходит для параллельной работы"},{"text":"Рефакторинг файла A → обновление импортов в B","category":"Нужна последовательность"},{"text":"3 независимых компонента","category":"Подходит для параллельной работы"},{"text":"Миграция БД → обновление моделей → обновление API","category":"Нужна последовательность"}]}
    ]},
  ]},
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 10: Итоговый экзамен
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Итоговый экзамен", "pos": 9, "lessons": [
    {"t": "Финальный тест", "xp": 30, "steps": [
      {"type":"quiz","question":"Как установить Claude Code?","options":[{"id":"a","text":"npm install -g @anthropic-ai/claude-code","correct":True},{"id":"b","text":"pip install claude","correct":False},{"id":"c","text":"brew install claude-code","correct":False},{"id":"d","text":"apt install claude","correct":False}]},
      {"type":"matching","pairs":[{"left":"CLAUDE.md","right":"Инструкции для Claude о проекте"},{"left":"/compact","right":"Сжатие контекста"},{"left":"MCP","right":"Подключение внешних инструментов"},{"left":"Hooks","right":"Автоматические действия при событиях"},{"left":"Sub-agents","right":"Параллельные дочерние процессы"},{"left":"Plan Mode","right":"Режим планирования без действий"}]},
      {"type":"multi-select","question":"Что Claude Code умеет делать?","options":[{"id":"a","text":"Читать и редактировать файлы","correct":True},{"id":"b","text":"Запускать shell-команды","correct":True},{"id":"c","text":"Создавать git-коммиты и PR","correct":True},{"id":"d","text":"Деплоить в продакшен автоматически","correct":False},{"id":"e","text":"Анализировать изображения","correct":True},{"id":"f","text":"Подключать внешние API через MCP","correct":True}]},
      {"type":"terminal-sim","prompt":"Запустите Claude Code и продолжите последнюю сессию","expectedCommand":"claude -c","output":"Resuming session: \"Full redesign\" (1 hour ago)\n>","hint":"Флаг -c"},
      {"type":"category-sort","categories":["Безопасно","Требует подтверждения","Невозможно"],"items":[{"text":"Чтение файлов","category":"Безопасно"},{"text":"Редактирование файлов","category":"Требует подтверждения"},{"text":"git push --force","category":"Невозможно"},{"text":"npm test","category":"Требует подтверждения"},{"text":"Grep по коду","category":"Безопасно"},{"text":"rm -rf /","category":"Невозможно"},{"text":"git diff","category":"Безопасно"}]},
      {"type":"highlight-text","instruction":"Выделите элементы хорошей конфигурации CLAUDE.md","segments":[{"text":"## Tech Stack","correct":True},{"text":"password: admin123","correct":False},{"text":"## Commands","correct":True},{"text":"- npm run dev","correct":True},{"text":"SECRET_KEY=abc","correct":False},{"text":"## Code Style","correct":True}]},
      {"type":"true-false","statement":"Claude Code может работать в CI/CD через headless-режим с флагом -p.","correct":True},
      {"type":"type-answer","question":"Какая slash-команда показывает потраченные токены?","acceptedAnswers":["/cost","cost"]}
    ]},
  ]},
]

async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping."); return

        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author: print("No users."); return

        course = Course(title=T, slug="claude-code-full-"+uuid.uuid4().hex[:4],
            description="Полный курс по всем возможностям Claude Code: slash-команды, CLAUDE.md, настройки, разрешения, hooks, MCP, git, IDE, sub-agents, plan mode, headless и многое другое. 40+ уроков с интерактивными заданиями.",
            author_id=author.id, category="Other", difficulty="Intermediate",
            price=0, currency="USD", status="published")
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
                x, y = SNAKE_X[c]*CANVAS_W, V_PAD+r*ROW_H
                nodes.append({"id":str(les.id),"x":x,"y":y})
                if lc > 0: edges.append({"id":f"e-{lc}","source":nodes[-2]["id"],"target":nodes[-1]["id"]})
                lc += 1; tl += 1
        course.roadmap_nodes = nodes; course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")

if __name__ == "__main__":
    asyncio.run(main())
