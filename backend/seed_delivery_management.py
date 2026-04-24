"""Seed: Delivery Management — от хаоса к системе — 8 sections, 35 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Delivery Management — от хаоса к системе"
DESC = (
    "Полный курс по delivery-менеджменту для руководителей и тимлидов: управление поставками, "
    "Agile/Kanban на практике, метрики delivery, работа со стейкхолдерами, управление рисками "
    "и масштабирование команд."
)

S = [
    # ===== SECTION 1: Основы Delivery Management =====
    {
        "title": "Основы Delivery Management",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое Delivery Management",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Роль Delivery Manager", "markdown": "## Что такое Delivery Management\n\n**Delivery Management (DM)** — дисциплина, обеспечивающая предсказуемую, качественную и своевременную поставку ценности пользователям.\n\n### Зоны ответственности DM:\n- **Процессы** — выстраивание и улучшение рабочих практик\n- **Поток** — устранение блокеров и ускорение доставки\n- **Прозрачность** — видимость прогресса для всей команды и стейкхолдеров\n- **Риски** — идентификация и управление угрозами\n- **Люди** — создание условий для продуктивной работы команды\n\n### Ключевые книги:\n- **\"The Phoenix Project\"** (Kim, Behr, Spafford) — роман о трансформации IT-поставок\n- **\"Accelerate\"** (Forsgren, Humble, Kim) — научные данные о высокопроизводительных командах\n\n### Главный вопрос DM:\n«Что мешает команде поставлять ценность быстро и надёжно?»\n\n### Delivery ≠ просто «сделать в срок»:\nДоставка — это система, которая должна работать **устойчиво** и **масштабируемо**."},
                    {"type": "quiz", "question": "Какой главный вопрос задаёт Delivery Manager?", "options": [{"id": "a", "text": "Сколько фич запланировано на квартал?", "correct": False}, {"id": "b", "text": "Что мешает команде поставлять ценность быстро и надёжно?", "correct": True}, {"id": "c", "text": "Какой бюджет на следующий спринт?", "correct": False}, {"id": "d", "text": "Кто виноват в задержке?", "correct": False}]},
                    {"type": "true-false", "statement": "Delivery Management сводится только к контролю сроков и дедлайнов.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Delivery Management", "back": "Дисциплина обеспечения предсказуемой и качественной поставки ценности пользователям"}, {"front": "The Phoenix Project", "back": "Книга-роман о трансформации IT, описывающая принципы DevOps и delivery"}, {"front": "Accelerate", "back": "Научное исследование Forsgren, Humble, Kim о факторах высокопроизводительных команд"}, {"front": "Поток (Flow)", "back": "Непрерывное движение задач от идеи до production без блокеров"}]},
                ],
            },
            {
                "t": "Delivery Manager vs другие роли",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "DM vs PM vs Scrum Master vs EM", "markdown": "## Delivery Manager vs другие роли\n\nВ командах часто путают роли. Разберём ключевые отличия.\n\n### Матрица ответственности:\n\n| Роль | Фокус | Отвечает за |\n|------|-------|-------------|\n| **DM** | КАК поставляем | Процессы, поток, предсказуемость |\n| **PM** | ЧТО и ЗАЧЕМ | Приоритеты, roadmap, ценность |\n| **Scrum Master** | Agile-процессы | Церемонии, ретро, блокеры команды |\n| **EM (Engineering Manager)** | Люди | Рост, найм, техническое качество |\n\n### Delivery Manager — это не:\n- ❌ Менеджер проекта (Project Manager)\n- ❌ Scrum Master (хотя пересечения есть)\n- ❌ Технический лид\n\n### Delivery Manager — это:\n- ✅ Системный мыслитель\n- ✅ Фасилитатор улучшений\n- ✅ Хранитель предсказуемости\n\n### В небольших компаниях:\nОдин человек часто совмещает роли DM + Scrum Master или DM + EM."},
                    {"type": "matching", "pairs": [{"left": "Delivery Manager", "right": "Как поставляем — процессы и поток"}, {"left": "Product Manager", "right": "Что и зачем — приоритеты и ценность"}, {"left": "Scrum Master", "right": "Agile-церемонии и блокеры команды"}, {"left": "Engineering Manager", "right": "Рост людей и техническое качество"}]},
                    {"type": "quiz", "question": "За что прежде всего отвечает Delivery Manager?", "options": [{"id": "a", "text": "Приоритизацию продуктового бэклога", "correct": False}, {"id": "b", "text": "Найм и профессиональный рост инженеров", "correct": False}, {"id": "c", "text": "Предсказуемость и эффективность процессов поставки", "correct": True}, {"id": "d", "text": "Написание технических спецификаций", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Delivery Manager", "items": ["Устранение блокеров в процессах", "Метрики потока", "Предсказуемость поставок"]}, {"name": "Product Manager", "items": ["Приоритизация бэклога", "Roadmap продукта", "Метрики ценности для пользователей"]}]},
                ],
            },
            {
                "t": "Delivery Lifecycle",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "От идеи до production", "markdown": "## Delivery Lifecycle — жизненный цикл поставки\n\nКаждая фича проходит через предсказуемый цикл от идеи до работающего продукта.\n\n### Этапы Delivery Lifecycle:\n\n1. **Discovery** — исследование проблемы и решения\n2. **Design** — проектирование UX и технической архитектуры\n3. **Development** — реализация\n4. **Testing** — QA, автоматические тесты\n5. **Staging** — финальная проверка в pre-production среде\n6. **Release** — деплой в production\n7. **Monitor** — мониторинг и сбор обратной связи\n\n### Definition of Done (DoD):\nСписок критериев, при выполнении которых задача считается завершённой.\n\n**Пример DoD:**\n- Код написан и прошёл code review\n- Unit и integration тесты написаны и проходят\n- Документация обновлена\n- QA проверил функциональность\n- Deployed to production и мониторинг настроен\n\n### Почему DoD важен:\nБез единого понимания «готово» каждый член команды понимает завершённость по-своему."},
                    {"type": "drag-order", "items": ["Discovery — исследование проблемы", "Design — проектирование решения", "Development — реализация", "Testing — контроль качества", "Staging — финальная проверка", "Release — деплой в production", "Monitor — мониторинг"]},
                    {"type": "quiz", "question": "Что такое Definition of Done?", "options": [{"id": "a", "text": "Список всех задач в бэклоге", "correct": False}, {"id": "b", "text": "Критерии, при выполнении которых задача считается завершённой", "correct": True}, {"id": "c", "text": "Техническое задание на фичу", "correct": False}, {"id": "d", "text": "Дата релиза продукта", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Список критериев завершённости задачи называется Definition of ___.", "answer": "Done"},
                    {"type": "true-false", "statement": "Definition of Done помогает всей команде одинаково понимать, что значит «задача выполнена».", "correct": True},
                ],
            },
            {
                "t": "Культура доставки",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Shift Left, Fail Fast, Continuous Delivery", "markdown": "## Культура доставки\n\nТехнические практики работают только при правильной культуре. Три ключевых принципа:\n\n### Shift Left — смещение влево\nОбнаруживать проблемы как можно раньше в цикле.\n- ❌ Тестирование только перед релизом\n- ✅ Тесты на каждом коммите, security review при проектировании\n\n### Fail Fast — быстро обнаруживать ошибки\nЛучше узнать о проблеме через 5 минут, чем через 5 дней.\n- Быстрые CI-пайплайны\n- Canary deployments с автоматическим откатом\n\n### Continuous Delivery Mindset\nПо книге **\"Continuous Delivery\"** (Humble & Farley):\n- Программный продукт **всегда** должен быть готов к деплою\n- Маленькие частые релизы безопаснее редких больших\n- Деплой — это рутина, а не событие\n\n### Психологическая безопасность:\nГугловое исследование Project Aristotle показало: **психологическая безопасность** — главный фактор эффективности команды. Люди должны не бояться ошибаться и говорить открыто."},
                    {"type": "quiz", "question": "Что означает принцип Shift Left в delivery?", "options": [{"id": "a", "text": "Переносить релизы на более ранние даты", "correct": False}, {"id": "b", "text": "Обнаруживать проблемы как можно раньше в цикле разработки", "correct": True}, {"id": "c", "text": "Делегировать задачи джуниорам", "correct": False}, {"id": "d", "text": "Уменьшать команду разработки", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Shift Left", "right": "Проблемы обнаруживаются как можно раньше"}, {"left": "Fail Fast", "right": "Быстро выявлять и исправлять ошибки"}, {"left": "Continuous Delivery", "right": "Продукт всегда готов к деплою"}, {"left": "Психологическая безопасность", "right": "Команда не боится ошибаться и говорить открыто"}]},
                    {"type": "true-false", "statement": "По принципу Continuous Delivery, деплой должен быть редким и значимым событием.", "correct": False},
                ],
            },
            {
                "t": "DORA метрики",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Четыре ключевые метрики delivery", "markdown": "## DORA Metrics\n\n**DORA** (DevOps Research and Assessment) — четыре метрики, которые по исследованиям книги **\"Accelerate\"** наилучшим образом предсказывают производительность команды.\n\n### 4 DORA метрики:\n\n**1. Deployment Frequency (Частота деплоев)**\nКак часто команда успешно деплоит в production.\n- Elite: несколько раз в день\n- High: раз в неделю — раз в месяц\n\n**2. Lead Time for Changes (Время от коммита до production)**\nСколько времени проходит от коммита кода до его работы в production.\n- Elite: менее 1 часа\n- High: 1 день — 1 неделя\n\n**3. MTTR (Mean Time to Restore)**\nСреднее время восстановления после инцидента.\n- Elite: менее 1 часа\n- High: менее 1 дня\n\n**4. Change Failure Rate (Процент неудачных изменений)**\nКакой процент деплоев приводит к инцидентам.\n- Elite: 0–15%\n- High: 16–30%\n\n### Ключевой вывод:\nВысокая частота + маленький Lead Time = **меньше рисков**, не больше."},
                    {"type": "matching", "pairs": [{"left": "Deployment Frequency", "right": "Как часто деплоим в production"}, {"left": "Lead Time for Changes", "right": "Время от коммита до production"}, {"left": "MTTR", "right": "Среднее время восстановления после инцидента"}, {"left": "Change Failure Rate", "right": "Процент деплоев, вызвавших инциденты"}]},
                    {"type": "quiz", "question": "Какой DORA-показатель для elite-команд при Lead Time for Changes?", "options": [{"id": "a", "text": "Менее 1 минуты", "correct": False}, {"id": "b", "text": "Менее 1 часа", "correct": True}, {"id": "c", "text": "Менее 1 дня", "correct": False}, {"id": "d", "text": "Менее 1 недели", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "DORA", "back": "DevOps Research and Assessment — 4 метрики производительности delivery-команды"}, {"front": "Deployment Frequency", "back": "Частота успешных деплоев в production"}, {"front": "Lead Time for Changes", "back": "Время от коммита кода до его работы в production"}, {"front": "MTTR", "back": "Mean Time to Restore — среднее время восстановления после инцидента"}, {"front": "Change Failure Rate", "back": "Доля деплоев, которые привели к инцидентам"}]},
                    {"type": "true-false", "statement": "По данным исследования Accelerate, высокая частота деплоев ведёт к большему числу инцидентов.", "correct": False},
                ],
            },
            {
                "t": "Ресурсы: Основы DM",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "Accelerate — книга (Goodreads)", "url": "https://www.goodreads.com/book/show/35747076-accelerate", "type": "link"},
                            {"label": "The Phoenix Project — книга", "url": "https://www.goodreads.com/book/show/17255186-the-phoenix-project", "type": "link"},
                            {"label": "DORA Metrics — официальный сайт", "url": "https://dora.dev", "type": "link"},
                            {"label": "What is a Delivery Manager? — Atlassian", "url": "https://www.atlassian.com/agile/project-management/delivery-manager", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 2: Agile и Kanban на практике =====
    {
        "title": "Agile и Kanban на практике",
        "pos": 1,
        "lessons": [
            {
                "t": "Scrum для delivery",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Спринты и церемонии в контексте delivery", "markdown": "## Scrum для Delivery Manager\n\n**Scrum** — фреймворк итеративной разработки, популярный во многих командах.\n\n### Ключевые церемонии:\n- **Sprint Planning** — команда берёт задачи из бэклога\n- **Daily Standup** — 15-минутная синхронизация\n- **Sprint Review** — демо результатов стейкхолдерам\n- **Sprint Retrospective** — улучшение процессов\n\n### Когда Scrum работает хорошо:\n- Требования меняются часто\n- Команда небольшая (5–9 человек)\n- Product Owner активно вовлечён\n- Работа хорошо делится на недельные итерации\n\n### Когда Scrum работает плохо:\n- Работа не делится на спринты (операционка, поддержка)\n- Product Owner недоступен\n- Команда распределена и не синхронизирована\n- Частые внешние прерывания нарушают спринты\n\n### Роль DM в Scrum:\nDM помогает команде соблюдать процесс, убирает системные блокеры и следит за метриками потока."},
                    {"type": "quiz", "question": "В каком случае Scrum подходит меньше всего?", "options": [{"id": "a", "text": "Команда небольшая, требования часто меняются", "correct": False}, {"id": "b", "text": "Product Owner активно вовлечён и доступен", "correct": False}, {"id": "c", "text": "Работа — это постоянная операционная поддержка с непредсказуемыми задачами", "correct": True}, {"id": "d", "text": "Новый продукт в стадии активной разработки", "correct": False}]},
                    {"type": "drag-order", "items": ["Sprint Planning — планирование задач на спринт", "Daily Standup — ежедневная синхронизация", "Работа над задачами в течение спринта", "Sprint Review — демо результатов", "Sprint Retrospective — улучшение процессов"]},
                    {"type": "true-false", "statement": "Delivery Manager в Scrum-команде несёт ответственность за устранение системных блокеров и метрики потока.", "correct": True},
                ],
            },
            {
                "t": "Kanban — поток вместо спринтов",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "WIP-лимиты и pull system", "markdown": "## Kanban для Delivery\n\nПо книге **\"Kanban\"** (David Anderson), Kanban — метод управления потоком работы через визуализацию и ограничение незавершённой работы.\n\n### Ключевые принципы:\n1. **Визуализируй работу** — всё на доске\n2. **Ограничь WIP** — Work In Progress не должен быть бесконечным\n3. **Управляй потоком** — задачи должны двигаться без остановок\n4. **Явные политики** — правила перехода между столбцами\n5. **Улучшай совместно** — команда принимает решения об изменениях\n\n### Pull System (вытягивание):\n- ❌ Push: менеджер раздаёт задачи\n- ✅ Pull: разработчик сам берёт следующую задачу, когда освобождается\n\n### WIP-лимиты:\nОграничение числа задач в каждом столбце.\n- Без лимита: все заняты, ничего не готово\n- С лимитом: задачи реально заканчиваются\n\n### «Остановись, чтобы двигаться быстрее»:\nКогда WIP-лимит нарушен — нужно помочь завершить текущее, а не брать новое."},
                    {"type": "quiz", "question": "Что такое Pull System в Kanban?", "options": [{"id": "a", "text": "Менеджер распределяет задачи по разработчикам", "correct": False}, {"id": "b", "text": "Разработчик сам берёт следующую задачу, когда освобождается", "correct": True}, {"id": "c", "text": "Задачи автоматически перемещаются по доске", "correct": False}, {"id": "d", "text": "Только senior-разработчики выбирают задачи", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "WIP-лимит", "right": "Ограничение числа задач одновременно в работе"}, {"left": "Pull System", "right": "Разработчик сам берёт задачу, когда готов"}, {"left": "Визуализация", "right": "Все задачи видны на доске"}, {"left": "Явные политики", "right": "Чёткие правила перехода задачи между столбцами"}]},
                    {"type": "true-false", "statement": "При нарушении WIP-лимита нужно срочно взять новые задачи, чтобы ускорить работу.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Kanban (книга)", "back": "David Anderson — метод управления потоком через визуализацию и WIP-лимиты"}, {"front": "WIP", "back": "Work In Progress — незавершённая работа, которую нужно ограничивать"}, {"front": "Pull System", "back": "Вытягивание: исполнитель сам берёт задачу при наличии пропускной способности"}, {"front": "Flow Efficiency", "back": "Доля активного времени работы над задачей к общему времени её выполнения"}]},
                ],
            },
            {
                "t": "Метрики потока",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Cycle Time, Throughput, CFD", "markdown": "## Метрики потока (Flow Metrics)\n\nДля управления delivery нужны конкретные измеримые показатели.\n\n### Cycle Time (Время цикла)\nВремя от начала работы над задачей до её завершения.\n- Измеряется в днях\n- Цель: уменьшать и делать предсказуемым\n\n### Lead Time (Время выполнения)\nВремя от создания задачи до её завершения (включая ожидание).\n- Lead Time ≥ Cycle Time\n\n### Throughput (Пропускная способность)\nКоличество задач, завершаемых за единицу времени (например, задач в неделю).\n- Не путать со скоростью в story points!\n\n### Flow Efficiency\n```\nFlow Efficiency = Active Time / Lead Time × 100%\n```\nТипично: 10–30%. Если выше 40% — отличный результат.\n\n### CFD (Cumulative Flow Diagram)\nГрафик, показывающий накопление задач в каждом состоянии со временем.\n- Параллельные полосы → стабильный поток\n- Расширяющаяся полоса → накопление незавершённой работы"},
                    {"type": "matching", "pairs": [{"left": "Cycle Time", "right": "Время от начала работы до завершения"}, {"left": "Lead Time", "right": "Время от создания задачи до завершения"}, {"left": "Throughput", "right": "Число задач, завершённых за период"}, {"left": "CFD", "right": "Cumulative Flow Diagram — накопление задач по состояниям"}]},
                    {"type": "quiz", "question": "Что такое Flow Efficiency?", "options": [{"id": "a", "text": "Количество story points за спринт", "correct": False}, {"id": "b", "text": "Доля активного времени работы над задачей к общему Lead Time", "correct": True}, {"id": "c", "text": "Число задач в колонке In Progress", "correct": False}, {"id": "d", "text": "Разница между Lead Time и Cycle Time", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Число задач, завершаемых командой за неделю — это метрика ___.", "answer": "Throughput"},
                ],
            },
            {
                "t": "Планирование поставок",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Capacity Planning и Estimation", "markdown": "## Планирование поставок\n\n### Capacity Planning (Планирование ёмкости)\nОпределение реального объёма работы, который команда может выполнить за период.\n\n**Формула:**\n```\nCapacity = (Дни в спринте) × (Команда) × (Фокус-фактор)\n```\nФокус-фактор обычно 0.7–0.8 (встречи, отпуска, задержки).\n\n### Velocity (Скорость)\nСредняя скорость команды — сколько story points завершается за спринт.\n- Не сравнивайте скорость разных команд!\n- Используйте для планирования, а не оценки продуктивности\n\n### Estimation (Оценка)\nПопулярные подходы:\n- **Story Points** — относительная оценка сложности\n- **T-shirt sizes** (S, M, L, XL) — грубая оценка\n- **#NoEstimates** — фокус на throughput, а не на точные оценки\n\n### Канбан-подход к планированию:\nВместо оценки задач — разбивайте работу на задачи одинакового размера (roughly equal sizing) и прогнозируйте по историческому throughput."},
                    {"type": "quiz", "question": "Для чего используется Velocity (скорость) в Scrum?", "options": [{"id": "a", "text": "Для сравнения производительности разных команд", "correct": False}, {"id": "b", "text": "Для планирования объёма работы в будущих спринтах", "correct": True}, {"id": "c", "text": "Для оценки зарплаты разработчиков", "correct": False}, {"id": "d", "text": "Для выбора технологического стека", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Scrum-подход к планированию", "items": ["Story Points", "Velocity", "Sprint Planning"]}, {"name": "Kanban-подход к планированию", "items": ["Исторический Throughput", "Equally-sized задачи", "Вероятностное прогнозирование"]}]},
                    {"type": "true-false", "statement": "Фокус-фактор при расчёте capacity обычно составляет 100%, так как команда работает полный день.", "correct": False},
                ],
            },
            {
                "t": "Ретроспективы",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Фасилитация ретроспектив", "markdown": "## Ретроспективы\n\n**Ретроспектива** — регулярная встреча команды для анализа процессов и поиска улучшений.\n\n### Форматы ретроспектив:\n\n**Start/Stop/Continue:**\n- Start: что начать делать?\n- Stop: что прекратить?\n- Continue: что продолжить?\n\n**4L's:**\n- Liked (понравилось)\n- Learned (узнали)\n- Lacked (не хватало)\n- Longed For (хотели бы)\n\n**Sailboat:**\n- Паруса (что помогает двигаться вперёд?)\n- Якоря (что тормозит?)\n- Ветер (внешние факторы)\n- Рифы (риски впереди)\n\n### Правила фасилитации:\n1. Создайте **психологическую безопасность**\n2. Фокус на **системе**, а не на людях\n3. Выбирайте **максимум 2–3 action items**\n4. Проверяйте выполнение предыдущих ретро\n\n### Антипаттерн:\nРетроспектива без action items — бесполезная жалобная сессия."},
                    {"type": "matching", "pairs": [{"left": "Start/Stop/Continue", "right": "Три категории: начать, прекратить, продолжить"}, {"left": "4L's", "right": "Liked, Learned, Lacked, Longed For"}, {"left": "Sailboat", "right": "Паруса, якоря, ветер, рифы"}, {"left": "Action Items", "right": "Конкретные улучшения с ответственным и сроком"}]},
                    {"type": "quiz", "question": "Что является антипаттерном ретроспективы?", "options": [{"id": "a", "text": "Выбирать 2–3 action items", "correct": False}, {"id": "b", "text": "Ретроспектива заканчивается без конкретных улучшений", "correct": True}, {"id": "c", "text": "Использовать разные форматы", "correct": False}, {"id": "d", "text": "Проверять выполнение предыдущих action items", "correct": False}]},
                    {"type": "multi-select", "question": "Какие форматы ретроспектив перечислены в уроке?", "options": [{"id": "a", "text": "Start/Stop/Continue", "correct": True}, {"id": "b", "text": "RICE", "correct": False}, {"id": "c", "text": "4L's", "correct": True}, {"id": "d", "text": "Sailboat", "correct": True}, {"id": "e", "text": "MoSCoW", "correct": False}]},
                ],
            },
            {
                "t": "Ресурсы: Agile и Kanban",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "Kanban — David Anderson (книга)", "url": "https://www.goodreads.com/book/show/8086552-kanban", "type": "link"},
                            {"label": "Scrum Guide — официальный", "url": "https://scrumguides.org", "type": "link"},
                            {"label": "Atlassian — Kanban Guide", "url": "https://www.atlassian.com/agile/kanban", "type": "link"},
                            {"label": "Retrospective Formats — FunRetrospectives", "url": "https://www.funretrospectives.com", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 3: Управление рисками =====
    {
        "title": "Управление рисками",
        "pos": 2,
        "lessons": [
            {
                "t": "Идентификация рисков",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "RAID Log, Risk Matrix, Pre-mortem", "markdown": "## Идентификация и управление рисками\n\n### RAID Log\nРаспространённый инструмент управления рисками:\n- **R** — Risks (риски)\n- **A** — Assumptions (допущения)\n- **I** — Issues (текущие проблемы)\n- **D** — Dependencies (зависимости)\n\n### Risk Matrix (Матрица рисков)\nОценка рисков по двум осям:\n- **Вероятность** (Probability): 1–5\n- **Влияние** (Impact): 1–5\n- **Risk Score** = Probability × Impact\n\n### Pre-mortem\nТехника, предложенная психологом Гэри Кляйном:\n«Представьте, что проект провалился. Что пошло не так?»\n\n**Процесс:**\n1. Команда воображает провал проекта\n2. Каждый пишет причины\n3. Список обсуждается и используется для планирования\n\n### Почему Pre-mortem работает:\n- Снимает оптимизм-bias\n- Люди честнее говорят о рисках\n- Создаёт психологическую безопасность («мы всё предусмотрели»)"},
                    {"type": "matching", "pairs": [{"left": "RAID", "right": "Risks, Assumptions, Issues, Dependencies"}, {"left": "Risk Matrix", "right": "Вероятность × Влияние"}, {"left": "Pre-mortem", "right": "«Проект провалился — что пошло не так?»"}, {"left": "Risk Score", "right": "Probability × Impact"}]},
                    {"type": "quiz", "question": "Что такое Pre-mortem?", "options": [{"id": "a", "text": "Анализ провала проекта после его завершения", "correct": False}, {"id": "b", "text": "Техника, где команда заранее воображает провал и ищет причины", "correct": True}, {"id": "c", "text": "Ежедневный мониторинг рисков", "correct": False}, {"id": "d", "text": "Технический аудит кода перед релизом", "correct": False}]},
                    {"type": "fill-blank", "sentence": "В RAID Log буква D означает ___.", "answer": "Dependencies"},
                ],
            },
            {
                "t": "Управление зависимостями",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Dependency Mapping и Critical Path", "markdown": "## Управление зависимостями\n\nЗависимости — одна из главных причин задержек в delivery.\n\n### Типы зависимостей:\n- **Internal** — внутри команды (задача B зависит от задачи A)\n- **External** — от другой команды или системы\n- **Technical** — библиотека, API, инфраструктура\n- **Regulatory** — юридические или compliance-требования\n\n### Dependency Mapping:\nВизуализация связей между задачами, командами и системами.\n- Помогает найти критические зависимости\n- Строится как граф или матрица\n\n### Critical Path (Критический путь):\nСамая длинная цепочка зависимых задач в проекте. Задержка любой задачи на критическом пути задерживает весь проект.\n\n```\nA(3д) → B(2д) → D(4д) = 9 дней (критический путь)\n       C(5д) ─────────────────┘\n       C тоже влияет, но через другую ветку\n```\n\n### Стратегии:\n- Декомпозировать зависимости\n- Параллелить независимые потоки\n- Формализовать API-контракты между командами заранее"},
                    {"type": "quiz", "question": "Что такое Critical Path?", "options": [{"id": "a", "text": "Самая короткая задача в проекте", "correct": False}, {"id": "b", "text": "Самая длинная цепочка зависимых задач, определяющая минимальный срок", "correct": True}, {"id": "c", "text": "Список рисков проекта", "correct": False}, {"id": "d", "text": "Дорогостоящие задачи, требующие одобрения", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Внутренние зависимости", "items": ["Задача B зависит от задачи A в команде", "Backend-API нужен фронтенду"]}, {"name": "Внешние зависимости", "items": ["Другая команда должна поставить компонент", "Платёжный провайдер должен открыть API"]}, {"name": "Регуляторные зависимости", "items": ["Нужно получить compliance-одобрение", "Юридическая проверка документов"]}]},
                    {"type": "true-false", "statement": "Задержка задачи на критическом пути обязательно задерживает весь проект.", "correct": True},
                ],
            },
            {
                "t": "Технический долг",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Tech Debt Quadrant и бюджет", "markdown": "## Технический долг\n\n**Технический долг** (по Мартину Фаулеру) — метафора для кода и архитектурных решений, которые сейчас «удобны», но создают сложности в будущем.\n\n### Tech Debt Quadrant (Фаулер):\n\n|  | Обдуманный | Необдуманный |\n|--|-----------|-------------|\n| **Намеренный** | «Мы знаем, это проблема, задокументировали» | «Некогда делать правильно» |\n| **Случайный** | «Теперь понимаем лучший подход» | «Что такое слои?» |\n\n### Четыре квадранта:\n1. **Prudent + Deliberate** — осознанный выбор быстрого решения с планом рефакторинга\n2. **Reckless + Deliberate** — «нет времени на дизайн», накапливает долг\n3. **Prudent + Inadvertent** — узнали лучший подход в процессе\n4. **Reckless + Inadvertent** — незнание лучших практик\n\n### Управление Tech Debt:\n- Выделяйте **бюджет** — 20% спринта на tech debt\n- Ведите **debt backlog** — список с приоритетами\n- Связывайте долг с **бизнес-болью** (замедляет новые фичи)\n\n### Главная опасность:\nИгнорируемый tech debt накапливается и в итоге полностью останавливает delivery."},
                    {"type": "quiz", "question": "Что означает «Prudent + Deliberate» в квадранте техдолга Фаулера?", "options": [{"id": "a", "text": "Команда не знает лучших практик", "correct": False}, {"id": "b", "text": "Осознанный выбор быстрого решения с пониманием последствий и планом рефакторинга", "correct": True}, {"id": "c", "text": "Случайно созданный долг из-за ошибок", "correct": False}, {"id": "d", "text": "Игнорирование всех архитектурных проблем", "correct": False}]},
                    {"type": "true-false", "statement": "Хорошая практика — выделять около 20% времени спринта на работу с техдолгом.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Технический долг", "back": "Накопленные архитектурные и кодовые компромиссы, затрудняющие будущие изменения"}, {"front": "Tech Debt Quadrant", "back": "Фреймворк Мартина Фаулера: Prudent/Reckless × Deliberate/Inadvertent"}, {"front": "Debt Backlog", "back": "Список технических задач по устранению долга с приоритизацией"}, {"front": "Reckless Debt", "back": "Техдолг, накапливаемый из-за небрежности или незнания лучших практик"}]},
                ],
            },
            {
                "t": "Кризисный менеджмент",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Incidents, Post-mortem, Blameless Culture", "markdown": "## Кризисный менеджмент в Delivery\n\n### Incident Management (Управление инцидентами)\n\n**Severity levels:**\n- **SEV1** — production полностью недоступен\n- **SEV2** — критическая функциональность нарушена\n- **SEV3** — неудобство без полного отказа\n\n**Процесс инцидента:**\n1. Обнаружение и алертинг\n2. Назначение Incident Commander\n3. Диагностика и восстановление\n4. Коммуникация стейкхолдерам\n5. Post-mortem\n\n### Post-mortem\nДокумент разбора инцидента. Включает:\n- Временная шкала событий\n- Root Cause Analysis\n- Что пошло хорошо\n- Action items для предотвращения повторения\n\n### Blameless Culture (Культура без обвинений)\nПринцип из книги **\"The Phoenix Project\"**:\n- Инциденты — это системные проблемы, а не ошибки людей\n- Цель: понять систему, а не наказать виновного\n- Открытость приводит к более глубокому анализу\n\n### Почему это важно:\nКоманды, боящиеся наказания, скрывают инциденты, что делает систему опаснее."},
                    {"type": "drag-order", "items": ["Обнаружение инцидента и алертинг", "Назначение Incident Commander", "Диагностика и восстановление сервиса", "Коммуникация стейкхолдерам", "Post-mortem — разбор и action items"]},
                    {"type": "quiz", "question": "Что означает Blameless Culture в контексте инцидентов?", "options": [{"id": "a", "text": "Никто никогда не несёт ответственности за ошибки", "correct": False}, {"id": "b", "text": "Инциденты рассматриваются как системные проблемы, а не вина конкретных людей", "correct": True}, {"id": "c", "text": "Post-mortem проводится анонимно", "correct": False}, {"id": "d", "text": "Только менеджеры анализируют инциденты", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "SEV1", "right": "Production полностью недоступен"}, {"left": "SEV2", "right": "Критическая функциональность нарушена"}, {"left": "Post-mortem", "back": "Разбор инцидента с root cause и action items"}, {"left": "Blameless Culture", "right": "Фокус на системе, а не на поиске виноватых"}]},
                ],
            },
            {
                "t": "Ресурсы: Управление рисками",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "RAID Log Template — Atlassian", "url": "https://www.atlassian.com/software/confluence/templates/raid-log", "type": "link"},
                            {"label": "Martin Fowler — Technical Debt", "url": "https://martinfowler.com/bliki/TechnicalDebt.html", "type": "link"},
                            {"label": "Blameless Post-Mortems — Etsy", "url": "https://www.etsy.com/codeascraft/blameless-postmortems", "type": "link"},
                            {"label": "Pre-mortem — HBR", "url": "https://hbr.org/2007/09/performing-a-project-premortem", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 4: Работа со стейкхолдерами =====
    {
        "title": "Работа со стейкхолдерами",
        "pos": 3,
        "lessons": [
            {
                "t": "Стейкхолдер-менеджмент",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Mapping и Power/Interest Grid", "markdown": "## Стейкхолдер-менеджмент\n\n**Стейкхолдер** — любой человек или группа, влияющая на проект или зависящая от его результатов.\n\n### Power/Interest Grid (Матрица власть/интерес):\n\n```\n        Высокая власть\n   ┌──────────────────────────┐\n   │   Управляй    │  Тесно   │\n   │   активно     │ работай  │\n   ├───────────────┼──────────┤\n   │   Держи в     │  Держи   │\n   │   курсе       │ доволен  │\n   └──────────────────────────┘\n        Низкий интерес → Высокий интерес\n```\n\n### Четыре стратегии:\n- **Manage Closely** — высокая власть, высокий интерес (C-level, ключевые PM)\n- **Keep Satisfied** — высокая власть, низкий интерес (CFO, Legal)\n- **Keep Informed** — низкая власть, высокий интерес (команды, пользователи)\n- **Monitor** — низкая власть, низкий интерес\n\n### Stakeholder Mapping:\n1. Составьте список всех стейкхолдеров\n2. Оцените их влияние и интерес\n3. Определите стратегию коммуникации\n4. Обновляйте регулярно — статусы меняются"},
                    {"type": "matching", "pairs": [{"left": "Manage Closely", "right": "Высокая власть + высокий интерес"}, {"left": "Keep Satisfied", "right": "Высокая власть + низкий интерес"}, {"left": "Keep Informed", "right": "Низкая власть + высокий интерес"}, {"left": "Monitor", "right": "Низкая власть + низкий интерес"}]},
                    {"type": "quiz", "question": "Какую стратегию применять к CEO компании с высокой властью и низким интересом к деталям проекта?", "options": [{"id": "a", "text": "Monitor — редко обновлять", "correct": False}, {"id": "b", "text": "Keep Informed — часто детальные отчёты", "correct": False}, {"id": "c", "text": "Keep Satisfied — кратко держать в курсе ключевых решений", "correct": True}, {"id": "d", "text": "Manage Closely — еженедельные встречи", "correct": False}]},
                    {"type": "true-false", "statement": "Список стейкхолдеров нужно составить один раз в начале проекта и не менять.", "correct": False},
                ],
            },
            {
                "t": "Отчётность и прозрачность",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Status Reports и Dashboards", "markdown": "## Отчётность и прозрачность в Delivery\n\n### Принцип прозрачности:\nСтейкхолдеры не должны узнавать о проблемах последними.\n«Плохие новости не становятся лучше со временем.»\n\n### Форматы отчётности:\n\n**Status Report (Отчёт о статусе):**\n- RAG-статус: Red / Amber / Green\n- Прогресс за период\n- Риски и блокеры\n- Планы на следующий период\n\n**Delivery Dashboard (Дашборд):**\n- DORA метрики в реальном времени\n- Cycle time и throughput\n- Открытые инциденты\n- Прогресс по milestone'ам\n\n### RAG-статус:\n- **Green** — всё идёт по плану\n- **Amber** — есть риски, требует внимания\n- **Red** — критическая проблема, нужна помощь\n\n### Правило подготовки отчётов:\n- Данные говорят сами за себя — не приукрашивайте\n- Amber лучше скрытого Red\n- Предлагайте варианты решений, а не только проблемы"},
                    {"type": "quiz", "question": "Что означает Amber в RAG-статусе?", "options": [{"id": "a", "text": "Всё идёт по плану", "correct": False}, {"id": "b", "text": "Критическая проблема, требующая немедленного вмешательства", "correct": False}, {"id": "c", "text": "Есть риски, требующие внимания, но критической угрозы нет", "correct": True}, {"id": "d", "text": "Проект завершён", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "RAG статус", "right": "Red / Amber / Green — цветовой индикатор здоровья"}, {"left": "Status Report", "right": "Периодический отчёт о прогрессе, рисках и планах"}, {"left": "Delivery Dashboard", "right": "Реальновременные метрики потока и качества"}, {"left": "Принцип прозрачности", "right": "Плохие новости не улучшаются от молчания"}]},
                    {"type": "true-false", "statement": "Amber-статус лучше скрытого Red, потому что честность позволяет вовремя принять меры.", "correct": True},
                ],
            },
            {
                "t": "Управление ожиданиями",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Scope Negotiation и Trade-off Triangle", "markdown": "## Управление ожиданиями\n\n### Trade-off Triangle (Треугольник ограничений)\nКлассическая модель управления проектами:\n\n```\n         Scope\n          /\\\n         /  \\\n        /    \\\n       /______\\\n    Time      Cost\n```\n\n«Быстро, дёшево, качественно — выбери два.»\n\n### В Agile — обратный подход:\n- **Фиксируем**: Time + Cost\n- **Варьируем**: Scope\n\nЭто позволяет команде фокусироваться на наиболее важных вещах в рамках реального бюджета.\n\n### Scope Negotiation:\nОбсуждение того, что войдёт в поставку:\n1. Определите **обязательные** требования (Must)\n2. Определите **желательные** (Should/Could)\n3. Честно оцените capacity\n4. Зафиксируйте договорённости письменно\n\n### Управление ожиданиями:\n- Обещайте **меньше**, делайте **больше**\n- Регулярно обновляйте прогноз\n- Предупреждайте об изменениях **заранее**\n- Никогда не «прячьте» плохие новости"},
                    {"type": "quiz", "question": "Что фиксируется в Agile-подходе к треугольнику ограничений?", "options": [{"id": "a", "text": "Scope и Quality", "correct": False}, {"id": "b", "text": "Time и Cost", "correct": True}, {"id": "c", "text": "Только Scope", "correct": False}, {"id": "d", "text": "Quality и Time", "correct": False}]},
                    {"type": "true-false", "statement": "Хорошая практика — обещать меньше и делать больше, а не наоборот.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Trade-off Triangle", "back": "Scope / Time / Cost — нельзя оптимизировать все три одновременно"}, {"front": "Scope Negotiation", "back": "Обсуждение с стейкхолдерами того, что войдёт в поставку в рамках ограничений"}, {"front": "Under-promise, over-deliver", "back": "Принцип: обещать меньше, делать больше — управляет ожиданиями"}]},
                ],
            },
            {
                "t": "Фасилитация встреч",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Timeboxing и Decision Frameworks", "markdown": "## Фасилитация встреч\n\n### Проблема неэффективных встреч:\n- Нет цели и повестки\n- Нет владельца\n- Нет решений и action items\n- Слишком много участников\n\n### Timeboxing:\nОграничение времени на каждый пункт повестки.\n- Daily standup: **15 минут строго**\n- Sprint Planning: **4 часа на 2-недельный спринт**\n- Retrospective: **1.5 часа**\n\n### Правила хорошей встречи:\n1. **Цель** — зачем мы собираемся?\n2. **Повестка** — отправить заранее\n3. **Право вето** — если нет роли, можно отказаться\n4. **Решения** — фиксируются письменно\n5. **Action items** — ответственный + срок\n\n### Decision Frameworks:\n- **DACI**: Driver, Approver, Contributor, Informed\n- **RACI**: Responsible, Accountable, Consulted, Informed\n- **Dot voting** — быстрое голосование за приоритеты\n- **Decider protocol** — «да/нет/да с условием»"},
                    {"type": "matching", "pairs": [{"left": "Timeboxing", "right": "Ограничение времени на каждый пункт повестки"}, {"left": "DACI", "right": "Driver, Approver, Contributor, Informed"}, {"left": "RACI", "right": "Responsible, Accountable, Consulted, Informed"}, {"left": "Action Items", "right": "Решения с ответственным и дедлайном"}]},
                    {"type": "quiz", "question": "Сколько времени по стандарту Scrum занимает Daily Standup?", "options": [{"id": "a", "text": "5 минут", "correct": False}, {"id": "b", "text": "15 минут", "correct": True}, {"id": "c", "text": "30 минут", "correct": False}, {"id": "d", "text": "1 час", "correct": False}]},
                    {"type": "multi-select", "question": "Какие элементы делают встречу эффективной?", "options": [{"id": "a", "text": "Чёткая цель встречи", "correct": True}, {"id": "b", "text": "Максимальное число участников", "correct": False}, {"id": "c", "text": "Повестка, отправленная заранее", "correct": True}, {"id": "d", "text": "Action items с ответственным и сроком", "correct": True}, {"id": "e", "text": "Встреча без конкретных решений", "correct": False}]},
                ],
            },
            {
                "t": "Ресурсы: Стейкхолдеры",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "Stakeholder Mapping — MindTools", "url": "https://www.mindtools.com/aol0rms/stakeholder-analysis", "type": "link"},
                            {"label": "RACI Matrix Guide — ProjectManager", "url": "https://www.projectmanager.com/blog/raci-chart-definition", "type": "link"},
                            {"label": "How to Run Better Meetings — HBR", "url": "https://hbr.org/2017/07/stop-the-meeting-madness", "type": "link"},
                            {"label": "Decision Making Frameworks — Untools", "url": "https://untools.co", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 5: Масштабирование =====
    {
        "title": "Масштабирование",
        "pos": 4,
        "lessons": [
            {
                "t": "Delivery в масштабе",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "SAFe, LeSS, Nexus", "markdown": "## Delivery в масштабе\n\nКогда над одним продуктом работают несколько команд, нужны фреймворки масштабирования.\n\n### SAFe (Scaled Agile Framework)\nСамый популярный корпоративный фреймворк.\n- Уровни: Team → Program → Large Solution → Portfolio\n- PI Planning — ключевое событие синхронизации\n- Подходит для крупных организаций (100+ человек)\n- Критика: тяжёлый, бюрократичный, плохо масштабируется снизу вверх\n\n### LeSS (Large-Scale Scrum)\n- До 8 команд на одном product backlog\n- Минимум дополнительных ролей и артефактов\n- Один Product Owner для всех команд\n- Философия: «больше Scrum, меньше управления»\n\n### Nexus\n- Фреймворк от Scrum.org\n- 3–9 Scrum-команд\n- Nexus Integration Team — координирующая роль\n- Интегрированный инкремент каждый спринт\n\n### Как выбирать:\n- Стартап / малый масштаб → Scrum или Kanban\n- 3–9 команд → LeSS или Nexus\n- Крупная корпорация → SAFe"},
                    {"type": "matching", "pairs": [{"left": "SAFe", "right": "Корпоративный многоуровневый фреймворк с PI Planning"}, {"left": "LeSS", "right": "Один Product Owner и backlog для нескольких команд"}, {"left": "Nexus", "right": "3–9 Scrum-команд с Nexus Integration Team"}, {"left": "PI Planning", "right": "Ключевое событие синхронизации всех команд в SAFe"}]},
                    {"type": "quiz", "question": "Сколько команд может объединять фреймворк Nexus?", "options": [{"id": "a", "text": "2–4 команды", "correct": False}, {"id": "b", "text": "3–9 команд", "correct": True}, {"id": "c", "text": "10–50 команд", "correct": False}, {"id": "d", "text": "Любое количество", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "SAFe", "items": ["PI Planning", "Многоуровневая структура", "Portfolio management"]}, {"name": "LeSS", "items": ["Один Product Owner на все команды", "Один общий Product Backlog", "Минимум дополнительных ролей"]}]},
                ],
            },
            {
                "t": "Program-level planning",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "PI Planning и Big Room Planning", "markdown": "## Program-level Planning\n\n### PI Planning (Program Increment Planning)\nКлючевое событие в SAFe — синхронизация всех Agile-команд.\n\n**Формат:**\n- Обычно 2 дня, очно или гибридно\n- Все команды, PO, архитекторы, стейкхолдеры\n- Результат: PI Objectives + Team Iteration Plans\n\n**Повестка:**\n1. Business context — бизнес-цели и стратегия\n2. Product/Solution Vision — направление развития\n3. Team Breakout 1 — планирование командами\n4. Draft Plan Review — согласование\n5. Team Breakout 2 — доработка\n6. Final Plan Review + Risks — финальное согласование\n\n### Big Room Planning\nНеформальный аналог PI Planning для организаций без SAFe.\n- Раз в квартал\n- Все команды синхронизируют приоритеты\n- Зависимости визуализируются на общей доске\n\n### PI Objectives:\nЧёткие, измеримые цели на PI (обычно 10–12 недель).\n- Business Value — оценка стейкхолдерами (1–10)\n- Stretch Objectives — амбициозные, но необязательные"},
                    {"type": "drag-order", "items": ["Business context — стратегия и бизнес-цели", "Product Vision — направление продукта", "Team Breakout 1 — командное планирование", "Draft Plan Review — согласование планов", "Team Breakout 2 — доработка", "Final Plan Review — итоговое согласование"]},
                    {"type": "quiz", "question": "Как часто проводится PI Planning в SAFe?", "options": [{"id": "a", "text": "Каждый спринт (2 недели)", "correct": False}, {"id": "b", "text": "Каждый Program Increment (обычно 10–12 недель)", "correct": True}, {"id": "c", "text": "Раз в год", "correct": False}, {"id": "d", "text": "При каждом релизе", "correct": False}]},
                    {"type": "true-false", "statement": "PI Objectives — это измеримые цели на Program Increment, которые оцениваются стейкхолдерами.", "correct": True},
                ],
            },
            {
                "t": "Cross-team delivery",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Координация команд", "markdown": "## Cross-team Delivery — координация команд\n\n### Главные вызовы:\n- Зависимости между командами замедляют доставку\n- Разные ритмы и приоритеты\n- Проблемы с коммуникацией и владением\n\n### Паттерны координации:\n\n**Communities of Practice (CoP)**\nГруппы по интересам (фронтенд-гильдия, архитекторы).\nОбмен знаниями и стандартами без формальной иерархии.\n\n**Scrum of Scrums**\nМета-standup: по одному представителю от каждой команды.\n- Синхронизация прогресса и блокеров между командами\n- Обычно 2–3 раза в неделю, 30 минут\n\n**Feature Teams vs Component Teams:**\n- **Feature Teams** — кросс-функциональные, поставляют сквозные фичи\n- **Component Teams** — специализируются на слое (backend, frontend, QA)\n- Feature teams быстрее доставляют ценность, меньше зависимостей\n\n### Team Topologies:\nПо книге Skelton & Pais — 4 типа команд:\n1. Stream-aligned\n2. Enabling\n3. Complicated Subsystem\n4. Platform"},
                    {"type": "matching", "pairs": [{"left": "Scrum of Scrums", "right": "Meta-standup с представителями от каждой команды"}, {"left": "Communities of Practice", "right": "Гильдии для обмена знаниями без иерархии"}, {"left": "Feature Teams", "right": "Кросс-функциональные команды, поставляющие сквозные фичи"}, {"left": "Component Teams", "right": "Специализируются на одном слое архитектуры"}]},
                    {"type": "quiz", "question": "Какой тип команд быстрее поставляет end-to-end ценность с меньшим числом зависимостей?", "options": [{"id": "a", "text": "Component Teams", "correct": False}, {"id": "b", "text": "Feature Teams", "correct": True}, {"id": "c", "text": "Platform Teams", "correct": False}, {"id": "d", "text": "Operations Teams", "correct": False}]},
                    {"type": "true-false", "statement": "Scrum of Scrums — это формат синхронизации между командами, не заменяющий внутрикомандный standup.", "correct": True},
                ],
            },
            {
                "t": "Release Management",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Feature Flags, Canary, Blue-Green", "markdown": "## Release Management\n\nМодернизация процессов релиза снижает риски и ускоряет delivery.\n\n### Feature Flags (Feature Toggles)\nМеханизм включения/выключения функциональности без деплоя.\n- Постепенное раскрытие (10% → 50% → 100%)\n- A/B тестирование в production\n- Мгновенный откат без code revert\n\n### Canary Release\nПостепенный релиз для небольшой доли пользователей.\n```\n[Новая версия] → 5% трафика\n[Старая версия] → 95% трафика\n```\nЕсли метрики в норме — расширяем аудиторию.\n\n### Blue-Green Deployment\nДве идентичные production-среды.\n- **Blue** — текущая версия (активная)\n- **Green** — новая версия (тестируется)\n- Переключение трафика мгновенно\n- При проблемах — откат за секунды\n\n### Rolling Deployment\nПостепенная замена инстансов без downtime.\n\n### Преимущества современных подходов:\n- Деплой и релиз — разные события\n- Минимальный downtime\n- Быстрый откат"},
                    {"type": "matching", "pairs": [{"left": "Feature Flags", "right": "Включение/выключение функций без деплоя"}, {"left": "Canary Release", "right": "Постепенный релиз на малую долю пользователей"}, {"left": "Blue-Green", "right": "Две среды с мгновенным переключением трафика"}, {"left": "Rolling Deployment", "right": "Постепенная замена инстансов без downtime"}]},
                    {"type": "quiz", "question": "В чём главное преимущество Blue-Green Deployment?", "options": [{"id": "a", "text": "Экономия серверных ресурсов", "correct": False}, {"id": "b", "text": "Мгновенный откат при проблемах путём переключения трафика", "correct": True}, {"id": "c", "text": "Автоматическое тестирование кода", "correct": False}, {"id": "d", "text": "Ускорение сборки образа Docker", "correct": False}]},
                    {"type": "true-false", "statement": "Feature Flags позволяют откатить функциональность без code revert и нового деплоя.", "correct": True},
                ],
            },
            {
                "t": "Value Stream Mapping",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "VSM, Bottleneck, Waste", "markdown": "## Value Stream Mapping (VSM)\n\nVSM — инструмент из **«Lean Thinking»** (Womack & Jones), адаптированный для software delivery.\n\n### Что такое Value Stream:\nПолная цепочка шагов от идеи клиента до ценности в его руках.\n\n### Зачем VSM:\n- Визуализировать весь поток создания ценности\n- Найти узкие места (bottlenecks)\n- Выявить потери (waste)\n\n### 8 видов потерь (Lean):\n1. **Транспортировка** — передача задач между командами\n2. **Запасы** — задачи, ждущие в очереди\n3. **Движение** — лишние переключения контекста\n4. **Ожидание** — блокеры, зависимости\n5. **Перепроизводство** — фичи, которых никто не использует\n6. **Переработка** — исправление дефектов\n7. **Дефекты** — баги, инциденты\n8. **Неиспользованный талант** — бюрократия, несоответствие задач навыкам\n\n### Как провести VSM:\n1. Определите начало и конец потока\n2. Нанесите все шаги и очереди\n3. Измерьте Process Time и Wait Time для каждого шага\n4. Вычислите Flow Efficiency\n5. Найдите bottleneck и атакуйте его"},
                    {"type": "drag-order", "items": ["Определить начало и конец потока ценности", "Нанести все шаги и очереди на карту", "Измерить Process Time и Wait Time каждого шага", "Вычислить Flow Efficiency", "Найти bottleneck и устранить его"]},
                    {"type": "quiz", "question": "Какой вид потерь по Lean описывает невостребованные фичи?", "options": [{"id": "a", "text": "Дефекты", "correct": False}, {"id": "b", "text": "Ожидание", "correct": False}, {"id": "c", "text": "Перепроизводство", "correct": True}, {"id": "d", "text": "Транспортировка", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Value Stream", "back": "Полная цепочка шагов от идеи до ценности для клиента"}, {"front": "VSM", "back": "Value Stream Mapping — визуализация потока и поиск потерь"}, {"front": "Bottleneck", "back": "Узкое место — шаг, ограничивающий пропускную способность всей системы"}, {"front": "Lean Thinking", "back": "Книга Womack & Jones о устранении потерь и создании ценности"}, {"front": "8 видов потерь (Lean)", "back": "Транспортировка, Запасы, Движение, Ожидание, Перепроизводство, Переработка, Дефекты, Таланты"}]},
                ],
            },
            {
                "t": "Ресурсы: Масштабирование",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "SAFe Framework — Official", "url": "https://www.scaledagileframework.com", "type": "link"},
                            {"label": "Lean Thinking — книга", "url": "https://www.goodreads.com/book/show/289467.Lean_Thinking", "type": "link"},
                            {"label": "Feature Flags — Martin Fowler", "url": "https://martinfowler.com/articles/feature-toggles.html", "type": "link"},
                            {"label": "Value Stream Mapping Guide", "url": "https://www.lean.org/lexicon-terms/value-stream-mapping", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 6: Люди и команды =====
    {
        "title": "Люди и команды",
        "pos": 5,
        "lessons": [
            {
                "t": "Формирование команды",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Tuckman и Team Topologies", "markdown": "## Формирование команды\n\n### Модель Такмана (Tuckman, 1965)\nЧетыре стадии развития команды:\n\n1. **Forming (Знакомство)** — вежливость, неопределённость, зависимость от лидера\n2. **Storming (Конфликты)** — разногласия по процессам, роли неясны\n3. **Norming (Нормализация)** — команда вырабатывает правила, растёт доверие\n4. **Performing (Результаты)** — высокая автономия и эффективность\n\n*(Позже Тукман добавил 5-ю стадию: Adjourning — расформирование)*\n\n### Роль DM на каждой стадии:\n- **Forming**: создать ясность по целям и ролям\n- **Storming**: фасилитировать конфликты конструктивно\n- **Norming**: закрепить рабочие соглашения\n- **Performing**: убирать блокеры, не вмешиваться\n\n### Team Topologies (Skelton & Pais)\nЧетыре типа команд:\n- **Stream-aligned** — поставляет ценность напрямую\n- **Enabling** — помогает другим командам\n- **Complicated Subsystem** — специализированная экспертиза\n- **Platform** — внутренние инструменты и инфраструктура"},
                    {"type": "drag-order", "items": ["Forming — знакомство и неопределённость", "Storming — конфликты и прояснение ролей", "Norming — выработка правил и рост доверия", "Performing — высокая автономия и результаты"]},
                    {"type": "matching", "pairs": [{"left": "Forming", "right": "Вежливость, зависимость от лидера"}, {"left": "Storming", "right": "Конфликты, разногласия по процессам"}, {"left": "Norming", "right": "Рабочие соглашения, растущее доверие"}, {"left": "Performing", "right": "Автономия и высокая эффективность"}]},
                    {"type": "quiz", "question": "На какой стадии по Такману DM должен меньше всего вмешиваться?", "options": [{"id": "a", "text": "Forming", "correct": False}, {"id": "b", "text": "Storming", "correct": False}, {"id": "c", "text": "Norming", "correct": False}, {"id": "d", "text": "Performing", "correct": True}]},
                ],
            },
            {
                "t": "Мотивация",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Drive (Pink): Autonomy, Mastery, Purpose", "markdown": "## Мотивация в командах\n\n### Drive — Дэниел Пинк\nКнига **\"Drive\"** (Pink, 2009) описывает три источника внутренней мотивации:\n\n**1. Autonomy (Автономия)**\nЖелание управлять своей работой.\n- Когда и как работаешь\n- С кем работаешь\n- Над чем работаешь\n\n**2. Mastery (Мастерство)**\nЖелание становиться лучше в том, что важно.\n- Состояние потока (flow)\n- Постоянное развитие\n- Сложные, но достижимые цели\n\n**3. Purpose (Смысл)**\nЖелание делать что-то важное.\n- Связь работы с большой целью\n- «Зачем мы это делаем?»\n\n### Психологическая безопасность (Google, Project Aristotle):\nГлавный предиктор эффективности команды — не умные люди, не правильные процессы, а **психологическая безопасность**: каждый может говорить открыто без страха осуждения.\n\n### Роль DM:\nСоздавать условия, а не управлять мотивацией напрямую."},
                    {"type": "matching", "pairs": [{"left": "Autonomy", "right": "Желание управлять своей работой"}, {"left": "Mastery", "right": "Желание становиться лучше в важном"}, {"left": "Purpose", "right": "Желание работать над чем-то значимым"}, {"left": "Психологическая безопасность", "right": "Возможность говорить открыто без страха осуждения"}]},
                    {"type": "quiz", "question": "Что является главным предиктором эффективности команды по исследованию Google Project Aristotle?", "options": [{"id": "a", "text": "IQ участников команды", "correct": False}, {"id": "b", "text": "Правильные Agile-процессы", "correct": False}, {"id": "c", "text": "Психологическая безопасность", "correct": True}, {"id": "d", "text": "Количество лет опыта в команде", "correct": False}]},
                    {"type": "true-false", "statement": "По книге Drive (Пинк), внешние вознаграждения (деньги, бонусы) — главный драйвер мотивации знаниевых работников.", "correct": False},
                ],
            },
            {
                "t": "Коучинг",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "GROW модель и 1:1 best practices", "markdown": "## Коучинг в работе Delivery Manager\n\n### GROW Model\nКлассическая модель коучинговой беседы:\n\n- **G — Goal** (Цель): Чего ты хочешь достичь?\n- **R — Reality** (Реальность): Где ты сейчас находишься?\n- **O — Options** (Варианты): Что ты можешь сделать?\n- **W — Will/Way Forward** (Действия): Что конкретно сделаешь?\n\n### 1:1 встречи — best practices:\n- Проводить **регулярно** (еженедельно или каждые 2 недели)\n- **Повестка принадлежит сотруднику**, не менеджеру\n- Слушать **80%, говорить 20%**\n- Задавать открытые вопросы, не давать готовые ответы\n- Делать заметки и отслеживать прогресс\n\n### Вопросы для 1:1:\n- «Что сейчас идёт хорошо?»\n- «Что тебя блокирует?»\n- «Что я могу сделать, чтобы помочь?»\n- «Над чем ты хотел бы работать больше?»\n\n### Коучинг ≠ менторинг:\n- **Менторинг**: делюсь своим опытом и советами\n- **Коучинг**: задаю вопросы, человек сам находит ответы"},
                    {"type": "drag-order", "items": ["G — Goal: чего хочешь достичь?", "R — Reality: где находишься сейчас?", "O — Options: какие есть варианты?", "W — Will: что конкретно сделаешь?"]},
                    {"type": "quiz", "question": "Чему принадлежит повестка 1:1 встречи?", "options": [{"id": "a", "text": "Менеджеру — он решает, что обсуждать", "correct": False}, {"id": "b", "text": "Сотруднику — это его встреча", "correct": True}, {"id": "c", "text": "Команде — коллективно обсуждаем", "correct": False}, {"id": "d", "text": "HR-отделу", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Менторинг", "right": "Делюсь своим опытом и советами"}, {"left": "Коучинг", "right": "Задаю вопросы, человек сам находит ответы"}, {"left": "GROW", "right": "Goal, Reality, Options, Will"}, {"left": "1:1", "right": "Регулярная встреча сотрудника с менеджером"}]},
                ],
            },
            {
                "t": "Управление конфликтами",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Thomas-Kilmann и Difficult Conversations", "markdown": "## Управление конфликтами\n\n### Модель Thomas-Kilmann\nПять стилей поведения в конфликте:\n\n```\n           Высокая напористость\n           ┌─────────────────────┐\n           │  Конкурент  │  Коллаборатор│\n           │ (Win-Lose)  │  (Win-Win)  │\n           ├─────────────┼─────────────┤\n           │  Компромисс │             │\n           ├─────────────┼─────────────┤\n           │  Избегатель │  Уступающий │\n           └─────────────────────┘\n           Низкая          Высокое\n           кооперативность\n```\n\n- **Competing (Конкурент)** — напористый, некооперативный: «Я должен выиграть»\n- **Collaborating (Коллаборатор)** — напористый + кооперативный: лучший стиль\n- **Compromising (Компромисс)** — середина: оба уступают\n- **Avoiding (Избегание)** — избегает конфликта: откладывает проблему\n- **Accommodating (Уступчивость)** — ненапористый, кооперативный: «Ладно, ты прав»\n\n### Difficult Conversations:\nПо книге Stone, Patton, Heen — три разговора внутри любого трудного:\n1. Что произошло? (разные версии)\n2. Чувства (эмоциональный слой)\n3. Идентичность (угроза самооценке)"},
                    {"type": "matching", "pairs": [{"left": "Competing", "right": "Напористый, некооперативный — «Я должен выиграть»"}, {"left": "Collaborating", "right": "Напористый и кооперативный — Win-Win"}, {"left": "Avoiding", "right": "Избегает конфликта, откладывает проблему"}, {"left": "Accommodating", "right": "Уступает — «Ладно, ты прав»"}]},
                    {"type": "quiz", "question": "Какой стиль по Thomas-Kilmann наилучший для разрешения конфликтов на работе?", "options": [{"id": "a", "text": "Competing — напористо отстаивать свою позицию", "correct": False}, {"id": "b", "text": "Avoiding — избегать конфликтов", "correct": False}, {"id": "c", "text": "Collaborating — напористый и кооперативный Win-Win", "correct": True}, {"id": "d", "text": "Accommodating — всегда уступать", "correct": False}]},
                    {"type": "true-false", "statement": "Стиль Avoiding (избегание конфликта) решает проблему, так как конфликт сам исчезает.", "correct": False},
                ],
            },
            {
                "t": "Ресурсы: Люди и команды",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "Team Topologies — книга", "url": "https://www.goodreads.com/book/show/44135420-team-topologies", "type": "link"},
                            {"label": "Drive — Daniel Pink (книга)", "url": "https://www.goodreads.com/book/show/6452796-drive", "type": "link"},
                            {"label": "Google re:Work — Psychological Safety", "url": "https://rework.withgoogle.com/guides/understanding-team-effectiveness", "type": "link"},
                            {"label": "GROW Model — MindTools", "url": "https://www.mindtools.com/a3mi0ly/the-grow-model", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 7: Инструменты =====
    {
        "title": "Инструменты Delivery Manager",
        "pos": 6,
        "lessons": [
            {
                "t": "Jira и Confluence для DM",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Workflows и дашборды в Jira", "markdown": "## Jira и Confluence для Delivery Manager\n\n### Jira — управление задачами\n\n**Ключевые возможности для DM:**\n- **Board** — Kanban или Scrum доска\n- **Backlog** — управление очередью задач\n- **Workflows** — настройка этапов (To Do → In Progress → Review → Done)\n- **Dashboards** — метрики в реальном времени\n- **Reports** — Burndown, Velocity, Cumulative Flow\n\n**Полезные дашборды:**\n- Cycle Time report\n- Throughput chart\n- Sprint Velocity\n- Epic Progress\n\n### Confluence — база знаний\n- Документация процессов и соглашений\n- Meeting notes\n- Runbooks (инструкции при инцидентах)\n- Architecture Decision Records (ADR)\n\n### Интеграция Jira + Confluence:\n- Связывать задачи Jira со страницами Confluence\n- Автоматически создавать отчёты\n- Хранить Definition of Done в Confluence, использовать в Jira"},
                    {"type": "quiz", "question": "Для чего используется Burndown chart в Jira?", "options": [{"id": "a", "text": "Для отображения накопленных задач в каждом состоянии", "correct": False}, {"id": "b", "text": "Для отслеживания оставшейся работы в спринте относительно времени", "correct": True}, {"id": "c", "text": "Для мониторинга production-инцидентов", "correct": False}, {"id": "d", "text": "Для управления доступами в Confluence", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Jira", "items": ["Kanban доска", "Sprint Backlog", "Velocity Report"]}, {"name": "Confluence", "items": ["Runbooks для инцидентов", "Architecture Decision Records", "Meeting Notes"]}]},
                    {"type": "true-false", "statement": "Cumulative Flow Diagram в Jira помогает увидеть накопление задач в каждом состоянии.", "correct": True},
                ],
            },
            {
                "t": "CI/CD pipeline",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Continuous Integration и Automated Testing", "markdown": "## CI/CD Pipeline\n\n### Continuous Integration (CI)\nПрактика частого объединения изменений кода с автоматической проверкой.\n\n**Типичный CI pipeline:**\n1. Разработчик делает коммит\n2. Автоматически запускаются тесты (unit, integration)\n3. Статический анализ кода (linting, SAST)\n4. Сборка артефакта\n5. Уведомление о результатах\n\n### Continuous Delivery (CD)\nАвтоматизация доставки артефакта до production-ready состояния.\n\n**CD pipeline:**\n1. CI прошёл успешно\n2. Deploy в staging\n3. Автоматические E2E тесты\n4. Ручное или автоматическое одобрение\n5. Deploy в production\n\n### Ключевые принципы:\n- **Fast feedback** — pipeline должен работать < 10 минут\n- **Broken build = top priority** — сломанный pipeline блокирует всех\n- **Everything as code** — конфигурация в репозитории\n\n### Популярные инструменты:\n- **GitHub Actions** — встроен в GitHub\n- **GitLab CI** — встроен в GitLab\n- **Jenkins** — самостоятельный сервер\n- **CircleCI, TeamCity, ArgoCD**"},
                    {"type": "drag-order", "items": ["Разработчик делает коммит", "Автоматически запускаются тесты", "Статический анализ кода", "Сборка артефакта", "Deploy в staging", "Тесты в staging", "Deploy в production"]},
                    {"type": "quiz", "question": "Какое правило CI гласит: «сломанный пайплайн блокирует всех»?", "options": [{"id": "a", "text": "Shift Left", "correct": False}, {"id": "b", "text": "Broken build = top priority", "correct": True}, {"id": "c", "text": "Definition of Done", "correct": False}, {"id": "d", "text": "WIP-лимит", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Continuous Integration", "right": "Частые коммиты с автоматическими тестами"}, {"left": "Continuous Delivery", "right": "Автоматическая доставка до production-ready"}, {"left": "Fast Feedback", "right": "Pipeline работает менее 10 минут"}, {"left": "Everything as Code", "right": "Конфигурация инфраструктуры хранится в репозитории"}]},
                ],
            },
            {
                "t": "Мониторинг",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "SLI, SLO, SLA и Alerting", "markdown": "## Мониторинг и надёжность\n\n### SLI / SLO / SLA\n\n**SLI (Service Level Indicator)**\nКонкретная измеримая метрика надёжности.\n- Availability (доступность)\n- Latency (задержка)\n- Error rate (процент ошибок)\n\n**SLO (Service Level Objective)**\nЦелевое значение SLI, которое мы стремимся соблюдать.\n- Availability SLO: 99.9% (три девятки)\n- Latency SLO: p95 < 200ms\n\n**SLA (Service Level Agreement)**\nЮридически обязывающее соглашение с клиентом об уровне сервиса.\n- SLA обычно строже SLO\n- Нарушение SLA → штрафы\n\n### Error Budget\nДопустимый «бюджет» ошибок = 1 - SLO.\n- SLO 99.9% → error budget = 0.1% ≈ 8.7 часов/год\n- Если бюджет исчерпан — останавливаем новые фичи, фокусируемся на надёжности\n\n### Alerting (Алертинг):\n- **Alert** — уведомление о нарушении порога\n- Хороший alert: actionable + срочный + без ложных срабатываний\n- On-call rotation — дежурство по ответу на алерты"},
                    {"type": "matching", "pairs": [{"left": "SLI", "right": "Конкретная измеримая метрика надёжности"}, {"left": "SLO", "right": "Целевое значение метрики надёжности"}, {"left": "SLA", "right": "Юридическое соглашение об уровне сервиса"}, {"left": "Error Budget", "right": "Допустимый бюджет отказов = 1 - SLO"}]},
                    {"type": "quiz", "question": "Если SLO = 99.9%, каков годовой error budget в часах?", "options": [{"id": "a", "text": "1 час", "correct": False}, {"id": "b", "text": "8.7 часов", "correct": True}, {"id": "c", "text": "87 часов", "correct": False}, {"id": "d", "text": "0.1 часа", "correct": False}]},
                    {"type": "true-false", "statement": "SLA — это внутренняя цель команды, а SLO — юридически обязывающее соглашение с клиентом.", "correct": False},
                ],
            },
            {
                "t": "Автоматизация процессов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "ChatOps и автоматические отчёты", "markdown": "## Автоматизация процессов\n\n### ChatOps\nУправление инфраструктурой и процессами через чат (Slack, Teams).\n\n**Примеры ChatOps-команд:**\n```\n/deploy service=api env=staging\n/rollback service=api version=1.2.3\n/incident create sev=2 title=\"Payment failing\"\n/report sprint-metrics\n```\n\n### Автоматические отчёты:\n- Еженедельный дайджест DORA-метрик\n- Sprint summary после окончания спринта\n- Incident weekly report\n- Deployment frequency trend\n\n### Инструменты автоматизации:\n- **GitHub Actions / GitLab CI** — автоматизация build/deploy\n- **Zapier / n8n** — no-code автоматизация\n- **Slack bots** — уведомления и команды\n- **Grafana** — дашборды и алерты\n- **PagerDuty / OpsGenie** — on-call и incident management\n\n### Принцип «автоматизируй скуку»:\nЛюбая повторяющаяся ручная работа — кандидат для автоматизации.\nВопрос: «Делаем ли мы это каждую неделю? Можно ли автоматизировать?»"},
                    {"type": "quiz", "question": "Что такое ChatOps?", "options": [{"id": "a", "text": "Мессенджер для общения команды", "correct": False}, {"id": "b", "text": "Управление инфраструктурой и процессами через чат-команды", "correct": True}, {"id": "c", "text": "Автоматическое тестирование в CI/CD", "correct": False}, {"id": "d", "text": "Agile-церемония ежедневного обмена", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Инструменты автоматизации", "items": ["GitHub Actions", "Zapier / n8n", "Slack bots"]}, {"name": "Инструменты мониторинга и алертинга", "items": ["Grafana", "PagerDuty", "OpsGenie"]}]},
                    {"type": "true-false", "statement": "Любая повторяющаяся ручная задача — кандидат для автоматизации.", "correct": True},
                ],
            },
            {
                "t": "Ресурсы: Инструменты DM",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "Jira Best Practices — Atlassian", "url": "https://www.atlassian.com/software/jira/guides", "type": "link"},
                            {"label": "CI/CD — GitLab Guide", "url": "https://docs.gitlab.com/ee/ci", "type": "link"},
                            {"label": "SLO/SLI/SLA — Google SRE Book", "url": "https://sre.google/sre-book/service-level-objectives", "type": "link"},
                            {"label": "ChatOps — Atlassian", "url": "https://www.atlassian.com/blog/software-teams/what-is-chatops", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
    # ===== SECTION 8: Карьера =====
    {
        "title": "Карьера Delivery Manager",
        "pos": 7,
        "lessons": [
            {
                "t": "Карьерный путь DM",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Junior → Head of Delivery", "markdown": "## Карьерный путь Delivery Manager\n\n### Уровни:\n\n**Junior DM / Delivery Coordinator**\n- Помогает в организации процессов одной команды\n- Ведёт RAID log, обновляет дашборды\n- Работает под руководством Senior DM\n\n**Delivery Manager (Middle)**\n- Самостоятельно управляет delivery одной-двух команд\n- Выстраивает процессы, проводит ретроспективы\n- Работает со стейкхолдерами\n\n**Senior Delivery Manager**\n- Отвечает за delivery нескольких команд\n- Менторит других DM\n- Влияет на инженерную культуру\n\n**Head of Delivery / VP of Engineering Delivery**\n- Стратегия delivery для всей организации\n- Управляет командой DM\n- DORA-трансформация на уровне компании\n\n### Альтернативные треки:\n- DM → Engineering Manager (больше фокус на людях)\n- DM → Product Manager (больше фокус на продукте)\n- DM → Agile Coach (трансформация организации)\n- DM → CTO / VP Engineering"},
                    {"type": "drag-order", "items": ["Junior DM / Delivery Coordinator", "Delivery Manager (Middle)", "Senior Delivery Manager", "Head of Delivery / VP Engineering Delivery"]},
                    {"type": "quiz", "question": "Какой переход характерен для DM, если он хочет больше фокусироваться на людях?", "options": [{"id": "a", "text": "DM → Product Manager", "correct": False}, {"id": "b", "text": "DM → Engineering Manager", "correct": True}, {"id": "c", "text": "DM → QA Lead", "correct": False}, {"id": "d", "text": "DM → Data Analyst", "correct": False}]},
                    {"type": "true-false", "statement": "Head of Delivery отвечает за стратегию delivery на уровне всей организации.", "correct": True},
                ],
            },
            {
                "t": "Сертификации",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "PSM, PMI-ACP, SAFe, ICAgile", "markdown": "## Сертификации для Delivery Manager\n\n### Scrum-сертификации (Scrum.org):\n- **PSM I** (Professional Scrum Master I) — базовый уровень\n- **PSM II** — продвинутый уровень\n- **PSM III** — экспертный уровень\n- Онлайн-экзамен, относительно доступен\n\n### PMI-ACP (Agile Certified Practitioner)\n- От PMI (Project Management Institute)\n- Охватывает несколько Agile-методологий\n- Требует опыт работы и часы обучения\n\n### SAFe сертификации:\n- **SA** (SAFe Agilist) — базовый\n- **RTE** (Release Train Engineer) — для PI Planning\n- **SPC** (SAFe Program Consultant) — для трансформации\n\n### ICAgile:\n- **ICP-ACC** — Agile Coaching\n- **ICP-ENT** — Enterprise Agile\n\n### DASA (DevOps Agile Skills Association):\n- Сертификации по DevOps и delivery\n\n### Рекомендация:\nНачните с **PSM I** — доступный, широко признаваемый, проверяет понимание Scrum."},
                    {"type": "matching", "pairs": [{"left": "PSM I", "right": "Professional Scrum Master — Scrum.org"}, {"left": "PMI-ACP", "right": "Agile Certified Practitioner — PMI"}, {"left": "RTE", "right": "Release Train Engineer — SAFe"}, {"left": "ICP-ACC", "right": "ICAgile Agile Coaching сертификат"}]},
                    {"type": "quiz", "question": "Какую сертификацию рекомендуется получить первой начинающему DM?", "options": [{"id": "a", "text": "SAFe SPC", "correct": False}, {"id": "b", "text": "PMI-ACP", "correct": False}, {"id": "c", "text": "PSM I", "correct": True}, {"id": "d", "text": "ICP-ENT", "correct": False}]},
                    {"type": "multi-select", "question": "Какие сертификации относятся к SAFe?", "options": [{"id": "a", "text": "SA (SAFe Agilist)", "correct": True}, {"id": "b", "text": "PSM II", "correct": False}, {"id": "c", "text": "RTE (Release Train Engineer)", "correct": True}, {"id": "d", "text": "SPC (SAFe Program Consultant)", "correct": True}, {"id": "e", "text": "PMI-ACP", "correct": False}]},
                ],
            },
            {
                "t": "Портфолио DM",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Case Studies и Interview Prep", "markdown": "## Портфолио Delivery Manager\n\n### Что включить в портфолио:\n\n**1. Delivery Case Studies:**\n- Ситуация: какая была проблема с delivery?\n- Действия: что вы сделали?\n- Результат: метрики до и после\n\n**Пример:**\n«Команда из 8 человек не выполняла обещания по срокам. Ввёл WIP-лимиты и еженедельный CFD-анализ. Cycle time уменьшился с 14 до 6 дней за 2 месяца.»\n\n**2. Метрики и трансформации:**\n- DORA metrics improvement\n- Снижение cycle time\n- Рост deployment frequency\n\n**3. Процессные артефакты:**\n- Примеры RAID log\n- Пример definition of done\n- Пример delivery dashboard\n\n### Подготовка к интервью:\n- Готовьте 3–5 STAR-историй про блокеры, конфликты, трансформации\n- Будьте готовы объяснить DORA-метрики и как их улучшали\n- Знайте отличие DM от PM, Scrum Master, EM\n\n### Если нет опыта:\n- Проведите анализ delivery-процессов в текущей компании\n- Сделайте личный проект по VSM или DORA-аудиту"},
                    {"type": "drag-order", "items": ["Описать ситуацию — какая была проблема с delivery", "Описать действия — что конкретно вы сделали", "Показать результат — метрики до и после", "Описать выводы — что узнали"]},
                    {"type": "quiz", "question": "Что является самым убедительным элементом DM-кейса?", "options": [{"id": "a", "text": "Красивый дизайн презентации", "correct": False}, {"id": "b", "text": "Конкретные метрики: до и после изменений", "correct": True}, {"id": "c", "text": "Количество сертификаций", "correct": False}, {"id": "d", "text": "Список использованных инструментов", "correct": False}]},
                    {"type": "true-false", "statement": "Для DM-портфолио обязательно иметь опыт в должности Delivery Manager — без него нечего показывать.", "correct": False},
                ],
            },
            {
                "t": "DM в 2025+",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "AI в delivery, remote-first, outcome-based", "markdown": "## Delivery Management в 2025+\n\n### AI в Delivery\n**Как AI меняет delivery:**\n- **AI-assisted planning** — прогнозирование сроков на основе исторических данных\n- **Automated testing** — AI-генерация тест-кейсов\n- **Incident prediction** — anomaly detection до падения системы\n- **Code review automation** — AI-ревью pull requests\n- **Sprint reports** — автоматическая генерация отчётов\n\n### Remote-first Delivery:\n- Async-first: уменьшение синхронных встреч\n- Документация как культура (writing > talking)\n- Инструменты: Notion, Linear, Loom, Miro\n- Overlap hours вместо «рабочих часов»\n- Explicit > implicit коммуникация\n\n### Outcome-based Delivery:\nСдвиг от «сделали фичи в срок» к «достигли бизнес-результата»\n- Метрики: не velocity, а бизнес KPI\n- OKR + DORA совместно\n- Teams as profit centers\n\n### Тренды:\n- **Platform Engineering** — внутренние разработчицкие платформы\n- **FinOps** — управление cloud-расходами\n- **Developer Experience (DevEx)** — улучшение жизни разработчиков\n- **AI-native teams** — команды, строящие AI-first продукты"},
                    {"type": "quiz", "question": "Что означает переход к Outcome-based Delivery?", "options": [{"id": "a", "text": "Фокус на количестве фич, сделанных в срок", "correct": False}, {"id": "b", "text": "Фокус на достижении бизнес-результатов, а не на выпуске фич", "correct": True}, {"id": "c", "text": "Ускорение темпов разработки любыми средствами", "correct": False}, {"id": "d", "text": "Полный переход на AI без участия людей", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "AI-assisted planning", "right": "Прогнозирование сроков на основе исторических данных"}, {"left": "Remote-first", "right": "Async-first коммуникация и документация как культура"}, {"left": "Platform Engineering", "right": "Внутренние платформы для повышения Developer Experience"}, {"left": "FinOps", "right": "Управление и оптимизация cloud-расходов"}]},
                    {"type": "flashcards", "cards": [{"front": "Outcome-based Delivery", "back": "Фокус на бизнес-результатах, а не на выпуске фич в срок"}, {"front": "Platform Engineering", "back": "Создание внутренних платформ и инструментов для разработчиков"}, {"front": "Developer Experience (DevEx)", "back": "Качество инструментов, процессов и среды для разработчиков"}, {"front": "FinOps", "back": "Практика управления cloud-затратами: прозрачность, оптимизация"}]},
                    {"type": "multi-select", "question": "Какие тренды в Delivery Management актуальны в 2025+?", "options": [{"id": "a", "text": "Platform Engineering", "correct": True}, {"id": "b", "text": "Waterfall-возрождение", "correct": False}, {"id": "c", "text": "AI-assisted planning", "correct": True}, {"id": "d", "text": "Developer Experience (DevEx)", "correct": True}, {"id": "e", "text": "Отказ от метрик", "correct": False}]},
                ],
            },
            {
                "t": "Ресурсы: Карьера DM",
                "xp": 10,
                "steps": [
                    {
                        "type": "resources",
                        "title": "Книги, статьи и шаблоны",
                        "description": "Изучите эти материалы для углубления знаний по теме.",
                        "items": [
                            {"label": "PMI-ACP Certification", "url": "https://www.pmi.org/certifications/agile-acp", "type": "link"},
                            {"label": "Scrum.org — PSM", "url": "https://www.scrum.org/assessments/professional-scrum-master-i-certification", "type": "link"},
                            {"label": "SAFe Certifications", "url": "https://www.scaledagileframework.com/certification", "type": "link"},
                            {"label": "Delivery Management Career Path — Gov.UK", "url": "https://www.gov.uk/guidance/delivery-manager", "type": "link"},
                        ],
                    }
                ],
            },
        ],
    },
]


async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping.")
            return
        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author:
            print("No users.")
            return
        course = Course(
            title=T,
            slug="delivery-management-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="management",
            difficulty="intermediate",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()
        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(course_id=course.id, title=sd["title"], position=sd["pos"])
            db.add(sec)
            await db.flush()
            for li, ld in enumerate(sd["lessons"]):
                les = CourseLesson(
                    section_id=sec.id,
                    title=ld["t"],
                    position=li,
                    content_type="interactive",
                    content_markdown="",
                    xp_reward=ld["xp"],
                    steps=ld["steps"],
                )
                db.add(les)
                await db.flush()
                r, c = lc // 5, lc % 5
                x, y = SNAKE_X[c] * CANVAS_W, V_PAD + r * ROW_H
                nodes.append({"id": str(les.id), "x": x, "y": y})
                if lc > 0:
                    edges.append(
                        {
                            "id": f"e-{lc}",
                            "source": nodes[-2]["id"],
                            "target": nodes[-1]["id"],
                        }
                    )
                lc += 1
                tl += 1
        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
