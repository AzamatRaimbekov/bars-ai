"""Seed: Vibe Coding Mastery — полный курс для новичков с видео, инструментами и Tower Defense."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSE_TITLE = "Vibe Coding Mastery"
COURSE_DESC = (
    "Полный курс по vibe coding — создавай приложения с помощью AI, "
    "не написав ни строчки кода вручную. Cursor, Claude Code, Bolt, v0, Lovable "
    "и другие инструменты. От первого промпта до деплоя."
)

SECTIONS = [
    # ===== SECTION 1: Что такое Vibe Coding =====
    {
        "title": "Что такое Vibe Coding",
        "pos": 0,
        "lessons": [
            {
                "t": "Введение в Vibe Coding",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Vibe Coding — новая эра разработки", "markdown": "## Что такое Vibe Coding?\n\nТермин **vibe coding** был популяризирован **Андреем Карпатым** (бывший директор AI в Tesla) в феврале 2025 года.\n\n> «Есть новый вид программирования, который я называю vibe coding. Ты полностью отдаёшься вайбу, принимаешь экспоненциальность и забываешь, что код вообще существует.»\n\n### Суть:\n- Ты **описываешь** что хочешь на человеческом языке\n- **AI генерирует** код за тебя\n- Ты **ревьюишь**, корректируешь, итерируешь\n- Результат — рабочее приложение\n\n### Когда это работает:\n- Прототипы и MVP\n- CRUD-приложения\n- Лендинги и сайты\n- Внутренние инструменты\n- Автоматизации\n\n### Когда НЕ работает:\n- Сложная архитектура с высокими нагрузками\n- Системы с критической безопасностью\n- Без понимания основ программирования\n\n### Главное правило:\n**Ты — архитектор, AI — строитель.** Чем лучше ты понимаешь что строишь, тем лучше результат."},
                    {"type": "video", "title": "Andrej Karpathy о Vibe Coding (оригинал)", "url": "https://www.youtube.com/watch?v=oGSYn0e6mJo"},
                    {"type": "quiz", "question": "Кто популяризировал термин 'vibe coding'?", "options": [{"id": "a", "text": "Андрей Карпатый (Andrej Karpathy)", "correct": True}, {"id": "b", "text": "Сэм Альтман", "correct": False}, {"id": "c", "text": "Илон Маск", "correct": False}, {"id": "d", "text": "Марк Цукерберг", "correct": False}]},
                    {"type": "true-false", "statement": "Vibe coding означает, что AI полностью заменяет программиста и понимание кода не нужно.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "Vibe Coding", "right": "Создание приложений через AI по описанию"}, {"left": "Промпт", "right": "Текстовое описание задачи для AI"}, {"left": "Итерация", "right": "Цикл: промпт → ревью → коррекция"}, {"left": "MVP", "right": "Минимально жизнеспособный продукт"}]},
                ],
            },
            {
                "t": "Workflow: от идеи до деплоя",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "5 шагов Vibe Coding", "markdown": "## Vibe Coding Workflow\n\n### Шаг 1: Описание (Describe)\nОпиши приложение или фичу простым языком. Чем конкретнее — тем лучше.\n\n**Плохо:** *«Сделай мне приложение»*\n**Хорошо:** *«Создай React-приложение для списка задач с возможностью добавлять, удалять и отмечать задачи как выполненные. Используй Tailwind CSS, тёмную тему, localStorage для хранения.»*\n\n### Шаг 2: Генерация (Generate)\nЗапусти AI-инструмент (Cursor, Claude Code, Bolt и т.д.) и дай ему промпт.\n\n### Шаг 3: Ревью (Review)\nПосмотри что сгенерировалось. Проверь:\n- Работает ли приложение?\n- Нет ли ошибок в консоли?\n- Выглядит ли UI как задумано?\n- Нет ли проблем с безопасностью?\n\n### Шаг 4: Итерация (Iterate)\nПопроси AI исправить баги, добавить фичи, улучшить UI.\n\n### Шаг 5: Деплой (Deploy)\nОпубликуй приложение: Vercel, Netlify, или встроенный деплой инструмента."},
                    {"type": "drag-order", "items": ["Описать идею и требования", "Сгенерировать код через AI", "Проревьюить результат", "Итерировать и улучшать", "Задеплоить приложение"]},
                    {"type": "quiz", "question": "Какой промпт лучше для vibe coding?", "options": [{"id": "a", "text": "Сделай приложение", "correct": False}, {"id": "b", "text": "Создай React-приложение для списка задач с Tailwind CSS, тёмной темой и localStorage", "correct": True}, {"id": "c", "text": "Напиши код", "correct": False}, {"id": "d", "text": "Мне нужен сайт", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Describe", "back": "Опиши что хочешь создать — конкретно, с деталями"}, {"front": "Generate", "back": "Запусти AI и дай промпт"}, {"front": "Review", "back": "Проверь результат: UI, ошибки, безопасность"}, {"front": "Iterate", "back": "Попроси AI исправить и улучшить"}, {"front": "Deploy", "back": "Опубликуй приложение в интернете"}]},
                ],
            },
        ],
    },
    # ===== SECTION 2: Инструменты =====
    {
        "title": "Инструменты Vibe Coding",
        "pos": 1,
        "lessons": [
            {
                "t": "Cursor — AI-редактор кода",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Cursor — главный инструмент vibe coder'а", "markdown": "## Cursor\n\n**Сайт:** [cursor.sh](https://cursor.sh)\n**Цена:** Бесплатный тариф / Pro $20/мес\n**Что это:** VS Code-форк со встроенным AI\n\n### Ключевые фичи:\n\n#### 1. Chat (Cmd+L)\nОткрой чат и опиши задачу. Cursor видит весь твой проект и может редактировать несколько файлов.\n\n#### 2. Inline Edit (Cmd+K)\nВыдели код → нажми Cmd+K → опиши изменение → AI перепишет выделенный фрагмент.\n\n#### 3. Autocomplete (Tab)\nAI предсказывает следующие строки кода по контексту.\n\n#### 4. Composer (Cmd+I)\nМультифайловый режим — Cursor создаёт и редактирует несколько файлов одновременно.\n\n#### 5. .cursorrules\nФайл в корне проекта с инструкциями для AI:\n```\nYou are an expert React/TypeScript developer.\nAlways use functional components with hooks.\nUse Tailwind CSS for styling.\nWrite tests with Vitest.\n```\n\n### Установка:\n1. Скачай с [cursor.sh](https://cursor.sh)\n2. Установи\n3. Войди / привяжи API ключ\n4. Открой проект → начни vibe coding!"},
                    {"type": "video", "title": "Cursor AI Tutorial для начинающих", "url": "https://www.youtube.com/watch?v=gqUQbjsYZLQ"},
                    {"type": "video", "title": "Cursor Tips & Tricks", "url": "https://www.youtube.com/watch?v=1CC88QGQiEA"},
                    {"type": "matching", "pairs": [{"left": "Cmd+L", "right": "Открыть AI Chat"}, {"left": "Cmd+K", "right": "Inline Edit (редакция кода)"}, {"left": "Tab", "right": "Автодополнение AI"}, {"left": "Cmd+I", "right": "Composer (мультифайловый режим)"}, {"left": ".cursorrules", "right": "Файл с инструкциями для AI"}]},
                    {"type": "quiz", "question": "Какой файл задаёт правила для AI в Cursor?", "options": [{"id": "a", "text": ".cursorrules", "correct": True}, {"id": "b", "text": ".env", "correct": False}, {"id": "c", "text": "cursor.config.js", "correct": False}, {"id": "d", "text": "settings.json", "correct": False}]},
                    {"type": "true-false", "statement": "Cursor — это отдельный редактор, не связанный с VS Code.", "correct": False},
                ],
            },
            {
                "t": "Claude Code — AI в терминале",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Claude Code — агентный кодинг", "markdown": "## Claude Code\n\n**Установка:** `npm install -g @anthropic-ai/claude-code`\n**Цена:** По подписке Claude / API\n**Что это:** CLI-инструмент от Anthropic для агентной разработки\n\n### Как работает:\n1. Открой терминал в папке проекта\n2. Введи `claude`\n3. Опиши задачу — Claude сам:\n   - Прочитает нужные файлы\n   - Напишет код\n   - Запустит тесты\n   - Сделает коммит\n\n### Ключевые команды:\n- `/help` — справка\n- `/clear` — очистить контекст\n- `/compact` — сжать историю\n- `/cost` — потраченные токены\n\n### CLAUDE.md\nФайл в корне проекта — инструкции для Claude:\n```markdown\n# Project: My App\n- Stack: React + TypeScript + Tailwind\n- Testing: Vitest\n- Style: functional components, no classes\n- Always run tests before committing\n```\n\n### Когда использовать:\n- Рефакторинг больших кодовых баз\n- Баг-фиксы с контекстом всего проекта\n- Создание новых фич от начала до конца\n- Git операции (коммиты, PR)"},
                    {"type": "video", "title": "Claude Code — полный обзор", "url": "https://www.youtube.com/watch?v=eHOGajMHhRE"},
                    {"type": "matching", "pairs": [{"left": "claude", "right": "Запустить Claude Code в терминале"}, {"left": "CLAUDE.md", "right": "Файл с инструкциями проекта"}, {"left": "/compact", "right": "Сжать историю диалога"}, {"left": "/cost", "right": "Показать потраченные токены"}]},
                    {"type": "quiz", "question": "Как установить Claude Code?", "options": [{"id": "a", "text": "npm install -g @anthropic-ai/claude-code", "correct": True}, {"id": "b", "text": "brew install claude", "correct": False}, {"id": "c", "text": "pip install claude-code", "correct": False}, {"id": "d", "text": "Скачать с сайта", "correct": False}]},
                    {"type": "type-answer", "question": "Какой файл в корне проекта содержит инструкции для Claude Code?", "acceptedAnswers": ["CLAUDE.md", "claude.md"]},
                ],
            },
            {
                "t": "Bolt, v0 и Lovable — генераторы приложений",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Браузерные AI-билдеры", "markdown": "## Bolt.new\n**Сайт:** [bolt.new](https://bolt.new)\n\nПолноценный билдер приложений прямо в браузере:\n- Пишешь промпт → получаешь работающее приложение\n- Редактируешь через чат\n- Деплоишь одной кнопкой\n- Работает на WebContainers (StackBlitz)\n\n## v0 by Vercel\n**Сайт:** [v0.dev](https://v0.dev)\n\nГенератор UI-компонентов:\n- Описываешь компонент → получаешь React + Tailwind + shadcn/ui\n- Идеален для лендингов, дашбордов, форм\n- Код можно скопировать в свой проект через `npx shadcn@latest add`\n\n## Lovable\n**Сайт:** [lovable.dev](https://lovable.dev)\n\nФуллстек генератор (бывший GPT Engineer):\n- Описываешь приложение → получаешь фронтенд + бэкенд + БД\n- Встроенный Supabase для базы данных\n- Встроенная авторизация\n- Хостинг из коробки\n\n## Replit Agent\n**Сайт:** [replit.com](https://replit.com)\n\n- Описываешь приложение → агент строит всё\n- Встроенный хостинг и домен\n- Хорошо для быстрых прототипов"},
                    {"type": "video", "title": "Bolt.new — создаём приложение за 5 минут", "url": "https://www.youtube.com/watch?v=S9lcREBRPTk"},
                    {"type": "video", "title": "v0.dev — генерация UI компонентов", "url": "https://www.youtube.com/watch?v=bNY_qlmPUqE"},
                    {"type": "category-sort", "categories": ["IDE с AI", "Браузерный билдер", "UI генератор"], "items": [{"text": "Cursor", "category": "IDE с AI"}, {"text": "Bolt.new", "category": "Браузерный билдер"}, {"text": "v0.dev", "category": "UI генератор"}, {"text": "Windsurf", "category": "IDE с AI"}, {"text": "Lovable", "category": "Браузерный билдер"}, {"text": "Replit Agent", "category": "Браузерный билдер"}]},
                    {"type": "matching", "pairs": [{"left": "bolt.new", "right": "Фуллстек приложение в браузере"}, {"left": "v0.dev", "right": "UI-компоненты React + Tailwind"}, {"left": "lovable.dev", "right": "Приложение + Supabase + хостинг"}, {"left": "replit.com", "right": "Облачная IDE + Agent + деплой"}]},
                    {"type": "quiz", "question": "Какой инструмент лучше всего подходит для генерации отдельных UI-компонентов?", "options": [{"id": "a", "text": "v0.dev", "correct": True}, {"id": "b", "text": "Bolt.new", "correct": False}, {"id": "c", "text": "Claude Code", "correct": False}, {"id": "d", "text": "Replit", "correct": False}]},
                ],
            },
            {
                "t": "Как выбрать инструмент",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Гид по выбору инструмента", "markdown": "## Какой инструмент выбрать?\n\n### По задаче:\n\n| Задача | Лучший инструмент |\n|---|---|\n| Полноценная разработка в IDE | **Cursor** или **Windsurf** |\n| Терминальный агентный кодинг | **Claude Code** |\n| Быстрый прототип в браузере | **Bolt.new** или **Lovable** |\n| Красивые UI компоненты | **v0.dev** |\n| Прототип + мгновенный деплой | **Replit Agent** |\n| Автодополнение в VS Code | **GitHub Copilot** |\n\n### По опыту:\n\n| Уровень | Рекомендация |\n|---|---|\n| Полный новичок | **Bolt.new** или **Lovable** — нужен только браузер |\n| Базовые знания | **Cursor** — учишься и кодишь одновременно |\n| Опытный разработчик | **Claude Code** — максимальный контроль |\n\n### Совет:\nНачни с **Bolt.new** для первого проекта (не нужно ничего устанавливать), потом переходи на **Cursor** для серьёзной работы."},
                    {"type": "quiz", "question": "Что лучше выбрать полному новичку?", "options": [{"id": "a", "text": "Bolt.new или Lovable — нужен только браузер", "correct": True}, {"id": "b", "text": "Claude Code — самый мощный", "correct": False}, {"id": "c", "text": "Devin — полностью автономный", "correct": False}, {"id": "d", "text": "GitHub Copilot — самый популярный", "correct": False}]},
                    {"type": "true-false", "statement": "Для vibe coding обязательно нужно устанавливать IDE на компьютер.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Bolt.new", "back": "Фуллстек приложение прямо в браузере, деплой одной кнопкой"}, {"front": "Cursor", "back": "AI-редактор (VS Code форк) для полноценной разработки"}, {"front": "Claude Code", "back": "CLI-агент от Anthropic, максимальный контроль"}, {"front": "v0.dev", "back": "Генератор UI-компонентов от Vercel"}, {"front": "Lovable", "back": "Фуллстек генератор с Supabase и хостингом"}]},
                ],
            },
        ],
    },
    # ===== SECTION 3: Промпт-инженеринг =====
    {
        "title": "Промпт-инженеринг для кода",
        "pos": 2,
        "lessons": [
            {
                "t": "Анатомия идеального промпта",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Как писать промпты для AI-кодинга", "markdown": "## Структура промпта\n\nХороший промпт для vibe coding содержит 5 элементов:\n\n### 1. Контекст (Context)\n*Кто ты и что за проект*\n> Я создаю SaaS-приложение для управления задачами.\n\n### 2. Задача (Task)\n*Что конкретно нужно сделать*\n> Создай страницу регистрации.\n\n### 3. Стек (Stack)\n*Какие технологии использовать*\n> React, TypeScript, Tailwind CSS, Supabase Auth.\n\n### 4. Детали (Details)\n*Конкретные требования к UI и поведению*\n> Форма с полями: email, пароль, подтверждение пароля. Валидация на клиенте. При успешной регистрации — редирект на /dashboard. Тёмная тема.\n\n### 5. Ограничения (Constraints)\n*Чего НЕ делать*\n> Не используй библиотеки для форм (react-hook-form). Не добавляй социальную авторизацию."},
                    {"type": "drag-order", "items": ["Контекст: что за проект", "Задача: что конкретно сделать", "Стек: какие технологии", "Детали: требования к UI и поведению", "Ограничения: чего НЕ делать"]},
                    {"type": "quiz", "question": "Какой элемент промпта описывает чего НЕ нужно делать?", "options": [{"id": "a", "text": "Ограничения (Constraints)", "correct": True}, {"id": "b", "text": "Контекст (Context)", "correct": False}, {"id": "c", "text": "Детали (Details)", "correct": False}, {"id": "d", "text": "Стек (Stack)", "correct": False}]},
                    {"type": "fill-blank", "text": "Хороший промпт содержит: контекст, задачу, ___, детали и ограничения.", "answers": ["стек"]},
                    {"type": "true-false", "statement": "Чем более расплывчатый промпт, тем лучше результат от AI.", "correct": False},
                ],
            },
            {
                "t": "Rules-файлы: .cursorrules и CLAUDE.md",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Настройка AI под свой проект", "markdown": "## Rules-файлы\n\nRules-файлы — это инструкции для AI, которые применяются ко ВСЕМУ проекту автоматически.\n\n### .cursorrules (для Cursor)\nФайл в корне проекта:\n```\nYou are an expert in React, TypeScript, and Tailwind CSS.\n\nCode Style:\n- Use functional components with hooks\n- Use 'const' for component declarations\n- Use TypeScript strict mode\n- Use Tailwind for all styling, no CSS files\n\nNaming:\n- Components: PascalCase (UserProfile.tsx)\n- Utilities: camelCase (formatDate.ts)\n- Constants: UPPER_SNAKE_CASE\n\nProject Structure:\n- src/components/ - React components\n- src/hooks/ - Custom hooks\n- src/lib/ - Utilities\n- src/types/ - TypeScript types\n```\n\n### CLAUDE.md (для Claude Code)\n```markdown\n# Project: TaskManager\n\n## Stack\n- Frontend: React 19 + TypeScript + Tailwind\n- Backend: FastAPI + PostgreSQL\n- Testing: Vitest (frontend), Pytest (backend)\n\n## Rules\n- Always run tests before committing\n- Use conventional commits\n- No any types in TypeScript\n```\n\n### Зачем это нужно?\n- AI следует стилю проекта **в каждом запросе**\n- Не нужно повторять одно и то же\n- Результат более консистентный"},
                    {"type": "quiz", "question": "Какой файл настраивает AI в Cursor для всего проекта?", "options": [{"id": "a", "text": ".cursorrules", "correct": True}, {"id": "b", "text": "CLAUDE.md", "correct": False}, {"id": "c", "text": ".env", "correct": False}, {"id": "d", "text": "ai.config.json", "correct": False}]},
                    {"type": "type-answer", "question": "Как называется файл инструкций для Claude Code?", "acceptedAnswers": ["CLAUDE.md", "claude.md"]},
                    {"type": "matching", "pairs": [{"left": ".cursorrules", "right": "Rules-файл для Cursor"}, {"left": "CLAUDE.md", "right": "Rules-файл для Claude Code"}, {"left": ".github/copilot-instructions.md", "right": "Rules-файл для Copilot"}, {"left": "Назначение rules-файлов", "right": "Единые инструкции для всего проекта"}]},
                    {"type": "true-false", "statement": "Rules-файл нужно создать один раз и он будет применяться ко всем запросам к AI.", "correct": True},
                ],
            },
            {
                "t": "Итеративная разработка",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Итерация — ключ к успеху", "markdown": "## Итеративный подход\n\nVibe coding — это **диалог**, не одноразовый запрос.\n\n### Принцип: Маленькие шаги\n\n**Плохо:**\n> Создай мне полностью готовый интернет-магазин с корзиной, оплатой, админкой и доставкой.\n\n**Хорошо (пошагово):**\n1. «Создай компонент карточки товара с названием, ценой и кнопкой «В корзину»»\n2. «Добавь страницу каталога с сеткой карточек»\n3. «Добавь корзину — sidebar с товарами и суммой»\n4. «Добавь форму оформления заказа»\n5. «Подключи Stripe для оплаты»\n\n### Каждый шаг:\n1. **Промпт** — одна конкретная задача\n2. **Проверка** — запусти, посмотри результат\n3. **Коммит** — сохрани рабочую версию в git\n4. **Следующий шаг** — на основе того что получилось\n\n### Золотое правило:\n> **Коммить после каждого работающего шага.** Если AI сломает что-то — можно откатиться."},
                    {"type": "drag-order", "items": ["Написать промпт для одной фичи", "Проверить результат в браузере", "Сделать git commit", "Написать следующий промпт"]},
                    {"type": "quiz", "question": "Почему важно коммитить после каждого шага?", "options": [{"id": "a", "text": "Чтобы откатиться если AI сломает что-то", "correct": True}, {"id": "b", "text": "Чтобы AI видел историю", "correct": False}, {"id": "c", "text": "Это не важно", "correct": False}, {"id": "d", "text": "Для статистики GitHub", "correct": False}]},
                    {"type": "true-false", "statement": "Лучше дать AI одну большую задачу чем разбивать на маленькие шаги.", "correct": False},
                ],
            },
        ],
    },
    # ===== SECTION 4: Практика =====
    {
        "title": "Практика: Создаём проект",
        "pos": 3,
        "lessons": [
            {
                "t": "Проект: Todo-приложение в Bolt",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Создаём первое приложение", "markdown": "## Практика: Todo App в Bolt.new\n\n### Шаг 1: Откройте Bolt.new\nПерейдите на [bolt.new](https://bolt.new)\n\n### Шаг 2: Введите промпт\n```\nCreate a beautiful todo list application with:\n- React + TypeScript + Tailwind CSS\n- Dark theme with gradient background\n- Add, complete, and delete tasks\n- Filter: All, Active, Completed\n- LocalStorage persistence\n- Smooth animations with framer-motion\n- Responsive design for mobile\n```\n\n### Шаг 3: Дождитесь генерации\nBolt создаст все файлы, установит зависимости и запустит приложение.\n\n### Шаг 4: Итерируйте\nПопробуйте добавить:\n- «Add a priority system with color-coded labels (high=red, medium=yellow, low=green)»\n- «Add a search bar to filter tasks»\n- «Add due dates with a date picker»\n\n### Шаг 5: Деплой\nНажмите кнопку Deploy в Bolt — приложение будет доступно по ссылке.\n\n### Ссылки на инструменты:\n- [bolt.new](https://bolt.new) — создание приложения\n- [vercel.com](https://vercel.com) — альтернативный деплой\n- [tailwindcss.com](https://tailwindcss.com) — документация Tailwind"},
                    {"type": "video", "title": "Bolt.new Tutorial — Build a Full App", "url": "https://www.youtube.com/watch?v=S9lcREBRPTk"},
                    {"type": "quiz", "question": "Что нужно для начала работы в Bolt.new?", "options": [{"id": "a", "text": "Только браузер и аккаунт", "correct": True}, {"id": "b", "text": "Node.js и npm", "correct": False}, {"id": "c", "text": "VS Code", "correct": False}, {"id": "d", "text": "Python", "correct": False}]},
                    {"type": "drag-order", "items": ["Открыть bolt.new", "Ввести промпт с описанием приложения", "Дождаться генерации и проверить результат", "Итерировать: добавить фичи через чат", "Нажать Deploy"]},
                    {"type": "true-false", "statement": "В Bolt.new нужно вручную устанавливать npm-пакеты через терминал.", "correct": False},
                ],
            },
            {
                "t": "Проект: Landing page в v0 + Cursor",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Создаём лендинг", "markdown": "## Практика: Лендинг в v0 + Cursor\n\n### Часть 1: Генерируем UI в v0\n\n1. Откройте [v0.dev](https://v0.dev)\n2. Введите промпт:\n```\nModern SaaS landing page with:\n- Hero section with gradient text and CTA button\n- Features grid (3 columns, icons)\n- Pricing table (3 tiers)\n- Testimonials carousel\n- Footer with links\nDark theme, professional look.\n```\n3. Скопируйте код (`npx shadcn@latest add`)\n\n### Часть 2: Дорабатываем в Cursor\n\n1. Создайте Next.js проект: `npx create-next-app@latest my-landing`\n2. Откройте в Cursor\n3. Вставьте код из v0\n4. Попросите Cursor:\n   - «Add smooth scroll animations with framer-motion»\n   - «Make the pricing toggle between monthly and annual»\n   - «Add a contact form with email validation»\n\n### Ссылки:\n- [v0.dev](https://v0.dev) — генерация UI\n- [cursor.sh](https://cursor.sh) — AI-редактор\n- [nextjs.org](https://nextjs.org) — Next.js\n- [ui.shadcn.com](https://ui.shadcn.com) — shadcn/ui компоненты"},
                    {"type": "video", "title": "v0.dev + Cursor workflow", "url": "https://www.youtube.com/watch?v=bNY_qlmPUqE"},
                    {"type": "quiz", "question": "Для чего v0.dev лучше всего подходит?", "options": [{"id": "a", "text": "Генерация UI-компонентов", "correct": True}, {"id": "b", "text": "Бэкенд разработка", "correct": False}, {"id": "c", "text": "Работа с базами данных", "correct": False}, {"id": "d", "text": "DevOps", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "v0.dev", "right": "Генерация UI компонентов"}, {"left": "Cursor", "right": "Доработка и итерация кода"}, {"left": "shadcn/ui", "right": "Библиотека компонентов"}, {"left": "Next.js", "right": "React-фреймворк для продакшена"}]},
                ],
            },
            {
                "t": "Типичные ошибки и как их избежать",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "6 ошибок новичков в vibe coding", "markdown": "## Типичные ошибки\n\n### 1. Слепое доверие AI\nAI может генерировать код с багами, уязвимостями и логическими ошибками.\n**Решение:** Всегда проверяй результат. Запускай приложение. Тестируй edge cases.\n\n### 2. Расплывчатые промпты\n«Сделай красиво» — это не промпт.\n**Решение:** Будь конкретным. Указывай стек, поведение, UI-детали.\n\n### 3. Гигантские промпты\nОписание всего приложения в одном промпте = хаос.\n**Решение:** Разбивай на маленькие шаги. Одна фича = один промпт.\n\n### 4. Нет git-коммитов\nAI сломал код → нет способа откатиться.\n**Решение:** `git commit` после каждого рабочего шага.\n\n### 5. Зависимость от AI\nИспользуешь AI не понимая что он делает.\n**Решение:** Учи основы (HTML, CSS, JS). Читай код который генерирует AI.\n\n### 6. Утечка секретов\nAI может захардкодить API-ключи прямо в код.\n**Решение:** Используй `.env` файлы. Проверяй что в коммите нет секретов."},
                    {"type": "category-sort", "categories": ["Ошибка", "Решение"], "items": [{"text": "Слепо доверять коду AI", "category": "Ошибка"}, {"text": "Всегда проверять и тестировать", "category": "Решение"}, {"text": "Писать расплывчатые промпты", "category": "Ошибка"}, {"text": "Быть конкретным: стек, UI, поведение", "category": "Решение"}, {"text": "Не делать git commit", "category": "Ошибка"}, {"text": "Коммитить после каждого шага", "category": "Решение"}]},
                    {"type": "quiz", "question": "Почему опасно не проверять код от AI?", "options": [{"id": "a", "text": "AI может генерировать код с багами и уязвимостями", "correct": True}, {"id": "b", "text": "AI-код всегда идеален", "correct": False}, {"id": "c", "text": "Проверка не нужна для прототипов", "correct": False}, {"id": "d", "text": "AI сам тестирует код", "correct": False}]},
                    {"type": "true-false", "statement": "API-ключи можно безопасно хранить прямо в коде если репозиторий приватный.", "correct": False},
                    {"type": "fill-blank", "text": "Для хранения секретных ключей нужно использовать файлы ___.", "answers": [".env"]},
                ],
            },
        ],
    },
    # ===== SECTION 5: Финальный тест — Tower Defense =====
    {
        "title": "Финальное испытание",
        "pos": 4,
        "lessons": [
            {
                "t": "Итоговый тест по Vibe Coding",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Финальная проверка знаний", "markdown": "## Итоговый тест\n\nПеред финальной игрой давай проверим что ты усвоил.\n\nВпереди вопросы по всем темам курса:\n- Что такое vibe coding\n- Инструменты\n- Промпт-инженеринг\n- Workflow\n- Безопасность\n\nПосле теста тебя ждёт **Tower Defense** — защити свою базу знаний!"},
                    {"type": "quiz", "question": "Что такое vibe coding?", "options": [{"id": "a", "text": "Создание приложений с помощью AI по описанию на человеческом языке", "correct": True}, {"id": "b", "text": "Музыкальное программирование", "correct": False}, {"id": "c", "text": "Программирование без компьютера", "correct": False}, {"id": "d", "text": "Визуальное программирование блоками", "correct": False}]},
                    {"type": "quiz", "question": "Какой инструмент работает прямо в терминале?", "options": [{"id": "a", "text": "Claude Code", "correct": True}, {"id": "b", "text": "Bolt.new", "correct": False}, {"id": "c", "text": "v0.dev", "correct": False}, {"id": "d", "text": "Lovable", "correct": False}]},
                    {"type": "quiz", "question": "Из каких 5 элементов состоит хороший промпт?", "options": [{"id": "a", "text": "Контекст, Задача, Стек, Детали, Ограничения", "correct": True}, {"id": "b", "text": "Заголовок, Тело, Подпись, Дата, PS", "correct": False}, {"id": "c", "text": "HTML, CSS, JS, React, Node", "correct": False}, {"id": "d", "text": "Input, Process, Output, Test, Deploy", "correct": False}]},
                    {"type": "true-false", "statement": "Rules-файл (.cursorrules / CLAUDE.md) нужно пересоздавать для каждого промпта.", "correct": False},
                    {"type": "true-false", "statement": "Итеративный подход (маленькие шаги + коммиты) эффективнее одного большого промпта.", "correct": True},
                    {"type": "quiz", "question": "Где хранить API-ключи?", "options": [{"id": "a", "text": "В .env файле", "correct": True}, {"id": "b", "text": "В коде напрямую", "correct": False}, {"id": "c", "text": "В README.md", "correct": False}, {"id": "d", "text": "В комментариях в коде", "correct": False}]},
                    {"type": "quiz", "question": "Что делать если AI сломал код?", "options": [{"id": "a", "text": "Откатиться через git (если был коммит)", "correct": True}, {"id": "b", "text": "Переписать всё с нуля", "correct": False}, {"id": "c", "text": "Закрыть проект", "correct": False}, {"id": "d", "text": "Ничего — AI не может сломать код", "correct": False}]},
                ],
            },
            {
                "t": "Tower Defense: Защити свои знания!",
                "xp": 50,
                "steps": [
                    {"type": "info", "title": "Время играть!", "markdown": "## Tower Defense: Защити базу знаний!\n\nТы прошёл весь курс по Vibe Coding. Теперь пора защитить свои знания!\n\n### Как играть:\n1. **Отвечай на вопросы** — зарабатывай монеты ⭐\n2. **Строй башни** — размести их на поле\n3. **Защищай базу** — не дай врагам пройти!\n\n### Башни:\n- 🔮 **Blaster** (30⭐) — быстрая стрельба\n- ⚡ **Zapper** (50⭐) — мощные удары\n- 🎯 **Cannon** (80⭐) — урон по площади\n\n### Улучшай башни до Lvl 3 для максимального урона!\n\nУдачи! 🎮"},
                    {"type": "quiz", "question": "Кто популяризировал термин vibe coding?", "options": [{"id": "a", "text": "Андрей Карпатый", "correct": True}, {"id": "b", "text": "Сэм Альтман", "correct": False}, {"id": "c", "text": "Дарио Амодей", "correct": False}]},
                    {"type": "true-false", "statement": "Cursor — это форк VS Code со встроенным AI.", "correct": True},
                    {"type": "quiz", "question": "Как установить Claude Code?", "options": [{"id": "a", "text": "npm install -g @anthropic-ai/claude-code", "correct": True}, {"id": "b", "text": "pip install claude", "correct": False}, {"id": "c", "text": "brew install claude-code", "correct": False}]},
                    {"type": "true-false", "statement": "Bolt.new требует установки Node.js на компьютер.", "correct": False},
                    {"type": "quiz", "question": "Для чего нужен файл .cursorrules?", "options": [{"id": "a", "text": "Инструкции для AI на весь проект", "correct": True}, {"id": "b", "text": "Настройки линтера", "correct": False}, {"id": "c", "text": "Конфигурация сборки", "correct": False}]},
                    {"type": "true-false", "statement": "Лучше давать AI одну огромную задачу чем разбивать на шаги.", "correct": False},
                    {"type": "quiz", "question": "Что такое v0.dev?", "options": [{"id": "a", "text": "Генератор UI-компонентов от Vercel", "correct": True}, {"id": "b", "text": "IDE для разработки", "correct": False}, {"id": "c", "text": "Хостинг платформа", "correct": False}]},
                    {"type": "quiz", "question": "Зачем коммитить после каждого шага?", "options": [{"id": "a", "text": "Чтобы откатиться если AI сломает код", "correct": True}, {"id": "b", "text": "Для красивого графика GitHub", "correct": False}, {"id": "c", "text": "Это не нужно", "correct": False}]},
                    {"type": "tower-defense"},
                ],
            },
        ],
    },
]


async def seed():
    async with async_session() as db:
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        if not user:
            print("No users found. Create a user first.")
            return

        existing = await db.execute(select(Course).where(Course.title == COURSE_TITLE))
        if existing.scalar_one_or_none():
            print(f"Course '{COURSE_TITLE}' already exists. Skipping.")
            return

        course = Course(
            title=COURSE_TITLE,
            slug="vibe-coding-mastery-" + uuid.uuid4().hex[:6],
            description=COURSE_DESC,
            author_id=user.id,
            category="Vibe Coding",
            difficulty="Beginner",
            status="published",
        )
        db.add(course)
        await db.flush()
        print(f"Created course: {course.title} (id={course.id})")

        all_lesson_ids = []

        for s_data in SECTIONS:
            section = CourseSection(
                course_id=course.id,
                title=s_data["title"],
                position=s_data["pos"],
            )
            db.add(section)
            await db.flush()
            print(f"  Section: {section.title}")

            for i, l_data in enumerate(s_data["lessons"]):
                lesson = CourseLesson(
                    section_id=section.id,
                    title=l_data["t"],
                    position=i,
                    content_type="interactive",
                    content_markdown="",
                    xp_reward=l_data["xp"],
                    steps=l_data.get("steps"),
                )
                db.add(lesson)
                await db.flush()
                all_lesson_ids.append(str(lesson.id))
                step_count = len(l_data.get("steps", []))
                has_td = any(s.get("type") == "tower-defense" for s in l_data.get("steps", []))
                td_flag = " [Tower Defense]" if has_td else ""
                print(f"    Lesson: {lesson.title} ({step_count} steps, {l_data['xp']} xp){td_flag}")

        positions = []
        for idx, lid in enumerate(all_lesson_ids):
            positions.append({
                "id": lid,
                "x": SNAKE_X[idx % 5] * CANVAS_W,
                "y": V_PAD + idx * ROW_H,
            })

        edges = [
            {"id": f"e-{i}", "source": positions[i - 1]["id"], "target": positions[i]["id"]}
            for i in range(1, len(positions))
        ]

        course.roadmap_nodes = positions
        course.roadmap_edges = edges

        await db.commit()
        print(f"\nDone! Course '{COURSE_TITLE}' with {len(all_lesson_ids)} lessons.")


if __name__ == "__main__":
    asyncio.run(seed())
