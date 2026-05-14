"""Seed: Notion и Second Brain — система знаний и продуктивности."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Notion и Second Brain — система знаний и продуктивности"
DESC = (
    "Personal Knowledge Management в 2026: настрой Notion как вторую "
    "память. Методы PARA, CODE, Zettelkasten. Базы данных, daily review, "
    "AI в Notion. Для knowledge workers."
)

def info(t, m): return {"type": "info", "title": t, "markdown": m}
def tf(s, c): return {"type": "true-false", "statement": s, "correct": c}
def quiz(q, opts): return {"type": "quiz", "question": q, "options": [{"id": chr(97+i), "text": t, "correct": ok} for i, (t, ok) in enumerate(opts)]}
def multi(q, opts): return {"type": "multi-select", "question": q, "options": [{"id": chr(97+i), "text": t, "correct": ok} for i, (t, ok) in enumerate(opts)]}
def order(items): return {"type": "drag-order", "items": items}
def match(pairs): return {"type": "matching", "pairs": [{"left": l, "right": r} for l, r in pairs]}
def cards(pairs): return {"type": "flashcards", "cards": [{"front": f, "back": b} for f, b in pairs]}
def sort_items(cats): return {"type": "category-sort", "categories": [{"name": n, "items": items} for n, items in cats]}


S = [
    {
        "title": "Зачем Second Brain",
        "pos": 0,
        "lessons": [
            {
                "t": "Перегруз информации",
                "xp": 20,
                "steps": [
                    info("Мозг не справляется", "## Проблема 2026\n\nКаждый день:\n- 100+ писем\n- 50+ сообщений в мессенджерах\n- 10+ статей и постов\n- 5+ встреч\n\nМозг **не предназначен** хранить всё это. Он для **рассуждений**, не для архива.\n\n## Second Brain\n\nСистема, где **записаны** все идеи, заметки, ссылки, проекты. Когда нужно — **достал и использовал**.\n\n### Что даёт\n- 🧠 Свободная голова — не помнишь всё\n- 🔍 Найдёшь любую заметку за 10 секунд\n- 🔗 Связи между идеями — рождаются инсайты\n- 📈 Накопление — через 1 год БД из заметок = твой второй мозг\n\n## Цитата Тиаго Форте\n> Your brain is for **having ideas**, not for **holding them**."),
                    multi("Что даёт Second Brain?", [
                        ("Освобождает голову для мышления", True),
                        ("Поиск любой заметки за секунды", True),
                        ("Связи между идеями", True),
                        ("Замена сна", False),
                    ]),
                    tf("Мозг плохо приспособлен хранить большие объёмы информации.", True),
                    quiz("Чья известная цитата 'Твой мозг — для идей, не для хранения'?", [
                        ("Илон Маск", False),
                        ("Тиаго Форте (Tiago Forte)", True),
                        ("Стив Джобс", False),
                    ]),
                ],
            },
            {
                "t": "Notion vs Obsidian vs Apple Notes",
                "xp": 15,
                "steps": [
                    info("Выбор инструмента", "## Главные опции 2026\n\n### Notion\n- Базы данных + страницы + шаблоны\n- Облако, синхронизация на всех устройствах\n- Бесплатно для личного использования\n- AI встроен ($10/мес)\n- **Минус:** медленнее на мобильнике\n\n### Obsidian\n- Локальные markdown-файлы\n- Graph view — визуально видишь связи\n- Бесплатно, плагины расширяют\n- **Минус:** UX сложнее, без баз данных\n\n### Apple Notes / Google Keep\n- Бесплатно, очень просто\n- **Минус:** нет баз, нет связей, маленький мозг\n\n### Roam Research\n- Bidirectional links, daily notes\n- Платно ($15/мес)\n- **Минус:** медленный, дорогой\n\n## Рекомендация\n- **Notion** — для большинства\n- **Obsidian** — если ты гик и хочешь markdown + локально"),
                    match([
                        ("Notion", "БД + страницы, облако, AI"),
                        ("Obsidian", "Локальные markdown, graph view"),
                        ("Apple Notes", "Простые заметки без структуры"),
                        ("Roam", "Bi-directional links, daily notes"),
                    ]),
                    quiz("С чего лучше начать новичку?", [
                        ("Apple Notes — просто записки", False),
                        ("Notion — баланс функций и простоты", True),
                        ("Свой custom-инструмент на Rust", False),
                    ]),
                    multi("Какие плюсы у Notion?", [
                        ("Базы данных", True),
                        ("AI встроенный", True),
                        ("Шаблоны", True),
                        ("Бесплатный для личного", True),
                        ("Самый быстрый на мобильнике", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Notion: основы",
        "pos": 1,
        "lessons": [
            {
                "t": "Страницы, блоки, базы данных",
                "xp": 25,
                "steps": [
                    info("3 уровня структуры", "## Иерархия Notion\n\n### 1. Workspace\nТвой аккаунт. Может быть личный + рабочий.\n\n### 2. Pages (Страницы)\nКаждая страница — отдельный документ. Вложенность бесконечная: страница в странице в странице.\n\n### 3. Blocks (Блоки)\nВсё внутри страницы — это блок: текст, заголовок, картинка, todo, embed, calque...\n\n**Слэш-команда `/`** — главный шорткат. `/h1` — заголовок, `/todo` — задача, `/database` — БД.\n\n### 4. Databases (Базы данных)\nГлавная фича Notion. Это **таблица с супер-возможностями**:\n- Каждая строка = страница\n- Колонки = свойства (тип, дата, статус, etc.)\n- Views: Table, Board, Calendar, Gallery, Timeline, List\n\n## Лайфхак\nКаждый «список» (книги, фильмы, задачи, проекты, контакты) → **должен быть базой данных**, не простыми буллетами."),
                    order([
                        "Workspace — твой аккаунт",
                        "Pages — отдельные страницы",
                        "Blocks — элементы внутри страницы",
                        "Databases — таблицы со страницами-строками",
                        "Views — Table/Board/Calendar для одной БД",
                    ]),
                    multi("Что такое блок в Notion?", [
                        ("Любой элемент на странице (текст, todo, embed)", True),
                        ("Вызывается через слэш-команду", True),
                        ("Заголовок, картинка, кнопка — всё блоки", True),
                        ("Только текст", False),
                    ]),
                    quiz("Что предпочесть для списка фильмов?", [
                        ("Список буллетов", False),
                        ("База данных с свойствами (рейтинг, дата, жанр)", True),
                        ("Простой документ", False),
                    ]),
                ],
            },
            {
                "t": "Свойства баз данных",
                "xp": 20,
                "steps": [
                    info("Типы колонок", "## Главные типы свойств\n\n- **Text** — обычный текст\n- **Number** — число\n- **Select** — выбор из одного (с цветами)\n- **Multi-select** — несколько тегов\n- **Date** — дата с временем\n- **Status** — Todo/Doing/Done (новый тип, с группировкой по этапам)\n- **Person** — пользователь Notion\n- **Files** — файлы и картинки\n- **Checkbox** — простой галочка\n- **URL / Email / Phone** — типизированные строки\n- **Relation** — связь с другой БД\n- **Rollup** — агрегат связанных данных\n- **Formula** — вычисление\n\n## Пример: БД задач\n```\n| Title | Status | Priority | Due Date | Project (relation) |\n|---|---|---|---|---|\n| Написать пост | In Progress | High | 2026-05-20 | → Marketing project |\n```\n\n### Relation — суперсила\nСвязка БД задач с БД проектов. В проекте видно все задачи. В задаче — к какому проекту относится."),
                    match([
                        ("Status", "Todo / Doing / Done с группировкой"),
                        ("Relation", "Связь с другой БД"),
                        ("Rollup", "Агрегат связанных данных"),
                        ("Formula", "Вычисление по другим свойствам"),
                        ("Select", "Один выбор из заданных"),
                    ]),
                    multi("Что даёт Relation между двумя БД?", [
                        ("Связь Tasks ↔ Projects", True),
                        ("Видеть в проекте список его задач", True),
                        ("Видеть в задаче её проект", True),
                        ("Удаление одной БД", False),
                    ]),
                    tf("Status — новый тип свойства с группировкой Not started / In progress / Done.", True),
                ],
            },
            {
                "t": "Views: разные взгляды на одну БД",
                "xp": 20,
                "steps": [
                    info("Одна БД — много вью", "## Виды представлений\n\n- **Table** — классическая таблица\n- **Board (Kanban)** — карточки по статусам\n- **Calendar** — события по дате\n- **List** — компактный список\n- **Gallery** — карточки с превью\n- **Timeline** — гант-чарт по датам\n\n## Зачем разные views\nОдна БД задач:\n- **Table** — для общего обзора\n- **Board** — для ежедневной работы (тяни карточки)\n- **Calendar** — для планирования по датам\n- **Timeline** — для квартального плана\n\nКаждый view — со своими фильтрами и сортировками!\n\n### Лайфхак\nСоздай view «Today» с фильтром `Due Date = today`. И **только это** видишь утром."),
                    multi("Какие view есть в Notion для БД?", [
                        ("Table", True),
                        ("Board (Kanban)", True),
                        ("Calendar", True),
                        ("Gallery", True),
                        ("Timeline", True),
                    ]),
                    quiz("Зачем создавать view 'Today' с фильтром по дате?", [
                        ("Чтобы видеть только сегодняшние задачи без отвлечения", True),
                        ("Чтобы создать больше работы", False),
                        ("Это бесполезно", False),
                    ]),
                    tf("В одной БД можно создать много view с разными фильтрами и сортировками.", True),
                ],
            },
        ],
    },
    {
        "title": "PARA, CODE и фреймворки",
        "pos": 2,
        "lessons": [
            {
                "t": "PARA: 4 категории всего",
                "xp": 25,
                "steps": [
                    info("Тиаго Форте", "## Что такое PARA\n\n4 категории, в которые попадает **всё** в твоей жизни:\n\n### P — Projects (Проекты)\nЦели с дедлайнами.\n- «Запустить лендинг»\n- «Подготовить доклад на конференцию»\n- «Найти новую работу»\n\n### A — Areas (Области ответственности)\nОбласти жизни без дедлайна, требующие постоянного внимания.\n- Здоровье\n- Финансы\n- Карьера\n- Семья\n\n### R — Resources (Ресурсы)\nТемы и материалы для будущего использования.\n- Дизайн (статьи, шаблоны)\n- Продуктивность (методики)\n- Любимые рецепты\n\n### A — Archive (Архив)\nЗавершённые проекты, неактуальные области, старые материалы.\n\n## Главное правило\nЛюбая заметка — в **одну из 4 категорий**. Не более."),
                    sort_items([
                        ("P — Projects", ["Запустить лендинг к 1 июня", "Подготовить отчёт за Q1", "Найти стажёра"]),
                        ("A — Areas", ["Здоровье", "Финансы", "Карьерное развитие", "Отношения"]),
                        ("R — Resources", ["Шаблоны email-кампаний", "Любимые рецепты", "Подборка статей про лидерство"]),
                        ("Archive", ["Завершённый проект 2024", "Старая работа", "Закрытый бизнес"]),
                    ]),
                    quiz("К чему относится 'Здоровье' в PARA?", [
                        ("P — Project", False),
                        ("A — Area (область ответственности без дедлайна)", True),
                        ("R — Resource", False),
                    ]),
                    multi("В чём разница Project и Area?", [
                        ("У Project есть дедлайн", True),
                        ("Area — постоянное внимание без deadline", True),
                        ("Project конечен, Area бесконечна", True),
                        ("Это одно и то же", False),
                    ]),
                ],
            },
            {
                "t": "CODE — workflow обработки информации",
                "xp": 20,
                "steps": [
                    info("4 шага", "## Capture — Organize — Distill — Express\n\n### C — Capture (Захват)\nКак только встретил интересное → сохрани. Не оценивай сразу.\n- Web clipper\n- Telegram «избранное»\n- Quick note в Notion\n- Голосовое\n\n### O — Organize (Организация)\nРаспредели по PARA. Когда? Раз в неделю на review.\n\n### D — Distill (Дистилляция)\nВыдели **суть** из заметки. Постепенно:\n- Прогрессивное summarization: выделение → жирным → в начало → в свои слова\n\n### E — Express (Выражение)\nИспользуй накопленное для своих **продуктов**: постов, статей, презентаций, решений.\n\n## Главное\nБольшинство ошибаются: захватывают много, никогда не используют. **Express — главный этап.**"),
                    order([
                        "Capture — мгновенный захват интересного",
                        "Organize — раз в неделю по PARA",
                        "Distill — постепенно выделить суть",
                        "Express — использовать в своих продуктах",
                    ]),
                    multi("Что должно быть в фазе Capture?", [
                        ("Web clipper для статей", True),
                        ("Quick note для идей", True),
                        ("Сохранение голосовых", True),
                        ("Оценка качества прямо сейчас", False),
                    ]),
                    tf("Главная ошибка — собирать много, никогда не использовать.", True),
                ],
            },
            {
                "t": "Zettelkasten: связи между заметками",
                "xp": 20,
                "steps": [
                    info("Метод Лумана", "## Что это\n\nНемецкий социолог **Никлас Луман** написал 70 книг и сотни статей с помощью картотеки заметок (Zettelkasten). 90 000 карточек.\n\n## Принципы\n\n### 1. Атомарность\nОдна идея = одна заметка. Не «всё про маркетинг» — а «5 правил холодного outreach в b2b».\n\n### 2. Linking\nКаждая заметка ссылается на другие. Через год → паутина связанных идей.\n\n### 3. Свои слова\nНе копипаст из статей. Перескажи **своим языком** — иначе не запомнишь.\n\n### 4. Permanent vs Fleeting\n- **Fleeting** — мгновенные мысли, набросок\n- **Literature** — конспект книги/статьи\n- **Permanent** — твоя оформленная мысль для будущего\n\n## В Notion\n- БД «Notes» с тегами\n- Relation Notes ↔ Notes для связей\n- Postupimo: тег `#permanent` для готовых идей"),
                    match([
                        ("Атомарность", "Одна идея = одна заметка"),
                        ("Linking", "Связи между заметками"),
                        ("Свои слова", "Не копипаст, пересказ"),
                        ("Permanent", "Готовая твоя идея для будущего"),
                    ]),
                    multi("Какие принципы Zettelkasten?", [
                        ("Атомарность", True),
                        ("Связи между заметками", True),
                        ("Свои слова, не копипаст", True),
                        ("Большие конспекты с тысячей пунктов", False),
                    ]),
                    quiz("Кто придумал Zettelkasten?", [
                        ("Тиаго Форте", False),
                        ("Никлас Луман", True),
                        ("Эверноут", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Workflow и AI",
        "pos": 3,
        "lessons": [
            {
                "t": "Daily Note + Weekly Review",
                "xp": 20,
                "steps": [
                    info("Ритуалы", "## Daily Note\n\nКаждый день — одна страница:\n- 🌅 **Утро:** 3 главные задачи на день, настроение\n- 📒 **В течение дня:** мысли, идеи, встречи\n- 🌙 **Вечер:** что получилось, чему научился, благодарности\n\nDate-based template в Notion → новая страница каждый день автоматом.\n\n## Weekly Review\n\nВоскресенье или понедельник — **30 минут**:\n\n1. **Прошлая неделя:** что сделал, что нет, почему\n2. **Заметки:** перенести из inbox в PARA\n3. **Проекты:** какие в фокусе на этой неделе?\n4. **Календарь:** запланировано всё важное?\n5. **Reset inbox:** Telegram favorites, email, todo\n\n## Monthly Review\n\nРаз в месяц — час:\n- Цели месяца — что закрыто?\n- Areas — где провисает?\n- Заметки — что переработать в Permanent?\n- Архив — что отправить?\n\n## Лайфхак\nReview без действий = бессмысленно. После review должна появиться **1-3 конкретных задачи** на следующий период."),
                    order([
                        "Daily: утренние 3 задачи + заметки в течение дня + вечерний обзор",
                        "Weekly: 30 мин в воскресенье — обзор недели, inbox, проекты",
                        "Monthly: 1 час — цели месяца, areas, заметки на Permanent",
                    ]),
                    multi("Что входит в Weekly Review?", [
                        ("Обзор сделанного за неделю", True),
                        ("Разбор накопившегося inbox", True),
                        ("Постановка фокуса на новую неделю", True),
                        ("Просто почитать ленту", False),
                    ]),
                    tf("Review без действий по итогам = бессмысленно.", True),
                ],
            },
            {
                "t": "Notion AI: автоматизация",
                "xp": 25,
                "steps": [
                    info("AI внутри документов", "## Что умеет Notion AI ($10/мес)\n\n### В тексте\n- Суммаризовать страницу\n- Перевести\n- Изменить тон\n- Найти action items\n- Сгенерировать черновик\n\n### В базе данных\n- **AI Auto-fill** — автоматически заполняет колонку по содержимому страницы\n- Sentiment, темы, краткое описание из длинного текста\n- Перевод email\n\n### Q&A\nЗадай вопрос своему workspace: «Какие задачи ждут меня на этой неделе?»\n\n## Примеры использования\n\n### 1. Заметки встреч\nЗакончил встречу → AI:\n- summary\n- action items\n- next steps\n\n### 2. Чтение статьи\nВставил большой текст → AI:\n- 3-bullet summary\n- ключевые цитаты\n- собственное мнение для размышления\n\n### 3. Подготовка к встрече\nСоздал страницу → AI:\n- сгенерировал agenda\n- список вопросов к собеседнику"),
                    multi("Что умеет Notion AI?", [
                        ("Суммаризовать длинные страницы", True),
                        ("Auto-fill свойств в БД", True),
                        ("Q&A по всему workspace", True),
                        ("Сам провести встречу за вас", False),
                    ]),
                    quiz("Что особенно полезно для встреч?", [
                        ("AI генерирует summary + action items", True),
                        ("Запрет общения", False),
                        ("Закрытие приложения", False),
                    ]),
                    tf("AI auto-fill может извлекать данные из длинного текста в свойства БД автоматически.", True),
                ],
            },
            {
                "t": "Шаблоны и финал",
                "xp": 25,
                "steps": [
                    info("Готовый старт", "## Базовые шаблоны для старта\n\n### 1. Tasks DB\nКолонки: Title, Status, Priority, Due Date, Project (relation)\nViews: Today, This Week, By Project, All\n\n### 2. Projects DB\nКолонки: Title, Status, Area (relation), Deadline\nViews: Active, Completed\n\n### 3. Areas DB\nКолонки: Title, Goals, Current focus\n\n### 4. Notes DB\nКолонки: Title, Tags (multi-select), Type (Fleeting/Literature/Permanent), Linked Notes (relation), Source\n\n### 5. Reading List\nКолонки: Title, Author, Status (Inbox/Reading/Done), My Notes, Rating\n\n### 6. Habits Tracker\nDate-based, каждый день — checkbox привычки\n\n## Где взять готовое\n- **Notion Templates Gallery** (notion.so/templates)\n- **YouTube** — '@AliAbdaal', 'Marie Poulin', '@AugustBradley'\n- **Twitter/X** — #BuildInPublic, #NotionTemplates\n\n## Финальный совет\n**Простая система, которой пользуешься** > **идеальная система, которой не пользуешься**.\n\nНачни с минимума:\n- Daily note\n- Tasks DB\n- Notes DB\n\nДобавляй по мере нужды."),
                    multi("Что должно быть в минимальной системе с нуля?", [
                        ("Daily note", True),
                        ("Tasks DB", True),
                        ("Notes DB", True),
                        ("100 разных БД сразу", False),
                    ]),
                    tf("Простая система, которой пользуешься > идеальная, которой не пользуешься.", True),
                    quiz("Где найти готовые шаблоны Notion?", [
                        ("Notion Templates Gallery", True),
                        ("Тонкая черная книга", False),
                        ("Только написать с нуля", False),
                    ]),
                    cards([
                        ("PARA", "Projects / Areas / Resources / Archive"),
                        ("CODE", "Capture → Organize → Distill → Express"),
                        ("Zettelkasten", "Атомарные заметки со связями"),
                        ("Permanent note", "Готовая твоя мысль для будущего"),
                        ("Weekly review", "30 мин раз в неделю"),
                        ("Notion AI", "Summary, auto-fill, Q&A по workspace"),
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
            title=T, slug="notion-second-brain-" + uuid.uuid4().hex[:4], description=DESC,
            author_id=author.id, category="Productivity", difficulty="Beginner",
            price=0, currency="USD", status="published",
            tags=["Productivity", "Notion", "Tools", "Knowledge"],
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
