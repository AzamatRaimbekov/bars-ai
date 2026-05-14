"""Seed: AI Video Generation — Sora, Veo, Runway, Kling, Higgsfield."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "AI Video Generation — Sora, Veo, Runway и Kling"
DESC = (
    "Полный гид по AI-видео 2026: ландшафт моделей, промптинг для видео "
    "(camera moves, narrative), image-to-video workflow, монтаж, "
    "use cases от рекламы до музклипов. Для креаторов и маркетологов."
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
        "title": "Ландшафт AI-видео 2026",
        "pos": 0,
        "lessons": [
            {
                "t": "Топ-модели и их сильные стороны",
                "xp": 20,
                "steps": [
                    info("Кто есть кто", "## Главные модели 2026\n\n| Модель | Вендор | Сильно | Длина |\n|---|---|---|---|\n| **Sora 2** | OpenAI | Реализм, длинные сцены, физика | до 60 сек |\n| **Veo 3** | Google | Качество, аудио из коробки | до 60 сек |\n| **Runway Gen-4** | Runway | Кинематографичность, контроль | до 16 сек |\n| **Kling 2.0** | Kuaishou | Реализм лиц, китайская спецификация | до 10 сек |\n| **Higgsfield** | Higgsfield | Camera moves, motion control | до 10 сек |\n| **Hailuo MiniMax** | MiniMax | Хорошее соотношение цена/качество | до 6 сек |\n| **Luma Dream Machine** | Luma | Простой UI, быстро | до 10 сек |\n| **Pika** | Pika Labs | Стиль, эффекты | до 10 сек |\n\n## Главное в 2026\n- **Длина сцены** растёт: 6 сек → 60 сек\n- **Аудио** генерируется одновременно (Veo 3)\n- **Контроль** через image-to-video и camera moves\n- **Цены падают** — Sora $200 → $20/мес"),
                    match([
                        ("Sora 2", "OpenAI, реализм, до 60 сек"),
                        ("Veo 3", "Google, аудио из коробки"),
                        ("Runway Gen-4", "Кинематограф, контроль"),
                        ("Higgsfield", "Camera moves, motion control"),
                        ("Kling", "Реализм лиц, китайская"),
                    ]),
                    multi("Что характерно для AI-видео 2026?", [
                        ("Длина сцены растёт до 60 секунд", True),
                        ("Veo 3 генерирует видео с аудио", True),
                        ("Цены падают", True),
                        ("Только чёрно-белое видео", False),
                    ]),
                    quiz("Какая модель отличается camera moves и motion control?", [
                        ("Sora 2", False),
                        ("Higgsfield", True),
                        ("Apple Notes", False),
                    ]),
                ],
            },
            {
                "t": "Когда AI-видео уже работает, а когда нет",
                "xp": 20,
                "steps": [
                    info("Реалистичные ожидания", "## ✅ Где AI-видео отлично\n\n- **Концепты, mood boards** — быстрые черновики\n- **Short-form реклама** (3-10 сек) — фон, абстракт, эффект\n- **Заставки и переходы**\n- **Анимационные циклы** для лоопов\n- **Stock-замена** — там, где нужны общие планы\n- **Music videos** — креативный, surrealistic стиль\n- **B-roll** — куда вставлять между основным\n\n## ❌ Где AI-видео ещё плохо\n\n- **Длинные нарративы** (>1 мин) — теряется консистентность\n- **Точные диалоги** — губы не синхронизируются идеально\n- **Конкретный человек** — твоё лицо или клиента (legal!) сложно\n- **Точное действие** («подними чашку правой рукой») — модель импровизирует\n- **Текст в кадре** — часто перевирает\n- **Документальная точность** — никаких фактов\n\n## Реальность\nAI-видео — **инструмент** в наборе. Не **замена** съёмки. Лучшие креаторы 2026 используют **гибрид**: реальная съёмка + AI-вставки + монтаж."),
                    sort_items([
                        ("✅ Хорошо работает", ["Концепт-видео", "Заставки 5 сек", "B-roll", "Абстрактные фоны", "Стилистические эффекты"]),
                        ("❌ Плохо работает", ["10-минутный фильм с сюжетом", "Точные движения по сценарию", "Текст в кадре", "Документальные факты", "Лицо конкретного человека"]),
                    ]),
                    multi("Где AI-видео реально полезен?", [
                        ("Заставки и переходы", True),
                        ("Концепт / mood board", True),
                        ("Музклипы с креативной картинкой", True),
                        ("Полнометражный документальный фильм", False),
                    ]),
                    tf("Лучшие креаторы используют AI-видео в гибриде с реальной съёмкой и монтажом.", True),
                ],
            },
        ],
    },
    {
        "title": "Промпты для видео",
        "pos": 1,
        "lessons": [
            {
                "t": "Структура промпта",
                "xp": 25,
                "steps": [
                    info("Формула SCENE", "## Структура хорошего промпта\n\n```\n[SUBJECT], [ACTION], [SETTING], [STYLE], [CAMERA], [LIGHTING], [MOOD]\n```\n\n### Пример плохого\n```\nКот\n```\n\n### Пример хорошего\n```\nA fluffy black cat with green eyes (SUBJECT) is slowly walking (ACTION) across a wet, neon-lit Tokyo alley at night (SETTING). Cinematic anime style with rain reflections (STYLE), low-angle dolly shot (CAMERA), soft purple and pink neon lighting (LIGHTING), mysterious and lonely atmosphere (MOOD).\n```\n\n## Главное правило\n**Будь конкретным.** Модель не угадает, что у тебя в голове. Лучше дать много деталей, чем мало."),
                    order([
                        "SUBJECT — кто/что в кадре",
                        "ACTION — что происходит",
                        "SETTING — где",
                        "STYLE — какой стиль (анимация, фотография, киноплёнка)",
                        "CAMERA — ракурс, движение камеры",
                        "LIGHTING — освещение",
                        "MOOD — настроение",
                    ]),
                    multi("Что входит в сильный промпт?", [
                        ("Конкретный subject с деталями", True),
                        ("Описание действия и среды", True),
                        ("Стиль и движение камеры", True),
                        ("Один общий запрос вроде 'красиво'", False),
                    ]),
                    tf("Чем подробнее промпт — тем ближе результат к задуманному.", True),
                ],
            },
            {
                "t": "Camera moves — кинематографический язык",
                "xp": 25,
                "steps": [
                    info("Главный buzz 2026", "## Типы движения камеры\n\n### Базовые\n- **Static** — камера неподвижна\n- **Pan** — вращение по горизонтали (стационарно)\n- **Tilt** — вращение по вертикали\n- **Zoom in/out** — приближение/отдаление\n\n### Сложные\n- **Dolly in/out** — камера ФИЗИЧЕСКИ движется к/от объекта\n- **Tracking shot** — следует за объектом\n- **Crane shot** — сверху вниз / снизу вверх\n- **Drone shot** — вид с дрона\n- **Steadicam** — плавный follow\n- **Whip pan** — быстрый pan, размытое движение\n- **Bullet time** — Matrix-эффект, медленно вокруг\n- **Orbit** — круговое движение вокруг объекта\n\n### Промпт-пример\n```\nA young woman dancing in a sunlit forest. Slow orbit camera move around her, golden hour lighting, cinematic depth of field.\n```\n\n## Higgsfield\nЭта модель **специализируется** на camera moves. У них библиотека пресетов — выбираешь стиль (Vertigo, Crash Zoom, Bullet Time) и применяется."),
                    match([
                        ("Pan", "Поворот камеры горизонтально"),
                        ("Dolly", "Камера физически движется к/от"),
                        ("Tracking", "Камера следует за объектом"),
                        ("Orbit", "Круговое движение вокруг"),
                        ("Drone shot", "Вид с дрона / сверху"),
                    ]),
                    multi("Что улучшает качество AI-видео?", [
                        ("Конкретные camera moves в промпте", True),
                        ("Описание lighting и mood", True),
                        ("Указание стиля", True),
                        ("Длина промпта в 1 слово", False),
                    ]),
                    quiz("Что специализируется на camera moves?", [
                        ("Higgsfield", True),
                        ("Apple Calculator", False),
                        ("Excel", False),
                    ]),
                ],
            },
            {
                "t": "Negative prompts и iteration",
                "xp": 20,
                "steps": [
                    info("Чего НЕ должно быть", "## Negative prompts\n\nНе все модели поддерживают, но где есть — мощный инструмент.\n\n### Что прописывать\n- Низкое качество: blurry, low quality, pixelated\n- Артефакты: extra fingers, deformed face, broken anatomy\n- Стиль: cartoon (если хочешь реализм), oversaturated\n- Текст: text, watermark, logo\n\n### Пример\n```\nPrompt: A man drinking coffee in a cafe...\n\nNegative: blurry, low quality, deformed face, extra fingers, oversaturated, watermark, text\n```\n\n## Итерация — главное умение\n\n### Первый рендер\nРедко идеальный. Это нормально.\n\n### Итерация\n1. Что НЕ так?\n2. Уточни промпт\n3. Сгенерируй снова\n4. Повтори 3-5 раз\n\n### Лайфхак: Image-to-video\nСначала сгенерируй **картинку** в MidJourney/DALL-E с нужной композицией. Потом подай как **референс** в AI-видео модель. **Гораздо точнее.**"),
                    multi("Что писать в negative prompt?", [
                        ("blurry, low quality", True),
                        ("deformed face, extra fingers", True),
                        ("watermark, text", True),
                        ("ничего никогда", False),
                    ]),
                    quiz("Image-to-video workflow — это:", [
                        ("Сначала сгенерировать картинку, потом превратить в видео", True),
                        ("Снять реальное видео", False),
                        ("Печатать текст", False),
                    ]),
                    tf("Image-to-video обычно даёт более точный результат, чем text-to-video.", True),
                ],
            },
        ],
    },
    {
        "title": "Workflow и продакшен",
        "pos": 2,
        "lessons": [
            {
                "t": "Сценарий → раскадровка → видео",
                "xp": 25,
                "steps": [
                    info("Структура продакшена", "## От идеи к готовому видео\n\n### 1. Концепция (15 мин)\nОдин абзац: что ты хочешь донести, для кого, какая эмоция.\n\n### 2. Сценарий (1 час)\nПо секундам: что в кадре, что в звуке.\n\n```\n0:00-0:03  Крупный план: глаз закрывается, расплывается\n0:03-0:06  Открывается в фантастическом мире\n0:06-0:09  Камера летит над городом будущего\n0:09-0:12  Возвращение, осознание\n```\n\n### 3. Раскадровка (2 часа)\nДля каждой сцены — генерируешь **картинку** в MidJourney с правильной композицией. Потом эти картинки = референсы для видео.\n\n### 4. Video generation (1-3 часа)\nДля каждой сцены — 2-3 генерации, выбираешь лучшую.\n\n### 5. Монтаж (1-2 часа)\nCapCut / Premiere:\n- Склейка сцен\n- Музыка\n- Звуковые эффекты\n- Цветокоррекция\n- Текст / титры\n\n### Реальные цифры\n30-секундный AI-ролик = **~6-10 часов** работы + $30-100 на генерации."),
                    order([
                        "Концепция — что и для кого",
                        "Сценарий по секундам",
                        "Раскадровка через image-генерацию (MidJourney)",
                        "Video generation по референсам",
                        "Монтаж и звук в CapCut/Premiere",
                    ]),
                    multi("Что делать перед video gen?", [
                        ("Сценарий по секундам", True),
                        ("Раскадровка через картинки", True),
                        ("Подбор музыки и SFX", True),
                        ("Сразу нажать кнопку", False),
                    ]),
                    tf("30-секундный AI-ролик требует около 6-10 часов работы.", True),
                ],
            },
            {
                "t": "Консистентность персонажа",
                "xp": 25,
                "steps": [
                    info("Главная проблема", "## Боль: в каждой сцене лицо разное\n\nКлассическая ошибка: в сцене 1 — блондинка, в сцене 2 — брюнетка с тем же именем.\n\n## Решения 2026\n\n### 1. Character reference\nМодели поддерживают **референсное фото**. Загружаешь 1-3 фото героини → в каждой генерации она.\n\n### 2. Embeddings / LoRA\nОбучаешь модель на 10-30 фото своего героя → используешь в промпте.\n\n### 3. Detailed description\nОчень подробное описание внешности — каждый раз одно и то же:\n```\n«Asian woman, age 28, shoulder-length straight black hair, almond eyes, fair skin, slim build, wearing white linen shirt and jeans...»\n```\nКопируй один блок в каждый промпт сцены.\n\n### 4. Image-to-video с одной и той же картинкой\nСгенерируй идеальную картинку героини. Используй её как референс для каждой сцены."),
                    multi("Как добиться консистентности персонажа?", [
                        ("Character reference (фото)", True),
                        ("Подробное описание, копируемое в каждый промпт", True),
                        ("Image-to-video с одной картинкой-референсом", True),
                        ("Надеяться на удачу", False),
                    ]),
                    quiz("Главная техническая проблема в нарративных AI-видео?", [
                        ("Длина", False),
                        ("Консистентность персонажа между сценами", True),
                        ("Шрифт", False),
                    ]),
                    tf("Image-to-video с одной картинкой даёт более консистентный результат, чем чистый text-to-video.", True),
                ],
            },
            {
                "t": "Звук и музыка",
                "xp": 15,
                "steps": [
                    info("Без звука — половина", "## Звук в AI-видео\n\n### Источники\n- **Veo 3** генерирует видео с аудио (диалоги, эффекты)\n- **Sora 2** — пока без звука по дефолту\n- **ElevenLabs** / **Suno** — генерация голоса и музыки отдельно\n- **Bibliothèque** платформ (Artlist, Epidemic Sound)\n\n## Музыка AI: Suno и Udio\n\n### Suno\n- Полная песня по тексту: 'Pop song about heartbreak in 80s style'\n- Бесплатно — 10 генераций в день\n- Pro $10/мес\n\n### Udio\n- Похоже, чуть лучшее качество для электроники\n\n## Workflow\n1. **Видео** в Sora/Veo/Runway\n2. **Музыка** в Suno (можно одну и ту же дорожку для нескольких роликов)\n3. **SFX** — Freesound.org или встроенные в CapCut\n4. **Голос** в ElevenLabs если нужно\n5. **Склейка** в CapCut/Premiere"),
                    match([
                        ("Sora 2", "Видео без звука по дефолту"),
                        ("Veo 3", "Видео + аудио сразу"),
                        ("ElevenLabs", "AI-голос"),
                        ("Suno", "AI-музыка по тексту"),
                        ("Udio", "AI-музыка, чуть другой стиль"),
                    ]),
                    multi("Что генерирует Suno?", [
                        ("Полную песню по описанию", True),
                        ("Музыку в разных жанрах", True),
                        ("Вокал и инструменты вместе", True),
                        ("Видео", False),
                    ]),
                    tf("Veo 3 — модель, которая генерирует видео уже со звуком.", True),
                ],
            },
        ],
    },
    {
        "title": "Use cases и кейсы",
        "pos": 3,
        "lessons": [
            {
                "t": "Реклама и контент-маркетинг",
                "xp": 20,
                "steps": [
                    info("Где экономия и скорость", "## Реклама с AI\n\n### Cases\n- **Coca-Cola** делала ролики на AI (Sora) для рождества 2024-2025\n- **Toys-R-Us** первая реклама полностью на Sora\n- **Heinz, Ryanair, Nike** — концепты и черновики\n\n### Преимущества\n- 🚀 **Скорость**: от идеи до ролика — день, а не месяц\n- 💰 **Стоимость**: $100-500 vs $10K-100K за классическую\n- 🌍 **Локализация**: разные версии для разных рынков\n- ⏱️ **A/B testing**: сгенерировать 10 вариантов, протестить, выбрать лучший\n\n### Ограничения\n- Юридические риски: нельзя использовать лица реальных людей без согласия\n- Brand safety: AI может сгенерировать нежелательное\n- Качество: для премиум-брендов всё ещё уступает реальной съёмке\n\n## Forматы рекламы где работает\n1. **Pre-roll YouTube** 5-15 сек\n2. **Reels/TikTok** креативы\n3. **Display banners** анимированные\n4. **Презентации продуктов**\n5. **In-game реклама**"),
                    multi("Где AI-видео ОК в рекламе?", [
                        ("Тестовые креативы для A/B", True),
                        ("Локализация под разные рынки", True),
                        ("Pre-roll 5-15 секунд", True),
                        ("Презентация конкретного человека-CEO", False),
                    ]),
                    tf("AI-видео сильно снижает стоимость и время до ролика по сравнению с классической съёмкой.", True),
                    quiz("Какие риски AI-видео в рекламе?", [
                        ("Юридические (лица людей)", True),
                        ("Brand safety", True),
                        ("Скорость", False),
                    ]),
                ],
            },
            {
                "t": "Творческие проекты: музклипы, арт",
                "xp": 20,
                "steps": [
                    info("Где AI силён", "## Музклипы\n\nAI-видео **отлично подходит** для:\n- Сюрреалистических визуалов\n- Абстрактных переходов\n- Стилизованных эпизодов\n- Альбомных трейлеров\n\n### Кейсы\n- **Lil Yachty**, **Linkin Park** — клипы с AI-сценами\n- **The Weeknd** — концепты\n- Indie-артисты с бюджетом 0 — целые клипы на AI\n\n## Арт-фильмы\n- **Surrealist** жанр идеально подходит\n- Анимация мечтаний, воспоминаний\n- Концепции вне физических ограничений\n\n## Игры и storytelling\n- Заставки игр\n- Trailer для inde-проектов\n- Cinematic cutscenes\n\n## Twitter / X — короткие сценки\nДоминируют 'AI shorts' аккаунты с 100K+ подписчиков, делают по 3-5 видео в неделю на бесконечные темы."),
                    multi("Где AI-видео творчески сильно?", [
                        ("Сюрреалистичные музклипы", True),
                        ("Концепты и трейлеры", True),
                        ("Анимация воспоминаний/мечтаний", True),
                        ("Документалистика", False),
                    ]),
                    tf("Indie-артист с нулевым бюджетом теперь может сделать полный музклип на AI.", True),
                    quiz("Какие жанры идеально подходят AI-видео?", [
                        ("Сюрреализм, абстрактное", True),
                        ("Документальный репортаж с фактами", False),
                        ("Юридический сериал с показанием в суде", False),
                    ]),
                ],
            },
            {
                "t": "Этика, авторские права, риски",
                "xp": 20,
                "steps": [
                    info("Что важно знать", "## Этические вопросы\n\n### 1. Дипфейки\nГенерировать видео с лицом конкретного человека (актёра, политика) **без согласия** — незаконно во многих юрисдикциях.\n- EU AI Act требует маркировки\n- В РФ — закон о персональных данных\n- В США — деликтное право\n\n### 2. Авторские права\n- **На обучающие данные** — судебные иски Getty, NY Times против OpenAI\n- **На вывод** — обычно ты владеешь сгенерированным (но не Sora 2 free tier)\n- **На стиль** — копировать стиль конкретного художника = серая зона\n\n### 3. Маркировка\nС 2025-2026 многие страны вводят **обязательную маркировку** AI-контента:\n- C2PA — стандарт от Adobe/Microsoft\n- Невидимые watermark от Google (SynthID)\n\n### 4. Misuse\nAI-видео используется для пропаганды, дезинформации, мошенничества. Будь ответственным.\n\n## Чеклист\n- [ ] Не использую лица без согласия\n- [ ] Не пытаюсь обмануть зрителя (выдать AI за реальность)\n- [ ] Маркирую если требуется законом\n- [ ] Не нарушаю чужие копирайты явно"),
                    multi("Что нельзя делать с AI-видео?", [
                        ("Генерировать лица конкретных людей без согласия", True),
                        ("Выдавать AI-контент за реальные новости", True),
                        ("Использовать для мошенничества", True),
                        ("Делать музклип со сюрреалистичными сценами", False),
                    ]),
                    tf("В EU AI Act требуется маркировка AI-генерированного контента.", True),
                    quiz("Какая система невидимой маркировки от Google?", [
                        ("C2PA", False),
                        ("SynthID", True),
                        ("Watermark Pro", False),
                    ]),
                    cards([
                        ("Sora 2", "OpenAI, реализм, до 60 сек"),
                        ("Veo 3", "Google, видео + аудио"),
                        ("Higgsfield", "Camera moves"),
                        ("Suno / Udio", "AI-музыка"),
                        ("ElevenLabs", "AI-голос"),
                        ("C2PA / SynthID", "Маркировка AI-контента"),
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
            title=T, slug="ai-video-gen-" + uuid.uuid4().hex[:4], description=DESC,
            author_id=author.id, category="AI", difficulty="Beginner",
            price=0, currency="USD", status="published",
            tags=["AI", "Video", "Creative", "Marketing", "Tools"],
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
