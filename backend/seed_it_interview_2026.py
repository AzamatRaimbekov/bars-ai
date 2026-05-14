"""Seed: Подготовка к собесу в IT 2026. Резюме, leetcode, system design, поведенческая."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Подготовка к собеседованию в IT — 2026"
DESC = (
    "Полный гайд по собеседованию в IT 2026: резюме и LinkedIn под "
    "AI-эпоху, алгоритмическая часть с паттернами, system design, "
    "поведенческая часть (STAR), переговоры по офферу."
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
        "title": "Резюме и LinkedIn под 2026",
        "pos": 0,
        "lessons": [
            {
                "t": "Резюме, которое читают",
                "xp": 20,
                "steps": [
                    info("ATS + человек", "## Двойная аудитория\n\nТвоё резюме читает:\n1. **ATS** (Applicant Tracking System) — софт, скорит по ключевым словам\n2. **Рекрутёр** — 7 секунд скользит глазами\n3. **Hiring Manager** — если первые два пропустили\n\n## Структура (1 страница для junior, 2 для senior)\n\n### Контакты\nИмя | Email | Phone | LinkedIn | GitHub\n\n### Summary (2-3 строки)\n«Senior Frontend разработчик с 5 годами опыта. React, TypeScript, Next.js. Запустил 3 продукта с MAU 50K+.»\n\n### Опыт\nДля каждой работы:\n- Компания, должность, даты\n- **3-5 буллетов с цифрами**\n  - «Снизил время загрузки страницы с 4с до 1.2с (-70%) через code splitting»\n  - «Возглавил миграцию с REST на GraphQL — команда 6 человек»\n\n### Образование, проекты, навыки\n\n## Главное правило: ЦИФРЫ\n- «Работал над приложением» = ноль\n- «Сократил время сборки на 60%, ускорил CI с 8 до 3 минут» = вау"),
                    multi("Что важно в резюме 2026?", [
                        ("Конкретные цифры в каждом буллете", True),
                        ("Ключевые слова для ATS", True),
                        ("Адаптация под конкретную вакансию", True),
                        ("Куча воды без конкретики", False),
                    ]),
                    tf("Рекрутёр в среднем смотрит на одно резюме около 7 секунд.", True),
                    quiz("Что лучше работает?", [
                        ("'Работал над оптимизацией'", False),
                        ("'Сократил latency API с 800ms до 120ms (-85%)'", True),
                    ]),
                ],
            },
            {
                "t": "LinkedIn профиль и нетворкинг",
                "xp": 20,
                "steps": [
                    info("Не только профиль", "## LinkedIn в IT-найме\n\n### Что важно\n- **Headline** = value-prop, не должность («Frontend dev → Senior, React/Next, ex-Yandex, 5y exp»)\n- **About** — расскажи историю, не только перечисление\n- **Open to Work** — включай тонко (#OpenToWork в фото или скрыто в настройках)\n\n### Контент\nПостить раз в неделю про:\n- Технические находки\n- Решённые задачи\n- Опыт работы с инструментами\n→ Тебя начнут замечать рекрутёры через ленту\n\n## Нетворкинг\n\n### Стратегии\n1. **Connect** с разработчиками своего уровня в нужных компаниях\n2. **Referrals** — внутренний рекомендатель повышает шанс прохода фильтра в 4-9 раз\n3. **Cold messages** к рекрутёрам — конкретно: «Заинтересован в роли X в компании Y, у меня опыт A, B, C»\n\n### Anti-pattern\n«Помогите устроиться» массовая рассылка → ноль ответов."),
                    multi("Что работает в LinkedIn для найма?", [
                        ("Сильный headline с value-prop", True),
                        ("Регулярный контент по специальности", True),
                        ("Referrals через коннекшены", True),
                        ("Массовая рассылка 'помогите устроиться'", False),
                    ]),
                    tf("Внутренний referral повышает шанс прохода первичного фильтра в несколько раз.", True),
                    quiz("Что лучше в cold message к рекрутёру?", [
                        ("'Привет, ищу работу, помогите'", False),
                        ("Конкретно: роль, компания, твой опыт, ценность", True),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Алгоритмическая часть",
        "pos": 1,
        "lessons": [
            {
                "t": "Топ-15 паттернов Leetcode",
                "xp": 25,
                "steps": [
                    info("Не зазубривать — понять", "## Топ-15 паттернов\n\n1. **Two Pointers** — два указателя, по массиву\n2. **Sliding Window** — окно фиксированного/переменного размера\n3. **Fast & Slow Pointers** — для цикла в LL\n4. **Merge Intervals** — слияние интервалов\n5. **Cyclic Sort** — числа от 1 до n\n6. **Reverse LL** — разворот списка\n7. **Tree BFS** — обход по уровням\n8. **Tree DFS** — глубина (pre/in/post)\n9. **Two Heaps** — min + max heap (поиск медианы)\n10. **Subsets / Backtracking** — генерация подмножеств\n11. **Binary Search** — для отсортированного\n12. **Top K elements** — heap размера K\n13. **K-way Merge** — слияние K списков\n14. **Topological Sort** — DAG\n15. **DP** (1D и 2D)\n\n## Стратегия\n- Решить **5-10 задач** на каждый паттерн\n- **Понять**, не выучить — после уже узнаёшь похожие\n- Реально нужно знать ~100-150 задач для медианной FAANG-собеседования"),
                    multi("Что важно в подготовке к алгоритмическому собесу?", [
                        ("Узнавать паттерны", True),
                        ("Понимание, не зазубривание", True),
                        ("Решать 5-10 задач на каждый паттерн", True),
                        ("Решить 2000 задач за неделю", False),
                    ]),
                    quiz("Какой подход эффективнее?", [
                        ("Решать всё подряд без классификации", False),
                        ("По паттернам — 5-10 задач на каждый", True),
                        ("Не решать вообще", False),
                    ]),
                    cards([
                        ("Two Pointers", "Два указателя по массиву / 2 списка"),
                        ("Sliding Window", "Окно фиксированного/переменного размера"),
                        ("BFS / DFS", "Обход графа/дерева вширь / в глубину"),
                        ("DP", "Сохраняй промежуточные результаты"),
                        ("Backtracking", "Перебор с откатом"),
                    ]),
                ],
            },
            {
                "t": "Подход к решению задачи",
                "xp": 25,
                "steps": [
                    info("UMPIRE / 5 шагов", "## UMPIRE\n\n### U — Understand\nПовтори задачу своими словами. Уточни:\n- Размер входа?\n- Дубликаты?\n- Отрицательные/нули?\n- Edge cases (пустой массив, один элемент)?\n\n### M — Match\nКакой паттерн подходит? Похоже на Two Pointers? Sliding Window?\n\n### P — Plan\nОпиши алгоритм **словами / псевдокодом** перед написанием.\n\n### I — Implement\nКод. Чисто, понятно, с осмысленными именами.\n\n### R — Review\nПробеги глазами. Off-by-one? Edge cases? Возврат правильного типа?\n\n### E — Evaluate\nO(time) и O(space). Можно ли быстрее? Меньше памяти?\n\n## Главное\n- **Думай вслух** на собесе. Интервьюер видит ход мысли.\n- **Не молчи** в тупике — задай вопрос или озвучь идею\n- **Не пиши код первым** — сначала план\n\n## Anti-pattern\nПовисший в код 20 минут без слов. Интервьюер не понимает, что у тебя в голове → плохой сигнал."),
                    order([
                        "U — Understand задачу и уточнить",
                        "M — Match с известным паттерном",
                        "P — Plan алгоритм словами",
                        "I — Implement в коде",
                        "R — Review на ошибки",
                        "E — Evaluate сложность",
                    ]),
                    multi("Что важно на алгоритмическом собесе?", [
                        ("Думать вслух", True),
                        ("Уточнить условия задачи", True),
                        ("Спланировать решение перед кодом", True),
                        ("Молчать 20 минут и писать", False),
                    ]),
                    tf("Уточняющие вопросы в начале — это сигнал зрелого разработчика, не слабости.", True),
                ],
            },
            {
                "t": "Big O и сложность",
                "xp": 20,
                "steps": [
                    info("Базовая теория", "## Big O\n\n**O(f(n))** = верхняя граница роста времени/памяти при росте n.\n\n### Топ по скорости (от лучших к худшим)\n```\nO(1)        — константа\nO(log n)    — логарифм (binary search)\nO(n)        — линейно (один цикл)\nO(n log n)  — сортировка\nO(n²)       — два вложенных цикла\nO(2^n)      — экспоненциально (плохо)\nO(n!)       — факториал (катастрофа)\n```\n\n### Пример\n```python\n# O(n) — один проход\nfor x in arr:\n    print(x)\n\n# O(n²) — вложенный\nfor x in arr:\n    for y in arr:\n        print(x, y)\n\n# O(log n) — binary search\nlo, hi = 0, len(arr) - 1\nwhile lo <= hi:\n    mid = (lo + hi) // 2\n    ...\n```\n\n## На собесе\n- Всегда **называй complexity** после кода\n- Думай **time и space** отдельно\n- Не путай 'я использовал sort()' с O(n) — это O(n log n)"),
                    match([
                        ("O(1)", "Константа, поиск в hash"),
                        ("O(log n)", "Binary search, balanced tree"),
                        ("O(n)", "Один проход массива"),
                        ("O(n log n)", "Стандартная сортировка"),
                        ("O(n²)", "Два вложенных цикла"),
                    ]),
                    multi("Что важно сказать после кода на собесе?", [
                        ("Time complexity", True),
                        ("Space complexity", True),
                        ("Possible optimizations", True),
                        ("Свой любимый цвет", False),
                    ]),
                    tf("sorted() в Python работает за O(n log n), не O(n).", True),
                ],
            },
        ],
    },
    {
        "title": "System Design",
        "pos": 2,
        "lessons": [
            {
                "t": "Структура SD собеседования",
                "xp": 25,
                "steps": [
                    info("Не пугайся", "## Что спрашивают\nНа senior/staff позициях задают вопросы: «Спроектируй Instagram», «Сделай URL shortener», «Создай систему уведомлений на 100M пользователей».\n\n## Фреймворк ответа (45 мин)\n\n### 1. Requirements (5 мин)\n- Функциональные: что делает?\n- Нефункциональные: scale, latency, availability\n- Уточни: ~~~ 100M пользователей? 1K rps?\n\n### 2. API design (5 мин)\nКакие endpoints?\n```\nPOST /shorten { url } → { short_url }\nGET  /:code     → 302 → original\n```\n\n### 3. Data model (5 мин)\nКакие таблицы? Какие поля?\n```\nurls(id, short_code, long_url, user_id, created_at)\nclicks(id, url_id, clicked_at, ip, ua)\n```\n\n### 4. High-level architecture (10 мин)\nКлиент → LB → API сервер → DB + Cache\nРисуй на доске.\n\n### 5. Deep dive (10 мин)\nИнтервьюер выберет тему: scaling DB, кэширование, очереди.\n\n### 6. Trade-offs (10 мин)\nЧто пожертвовал? Почему?\n\n## Главное\nНе бойся **сказать 'не знаю, но подумаю'**. Это нормально."),
                    order([
                        "Requirements — функциональные и нефункциональные",
                        "API design — endpoints",
                        "Data model — БД",
                        "High-level architecture — рисуем",
                        "Deep dive — тема от интервьюера",
                        "Trade-offs — что пожертвовали",
                    ]),
                    multi("Что входит в SD-собес?", [
                        ("Уточнение requirements", True),
                        ("API design", True),
                        ("Trade-offs", True),
                        ("Сразу написать продакшен-код", False),
                    ]),
                    tf("На SD-собесе нормально говорить 'не знаю, но давайте подумаем'.", True),
                ],
            },
            {
                "t": "Базовые компоненты",
                "xp": 25,
                "steps": [
                    info("Lego системного дизайна", "## Главные компоненты\n\n### Load Balancer (LB)\nРаспределяет запросы между серверами.\n- L4 (TCP) vs L7 (HTTP) LB\n- Алгоритмы: round-robin, least connections, IP hash\n- HAProxy, Nginx, AWS ELB\n\n### Кэш\nХранит часто запрашиваемое в RAM, отвечает за миллисекунды.\n- **Redis** — главный\n- **Memcached** — проще\n- Стратегии: cache-aside, write-through, write-back\n- Eviction: LRU (Least Recently Used)\n\n### CDN\nGeo-distributed cache для статики (картинки, JS, CSS).\n- CloudFlare, AWS CloudFront, Fastly\n\n### База данных\n- **SQL** (Postgres, MySQL) — ACID, relations\n- **NoSQL**:\n  - Key-Value (Redis, DynamoDB) — для кэша/простых\n  - Document (MongoDB) — для JSON\n  - Column (Cassandra) — для time-series\n  - Graph (Neo4j) — для связей\n- **Read replicas** — для масштабирования чтения\n- **Sharding** — для масштабирования записи\n\n### Очередь сообщений\nДля async обработки.\n- **Kafka** — high throughput, durability\n- **RabbitMQ** — flexible routing\n- **AWS SQS** — managed\n\n### Поиск\n- **Elasticsearch** / **Opensearch** — full-text search\n\n### Object storage\n- **S3** для файлов и медиа"),
                    match([
                        ("Load Balancer", "Распределение запросов между серверами"),
                        ("Redis", "Кэш в RAM"),
                        ("CDN", "Geo-distributed кэш статики"),
                        ("Kafka", "Очередь сообщений, durability"),
                        ("S3", "Object storage для файлов"),
                        ("Elasticsearch", "Full-text search"),
                    ]),
                    multi("Что использовать для асинхронной обработки?", [
                        ("Kafka", True),
                        ("RabbitMQ", True),
                        ("AWS SQS", True),
                        ("Excel", False),
                    ]),
                    quiz("Что обычно используется как кэш в RAM?", [
                        ("Redis", True),
                        ("Postgres", False),
                        ("S3", False),
                    ]),
                ],
            },
            {
                "t": "CAP, scale, trade-offs",
                "xp": 20,
                "steps": [
                    info("Трейд-офы", "## CAP-теорема\nВ распределённой системе можно выбрать **2 из 3**:\n- **C** — Consistency (все ноды видят одинаковые данные)\n- **A** — Availability (система всегда отвечает)\n- **P** — Partition tolerance (работает при сетевых разрывах)\n\nP в реальности **обязателен** — сети ломаются. Так что выбор между C и A.\n\n### CP-системы\nMongoDB по умолчанию, etcd, ZooKeeper. Лучше отказать, чем дать устаревший ответ.\n\n### AP-системы\nDynamoDB, Cassandra. Лучше дать ответ (может устаревший), чем отказать.\n\n## Scaling\n\n### Vertical (вверх)\nБольше CPU/RAM на одной машине. Просто, но потолок.\n\n### Horizontal (вширь)\nБольше машин. Сложнее, но безграничнее.\n\n### Read vs Write\n- Read-heavy: read replicas + cache\n- Write-heavy: sharding, очереди\n\n## Типичные trade-offs\n- **Latency vs Consistency** — strong vs eventual\n- **Cost vs Speed** — больше железа = быстрее\n- **Simplicity vs Flexibility** — monolith vs microservices\n- **Build vs Buy** — managed services\n\n## Главное\nНет «правильного» ответа. Покажи, что **видишь компромиссы** и выбираешь осознанно."),
                    multi("Что входит в CAP?", [
                        ("Consistency", True),
                        ("Availability", True),
                        ("Partition tolerance", True),
                        ("Cost-effectiveness", False),
                    ]),
                    tf("В реальной распределённой системе Partition tolerance обязательна, выбор идёт между C и A.", True),
                    quiz("Чем отличается horizontal scaling от vertical?", [
                        ("Vertical — больше машин, horizontal — мощнее одну", False),
                        ("Vertical — мощнее одну, horizontal — больше машин", True),
                    ]),
                    multi("Что показывает зрелого SD-инженера?", [
                        ("Понимание trade-offs", True),
                        ("Осознанный выбор compromises", True),
                        ("Видение масштабирования", True),
                        ("Уверенность что есть один правильный ответ", False),
                    ]),
                ],
            },
        ],
    },
    {
        "title": "Поведенческая и оффер",
        "pos": 3,
        "lessons": [
            {
                "t": "STAR-методика",
                "xp": 25,
                "steps": [
                    info("Структура ответа", "## Что такое\n\nПри поведенческих вопросах («Расскажи про сложный конфликт», «Когда ты ошибся») отвечай по структуре **STAR**:\n\n### S — Situation\nКонтекст: проект, команда, время.\n«Я был tech lead команды из 5 человек, шёл проект редизайна оплаты.»\n\n### T — Task\nКонкретная задача / проблема перед тобой.\n«Дизайнер прислал макет, который **технически нереализуем** за оставшиеся 2 недели. PM настаивал на сроке.»\n\n### A — Action\nЧто **ты** сделал. Конкретно. Не команда — ты.\n«Я подготовил техническое обоснование с 3 вариантами: A) сделать как просят, +6 недель; B) упрощённая версия за 2 недели; C) фокус на критическом, остальное в фазу 2. Презентовал команде и PM.»\n\n### R — Result\nЧисло, если возможно. Что узнал.\n«Согласовали вариант C. Сделали в срок, привлекли 30K пользователей. PM поблагодарил за конструктивный подход.»\n\n## Главное\n- **Ты в центре** — не размывай в «мы»\n- **Числа** где возможно\n- **Чему научился** — рефлексия ценится\n- **Не критикуй коллег** прямо — даже если они были не правы"),
                    order([
                        "S — Situation: контекст",
                        "T — Task: задача перед тобой",
                        "A — Action: что именно ТЫ сделал",
                        "R — Result: число + чему научился",
                    ]),
                    multi("Что важно в STAR-ответе?", [
                        ("Конкретика, не общие слова", True),
                        ("Ты в центре, не размытое 'мы'", True),
                        ("Числа в результате", True),
                        ("Рефлексия и обучение", True),
                        ("Критика прежних коллег", False),
                    ]),
                    tf("Конкретные цифры в результате делают ответ более убедительным.", True),
                ],
            },
            {
                "t": "Топ-10 поведенческих вопросов",
                "xp": 20,
                "steps": [
                    info("Подготовь истории", "## Подготовь 10 историй\n\nДля каждой — STAR на 2-3 минуты.\n\n### Вопросы\n1. Расскажи про самый сложный проект\n2. Когда ты не согласился с менеджером\n3. Когда ты ошибся\n4. Когда у тебя не было всей информации\n5. Когда ты помогал коллеге\n6. Когда пришлось сделать tough decision\n7. Когда ты не справился с задачей\n8. Расскажи про конфликт в команде\n9. Когда ты делал что-то впервые\n10. Чему ты научился за последний год\n\n## Главное правило\n**Одна история = много вопросов**.\nИстория про конфликт может ответить на:\n- «Конфликт в команде»\n- «Сложный коллега»\n- «Когда не согласился»\n- «Tough decision»\n\nПодготовь 5-7 хороших историй — закроют все вопросы.\n\n## Что не делать\n- Импровизировать с нуля — будет вода\n- Длинно (>5 минут) — интервьюер заскучает\n- Только успехи — нужны провалы и уроки\n- Винить других"),
                    multi("Что нужно подготовить для поведенческого собеса?", [
                        ("5-7 STAR-историй из реального опыта", True),
                        ("Истории с уроками из провалов", True),
                        ("Конкретные цифры", True),
                        ("Только идеальные успехи", False),
                    ]),
                    tf("Одна STAR-история может ответить на несколько разных вопросов.", True),
                    quiz("Какая длительность ответа оптимальна?", [
                        ("30 секунд", False),
                        ("2-3 минуты", True),
                        ("10 минут", False),
                    ]),
                ],
            },
            {
                "t": "Переговоры по офферу",
                "xp": 25,
                "steps": [
                    info("Где люди теряют деньги", "## Что обсуждать в оффере\n\n### 1. Base salary\nГлавное. Базовая зарплата.\n\n### 2. Бонус\n- Sign-on bonus (единоразовый при найме)\n- Annual / quarterly\n- Equity / акции\n\n### 3. Льготы\n- ДМС\n- Удалёнка / гибрид\n- Обучение, конференции\n- Спорт, психолог\n- Отпуск\n\n### 4. Карьерный путь\n- Возможности роста\n- Performance review когда\n\n## Стратегия переговоров\n\n### 1. **Никогда не называй цифру первым**\nЕсли спрашивают «сколько хочешь?» — ответь:\n«Хочу понять полный пакет компании. Что вы обычно предлагаете для этой роли?»\n\n### 2. **Имей альтернативу** (BATNA)\nДругой оффер или текущая работа = твоя сила.\n\n### 3. **Negotiate всегда**\nСкажут «нет» = ничего не теряешь. Согласятся на +10-20% = большая разница за пару писем.\n\n### 4. **Не только деньги**\nЕсли base потолок — попроси sign-on, дополнительный отпуск, ремоут.\n\n### 5. **В письме, не голосом**\nЕсть время подумать обеим сторонам.\n\n## Anti-pattern\n«О, какой щедрый оффер, я согласен» = упустишь 10-30% базы.\n\n## Реальность\nПереговоры в IT — **норма**. 80% компаний ожидают и закладывают buffer."),
                    multi("Что обсуждать в оффере?", [
                        ("Base salary", True),
                        ("Бонусы и equity", True),
                        ("Удалёнка/гибрид и льготы", True),
                        ("Только согласие или отказ", False),
                    ]),
                    tf("В IT принято торговаться по офферу — компании закладывают buffer.", True),
                    quiz("Что делать, если спрашивают 'сколько хочешь'?", [
                        ("Назвать свою цифру первым", False),
                        ("Спросить про общий пакет компании", True),
                        ("Замолчать", False),
                    ]),
                    cards([
                        ("UMPIRE", "Understand, Match, Plan, Implement, Review, Evaluate"),
                        ("Big O", "Сложность алгоритма по времени и памяти"),
                        ("CAP", "Consistency / Availability / Partition tolerance"),
                        ("STAR", "Situation, Task, Action, Result"),
                        ("BATNA", "Best Alternative — твоя сила в переговорах"),
                        ("Negotiate", "Всегда обсуждай оффер, не соглашайся сразу"),
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
            title=T, slug="it-interview-2026-" + uuid.uuid4().hex[:4], description=DESC,
            author_id=author.id, category="Programming", difficulty="Intermediate",
            price=0, currency="USD", status="published",
            tags=["Programming", "Career", "Interview", "Algorithms", "System Design"],
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
