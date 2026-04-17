"""Seed: Турецкий язык — Начальный курс. 8 sections, 40 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSE_TITLE = "Турецкий язык — Начальный курс"
COURSE_SLUG = "turkish-beginner-" + uuid.uuid4().hex[:4]
COURSE_DESC = (
    "Начальный курс турецкого языка: алфавит, произношение, грамматика, "
    "бытовая лексика, диалоги. Гармония гласных, аффиксы, базовые конструкции."
)

SECTIONS = [
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 1: Алфавит и произношение
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Алфавит и произношение",
        "pos": 0,
        "lessons": [
            {
                "t": "Турецкий алфавит — 29 букв",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Турецкий алфавит", "markdown": "## Турецкий алфавит — 29 букв\n\nТурецкий алфавит основан на латинице и содержит **29 букв**.\n\n### Все буквы:\nA B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z\n\n### Особые буквы (которых нет в английском):\n| Буква | Звук | Пример |\n|-------|------|--------|\n| **Ç ç** | [ч] | **ç**ay — чай |\n| **Ğ ğ** | удлиняет гласную | da**ğ** — гора |\n| **I ı** | [ы] | **ı**rmak — река |\n| **İ i** | [и] | **i**stanbul |\n| **Ö ö** | [ё] | **ö**ğretmen — учитель |\n| **Ş ş** | [ш] | **ş**eker — сахар |\n| **Ü ü** | [ю] | **ü**niversite — университет |\n\n### Важно:\n- В турецком **нет** букв Q, W, X\n- Буквы **I/ı** (без точки) и **İ/i** (с точкой) — это РАЗНЫЕ буквы!"},
                    {"type": "flashcards", "cards": [{"front": "Ç ç", "back": "Звук [ч] — çay (чай)"}, {"front": "Ğ ğ", "back": "Удлиняет гласную — dağ (гора)"}, {"front": "I ı", "back": "Звук [ы] — ırmak (река)"}, {"front": "İ i", "back": "Звук [и] — İstanbul"}, {"front": "Ö ö", "back": "Звук [ё] — öğretmen (учитель)"}, {"front": "Ş ş", "back": "Звук [ш] — şeker (сахар)"}, {"front": "Ü ü", "back": "Звук [ю] — üniversite (университет)"}]},
                    {"type": "matching", "pairs": [{"left": "Ç", "right": "[ч]"}, {"left": "Ş", "right": "[ш]"}, {"left": "Ö", "right": "[ё]"}, {"left": "Ü", "right": "[ю]"}, {"left": "I (без точки)", "right": "[ы]"}]},
                    {"type": "quiz", "question": "Сколько букв в турецком алфавите?", "options": [{"id": "a", "text": "26", "correct": False}, {"id": "b", "text": "29", "correct": True}, {"id": "c", "text": "33", "correct": False}, {"id": "d", "text": "31", "correct": False}]},
                    {"type": "true-false", "statement": "В турецком алфавите есть буквы Q, W и X.", "correct": False},
                    {"type": "multi-select", "question": "Какие буквы являются особыми турецкими (нет в английском)?", "options": [{"id": "a", "text": "Ç", "correct": True}, {"id": "b", "text": "B", "correct": False}, {"id": "c", "text": "Ş", "correct": True}, {"id": "d", "text": "Ğ", "correct": True}, {"id": "e", "text": "K", "correct": False}]},
                    {"type": "type-answer", "question": "Какая турецкая буква обозначает звук [ч]?", "acceptedAnswers": ["Ç", "ç"]},
                    {"type": "quiz", "question": "Чем отличаются буквы I и İ в турецком?", "options": [{"id": "a", "text": "Ничем не отличаются", "correct": False}, {"id": "b", "text": "I (без точки) = [ы], İ (с точкой) = [и]", "correct": True}, {"id": "c", "text": "I = прописная, İ = строчная", "correct": False}, {"id": "d", "text": "Одна гласная, другая согласная", "correct": False}]},
                    {"type": "fill-blank", "text": "В турецком алфавите ___ букв.", "answers": ["29"]},
                    {"type": "drag-order", "items": ["A", "B", "C", "Ç", "D", "E", "F"]},
                ],
            },
            {
                "t": "Гласные звуки турецкого языка",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "8 гласных турецкого языка", "markdown": "## 8 гласных звуков\n\nВ турецком языке **8 гласных** — это основа системы гармонии гласных.\n\n### Таблица гласных:\n| | **Передние** | **Задние** |\n|---|---|---|\n| **Закрытые, неогубл.** | i | ı |\n| **Закрытые, огубл.** | ü | u |\n| **Открытые, неогубл.** | e | a |\n| **Открытые, огубл.** | ö | o |\n\n### Примеры:\n- **a** — araba (машина)\n- **e** — ev (дом)\n- **ı** — sıcak (горячий)\n- **i** — bir (один)\n- **o** — okul (школа)\n- **ö** — göz (глаз)\n- **u** — uzun (длинный)\n- **ü** — gül (роза)\n\n### Запомните:\n- Передние: **e, i, ö, ü**\n- Задние: **a, ı, o, u**"},
                    {"type": "flashcards", "cards": [{"front": "araba", "back": "машина"}, {"front": "ev", "back": "дом"}, {"front": "okul", "back": "школа"}, {"front": "göz", "back": "глаз"}, {"front": "gül", "back": "роза"}, {"front": "bir", "back": "один"}, {"front": "uzun", "back": "длинный"}, {"front": "sıcak", "back": "горячий"}]},
                    {"type": "matching", "pairs": [{"left": "araba", "right": "машина"}, {"left": "ev", "right": "дом"}, {"left": "okul", "right": "школа"}, {"left": "göz", "right": "глаз"}, {"left": "gül", "right": "роза"}]},
                    {"type": "quiz", "question": "Сколько гласных букв в турецком языке?", "options": [{"id": "a", "text": "5", "correct": False}, {"id": "b", "text": "6", "correct": False}, {"id": "c", "text": "8", "correct": True}, {"id": "d", "text": "10", "correct": False}]},
                    {"type": "category-sort", "categories": ["Передние гласные", "Задние гласные"], "items": [{"text": "e", "category": "Передние гласные"}, {"text": "i", "category": "Передние гласные"}, {"text": "ö", "category": "Передние гласные"}, {"text": "ü", "category": "Передние гласные"}, {"text": "a", "category": "Задние гласные"}, {"text": "ı", "category": "Задние гласные"}, {"text": "o", "category": "Задние гласные"}, {"text": "u", "category": "Задние гласные"}]},
                    {"type": "type-answer", "question": "Переведите на турецкий: дом", "acceptedAnswers": ["ev", "Ev"]},
                    {"type": "true-false", "statement": "В турецком языке 5 гласных, как в английском.", "correct": False},
                    {"type": "fill-blank", "text": "Передние гласные: e, i, ö, ___", "answers": ["ü"]},
                    {"type": "multi-select", "question": "Какие гласные являются задними?", "options": [{"id": "a", "text": "a", "correct": True}, {"id": "b", "text": "e", "correct": False}, {"id": "c", "text": "ı", "correct": True}, {"id": "d", "text": "ö", "correct": False}, {"id": "e", "text": "u", "correct": True}]},
                    {"type": "drag-order", "items": ["a", "e", "ı", "i", "o", "ö", "u", "ü"]},
                ],
            },
            {
                "t": "Согласные и произношение",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Согласные звуки", "markdown": "## Согласные звуки турецкого языка\n\nВ турецком **21 согласная**. Большинство произносятся как в русском, но есть особенности:\n\n### Особые согласные:\n| Буква | Звук | Пример |\n|-------|------|--------|\n| **C c** | [дж] | **c**am — стекло |\n| **Ç ç** | [ч] | **ç**ay — чай |\n| **G g** | [г] | **g**el — приходи |\n| **Ğ ğ** | удлиняет гласную | da**ğ** — гора |\n| **H h** | [х] (мягкий) | **h**ava — воздух |\n| **J j** | [ж] | **j**andarma — жандарм |\n| **Ş ş** | [ш] | **ş**ehir — город |\n| **Y y** | [й] | **y**aş — возраст |\n\n### Важно:\n- **C** = [дж], НЕ [к] как в английском!\n- **Ğ** (юмушак ге) никогда не стоит в начале слова\n- Турецкие согласные могут быть глухими и звонкими"},
                    {"type": "flashcards", "cards": [{"front": "cam", "back": "стекло [джам]"}, {"front": "çay", "back": "чай [чай]"}, {"front": "dağ", "back": "гора [даа]"}, {"front": "hava", "back": "воздух [хава]"}, {"front": "şehir", "back": "город [шехир]"}, {"front": "gel", "back": "приходи [гель]"}]},
                    {"type": "matching", "pairs": [{"left": "C", "right": "[дж]"}, {"left": "Ç", "right": "[ч]"}, {"left": "Ş", "right": "[ш]"}, {"left": "J", "right": "[ж]"}, {"left": "H", "right": "[х]"}, {"left": "Y", "right": "[й]"}]},
                    {"type": "quiz", "question": "Как произносится турецкая буква C?", "options": [{"id": "a", "text": "[к] как в английском", "correct": False}, {"id": "b", "text": "[ц] как в немецком", "correct": False}, {"id": "c", "text": "[дж] как в слове «джем»", "correct": True}, {"id": "d", "text": "[с] как в русском", "correct": False}]},
                    {"type": "true-false", "statement": "Буква Ğ может стоять в начале турецкого слова.", "correct": False},
                    {"type": "type-answer", "question": "Переведите на турецкий: чай", "acceptedAnswers": ["çay", "Çay"]},
                    {"type": "type-answer", "question": "Переведите на турецкий: гора", "acceptedAnswers": ["dağ", "Dağ"]},
                    {"type": "fill-blank", "text": "Буква C в турецком произносится как [___].", "answers": ["дж"]},
                    {"type": "multi-select", "question": "Какие утверждения верны?", "options": [{"id": "a", "text": "C произносится как [дж]", "correct": True}, {"id": "b", "text": "Ğ удлиняет предыдущую гласную", "correct": True}, {"id": "c", "text": "H не произносится", "correct": False}, {"id": "d", "text": "Ş произносится как [ш]", "correct": True}]},
                    {"type": "drag-order", "items": ["cam — [дж]ам", "çay — [ч]ай", "şehir — [ш]ехир", "jandarma — [ж]андарма"]},
                ],
            },
            {
                "t": "Ударение и интонация",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Ударение в турецком", "markdown": "## Ударение\n\nВ турецком языке ударение обычно падает на **последний слог**.\n\n### Основные правила:\n1. **Обычные слова** — ударение на последнем слоге:\n   - kitap → kita**P** (книга)\n   - araba → araba**A** (машина)\n\n2. **Исключения — ударение НЕ на последнем слоге:**\n   - Географические названия: **An**kara, **İs**tanbul\n   - Наречия: **şim**di (сейчас), **son**ra (потом)\n   - Заимствования: **lo**kanta (ресторан)\n   - Отрицание -me/-ma: gel**ME** (не приходи)\n\n3. **Вопросительная частица mı/mi/mu/mü** — безударная:\n   - Geliyor **mu**sun? (Ты идёшь?)\n\n### Интонация:\n- Утверждение — нисходящая ↘\n- Вопрос с mı — восходящая ↗\n- Вопрос с вопросительным словом — нисходящая ↘"},
                    {"type": "quiz", "question": "На какой слог обычно падает ударение в турецком?", "options": [{"id": "a", "text": "На первый", "correct": False}, {"id": "b", "text": "На последний", "correct": True}, {"id": "c", "text": "На предпоследний", "correct": False}, {"id": "d", "text": "Ударения нет", "correct": False}]},
                    {"type": "true-false", "statement": "В слове İstanbul ударение на последнем слоге.", "correct": False},
                    {"type": "true-false", "statement": "Вопросительная частица mı/mi всегда безударна.", "correct": True},
                    {"type": "category-sort", "categories": ["Ударение на последнем слоге", "Ударение НЕ на последнем слоге"], "items": [{"text": "kitap (книга)", "category": "Ударение на последнем слоге"}, {"text": "araba (машина)", "category": "Ударение на последнем слоге"}, {"text": "Ankara", "category": "Ударение НЕ на последнем слоге"}, {"text": "şimdi (сейчас)", "category": "Ударение НЕ на последнем слоге"}, {"text": "lokanta (ресторан)", "category": "Ударение НЕ на последнем слоге"}, {"text": "deniz (море)", "category": "Ударение на последнем слоге"}]},
                    {"type": "flashcards", "cards": [{"front": "kitap", "back": "книга (ударение: kitaP)"}, {"front": "şimdi", "back": "сейчас (ударение: ŞIMdi)"}, {"front": "sonra", "back": "потом (ударение: SONra)"}, {"front": "lokanta", "back": "ресторан (ударение: loKANta)"}]},
                    {"type": "fill-blank", "text": "В турецком языке ударение обычно падает на ___ слог.", "answers": ["последний"]},
                    {"type": "matching", "pairs": [{"left": "Утверждение", "right": "Нисходящая интонация ↘"}, {"left": "Вопрос с mı", "right": "Восходящая интонация ↗"}, {"left": "Вопрос с вопросительным словом", "right": "Нисходящая интонация ↘"}]},
                    {"type": "quiz", "question": "Какая интонация в вопросах с частицей mı/mi?", "options": [{"id": "a", "text": "Нисходящая", "correct": False}, {"id": "b", "text": "Восходящая", "correct": True}, {"id": "c", "text": "Ровная", "correct": False}, {"id": "d", "text": "Зависит от слова", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова являются исключениями (ударение НЕ на последнем слоге)?", "options": [{"id": "a", "text": "Ankara", "correct": True}, {"id": "b", "text": "kitap", "correct": False}, {"id": "c", "text": "şimdi", "correct": True}, {"id": "d", "text": "deniz", "correct": False}]},
                ],
            },
            {
                "t": "Приветствия и базовые фразы",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Merhaba! Приветствия", "markdown": "## Приветствия и базовые фразы\n\n### Приветствия:\n| Турецкий | Русский |\n|----------|--------|\n| **Merhaba** | Привет / Здравствуйте |\n| **Selam** | Привет (неформально) |\n| **Günaydın** | Доброе утро |\n| **İyi günler** | Добрый день |\n| **İyi akşamlar** | Добрый вечер |\n| **İyi geceler** | Спокойной ночи |\n\n### Прощания:\n| Турецкий | Русский |\n|----------|--------|\n| **Hoşça kal** | Пока (говорит уходящий) |\n| **Güle güle** | Пока (говорит остающийся) |\n| **Görüşürüz** | Увидимся |\n\n### Вежливость:\n| Турецкий | Русский |\n|----------|--------|\n| **Hoş geldiniz** | Добро пожаловать |\n| **Hoş bulduk** | Ответ на «Добро пожаловать» |\n| **Teşekkür ederim** | Спасибо |\n| **Rica ederim** | Пожалуйста (в ответ на спасибо) |\n| **Lütfen** | Пожалуйста (просьба) |\n| **Affedersiniz** | Извините |"},
                    {"type": "flashcards", "cards": [{"front": "Merhaba", "back": "Привет / Здравствуйте"}, {"front": "Günaydın", "back": "Доброе утро"}, {"front": "İyi akşamlar", "back": "Добрый вечер"}, {"front": "Hoş geldiniz", "back": "Добро пожаловать"}, {"front": "Teşekkür ederim", "back": "Спасибо"}, {"front": "Güle güle", "back": "Пока (говорит остающийся)"}, {"front": "Lütfen", "back": "Пожалуйста (просьба)"}, {"front": "Affedersiniz", "back": "Извините"}]},
                    {"type": "matching", "pairs": [{"left": "Merhaba", "right": "Привет"}, {"left": "Günaydın", "right": "Доброе утро"}, {"left": "Teşekkür ederim", "right": "Спасибо"}, {"left": "Lütfen", "right": "Пожалуйста"}, {"left": "Hoş geldiniz", "right": "Добро пожаловать"}, {"left": "Güle güle", "right": "Пока"}]},
                    {"type": "quiz", "question": "Как сказать «Добро пожаловать» по-турецки?", "options": [{"id": "a", "text": "Merhaba", "correct": False}, {"id": "b", "text": "Hoş geldiniz", "correct": True}, {"id": "c", "text": "Günaydın", "correct": False}, {"id": "d", "text": "Teşekkür ederim", "correct": False}]},
                    {"type": "type-answer", "question": "Как сказать «спасибо» по-турецки?", "acceptedAnswers": ["Teşekkür ederim", "teşekkür ederim"]},
                    {"type": "type-answer", "question": "Как сказать «привет» по-турецки?", "acceptedAnswers": ["Merhaba", "merhaba", "Selam", "selam"]},
                    {"type": "true-false", "statement": "Hoş geldiniz — это приветствие, а Hoş bulduk — ответ на него.", "correct": True},
                    {"type": "fill-blank", "text": "— Hoş geldiniz!\n— Hoş ___!", "answers": ["bulduk"]},
                    {"type": "quiz", "question": "Кто говорит «Güle güle»?", "options": [{"id": "a", "text": "Тот, кто уходит", "correct": False}, {"id": "b", "text": "Тот, кто остаётся", "correct": True}, {"id": "c", "text": "Оба собеседника", "correct": False}, {"id": "d", "text": "Только формально", "correct": False}]},
                    {"type": "drag-order", "items": ["Merhaba! (привет)", "Hoş geldiniz! (добро пожаловать)", "Hoş bulduk! (ответ)", "Teşekkür ederim! (спасибо)", "Güle güle! (пока)"]},
                    {"type": "multi-select", "question": "Какие фразы используются для прощания?", "options": [{"id": "a", "text": "Hoşça kal", "correct": True}, {"id": "b", "text": "Güle güle", "correct": True}, {"id": "c", "text": "Görüşürüz", "correct": True}, {"id": "d", "text": "Günaydın", "correct": False}, {"id": "e", "text": "Merhaba", "correct": False}]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 2: Знакомство
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Знакомство",
        "pos": 1,
        "lessons": [
            {
                "t": "Adınız ne? — Как вас зовут?",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Знакомство по-турецки", "markdown": "## Adınız ne? — Как вас зовут?\n\n### Основные фразы:\n| Турецкий | Русский |\n|----------|--------|\n| **Adınız ne?** | Как вас зовут? (формально) |\n| **Adın ne?** | Как тебя зовут? (неформально) |\n| **Benim adım...** | Меня зовут... |\n| **Tanıştığımıza memnunum** | Приятно познакомиться |\n| **Nasılsınız?** | Как дела? (формально) |\n| **Nasılsın?** | Как дела? (неформально) |\n| **İyiyim, teşekkürler** | Хорошо, спасибо |\n| **Ya siz?** | А вы? |\n\n### Диалог:\n— Merhaba! Adınız ne?\n— Merhaba! Benim adım Ali. Ya sizin adınız?\n— Benim adım Ayşe. Tanıştığımıza memnunum.\n— Ben de memnunum. Nasılsınız?\n— İyiyim, teşekkürler. Ya siz?\n— Ben de iyiyim."},
                    {"type": "flashcards", "cards": [{"front": "Adınız ne?", "back": "Как вас зовут? (формально)"}, {"front": "Benim adım...", "back": "Меня зовут..."}, {"front": "Tanıştığımıza memnunum", "back": "Приятно познакомиться"}, {"front": "Nasılsınız?", "back": "Как дела? (формально)"}, {"front": "İyiyim", "back": "Хорошо (я в порядке)"}, {"front": "Ya siz?", "back": "А вы?"}]},
                    {"type": "matching", "pairs": [{"left": "Adınız ne?", "right": "Как вас зовут?"}, {"left": "Benim adım...", "right": "Меня зовут..."}, {"left": "Nasılsınız?", "right": "Как дела?"}, {"left": "İyiyim", "right": "Хорошо"}, {"left": "Ya siz?", "right": "А вы?"}]},
                    {"type": "quiz", "question": "Как сказать «Меня зовут Али» по-турецки?", "options": [{"id": "a", "text": "Adım Ali", "correct": False}, {"id": "b", "text": "Benim adım Ali", "correct": True}, {"id": "c", "text": "Ali benim", "correct": False}, {"id": "d", "text": "Ben Ali adım", "correct": False}]},
                    {"type": "type-answer", "question": "Как спросить «Как дела?» формально?", "acceptedAnswers": ["Nasılsınız?", "nasılsınız?", "Nasılsınız"]},
                    {"type": "fill-blank", "text": "— Adınız ne?\n— Benim ___ Ayşe.", "answers": ["adım"]},
                    {"type": "true-false", "statement": "Adın ne? — это формальная форма вопроса «Как вас зовут?».", "correct": False},
                    {"type": "drag-order", "items": ["Merhaba!", "Adınız ne?", "Benim adım Ali.", "Tanıştığımıza memnunum.", "Nasılsınız?", "İyiyim, teşekkürler."]},
                    {"type": "quiz", "question": "Что означает «Tanıştığımıza memnunum»?", "options": [{"id": "a", "text": "До свидания", "correct": False}, {"id": "b", "text": "Приятно познакомиться", "correct": True}, {"id": "c", "text": "Как дела?", "correct": False}, {"id": "d", "text": "Спасибо", "correct": False}]},
                    {"type": "multi-select", "question": "Какие фразы используются при знакомстве?", "options": [{"id": "a", "text": "Adınız ne?", "correct": True}, {"id": "b", "text": "Benim adım...", "correct": True}, {"id": "c", "text": "Güle güle", "correct": False}, {"id": "d", "text": "Tanıştığımıza memnunum", "correct": True}]},
                ],
            },
            {
                "t": "Числа от 1 до 20",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Числа 1-20", "markdown": "## Числа от 1 до 20\n\n| Число | Турецкий | | Число | Турецкий |\n|-------|----------|-|-------|----------|\n| 1 | **bir** | | 11 | **on bir** |\n| 2 | **iki** | | 12 | **on iki** |\n| 3 | **üç** | | 13 | **on üç** |\n| 4 | **dört** | | 14 | **on dört** |\n| 5 | **beş** | | 15 | **on beş** |\n| 6 | **altı** | | 16 | **on altı** |\n| 7 | **yedi** | | 17 | **on yedi** |\n| 8 | **sekiz** | | 18 | **on sekiz** |\n| 9 | **dokuz** | | 19 | **on dokuz** |\n| 10 | **on** | | 20 | **yirmi** |\n\n### Принцип:\nЧисла 11-19 = **on** + единица (on bir = 10+1)"},
                    {"type": "flashcards", "cards": [{"front": "bir", "back": "1"}, {"front": "iki", "back": "2"}, {"front": "üç", "back": "3"}, {"front": "dört", "back": "4"}, {"front": "beş", "back": "5"}, {"front": "altı", "back": "6"}, {"front": "yedi", "back": "7"}, {"front": "sekiz", "back": "8"}, {"front": "dokuz", "back": "9"}, {"front": "on", "back": "10"}]},
                    {"type": "matching", "pairs": [{"left": "bir", "right": "1"}, {"left": "üç", "right": "3"}, {"left": "beş", "right": "5"}, {"left": "yedi", "right": "7"}, {"left": "on", "right": "10"}, {"left": "yirmi", "right": "20"}]},
                    {"type": "type-answer", "question": "Как будет 5 по-турецки?", "acceptedAnswers": ["beş", "Beş"]},
                    {"type": "type-answer", "question": "Как будет 15 по-турецки?", "acceptedAnswers": ["on beş", "On beş"]},
                    {"type": "quiz", "question": "Как сказать 17 по-турецки?", "options": [{"id": "a", "text": "yedi on", "correct": False}, {"id": "b", "text": "on yedi", "correct": True}, {"id": "c", "text": "yirmi yedi", "correct": False}, {"id": "d", "text": "bir yedi", "correct": False}]},
                    {"type": "fill-blank", "text": "12 по-турецки = on ___", "answers": ["iki"]},
                    {"type": "true-false", "statement": "Число 14 по-турецки — dört on.", "correct": False},
                    {"type": "drag-order", "items": ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on"]},
                    {"type": "multi-select", "question": "Какие числа правильно написаны?", "options": [{"id": "a", "text": "on bir = 11", "correct": True}, {"id": "b", "text": "on üç = 13", "correct": True}, {"id": "c", "text": "iki on = 12", "correct": False}, {"id": "d", "text": "yirmi = 20", "correct": True}]},
                ],
            },
            {
                "t": "Ülkeler — Страны и национальности",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Страны и национальности", "markdown": "## Ülkeler ve Milletler — Страны и национальности\n\n### Страны:\n| Турецкий | Русский |\n|----------|--------|\n| **Türkiye** | Турция |\n| **Rusya** | Россия |\n| **Kazakistan** | Казахстан |\n| **Almanya** | Германия |\n| **İngiltere** | Англия |\n| **Fransa** | Франция |\n| **Amerika** | Америка |\n| **Japonya** | Япония |\n\n### Национальности (суффикс -lı/-li/-lu/-lü):\n| Я из... | Я... |\n|---------|------|\n| Türkiye**li** | турок/турчанка |\n| Rusya**lı** | русский/русская |\n| Alman | немец/немка |\n| Fransız | француз/француженка |\n\n### Фразы:\n- **Nerelisiniz?** — Откуда вы?\n- **Ben Rusyalıyım** — Я из России\n- **Türkiyeliyim** — Я из Турции"},
                    {"type": "flashcards", "cards": [{"front": "Türkiye", "back": "Турция"}, {"front": "Rusya", "back": "Россия"}, {"front": "Almanya", "back": "Германия"}, {"front": "Japonya", "back": "Япония"}, {"front": "Nerelisiniz?", "back": "Откуда вы?"}, {"front": "Ben Rusyalıyım", "back": "Я из России"}]},
                    {"type": "matching", "pairs": [{"left": "Türkiye", "right": "Турция"}, {"left": "Rusya", "right": "Россия"}, {"left": "Almanya", "right": "Германия"}, {"left": "İngiltere", "right": "Англия"}, {"left": "Fransa", "right": "Франция"}, {"left": "Japonya", "right": "Япония"}]},
                    {"type": "quiz", "question": "Как спросить «Откуда вы?» по-турецки?", "options": [{"id": "a", "text": "Nasılsınız?", "correct": False}, {"id": "b", "text": "Nerelisiniz?", "correct": True}, {"id": "c", "text": "Adınız ne?", "correct": False}, {"id": "d", "text": "Ne yapıyorsunuz?", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «Россия»?", "acceptedAnswers": ["Rusya", "rusya"]},
                    {"type": "fill-blank", "text": "Ben ___yalıyım. (Я из России)", "answers": ["Rus"]},
                    {"type": "true-false", "statement": "Almanya — это Англия по-турецки.", "correct": False},
                    {"type": "type-answer", "question": "Как по-турецки «Турция»?", "acceptedAnswers": ["Türkiye", "türkiye"]},
                    {"type": "quiz", "question": "Какой суффикс образует национальность от названия страны?", "options": [{"id": "a", "text": "-cı/-ci", "correct": False}, {"id": "b", "text": "-lı/-li/-lu/-lü", "correct": True}, {"id": "c", "text": "-sız/-siz", "correct": False}, {"id": "d", "text": "-lar/-ler", "correct": False}]},
                    {"type": "multi-select", "question": "Какие пары «страна — перевод» верны?", "options": [{"id": "a", "text": "Japonya — Япония", "correct": True}, {"id": "b", "text": "İngiltere — Италия", "correct": False}, {"id": "c", "text": "Fransa — Франция", "correct": True}, {"id": "d", "text": "Almanya — Германия", "correct": True}]},
                ],
            },
            {
                "t": "Meslekler — Профессии",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Профессии по-турецки", "markdown": "## Meslekler — Профессии\n\n| Турецкий | Русский |\n|----------|--------|\n| **öğretmen** | учитель |\n| **doktor** | врач |\n| **mühendis** | инженер |\n| **avukat** | адвокат |\n| **öğrenci** | студент |\n| **hemşire** | медсестра |\n| **polis** | полицейский |\n| **aşçı** | повар |\n| **şoför** | водитель |\n| **garson** | официант |\n\n### Как сказать свою профессию:\n- **Ben öğretmenim** — Я учитель\n- **Ben doktorum** — Я врач\n- **Ben öğrenciyim** — Я студент\n\n### Как спросить:\n- **Mesleğiniz ne?** — Какая у вас профессия?\n- **Ne iş yapıyorsunuz?** — Чем вы занимаетесь?"},
                    {"type": "flashcards", "cards": [{"front": "öğretmen", "back": "учитель"}, {"front": "doktor", "back": "врач"}, {"front": "mühendis", "back": "инженер"}, {"front": "avukat", "back": "адвокат"}, {"front": "öğrenci", "back": "студент"}, {"front": "aşçı", "back": "повар"}, {"front": "şoför", "back": "водитель"}, {"front": "garson", "back": "официант"}]},
                    {"type": "matching", "pairs": [{"left": "öğretmen", "right": "учитель"}, {"left": "doktor", "right": "врач"}, {"left": "mühendis", "right": "инженер"}, {"left": "öğrenci", "right": "студент"}, {"left": "aşçı", "right": "повар"}, {"left": "garson", "right": "официант"}]},
                    {"type": "quiz", "question": "Как сказать «Я врач» по-турецки?", "options": [{"id": "a", "text": "Ben doktorum", "correct": True}, {"id": "b", "text": "Ben doktor", "correct": False}, {"id": "c", "text": "Doktor benim", "correct": False}, {"id": "d", "text": "Ben bir doktor var", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: учитель", "acceptedAnswers": ["öğretmen", "Öğretmen"]},
                    {"type": "type-answer", "question": "Переведите: студент", "acceptedAnswers": ["öğrenci", "Öğrenci"]},
                    {"type": "fill-blank", "text": "Ben ___yim. (Я студент)", "answers": ["öğrenci"]},
                    {"type": "true-false", "statement": "Aşçı — это адвокат по-турецки.", "correct": False},
                    {"type": "quiz", "question": "Как спросить «Какая у вас профессия?»", "options": [{"id": "a", "text": "Mesleğiniz ne?", "correct": True}, {"id": "b", "text": "Adınız ne?", "correct": False}, {"id": "c", "text": "Nerelisiniz?", "correct": False}, {"id": "d", "text": "Kaç yaşındasınız?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие переводы верны?", "options": [{"id": "a", "text": "polis — полицейский", "correct": True}, {"id": "b", "text": "hemşire — медсестра", "correct": True}, {"id": "c", "text": "şoför — повар", "correct": False}, {"id": "d", "text": "garson — официант", "correct": True}]},
                ],
            },
            {
                "t": "Ben, Sen, O — Личные местоимения",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Личные местоимения", "markdown": "## Личные местоимения\n\n| Турецкий | Русский |\n|----------|--------|\n| **Ben** | Я |\n| **Sen** | Ты |\n| **O** | Он/Она/Оно |\n| **Biz** | Мы |\n| **Siz** | Вы (мн./вежл.) |\n| **Onlar** | Они |\n\n### Глагол «быть» (именное сказуемое):\n| Местоимение | Суффикс | Пример |\n|------------|---------|--------|\n| Ben | -(y)ım/-(y)im/-(y)um/-(y)üm | Ben öğretmen**im** |\n| Sen | -sın/-sin/-sun/-sün | Sen doktor**sun** |\n| O | — (нулевой) | O mühendis |\n| Biz | -(y)ız/-(y)iz/-(y)uz/-(y)üz | Biz öğrenci**yiz** |\n| Siz | -sınız/-siniz/-sunuz/-sünüz | Siz Türk**sünüz** |\n| Onlar | -(lar/ler) | Onlar doktor(lar) |\n\n### Важно:\nВ турецком **нет грамматического рода** — O = он, она, оно."},
                    {"type": "flashcards", "cards": [{"front": "Ben", "back": "Я"}, {"front": "Sen", "back": "Ты"}, {"front": "O", "back": "Он / Она / Оно"}, {"front": "Biz", "back": "Мы"}, {"front": "Siz", "back": "Вы"}, {"front": "Onlar", "back": "Они"}]},
                    {"type": "matching", "pairs": [{"left": "Ben", "right": "Я"}, {"left": "Sen", "right": "Ты"}, {"left": "O", "right": "Он/Она"}, {"left": "Biz", "right": "Мы"}, {"left": "Siz", "right": "Вы"}, {"left": "Onlar", "right": "Они"}]},
                    {"type": "quiz", "question": "Что означает местоимение «O» в турецком?", "options": [{"id": "a", "text": "Только «он»", "correct": False}, {"id": "b", "text": "Он, она и оно", "correct": True}, {"id": "c", "text": "Только «она»", "correct": False}, {"id": "d", "text": "Мы", "correct": False}]},
                    {"type": "fill-blank", "text": "___ öğretmenim. (Я учитель)", "answers": ["Ben"]},
                    {"type": "fill-blank", "text": "Sen doktor___. (Ты врач)", "answers": ["sun"]},
                    {"type": "type-answer", "question": "Как будет «мы» по-турецки?", "acceptedAnswers": ["Biz", "biz"]},
                    {"type": "true-false", "statement": "В турецком языке есть грамматический род (мужской/женский).", "correct": False},
                    {"type": "quiz", "question": "Какой суффикс «быть» для Ben?", "options": [{"id": "a", "text": "-sın", "correct": False}, {"id": "b", "text": "-(y)ım/-(y)im", "correct": True}, {"id": "c", "text": "-sınız", "correct": False}, {"id": "d", "text": "нулевой", "correct": False}]},
                    {"type": "drag-order", "items": ["Ben — Я", "Sen — Ты", "O — Он/Она", "Biz — Мы", "Siz — Вы", "Onlar — Они"]},
                    {"type": "multi-select", "question": "Какие утверждения верны?", "options": [{"id": "a", "text": "O означает он, она и оно", "correct": True}, {"id": "b", "text": "Siz — только множественное число", "correct": False}, {"id": "c", "text": "В турецком нет грамматического рода", "correct": True}, {"id": "d", "text": "Суффикс для O — нулевой", "correct": True}]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 3: Гармония гласных
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Гармония гласных",
        "pos": 2,
        "lessons": [
            {
                "t": "Большая гармония гласных (büyük ünlü uyumu)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Большая гармония гласных", "markdown": "## Büyük Ünlü Uyumu — Большая гармония гласных\n\nОсновное правило турецкой фонетики: **все гласные в слове должны быть одного ряда** — либо передние, либо задние.\n\n### Правило:\n| Последняя гласная корня | Суффикс содержит |\n|------------------------|------------------|\n| **a, ı** (задние, неогубл.) | **a** или **ı** |\n| **o, u** (задние, огубл.) | **a** или **u** |\n| **e, i** (передние, неогубл.) | **e** или **i** |\n| **ö, ü** (передние, огубл.) | **e** или **ü** |\n\n### Примеры с суффиксом множественного числа -lar/-ler:\n- araba → araba**lar** (машины) — задний ряд → -lar\n- ev → ev**ler** (дома) — передний ряд → -ler\n- göz → göz**ler** (глаза) — передний ряд → -ler\n- okul → okul**lar** (школы) — задний ряд → -lar\n\n### Исключения:\nНекоторые заимствования нарушают гармонию: saat (часы), televizyon."},
                    {"type": "quiz", "question": "Что определяет большая гармония гласных?", "options": [{"id": "a", "text": "Ряд гласных в суффиксе зависит от последней гласной корня", "correct": True}, {"id": "b", "text": "Ударение в слове", "correct": False}, {"id": "c", "text": "Порядок согласных", "correct": False}, {"id": "d", "text": "Длину слова", "correct": False}]},
                    {"type": "category-sort", "categories": ["Суффикс -lar (задний ряд)", "Суффикс -ler (передний ряд)"], "items": [{"text": "araba (машина)", "category": "Суффикс -lar (задний ряд)"}, {"text": "ev (дом)", "category": "Суффикс -ler (передний ряд)"}, {"text": "göz (глаз)", "category": "Суффикс -ler (передний ряд)"}, {"text": "okul (школа)", "category": "Суффикс -lar (задний ряд)"}, {"text": "kitap (книга)", "category": "Суффикс -lar (задний ряд)"}, {"text": "deniz (море)", "category": "Суффикс -ler (передний ряд)"}]},
                    {"type": "fill-blank", "text": "araba + мн. число = araba___ (машины)", "answers": ["lar"]},
                    {"type": "fill-blank", "text": "ev + мн. число = ev___ (дома)", "answers": ["ler"]},
                    {"type": "matching", "pairs": [{"left": "araba + мн.ч.", "right": "arabalar"}, {"left": "ev + мн.ч.", "right": "evler"}, {"left": "göz + мн.ч.", "right": "gözler"}, {"left": "okul + мн.ч.", "right": "okullar"}]},
                    {"type": "type-answer", "question": "Образуйте мн. число от «kitap» (книга)", "acceptedAnswers": ["kitaplar", "Kitaplar"]},
                    {"type": "true-false", "statement": "Слово «televizyon» подчиняется большой гармонии гласных.", "correct": False},
                    {"type": "quiz", "question": "Какой суффикс мн. числа у слова «deniz» (море)?", "options": [{"id": "a", "text": "-lar", "correct": False}, {"id": "b", "text": "-ler", "correct": True}, {"id": "c", "text": "-lar и -ler оба верны", "correct": False}, {"id": "d", "text": "без суффикса", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова получают суффикс -ler?", "options": [{"id": "a", "text": "ev (дом)", "correct": True}, {"id": "b", "text": "göz (глаз)", "correct": True}, {"id": "c", "text": "araba (машина)", "correct": False}, {"id": "d", "text": "deniz (море)", "correct": True}, {"id": "e", "text": "okul (школа)", "correct": False}]},
                ],
            },
            {
                "t": "Малая гармония гласных (küçük ünlü uyumu)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Малая гармония гласных", "markdown": "## Küçük Ünlü Uyumu — Малая гармония гласных\n\nМалая гармония определяет выбор между **4 вариантами** суффикса.\n\n### Правило (4-вариантная гармония):\n| Последняя гласная | Суффикс |\n|-------------------|--------|\n| **a, ı** | **ı** |\n| **e, i** | **i** |\n| **o, u** | **u** |\n| **ö, ü** | **ü** |\n\n### Примеры с суффиксом винительного падежа -ı/-i/-u/-ü:\n- araba → araba**yı** (машину)\n- ev → ev**i** (дом — вин. п.)\n- okul → okul**u** (школу)\n- göz → göz**ü** (глаз — вин. п.)\n\n### Примеры с суффиксом принадлежности -ım/-im/-um/-üm:\n- kalem**im** — мой карандаш\n- araba**m** → arabam (моя машина)\n- okul**um** — моя школа\n- göz**üm** — мой глаз\n\n### Важно:\nМалая гармония учитывает **и ряд, и огубленность** последней гласной."},
                    {"type": "quiz", "question": "Сколько вариантов суффикса даёт малая гармония?", "options": [{"id": "a", "text": "2 варианта", "correct": False}, {"id": "b", "text": "4 варианта", "correct": True}, {"id": "c", "text": "8 вариантов", "correct": False}, {"id": "d", "text": "1 вариант", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "araba + вин. п.", "right": "arabayı"}, {"left": "ev + вин. п.", "right": "evi"}, {"left": "okul + вин. п.", "right": "okulu"}, {"left": "göz + вин. п.", "right": "gözü"}]},
                    {"type": "fill-blank", "text": "okul + принадлежность (мой) = okul___", "answers": ["um"]},
                    {"type": "fill-blank", "text": "göz + принадлежность (мой) = göz___", "answers": ["üm"]},
                    {"type": "category-sort", "categories": ["Суффикс -ı", "Суффикс -i", "Суффикс -u", "Суффикс -ü"], "items": [{"text": "araba (последняя a)", "category": "Суффикс -ı"}, {"text": "ev (последняя e)", "category": "Суффикс -i"}, {"text": "okul (последняя u)", "category": "Суффикс -u"}, {"text": "göz (последняя ö)", "category": "Суффикс -ü"}]},
                    {"type": "type-answer", "question": "Добавьте суффикс вин. падежа к слову «ev»", "acceptedAnswers": ["evi", "Evi"]},
                    {"type": "true-false", "statement": "Малая гармония учитывает только ряд гласной (передний/задний).", "correct": False},
                    {"type": "quiz", "question": "Какой суффикс принадлежности (мой) у слова «kalem» (карандаш)?", "options": [{"id": "a", "text": "-ım", "correct": False}, {"id": "b", "text": "-im", "correct": True}, {"id": "c", "text": "-um", "correct": False}, {"id": "d", "text": "-üm", "correct": False}]},
                    {"type": "multi-select", "question": "Какие пары «слово → суффикс» верны?", "options": [{"id": "a", "text": "araba → -ı", "correct": True}, {"id": "b", "text": "göz → -ü", "correct": True}, {"id": "c", "text": "okul → -i", "correct": False}, {"id": "d", "text": "ev → -i", "correct": True}]},
                ],
            },
            {
                "t": "Аффиксы и суффиксы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Система аффиксов", "markdown": "## Аффиксы турецкого языка\n\nТурецкий — **агглютинативный** язык: слова строятся путём добавления суффиксов к корню.\n\n### Основные суффиксы:\n| Суффикс | Значение | Пример |\n|---------|----------|--------|\n| **-lar/-ler** | множ. число | ev → ev**ler** (дома) |\n| **-lı/-li/-lu/-lü** | имеющий | süt**lü** (с молоком) |\n| **-sız/-siz/-suz/-süz** | без | süt**süz** (без молока) |\n| **-cı/-ci/-cu/-cü** | деятель | balık**çı** (рыбак) |\n| **-lık/-lik/-luk/-lük** | абстр. сущ. | güzel**lik** (красота) |\n\n### Порядок суффиксов:\nКорень + мн. число + падеж + принадлежность\n\n### Пример цепочки:\n**ev** (дом) → ev**ler** (дома) → evler**imiz** (наши дома) → evlerimiz**de** (в наших домах)\n\n### Важно:\nКаждый суффикс подчиняется правилам гармонии гласных!"},
                    {"type": "flashcards", "cards": [{"front": "-lar/-ler", "back": "Множественное число: ev → evler"}, {"front": "-lı/-li/-lu/-lü", "back": "Имеющий что-то: sütlü (с молоком)"}, {"front": "-sız/-siz/-suz/-süz", "back": "Без чего-то: sütsüz (без молока)"}, {"front": "-cı/-ci/-cu/-cü", "back": "Деятель: balıkçı (рыбак)"}, {"front": "-lık/-lik/-luk/-lük", "back": "Абстрактное существительное: güzellik (красота)"}]},
                    {"type": "matching", "pairs": [{"left": "-lar/-ler", "right": "множественное число"}, {"left": "-lı/-li", "right": "имеющий что-то"}, {"left": "-sız/-siz", "right": "без чего-то"}, {"left": "-cı/-ci", "right": "деятель"}, {"left": "-lık/-lik", "right": "абстрактное существительное"}]},
                    {"type": "quiz", "question": "Что означает суффикс -sız/-siz/-suz/-süz?", "options": [{"id": "a", "text": "Имеющий что-то", "correct": False}, {"id": "b", "text": "Без чего-то", "correct": True}, {"id": "c", "text": "Множественное число", "correct": False}, {"id": "d", "text": "Деятель", "correct": False}]},
                    {"type": "fill-blank", "text": "balık (рыба) + деятель = balık___ (рыбак)", "answers": ["çı"]},
                    {"type": "fill-blank", "text": "güzel (красивый) + абстр. = güzel___ (красота)", "answers": ["lik"]},
                    {"type": "type-answer", "question": "Как будет «без молока» (süt = молоко)?", "acceptedAnswers": ["sütsüz", "Sütsüz"]},
                    {"type": "true-false", "statement": "Турецкий язык — агглютинативный (слова строятся добавлением суффиксов).", "correct": True},
                    {"type": "quiz", "question": "Что означает слово «evlerimizde»?", "options": [{"id": "a", "text": "Мой дом", "correct": False}, {"id": "b", "text": "В наших домах", "correct": True}, {"id": "c", "text": "Наш дом", "correct": False}, {"id": "d", "text": "Дома (множ. ч.)", "correct": False}]},
                    {"type": "drag-order", "items": ["ev (корень: дом)", "evler (мн. число: дома)", "evlerimiz (наши дома)", "evlerimizde (в наших домах)"]},
                    {"type": "multi-select", "question": "Какие суффиксы имеют 4 варианта гармонии?", "options": [{"id": "a", "text": "-lı/-li/-lu/-lü", "correct": True}, {"id": "b", "text": "-lar/-ler", "correct": False}, {"id": "c", "text": "-sız/-siz/-suz/-süz", "correct": True}, {"id": "d", "text": "-cı/-ci/-cu/-cü", "correct": True}]},
                ],
            },
            {
                "t": "Буферные буквы (kaynaştırma ünsüzleri)",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Буферные согласные", "markdown": "## Kaynaştırma Ünsüzleri — Буферные согласные\n\nКогда к слову на гласную добавляется суффикс на гласную, вставляется **буферная согласная** для благозвучия.\n\n### Буферные буквы:\n| Буква | Когда | Пример |\n|-------|-------|--------|\n| **y** | между гласными (самая частая) | araba**y**ı (машину) |\n| **n** | после притяж. суффикса 3 лица | araba**s**ı**n**ın (его машины) |\n| **s** | притяж. 3 лица после гласной | araba**s**ı (его машина) |\n| **ş** | в числительных | altı**ş**ar (по шесть) |\n\n### Примеры с буфером -y-:\n- araba + вин. п. (-ı) → araba**y**ı\n- oda + вин. п. (-ı) → oda**y**ı (комнату)\n- kapı + вин. п. (-ı) → kapı**y**ı (дверь — вин. п.)\n\n### Примеры с буфером -s-:\n- araba + его/её (-ı) → araba**s**ı (его машина)\n- oda + его/её (-ı) → oda**s**ı (его комната)\n\n### Чередование согласных (ünsüz yumuşaması):\np → b, ç → c, t → d, k → ğ перед гласным суффиксом:\n- kitap → kitab**ı** (книгу)\n- ağaç → ağac**ı** (дерево — вин. п.)"},
                    {"type": "quiz", "question": "Какая буферная буква самая частая в турецком?", "options": [{"id": "a", "text": "n", "correct": False}, {"id": "b", "text": "y", "correct": True}, {"id": "c", "text": "s", "correct": False}, {"id": "d", "text": "ş", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "araba + вин.п.", "right": "arabayı"}, {"left": "araba + его/её", "right": "arabası"}, {"left": "kitap + вин.п.", "right": "kitabı"}, {"left": "ağaç + вин.п.", "right": "ağacı"}]},
                    {"type": "fill-blank", "text": "araba + вин. падеж = araba___ı", "answers": ["y"]},
                    {"type": "fill-blank", "text": "araba + его/её = araba___ı", "answers": ["s"]},
                    {"type": "true-false", "statement": "Чередование p → b происходит перед гласным суффиксом: kitap → kitabı.", "correct": True},
                    {"type": "type-answer", "question": "Как будет «его комната» (oda = комната)?", "acceptedAnswers": ["odası", "Odası"]},
                    {"type": "category-sort", "categories": ["Буфер -y-", "Буфер -s-"], "items": [{"text": "araba + вин. п. → arabayı", "category": "Буфер -y-"}, {"text": "oda + вин. п. → odayı", "category": "Буфер -y-"}, {"text": "araba + его → arabası", "category": "Буфер -s-"}, {"text": "oda + его → odası", "category": "Буфер -s-"}]},
                    {"type": "quiz", "question": "Какое чередование происходит в слове «kitap» перед гласным суффиксом?", "options": [{"id": "a", "text": "p → b", "correct": True}, {"id": "b", "text": "p → v", "correct": False}, {"id": "c", "text": "p не меняется", "correct": False}, {"id": "d", "text": "p → f", "correct": False}]},
                    {"type": "multi-select", "question": "Какие чередования согласных есть в турецком?", "options": [{"id": "a", "text": "p → b", "correct": True}, {"id": "b", "text": "ç → c", "correct": True}, {"id": "c", "text": "t → d", "correct": True}, {"id": "d", "text": "k → ğ", "correct": True}, {"id": "e", "text": "m → n", "correct": False}]},
                ],
            },
            {
                "t": "Практика гармонии гласных",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Обобщение: гармония гласных", "markdown": "## Практика гармонии гласных\n\n### Алгоритм выбора суффикса:\n1. Определите **последнюю гласную** корня\n2. Определите **тип суффикса**: 2-вариантный или 4-вариантный\n3. Примените правило гармонии\n\n### 2-вариантные суффиксы (a/e):\n- -lar/**ler**, -da/**de**, -dan/**den**\n- Задние (a,ı,o,u) → **a**\n- Передние (e,i,ö,ü) → **e**\n\n### 4-вариантные суффиксы (ı/i/u/ü):\n- -lı/li/lu/lü, -mış/miş/muş/müş\n- a,ı → **ı** | e,i → **i** | o,u → **u** | ö,ü → **ü**\n\n### Тест:\n- çiçek (цветок) + мн.ч. → çiçek**ler** (передний, 2-вар.)\n- çiçek + -li → çiçek**li** (с цветами, 4-вар.)\n- balık (рыба) + мн.ч. → balık**lar** (задний, 2-вар.)\n- balık + -cı → balık**çı** (рыбак, 4-вар.)"},
                    {"type": "fill-blank", "text": "çiçek (цветок) + мн. число = çiçek___", "answers": ["ler"]},
                    {"type": "fill-blank", "text": "balık (рыба) + деятель = balık___", "answers": ["çı"]},
                    {"type": "fill-blank", "text": "okul (школа) + мн. число = okul___", "answers": ["lar"]},
                    {"type": "fill-blank", "text": "göz (глаз) + мой = göz___", "answers": ["üm"]},
                    {"type": "type-answer", "question": "Множественное число от «şehir» (город)?", "acceptedAnswers": ["şehirler", "Şehirler"]},
                    {"type": "type-answer", "question": "Множественное число от «yol» (дорога)?", "acceptedAnswers": ["yollar", "Yollar"]},
                    {"type": "matching", "pairs": [{"left": "çiçek + -ler", "right": "цветы"}, {"left": "balık + -çı", "right": "рыбак"}, {"left": "süt + -lü", "right": "с молоком"}, {"left": "süt + -süz", "right": "без молока"}, {"left": "güzel + -lik", "right": "красота"}]},
                    {"type": "quiz", "question": "Какой суффикс получит «kuş» (птица) + множ.ч.?", "options": [{"id": "a", "text": "-lar", "correct": True}, {"id": "b", "text": "-ler", "correct": False}]},
                    {"type": "true-false", "statement": "Суффикс -da/-de — это 2-вариантный суффикс.", "correct": True},
                    {"type": "multi-select", "question": "Какие формы правильны?", "options": [{"id": "a", "text": "evler (дома)", "correct": True}, {"id": "b", "text": "evlar", "correct": False}, {"id": "c", "text": "arabalar (машины)", "correct": True}, {"id": "d", "text": "arabaler", "correct": False}, {"id": "e", "text": "gözler (глаза)", "correct": True}]},
                    {"type": "drag-order", "items": ["Определить последнюю гласную корня", "Определить тип суффикса (2 или 4 варианта)", "Определить ряд гласной (передний/задний)", "Выбрать нужный вариант суффикса", "Проверить буферные буквы"]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 4: Повседневная жизнь
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Повседневная жизнь",
        "pos": 3,
        "lessons": [
            {
                "t": "Günler — Дни недели",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Дни недели", "markdown": "## Haftanın Günleri — Дни недели\n\n| Турецкий | Русский |\n|----------|--------|\n| **Pazartesi** | Понедельник |\n| **Salı** | Вторник |\n| **Çarşamba** | Среда |\n| **Perşembe** | Четверг |\n| **Cuma** | Пятница |\n| **Cumartesi** | Суббота |\n| **Pazar** | Воскресенье |\n\n### Полезные фразы:\n- **Bugün ne günü?** — Какой сегодня день?\n- **Bugün Pazartesi.** — Сегодня понедельник.\n- **Hafta sonu** — выходные (суббота+воскресенье)\n- **Hafta içi** — будни"},
                    {"type": "flashcards", "cards": [{"front": "Pazartesi", "back": "Понедельник"}, {"front": "Salı", "back": "Вторник"}, {"front": "Çarşamba", "back": "Среда"}, {"front": "Perşembe", "back": "Четверг"}, {"front": "Cuma", "back": "Пятница"}, {"front": "Cumartesi", "back": "Суббота"}, {"front": "Pazar", "back": "Воскресенье"}]},
                    {"type": "matching", "pairs": [{"left": "Pazartesi", "right": "Понедельник"}, {"left": "Salı", "right": "Вторник"}, {"left": "Çarşamba", "right": "Среда"}, {"left": "Cuma", "right": "Пятница"}, {"left": "Pazar", "right": "Воскресенье"}]},
                    {"type": "quiz", "question": "Какой день — Çarşamba?", "options": [{"id": "a", "text": "Понедельник", "correct": False}, {"id": "b", "text": "Среда", "correct": True}, {"id": "c", "text": "Пятница", "correct": False}, {"id": "d", "text": "Воскресенье", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «пятница»?", "acceptedAnswers": ["Cuma", "cuma"]},
                    {"type": "fill-blank", "text": "Hafta ___ = выходные (суббота и воскресенье)", "answers": ["sonu"]},
                    {"type": "true-false", "statement": "Pazar — это суббота по-турецки.", "correct": False},
                    {"type": "drag-order", "items": ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]},
                    {"type": "quiz", "question": "Что означает «hafta içi»?", "options": [{"id": "a", "text": "Выходные", "correct": False}, {"id": "b", "text": "Будни", "correct": True}, {"id": "c", "text": "Каникулы", "correct": False}, {"id": "d", "text": "Праздник", "correct": False}]},
                    {"type": "multi-select", "question": "Какие дни входят в «hafta sonu» (выходные)?", "options": [{"id": "a", "text": "Cumartesi", "correct": True}, {"id": "b", "text": "Pazar", "correct": True}, {"id": "c", "text": "Cuma", "correct": False}, {"id": "d", "text": "Pazartesi", "correct": False}]},
                ],
            },
            {
                "t": "Aylar — Месяцы",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Месяцы года", "markdown": "## Aylar — Месяцы\n\n| Турецкий | Русский |\n|----------|--------|\n| **Ocak** | Январь |\n| **Şubat** | Февраль |\n| **Mart** | Март |\n| **Nisan** | Апрель |\n| **Mayıs** | Май |\n| **Haziran** | Июнь |\n| **Temmuz** | Июль |\n| **Ağustos** | Август |\n| **Eylül** | Сентябрь |\n| **Ekim** | Октябрь |\n| **Kasım** | Ноябрь |\n| **Aralık** | Декабрь |\n\n### Полезные фразы:\n- **Bugün kaç?** — Какое сегодня число?\n- **Bugün 15 Nisan.** — Сегодня 15 апреля.\n- **Doğum günüm Mayıs'ta.** — Мой день рождения в мае."},
                    {"type": "flashcards", "cards": [{"front": "Ocak", "back": "Январь"}, {"front": "Şubat", "back": "Февраль"}, {"front": "Nisan", "back": "Апрель"}, {"front": "Haziran", "back": "Июнь"}, {"front": "Eylül", "back": "Сентябрь"}, {"front": "Aralık", "back": "Декабрь"}]},
                    {"type": "matching", "pairs": [{"left": "Ocak", "right": "Январь"}, {"left": "Mart", "right": "Март"}, {"left": "Mayıs", "right": "Май"}, {"left": "Temmuz", "right": "Июль"}, {"left": "Ekim", "right": "Октябрь"}, {"left": "Aralık", "right": "Декабрь"}]},
                    {"type": "quiz", "question": "Какой месяц — Haziran?", "options": [{"id": "a", "text": "Март", "correct": False}, {"id": "b", "text": "Июнь", "correct": True}, {"id": "c", "text": "Сентябрь", "correct": False}, {"id": "d", "text": "Ноябрь", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «апрель»?", "acceptedAnswers": ["Nisan", "nisan"]},
                    {"type": "fill-blank", "text": "Doğum günüm ___'ta. (Мой день рождения в мае)", "answers": ["Mayıs"]},
                    {"type": "true-false", "statement": "Kasım — это октябрь по-турецки.", "correct": False},
                    {"type": "drag-order", "items": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]},
                    {"type": "quiz", "question": "Какой месяц — Eylül?", "options": [{"id": "a", "text": "Июль", "correct": False}, {"id": "b", "text": "Август", "correct": False}, {"id": "c", "text": "Сентябрь", "correct": True}, {"id": "d", "text": "Октябрь", "correct": False}]},
                    {"type": "multi-select", "question": "Какие пары «месяц — перевод» верны?", "options": [{"id": "a", "text": "Ocak — Январь", "correct": True}, {"id": "b", "text": "Şubat — Март", "correct": False}, {"id": "c", "text": "Temmuz — Июль", "correct": True}, {"id": "d", "text": "Ağustos — Август", "correct": True}]},
                ],
            },
            {
                "t": "Saat kaç? — Который час?",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Время по-турецки", "markdown": "## Saat Kaç? — Который час?\n\n### Основные конструкции:\n| Турецкий | Русский |\n|----------|--------|\n| **Saat kaç?** | Который час? |\n| **Saat bir.** | Час (1:00). |\n| **Saat iki.** | Два часа (2:00). |\n| **Saat üç buçuk.** | Половина четвёртого (3:30). |\n| **Saat dörde çeyrek var.** | Без четверти четыре (3:45). |\n| **Saat dördü çeyrek geçiyor.** | Четверть пятого (4:15). |\n\n### Ключевые слова:\n- **buçuk** — половина\n- **çeyrek** — четверть\n- **var** — без (до часа)\n- **geçiyor** — после (прошло)\n\n### Примеры:\n- 5:00 → Saat beş\n- 5:30 → Saat beş buçuk\n- 5:15 → Saat beşi çeyrek geçiyor\n- 5:45 → Saat altıya çeyrek var"},
                    {"type": "flashcards", "cards": [{"front": "Saat kaç?", "back": "Который час?"}, {"front": "buçuk", "back": "половина"}, {"front": "çeyrek", "back": "четверть"}, {"front": "var", "back": "без (осталось до)"}, {"front": "geçiyor", "back": "после (прошло)"}]},
                    {"type": "matching", "pairs": [{"left": "Saat bir", "right": "1:00"}, {"left": "Saat iki buçuk", "right": "2:30"}, {"left": "Saat üçe çeyrek var", "right": "2:45"}, {"left": "Saat üçü çeyrek geçiyor", "right": "3:15"}]},
                    {"type": "quiz", "question": "Как сказать 5:30 по-турецки?", "options": [{"id": "a", "text": "Saat beş buçuk", "correct": True}, {"id": "b", "text": "Saat beş çeyrek", "correct": False}, {"id": "c", "text": "Saat altı buçuk", "correct": False}, {"id": "d", "text": "Saat beş var", "correct": False}]},
                    {"type": "fill-blank", "text": "3:30 = Saat üç ___", "answers": ["buçuk"]},
                    {"type": "type-answer", "question": "Как спросить «Который час?»?", "acceptedAnswers": ["Saat kaç?", "saat kaç?", "Saat kaç"]},
                    {"type": "true-false", "statement": "Buçuk означает «четверть» по-турецки.", "correct": False},
                    {"type": "quiz", "question": "Что означает «Saat altıya çeyrek var»?", "options": [{"id": "a", "text": "6:15", "correct": False}, {"id": "b", "text": "5:45", "correct": True}, {"id": "c", "text": "6:45", "correct": False}, {"id": "d", "text": "6:30", "correct": False}]},
                    {"type": "fill-blank", "text": "4:15 = Saat dördü çeyrek ___", "answers": ["geçiyor"]},
                    {"type": "multi-select", "question": "Какие слова связаны со временем?", "options": [{"id": "a", "text": "buçuk (половина)", "correct": True}, {"id": "b", "text": "çeyrek (четверть)", "correct": True}, {"id": "c", "text": "güzel (красивый)", "correct": False}, {"id": "d", "text": "var (без/осталось)", "correct": True}]},
                ],
            },
            {
                "t": "Aile — Семья",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Семья по-турецки", "markdown": "## Aile — Семья\n\n| Турецкий | Русский |\n|----------|--------|\n| **anne** | мама |\n| **baba** | папа |\n| **kardeş** | брат/сестра |\n| **ağabey (abi)** | старший брат |\n| **abla** | старшая сестра |\n| **dede** | дедушка |\n| **babaanne** | бабушка (по отцу) |\n| **anneanne** | бабушка (по маме) |\n| **amca** | дядя (по отцу) |\n| **teyze** | тётя (по маме) |\n| **eş** | супруг/супруга |\n| **çocuk** | ребёнок |\n| **oğul** | сын |\n| **kız** | дочь |\n\n### Интересно:\nВ турецком языке есть разные слова для родственников по отцу и по маме:\n- **amca** — дядя по отцу, **dayı** — дядя по маме\n- **hala** — тётя по отцу, **teyze** — тётя по маме"},
                    {"type": "flashcards", "cards": [{"front": "anne", "back": "мама"}, {"front": "baba", "back": "папа"}, {"front": "ağabey", "back": "старший брат"}, {"front": "abla", "back": "старшая сестра"}, {"front": "dede", "back": "дедушка"}, {"front": "çocuk", "back": "ребёнок"}, {"front": "oğul", "back": "сын"}, {"front": "kız", "back": "дочь"}]},
                    {"type": "matching", "pairs": [{"left": "anne", "right": "мама"}, {"left": "baba", "right": "папа"}, {"left": "dede", "right": "дедушка"}, {"left": "abla", "right": "старшая сестра"}, {"left": "çocuk", "right": "ребёнок"}, {"left": "oğul", "right": "сын"}]},
                    {"type": "quiz", "question": "Как по-турецки «старший брат»?", "options": [{"id": "a", "text": "kardeş", "correct": False}, {"id": "b", "text": "ağabey", "correct": True}, {"id": "c", "text": "amca", "correct": False}, {"id": "d", "text": "oğul", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: мама", "acceptedAnswers": ["anne", "Anne"]},
                    {"type": "type-answer", "question": "Переведите: ребёнок", "acceptedAnswers": ["çocuk", "Çocuk"]},
                    {"type": "fill-blank", "text": "___ — дядя по отцу, dayı — дядя по маме.", "answers": ["amca", "Amca"]},
                    {"type": "true-false", "statement": "В турецком одно слово для «бабушка» — как и в русском.", "correct": False},
                    {"type": "category-sort", "categories": ["По отцу", "По маме"], "items": [{"text": "amca (дядя)", "category": "По отцу"}, {"text": "dayı (дядя)", "category": "По маме"}, {"text": "hala (тётя)", "category": "По отцу"}, {"text": "teyze (тётя)", "category": "По маме"}, {"text": "babaanne (бабушка)", "category": "По отцу"}, {"text": "anneanne (бабушка)", "category": "По маме"}]},
                    {"type": "multi-select", "question": "Какие слова означают женщин-родственниц?", "options": [{"id": "a", "text": "anne", "correct": True}, {"id": "b", "text": "abla", "correct": True}, {"id": "c", "text": "ağabey", "correct": False}, {"id": "d", "text": "teyze", "correct": True}, {"id": "e", "text": "baba", "correct": False}]},
                ],
            },
            {
                "t": "Ev — Дом и комнаты",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Дом и комнаты", "markdown": "## Ev — Дом\n\n| Турецкий | Русский |\n|----------|--------|\n| **ev** | дом |\n| **oda** | комната |\n| **salon** | гостиная |\n| **yatak odası** | спальня |\n| **mutfak** | кухня |\n| **banyo** | ванная |\n| **tuvalet** | туалет |\n| **balkon** | балкон |\n| **bahçe** | сад |\n| **kapı** | дверь |\n| **pencere** | окно |\n| **merdiven** | лестница |\n\n### Предметы в доме:\n| Турецкий | Русский |\n|----------|--------|\n| **masa** | стол |\n| **sandalye** | стул |\n| **yatak** | кровать |\n| **dolap** | шкаф |\n| **koltuk** | кресло |\n\n### Фразы:\n- **Evim büyük.** — Мой дом большой.\n- **Mutfakta yemek yapıyorum.** — Я готовлю на кухне."},
                    {"type": "flashcards", "cards": [{"front": "ev", "back": "дом"}, {"front": "mutfak", "back": "кухня"}, {"front": "yatak odası", "back": "спальня"}, {"front": "banyo", "back": "ванная"}, {"front": "bahçe", "back": "сад"}, {"front": "pencere", "back": "окно"}, {"front": "masa", "back": "стол"}, {"front": "yatak", "back": "кровать"}]},
                    {"type": "matching", "pairs": [{"left": "ev", "right": "дом"}, {"left": "mutfak", "right": "кухня"}, {"left": "banyo", "right": "ванная"}, {"left": "bahçe", "right": "сад"}, {"left": "pencere", "right": "окно"}, {"left": "masa", "right": "стол"}]},
                    {"type": "quiz", "question": "Как по-турецки «кухня»?", "options": [{"id": "a", "text": "salon", "correct": False}, {"id": "b", "text": "mutfak", "correct": True}, {"id": "c", "text": "banyo", "correct": False}, {"id": "d", "text": "oda", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: окно", "acceptedAnswers": ["pencere", "Pencere"]},
                    {"type": "type-answer", "question": "Переведите: сад", "acceptedAnswers": ["bahçe", "Bahçe"]},
                    {"type": "fill-blank", "text": "Yatak ___ = спальня (комната для сна)", "answers": ["odası"]},
                    {"type": "true-false", "statement": "Salon — это кухня по-турецки.", "correct": False},
                    {"type": "category-sort", "categories": ["Комнаты", "Мебель"], "items": [{"text": "mutfak", "category": "Комнаты"}, {"text": "banyo", "category": "Комнаты"}, {"text": "salon", "category": "Комнаты"}, {"text": "masa", "category": "Мебель"}, {"text": "sandalye", "category": "Мебель"}, {"text": "koltuk", "category": "Мебель"}]},
                    {"type": "multi-select", "question": "Какие слова обозначают мебель?", "options": [{"id": "a", "text": "masa (стол)", "correct": True}, {"id": "b", "text": "yatak (кровать)", "correct": True}, {"id": "c", "text": "bahçe (сад)", "correct": False}, {"id": "d", "text": "dolap (шкаф)", "correct": True}]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 5: Глаголы
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Глаголы",
        "pos": 4,
        "lessons": [
            {
                "t": "Настоящее время (-yor)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Настоящее продолженное время", "markdown": "## Şimdiki Zaman — Настоящее продолженное время (-yor)\n\n### Образование:\nОснова глагола + **-yor** + личное окончание\n\n### Спряжение (gelmek — приходить):\n| Лицо | Форма | Перевод |\n|------|-------|--------|\n| Ben | gel**iyorum** | я прихожу |\n| Sen | gel**iyorsun** | ты приходишь |\n| O | gel**iyor** | он приходит |\n| Biz | gel**iyoruz** | мы приходим |\n| Siz | gel**iyorsunuz** | вы приходите |\n| Onlar | gel**iyorlar** | они приходят |\n\n### Правило:\nЕсли основа оканчивается на гласную — гласная заменяется:\n- **beklemek** (ждать) → bekl**iyor** (НЕ bekle-iyor)\n- **okumak** (читать) → ok**uyor**\n\n### Важные глаголы:\n- **yapmak** — делать → yapıyor\n- **gitmek** — идти → gidiyor\n- **yemek** — есть → yiyor\n- **içmek** — пить → içiyor\n- **çalışmak** — работать → çalışıyor"},
                    {"type": "flashcards", "cards": [{"front": "gelmek", "back": "приходить — geliyorum"}, {"front": "yapmak", "back": "делать — yapıyorum"}, {"front": "gitmek", "back": "идти — gidiyorum"}, {"front": "yemek", "back": "есть — yiyorum"}, {"front": "içmek", "back": "пить — içiyorum"}, {"front": "çalışmak", "back": "работать — çalışıyorum"}]},
                    {"type": "matching", "pairs": [{"left": "geliyorum", "right": "я прихожу"}, {"left": "yapıyorsun", "right": "ты делаешь"}, {"left": "gidiyor", "right": "он идёт"}, {"left": "çalışıyoruz", "right": "мы работаем"}, {"left": "içiyorsunuz", "right": "вы пьёте"}]},
                    {"type": "quiz", "question": "Какой суффикс образует настоящее время в турецком?", "options": [{"id": "a", "text": "-mış", "correct": False}, {"id": "b", "text": "-yor", "correct": True}, {"id": "c", "text": "-acak", "correct": False}, {"id": "d", "text": "-di", "correct": False}]},
                    {"type": "fill-blank", "text": "Ben gel___ (я прихожу)", "answers": ["iyorum"]},
                    {"type": "fill-blank", "text": "O çalış___ (он работает)", "answers": ["ıyor"]},
                    {"type": "type-answer", "question": "Проспрягайте «gitmek» для Ben в настоящем времени", "acceptedAnswers": ["gidiyorum", "Gidiyorum"]},
                    {"type": "true-false", "statement": "Суффикс -yor не подчиняется гармонии гласных.", "correct": True},
                    {"type": "quiz", "question": "Как будет «мы работаем»?", "options": [{"id": "a", "text": "çalışıyoruz", "correct": True}, {"id": "b", "text": "çalışıyorum", "correct": False}, {"id": "c", "text": "çalışıyorsunuz", "correct": False}, {"id": "d", "text": "çalışıyorlar", "correct": False}]},
                    {"type": "multi-select", "question": "Какие формы настоящего времени правильны?", "options": [{"id": "a", "text": "geliyorum (я прихожу)", "correct": True}, {"id": "b", "text": "yapıyorsun (ты делаешь)", "correct": True}, {"id": "c", "text": "gidiyorlar (они идут)", "correct": True}, {"id": "d", "text": "içiyormek", "correct": False}]},
                ],
            },
            {
                "t": "Прошедшее время (-di)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Прошедшее определённое время", "markdown": "## Geçmiş Zaman — Прошедшее время (-di)\n\n### Образование:\nОснова + **-dı/-di/-du/-dü** (или -tı/-ti/-tu/-tü) + личное окончание\n\n### Спряжение (gelmek — приходить):\n| Лицо | Форма | Перевод |\n|------|-------|--------|\n| Ben | gel**dim** | я пришёл |\n| Sen | gel**din** | ты пришёл |\n| O | gel**di** | он пришёл |\n| Biz | gel**dik** | мы пришли |\n| Siz | gel**diniz** | вы пришли |\n| Onlar | gel**diler** | они пришли |\n\n### Выбор -dı или -tı:\n- После звонких согласных и гласных → **-dı/-di/-du/-dü**\n- После глухих (p, ç, t, k, f, h, s, ş) → **-tı/-ti/-tu/-tü**\n\n### Примеры:\n- **gitmek** → git**tim** (я пошёл) — после t → -ti\n- **yapmak** → yap**tım** (я сделал) — после p → -tı\n- **okumak** → oku**dum** (я прочитал) — после гласной → -du"},
                    {"type": "flashcards", "cards": [{"front": "geldim", "back": "я пришёл"}, {"front": "gittim", "back": "я пошёл"}, {"front": "yaptım", "back": "я сделал"}, {"front": "okudum", "back": "я прочитал"}, {"front": "içtim", "back": "я выпил"}, {"front": "çalıştım", "back": "я работал"}]},
                    {"type": "matching", "pairs": [{"left": "geldim", "right": "я пришёл"}, {"left": "gittim", "right": "я пошёл"}, {"left": "yaptım", "right": "я сделал"}, {"left": "okudum", "right": "я прочитал"}, {"left": "içtim", "right": "я выпил"}]},
                    {"type": "quiz", "question": "Какой суффикс образует прошедшее время?", "options": [{"id": "a", "text": "-yor", "correct": False}, {"id": "b", "text": "-di/-tı (и варианты)", "correct": True}, {"id": "c", "text": "-acak", "correct": False}, {"id": "d", "text": "-miş", "correct": False}]},
                    {"type": "fill-blank", "text": "Ben gel___ (я пришёл)", "answers": ["dim"]},
                    {"type": "fill-blank", "text": "Ben git___ (я пошёл)", "answers": ["tim"]},
                    {"type": "type-answer", "question": "Как будет «я сделал» (yapmak)?", "acceptedAnswers": ["yaptım", "Yaptım"]},
                    {"type": "true-false", "statement": "После глухих согласных используется -tı/-ti/-tu/-tü.", "correct": True},
                    {"type": "quiz", "question": "Как будет «мы прочитали» (okumak)?", "options": [{"id": "a", "text": "okuduk", "correct": True}, {"id": "b", "text": "okutuk", "correct": False}, {"id": "c", "text": "okudum", "correct": False}, {"id": "d", "text": "okudunuz", "correct": False}]},
                    {"type": "multi-select", "question": "После каких согласных используется -tı (глухой вариант)?", "options": [{"id": "a", "text": "p", "correct": True}, {"id": "b", "text": "ç", "correct": True}, {"id": "c", "text": "l", "correct": False}, {"id": "d", "text": "k", "correct": True}, {"id": "e", "text": "n", "correct": False}]},
                ],
            },
            {
                "t": "Будущее время (-acak/-ecek)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Будущее время", "markdown": "## Gelecek Zaman — Будущее время (-acak/-ecek)\n\n### Образование:\nОснова + **-acak/-ecek** + личное окончание\n\n### Спряжение (gelmek — приходить):\n| Лицо | Форма | Перевод |\n|------|-------|--------|\n| Ben | gel**eceğim** | я приду |\n| Sen | gel**eceksin** | ты придёшь |\n| O | gel**ecek** | он придёт |\n| Biz | gel**eceğiz** | мы придём |\n| Siz | gel**eceksiniz** | вы придёте |\n| Onlar | gel**ecekler** | они придут |\n\n### Гармония:\n- Задние гласные → **-acak**: yapmak → yap**acağım**\n- Передние гласные → **-ecek**: gelmek → gel**eceğim**\n\n### Чередование k → ğ:\nПеред гласным суффиксом: gelece**k** → geleceğ**im** (k → ğ)\n\n### Примеры:\n- **gitmek** → gid**eceğim** (я пойду)\n- **yapmak** → yap**acağım** (я сделаю)\n- **okumak** → oku**yacağım** (я прочитаю)"},
                    {"type": "flashcards", "cards": [{"front": "geleceğim", "back": "я приду"}, {"front": "gideceğim", "back": "я пойду"}, {"front": "yapacağım", "back": "я сделаю"}, {"front": "okuyacağım", "back": "я прочитаю"}, {"front": "çalışacağım", "back": "я буду работать"}]},
                    {"type": "matching", "pairs": [{"left": "geleceğim", "right": "я приду"}, {"left": "yapacaksın", "right": "ты сделаешь"}, {"left": "gidecek", "right": "он пойдёт"}, {"left": "okuyacağız", "right": "мы прочитаем"}, {"left": "çalışacaklar", "right": "они будут работать"}]},
                    {"type": "quiz", "question": "Какой суффикс образует будущее время?", "options": [{"id": "a", "text": "-yor", "correct": False}, {"id": "b", "text": "-di", "correct": False}, {"id": "c", "text": "-acak/-ecek", "correct": True}, {"id": "d", "text": "-mış", "correct": False}]},
                    {"type": "fill-blank", "text": "Ben gel___ (я приду)", "answers": ["eceğim"]},
                    {"type": "fill-blank", "text": "O yap___ (он сделает)", "answers": ["acak"]},
                    {"type": "type-answer", "question": "Как будет «я пойду» (gitmek)?", "acceptedAnswers": ["gideceğim", "Gideceğim"]},
                    {"type": "true-false", "statement": "В будущем времени k перед гласным суффиксом переходит в ğ.", "correct": True},
                    {"type": "quiz", "question": "Как будет «мы сделаем» (yapmak)?", "options": [{"id": "a", "text": "yapacağız", "correct": True}, {"id": "b", "text": "yapacağım", "correct": False}, {"id": "c", "text": "yapacaklar", "correct": False}, {"id": "d", "text": "yapacaksınız", "correct": False}]},
                    {"type": "multi-select", "question": "Какие формы будущего времени правильны?", "options": [{"id": "a", "text": "geleceğim", "correct": True}, {"id": "b", "text": "gelecekım", "correct": False}, {"id": "c", "text": "yapacağız", "correct": True}, {"id": "d", "text": "gideceğiz", "correct": True}]},
                ],
            },
            {
                "t": "Отрицание глаголов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Отрицательные формы глаголов", "markdown": "## Olumsuz — Отрицание\n\n### Суффикс отрицания: -ma/-me\n\nВставляется между основой и временным суффиксом.\n\n### Настоящее время (-mıyor):\n- geliyorum → gel**m**iyorum (я не прихожу)\n- yapıyorum → yap**m**ıyorum (я не делаю)\n\n### Прошедшее время (-madı/-medi):\n- geldim → gel**me**dim (я не пришёл)\n- yaptım → yap**ma**dım (я не сделал)\n\n### Будущее время (-mayacak/-meyecek):\n- geleceğim → gel**me**yeceğim (я не приду)\n- yapacağım → yap**ma**yacağım (я не сделаю)\n\n### Примеры:\n| Утверждение | Отрицание |\n|-------------|----------|\n| Geliyorum (прихожу) | Gel**m**iyorum (не прихожу) |\n| Gittim (пошёл) | Git**me**dim (не пошёл) |\n| Yapacağım (сделаю) | Yap**ma**yacağım (не сделаю) |\n| Biliyorum (знаю) | Bil**m**iyorum (не знаю) |"},
                    {"type": "flashcards", "cards": [{"front": "gelmiyorum", "back": "я не прихожу"}, {"front": "gitmedim", "back": "я не пошёл"}, {"front": "yapmayacağım", "back": "я не сделаю"}, {"front": "bilmiyorum", "back": "я не знаю"}, {"front": "anlamıyorum", "back": "я не понимаю"}]},
                    {"type": "matching", "pairs": [{"left": "gelmiyorum", "right": "я не прихожу"}, {"left": "gitmedim", "right": "я не пошёл"}, {"left": "bilmiyorum", "right": "я не знаю"}, {"left": "yapmayacağım", "right": "я не сделаю"}, {"left": "anlamıyorum", "right": "я не понимаю"}]},
                    {"type": "quiz", "question": "Какой суффикс образует отрицание в турецком?", "options": [{"id": "a", "text": "-ma/-me", "correct": True}, {"id": "b", "text": "-değil", "correct": False}, {"id": "c", "text": "-yok", "correct": False}, {"id": "d", "text": "-sız/-siz", "correct": False}]},
                    {"type": "fill-blank", "text": "Я не знаю = Bil___iyorum", "answers": ["m"]},
                    {"type": "fill-blank", "text": "Я не пошёл = Git___dim", "answers": ["me"]},
                    {"type": "type-answer", "question": "Как сказать «я не понимаю» (anlamak)?", "acceptedAnswers": ["anlamıyorum", "Anlamıyorum"]},
                    {"type": "true-false", "statement": "Отрицательный суффикс -ma/-me ставится после временного суффикса.", "correct": False},
                    {"type": "quiz", "question": "Как будет «он не сделает» (yapmak)?", "options": [{"id": "a", "text": "yapmayacak", "correct": True}, {"id": "b", "text": "yapmıyacak", "correct": False}, {"id": "c", "text": "yapamayacak", "correct": False}, {"id": "d", "text": "yapmadı", "correct": False}]},
                    {"type": "multi-select", "question": "Какие отрицательные формы правильны?", "options": [{"id": "a", "text": "gelmiyorum", "correct": True}, {"id": "b", "text": "gelmiyor", "correct": True}, {"id": "c", "text": "gelmeiyorum", "correct": False}, {"id": "d", "text": "gitmedim", "correct": True}]},
                ],
            },
            {
                "t": "Вопросительные формы глаголов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Вопросы с глаголами", "markdown": "## Soru — Вопросительная форма\n\n### Вопросительная частица: mı/mi/mu/mü\n\nСтавится **после временного суффикса**, перед личным окончанием.\n\n### Настоящее время:\n- Geliyor **mu**sun? — Ты приходишь?\n- Geliyor **mu**sunuz? — Вы приходите?\n- Geliyor **mu**? — Он приходит?\n\n### Прошедшее время:\n- Geldin **mi**? — Ты пришёл?\n- Yaptınız **mı**? — Вы сделали?\n\n### Будущее время:\n- Gelecek **mi**sin? — Ты придёшь?\n- Yapacak **mı**sınız? — Вы сделаете?\n\n### Вопросительные слова:\n| Турецкий | Русский |\n|----------|--------|\n| **ne?** | что? |\n| **kim?** | кто? |\n| **nerede?** | где? |\n| **nereye?** | куда? |\n| **ne zaman?** | когда? |\n| **nasıl?** | как? |\n| **neden/niçin/niye?** | почему? |\n| **kaç?** | сколько? |"},
                    {"type": "flashcards", "cards": [{"front": "ne?", "back": "что?"}, {"front": "kim?", "back": "кто?"}, {"front": "nerede?", "back": "где?"}, {"front": "nereye?", "back": "куда?"}, {"front": "ne zaman?", "back": "когда?"}, {"front": "nasıl?", "back": "как?"}, {"front": "neden?", "back": "почему?"}, {"front": "kaç?", "back": "сколько?"}]},
                    {"type": "matching", "pairs": [{"left": "ne?", "right": "что?"}, {"left": "kim?", "right": "кто?"}, {"left": "nerede?", "right": "где?"}, {"left": "ne zaman?", "right": "когда?"}, {"left": "nasıl?", "right": "как?"}, {"left": "kaç?", "right": "сколько?"}]},
                    {"type": "quiz", "question": "Где ставится вопросительная частица mı/mi?", "options": [{"id": "a", "text": "В начале предложения", "correct": False}, {"id": "b", "text": "После временного суффикса, перед личным окончанием", "correct": True}, {"id": "c", "text": "В конце предложения", "correct": False}, {"id": "d", "text": "Перед глаголом", "correct": False}]},
                    {"type": "fill-blank", "text": "Geliyor ___sun? (Ты приходишь?)", "answers": ["mu"]},
                    {"type": "type-answer", "question": "Как спросить «где?» по-турецки?", "acceptedAnswers": ["nerede?", "nerede", "Nerede?", "Nerede"]},
                    {"type": "type-answer", "question": "Как спросить «когда?» по-турецки?", "acceptedAnswers": ["ne zaman?", "ne zaman", "Ne zaman?", "Ne zaman"]},
                    {"type": "true-false", "statement": "Частица mı/mi подчиняется гармонии гласных.", "correct": True},
                    {"type": "quiz", "question": "Как спросить «Ты пришёл?»?", "options": [{"id": "a", "text": "Geldin mi?", "correct": True}, {"id": "b", "text": "Geliyor musun?", "correct": False}, {"id": "c", "text": "Gelecek misin?", "correct": False}, {"id": "d", "text": "Gelir misin?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие вопросительные слова переведены верно?", "options": [{"id": "a", "text": "ne = что", "correct": True}, {"id": "b", "text": "kim = где", "correct": False}, {"id": "c", "text": "nasıl = как", "correct": True}, {"id": "d", "text": "kaç = сколько", "correct": True}]},
                    {"type": "drag-order", "items": ["ne? — что?", "kim? — кто?", "nerede? — где?", "ne zaman? — когда?", "nasıl? — как?", "kaç? — сколько?"]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 6: В городе
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "В городе",
        "pos": 5,
        "lessons": [
            {
                "t": "Ulaşım — Транспорт",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Транспорт", "markdown": "## Ulaşım — Транспорт\n\n| Турецкий | Русский |\n|----------|--------|\n| **otobüs** | автобус |\n| **taksi** | такси |\n| **metro** | метро |\n| **tramvay** | трамвай |\n| **tren** | поезд |\n| **uçak** | самолёт |\n| **gemi** | корабль |\n| **araba** | машина |\n| **bisiklet** | велосипед |\n| **dolmuş** | маршрутка |\n\n### Полезные фразы:\n- **Otobüs durağı nerede?** — Где автобусная остановка?\n- **Bilet ne kadar?** — Сколько стоит билет?\n- **Bir bilet lütfen.** — Один билет, пожалуйста.\n- **Bu otobüs Taksim'e gidiyor mu?** — Этот автобус едет на Таксим?"},
                    {"type": "flashcards", "cards": [{"front": "otobüs", "back": "автобус"}, {"front": "taksi", "back": "такси"}, {"front": "metro", "back": "метро"}, {"front": "tren", "back": "поезд"}, {"front": "uçak", "back": "самолёт"}, {"front": "dolmuş", "back": "маршрутка"}, {"front": "bisiklet", "back": "велосипед"}]},
                    {"type": "matching", "pairs": [{"left": "otobüs", "right": "автобус"}, {"left": "tren", "right": "поезд"}, {"left": "uçak", "right": "самолёт"}, {"left": "gemi", "right": "корабль"}, {"left": "bisiklet", "right": "велосипед"}, {"left": "dolmuş", "right": "маршрутка"}]},
                    {"type": "quiz", "question": "Что такое «dolmuş»?", "options": [{"id": "a", "text": "Такси", "correct": False}, {"id": "b", "text": "Маршрутка", "correct": True}, {"id": "c", "text": "Трамвай", "correct": False}, {"id": "d", "text": "Метро", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: самолёт", "acceptedAnswers": ["uçak", "Uçak"]},
                    {"type": "fill-blank", "text": "Otobüs ___ nerede? (Где автобусная остановка?)", "answers": ["durağı"]},
                    {"type": "true-false", "statement": "Dolmuş — это маршрутное такси, типичное для Турции.", "correct": True},
                    {"type": "quiz", "question": "Как спросить «Сколько стоит билет?»?", "options": [{"id": "a", "text": "Bilet ne kadar?", "correct": True}, {"id": "b", "text": "Bilet nerede?", "correct": False}, {"id": "c", "text": "Bilet ne?", "correct": False}, {"id": "d", "text": "Bilet kaç?", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: поезд", "acceptedAnswers": ["tren", "Tren"]},
                    {"type": "multi-select", "question": "Какие виды наземного транспорта?", "options": [{"id": "a", "text": "otobüs", "correct": True}, {"id": "b", "text": "uçak", "correct": False}, {"id": "c", "text": "tramvay", "correct": True}, {"id": "d", "text": "gemi", "correct": False}, {"id": "e", "text": "dolmuş", "correct": True}]},
                ],
            },
            {
                "t": "Yönler — Направления",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Направления", "markdown": "## Yönler — Направления\n\n| Турецкий | Русский |\n|----------|--------|\n| **sağ** | право |\n| **sol** | лево |\n| **düz** | прямо |\n| **karşı** | напротив |\n| **yanında** | рядом |\n| **arkasında** | за/позади |\n| **önünde** | перед |\n| **arasında** | между |\n| **köşe** | угол |\n| **cadde** | проспект/улица |\n| **sokak** | переулок |\n\n### Полезные фразы:\n- **Sağa dönün.** — Поверните направо.\n- **Sola dönün.** — Поверните налево.\n- **Düz gidin.** — Идите прямо.\n- **Affedersiniz, ... nerede?** — Извините, где ...?\n- **Burası neresi?** — Где я (это место)?"},
                    {"type": "flashcards", "cards": [{"front": "sağ", "back": "право"}, {"front": "sol", "back": "лево"}, {"front": "düz", "back": "прямо"}, {"front": "karşı", "back": "напротив"}, {"front": "yanında", "back": "рядом"}, {"front": "köşe", "back": "угол"}]},
                    {"type": "matching", "pairs": [{"left": "sağ", "right": "право"}, {"left": "sol", "right": "лево"}, {"left": "düz", "right": "прямо"}, {"left": "karşı", "right": "напротив"}, {"left": "yanında", "right": "рядом"}, {"left": "arkasında", "right": "позади"}]},
                    {"type": "quiz", "question": "Как сказать «Идите прямо»?", "options": [{"id": "a", "text": "Sağa dönün", "correct": False}, {"id": "b", "text": "Düz gidin", "correct": True}, {"id": "c", "text": "Sola dönün", "correct": False}, {"id": "d", "text": "Geri dönün", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «направо»?", "acceptedAnswers": ["sağa", "Sağa", "sağ"]},
                    {"type": "fill-blank", "text": "___ dönün. (Поверните налево.)", "answers": ["Sola"]},
                    {"type": "true-false", "statement": "Cadde — это переулок по-турецки.", "correct": False},
                    {"type": "fill-blank", "text": "Affedersiniz, banka ___? (Извините, где банк?)", "answers": ["nerede"]},
                    {"type": "quiz", "question": "Что означает «yanında»?", "options": [{"id": "a", "text": "Позади", "correct": False}, {"id": "b", "text": "Рядом", "correct": True}, {"id": "c", "text": "Напротив", "correct": False}, {"id": "d", "text": "Далеко", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова обозначают положение в пространстве?", "options": [{"id": "a", "text": "yanında (рядом)", "correct": True}, {"id": "b", "text": "arkasında (позади)", "correct": True}, {"id": "c", "text": "cadde (улица)", "correct": False}, {"id": "d", "text": "önünde (перед)", "correct": True}]},
                ],
            },
            {
                "t": "Restoran — В ресторане",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "В ресторане", "markdown": "## Restoran — В ресторане\n\n### Полезные фразы:\n| Турецкий | Русский |\n|----------|--------|\n| **Menü, lütfen.** | Меню, пожалуйста. |\n| **Ne önerirsiniz?** | Что посоветуете? |\n| **Hesap, lütfen.** | Счёт, пожалуйста. |\n| **Afiyet olsun!** | Приятного аппетита! |\n| **Çok lezzetli!** | Очень вкусно! |\n\n### Еда:\n| Турецкий | Русский |\n|----------|--------|\n| **et** | мясо |\n| **tavuk** | курица |\n| **balık** | рыба |\n| **çorba** | суп |\n| **salata** | салат |\n| **pilav** | рис/плов |\n| **ekmek** | хлеб |\n| **su** | вода |\n| **çay** | чай |\n| **kahve** | кофе |\n| **meyve suyu** | сок |\n| **dondurma** | мороженое |"},
                    {"type": "flashcards", "cards": [{"front": "et", "back": "мясо"}, {"front": "tavuk", "back": "курица"}, {"front": "balık", "back": "рыба"}, {"front": "çorba", "back": "суп"}, {"front": "ekmek", "back": "хлеб"}, {"front": "kahve", "back": "кофе"}, {"front": "dondurma", "back": "мороженое"}, {"front": "Afiyet olsun!", "back": "Приятного аппетита!"}]},
                    {"type": "matching", "pairs": [{"left": "et", "right": "мясо"}, {"left": "tavuk", "right": "курица"}, {"left": "çorba", "right": "суп"}, {"left": "ekmek", "right": "хлеб"}, {"left": "kahve", "right": "кофе"}, {"left": "dondurma", "right": "мороженое"}]},
                    {"type": "quiz", "question": "Как попросить счёт в ресторане?", "options": [{"id": "a", "text": "Menü, lütfen", "correct": False}, {"id": "b", "text": "Hesap, lütfen", "correct": True}, {"id": "c", "text": "Su, lütfen", "correct": False}, {"id": "d", "text": "Teşekkürler", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «суп»?", "acceptedAnswers": ["çorba", "Çorba"]},
                    {"type": "type-answer", "question": "Как сказать «Приятного аппетита»?", "acceptedAnswers": ["Afiyet olsun!", "Afiyet olsun", "afiyet olsun"]},
                    {"type": "fill-blank", "text": "Çok ___! (Очень вкусно!)", "answers": ["lezzetli"]},
                    {"type": "true-false", "statement": "Pilav — это салат по-турецки.", "correct": False},
                    {"type": "category-sort", "categories": ["Еда", "Напитки"], "items": [{"text": "et (мясо)", "category": "Еда"}, {"text": "tavuk (курица)", "category": "Еда"}, {"text": "çorba (суп)", "category": "Еда"}, {"text": "su (вода)", "category": "Напитки"}, {"text": "çay (чай)", "category": "Напитки"}, {"text": "kahve (кофе)", "category": "Напитки"}]},
                    {"type": "multi-select", "question": "Какие фразы полезны в ресторане?", "options": [{"id": "a", "text": "Menü, lütfen", "correct": True}, {"id": "b", "text": "Hesap, lütfen", "correct": True}, {"id": "c", "text": "Nerelisiniz?", "correct": False}, {"id": "d", "text": "Afiyet olsun!", "correct": True}]},
                ],
            },
            {
                "t": "Alışveriş — Покупки",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Покупки", "markdown": "## Alışveriş — Покупки\n\n### Полезные фразы:\n| Турецкий | Русский |\n|----------|--------|\n| **Bu ne kadar?** | Сколько это стоит? |\n| **Çok pahalı!** | Очень дорого! |\n| **İndirim var mı?** | Есть скидка? |\n| **Bunu alacağım.** | Я возьму это. |\n| **Kredi kartı geçiyor mu?** | Принимаете карту? |\n| **Nakit ödeyeceğim.** | Заплачу наличными. |\n| **Fişi alabilir miyim?** | Можно чек? |\n\n### Места:\n| Турецкий | Русский |\n|----------|--------|\n| **market** | магазин |\n| **çarşı** | рынок/базар |\n| **alışveriş merkezi (AVM)** | торговый центр |\n| **bakkal** | продуктовая лавка |\n| **eczane** | аптека |\n| **fırın** | пекарня |\n\n### Важно:\nНа турецких базарах принято **торговаться** (pazarlık yapmak)!"},
                    {"type": "flashcards", "cards": [{"front": "Bu ne kadar?", "back": "Сколько это стоит?"}, {"front": "Çok pahalı!", "back": "Очень дорого!"}, {"front": "İndirim var mı?", "back": "Есть скидка?"}, {"front": "çarşı", "back": "рынок/базар"}, {"front": "eczane", "back": "аптека"}, {"front": "fırın", "back": "пекарня"}]},
                    {"type": "matching", "pairs": [{"left": "Bu ne kadar?", "right": "Сколько это стоит?"}, {"left": "Çok pahalı!", "right": "Очень дорого!"}, {"left": "çarşı", "right": "рынок/базар"}, {"left": "eczane", "right": "аптека"}, {"left": "bakkal", "right": "продуктовая лавка"}, {"left": "fırın", "right": "пекарня"}]},
                    {"type": "quiz", "question": "Как спросить «Сколько это стоит?»?", "options": [{"id": "a", "text": "Bu ne kadar?", "correct": True}, {"id": "b", "text": "Bu ne?", "correct": False}, {"id": "c", "text": "Kaç tane?", "correct": False}, {"id": "d", "text": "Nerede?", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «аптека»?", "acceptedAnswers": ["eczane", "Eczane"]},
                    {"type": "fill-blank", "text": "___ var mı? (Есть скидка?)", "answers": ["İndirim"]},
                    {"type": "true-false", "statement": "На турецких базарах не принято торговаться.", "correct": False},
                    {"type": "type-answer", "question": "Как сказать «Очень дорого!»?", "acceptedAnswers": ["Çok pahalı!", "Çok pahalı", "çok pahalı"]},
                    {"type": "quiz", "question": "Что такое AVM?", "options": [{"id": "a", "text": "Торговый центр", "correct": True}, {"id": "b", "text": "Аэропорт", "correct": False}, {"id": "c", "text": "Автовокзал", "correct": False}, {"id": "d", "text": "Аптека", "correct": False}]},
                    {"type": "category-sort", "categories": ["Фразы покупателя", "Места"], "items": [{"text": "Bu ne kadar?", "category": "Фразы покупателя"}, {"text": "Bunu alacağım", "category": "Фразы покупателя"}, {"text": "İndirim var mı?", "category": "Фразы покупателя"}, {"text": "çarşı", "category": "Места"}, {"text": "eczane", "category": "Места"}, {"text": "bakkal", "category": "Места"}]},
                    {"type": "multi-select", "question": "Какие фразы полезны при покупках?", "options": [{"id": "a", "text": "Bu ne kadar?", "correct": True}, {"id": "b", "text": "İndirim var mı?", "correct": True}, {"id": "c", "text": "Nasılsınız?", "correct": False}, {"id": "d", "text": "Kredi kartı geçiyor mu?", "correct": True}]},
                ],
            },
            {
                "t": "Числа 20-1000 и деньги",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Числа 20-1000", "markdown": "## Числа от 20 до 1000\n\n### Десятки:\n| Число | Турецкий |\n|-------|----------|\n| 20 | **yirmi** |\n| 30 | **otuz** |\n| 40 | **kırk** |\n| 50 | **elli** |\n| 60 | **altmış** |\n| 70 | **yetmiş** |\n| 80 | **seksen** |\n| 90 | **doksan** |\n| 100 | **yüz** |\n| 1000 | **bin** |\n\n### Составные числа:\n- 25 = yirmi beş\n- 43 = kırk üç\n- 156 = yüz elli altı\n- 999 = dokuz yüz doksan dokuz\n\n### Деньги:\n- **Türk Lirası (TL)** — турецкая лира\n- **kuruş** — курущ (1 лира = 100 курущей)\n- **Bu elli lira.** — Это 50 лир.\n- **Yüz lira var mı?** — У вас есть 100 лир?"},
                    {"type": "flashcards", "cards": [{"front": "yirmi", "back": "20"}, {"front": "otuz", "back": "30"}, {"front": "kırk", "back": "40"}, {"front": "elli", "back": "50"}, {"front": "yüz", "back": "100"}, {"front": "bin", "back": "1000"}, {"front": "Türk Lirası", "back": "Турецкая лира (TL)"}]},
                    {"type": "matching", "pairs": [{"left": "yirmi", "right": "20"}, {"left": "kırk", "right": "40"}, {"left": "elli", "right": "50"}, {"left": "yetmiş", "right": "70"}, {"left": "yüz", "right": "100"}, {"left": "bin", "right": "1000"}]},
                    {"type": "quiz", "question": "Как сказать 156 по-турецки?", "options": [{"id": "a", "text": "yüz elli altı", "correct": True}, {"id": "b", "text": "bir yüz beş altı", "correct": False}, {"id": "c", "text": "yüz altmış beş", "correct": False}, {"id": "d", "text": "elli altı yüz", "correct": False}]},
                    {"type": "type-answer", "question": "Как будет 50 по-турецки?", "acceptedAnswers": ["elli", "Elli"]},
                    {"type": "type-answer", "question": "Как будет 1000 по-турецки?", "acceptedAnswers": ["bin", "Bin"]},
                    {"type": "fill-blank", "text": "43 = ___ üç", "answers": ["kırk"]},
                    {"type": "true-false", "statement": "Yüz означает 1000 по-турецки.", "correct": False},
                    {"type": "quiz", "question": "Как называется турецкая валюта?", "options": [{"id": "a", "text": "Türk Lirası", "correct": True}, {"id": "b", "text": "Türk Markı", "correct": False}, {"id": "c", "text": "Türk Doları", "correct": False}, {"id": "d", "text": "Türk Eurosu", "correct": False}]},
                    {"type": "drag-order", "items": ["yirmi (20)", "otuz (30)", "kırk (40)", "elli (50)", "altmış (60)", "yetmiş (70)", "seksen (80)", "doksan (90)", "yüz (100)"]},
                    {"type": "multi-select", "question": "Какие числа верно записаны?", "options": [{"id": "a", "text": "25 = yirmi beş", "correct": True}, {"id": "b", "text": "40 = kırk", "correct": True}, {"id": "c", "text": "60 = elli", "correct": False}, {"id": "d", "text": "999 = dokuz yüz doksan dokuz", "correct": True}]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 7: Путешествия
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Путешествия",
        "pos": 6,
        "lessons": [
            {
                "t": "Havalimanı — Аэропорт",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "В аэропорту", "markdown": "## Havalimanı — Аэропорт\n\n### Лексика:\n| Турецкий | Русский |\n|----------|--------|\n| **havalimanı** | аэропорт |\n| **uçuş** | рейс |\n| **gidiş** | вылет |\n| **varış** | прилёт |\n| **pasaport kontrolü** | паспортный контроль |\n| **bagaj** | багаж |\n| **biniş kartı** | посадочный талон |\n| **kapı (gate)** | выход (гейт) |\n| **gümrük** | таможня |\n| **aktarma** | пересадка |\n\n### Полезные фразы:\n- **Uçuşum saat kaçta?** — Во сколько мой рейс?\n- **Kapı numarası kaç?** — Какой номер выхода?\n- **Bagajım kayboldu.** — Мой багаж потерялся.\n- **Nereye aktarma yapacağım?** — Где мне делать пересадку?"},
                    {"type": "flashcards", "cards": [{"front": "havalimanı", "back": "аэропорт"}, {"front": "uçuş", "back": "рейс"}, {"front": "bagaj", "back": "багаж"}, {"front": "biniş kartı", "back": "посадочный талон"}, {"front": "gümrük", "back": "таможня"}, {"front": "aktarma", "back": "пересадка"}]},
                    {"type": "matching", "pairs": [{"left": "havalimanı", "right": "аэропорт"}, {"left": "uçuş", "right": "рейс"}, {"left": "bagaj", "right": "багаж"}, {"left": "biniş kartı", "right": "посадочный талон"}, {"left": "gümrük", "right": "таможня"}, {"left": "aktarma", "right": "пересадка"}]},
                    {"type": "quiz", "question": "Как по-турецки «посадочный талон»?", "options": [{"id": "a", "text": "bagaj", "correct": False}, {"id": "b", "text": "biniş kartı", "correct": True}, {"id": "c", "text": "pasaport", "correct": False}, {"id": "d", "text": "bilet", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: аэропорт", "acceptedAnswers": ["havalimanı", "Havalimanı"]},
                    {"type": "fill-blank", "text": "Bagajım ___. (Мой багаж потерялся.)", "answers": ["kayboldu"]},
                    {"type": "true-false", "statement": "Gidiş означает «прилёт» по-турецки.", "correct": False},
                    {"type": "type-answer", "question": "Переведите: пересадка", "acceptedAnswers": ["aktarma", "Aktarma"]},
                    {"type": "quiz", "question": "Как спросить «Какой номер выхода?»?", "options": [{"id": "a", "text": "Kapı numarası kaç?", "correct": True}, {"id": "b", "text": "Uçuş numarası ne?", "correct": False}, {"id": "c", "text": "Bagaj nerede?", "correct": False}, {"id": "d", "text": "Bilet ne kadar?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова связаны с аэропортом?", "options": [{"id": "a", "text": "uçuş", "correct": True}, {"id": "b", "text": "gümrük", "correct": True}, {"id": "c", "text": "çarşı", "correct": False}, {"id": "d", "text": "biniş kartı", "correct": True}, {"id": "e", "text": "mutfak", "correct": False}]},
                ],
            },
            {
                "t": "Otel — Гостиница",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "В гостинице", "markdown": "## Otel — Гостиница\n\n### Лексика:\n| Турецкий | Русский |\n|----------|--------|\n| **oda** | номер/комната |\n| **tek kişilik oda** | одноместный номер |\n| **çift kişilik oda** | двухместный номер |\n| **kahvaltı** | завтрак |\n| **resepsiyon** | ресепшн |\n| **anahtar** | ключ |\n| **asansör** | лифт |\n| **kat** | этаж |\n| **havuz** | бассейн |\n| **otopark** | парковка |\n\n### Полезные фразы:\n- **Bir oda ayırtmak istiyorum.** — Хочу забронировать номер.\n- **Kahvaltı dahil mi?** — Завтрак включён?\n- **Wi-Fi şifresi ne?** — Какой пароль от Wi-Fi?\n- **Saat kaçta çıkış yapmalıyım?** — Во сколько чек-аут?\n- **Odamda sorun var.** — В моём номере проблема."},
                    {"type": "flashcards", "cards": [{"front": "oda", "back": "номер/комната"}, {"front": "kahvaltı", "back": "завтрак"}, {"front": "anahtar", "back": "ключ"}, {"front": "asansör", "back": "лифт"}, {"front": "havuz", "back": "бассейн"}, {"front": "kat", "back": "этаж"}]},
                    {"type": "matching", "pairs": [{"left": "tek kişilik oda", "right": "одноместный номер"}, {"left": "çift kişilik oda", "right": "двухместный номер"}, {"left": "kahvaltı", "right": "завтрак"}, {"left": "anahtar", "right": "ключ"}, {"left": "asansör", "right": "лифт"}, {"left": "havuz", "right": "бассейн"}]},
                    {"type": "quiz", "question": "Как сказать «Завтрак включён?»?", "options": [{"id": "a", "text": "Kahvaltı dahil mi?", "correct": True}, {"id": "b", "text": "Kahvaltı var mı?", "correct": False}, {"id": "c", "text": "Kahvaltı nerede?", "correct": False}, {"id": "d", "text": "Kahvaltı ne kadar?", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: ключ", "acceptedAnswers": ["anahtar", "Anahtar"]},
                    {"type": "fill-blank", "text": "Bir oda ___ istiyorum. (Хочу забронировать номер.)", "answers": ["ayırtmak"]},
                    {"type": "true-false", "statement": "Kat означает «комната» по-турецки.", "correct": False},
                    {"type": "type-answer", "question": "Переведите: завтрак", "acceptedAnswers": ["kahvaltı", "Kahvaltı"]},
                    {"type": "quiz", "question": "Как спросить пароль от Wi-Fi?", "options": [{"id": "a", "text": "Wi-Fi şifresi ne?", "correct": True}, {"id": "b", "text": "Wi-Fi var mı?", "correct": False}, {"id": "c", "text": "İnternet nerede?", "correct": False}, {"id": "d", "text": "Wi-Fi ne kadar?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова связаны с отелем?", "options": [{"id": "a", "text": "resepsiyon", "correct": True}, {"id": "b", "text": "anahtar", "correct": True}, {"id": "c", "text": "dolmuş", "correct": False}, {"id": "d", "text": "havuz", "correct": True}]},
                ],
            },
            {
                "t": "Geziler — Экскурсии и достопримечательности",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Экскурсии", "markdown": "## Geziler — Экскурсии\n\n### Достопримечательности:\n| Турецкий | Русский |\n|----------|--------|\n| **cami** | мечеть |\n| **müze** | музей |\n| **saray** | дворец |\n| **kale** | крепость |\n| **çeşme** | фонтан |\n| **köprü** | мост |\n| **plaj** | пляж |\n| **ada** | остров |\n\n### Фразы:\n- **Bilet ne kadar?** — Сколько стоит билет?\n- **Rehber var mı?** — Есть гид?\n- **Fotoğraf çekebilir miyim?** — Можно фотографировать?\n- **Müze saat kaçta kapanıyor?** — Во сколько закрывается музей?\n- **Burası çok güzel!** — Здесь очень красиво!\n\n### Популярные места Турции:\n- **Ayasofya** — Собор Святой Софии\n- **Topkapı Sarayı** — Дворец Топкапы\n- **Kapadokya** — Каппадокия\n- **Pamukkale** — Памуккале"},
                    {"type": "flashcards", "cards": [{"front": "cami", "back": "мечеть"}, {"front": "müze", "back": "музей"}, {"front": "saray", "back": "дворец"}, {"front": "kale", "back": "крепость"}, {"front": "plaj", "back": "пляж"}, {"front": "ada", "back": "остров"}, {"front": "Kapadokya", "back": "Каппадокия"}, {"front": "Pamukkale", "back": "Памуккале"}]},
                    {"type": "matching", "pairs": [{"left": "cami", "right": "мечеть"}, {"left": "müze", "right": "музей"}, {"left": "saray", "right": "дворец"}, {"left": "kale", "right": "крепость"}, {"left": "plaj", "right": "пляж"}, {"left": "ada", "right": "остров"}]},
                    {"type": "quiz", "question": "Как спросить «Можно фотографировать?»?", "options": [{"id": "a", "text": "Fotoğraf çekebilir miyim?", "correct": True}, {"id": "b", "text": "Fotoğraf var mı?", "correct": False}, {"id": "c", "text": "Fotoğraf nerede?", "correct": False}, {"id": "d", "text": "Fotoğraf ne kadar?", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: мечеть", "acceptedAnswers": ["cami", "Cami"]},
                    {"type": "type-answer", "question": "Переведите: музей", "acceptedAnswers": ["müze", "Müze"]},
                    {"type": "fill-blank", "text": "Burası çok ___! (Здесь очень красиво!)", "answers": ["güzel"]},
                    {"type": "true-false", "statement": "Saray — это мечеть по-турецки.", "correct": False},
                    {"type": "quiz", "question": "Что такое Ayasofya?", "options": [{"id": "a", "text": "Собор Святой Софии", "correct": True}, {"id": "b", "text": "Голубая мечеть", "correct": False}, {"id": "c", "text": "Дворец Топкапы", "correct": False}, {"id": "d", "text": "Памуккале", "correct": False}]},
                    {"type": "multi-select", "question": "Какие слова обозначают достопримечательности?", "options": [{"id": "a", "text": "cami", "correct": True}, {"id": "b", "text": "müze", "correct": True}, {"id": "c", "text": "market", "correct": False}, {"id": "d", "text": "kale", "correct": True}]},
                ],
            },
            {
                "t": "Sorunlar — Проблемы в путешествии",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Проблемы и помощь", "markdown": "## Sorunlar — Проблемы\n\n### Экстренные фразы:\n| Турецкий | Русский |\n|----------|--------|\n| **Yardım edin!** | Помогите! |\n| **İmdat!** | На помощь! |\n| **Polis çağırın!** | Вызовите полицию! |\n| **Ambulans çağırın!** | Вызовите скорую! |\n| **Kayboldum.** | Я потерялся/потерялась. |\n| **Pasaportumu kaybettim.** | Я потерял(а) паспорт. |\n| **Cüzdanım çalındı.** | Мой кошелёк украли. |\n| **Türkçe bilmiyorum.** | Я не знаю турецкий. |\n| **İngilizce bilen var mı?** | Кто-нибудь говорит по-английски? |\n\n### Полезные номера:\n- **112** — Скорая помощь\n- **155** — Полиция\n- **110** — Пожарная служба"},
                    {"type": "flashcards", "cards": [{"front": "Yardım edin!", "back": "Помогите!"}, {"front": "Kayboldum", "back": "Я потерялся"}, {"front": "Pasaportumu kaybettim", "back": "Я потерял паспорт"}, {"front": "Cüzdanım çalındı", "back": "Мой кошелёк украли"}, {"front": "112", "back": "Скорая помощь"}, {"front": "155", "back": "Полиция"}]},
                    {"type": "matching", "pairs": [{"left": "Yardım edin!", "right": "Помогите!"}, {"left": "Kayboldum", "right": "Я потерялся"}, {"left": "112", "right": "Скорая помощь"}, {"left": "155", "right": "Полиция"}, {"left": "110", "right": "Пожарная служба"}]},
                    {"type": "quiz", "question": "Какой номер экстренной помощи (скорая) в Турции?", "options": [{"id": "a", "text": "911", "correct": False}, {"id": "b", "text": "112", "correct": True}, {"id": "c", "text": "103", "correct": False}, {"id": "d", "text": "999", "correct": False}]},
                    {"type": "type-answer", "question": "Как сказать «Помогите!» по-турецки?", "acceptedAnswers": ["Yardım edin!", "Yardım edin", "yardım edin"]},
                    {"type": "fill-blank", "text": "Pasaportumu ___. (Я потерял паспорт.)", "answers": ["kaybettim"]},
                    {"type": "true-false", "statement": "Номер полиции в Турции — 155.", "correct": True},
                    {"type": "type-answer", "question": "Как сказать «Я потерялся»?", "acceptedAnswers": ["Kayboldum", "kayboldum"]},
                    {"type": "quiz", "question": "Как спросить «Кто-нибудь говорит по-английски?»?", "options": [{"id": "a", "text": "İngilizce bilen var mı?", "correct": True}, {"id": "b", "text": "İngilizce konuşun!", "correct": False}, {"id": "c", "text": "İngilizce biliyorum.", "correct": False}, {"id": "d", "text": "İngilizce nerede?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие фразы используются в экстренных ситуациях?", "options": [{"id": "a", "text": "Yardım edin!", "correct": True}, {"id": "b", "text": "İmdat!", "correct": True}, {"id": "c", "text": "Merhaba!", "correct": False}, {"id": "d", "text": "Polis çağırın!", "correct": True}]},
                ],
            },
            {
                "t": "Doktor — У врача",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "У врача", "markdown": "## Doktor — У врача\n\n### Части тела:\n| Турецкий | Русский |\n|----------|--------|\n| **baş** | голова |\n| **göz** | глаз |\n| **kulak** | ухо |\n| **burun** | нос |\n| **ağız** | рот |\n| **diş** | зуб |\n| **boğaz** | горло |\n| **karın** | живот |\n| **sırt** | спина |\n| **bacak** | нога |\n| **kol** | рука |\n\n### Фразы у врача:\n| Турецкий | Русский |\n|----------|--------|\n| **Hastayım.** | Я болен/больна. |\n| **Başım ağrıyor.** | У меня болит голова. |\n| **Ateşim var.** | У меня температура. |\n| **Alerjim var.** | У меня аллергия. |\n| **İlaç almam lazım.** | Мне нужно лекарство. |\n| **Reçete yazabilir misiniz?** | Можете выписать рецепт? |"},
                    {"type": "flashcards", "cards": [{"front": "baş", "back": "голова"}, {"front": "göz", "back": "глаз"}, {"front": "boğaz", "back": "горло"}, {"front": "karın", "back": "живот"}, {"front": "Hastayım", "back": "Я болен/больна"}, {"front": "Başım ağrıyor", "back": "У меня болит голова"}, {"front": "Ateşim var", "back": "У меня температура"}]},
                    {"type": "matching", "pairs": [{"left": "baş", "right": "голова"}, {"left": "göz", "right": "глаз"}, {"left": "kulak", "right": "ухо"}, {"left": "boğaz", "right": "горло"}, {"left": "karın", "right": "живот"}, {"left": "diş", "right": "зуб"}]},
                    {"type": "quiz", "question": "Как сказать «У меня болит голова»?", "options": [{"id": "a", "text": "Başım ağrıyor", "correct": True}, {"id": "b", "text": "Karınım ağrıyor", "correct": False}, {"id": "c", "text": "Gözüm ağrıyor", "correct": False}, {"id": "d", "text": "Hastayım", "correct": False}]},
                    {"type": "type-answer", "question": "Переведите: горло", "acceptedAnswers": ["boğaz", "Boğaz"]},
                    {"type": "type-answer", "question": "Как сказать «Я болен»?", "acceptedAnswers": ["Hastayım", "hastayım"]},
                    {"type": "fill-blank", "text": "___ var. (У меня температура.)", "answers": ["Ateşim"]},
                    {"type": "true-false", "statement": "Karın означает «голова» по-турецки.", "correct": False},
                    {"type": "category-sort", "categories": ["Голова", "Тело"], "items": [{"text": "göz (глаз)", "category": "Голова"}, {"text": "kulak (ухо)", "category": "Голова"}, {"text": "burun (нос)", "category": "Голова"}, {"text": "karın (живот)", "category": "Тело"}, {"text": "sırt (спина)", "category": "Тело"}, {"text": "bacak (нога)", "category": "Тело"}]},
                    {"type": "quiz", "question": "Как попросить рецепт у врача?", "options": [{"id": "a", "text": "Reçete yazabilir misiniz?", "correct": True}, {"id": "b", "text": "İlaç var mı?", "correct": False}, {"id": "c", "text": "Doktor nerede?", "correct": False}, {"id": "d", "text": "Hastane ne kadar?", "correct": False}]},
                    {"type": "multi-select", "question": "Какие фразы полезны у врача?", "options": [{"id": "a", "text": "Hastayım", "correct": True}, {"id": "b", "text": "Ateşim var", "correct": True}, {"id": "c", "text": "Hesap, lütfen", "correct": False}, {"id": "d", "text": "Alerjim var", "correct": True}]},
                ],
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # SECTION 8: Культура и обзор
    # ═══════════════════════════════════════════════════════════════════
    {
        "title": "Культура и обзор",
        "pos": 7,
        "lessons": [
            {
                "t": "Турецкая культура и традиции",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Культура Турции", "markdown": "## Türk Kültürü — Турецкая культура\n\n### Ключевые понятия:\n| Турецкий | Русский |\n|----------|--------|\n| **misafirperverlik** | гостеприимство |\n| **bayram** | праздник |\n| **nazar boncuğu** | оберег от сглаза |\n| **hamam** | турецкая баня |\n| **çay kültürü** | чайная культура |\n\n### Традиции:\n- **Гостеприимство** — турки очень гостеприимны. Гостю всегда предложат çay (чай)\n- **Nazar boncuğu** — синий глаз, защита от сглаза. Есть везде!\n- **Bayramlar** — главные праздники: Ramazan Bayramı, Kurban Bayramı\n- **Çay** — турки пьют больше чая, чем кофе. Чай подают в стаканчиках-тюльпанах (ince belli bardak)\n- **Hamam** — традиционная турецкая баня, важная часть культуры\n\n### Этикет:\n- Снимайте обувь при входе в дом и мечеть\n- Старшим говорят **siz** (вы), а не **sen** (ты)\n- Рукопожатие — стандартное приветствие"},
                    {"type": "flashcards", "cards": [{"front": "misafirperverlik", "back": "гостеприимство"}, {"front": "bayram", "back": "праздник"}, {"front": "nazar boncuğu", "back": "оберег от сглаза (синий глаз)"}, {"front": "hamam", "back": "турецкая баня"}, {"front": "çay kültürü", "back": "чайная культура"}]},
                    {"type": "matching", "pairs": [{"left": "misafirperverlik", "right": "гостеприимство"}, {"left": "bayram", "right": "праздник"}, {"left": "nazar boncuğu", "right": "оберег от сглаза"}, {"left": "hamam", "right": "турецкая баня"}, {"left": "çay", "right": "чай"}]},
                    {"type": "quiz", "question": "Что такое nazar boncuğu?", "options": [{"id": "a", "text": "Турецкий чай", "correct": False}, {"id": "b", "text": "Оберег от сглаза (синий глаз)", "correct": True}, {"id": "c", "text": "Турецкая сладость", "correct": False}, {"id": "d", "text": "Турецкая баня", "correct": False}]},
                    {"type": "true-false", "statement": "В Турции пьют больше кофе, чем чая.", "correct": False},
                    {"type": "true-false", "statement": "При входе в турецкий дом принято снимать обувь.", "correct": True},
                    {"type": "fill-blank", "text": "Турецкий чай подают в стаканчиках-___ (тюльпанах).", "answers": ["тюльпанах", "ince belli bardak"]},
                    {"type": "quiz", "question": "Какой главный праздник в Турции?", "options": [{"id": "a", "text": "Ramazan Bayramı", "correct": True}, {"id": "b", "text": "Yılbaşı", "correct": False}, {"id": "c", "text": "Doğum günü", "correct": False}, {"id": "d", "text": "Okul bayramı", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «гостеприимство»?", "acceptedAnswers": ["misafirperverlik", "Misafirperverlik"]},
                    {"type": "multi-select", "question": "Какие утверждения о турецкой культуре верны?", "options": [{"id": "a", "text": "Турки очень гостеприимны", "correct": True}, {"id": "b", "text": "Обувь не снимают в доме", "correct": False}, {"id": "c", "text": "Nazar boncuğu — оберег от сглаза", "correct": True}, {"id": "d", "text": "Старшим говорят siz (вы)", "correct": True}]},
                ],
            },
            {
                "t": "Türk Mutfağı — Турецкая кухня",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Турецкая кухня", "markdown": "## Türk Mutfağı — Турецкая кухня\n\n### Знаменитые блюда:\n| Турецкий | Русский |\n|----------|--------|\n| **kebap** | кебаб |\n| **döner** | дёнер |\n| **lahmacun** | лахмаджун (турецкая пицца) |\n| **pide** | пиде (лепёшка с начинкой) |\n| **köfte** | кёфте (фрикадельки) |\n| **baklava** | баклава |\n| **lokum** | лукум |\n| **börek** | бёрек (слоёный пирог) |\n| **dolma** | долма |\n| **çorba** | суп |\n| **ayran** | айран |\n| **türk kahvesi** | турецкий кофе |\n\n### Завтрак (kahvaltı):\nТурецкий завтрак — это целый стол:\n- Сыр (peynir), оливки (zeytin), помидоры (domates), огурцы (salatalık), мёд (bal), варенье (reçel), яйца (yumurta), хлеб (ekmek)\n\n### Поговорка:\n**Afiyet olsun!** — Приятного аппетита!"},
                    {"type": "flashcards", "cards": [{"front": "kebap", "back": "кебаб"}, {"front": "döner", "back": "дёнер"}, {"front": "lahmacun", "back": "лахмаджун (турецкая пицца)"}, {"front": "baklava", "back": "баклава"}, {"front": "lokum", "back": "лукум"}, {"front": "börek", "back": "бёрек (слоёный пирог)"}, {"front": "ayran", "back": "айран"}, {"front": "türk kahvesi", "back": "турецкий кофе"}]},
                    {"type": "matching", "pairs": [{"left": "kebap", "right": "кебаб"}, {"left": "döner", "right": "дёнер"}, {"left": "baklava", "right": "баклава"}, {"left": "lokum", "right": "лукум"}, {"left": "ayran", "right": "айран"}, {"left": "börek", "right": "слоёный пирог"}]},
                    {"type": "quiz", "question": "Что такое lahmacun?", "options": [{"id": "a", "text": "Турецкий кофе", "correct": False}, {"id": "b", "text": "Турецкая пицца", "correct": True}, {"id": "c", "text": "Слоёный пирог", "correct": False}, {"id": "d", "text": "Фрикадельки", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «баклава»?", "acceptedAnswers": ["baklava", "Baklava"]},
                    {"type": "fill-blank", "text": "Türk ___ — турецкий кофе", "answers": ["kahvesi"]},
                    {"type": "true-false", "statement": "Турецкий завтрак обычно очень скромный — только чай и хлеб.", "correct": False},
                    {"type": "category-sort", "categories": ["Основные блюда", "Десерты/Напитки"], "items": [{"text": "kebap", "category": "Основные блюда"}, {"text": "döner", "category": "Основные блюда"}, {"text": "köfte", "category": "Основные блюда"}, {"text": "baklava", "category": "Десерты/Напитки"}, {"text": "lokum", "category": "Десерты/Напитки"}, {"text": "ayran", "category": "Десерты/Напитки"}]},
                    {"type": "quiz", "question": "Что НЕ входит в типичный турецкий завтрак?", "options": [{"id": "a", "text": "Peynir (сыр)", "correct": False}, {"id": "b", "text": "Zeytin (оливки)", "correct": False}, {"id": "c", "text": "Kebap (кебаб)", "correct": True}, {"id": "d", "text": "Ekmek (хлеб)", "correct": False}]},
                    {"type": "multi-select", "question": "Какие блюда относятся к турецкой кухне?", "options": [{"id": "a", "text": "döner", "correct": True}, {"id": "b", "text": "sushi", "correct": False}, {"id": "c", "text": "lahmacun", "correct": True}, {"id": "d", "text": "börek", "correct": True}]},
                ],
            },
            {
                "t": "Türk Dizileri — Турецкие сериалы",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Турецкие сериалы", "markdown": "## Türk Dizileri — Турецкие сериалы\n\nТурецкие сериалы (dizi) — популярны во всём мире!\n\n### Полезная лексика:\n| Турецкий | Русский |\n|----------|--------|\n| **dizi** | сериал |\n| **film** | фильм |\n| **oyuncu** | актёр/актриса |\n| **yönetmen** | режиссёр |\n| **bölüm** | серия/эпизод |\n| **sezon** | сезон |\n| **altyazı** | субтитры |\n| **dublaj** | дубляж |\n\n### Жанры:\n- **Aşk dizisi** — любовная драма\n- **Tarihi dizi** — исторический сериал\n- **Komedi** — комедия\n- **Aksiyon** — боевик\n\n### Как сериалы помогают учить турецкий:\n1. Живая разговорная речь\n2. Культурный контекст\n3. Повторяющаяся лексика\n4. Сначала с субтитрами (altyazılı), потом без"},
                    {"type": "flashcards", "cards": [{"front": "dizi", "back": "сериал"}, {"front": "bölüm", "back": "серия/эпизод"}, {"front": "oyuncu", "back": "актёр/актриса"}, {"front": "altyazı", "back": "субтитры"}, {"front": "aşk dizisi", "back": "любовная драма"}, {"front": "tarihi dizi", "back": "исторический сериал"}]},
                    {"type": "matching", "pairs": [{"left": "dizi", "right": "сериал"}, {"left": "bölüm", "right": "серия"}, {"left": "oyuncu", "right": "актёр"}, {"left": "yönetmen", "right": "режиссёр"}, {"left": "altyazı", "right": "субтитры"}]},
                    {"type": "quiz", "question": "Как по-турецки «субтитры»?", "options": [{"id": "a", "text": "dublaj", "correct": False}, {"id": "b", "text": "altyazı", "correct": True}, {"id": "c", "text": "bölüm", "correct": False}, {"id": "d", "text": "sezon", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «сериал»?", "acceptedAnswers": ["dizi", "Dizi"]},
                    {"type": "fill-blank", "text": "Tarihi ___ — исторический сериал", "answers": ["dizi"]},
                    {"type": "true-false", "statement": "Турецкие сериалы популярны только в Турции.", "correct": False},
                    {"type": "quiz", "question": "Что такое «bölüm»?", "options": [{"id": "a", "text": "Сезон", "correct": False}, {"id": "b", "text": "Серия/эпизод", "correct": True}, {"id": "c", "text": "Актёр", "correct": False}, {"id": "d", "text": "Жанр", "correct": False}]},
                    {"type": "multi-select", "question": "Как сериалы помогают учить язык?", "options": [{"id": "a", "text": "Живая разговорная речь", "correct": True}, {"id": "b", "text": "Культурный контекст", "correct": True}, {"id": "c", "text": "Заменяют грамматику", "correct": False}, {"id": "d", "text": "Повторяющаяся лексика", "correct": True}]},
                ],
            },
            {
                "t": "Deyimler — Турецкие идиомы и пословицы",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Идиомы и пословицы", "markdown": "## Deyimler ve Atasözleri — Идиомы и пословицы\n\n### Популярные выражения:\n| Турецкий | Дословно | Значение |\n|----------|----------|----------|\n| **Kolay gelsin** | Пусть будет легко | Удачи в работе |\n| **Geçmiş olsun** | Пусть пройдёт | Выздоравливай |\n| **Allah korusun** | Боже упаси | Не дай бог |\n| **Eline sağlık** | Здоровья рукам | Спасибо за еду (повару) |\n| **Maşallah** | Машалла | Восхищение (защита от сглаза) |\n| **İnşallah** | Иншалла | Если бог даст / Надеюсь |\n\n### Пословицы:\n- **Damlaya damlaya göl olur** — Капля за каплей — озеро (Терпение и труд)\n- **Bir elin nesi var, iki elin sesi var** — У одной руки нет ничего, у двух рук — звук (Вместе мы сила)\n- **Gülen ağıza yumruk gelmez** — К улыбающемуся рту кулак не летит (Добром добро)"},
                    {"type": "flashcards", "cards": [{"front": "Kolay gelsin", "back": "Удачи в работе (пусть будет легко)"}, {"front": "Geçmiş olsun", "back": "Выздоравливай (пусть пройдёт)"}, {"front": "Eline sağlık", "back": "Спасибо за еду (здоровья рукам)"}, {"front": "Maşallah", "back": "Восхищение (защита от сглаза)"}, {"front": "İnşallah", "back": "Если бог даст / Надеюсь"}]},
                    {"type": "matching", "pairs": [{"left": "Kolay gelsin", "right": "Удачи в работе"}, {"left": "Geçmiş olsun", "right": "Выздоравливай"}, {"left": "Eline sağlık", "right": "Спасибо за еду"}, {"left": "Maşallah", "right": "Восхищение"}, {"left": "İnşallah", "right": "Надеюсь / Если бог даст"}]},
                    {"type": "quiz", "question": "Когда говорят «Kolay gelsin»?", "options": [{"id": "a", "text": "Когда кто-то работает (желая удачи)", "correct": True}, {"id": "b", "text": "Когда кто-то болеет", "correct": False}, {"id": "c", "text": "Когда кто-то готовит", "correct": False}, {"id": "d", "text": "На прощание", "correct": False}]},
                    {"type": "type-answer", "question": "Что говорят повару в благодарность?", "acceptedAnswers": ["Eline sağlık", "eline sağlık"]},
                    {"type": "fill-blank", "text": "___ olsun! (Выздоравливай!)", "answers": ["Geçmiş"]},
                    {"type": "true-false", "statement": "Maşallah говорят, когда чем-то восхищаются.", "correct": True},
                    {"type": "quiz", "question": "Что означает пословица «Damlaya damlaya göl olur»?", "options": [{"id": "a", "text": "Терпение и труд всё перетрут", "correct": True}, {"id": "b", "text": "Один в поле не воин", "correct": False}, {"id": "c", "text": "Время — деньги", "correct": False}, {"id": "d", "text": "Тише едешь — дальше будешь", "correct": False}]},
                    {"type": "type-answer", "question": "Как по-турецки «Надеюсь / Если бог даст»?", "acceptedAnswers": ["İnşallah", "inşallah"]},
                    {"type": "multi-select", "question": "Какие выражения используются ежедневно в Турции?", "options": [{"id": "a", "text": "Kolay gelsin", "correct": True}, {"id": "b", "text": "Maşallah", "correct": True}, {"id": "c", "text": "İnşallah", "correct": True}, {"id": "d", "text": "Abrakadabra", "correct": False}]},
                ],
            },
            {
                "t": "Итоговый тест",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Итоговый тест", "markdown": "## Итоговый тест — Türkçe Sınavı\n\nПоздравляем! Вы прошли начальный курс турецкого языка!\n\n### Что вы изучили:\n1. Турецкий алфавит (29 букв)\n2. Гармония гласных (большая и малая)\n3. Личные местоимения и глагол «быть»\n4. Настоящее, прошедшее и будущее время\n5. Повседневная лексика\n6. Фразы для путешествий\n7. Турецкая культура\n\nСейчас проверим ваши знания!"},
                    {"type": "quiz", "question": "Сколько букв в турецком алфавите?", "options": [{"id": "a", "text": "26", "correct": False}, {"id": "b", "text": "29", "correct": True}, {"id": "c", "text": "33", "correct": False}, {"id": "d", "text": "31", "correct": False}]},
                    {"type": "quiz", "question": "Как произносится буква C в турецком?", "options": [{"id": "a", "text": "[к]", "correct": False}, {"id": "b", "text": "[дж]", "correct": True}, {"id": "c", "text": "[ц]", "correct": False}, {"id": "d", "text": "[с]", "correct": False}]},
                    {"type": "fill-blank", "text": "Merhaba! Benim ___ Ali. (Привет! Меня зовут Али.)", "answers": ["adım"]},
                    {"type": "type-answer", "question": "Как сказать «спасибо» по-турецки?", "acceptedAnswers": ["Teşekkür ederim", "teşekkür ederim"]},
                    {"type": "quiz", "question": "Какой суффикс мн. числа у слова «ev» (дом)?", "options": [{"id": "a", "text": "-lar", "correct": False}, {"id": "b", "text": "-ler", "correct": True}]},
                    {"type": "fill-blank", "text": "Ben gel___ (я прихожу — настоящее время)", "answers": ["iyorum"]},
                    {"type": "type-answer", "question": "Как будет «я пошёл» (gitmek)?", "acceptedAnswers": ["gittim", "Gittim"]},
                    {"type": "quiz", "question": "Как спросить «Сколько это стоит?»?", "options": [{"id": "a", "text": "Bu ne kadar?", "correct": True}, {"id": "b", "text": "Bu ne?", "correct": False}, {"id": "c", "text": "Bu nerede?", "correct": False}, {"id": "d", "text": "Bu kim?", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Merhaba", "right": "Привет"}, {"left": "Teşekkür ederim", "right": "Спасибо"}, {"left": "Hoş geldiniz", "right": "Добро пожаловать"}, {"left": "Güle güle", "right": "Пока"}, {"left": "Afiyet olsun", "right": "Приятного аппетита"}]},
                    {"type": "true-false", "statement": "В турецком языке есть грамматический род.", "correct": False},
                    {"type": "type-answer", "question": "Переведите: Я не понимаю (anlamak)", "acceptedAnswers": ["Anlamıyorum", "anlamıyorum"]},
                    {"type": "quiz", "question": "Что такое nazar boncuğu?", "options": [{"id": "a", "text": "Турецкий чай", "correct": False}, {"id": "b", "text": "Оберег от сглаза", "correct": True}, {"id": "c", "text": "Традиционное блюдо", "correct": False}, {"id": "d", "text": "Турецкая баня", "correct": False}]},
                    {"type": "fill-blank", "text": "Kolay ___! (Удачи в работе!)", "answers": ["gelsin"]},
                    {"type": "multi-select", "question": "Какие утверждения о турецком языке верны?", "options": [{"id": "a", "text": "Алфавит на латинице", "correct": True}, {"id": "b", "text": "Агглютинативный язык", "correct": True}, {"id": "c", "text": "Есть гармония гласных", "correct": True}, {"id": "d", "text": "Есть грамматический род", "correct": False}, {"id": "e", "text": "Ударение обычно на последнем слоге", "correct": True}]},
                    {"type": "drag-order", "items": ["A — алфавит", "B — знакомство", "C — гармония гласных", "D — повседневная жизнь", "E — глаголы", "F — в городе", "G — путешествия", "H — культура"]},
                ],
            },
        ],
    },
]


async def seed():
    async with async_session() as db:
        # Find admin or first user
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        if not user:
            print("No users found. Create a user first.")
            return

        # Check if course already exists
        existing = await db.execute(
            select(Course).where(Course.title == COURSE_TITLE)
        )
        if existing.scalar_one_or_none():
            print(f"Course '{COURSE_TITLE}' already exists. Skipping.")
            return

        # Create course
        course = Course(
            title=COURSE_TITLE,
            slug=COURSE_SLUG,
            description=COURSE_DESC,
            author_id=user.id,
            category="Languages",
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
                print(f"    Lesson: {lesson.title} ({len(l_data.get('steps', []))} steps, {l_data['xp']} xp)")

        # Build roadmap
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
        print(f"\nDone! Course '{COURSE_TITLE}' created with {len(all_lesson_ids)} lessons.")


if __name__ == "__main__":
    asyncio.run(seed())
