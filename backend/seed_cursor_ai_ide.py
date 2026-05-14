"""Seed: Cursor & AI IDE 2026 — продуктивный кодинг с AI."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Cursor & AI IDE 2026 — кодинг с ИИ-напарником"
DESC = (
    "Полный гид по AI-IDE 2026: Cursor, Windsurf, Claude Code. Tab, "
    "Composer, Agent mode, rules, контекст, безопасный workflow. "
    "Для разработчиков любого уровня."
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
        "title": "AI-IDE: ландшафт 2026",
        "pos": 0,
        "lessons": [
            {
                "t": "Cursor, Windsurf, Claude Code, Copilot",
                "xp": 15,
                "steps": [
                    info("Кто есть кто", "## Инструменты 2026\n\n### Cursor (Anysphere)\nVS Code-fork. Самый зрелый AI-IDE. **Tab** (автодополнение), **Cmd+K** (inline-edit), **Composer** (multi-file), **Agent mode** (автономные изменения).\n\n### Windsurf (Codeium)\nКонкурент Cursor. Cascade — multi-file агент. Бесплатный план мощнее, чем у Cursor.\n\n### Claude Code (Anthropic)\nCLI-tool (в терминале) и расширения для IDE. Глубокая интеграция с Anthropic API. Подходит для серверной работы, agentic flows.\n\n### GitHub Copilot\nКлассический автокомплит + Chat. Хорош, но проигрывает Cursor по multi-file.\n\n### Zed AI\nБыстрый редактор с AI. Альтернатива для тех, кто не хочет VS Code.\n\n### Сравнение\n| Инструмент | Сильно | Слабо |\n|---|---|---|\n| Cursor | Composer, Agent, ecosystem | Дорого ($20/мес) |\n| Windsurf | Free tier, Cascade | Меньше плагинов |\n| Claude Code | CLI, агентность | Не GUI-first |\n| Copilot | Стабильность | Слабее в multi-file |"),
                    match([
                        ("Cursor", "VS Code-форк, Composer/Agent, $20/мес"),
                        ("Windsurf", "Cascade, мощный free tier"),
                        ("Claude Code", "CLI + IDE-плагины, агентность"),
                        ("Copilot", "Классический автокомплит от GitHub"),
                    ]),
                    quiz("Что общее у Cursor и Windsurf?", [
                        ("Это терминальные инструменты", False),
                        ("Это форки/конкуренты VS Code с глубокой AI-интеграцией", True),
                        ("Это плагины для Vim", False),
                    ]),
                    multi("Что лучше для multi-file редактирования?", [
                        ("Cursor Composer", True),
                        ("Windsurf Cascade", True),
                        ("Старый VS Code без AI", False),
                        ("Claude Code в режиме agentic", True),
                    ]),
                ],
            },
            {
                "t": "Tab-комплит: твой бесшумный помощник",
                "xp": 20,
                "steps": [
                    info("Главный шорткат", "## Tab-комплит\n\nКогда пишешь код, IDE предсказывает следующие 1-30 строк. Жмёшь **Tab** — вставляет.\n\n### Когда работает супер\n- Шаблонный код (boilerplate)\n- Повторяющиеся паттерны (3-я похожая функция → угадает целиком)\n- Тесты после написания функции\n- Migration после изменения модели\n\n### Когда мешает\n- Креативный/неочевидный код — предлагает плохое\n- Когда сам обдумываешь архитектуру — отвлекает\n\n### Лайфхак\nПиши **комментарий** перед нужным кодом — Tab часто реализует именно его:\n```python\n# Считать CSV, отфильтровать по дате, вернуть top-10 по сумме\n[Tab → реализация целиком]\n```\n\n### Контр-навык\nУмение **отказаться** от плохого предложения. Не Tab’ай тупо — читай."),
                    multi("Когда Tab особенно полезен?", [
                        ("Шаблонный boilerplate", True),
                        ("Тесты к написанной функции", True),
                        ("Повторяющиеся паттерны", True),
                        ("Креативный архитектурный код", False),
                    ]),
                    tf("Хорошая практика — нажимать Tab на всё подряд без чтения.", False),
                    quiz("Что увеличивает качество Tab-предложений?", [
                        ("Понятные имена переменных и комментарии перед кодом", True),
                        ("Случайные имена a, b, c, d", False),
                        ("Минифицированный код", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Базовый workflow в Cursor",
        "pos": 1,
        "lessons": [
            {
                "t": "Cmd+K: inline edit",
                "xp": 20,
                "steps": [
                    info("Превратить выделение в нужный код", "## Cmd+K (Mac) / Ctrl+K (Win)\n\n### Сценарии\n1. **Выдели функцию** → Cmd+K → «добавь обработку ошибок и логирование»\n2. **Выдели SQL** → Cmd+K → «преврати в Prisma query»\n3. **Поставь курсор в пустую строку** → Cmd+K → «функция, которая считает X»\n4. **Выдели CSS** → Cmd+K → «адаптивно для мобилки, breakpoint sm»\n\n### Хорошие промпты для Cmd+K\n```\n+ «добавь TypeScript типы»\n+ «зарефакторь в hook»\n+ «преврати в async/await»\n+ «добавь jsdoc»\n```\n\n### Плохие\n```\n- «улучши» (что улучшить?)\n- «сделай красивее» (что значит красивее?)\n```"),
                    multi("Хорошие промпты для inline-edit:", [
                        ("«добавь обработку ошибок»", True),
                        ("«добавь TypeScript типы»", True),
                        ("«зарефакторь в hook»", True),
                        ("«улучши»", False),
                        ("«сделай круто»", False),
                    ]),
                    quiz("Что делает Cmd+K в Cursor?", [
                        ("Открывает терминал", False),
                        ("Inline-редактирование выделенного кода по промпту", True),
                        ("Сохраняет файл", False),
                    ]),
                    tf("Чёткий промпт даёт сильно лучший результат, чем 'улучши'.", True),
                ],
            },
            {
                "t": "Composer: правки на много файлов сразу",
                "xp": 25,
                "steps": [
                    info("Multi-file редактор", "## Composer (Cmd+I)\n\nРедактор многофайловых изменений. Описываешь задачу — AI правит несколько файлов сразу с превью.\n\n### Сценарии\n- «Добавь dark mode: переключатель в Header, store, применение в Layout»\n- «Переименуй userId → accountId по всему проекту»\n- «Добавь страницу /pricing с роутом, компонентом и линком из меню»\n\n### Workflow\n1. Открой Composer (Cmd+I)\n2. Опиши задачу подробно\n3. AI показывает **diff** по всем затронутым файлам\n4. Принимаешь файлы по одному (можно правки внутри)\n5. **Запускаешь и проверяешь!**\n\n### Контекст\nДобавь файлы через **@** (`@components/Header.tsx`) — AI учтёт их структуру.\n\n### Agent mode\nСамое автономное: AI пишет, запускает тесты, исправляет ошибки сам. Только под надзором!"),
                    order([
                        "Открыть Composer (Cmd+I)",
                        "Описать задачу подробно",
                        "Добавить релевантные файлы через @",
                        "AI показывает diff",
                        "Принимать изменения по файлам",
                        "Запустить и проверить",
                    ]),
                    multi("Что эффективно делать в Composer?", [
                        ("Multi-file рефакторинг", True),
                        ("Добавить feature, затрагивающую несколько файлов", True),
                        ("Переименование через проект", True),
                        ("Маленькую правку в одной строке", False),
                    ]),
                    tf("Перед принятием diff от Composer стоит просмотреть каждый файл.", True),
                    quiz("Как добавить файл в контекст Composer?", [
                        ("Перетащить в окно", False),
                        ("Использовать @file-name в промпте", True),
                        ("Скопировать в буфер", False),
                    ]),
                ],
            },
            {
                "t": "Контекст: codebase indexing",
                "xp": 20,
                "steps": [
                    info("Чтобы AI знал твой проект", "## Что такое codebase indexing\n\nCursor сканирует все файлы проекта, делает embeddings, кладёт в локальную векторную БД. **Когда ты задаёшь вопрос — AI находит релевантные файлы автоматом.**\n\n### Когда работает\n- «Где в коде хранится логика логина?» — найдёт\n- «Зарефакторь все формы» — соберёт все формы\n- «Как наш API возвращает ошибки?» — посмотрит обработчики\n\n### Когда НЕ работает\n- Очень большая кодовая база (миллионы строк) — медленно\n- Файлы в .gitignore — пропускаются\n- Если индекс не обновился после изменений\n\n### Управление\n- `Cmd+Shift+P → Reindex`\n- `.cursorignore` — что **не** индексировать (как .gitignore)\n- Privacy mode — не отправлять код на сервера AI"),
                    quiz("Что такое codebase indexing?", [
                        ("Просто список файлов", False),
                        ("Векторный индекс по всему коду для семантического поиска контекста", True),
                        ("Сжатие репозитория", False),
                    ]),
                    multi("Что управляет индексацией?", [
                        (".cursorignore — что не индексировать", True),
                        ("Privacy mode — не отправлять код на сервера", True),
                        ("Reindex команда — пересоздать индекс", True),
                        ("Размер монитора", False),
                    ]),
                    tf("После больших изменений в проекте стоит сделать Reindex для актуальности контекста.", True),
                ],
            },
        ],
    },
    {
        "title": "Продвинутые техники",
        "pos": 2,
        "lessons": [
            {
                "t": "Rules: правила для всего проекта",
                "xp": 25,
                "steps": [
                    info(".cursorrules / .cursor/rules", "## Rules — твой код-стайл для AI\n\nФайл `.cursorrules` (или папка `.cursor/rules/*.md`) в корне проекта. AI читает его при **каждом** запросе и следует правилам.\n\n### Что писать\n```markdown\n# Project: shopping-cart\n\n## Стек\n- Next.js 16, React 19\n- Tailwind v4\n- Zustand для state\n- TanStack Query для данных\n\n## Стиль кода\n- Function components, no class components\n- Hooks для всей логики\n- Tailwind, no CSS modules\n- Pure functions где возможно\n\n## Запреты\n- Никаких console.log в production коде\n- Никаких any в TypeScript\n- Не использовать moment.js — только date-fns\n\n## Тесты\n- Vitest + Testing Library\n- Каждый компонент с user-interaction тестируется\n```\n\n### Эффект\nAI перестаёт предлагать moment.js, использует Zustand вместо Redux, и т.д.\n\n### Лайфхак\nКогда AI делает что-то не так — допиши правило, и больше не повторится."),
                    multi("Что полезно описать в .cursorrules?", [
                        ("Технологический стек", True),
                        ("Стиль кода и naming conventions", True),
                        ("Запреты (no any, no console.log)", True),
                        ("Личные предпочтения по цветовой схеме редактора", False),
                    ]),
                    tf("Чёткие правила в .cursorrules заставляют AI следовать стилю проекта.", True),
                    quiz("Где хранятся rules в проекте?", [
                        ("В переменных окружения", False),
                        ("В .cursorrules или .cursor/rules/*.md в корне", True),
                        ("В package.json", False),
                    ]),
                    cards([
                        (".cursorrules", "Файл правил в корне проекта"),
                        (".cursorignore", "Файл, какие пути не индексировать"),
                        ("Privacy mode", "Запрет отправки кода на сервера AI"),
                        ("@file", "Способ явно добавить файл в контекст"),
                    ]),
                ],
            },
            {
                "t": "Промпты для сложных задач",
                "xp": 25,
                "steps": [
                    info("Структура хорошего промпта", "## Когда задача сложная\n\n### Плохой промпт\n```\nДобавь авторизацию\n```\n\n### Хороший промпт\n```\nДобавь авторизацию по email+пароль.\n\nКонтекст:\n- Backend: FastAPI (см. @backend/app/routers/users.py)\n- Frontend: Next.js, store на Zustand (@store/auth.ts)\n- JWT в httpOnly cookie, refresh через /api/auth/refresh\n\nЗадача:\n1. POST /api/auth/login — принимает email/password, проверяет, выдаёт JWT\n2. Frontend: страница /login с формой\n3. Zustand store с user, login, logout\n4. Защищённый route /dashboard перенаправляет на /login если не залогинен\n\nЗапреты:\n- Не использовать NextAuth — у нас своё\n- Пароли через bcrypt, не SHA\n- JWT в httpOnly cookie, не localStorage\n```\n\n### Формула\n`Контекст` + `Чёткая задача (нумерованная)` + `Запреты` + `Ссылки на файлы через @`"),
                    order([
                        "Контекст — где сейчас находимся",
                        "Чёткая задача, нумерованная",
                        "Запреты / ограничения",
                        "Ссылки на существующие файлы через @",
                    ]),
                    multi("Что улучшает промпт для сложной задачи?", [
                        ("Контекст (что есть сейчас)", True),
                        ("Нумерованный список задач", True),
                        ("Запреты", True),
                        ("Ссылки на файлы через @", True),
                        ("Одно слово 'сделай'", False),
                    ]),
                    tf("Чем подробнее задача — тем меньше итераций нужно для готового решения.", True),
                ],
            },
            {
                "t": "Agent mode: автономные изменения",
                "xp": 20,
                "steps": [
                    info("Когда отпустить вожжи", "## Agent mode\n\nAI **сам**:\n- Решает, какие файлы открыть\n- Делает правки\n- Запускает тесты\n- Видит ошибки → правит\n- Так до зелёного / лимита\n\n### Когда использовать\n- Утилитарные задачи (миграции, формат, рефакторинги)\n- Когда не критично к деталям\n- Когда есть хорошие тесты — AI сам проверит\n\n### Когда НЕ использовать\n- Архитектурные решения\n- Деструктивные операции в БД\n- Production deploys\n- Когда нет тестов (AI не узнает, что сломал)\n\n### Безопасность\n- Запускай в отдельной ветке\n- Просматривай diff целиком перед merge\n- Имей revert-план\n- Не давай agent доступ к prod credentials\n\n### Лайфхак\nИспользуй agent mode для **исследования**: «найди все места, где мы используем deprecated API X, и предложи план миграции». Он сам проползёт код и составит план."),
                    multi("Когда стоит использовать Agent mode?", [
                        ("Рефакторинги с покрытием тестами", True),
                        ("Исследовательские задачи", True),
                        ("Утилитарные миграции", True),
                        ("Production-deploy критичной фичи", False),
                    ]),
                    tf("Перед использованием Agent mode стоит создать отдельную git-ветку.", True),
                    quiz("Что главное при работе с Agent mode?", [
                        ("Дать ему доступ ко всему сразу", False),
                        ("Тесты + ревью diff + отдельная ветка", True),
                        ("Закрыть тесты, чтобы быстрее работал", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Безопасность и этика",
        "pos": 3,
        "lessons": [
            {
                "t": "Что НЕ отправлять в AI",
                "xp": 20,
                "steps": [
                    info("Privacy в AI-IDE", "## Что попадает на сервер AI\n\nКогда ты юзаешь Cursor/Copilot, твой код **отправляется** в облако вендора (если не включён Privacy mode).\n\n### Не клади в индекс\n- 🔒 Production API keys, токены, пароли\n- 🔒 Реальные данные клиентов (PII)\n- 🔒 Коммерческую тайну (NDA-материалы)\n- 🔒 Закрытые алгоритмы под NDA\n\n### Защита\n- **`.cursorignore`** для секретов\n- **`.env`** никогда не индексируется (по умолчанию)\n- **Privacy mode** — обработка локально или без сохранения\n- **Self-hosted** — Continue.dev, локальная Llama\n\n### Корпоративная защита\n- Cursor Business / Enterprise — SOC 2, без обучения на твоём коде\n- Claude Code — Anthropic Enterprise гарантии\n- GitHub Copilot Business — без обучения на коде"),
                    multi("Что НЕ должно попадать в AI-IDE?", [
                        ("Production API keys", True),
                        ("Реальные данные клиентов", True),
                        ("Коммерческая тайна под NDA", True),
                        ("Открытый readme.md", False),
                    ]),
                    quiz("Что обеспечивают Business/Enterprise планы?", [
                        ("Бесплатный доступ", False),
                        ("SOC 2, отсутствие обучения на коде клиента", True),
                        ("Случайный код от других пользователей", False),
                    ]),
                    tf("Файл .env по умолчанию не индексируется в Cursor.", True),
                ],
            },
            {
                "t": "Code review AI-кода",
                "xp": 20,
                "steps": [
                    info("Доверяй, но проверяй", "## Чек-лист ревью AI-кода\n\n### Корректность\n- [ ] Код **запускается** без ошибок\n- [ ] Тесты проходят\n- [ ] Edge cases обработаны (null, empty, большие числа)\n\n### Безопасность\n- [ ] SQL без injection (parameterized queries)\n- [ ] Валидация входов\n- [ ] Никаких hardcoded секретов\n- [ ] CORS правильно настроен\n\n### Архитектура\n- [ ] Не дублирует существующий код (DRY)\n- [ ] Соответствует стилю проекта\n- [ ] Зависимости минимальны (не добавляет ненужное)\n\n### Производительность\n- [ ] N+1 запросов нет\n- [ ] Нет утечек памяти (event listeners закрываются)\n- [ ] Большие данные пейджинируются\n\n### Зрелость\nAI может писать **функционирующий** код, который при этом **плохой** (medlennyy, уязвимый, неподдерживаемый). Опыт разработчика — ловить эти проблемы."),
                    multi("Что проверять в AI-коде перед merge?", [
                        ("SQL injection отсутствует", True),
                        ("Валидация входов", True),
                        ("Соответствие стилю проекта", True),
                        ("Никаких hardcoded ключей", True),
                        ("Шрифт комментариев", False),
                    ]),
                    tf("AI-код всегда оптимальный по производительности.", False),
                    quiz("Что НЕ стоит делать с AI-кодом?", [
                        ("Безусловно мерджить без ревью", True),
                        ("Запускать тесты", False),
                        ("Просматривать diff", False),
                    ]),
                ],
            },
            {
                "t": "Привычки сильного AI-кодера",
                "xp": 25,
                "steps": [
                    info("Что отличает", "## Сильный AI-кодер...\n\n### Уважает фундамент\n- Знает язык и фреймворк глубже, чем AI\n- Может написать сам — AI просто быстрее\n\n### Промпт-инженер на ходу\n- Чёткие промпты с первого раза\n- Контекст через @-references\n- Использует rules для общих требований\n\n### Read-first\n- Сначала читает diff, потом принимает\n- Не Tab’ает на всё подряд\n- Знает, когда отказать AI и переписать вручную\n\n### Думает архитектурой\n- AI делает локальные оптимумы\n- Архитектура — это его, человека\n- AI не выберет правильный паттерн системы за тебя\n\n### Растёт\n- После каждой AI-сессии: что AI делал лучше? хуже? Чему научиться?\n- Делится промптами с командой\n- Обновляет .cursorrules по мере роста проекта\n\n### Понимает ограничения\n- AI **не** знает свежую документацию\n- AI **не** видит runtime ошибок\n- AI **не** думает о бизнес-целях"),
                    multi("Что характеризует сильного AI-кодера?", [
                        ("Знает фундамент глубже, чем AI", True),
                        ("Чёткие промпты с контекстом", True),
                        ("Ревьюит diff перед принятием", True),
                        ("Принимает любые предложения AI без чтения", False),
                        ("Поддерживает актуальный .cursorrules", True),
                    ]),
                    tf("AI заменяет необходимость знать фундаментальные основы разработки.", False),
                    quiz("Чем человек сильнее AI в кодинге?", [
                        ("Архитектура и бизнес-цели", True),
                        ("Скорость написания boilerplate", False),
                        ("Запоминание синтаксиса", False),
                    ]),
                    cards([
                        ("Tab", "Автодополнение 1-30 строк"),
                        ("Cmd+K", "Inline edit выделенного"),
                        ("Composer (Cmd+I)", "Multi-file правки с превью"),
                        ("Agent mode", "Автономные изменения с тестами"),
                        (".cursorrules", "Правила стиля для AI"),
                        ("@file", "Добавить файл в контекст"),
                    ]),
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
            title=T, slug="cursor-ai-ide-" + uuid.uuid4().hex[:4], description=DESC,
            author_id=author.id, category="Programming", difficulty="Beginner",
            price=0, currency="USD", status="published",
            tags=["AI", "Programming", "Productivity", "Tools"],
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
