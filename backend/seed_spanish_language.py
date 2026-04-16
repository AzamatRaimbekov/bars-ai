"""Seed: Испанский язык — Начальный курс — 8 sections, ~40 lessons."""
import asyncio, uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90
T = "Испанский язык — Начальный курс"
DESC = "Начальный курс испанского языка: алфавит, произношение, базовая грамматика, повседневная лексика, путешествия и культура. 8 разделов, 40 уроков с интерактивными упражнениями."

S = [
  # ═══════════════════════════════════════════════════════════════════
  # SECTION 1: Алфавит и произношение
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Алфавит и произношение", "pos": 0, "lessons": [
    # ── Lesson 1.1: Испанский алфавит (5 steps, 15 XP) ──
    {"t": "Испанский алфавит", "xp": 15, "steps": [
      {"type":"info","title":"El alfabeto español","markdown":"## Испанский алфавит\n\nИспанский алфавит содержит **27 букв** — 26 стандартных латинских + особая буква **Ñ** (эне).\n\n### Гласные (vocales):\nA [а], E [э], I [и], O [о], U [у]\n\n### Особые буквы:\n- **Ñ** [нь] — señor, España\n- **LL** [й/ль] — llamar, calle\n- **CH** [ч] — chico, noche\n- **RR** [рр] — perro, carro (раскатистый)\n\n### Важно:\n- **H** всегда немая: hola [ола], hotel [отэль]\n- **J** читается как [х]: Juan, jardín\n- **Z** читается как [с] (в Латинской Америке): zapato [сапато]\n- **V** и **B** произносятся одинаково: [б]"},
      {"type":"quiz","question":"Сколько букв в испанском алфавите?","options":[{"id":"a","text":"27","correct":True},{"id":"b","text":"26","correct":False},{"id":"c","text":"33","correct":False},{"id":"d","text":"24","correct":False}]},
      {"type":"matching","pairs":[{"left":"Ñ","right":"[нь] — señor"},{"left":"H","right":"немая — hola"},{"left":"J","right":"[х] — Juan"},{"left":"LL","right":"[й/ль] — llamar"},{"left":"RR","right":"раскатистый [рр] — perro"}]},
      {"type":"true-false","statement":"Буква H в испанском языке всегда произносится.","correct":False},
      {"type":"flashcards","cards":[{"front":"A","back":"[а] — amigo (друг)"},{"front":"E","back":"[э] — escuela (школа)"},{"front":"I","back":"[и] — isla (остров)"},{"front":"O","back":"[о] — ojo (глаз)"},{"front":"U","back":"[у] — uva (виноград)"},{"front":"Ñ","back":"[нь] — España (Испания)"}]}
    ]},
    # ── Lesson 1.2: Гласные и дифтонги (4 steps, 15 XP) ──
    {"t": "Гласные и дифтонги", "xp": 15, "steps": [
      {"type":"info","title":"Vocales y diptongos","markdown":"## Гласные звуки\n\nВ испанском языке **5 чистых гласных** — они всегда произносятся одинаково:\n\n| Буква | Звук | Пример |\n|-------|------|--------|\n| A | [а] | casa (дом) |\n| E | [э] | mesa (стол) |\n| I | [и] | vida (жизнь) |\n| O | [о] | sol (солнце) |\n| U | [у] | luna (луна) |\n\n### Дифтонги (diptongos):\nСочетание двух гласных в одном слоге:\n- **ie** — bien [бьен], tiempo [тьемпо]\n- **ue** — bueno [буэно], puerta [пуэрта]\n- **ai/ay** — baile [байле]\n- **ei/ey** — rey [рэй]\n- **oi/oy** — hoy [ой]"},
      {"type":"quiz","question":"Сколько гласных звуков в испанском языке?","options":[{"id":"a","text":"5","correct":True},{"id":"b","text":"6","correct":False},{"id":"c","text":"10","correct":False},{"id":"d","text":"8","correct":False}]},
      {"type":"fill-blank","text":"Сочетание двух гласных в одном слоге называется ___","answers":["дифтонг","diptongo"]},
      {"type":"matching","pairs":[{"left":"ie","right":"bien, tiempo"},{"left":"ue","right":"bueno, puerta"},{"left":"ai/ay","right":"baile"},{"left":"oi/oy","right":"hoy"},{"left":"ei/ey","right":"rey"}]}
    ]},
    # ── Lesson 1.3: Согласные и их произношение (4 steps, 20 XP) ──
    {"t": "Согласные и их произношение", "xp": 20, "steps": [
      {"type":"info","title":"Las consonantes","markdown":"## Особенности согласных\n\n### Буквы с необычным произношением:\n\n| Буква | Перед a/o/u | Перед e/i |\n|-------|------------|----------|\n| **C** | [к] — casa | [с/θ] — cena |\n| **G** | [г] — gato | [х] — gente |\n| **Q** | всегда qu + e/i: que [кэ], quien [кьен] |\n\n### Другие правила:\n- **B** и **V** — оба [б]: vaca = baca\n- **D** между гласными — мягкий [д̞]: nada [нада]\n- **S** — всегда [с]: casa [каса]\n- **Z** — [с] в Латинской Америке, [θ] в Испании\n- **GU** перед e/i — [г]: guitarra, guerra\n- **GÜ** (с диэрезисом) — [гу]: pingüino"},
      {"type":"quiz","question":"Как произносится буква G перед E и I?","options":[{"id":"a","text":"[х] — как русское Х","correct":True},{"id":"b","text":"[г] — как русское Г","correct":False},{"id":"c","text":"[дж] — как в английском","correct":False},{"id":"d","text":"не произносится","correct":False}]},
      {"type":"multi-select","question":"Какие утверждения верны для испанского?","options":[{"id":"a","text":"B и V произносятся одинаково","correct":True},{"id":"b","text":"H всегда немая","correct":True},{"id":"c","text":"J читается как [дж]","correct":False},{"id":"d","text":"S всегда читается как [с]","correct":True},{"id":"e","text":"Z читается как [з]","correct":False}]},
      {"type":"flashcards","cards":[{"front":"C + a/o/u","back":"[к] — casa, como, cubo"},{"front":"C + e/i","back":"[с] или [θ] — cena, cine"},{"front":"G + a/o/u","back":"[г] — gato, gordo, gusto"},{"front":"G + e/i","back":"[х] — gente, girar"},{"front":"GU + e/i","back":"[г] — guerra, guitarra"},{"front":"GÜ + e/i","back":"[гу] — pingüino, vergüenza"}]}
    ]},
    # ── Lesson 1.4: Ударение и акценты (4 steps, 15 XP) ──
    {"t": "Ударение и акценты", "xp": 15, "steps": [
      {"type":"info","title":"El acento","markdown":"## Правила ударения\n\nВ испанском есть чёткие правила ударения:\n\n### 1. Слова на гласную, -n, -s:\nУдарение на **предпоследний** слог:\n- ca**sa**, ha**blan**, li**bros**\n\n### 2. Слова на согласную (кроме -n, -s):\nУдарение на **последний** слог:\n- ha**blar**, ciu**dad**, es**pa**ñol\n\n### 3. Исключения — с акцентом (tilde):\nЕсли ударение не по правилам, ставится **´**:\n- ca**fé**, te**lé**fono, mú**si**ca, á**rbol**\n\n### Типы слов:\n- **Agudas** — ударение на последний слог: café\n- **Llanas** — на предпоследний: casa\n- **Esdrújulas** — на третий с конца: teléfono (всегда с tilde)"},
      {"type":"quiz","question":"Где ударение в слове 'hablar'?","options":[{"id":"a","text":"На последнем слоге — habLAR","correct":True},{"id":"b","text":"На первом слоге — HAblar","correct":False},{"id":"c","text":"На предпоследнем — haBLAR","correct":False},{"id":"d","text":"Нет ударения","correct":False}]},
      {"type":"drag-order","items":["Посмотреть, на какую букву заканчивается слово","Если на гласную, -n, -s → ударение на предпоследний слог","Если на другую согласную → ударение на последний слог","Если есть tilde (´) → ударение там, где tilde"]},
      {"type":"type-answer","question":"Как называется знак ударения (´) в испанском?","acceptedAnswers":["tilde","тильда","тильде","acento"]}
    ]},
    # ── Lesson 1.5: Первые приветствия (5 steps, 20 XP) ──
    {"t": "Первые приветствия", "xp": 20, "steps": [
      {"type":"info","title":"Saludos y despedidas","markdown":"## Приветствия и прощания\n\n### Приветствия (saludos):\n| Испанский | Русский |\n|-----------|---------|\n| ¡Hola! | Привет! |\n| Buenos días | Доброе утро |\n| Buenas tardes | Добрый день |\n| Buenas noches | Добрый вечер / Спокойной ночи |\n| ¿Qué tal? | Как дела? |\n| ¿Cómo estás? | Как ты? |\n\n### Прощания (despedidas):\n| Испанский | Русский |\n|-----------|---------|\n| Adiós | До свидания |\n| Hasta luego | До встречи |\n| Hasta mañana | До завтра |\n| Nos vemos | Увидимся |\n| Chao | Пока |"},
      {"type":"flashcards","cards":[{"front":"¡Hola!","back":"Привет!"},{"front":"Buenos días","back":"Доброе утро"},{"front":"Buenas tardes","back":"Добрый день"},{"front":"Buenas noches","back":"Добрый вечер / Спокойной ночи"},{"front":"Adiós","back":"До свидания"},{"front":"Hasta luego","back":"До встречи"},{"front":"¿Qué tal?","back":"Как дела?"}]},
      {"type":"matching","pairs":[{"left":"¡Hola!","right":"Привет!"},{"left":"Adiós","right":"До свидания"},{"left":"Buenos días","right":"Доброе утро"},{"left":"Hasta mañana","right":"До завтра"},{"left":"¿Qué tal?","right":"Как дела?"}]},
      {"type":"fill-blank","text":"Чтобы сказать 'Добрый день' по-испански, мы говорим: Buenas ___","answers":["tardes"]},
      {"type":"quiz","question":"Как сказать 'До встречи' по-испански?","options":[{"id":"a","text":"Hasta luego","correct":True},{"id":"b","text":"Buenos días","correct":False},{"id":"c","text":"¿Qué tal?","correct":False},{"id":"d","text":"Buenas noches","correct":False}]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 2: Знакомство
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Знакомство", "pos": 1, "lessons": [
    # ── Lesson 2.1: Hola и Adiós — формы вежливости (4 steps, 15 XP) ──
    {"t": "Hola и Adiós — формы вежливости", "xp": 15, "steps": [
      {"type":"info","title":"Formal e informal","markdown":"## Формальное и неформальное обращение\n\n### Неформальное (tú):\n- ¡Hola! ¿Cómo **estás**? — Привет! Как ты?\n- ¿Qué tal? — Как дела?\n- ¡Chao! — Пока!\n\n### Формальное (usted):\n- Buenos días. ¿Cómo **está** usted? — Здравствуйте. Как вы?\n- Mucho gusto. — Очень приятно.\n- Hasta luego. — До свидания.\n\n### Ответы:\n- **Bien, gracias. ¿Y tú?** — Хорошо, спасибо. А ты?\n- **Muy bien.** — Очень хорошо.\n- **Regular.** — Так себе.\n- **Mal.** — Плохо."},
      {"type":"quiz","question":"Как вежливо спросить 'Как вы?' (формально)?","options":[{"id":"a","text":"¿Cómo está usted?","correct":True},{"id":"b","text":"¿Qué tal?","correct":False},{"id":"c","text":"¿Cómo estás?","correct":False},{"id":"d","text":"¡Hola!","correct":False}]},
      {"type":"matching","pairs":[{"left":"Bien, gracias","right":"Хорошо, спасибо"},{"left":"Muy bien","right":"Очень хорошо"},{"left":"Regular","right":"Так себе"},{"left":"Mal","right":"Плохо"},{"left":"Mucho gusto","right":"Очень приятно"}]},
      {"type":"true-false","statement":"'Tú' используется в формальном обращении.","correct":False}
    ]},
    # ── Lesson 2.2: ¿Cómo te llamas? (5 steps, 20 XP) ──
    {"t": "¿Cómo te llamas?", "xp": 20, "steps": [
      {"type":"info","title":"Presentarse","markdown":"## Как представиться\n\n### Спросить имя:\n- **¿Cómo te llamas?** — Как тебя зовут? (неформ.)\n- **¿Cómo se llama usted?** — Как вас зовут? (форм.)\n\n### Ответить:\n- **Me llamo...** — Меня зовут...\n- **Soy...** — Я...\n- **Mi nombre es...** — Моё имя...\n\n### Диалог-пример:\n— ¡Hola! ¿Cómo te llamas?\n— Me llamo María. ¿Y tú?\n— Soy Pedro. Mucho gusto.\n— Encantada.\n\n### Encantado/Encantada:\n- Мужчина говорит: **Encantado**\n- Женщина говорит: **Encantada**"},
      {"type":"fill-blank","text":"¿Cómo ___ llamas? — Me llamo Ana.","answers":["te"]},
      {"type":"quiz","question":"Как женщина скажет 'Очень приятно'?","options":[{"id":"a","text":"Encantada","correct":True},{"id":"b","text":"Encantado","correct":False},{"id":"c","text":"Mucho gusto","correct":False},{"id":"d","text":"Bien, gracias","correct":False}]},
      {"type":"drag-order","items":["¡Hola! ¿Cómo te llamas?","Me llamo María. ¿Y tú?","Soy Pedro. Mucho gusto.","Encantada."]},
      {"type":"type-answer","question":"Переведите: 'Меня зовут...' (начните с Me...)","acceptedAnswers":["Me llamo","Me llamo...","me llamo"]}
    ]},
    # ── Lesson 2.3: Числа 1-20 (4 steps, 15 XP) ──
    {"t": "Числа 1-20", "xp": 15, "steps": [
      {"type":"info","title":"Los números 1-20","markdown":"## Числа от 1 до 20\n\n| Число | Испанский | Число | Испанский |\n|-------|-----------|-------|-----------|\n| 1 | uno | 11 | once |\n| 2 | dos | 12 | doce |\n| 3 | tres | 13 | trece |\n| 4 | cuatro | 14 | catorce |\n| 5 | cinco | 15 | quince |\n| 6 | seis | 16 | dieciséis |\n| 7 | siete | 17 | diecisiete |\n| 8 | ocho | 18 | dieciocho |\n| 9 | nueve | 19 | diecinueve |\n| 10 | diez | 20 | veinte |\n\n### Запомните:\n- 11-15 — особые формы\n- 16-19 — dieci + единица (пишутся слитно)"},
      {"type":"flashcards","cards":[{"front":"1","back":"uno"},{"front":"5","back":"cinco"},{"front":"7","back":"siete"},{"front":"10","back":"diez"},{"front":"12","back":"doce"},{"front":"15","back":"quince"},{"front":"18","back":"dieciocho"},{"front":"20","back":"veinte"}]},
      {"type":"matching","pairs":[{"left":"3","right":"tres"},{"left":"8","right":"ocho"},{"left":"11","right":"once"},{"left":"14","right":"catorce"},{"left":"17","right":"diecisiete"}]},
      {"type":"type-answer","question":"Как будет число 9 по-испански?","acceptedAnswers":["nueve"]}
    ]},
    # ── Lesson 2.4: Национальности (4 steps, 20 XP) ──
    {"t": "Национальности", "xp": 20, "steps": [
      {"type":"info","title":"Las nacionalidades","markdown":"## Национальности\n\nВ испанском национальности изменяются по роду:\n\n| Страна | Мужской | Женский |\n|--------|---------|--------|\n| España | español | española |\n| Rusia | ruso | rusa |\n| Estados Unidos | estadounidense | estadounidense |\n| Francia | francés | francesa |\n| Alemania | alemán | alemana |\n| Italia | italiano | italiana |\n| China | chino | china |\n| Japón | japonés | japonesa |\n| México | mexicano | mexicana |\n| Brasil | brasileño | brasileña |\n\n### Правило:\n- Оканчиваются на **-o/-a**: ruso → rusa\n- Оканчиваются на **согласную**: + a для женского: español → española\n- Оканчиваются на **-e**: одна форма: estadounidense\n\n### Фраза:\n- **Soy ruso/rusa.** — Я русский/русская.\n- **¿De dónde eres?** — Откуда ты?"},
      {"type":"matching","pairs":[{"left":"España","right":"español / española"},{"left":"Rusia","right":"ruso / rusa"},{"left":"Francia","right":"francés / francesa"},{"left":"Japón","right":"japonés / japonesa"},{"left":"México","right":"mexicano / mexicana"}]},
      {"type":"fill-blank","text":"¿De dónde eres? — Soy ___ (русский, муж. род).","answers":["ruso"]},
      {"type":"multi-select","question":"Какие национальности имеют одну форму для обоих родов?","options":[{"id":"a","text":"estadounidense","correct":True},{"id":"b","text":"español","correct":False},{"id":"c","text":"canadiense","correct":True},{"id":"d","text":"italiano","correct":False}]}
    ]},
    # ── Lesson 2.5: Профессии (5 steps, 20 XP) ──
    {"t": "Профессии — Las profesiones", "xp": 20, "steps": [
      {"type":"info","title":"Las profesiones","markdown":"## Профессии\n\n| Испанский (м/ж) | Русский |\n|------------------|---------|\n| profesor / profesora | учитель |\n| médico / médica | врач |\n| estudiante | студент(ка) |\n| ingeniero / ingeniera | инженер |\n| abogado / abogada | адвокат |\n| enfermero / enfermera | медсестра/медбрат |\n| cocinero / cocinera | повар |\n| camarero / camarera | официант(ка) |\n| periodista | журналист(ка) |\n| programador / programadora | программист(ка) |\n\n### Фраза:\n- **Soy programador.** — Я программист.\n- **¿A qué te dedicas?** — Чем ты занимаешься?\n- **Trabajo de camarero.** — Я работаю официантом."},
      {"type":"flashcards","cards":[{"front":"profesor","back":"учитель (profesora — учительница)"},{"front":"médico","back":"врач (médica — ж.р.)"},{"front":"estudiante","back":"студент(ка) — одна форма для м. и ж. рода"},{"front":"programador","back":"программист (programadora — ж.р.)"},{"front":"cocinero","back":"повар (cocinera — ж.р.)"},{"front":"abogado","back":"адвокат (abogada — ж.р.)"}]},
      {"type":"quiz","question":"Как сказать 'Чем ты занимаешься?'","options":[{"id":"a","text":"¿A qué te dedicas?","correct":True},{"id":"b","text":"¿Cómo te llamas?","correct":False},{"id":"c","text":"¿De dónde eres?","correct":False},{"id":"d","text":"¿Qué tal?","correct":False}]},
      {"type":"matching","pairs":[{"left":"médico","right":"врач"},{"left":"enfermero","right":"медбрат"},{"left":"camarero","right":"официант"},{"left":"periodista","right":"журналист"},{"left":"ingeniero","right":"инженер"}]},
      {"type":"fill-blank","text":"Soy ___. (программист, муж. род)","answers":["programador"]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 3: Повседневная жизнь
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Повседневная жизнь", "pos": 2, "lessons": [
    # ── Lesson 3.1: Дни недели (4 steps, 15 XP) ──
    {"t": "Дни недели — Los días de la semana", "xp": 15, "steps": [
      {"type":"info","title":"Los días de la semana","markdown":"## Дни недели\n\n| Испанский | Русский |\n|-----------|---------|\n| lunes | понедельник |\n| martes | вторник |\n| miércoles | среда |\n| jueves | четверг |\n| viernes | пятница |\n| sábado | суббота |\n| domingo | воскресенье |\n\n### Правила:\n- Дни недели пишутся **с маленькой буквы**\n- Артикль **el** для одного дня: el lunes (в понедельник)\n- Артикль **los** для повторяющегося: los lunes (по понедельникам)\n- **El fin de semana** — выходные (суббота и воскресенье)"},
      {"type":"flashcards","cards":[{"front":"lunes","back":"понедельник"},{"front":"martes","back":"вторник"},{"front":"miércoles","back":"среда"},{"front":"jueves","back":"четверг"},{"front":"viernes","back":"пятница"},{"front":"sábado","back":"суббота"},{"front":"domingo","back":"воскресенье"}]},
      {"type":"drag-order","items":["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]},
      {"type":"quiz","question":"Как сказать 'по понедельникам' (повторяющееся)?","options":[{"id":"a","text":"los lunes","correct":True},{"id":"b","text":"el lunes","correct":False},{"id":"c","text":"un lunes","correct":False},{"id":"d","text":"lunes","correct":False}]}
    ]},
    # ── Lesson 3.2: Месяцы и времена года (4 steps, 15 XP) ──
    {"t": "Месяцы и времена года", "xp": 15, "steps": [
      {"type":"info","title":"Meses y estaciones","markdown":"## Месяцы (los meses)\n\n| Испанский | Русский |\n|-----------|---------|\n| enero | январь |\n| febrero | февраль |\n| marzo | март |\n| abril | апрель |\n| mayo | май |\n| junio | июнь |\n| julio | июль |\n| agosto | август |\n| septiembre | сентябрь |\n| octubre | октябрь |\n| noviembre | ноябрь |\n| diciembre | декабрь |\n\n## Времена года (las estaciones):\n- **la primavera** — весна\n- **el verano** — лето\n- **el otoño** — осень\n- **el invierno** — зима\n\n### Фраза:\n- **Mi cumpleaños es en mayo.** — Мой день рождения в мае."},
      {"type":"matching","pairs":[{"left":"la primavera","right":"весна"},{"left":"el verano","right":"лето"},{"left":"el otoño","right":"осень"},{"left":"el invierno","right":"зима"}]},
      {"type":"fill-blank","text":"Mi cumpleaños es en ___ (январь).","answers":["enero"]},
      {"type":"multi-select","question":"Какие месяцы относятся к лету в Испании?","options":[{"id":"a","text":"junio","correct":True},{"id":"b","text":"julio","correct":True},{"id":"c","text":"agosto","correct":True},{"id":"d","text":"diciembre","correct":False},{"id":"e","text":"febrero","correct":False}]}
    ]},
    # ── Lesson 3.3: Время — ¿Qué hora es? (5 steps, 20 XP) ──
    {"t": "Время — ¿Qué hora es?", "xp": 20, "steps": [
      {"type":"info","title":"La hora","markdown":"## Который час?\n\n### Спросить время:\n- **¿Qué hora es?** — Который час?\n\n### Ответить:\n- **Es la una.** — Час (1:00) — единственное число!\n- **Son las dos.** — Два часа (2:00)\n- **Son las tres y media.** — 3:30\n- **Son las cuatro y cuarto.** — 4:15\n- **Son las cinco menos cuarto.** — 4:45\n- **Son las seis y diez.** — 6:10\n- **Son las siete menos veinte.** — 6:40\n\n### Части дня:\n- **de la mañana** — утра\n- **de la tarde** — дня\n- **de la noche** — вечера/ночи\n- **Es mediodía.** — Полдень.\n- **Es medianoche.** — Полночь."},
      {"type":"quiz","question":"Как сказать 3:30?","options":[{"id":"a","text":"Son las tres y media","correct":True},{"id":"b","text":"Son las tres y cuarto","correct":False},{"id":"c","text":"Es la tres y media","correct":False},{"id":"d","text":"Son las tres menos media","correct":False}]},
      {"type":"matching","pairs":[{"left":"1:00","right":"Es la una"},{"left":"2:15","right":"Son las dos y cuarto"},{"left":"3:30","right":"Son las tres y media"},{"left":"4:45","right":"Son las cinco menos cuarto"},{"left":"12:00","right":"Es mediodía"}]},
      {"type":"true-false","statement":"Для 1:00 мы говорим 'Son la una'.","correct":False},
      {"type":"type-answer","question":"Как спросить 'Который час?' по-испански?","acceptedAnswers":["¿Qué hora es?","Qué hora es","que hora es"]}
    ]},
    # ── Lesson 3.4: Моя семья — Mi familia (4 steps, 20 XP) ──
    {"t": "Моя семья — Mi familia", "xp": 20, "steps": [
      {"type":"info","title":"La familia","markdown":"## Семья\n\n| Испанский | Русский |\n|-----------|---------|\n| el padre / la madre | отец / мать |\n| los padres | родители |\n| el hijo / la hija | сын / дочь |\n| el hermano / la hermana | брат / сестра |\n| el abuelo / la abuela | дедушка / бабушка |\n| el tío / la tía | дядя / тётя |\n| el primo / la prima | двоюродный брат / сестра |\n| el esposo / la esposa | муж / жена |\n| el novio / la novia | жених (парень) / невеста (девушка) |\n\n### Притяжательные:\n- **mi** — мой/моя: mi padre\n- **tu** — твой/твоя: tu hermana\n- **su** — его/её/ваш: su hijo\n\n### Пример:\n**Mi familia es grande. Tengo dos hermanos y una hermana.**\n(Моя семья большая. У меня два брата и одна сестра.)"},
      {"type":"flashcards","cards":[{"front":"el padre","back":"отец"},{"front":"la madre","back":"мать"},{"front":"el hermano","back":"брат"},{"front":"la hermana","back":"сестра"},{"front":"el abuelo","back":"дедушка"},{"front":"la abuela","back":"бабушка"},{"front":"el hijo","back":"сын"},{"front":"la hija","back":"дочь"}]},
      {"type":"matching","pairs":[{"left":"mi padre","right":"мой отец"},{"left":"tu hermana","right":"твоя сестра"},{"left":"su hijo","right":"его/её сын"},{"left":"los abuelos","right":"дедушка и бабушка"},{"left":"los padres","right":"родители"}]},
      {"type":"fill-blank","text":"___ familia es grande. (Моя)","answers":["Mi","mi"]}
    ]},
    # ── Lesson 3.5: Мой дом — Mi casa (4 steps, 15 XP) ──
    {"t": "Мой дом — Mi casa", "xp": 15, "steps": [
      {"type":"info","title":"Mi casa","markdown":"## Дом и комнаты\n\n| Испанский | Русский |\n|-----------|---------|\n| la casa | дом |\n| el piso / el apartamento | квартира |\n| la cocina | кухня |\n| el salón / la sala | гостиная |\n| el dormitorio / la habitación | спальня |\n| el baño | ванная |\n| el jardín | сад |\n| el balcón | балкон |\n| la ventana | окно |\n| la puerta | дверь |\n| la mesa | стол |\n| la silla | стул |\n| la cama | кровать |\n\n### Описание:\n- **Mi casa es pequeña pero bonita.**\n  (Мой дом маленький, но красивый.)\n- **Hay tres habitaciones.**\n  (Есть три комнаты.) — hay = есть/имеется"},
      {"type":"flashcards","cards":[{"front":"la cocina","back":"кухня"},{"front":"el salón","back":"гостиная"},{"front":"el dormitorio","back":"спальня"},{"front":"el baño","back":"ванная"},{"front":"la ventana","back":"окно"},{"front":"la puerta","back":"дверь"}]},
      {"type":"matching","pairs":[{"left":"la cocina","right":"кухня"},{"left":"el baño","right":"ванная"},{"left":"la cama","right":"кровать"},{"left":"la mesa","right":"стол"},{"left":"la silla","right":"стул"}]},
      {"type":"quiz","question":"Что означает 'Hay tres habitaciones'?","options":[{"id":"a","text":"Есть три комнаты","correct":True},{"id":"b","text":"У меня три дома","correct":False},{"id":"c","text":"Три комнаты большие","correct":False},{"id":"d","text":"Я хочу три комнаты","correct":False}]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 4: В городе
  # ═══════════════════════════════════════════════════════════════════
  {"title": "В городе", "pos": 3, "lessons": [
    # ── Lesson 4.1: Транспорт (4 steps, 15 XP) ──
    {"t": "Транспорт — El transporte", "xp": 15, "steps": [
      {"type":"info","title":"El transporte","markdown":"## Транспорт\n\n| Испанский | Русский |\n|-----------|---------|\n| el autobús | автобус |\n| el metro | метро |\n| el tren | поезд |\n| el taxi | такси |\n| el avión | самолёт |\n| el coche / el carro | машина |\n| la bicicleta / la bici | велосипед |\n| a pie | пешком |\n\n### Фразы:\n- **Voy en autobús.** — Я еду на автобусе.\n- **Voy en metro.** — Я еду на метро.\n- **Voy a pie.** — Я иду пешком.\n- **¿Dónde está la parada?** — Где остановка?\n- **¿Cuánto cuesta el billete?** — Сколько стоит билет?"},
      {"type":"flashcards","cards":[{"front":"el autobús","back":"автобус"},{"front":"el metro","back":"метро"},{"front":"el tren","back":"поезд"},{"front":"el avión","back":"самолёт"},{"front":"la bicicleta","back":"велосипед"},{"front":"a pie","back":"пешком"}]},
      {"type":"quiz","question":"Как сказать 'Я иду пешком'?","options":[{"id":"a","text":"Voy a pie","correct":True},{"id":"b","text":"Voy en pie","correct":False},{"id":"c","text":"Voy con pie","correct":False},{"id":"d","text":"Voy de pie","correct":False}]},
      {"type":"fill-blank","text":"¿Dónde está la ___? (остановка)","answers":["parada"]}
    ]},
    # ── Lesson 4.2: Направления (5 steps, 20 XP) ──
    {"t": "Направления — Las direcciones", "xp": 20, "steps": [
      {"type":"info","title":"Las direcciones","markdown":"## Как спросить дорогу\n\n### Спросить:\n- **¿Dónde está...?** — Где находится...?\n- **¿Cómo llego a...?** — Как мне добраться до...?\n- **¿Está lejos/cerca?** — Это далеко/близко?\n\n### Направления:\n| Испанский | Русский |\n|-----------|---------|\n| a la derecha | направо |\n| a la izquierda | налево |\n| todo recto / derecho | прямо |\n| la primera calle | первая улица |\n| la segunda calle | вторая улица |\n| en la esquina | на углу |\n| al lado de | рядом с |\n| enfrente de | напротив |\n| entre | между |\n\n### Пример:\n**Sigue todo recto, gira a la derecha en la segunda calle.**\n(Идите прямо, поверните направо на второй улице.)"},
      {"type":"matching","pairs":[{"left":"a la derecha","right":"направо"},{"left":"a la izquierda","right":"налево"},{"left":"todo recto","right":"прямо"},{"left":"en la esquina","right":"на углу"},{"left":"enfrente de","right":"напротив"}]},
      {"type":"drag-order","items":["Sigue todo recto","Gira a la izquierda","Pasa la primera calle","El banco está a la derecha"]},
      {"type":"fill-blank","text":"Gira a la ___ (направо).","answers":["derecha"]},
      {"type":"quiz","question":"Как спросить 'Где находится банк?'","options":[{"id":"a","text":"¿Dónde está el banco?","correct":True},{"id":"b","text":"¿Cuánto cuesta el banco?","correct":False},{"id":"c","text":"¿Qué hora es el banco?","correct":False},{"id":"d","text":"¿Cómo te llamas banco?","correct":False}]}
    ]},
    # ── Lesson 4.3: В магазине (4 steps, 20 XP) ──
    {"t": "В магазине — En la tienda", "xp": 20, "steps": [
      {"type":"info","title":"En la tienda","markdown":"## В магазине\n\n### Полезные фразы:\n| Испанский | Русский |\n|-----------|---------|\n| ¿Cuánto cuesta? | Сколько стоит? |\n| ¿Cuánto es? | Сколько всего? |\n| ¿Tiene...? | У вас есть...? |\n| Quiero... | Я хочу... |\n| Me gustaría... | Мне бы хотелось... |\n| ¿Algo más? | Что-нибудь ещё? |\n| Nada más, gracias. | Больше ничего, спасибо. |\n| Es muy caro. | Это очень дорого. |\n| ¿Tiene algo más barato? | Есть что-нибудь подешевле? |\n| Me lo llevo. | Я это беру. |\n\n### Диалог:\n— Buenos días. ¿Qué desea?\n— Quiero una camiseta, por favor.\n— ¿De qué talla?\n— Talla M. ¿Cuánto cuesta?\n— Veinte euros.\n— Me la llevo."},
      {"type":"flashcards","cards":[{"front":"¿Cuánto cuesta?","back":"Сколько стоит?"},{"front":"¿Tiene...?","back":"У вас есть...?"},{"front":"Me lo llevo","back":"Я это беру"},{"front":"Es muy caro","back":"Это очень дорого"},{"front":"Nada más, gracias","back":"Больше ничего, спасибо"}]},
      {"type":"quiz","question":"Как вежливо сказать 'Мне бы хотелось...'?","options":[{"id":"a","text":"Me gustaría...","correct":True},{"id":"b","text":"Quiero...","correct":False},{"id":"c","text":"Dame...","correct":False},{"id":"d","text":"Tengo...","correct":False}]},
      {"type":"type-answer","question":"Как спросить 'Сколько стоит?' по-испански?","acceptedAnswers":["¿Cuánto cuesta?","Cuánto cuesta","cuanto cuesta"]}
    ]},
    # ── Lesson 4.4: В ресторане (5 steps, 25 XP) ──
    {"t": "В ресторане — En el restaurante", "xp": 25, "steps": [
      {"type":"info","title":"En el restaurante","markdown":"## В ресторане\n\n### Полезные фразы:\n| Испанский | Русский |\n|-----------|---------|\n| Una mesa para dos, por favor. | Столик на двоих. |\n| La carta / el menú, por favor. | Меню, пожалуйста. |\n| ¿Qué me recomienda? | Что посоветуете? |\n| De primer plato... | На первое... |\n| De segundo plato... | На второе... |\n| De postre... | На десерт... |\n| La cuenta, por favor. | Счёт, пожалуйста. |\n| ¿Está incluida la propina? | Чаевые включены? |\n\n### Заказ напитков:\n- **Un vaso de agua** — стакан воды\n- **Una copa de vino** — бокал вина\n- **Una cerveza** — пиво\n- **Un café con leche** — кофе с молоком"},
      {"type":"matching","pairs":[{"left":"La carta, por favor","right":"Меню, пожалуйста"},{"left":"La cuenta, por favor","right":"Счёт, пожалуйста"},{"left":"De primer plato","right":"На первое"},{"left":"De postre","right":"На десерт"},{"left":"¿Qué me recomienda?","right":"Что посоветуете?"}]},
      {"type":"drag-order","items":["Una mesa para dos, por favor.","La carta, por favor.","De primer plato, una ensalada.","De segundo, paella.","La cuenta, por favor."]},
      {"type":"fill-blank","text":"La ___, por favor. (Счёт)","answers":["cuenta"]},
      {"type":"true-false","statement":"'La carta' и 'el menú' оба означают 'меню'.","correct":True}
    ]},
    # ── Lesson 4.5: Числа 20-100 (4 steps, 15 XP) ──
    {"t": "Числа 20-100", "xp": 15, "steps": [
      {"type":"info","title":"Los números 20-100","markdown":"## Числа от 20 до 100\n\n### Десятки:\n| Число | Испанский |\n|-------|-----------|\n| 20 | veinte |\n| 30 | treinta |\n| 40 | cuarenta |\n| 50 | cincuenta |\n| 60 | sesenta |\n| 70 | setenta |\n| 80 | ochenta |\n| 90 | noventa |\n| 100 | cien |\n\n### Составные числа:\n- 21-29 — пишутся слитно: **veintiuno, veintidós, veintitrés...**\n- 31-99 — через **y**: **treinta y uno, cuarenta y dos...**\n\n### Примеры:\n- 25 — **veinticinco**\n- 37 — **treinta y siete**\n- 54 — **cincuenta y cuatro**\n- 100 — **cien** (но: 101 — **ciento uno**)"},
      {"type":"matching","pairs":[{"left":"30","right":"treinta"},{"left":"50","right":"cincuenta"},{"left":"70","right":"setenta"},{"left":"90","right":"noventa"},{"left":"100","right":"cien"}]},
      {"type":"quiz","question":"Как пишется число 25 по-испански?","options":[{"id":"a","text":"veinticinco (слитно)","correct":True},{"id":"b","text":"veinte y cinco (раздельно)","correct":False},{"id":"c","text":"venti cinco","correct":False},{"id":"d","text":"veintcinco","correct":False}]},
      {"type":"type-answer","question":"Напишите число 43 по-испански.","acceptedAnswers":["cuarenta y tres"]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 5: Глаголы — настоящее время
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Глаголы — настоящее время", "pos": 4, "lessons": [
    # ── Lesson 5.1: Ser и Estar (5 steps, 25 XP) ──
    {"t": "Ser и Estar — два глагола 'быть'", "xp": 25, "steps": [
      {"type":"info","title":"Ser y Estar","markdown":"## Два глагола 'быть'\n\nВ испанском два глагола 'быть' — **ser** и **estar**.\n\n### SER — постоянные качества:\n| Лицо | Форма |\n|------|-------|\n| yo | soy |\n| tú | eres |\n| él/ella/usted | es |\n| nosotros | somos |\n| ellos/ustedes | son |\n\nИспользуется для: имя, национальность, профессия, характер, материал, время.\n- **Soy Pedro.** / **Soy español.** / **Es profesor.**\n\n### ESTAR — состояния и местоположение:\n| Лицо | Форма |\n|------|-------|\n| yo | estoy |\n| tú | estás |\n| él/ella/usted | está |\n| nosotros | estamos |\n| ellos/ustedes | están |\n\nИспользуется для: местоположение, настроение, состояние.\n- **Estoy bien.** / **Madrid está en España.** / **Estoy cansado.**"},
      {"type":"quiz","question":"Какой глагол используется для национальности?","options":[{"id":"a","text":"Ser — Soy español","correct":True},{"id":"b","text":"Estar — Estoy español","correct":False},{"id":"c","text":"Оба варианта верны","correct":False},{"id":"d","text":"Ни один","correct":False}]},
      {"type":"matching","pairs":[{"left":"Soy profesor","right":"Я учитель (профессия — ser)"},{"left":"Estoy cansado","right":"Я устал (состояние — estar)"},{"left":"Madrid es grande","right":"Мадрид большой (качество — ser)"},{"left":"Estoy en casa","right":"Я дома (место — estar)"},{"left":"Son las tres","right":"Три часа (время — ser)"}]},
      {"type":"fill-blank","text":"¿Cómo ___ (tú)? — Estoy bien, gracias.","answers":["estás"]},
      {"type":"multi-select","question":"Когда используется SER?","options":[{"id":"a","text":"Национальность","correct":True},{"id":"b","text":"Профессия","correct":True},{"id":"c","text":"Местоположение","correct":False},{"id":"d","text":"Время","correct":True},{"id":"e","text":"Настроение","correct":False}]}
    ]},
    # ── Lesson 5.2: Глаголы -ar, -er, -ir (5 steps, 25 XP) ──
    {"t": "Глаголы -ar, -er, -ir", "xp": 25, "steps": [
      {"type":"info","title":"Verbos regulares","markdown":"## Правильные глаголы\n\nВсе испанские глаголы делятся на три группы по окончанию инфинитива:\n\n### -AR (hablar — говорить):\n| Лицо | Окончание | Пример |\n|------|-----------|--------|\n| yo | -o | hablo |\n| tú | -as | hablas |\n| él/ella | -a | habla |\n| nosotros | -amos | hablamos |\n| ellos | -an | hablan |\n\n### -ER (comer — есть):\n| yo | -o | como |\n| tú | -es | comes |\n| él/ella | -e | come |\n| nosotros | -emos | comemos |\n| ellos | -en | comen |\n\n### -IR (vivir — жить):\n| yo | -o | vivo |\n| tú | -es | vives |\n| él/ella | -e | vive |\n| nosotros | -imos | vivimos |\n| ellos | -en | viven |\n\n### Популярные глаголы:\n- **trabajar** (работать), **estudiar** (учиться), **comprar** (покупать)\n- **leer** (читать), **beber** (пить), **aprender** (учить)\n- **escribir** (писать), **abrir** (открывать)"},
      {"type":"flashcards","cards":[{"front":"hablar","back":"говорить: hablo, hablas, habla, hablamos, hablan"},{"front":"comer","back":"есть: como, comes, come, comemos, comen"},{"front":"vivir","back":"жить: vivo, vives, vive, vivimos, viven"},{"front":"trabajar","back":"работать: trabajo, trabajas, trabaja, trabajamos, trabajan"},{"front":"estudiar","back":"учиться: estudio, estudias, estudia, estudiamos, estudian"}]},
      {"type":"fill-blank","text":"Yo ___ español. (hablar — yo)","answers":["hablo"]},
      {"type":"matching","pairs":[{"left":"yo (hablar)","right":"hablo"},{"left":"tú (comer)","right":"comes"},{"left":"él (vivir)","right":"vive"},{"left":"nosotros (trabajar)","right":"trabajamos"},{"left":"ellos (beber)","right":"beben"}]},
      {"type":"quiz","question":"Как спрягается 'vivir' для 'nosotros'?","options":[{"id":"a","text":"vivimos","correct":True},{"id":"b","text":"vivemos","correct":False},{"id":"c","text":"vivamos","correct":False},{"id":"d","text":"viven","correct":False}]}
    ]},
    # ── Lesson 5.3: Неправильные глаголы (4 steps, 25 XP) ──
    {"t": "Неправильные глаголы — Verbos irregulares", "xp": 25, "steps": [
      {"type":"info","title":"Verbos irregulares","markdown":"## Неправильные глаголы\n\n### Самые важные:\n\n**IR (идти/ехать):**\nvoy, vas, va, vamos, van\n- **Voy al cine.** — Я иду в кино.\n\n**HACER (делать):**\nhago, haces, hace, hacemos, hacen\n- **¿Qué haces?** — Что ты делаешь?\n\n**PODER (мочь):**\npuedo, puedes, puede, podemos, pueden\n- **¿Puedo entrar?** — Можно войти?\n\n**QUERER (хотеть):**\nquiero, quieres, quiere, queremos, quieren\n- **Quiero agua.** — Я хочу воды.\n\n**SABER (знать):**\nsé, sabes, sabe, sabemos, saben\n\n**DECIR (говорить/сказать):**\ndigo, dices, dice, decimos, dicen\n\n**VENIR (приходить):**\nvengo, vienes, viene, venimos, vienen"},
      {"type":"matching","pairs":[{"left":"ir (yo)","right":"voy"},{"left":"hacer (tú)","right":"haces"},{"left":"poder (yo)","right":"puedo"},{"left":"querer (él)","right":"quiere"},{"left":"saber (yo)","right":"sé"}]},
      {"type":"fill-blank","text":"¿___ entrar? (Можно войти? — poder, yo)","answers":["Puedo","puedo"]},
      {"type":"quiz","question":"Как сказать 'Я иду в кино'?","options":[{"id":"a","text":"Voy al cine","correct":True},{"id":"b","text":"Ir al cine","correct":False},{"id":"c","text":"Va al cine","correct":False},{"id":"d","text":"Vamos al cine","correct":False}]}
    ]},
    # ── Lesson 5.4: Gustar — нравиться (4 steps, 20 XP) ──
    {"t": "Gustar — нравиться", "xp": 20, "steps": [
      {"type":"info","title":"El verbo gustar","markdown":"## Глагол gustar\n\nGustar работает не так, как в русском! Буквально: 'мне нравится' = 'оно мне приятно'.\n\n### Структура:\n**Кому + gusta/gustan + что**\n\n| Кому | Испанский |\n|------|-----------|\n| мне | me gusta(n) |\n| тебе | te gusta(n) |\n| ему/ей | le gusta(n) |\n| нам | nos gusta(n) |\n| им/вам | les gusta(n) |\n\n### Правило:\n- **gusta** + инфинитив или ед. число: Me gusta el café. / Me gusta bailar.\n- **gustan** + мн. число: Me gustan los gatos.\n\n### Примеры:\n- **Me gusta la música.** — Мне нравится музыка.\n- **No me gustan las arañas.** — Мне не нравятся пауки.\n- **¿Te gusta cocinar?** — Тебе нравится готовить?\n- **A María le gusta leer.** — Марии нравится читать."},
      {"type":"quiz","question":"Как сказать 'Мне нравятся кошки'?","options":[{"id":"a","text":"Me gustan los gatos","correct":True},{"id":"b","text":"Me gusta los gatos","correct":False},{"id":"c","text":"Yo gusto los gatos","correct":False},{"id":"d","text":"Mi gusta los gatos","correct":False}]},
      {"type":"fill-blank","text":"¿Te ___ bailar? (нравится)","answers":["gusta"]},
      {"type":"true-false","statement":"'Me gustan el café' — правильное предложение.","correct":False}
    ]},
    # ── Lesson 5.5: Tener — иметь (5 steps, 20 XP) ──
    {"t": "Tener — иметь и выражения", "xp": 20, "steps": [
      {"type":"info","title":"El verbo tener","markdown":"## Глагол tener (иметь)\n\n### Спряжение:\n| Лицо | Форма |\n|------|-------|\n| yo | tengo |\n| tú | tienes |\n| él/ella | tiene |\n| nosotros | tenemos |\n| ellos | tienen |\n\n### Базовое значение:\n- **Tengo un hermano.** — У меня есть брат.\n- **¿Tienes hambre?** — Ты голоден?\n\n### Выражения с tener:\n| Испанский | Русский |\n|-----------|---------|\n| tener hambre | быть голодным (иметь голод) |\n| tener sed | хотеть пить |\n| tener frío | мёрзнуть |\n| tener calor | быть жарко |\n| tener sueño | хотеть спать |\n| tener miedo | бояться |\n| tener prisa | спешить |\n| tener razón | быть правым |\n| tener ... años | быть ... лет |\n\n### Пример:\n**Tengo 25 años y tengo mucha hambre.**\n(Мне 25 лет и я очень голоден.)"},
      {"type":"flashcards","cards":[{"front":"tener hambre","back":"быть голодным — Tengo hambre (Я голоден)"},{"front":"tener sed","back":"хотеть пить — Tengo sed (Я хочу пить)"},{"front":"tener frío","back":"мёрзнуть — Tengo frío (Мне холодно)"},{"front":"tener sueño","back":"хотеть спать — Tengo sueño (Я хочу спать)"},{"front":"tener miedo","back":"бояться — Tengo miedo (Мне страшно)"},{"front":"tener ... años","back":"быть ... лет — Tengo 20 años (Мне 20 лет)"}]},
      {"type":"matching","pairs":[{"left":"tener hambre","right":"быть голодным"},{"left":"tener sed","right":"хотеть пить"},{"left":"tener razón","right":"быть правым"},{"left":"tener prisa","right":"спешить"},{"left":"tener miedo","right":"бояться"}]},
      {"type":"fill-blank","text":"___ 25 años. (Мне 25 лет — yo)","answers":["Tengo","tengo"]},
      {"type":"quiz","question":"Как сказать 'Мне холодно' по-испански?","options":[{"id":"a","text":"Tengo frío","correct":True},{"id":"b","text":"Soy frío","correct":False},{"id":"c","text":"Estoy frío","correct":False},{"id":"d","text":"Hace frío","correct":False}]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 6: Еда и покупки
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Еда и покупки", "pos": 5, "lessons": [
    # ── Lesson 6.1: Продукты питания (4 steps, 15 XP) ──
    {"t": "Продукты питания — La comida", "xp": 15, "steps": [
      {"type":"info","title":"La comida","markdown":"## Продукты питания\n\n### Фрукты (las frutas):\nmanzana (яблоко), naranja (апельсин), plátano (банан), fresa (клубника), uva (виноград)\n\n### Овощи (las verduras):\ntomate (помидор), patata (картошка), cebolla (лук), lechuga (салат), zanahoria (морковь)\n\n### Мясо и рыба:\npollo (курица), carne (мясо), pescado (рыба), jamón (ветчина), cerdo (свинина)\n\n### Другое:\npan (хлеб), arroz (рис), leche (молоко), huevo (яйцо), queso (сыр), aceite (масло)\n\n### Приёмы пищи:\n- **el desayuno** — завтрак\n- **la comida / el almuerzo** — обед\n- **la cena** — ужин"},
      {"type":"flashcards","cards":[{"front":"la manzana","back":"яблоко"},{"front":"el pollo","back":"курица"},{"front":"el pan","back":"хлеб"},{"front":"la leche","back":"молоко"},{"front":"el huevo","back":"яйцо"},{"front":"el queso","back":"сыр"},{"front":"el pescado","back":"рыба"},{"front":"el arroz","back":"рис"}]},
      {"type":"matching","pairs":[{"left":"el desayuno","right":"завтрак"},{"left":"la comida","right":"обед"},{"left":"la cena","right":"ужин"},{"left":"la fruta","right":"фрукт"},{"left":"la verdura","right":"овощ"}]},
      {"type":"quiz","question":"Как переводится 'jamón'?","options":[{"id":"a","text":"ветчина","correct":True},{"id":"b","text":"курица","correct":False},{"id":"c","text":"рыба","correct":False},{"id":"d","text":"хлеб","correct":False}]}
    ]},
    # ── Lesson 6.2: На рынке — En el mercado (4 steps, 20 XP) ──
    {"t": "На рынке — En el mercado", "xp": 20, "steps": [
      {"type":"info","title":"En el mercado","markdown":"## На рынке\n\n### Полезные фразы:\n| Испанский | Русский |\n|-----------|---------|\n| ¿Cuánto cuesta el kilo de...? | Сколько стоит килограмм...? |\n| Deme un kilo de tomates. | Дайте мне килограмм помидоров. |\n| Medio kilo, por favor. | Полкило, пожалуйста. |\n| ¿Tiene fresas frescas? | У вас есть свежая клубника? |\n| Está muy fresco. | Это очень свежее. |\n| ¿A cuánto están las naranjas? | Почём апельсины? |\n\n### Количество:\n- **un kilo** — килограмм\n- **medio kilo** — полкило\n- **una docena** — дюжина\n- **un litro** — литр\n- **una botella de** — бутылка\n- **un paquete de** — пакет/упаковка"},
      {"type":"fill-blank","text":"Deme ___ kilo de manzanas, por favor. (полкило)","answers":["medio"]},
      {"type":"matching","pairs":[{"left":"un kilo","right":"килограмм"},{"left":"medio kilo","right":"полкило"},{"left":"una docena","right":"дюжина"},{"left":"un litro","right":"литр"},{"left":"una botella","right":"бутылка"}]},
      {"type":"drag-order","items":["Buenos días, ¿qué desea?","Deme un kilo de tomates.","¿Algo más?","Medio kilo de naranjas, por favor.","Nada más. ¿Cuánto es?"]}
    ]},
    # ── Lesson 6.3: Цвета — Los colores (4 steps, 15 XP) ──
    {"t": "Цвета — Los colores", "xp": 15, "steps": [
      {"type":"info","title":"Los colores","markdown":"## Цвета\n\n| Испанский | Русский |\n|-----------|---------|\n| rojo/roja | красный |\n| azul | синий |\n| verde | зелёный |\n| amarillo/a | жёлтый |\n| blanco/a | белый |\n| negro/a | чёрный |\n| gris | серый |\n| marrón | коричневый |\n| naranja | оранжевый |\n| rosa / rosado | розовый |\n| morado/a | фиолетовый |\n\n### Правила:\n- Цвета на **-o** меняют род: rojo → roja, blanco → blanca\n- Цвета на **-e** или согласную — одна форма: verde, azul, gris\n- Ставятся **после** существительного: **el coche rojo** (красная машина)"},
      {"type":"flashcards","cards":[{"front":"rojo","back":"красный"},{"front":"azul","back":"синий"},{"front":"verde","back":"зелёный"},{"front":"amarillo","back":"жёлтый"},{"front":"blanco","back":"белый"},{"front":"negro","back":"чёрный"},{"front":"marrón","back":"коричневый"}]},
      {"type":"matching","pairs":[{"left":"rojo","right":"красный"},{"left":"azul","right":"синий"},{"left":"verde","right":"зелёный"},{"left":"amarillo","right":"жёлтый"},{"left":"negro","right":"чёрный"}]},
      {"type":"true-false","statement":"В испанском цвет ставится ПЕРЕД существительным, как в английском.","correct":False}
    ]},
    # ── Lesson 6.4: Одежда — La ropa (4 steps, 20 XP) ──
    {"t": "Одежда — La ropa", "xp": 20, "steps": [
      {"type":"info","title":"La ropa","markdown":"## Одежда\n\n| Испанский | Русский |\n|-----------|---------|\n| la camiseta | футболка |\n| la camisa | рубашка |\n| los pantalones | брюки |\n| los vaqueros / jeans | джинсы |\n| la falda | юбка |\n| el vestido | платье |\n| la chaqueta | куртка/пиджак |\n| el abrigo | пальто |\n| los zapatos | туфли/ботинки |\n| las zapatillas | кроссовки |\n| el sombrero | шляпа |\n| los calcetines | носки |\n\n### Размеры (las tallas):\nS (pequeña), M (mediana), L (grande), XL (extra grande)\n\n### Фразы:\n- **¿Puedo probármelo?** — Можно примерить?\n- **Me queda bien / mal.** — Мне хорошо / плохо сидит.\n- **¿Tiene una talla más grande?** — Есть размер побольше?"},
      {"type":"flashcards","cards":[{"front":"la camiseta","back":"футболка"},{"front":"los pantalones","back":"брюки"},{"front":"la falda","back":"юбка"},{"front":"el vestido","back":"платье"},{"front":"la chaqueta","back":"куртка/пиджак"},{"front":"los zapatos","back":"туфли/ботинки"}]},
      {"type":"quiz","question":"Как попросить примерить одежду?","options":[{"id":"a","text":"¿Puedo probármelo?","correct":True},{"id":"b","text":"¿Cuánto cuesta?","correct":False},{"id":"c","text":"¿Tiene otra talla?","correct":False},{"id":"d","text":"Me lo llevo","correct":False}]},
      {"type":"fill-blank","text":"Me queda ___. (хорошо)","answers":["bien"]}
    ]},
    # ── Lesson 6.5: Деньги — El dinero (4 steps, 15 XP) ──
    {"t": "Деньги — El dinero", "xp": 15, "steps": [
      {"type":"info","title":"El dinero","markdown":"## Деньги\n\n### Валюты:\n- **el euro (€)** — в Испании\n- **el peso ($)** — в Мексике, Аргентине, Колумбии\n- **el dólar ($)** — в Эквадоре, Панаме\n\n### Полезные фразы:\n| Испанский | Русский |\n|-----------|---------|\n| ¿Cuánto cuesta? | Сколько стоит? |\n| ¿Aceptan tarjeta? | Вы принимаете карту? |\n| En efectivo | Наличными |\n| Con tarjeta | Картой |\n| El cambio | Сдача |\n| ¿Me puede dar el recibo? | Можете дать чек? |\n| Es muy caro / barato | Очень дорого / дёшево |\n| ¿Hay descuento? | Есть скидка? |\n\n### Диалог:\n— Son quince euros con cincuenta. (15,50€)\n— ¿Aceptan tarjeta?\n— Sí, claro."},
      {"type":"matching","pairs":[{"left":"en efectivo","right":"наличными"},{"left":"con tarjeta","right":"картой"},{"left":"el cambio","right":"сдача"},{"left":"el recibo","right":"чек"},{"left":"el descuento","right":"скидка"}]},
      {"type":"quiz","question":"Как спросить 'Принимаете карту?'","options":[{"id":"a","text":"¿Aceptan tarjeta?","correct":True},{"id":"b","text":"¿Cuánto cuesta tarjeta?","correct":False},{"id":"c","text":"¿Tiene tarjeta?","correct":False},{"id":"d","text":"¿Dónde está tarjeta?","correct":False}]},
      {"type":"true-false","statement":"В Испании используется песо (peso).","correct":False}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 7: Путешествия
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Путешествия", "pos": 6, "lessons": [
    # ── Lesson 7.1: В аэропорту (5 steps, 20 XP) ──
    {"t": "В аэропорту — En el aeropuerto", "xp": 20, "steps": [
      {"type":"info","title":"En el aeropuerto","markdown":"## В аэропорту\n\n### Лексика:\n| Испанский | Русский |\n|-----------|---------|\n| el aeropuerto | аэропорт |\n| el vuelo | рейс |\n| la puerta de embarque | выход на посадку |\n| el equipaje | багаж |\n| la maleta | чемодан |\n| el pasaporte | паспорт |\n| la tarjeta de embarque | посадочный талон |\n| el control de seguridad | контроль безопасности |\n| las llegadas | прилёты |\n| las salidas | вылеты |\n| con retraso | с задержкой |\n\n### Фразы:\n- **¿A qué hora sale el vuelo?** — Во сколько вылет?\n- **¿Dónde es la puerta de embarque?** — Где выход на посадку?\n- **Mi vuelo tiene retraso.** — Мой рейс задерживается.\n- **¿Dónde puedo recoger el equipaje?** — Где можно забрать багаж?"},
      {"type":"flashcards","cards":[{"front":"el vuelo","back":"рейс"},{"front":"la maleta","back":"чемодан"},{"front":"el pasaporte","back":"паспорт"},{"front":"la tarjeta de embarque","back":"посадочный талон"},{"front":"las llegadas","back":"прилёты"},{"front":"las salidas","back":"вылеты"}]},
      {"type":"matching","pairs":[{"left":"el vuelo","right":"рейс"},{"left":"la maleta","right":"чемодан"},{"left":"el equipaje","right":"багаж"},{"left":"la puerta de embarque","right":"выход на посадку"},{"left":"con retraso","right":"с задержкой"}]},
      {"type":"fill-blank","text":"¿A qué hora sale el ___? (рейс)","answers":["vuelo"]},
      {"type":"quiz","question":"Как сказать 'Мой рейс задерживается'?","options":[{"id":"a","text":"Mi vuelo tiene retraso","correct":True},{"id":"b","text":"Mi vuelo es rápido","correct":False},{"id":"c","text":"Mi vuelo está aquí","correct":False},{"id":"d","text":"Mi vuelo sale ahora","correct":False}]}
    ]},
    # ── Lesson 7.2: В отеле (4 steps, 20 XP) ──
    {"t": "В отеле — En el hotel", "xp": 20, "steps": [
      {"type":"info","title":"En el hotel","markdown":"## В отеле\n\n### Лексика:\n| Испанский | Русский |\n|-----------|---------|\n| la habitación | номер |\n| habitación individual | одноместный |\n| habitación doble | двухместный |\n| la reserva | бронирование |\n| la llave / la tarjeta | ключ / карточка |\n| la recepción | ресепшн |\n| el desayuno incluido | завтрак включён |\n| la piscina | бассейн |\n| el ascensor | лифт |\n| la planta / el piso | этаж |\n\n### Фразы:\n- **Tengo una reserva a nombre de...** — У меня бронь на имя...\n- **¿A qué hora es el check-out?** — Во сколько выезд?\n- **¿Tiene habitaciones libres?** — Есть свободные номера?\n- **¿El desayuno está incluido?** — Завтрак включён?\n- **La habitación 305, por favor.** — Номер 305, пожалуйста."},
      {"type":"matching","pairs":[{"left":"la habitación individual","right":"одноместный номер"},{"left":"la habitación doble","right":"двухместный номер"},{"left":"la reserva","right":"бронирование"},{"left":"la piscina","right":"бассейн"},{"left":"el ascensor","right":"лифт"}]},
      {"type":"fill-blank","text":"Tengo una ___ a nombre de García. (бронирование)","answers":["reserva"]},
      {"type":"quiz","question":"Как спросить 'Есть свободные номера?'","options":[{"id":"a","text":"¿Tiene habitaciones libres?","correct":True},{"id":"b","text":"¿Cuánto cuesta?","correct":False},{"id":"c","text":"¿Dónde está la habitación?","correct":False},{"id":"d","text":"¿A qué hora es el desayuno?","correct":False}]}
    ]},
    # ── Lesson 7.3: Экскурсии (4 steps, 20 XP) ──
    {"t": "Экскурсии — Las excursiones", "xp": 20, "steps": [
      {"type":"info","title":"Las excursiones","markdown":"## Экскурсии и достопримечательности\n\n### Лексика:\n| Испанский | Русский |\n|-----------|---------|\n| la excursión | экскурсия |\n| el museo | музей |\n| la catedral | собор |\n| el castillo | замок |\n| la playa | пляж |\n| la montaña | гора |\n| el parque | парк |\n| la plaza | площадь |\n| el guía turístico | гид |\n| sacar fotos | фотографировать |\n\n### Фразы:\n- **¿Hay excursiones guiadas?** — Есть экскурсии с гидом?\n- **¿Se puede sacar fotos aquí?** — Здесь можно фотографировать?\n- **¿Cuánto dura la excursión?** — Сколько длится экскурсия?\n- **¿A qué hora empieza?** — Во сколько начинается?\n- **Me gustaría visitar el museo.** — Мне бы хотелось посетить музей."},
      {"type":"flashcards","cards":[{"front":"el museo","back":"музей"},{"front":"la catedral","back":"собор"},{"front":"el castillo","back":"замок"},{"front":"la playa","back":"пляж"},{"front":"la montaña","back":"гора"},{"front":"sacar fotos","back":"фотографировать"}]},
      {"type":"matching","pairs":[{"left":"el museo","right":"музей"},{"left":"la playa","right":"пляж"},{"left":"el castillo","right":"замок"},{"left":"la plaza","right":"площадь"},{"left":"el guía turístico","right":"гид"}]},
      {"type":"type-answer","question":"Как сказать 'фотографировать' по-испански?","acceptedAnswers":["sacar fotos","hacer fotos"]}
    ]},
    # ── Lesson 7.4: Проблемы в путешествии (4 steps, 25 XP) ──
    {"t": "Проблемы в путешествии", "xp": 25, "steps": [
      {"type":"info","title":"Problemas de viaje","markdown":"## Проблемы в путешествии\n\n### Экстренные фразы:\n| Испанский | Русский |\n|-----------|---------|\n| ¡Ayuda! | Помогите! |\n| ¡Llame a la policía! | Вызовите полицию! |\n| Necesito un médico. | Мне нужен врач. |\n| He perdido mi pasaporte. | Я потерял паспорт. |\n| Me han robado. | Меня обокрали. |\n| Estoy perdido/perdida. | Я заблудился/заблудилась. |\n| No me siento bien. | Я плохо себя чувствую. |\n| ¿Dónde está la farmacia? | Где аптека? |\n| ¿Dónde está la comisaría? | Где полицейский участок? |\n| No hablo español. | Я не говорю по-испански. |\n| ¿Habla inglés/ruso? | Вы говорите по-английски/по-русски? |\n\n### В больнице:\n- **Me duele la cabeza.** — У меня болит голова.\n- **Me duele el estómago.** — У меня болит живот.\n- **Soy alérgico/a a...** — У меня аллергия на..."},
      {"type":"flashcards","cards":[{"front":"¡Ayuda!","back":"Помогите!"},{"front":"He perdido mi pasaporte","back":"Я потерял паспорт"},{"front":"Estoy perdido/a","back":"Я заблудился/заблудилась"},{"front":"Necesito un médico","back":"Мне нужен врач"},{"front":"Me duele la cabeza","back":"У меня болит голова"},{"front":"No hablo español","back":"Я не говорю по-испански"}]},
      {"type":"matching","pairs":[{"left":"¡Ayuda!","right":"Помогите!"},{"left":"Me han robado","right":"Меня обокрали"},{"left":"Estoy perdido","right":"Я заблудился"},{"left":"No me siento bien","right":"Я плохо себя чувствую"},{"left":"la farmacia","right":"аптека"}]},
      {"type":"multi-select","question":"Какие фразы пригодятся при потере паспорта?","options":[{"id":"a","text":"He perdido mi pasaporte","correct":True},{"id":"b","text":"¿Dónde está la comisaría?","correct":True},{"id":"c","text":"Necesito un médico","correct":False},{"id":"d","text":"¡Llame a la policía!","correct":True},{"id":"e","text":"Me duele la cabeza","correct":False}]}
    ]},
    # ── Lesson 7.5: Прошедшее время — Pretérito indefinido (5 steps, 30 XP) ──
    {"t": "Прошедшее время — Pretérito indefinido", "xp": 30, "steps": [
      {"type":"info","title":"El pretérito indefinido","markdown":"## Прошедшее время (Pretérito indefinido)\n\nИспользуется для завершённых действий в прошлом.\n\n### Правильные глаголы:\n\n**-AR (hablar):**\n| Лицо | Форма |\n|------|-------|\n| yo | hablé |\n| tú | hablaste |\n| él/ella | habló |\n| nosotros | hablamos |\n| ellos | hablaron |\n\n**-ER/-IR (comer, vivir):**\n| yo | comí / viví |\n| tú | comiste / viviste |\n| él/ella | comió / vivió |\n| nosotros | comimos / vivimos |\n| ellos | comieron / vivieron |\n\n### Неправильные:\n- **ir/ser** — fui, fuiste, fue, fuimos, fueron\n- **hacer** — hice, hiciste, hizo, hicimos, hicieron\n- **estar** — estuve, estuviste, estuvo, estuvimos, estuvieron\n\n### Маркеры:\nayer (вчера), la semana pasada (на прошлой неделе), el año pasado (в прошлом году)"},
      {"type":"matching","pairs":[{"left":"yo (hablar)","right":"hablé"},{"left":"tú (comer)","right":"comiste"},{"left":"él (vivir)","right":"vivió"},{"left":"yo (ir)","right":"fui"},{"left":"él (hacer)","right":"hizo"}]},
      {"type":"fill-blank","text":"Ayer ___ a Madrid. (ir — yo)","answers":["fui"]},
      {"type":"quiz","question":"Как сказать 'Вчера я говорил с Марией'?","options":[{"id":"a","text":"Ayer hablé con María","correct":True},{"id":"b","text":"Ayer hablo con María","correct":False},{"id":"c","text":"Ayer hablar con María","correct":False},{"id":"d","text":"Ayer hablaba con María","correct":False}]},
      {"type":"drag-order","items":["Определить, что действие завершено в прошлом","Найти основу глагола (убрать -ar/-er/-ir)","Добавить окончание прошедшего времени","Проверить: глагол правильный или неправильный?"]}
    ]}
  ]},

  # ═══════════════════════════════════════════════════════════════════
  # SECTION 8: Культура и обзор
  # ═══════════════════════════════════════════════════════════════════
  {"title": "Культура и обзор", "pos": 7, "lessons": [
    # ── Lesson 8.1: Испания vs Латинская Америка (4 steps, 15 XP) ──
    {"t": "Испания vs Латинская Америка", "xp": 15, "steps": [
      {"type":"info","title":"España vs Latinoamérica","markdown":"## Различия испанского\n\nИспанский — официальный язык **20 стран**!\n\n### Произношение:\n| Особенность | Испания | Латинская Америка |\n|-------------|---------|-------------------|\n| Z, C (перед e/i) | [θ] — como 'th' (zapato) | [s] — (sapato) |\n| S в конце слога | чёткое [s] | часто 'проглатывается' |\n| LL | [ль] | [й] или [ж] (Аргентина) |\n\n### Грамматика:\n- **Vosotros** (вы, неформ.) — только в Испании\n- **Ustedes** — в Латинской Америке для любого 'вы'\n- **Vos** вместо **tú** — в Аргентине, Уругвае\n\n### Лексика:\n| Значение | Испания | Лат. Америка |\n|----------|---------|-------------|\n| машина | coche | carro |\n| квартира | piso | departamento/apartamento |\n| компьютер | ordenador | computadora |\n| мобильный | móvil | celular |\n| автобус | autobús | camión (Мексика), bus |\n| картошка | patata | papa |"},
      {"type":"matching","pairs":[{"left":"coche (Испания)","right":"carro (Лат. Америка)"},{"left":"ordenador (Испания)","right":"computadora (Лат. Америка)"},{"left":"móvil (Испания)","right":"celular (Лат. Америка)"},{"left":"patata (Испания)","right":"papa (Лат. Америка)"},{"left":"piso (Испания)","right":"departamento (Лат. Америка)"}]},
      {"type":"true-false","statement":"Местоимение 'vosotros' используется и в Испании, и в Латинской Америке.","correct":False},
      {"type":"multi-select","question":"Какие различия есть между испанским в Испании и Латинской Америке?","options":[{"id":"a","text":"Произношение Z и C","correct":True},{"id":"b","text":"Использование vosotros","correct":True},{"id":"c","text":"Разная лексика (coche/carro)","correct":True},{"id":"d","text":"Разный алфавит","correct":False}]}
    ]},
    # ── Lesson 8.2: Музыка — La música (3 steps, 15 XP) ──
    {"t": "Музыка — La música española", "xp": 15, "steps": [
      {"type":"info","title":"La música","markdown":"## Музыка испаноязычного мира\n\n### Жанры:\n- **Flamenco** — традиционная музыка юга Испании (Андалусия). Гитара, голос, танец.\n- **Reggaetón** — урбан-жанр из Пуэрто-Рико. Bad Bunny, Daddy Yankee.\n- **Salsa** — карибский танцевальный жанр. Куба, Пуэрто-Рико.\n- **Cumbia** — народный жанр Колумбии, популярен по всей Лат. Америке.\n- **Tango** — аргентинский жанр. Карлос Гардель.\n- **Bachata** — доминиканский жанр. Romeo Santos.\n\n### Известные исполнители:\n- **Shakira** (Колумбия)\n- **Bad Bunny** (Пуэрто-Рико)\n- **Rosalía** (Испания)\n- **Luis Miguel** (Мексика)\n- **Julio Iglesias** (Испания)\n\n### Полезная лексика:\n- **la canción** — песня\n- **la guitarra** — гитара\n- **bailar** — танцевать\n- **el ritmo** — ритм"},
      {"type":"matching","pairs":[{"left":"Flamenco","right":"Испания (Андалусия)"},{"left":"Tango","right":"Аргентина"},{"left":"Salsa","right":"Куба, Пуэрто-Рико"},{"left":"Cumbia","right":"Колумбия"},{"left":"Bachata","right":"Доминиканская Республика"}]},
      {"type":"quiz","question":"Откуда родом фламенко?","options":[{"id":"a","text":"Из Андалусии (юг Испании)","correct":True},{"id":"b","text":"Из Мексики","correct":False},{"id":"c","text":"Из Аргентины","correct":False},{"id":"d","text":"Из Кубы","correct":False}]}
    ]},
    # ── Lesson 8.3: Праздники — Las fiestas (4 steps, 20 XP) ──
    {"t": "Праздники — Las fiestas", "xp": 20, "steps": [
      {"type":"info","title":"Las fiestas","markdown":"## Праздники испаноязычного мира\n\n### Испания:\n- **La Tomatina** (август) — битва помидорами в Буньоле\n- **San Fermín** (июль) — бег быков в Памплоне\n- **Las Fallas** (март) — сжигание фигур в Валенсии\n- **Semana Santa** — Страстная неделя (процессии)\n\n### Латинская Америка:\n- **Día de los Muertos** (2 ноября) — День мёртвых (Мексика)\n- **Carnaval** — Карнавал (Бразилия, но также в Лат. Америке)\n- **Las Posadas** (декабрь) — рождественские процессии (Мексика)\n\n### Общие:\n- **Navidad** — Рождество (25 декабря)\n- **Nochevieja** — Новогодняя ночь\n- **Reyes Magos** (6 января) — День Трёх Королей (дети получают подарки)\n\n### Традиция:\nВ Новогоднюю ночь испанцы едят **12 виноградин** — по одной на каждый удар курантов!"},
      {"type":"flashcards","cards":[{"front":"La Tomatina","back":"Битва помидорами в Буньоле (Испания, август)"},{"front":"San Fermín","back":"Бег быков в Памплоне (Испания, июль)"},{"front":"Día de los Muertos","back":"День мёртвых (Мексика, 2 ноября)"},{"front":"Nochevieja","back":"Новогодняя ночь — едят 12 виноградин"},{"front":"Reyes Magos","back":"День Трёх Королей (6 января) — дети получают подарки"}]},
      {"type":"quiz","question":"Что делают испанцы в Новогоднюю ночь?","options":[{"id":"a","text":"Едят 12 виноградин под бой курантов","correct":True},{"id":"b","text":"Бегут с быками","correct":False},{"id":"c","text":"Бросают помидоры","correct":False},{"id":"d","text":"Сжигают фигуры","correct":False}]},
      {"type":"true-false","statement":"Día de los Muertos — это испанский праздник.","correct":False}
    ]},
    # ── Lesson 8.4: Введение в Subjuntivo (4 steps, 25 XP) ──
    {"t": "Введение в Subjuntivo", "xp": 25, "steps": [
      {"type":"info","title":"El subjuntivo — introducción","markdown":"## Сослагательное наклонение (Subjuntivo)\n\nSubjuntivo — особое наклонение, которое **не существует** в русском языке.\n\nОно выражает: желание, сомнение, эмоции, нереальность.\n\n### Когда используется:\n1. **Желание:** Quiero que **vengas**. (Я хочу, чтобы ты пришёл.)\n2. **Эмоции:** Me alegra que **estés** aquí. (Я рад, что ты здесь.)\n3. **Сомнение:** No creo que **sea** verdad. (Не думаю, что это правда.)\n4. **Просьба:** Es importante que **estudies**. (Важно, чтобы ты учился.)\n\n### Формы (presente de subjuntivo):\n| -AR (hablar) | -ER (comer) | -IR (vivir) |\n|-------------|------------|------------|\n| hable | coma | viva |\n| hables | comas | vivas |\n| hable | coma | viva |\n| hablemos | comamos | vivamos |\n| hablen | coman | vivan |\n\n### Формула: берём форму yo, убираем -o, добавляем 'перевёрнутые' окончания:\n- -AR глаголы → окончания -ER (-e, -es, -e...)\n- -ER/-IR глаголы → окончания -AR (-a, -as, -a...)"},
      {"type":"quiz","question":"Что выражает Subjuntivo?","options":[{"id":"a","text":"Желание, сомнение, эмоции","correct":True},{"id":"b","text":"Факты и реальность","correct":False},{"id":"c","text":"Только прошедшее время","correct":False},{"id":"d","text":"Только будущее время","correct":False}]},
      {"type":"matching","pairs":[{"left":"Quiero que vengas","right":"Желание"},{"left":"Me alegra que estés aquí","right":"Эмоции"},{"left":"No creo que sea verdad","right":"Сомнение"},{"left":"Es importante que estudies","right":"Необходимость/просьба"}]},
      {"type":"fill-blank","text":"Quiero que ___ español. (hablar — tú, subjuntivo)","answers":["hables"]}
    ]},
    # ── Lesson 8.5: Итоговый тест (5 steps, 30 XP) ──
    {"t": "Итоговый тест — Examen final", "xp": 30, "steps": [
      {"type":"info","title":"¡Examen final!","markdown":"## Итоговый тест\n\nПоздравляем! Вы прошли весь начальный курс испанского языка!\n\nДавайте проверим ваши знания по всем темам:\n- Алфавит и произношение\n- Знакомство и числа\n- Повседневная жизнь\n- В городе\n- Глаголы\n- Еда и покупки\n- Путешествия\n- Культура\n\n**¡Buena suerte!** (Удачи!)"},
      {"type":"quiz","question":"Как сказать 'Меня зовут Анна' по-испански?","options":[{"id":"a","text":"Me llamo Anna","correct":True},{"id":"b","text":"Mi nombre Anna","correct":False},{"id":"c","text":"Soy llamo Anna","correct":False},{"id":"d","text":"Estoy Anna","correct":False}]},
      {"type":"matching","pairs":[{"left":"ser","right":"постоянные качества (имя, профессия)"},{"left":"estar","right":"состояние и местоположение"},{"left":"tener","right":"иметь (+ выражения)"},{"left":"gustar","right":"нравиться (особая конструкция)"},{"left":"ir","right":"идти/ехать (voy, vas, va...)"}]},
      {"type":"multi-select","question":"Выберите все правильные предложения:","options":[{"id":"a","text":"Me gustan los gatos","correct":True},{"id":"b","text":"Soy de Rusia","correct":True},{"id":"c","text":"Tengo 25 años","correct":True},{"id":"d","text":"Estoy profesor","correct":False},{"id":"e","text":"Me gusta los libros","correct":False}]},
      {"type":"drag-order","items":["A — Алфавит и произношение","B — Знакомство (¿Cómo te llamas?)","C — Повседневная жизнь (familia, casa, hora)","D — В городе (transporte, restaurante)","E — Глаголы (ser, estar, tener, gustar)","F — Еда и покупки (comida, ropa, dinero)","G — Путешествия (aeropuerto, hotel, pretérito)","H — Культура (fiestas, música, subjuntivo)"]}
    ]}
  ]}
]

async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping."); return
        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author: print("No users."); return
        course = Course(title=T, slug="spanish-beginner-"+uuid.uuid4().hex[:4],
            description=DESC, author_id=author.id, category="Languages", difficulty="Beginner",
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
