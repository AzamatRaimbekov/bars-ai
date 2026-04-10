"""Seed: English Language course — full course using all 5 new language step types."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSE_TITLE = "English from Zero to Confidence"
COURSE_DESC = (
    "Полный курс английского языка — от алфавита до свободного общения. "
    "Грамматика, лексика, аудирование, произношение, перевод и деловой английский. "
    "Интерактивные упражнения с AI-проверкой."
)

SECTIONS = [
    # ===== SECTION 1: Basics =====
    {
        "title": "Основы: Алфавит и звуки",
        "pos": 0,
        "lessons": [
            {
                "t": "Английский алфавит",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "26 букв английского алфавита", "markdown": "## Английский алфавит\n\nАнглийский алфавит состоит из **26 букв**: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.\n\n### Гласные (Vowels):\n**A, E, I, O, U** — 5 гласных букв, но в английском более 20 гласных звуков!\n\n### Согласные (Consonants):\nОстальные 21 буква — согласные.\n\n### Важно знать:\n- Буква **C** читается как /k/ (cat) или /s/ (city)\n- Буква **G** читается как /g/ (go) или /dʒ/ (gym)\n- Буква **X** обычно читается как /ks/ (fox)\n- **Y** может быть и гласной (gym) и согласной (yes)"},
                    {"type": "word-builder", "hint": "Алфавит (по-английски)", "word": "alphabet", "image": ""},
                    {"type": "matching", "pairs": [{"left": "A, E, I, O, U", "right": "Гласные (Vowels)"}, {"left": "B, C, D, F, G...", "right": "Согласные (Consonants)"}, {"left": "26", "right": "Количество букв"}, {"left": "Y", "right": "Может быть и гласной и согласной"}]},
                    {"type": "category-sort", "categories": ["Vowels", "Consonants"], "items": [{"text": "A", "category": "Vowels"}, {"text": "B", "category": "Consonants"}, {"text": "E", "category": "Vowels"}, {"text": "K", "category": "Consonants"}, {"text": "I", "category": "Vowels"}, {"text": "T", "category": "Consonants"}, {"text": "O", "category": "Vowels"}, {"text": "U", "category": "Vowels"}]},
                    {"type": "quiz", "question": "Сколько букв в английском алфавите?", "options": [{"id": "a", "text": "24", "correct": False}, {"id": "b", "text": "26", "correct": True}, {"id": "c", "text": "28", "correct": False}, {"id": "d", "text": "33", "correct": False}]},
                ],
            },
            {
                "t": "Звуки и произношение",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "44 звука английского языка", "markdown": "## Звуки английского языка\n\nВ английском **44 звука** (phonemes), хотя букв всего 26.\n\n### Краткие гласные:\n- /ɪ/ — s**i**t\n- /e/ — b**e**d\n- /æ/ — c**a**t\n- /ʌ/ — c**u**p\n- /ʊ/ — p**u**t\n\n### Долгие гласные:\n- /iː/ — s**ee**\n- /ɑː/ — c**ar**\n- /uː/ — bl**ue**\n\n### Дифтонги:\n- /aɪ/ — t**i**me\n- /eɪ/ — d**ay**\n- /ɔɪ/ — b**oy**\n\n### Сложные согласные:\n- /θ/ — **th**ink (язык между зубами, без голоса)\n- /ð/ — **th**is (язык между зубами, с голосом)\n- /ŋ/ — si**ng** (носовой звук)"},
                    {"type": "pronunciation", "word": "think", "phonetic": "/θɪŋk/", "acceptedForms": ["think", "Think"]},
                    {"type": "pronunciation", "word": "this", "phonetic": "/ðɪs/", "acceptedForms": ["this", "This", "these"]},
                    {"type": "flashcards", "cards": [{"front": "/θ/", "back": "th как в think — без голоса, язык между зубами"}, {"front": "/ð/", "back": "th как в this — с голосом, язык между зубами"}, {"front": "/iː/", "back": "Долгое «и» — see, tree, eat"}, {"front": "/æ/", "back": "Среднее между «а» и «э» — cat, bad, man"}, {"front": "/ŋ/", "back": "Носовой «н» — sing, ring, long"}]},
                    {"type": "quiz", "question": "Сколько звуков (phonemes) в английском языке?", "options": [{"id": "a", "text": "26", "correct": False}, {"id": "b", "text": "33", "correct": False}, {"id": "c", "text": "44", "correct": True}, {"id": "d", "text": "52", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "/θ/", "right": "think (глухой)"}, {"left": "/ð/", "right": "this (звонкий)"}, {"left": "/ŋ/", "right": "sing (носовой)"}, {"left": "/æ/", "right": "cat (открытый)"}]},
                ],
            },
        ],
    },
    # ===== SECTION 2: Basic Grammar =====
    {
        "title": "Базовая грамматика",
        "pos": 1,
        "lessons": [
            {
                "t": "Структура предложения SVO",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Subject — Verb — Object", "markdown": "## Порядок слов в английском\n\nАнглийский — язык **SVO** (Subject-Verb-Object):\n\n**Subject** (Кто?) + **Verb** (Что делает?) + **Object** (Кого/Что?)\n\n### Примеры:\n- **I** read **books**. (Я читаю книги)\n- **She** likes **coffee**. (Она любит кофе)\n- **They** play **football**. (Они играют в футбол)\n\n### Важно:\nВ русском порядок слов свободный: «Книги я читаю» = «Я читаю книги».\nВ английском порядок **фиксированный**: ~~Books I read~~ → **I read books**."},
                    {"type": "drag-order", "items": ["She", "likes", "coffee"]},
                    {"type": "drag-order", "items": ["They", "play", "football", "every day"]},
                    {"type": "drag-order", "items": ["My brother", "studies", "English", "at school"]},
                    {"type": "sentence-translation", "sentence": "Я читаю книги", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["I read books", "i read books"], "aiCheck": True},
                    {"type": "sentence-translation", "sentence": "Она любит кофе", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["She likes coffee", "she likes coffee"], "aiCheck": True},
                    {"type": "quiz", "question": "Какой порядок слов в английском предложении?", "options": [{"id": "a", "text": "Subject — Verb — Object", "correct": True}, {"id": "b", "text": "Verb — Subject — Object", "correct": False}, {"id": "c", "text": "Object — Verb — Subject", "correct": False}, {"id": "d", "text": "Свободный порядок", "correct": False}]},
                ],
            },
            {
                "t": "Present Simple",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Present Simple — настоящее простое", "markdown": "## Present Simple\n\nИспользуется для **привычных действий**, фактов и расписаний.\n\n### Образование:\n- **I / You / We / They** + глагол: *I work, They play*\n- **He / She / It** + глагол + **s/es**: *He works, She plays*\n\n### Отрицание:\n- I **don't** work. / He **doesn't** work.\n\n### Вопрос:\n- **Do** you work? / **Does** he work?\n\n### Слова-маркеры:\nalways, usually, often, sometimes, never, every day/week/month"},
                    {"type": "cloze-passage", "instruction": "Заполните пропуски правильной формой глагола", "segments": [{"type": "text", "value": "She "}, {"type": "blank", "answer": "likes", "options": ["like", "likes", "liked"]}, {"type": "text", "value": " coffee. They "}, {"type": "blank", "answer": "play", "options": ["play", "plays", "playing"]}, {"type": "text", "value": " football every day. He "}, {"type": "blank", "answer": "doesn't", "options": ["don't", "doesn't", "isn't"]}, {"type": "text", "value": " eat meat."}]},
                    {"type": "cloze-passage", "instruction": "Вставьте do или does", "segments": [{"type": "blank", "answer": "Do", "options": ["Do", "Does"]}, {"type": "text", "value": " you speak English? "}, {"type": "blank", "answer": "Does", "options": ["Do", "Does"]}, {"type": "text", "value": " she live in Moscow? "}, {"type": "blank", "answer": "Do", "options": ["Do", "Does"]}, {"type": "text", "value": " they work here?"}]},
                    {"type": "sentence-translation", "sentence": "Я работаю каждый день", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["I work every day", "i work every day"], "aiCheck": True},
                    {"type": "sentence-translation", "sentence": "Он не говорит по-русски", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["He doesn't speak Russian", "He does not speak Russian", "he doesn't speak russian"], "aiCheck": True},
                    {"type": "true-false", "statement": "В Present Simple с He/She/It к глаголу добавляется окончание -s/-es.", "correct": True},
                    {"type": "true-false", "statement": "В вопросах Present Simple вспомогательный глагол — is/are.", "correct": False},
                ],
            },
            {
                "t": "Present Continuous",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Present Continuous — действие прямо сейчас", "markdown": "## Present Continuous\n\nИспользуется для действий, которые происходят **прямо сейчас** или **временно**.\n\n### Образование:\n**am/is/are** + глагол + **-ing**\n\n- I **am reading** a book. (Я читаю книгу сейчас)\n- She **is working** now. (Она работает сейчас)\n- They **are playing** outside. (Они играют на улице)\n\n### Отрицание:\n- I **am not** (I'm not) working.\n- He **is not** (isn't) sleeping.\n\n### Вопрос:\n- **Are** you listening? / **Is** she coming?\n\n### Маркеры:\nnow, right now, at the moment, currently, Look! Listen!"},
                    {"type": "cloze-passage", "instruction": "Поставьте глагол в Present Continuous", "segments": [{"type": "text", "value": "Look! She "}, {"type": "blank", "answer": "is dancing"}, {"type": "text", "value": " (dance). They "}, {"type": "blank", "answer": "are watching"}, {"type": "text", "value": " (watch) TV right now. I "}, {"type": "blank", "answer": "am studying"}, {"type": "text", "value": " (study) English at the moment."}]},
                    {"type": "category-sort", "categories": ["Present Simple", "Present Continuous"], "items": [{"text": "every day", "category": "Present Simple"}, {"text": "right now", "category": "Present Continuous"}, {"text": "always", "category": "Present Simple"}, {"text": "at the moment", "category": "Present Continuous"}, {"text": "usually", "category": "Present Simple"}, {"text": "Look!", "category": "Present Continuous"}, {"text": "never", "category": "Present Simple"}, {"text": "currently", "category": "Present Continuous"}]},
                    {"type": "sentence-translation", "sentence": "Я сейчас читаю книгу", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["I am reading a book now", "I'm reading a book now", "I am reading a book", "I'm reading a book right now"], "aiCheck": True},
                    {"type": "quiz", "question": "Какое предложение в Present Continuous?", "options": [{"id": "a", "text": "She is cooking dinner now.", "correct": True}, {"id": "b", "text": "She cooks dinner every day.", "correct": False}, {"id": "c", "text": "She cooked dinner yesterday.", "correct": False}, {"id": "d", "text": "She will cook dinner.", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 3: Vocabulary =====
    {
        "title": "Лексика: Повседневные слова",
        "pos": 2,
        "lessons": [
            {
                "t": "Приветствия и знакомство",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Как здороваться по-английски", "markdown": "## Приветствия (Greetings)\n\n### Формальные:\n- **Good morning** — Доброе утро\n- **Good afternoon** — Добрый день\n- **Good evening** — Добрый вечер\n- **How do you do?** — Формальное приветствие\n\n### Неформальные:\n- **Hi / Hey** — Привет\n- **What's up?** — Как дела? (сленг)\n- **How's it going?** — Как дела?\n\n### Знакомство:\n- **What's your name?** — Как вас зовут?\n- **My name is...** / **I'm...** — Меня зовут...\n- **Nice to meet you!** — Приятно познакомиться!\n- **Where are you from?** — Откуда вы?"},
                    {"type": "word-builder", "hint": "Привет (неформально)", "word": "hello"},
                    {"type": "word-builder", "hint": "Доброе утро", "word": "morning"},
                    {"type": "pronunciation", "word": "Nice to meet you", "phonetic": "/naɪs tə miːt juː/", "acceptedForms": ["nice to meet you", "Nice to meet you"]},
                    {"type": "matching", "pairs": [{"left": "Good morning", "right": "Доброе утро"}, {"left": "What's your name?", "right": "Как вас зовут?"}, {"left": "Nice to meet you", "right": "Приятно познакомиться"}, {"left": "Where are you from?", "right": "Откуда вы?"}, {"left": "How's it going?", "right": "Как дела?"}]},
                    {"type": "conversation-sim", "scenario": "Вы встречаете нового коллегу в офисе.", "messages": [{"role": "assistant", "text": "Hi! I'm Sarah. What's your name?"}], "choices": [{"id": "a", "text": "Hi Sarah! I'm Alex. Nice to meet you!", "correct": True, "feedback": "Отлично! Вы представились и выразили радость от знакомства."}, {"id": "b", "text": "Good. You?", "correct": False, "feedback": "Слишком кратко. Sarah спросила ваше имя — нужно представиться."}, {"id": "c", "text": "I don't speak English.", "correct": False, "feedback": "Не уходите от общения! Попробуйте представиться."}]},
                    {"type": "sentence-translation", "sentence": "Приятно познакомиться!", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["Nice to meet you!", "Nice to meet you", "nice to meet you"], "aiCheck": True},
                ],
            },
            {
                "t": "Числа и время",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Числа от 1 до 100 и время", "markdown": "## Числа (Numbers)\n\n### 1-12:\none, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve\n\n### 13-19 (-teen):\nthirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen\n\n### Десятки (-ty):\ntwenty, thirty, forty, fifty, sixty, seventy, eighty, ninety\n\n### Составные:\ntwenty-one (21), thirty-five (35), ninety-nine (99)\n\n## Время (Time)\n\n- **What time is it?** — Который час?\n- **It's 3 o'clock** — 3 часа\n- **It's half past 3** — Половина четвёртого (3:30)\n- **It's quarter past 3** — Четверть четвёртого (3:15)\n- **It's quarter to 4** — Без четверти четыре (3:45)"},
                    {"type": "word-builder", "hint": "13 (тринадцать)", "word": "thirteen"},
                    {"type": "word-builder", "hint": "50 (пятьдесят)", "word": "fifty"},
                    {"type": "type-answer", "question": "Напишите число 15 по-английски", "acceptedAnswers": ["fifteen"]},
                    {"type": "type-answer", "question": "Напишите число 40 по-английски", "acceptedAnswers": ["forty"]},
                    {"type": "matching", "pairs": [{"left": "3:00", "right": "three o'clock"}, {"left": "3:30", "right": "half past three"}, {"left": "3:15", "right": "quarter past three"}, {"left": "3:45", "right": "quarter to four"}]},
                    {"type": "quiz", "question": "Как правильно пишется число 40?", "options": [{"id": "a", "text": "fourty", "correct": False}, {"id": "b", "text": "forty", "correct": True}, {"id": "c", "text": "fourthy", "correct": False}, {"id": "d", "text": "forthy", "correct": False}]},
                ],
            },
            {
                "t": "Еда и напитки",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Food & Drinks — Еда и напитки", "markdown": "## Еда (Food)\n\n### Фрукты (Fruits):\napple, banana, orange, grape, strawberry, lemon\n\n### Овощи (Vegetables):\ntomato, potato, carrot, onion, cucumber, pepper\n\n### Мясо (Meat):\nchicken, beef, pork, fish, lamb\n\n### Другое:\nbread, rice, pasta, cheese, egg, butter\n\n## Напитки (Drinks):\nwater, tea, coffee, juice, milk, soda\n\n## Полезные фразы:\n- **I'd like...** — Я бы хотел...\n- **Can I have...?** — Можно мне...?\n- **How much is...?** — Сколько стоит...?"},
                    {"type": "flashcards", "cards": [{"front": "apple", "back": "яблоко 🍎"}, {"front": "bread", "back": "хлеб 🍞"}, {"front": "chicken", "back": "курица 🍗"}, {"front": "coffee", "back": "кофе ☕"}, {"front": "tomato", "back": "помидор 🍅"}, {"front": "water", "back": "вода 💧"}]},
                    {"type": "word-builder", "hint": "клубника", "word": "strawberry"},
                    {"type": "category-sort", "categories": ["Fruits", "Vegetables", "Drinks"], "items": [{"text": "apple", "category": "Fruits"}, {"text": "tomato", "category": "Vegetables"}, {"text": "coffee", "category": "Drinks"}, {"text": "banana", "category": "Fruits"}, {"text": "carrot", "category": "Vegetables"}, {"text": "juice", "category": "Drinks"}, {"text": "orange", "category": "Fruits"}, {"text": "onion", "category": "Vegetables"}]},
                    {"type": "conversation-sim", "scenario": "Вы в кафе и хотите заказать еду.", "messages": [{"role": "assistant", "text": "Welcome! What can I get for you today?"}], "choices": [{"id": "a", "text": "I'd like a coffee and a sandwich, please.", "correct": True, "feedback": "Отлично! Вежливый и правильный заказ с 'I'd like' и 'please'."}, {"id": "b", "text": "Give me food.", "correct": False, "feedback": "Слишком грубо. Используйте 'I'd like...' или 'Can I have...' + please."}, {"id": "c", "text": "Coffee. Sandwich.", "correct": False, "feedback": "Нужно строить полные предложения: 'I'd like a coffee and a sandwich, please.'"}]},
                    {"type": "sentence-translation", "sentence": "Можно мне чашку чая, пожалуйста?", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["Can I have a cup of tea, please?", "Can I have a cup of tea please?", "Could I have a cup of tea, please?"], "aiCheck": True},
                ],
            },
        ],
    },
    # ===== SECTION 4: Listening & Speaking =====
    {
        "title": "Аудирование и говорение",
        "pos": 3,
        "lessons": [
            {
                "t": "Простые диалоги",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Учимся слушать и понимать", "markdown": "## Аудирование (Listening)\n\nАудирование — один из самых важных навыков. Советы:\n\n1. **Слушайте каждый день** — подкасты, YouTube, песни\n2. **Не пытайтесь понять каждое слово** — улавливайте общий смысл\n3. **Используйте субтитры** — сначала английские, потом без них\n4. **Повторяйте за спикером** (shadowing) — тренирует произношение\n\n### Полезные фразы для переспроса:\n- **Sorry, could you repeat that?** — Извините, повторите?\n- **What do you mean?** — Что вы имеете в виду?\n- **Could you speak slower, please?** — Можете говорить медленнее?"},
                    {"type": "listening-comprehension", "audioUrl": "https://upload.wikimedia.org/wikipedia/commons/2/22/En-us-hello.ogg", "transcript": "Hello! How are you doing today? I'm fine, thank you.", "questions": [{"question": "Какое приветствие вы услышали?", "options": [{"id": "a", "text": "Hello", "correct": True}, {"id": "b", "text": "Good morning", "correct": False}, {"id": "c", "text": "Hey", "correct": False}]}]},
                    {"type": "pronunciation", "word": "Could you repeat that?", "phonetic": "/kʊd juː rɪˈpiːt ðæt/", "acceptedForms": ["could you repeat that", "Could you repeat that", "could you repeat that?"]},
                    {"type": "pronunciation", "word": "How are you?", "phonetic": "/haʊ ɑːr juː/", "acceptedForms": ["how are you", "How are you", "how are you?"]},
                    {"type": "conversation-sim", "scenario": "Ваш собеседник говорит слишком быстро. Вы не поняли.", "messages": [{"role": "assistant", "text": "So basically the quarterly report shows that our KPIs exceeded expectations and the stakeholder alignment is progressing well with the new initiative."}], "choices": [{"id": "a", "text": "Sorry, could you speak a bit slower, please?", "correct": True, "feedback": "Отлично! Вежливая просьба говорить медленнее."}, {"id": "b", "text": "Yes, yes, I understand.", "correct": False, "feedback": "Не притворяйтесь что поняли! Лучше переспросить."}, {"id": "c", "text": "What?!", "correct": False, "feedback": "Слишком грубо. Используйте 'Sorry, could you repeat that?' или 'Could you speak slower?'"}]},
                    {"type": "matching", "pairs": [{"left": "Could you repeat that?", "right": "Повторите, пожалуйста"}, {"left": "What do you mean?", "right": "Что вы имеете в виду?"}, {"left": "Could you speak slower?", "right": "Говорите медленнее"}, {"left": "I didn't catch that.", "right": "Я не расслышал"}]},
                ],
            },
            {
                "t": "Произношение: Сложные звуки",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Звуки, которых нет в русском", "markdown": "## Трудные звуки для русскоговорящих\n\n### /θ/ и /ð/ — th\nСамые сложные! Язык между зубами.\n- **/θ/** (глухой): **th**ink, **th**ree, **th**ank\n- **/ð/** (звонкий): **th**is, **th**at, **th**e\n\n### /w/ — не «в»!\n- **w**ater, **w**ork, **w**hat\n- Губы трубочкой, как для «у», затем раскрываем\n\n### /r/ — не русская «р»!\n- **r**ed, **r**ight, **r**ead\n- Язык НЕ вибрирует, загнут назад\n\n### /ŋ/ — носовой звук\n- si**ng**, thi**ng**, lo**ng**\n- Звук идёт через нос, не через рот"},
                    {"type": "pronunciation", "word": "three", "phonetic": "/θriː/", "acceptedForms": ["three", "Three"]},
                    {"type": "pronunciation", "word": "water", "phonetic": "/ˈwɔːtər/", "acceptedForms": ["water", "Water"]},
                    {"type": "pronunciation", "word": "right", "phonetic": "/raɪt/", "acceptedForms": ["right", "Right", "write"]},
                    {"type": "pronunciation", "word": "sing", "phonetic": "/sɪŋ/", "acceptedForms": ["sing", "Sing"]},
                    {"type": "highlight-text", "instruction": "Выделите слова со звуком /θ/ (глухой th)", "segments": [{"text": "I ", "correct": False}, {"text": "think ", "correct": True}, {"text": "that ", "correct": False}, {"text": "three ", "correct": True}, {"text": "things ", "correct": True}, {"text": "are ", "correct": False}, {"text": "the ", "correct": False}, {"text": "best.", "correct": False}]},
                    {"type": "category-sort", "categories": ["/θ/ (глухой)", "/ð/ (звонкий)"], "items": [{"text": "think", "category": "/θ/ (глухой)"}, {"text": "this", "category": "/ð/ (звонкий)"}, {"text": "three", "category": "/θ/ (глухой)"}, {"text": "that", "category": "/ð/ (звонкий)"}, {"text": "thank", "category": "/θ/ (глухой)"}, {"text": "the", "category": "/ð/ (звонкий)"}]},
                ],
            },
        ],
    },
    # ===== SECTION 5: Business English =====
    {
        "title": "Деловой английский",
        "pos": 4,
        "lessons": [
            {
                "t": "Email: Деловая переписка",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Как писать деловые письма", "markdown": "## Деловые письма (Business Emails)\n\n### Структура:\n1. **Subject line** — тема письма\n2. **Greeting** — приветствие\n3. **Body** — основной текст\n4. **Closing** — завершение\n5. **Signature** — подпись\n\n### Приветствия:\n- **Dear Mr./Ms. Smith,** — формальное\n- **Hello John,** — полуформальное\n- **Hi team,** — неформальное\n\n### Полезные фразы:\n- **I'm writing to...** — Я пишу, чтобы...\n- **Please find attached...** — Во вложении...\n- **I look forward to hearing from you.** — Жду вашего ответа.\n- **Best regards,** / **Kind regards,** — С уважением,"},
                    {"type": "drag-order", "items": ["Dear Ms. Johnson,", "I'm writing to follow up on our meeting.", "Please find attached the report.", "I look forward to hearing from you.", "Best regards,", "Alex"]},
                    {"type": "cloze-passage", "instruction": "Заполните пропуски в деловом письме", "segments": [{"type": "text", "value": "Dear "}, {"type": "blank", "answer": "Mr.", "options": ["Mr.", "Hey", "Yo"]}, {"type": "text", "value": " Smith,\n\nI'm "}, {"type": "blank", "answer": "writing", "options": ["writing", "write", "wrote"]}, {"type": "text", "value": " to confirm our meeting on Monday. Please "}, {"type": "blank", "answer": "find", "options": ["find", "see", "look"]}, {"type": "text", "value": " attached the agenda.\n\nBest "}, {"type": "blank", "answer": "regards", "options": ["regards", "wishes", "luck"]}, {"type": "text", "value": ",\nAlex"}]},
                    {"type": "sentence-translation", "sentence": "Жду вашего ответа.", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["I look forward to hearing from you.", "I look forward to hearing from you", "Looking forward to hearing from you."], "aiCheck": True},
                    {"type": "matching", "pairs": [{"left": "Dear Mr./Ms.", "right": "Формальное приветствие"}, {"left": "I'm writing to...", "right": "Цель письма"}, {"left": "Please find attached", "right": "Вложение"}, {"left": "Best regards", "right": "Подпись"}]},
                    {"type": "true-false", "statement": "'Hey dude' — подходящее приветствие для делового письма.", "correct": False},
                ],
            },
            {
                "t": "Собеседование на английском",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Job Interview — Собеседование", "markdown": "## Собеседование на английском\n\n### Частые вопросы:\n1. **Tell me about yourself.** — Расскажите о себе.\n2. **What are your strengths?** — Ваши сильные стороны?\n3. **What are your weaknesses?** — Ваши слабые стороны?\n4. **Why do you want this job?** — Почему хотите эту работу?\n5. **Where do you see yourself in 5 years?** — Где видите себя через 5 лет?\n\n### Советы:\n- Используйте **STAR-метод**: Situation, Task, Action, Result\n- Не говорите «I don't know» — лучше «That's a great question, let me think...»\n- Подготовьте вопросы для интервьюера"},
                    {"type": "conversation-sim", "scenario": "Вы на собеседовании. Интервьюер задаёт первый вопрос.", "messages": [{"role": "assistant", "text": "So, tell me about yourself."}], "choices": [{"id": "a", "text": "I'm a software developer with 3 years of experience. I specialize in React and Node.js. I'm passionate about building user-friendly applications.", "correct": True, "feedback": "Отлично! Краткое, профессиональное представление с конкретикой."}, {"id": "b", "text": "Well, I was born in 1995, I like cats, and I enjoy cooking on weekends.", "correct": False, "feedback": "Слишком личное! На собеседовании нужно говорить о профессиональном опыте."}, {"id": "c", "text": "I need money.", "correct": False, "feedback": "Это не ответ на вопрос. Расскажите о своём опыте и навыках."}]},
                    {"type": "conversation-sim", "scenario": "Продолжение собеседования.", "messages": [{"role": "assistant", "text": "What would you say is your biggest weakness?"}], "choices": [{"id": "a", "text": "I sometimes focus too much on details, but I've been working on prioritizing tasks better and setting time limits.", "correct": True, "feedback": "Идеально! Вы назвали слабость и показали как работаете над ней."}, {"id": "b", "text": "I don't have any weaknesses.", "correct": False, "feedback": "Это звучит неискренне. Все люди имеют зоны роста."}, {"id": "c", "text": "I'm always late and I hate mornings.", "correct": False, "feedback": "Слишком честно! Выберите профессиональную слабость и покажите рост."}]},
                    {"type": "flashcards", "cards": [{"front": "Tell me about yourself", "back": "Расскажите о себе — кратко о профессиональном опыте"}, {"front": "STAR method", "back": "Situation → Task → Action → Result — метод структурирования ответов"}, {"front": "What are your strengths?", "back": "Назовите 2-3 сильные стороны с примерами"}, {"front": "Why should we hire you?", "back": "Покажите как ваши навыки решают проблемы компании"}]},
                    {"type": "sentence-translation", "sentence": "Я хочу работать в вашей компании, потому что мне нравится ваш продукт.", "sourceLanguage": "ru", "targetLanguage": "en", "acceptedAnswers": ["I want to work at your company because I like your product.", "I want to work in your company because I like your product."], "aiCheck": True},
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
            slug="english-from-zero-" + uuid.uuid4().hex[:6],
            description=COURSE_DESC,
            author_id=user.id,
            category="English",
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
