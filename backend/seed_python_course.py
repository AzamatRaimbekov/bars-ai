"""Seed: Python — с нуля до Junior — 8 sections, ~45 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Python — с нуля до Junior"
DESC = (
    "Полный курс Python для начинающих — от установки до ООП и финального проекта. "
    "Переменные, циклы, функции, работа с файлами, исключения и объектно-ориентированное "
    "программирование. Интерактивные задания с реальными примерами кода."
)

S = [
    # ==================== SECTION 1: Введение в Python ====================
    {
        "title": "Введение в Python",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое Python?",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Знакомство с Python", "markdown": "## Что такое Python?\n\n**Python** — высокоуровневый язык программирования общего назначения, созданный **Гвидо ван Россумом** в 1991 году.\n\n### Почему Python популярен?\n- **Простой синтаксис** — читается почти как английский текст\n- **Универсальность** — веб, data science, AI, автоматизация, игры\n- **Огромное сообщество** — миллионы разработчиков по всему миру\n- **Богатая экосистема** — более 400 000 пакетов на PyPI\n\n### Где используется Python?\n- **Google** — YouTube, поисковый движок\n- **Instagram** — серверная часть\n- **Netflix** — рекомендательная система\n- **NASA** — научные вычисления\n- **Spotify** — анализ данных\n\n### Python — интерпретируемый язык\nКод выполняется построчно интерпретатором, без компиляции в машинный код."},
                    {"type": "quiz", "question": "Кто создал язык Python?", "options": [{"id": "a", "text": "Линус Торвальдс", "correct": False}, {"id": "b", "text": "Гвидо ван Россум", "correct": True}, {"id": "c", "text": "Джеймс Гослинг", "correct": False}, {"id": "d", "text": "Брендан Эйх", "correct": False}]},
                    {"type": "true-false", "statement": "Python — компилируемый язык программирования.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "Google", "right": "YouTube, поиск"}, {"left": "Instagram", "right": "Серверная часть"}, {"left": "Netflix", "right": "Рекомендации"}, {"left": "NASA", "right": "Научные вычисления"}]},
                ],
            },
            {
                "t": "Установка Python",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Установка Python на компьютер", "markdown": "## Установка Python\n\n### Windows:\n1. Перейдите на [python.org](https://python.org)\n2. Скачайте последнюю версию Python 3.x\n3. Запустите установщик\n4. **Обязательно** поставьте галочку **\"Add Python to PATH\"**\n5. Нажмите \"Install Now\"\n\n### macOS:\n```bash\nbrew install python3\n```\nИли скачайте установщик с python.org.\n\n### Linux (Ubuntu/Debian):\n```bash\nsudo apt update\nsudo apt install python3 python3-pip\n```\n\n### Проверка установки:\nОткройте терминал и введите:\n```bash\npython3 --version\n```\nВы увидите что-то вроде: `Python 3.12.1`\n\n### Редакторы кода:\n- **VS Code** — бесплатный, с расширением Python\n- **PyCharm** — мощная IDE для Python\n- **Jupyter Notebook** — для экспериментов и data science"},
                    {"type": "drag-order", "items": ["Перейти на python.org", "Скачать установщик Python 3", "Поставить галочку Add to PATH", "Нажать Install Now", "Проверить: python3 --version"]},
                    {"type": "quiz", "question": "Какую галочку нужно обязательно поставить при установке Python на Windows?", "options": [{"id": "a", "text": "Install for all users", "correct": False}, {"id": "b", "text": "Add Python to PATH", "correct": True}, {"id": "c", "text": "Install pip", "correct": False}, {"id": "d", "text": "Create desktop shortcut", "correct": False}]},
                    {"type": "category-sort", "categories": ["Редакторы кода", "Команды терминала"], "items": [{"text": "VS Code", "category": "Редакторы кода"}, {"text": "python3 --version", "category": "Команды терминала"}, {"text": "PyCharm", "category": "Редакторы кода"}, {"text": "pip install", "category": "Команды терминала"}, {"text": "Jupyter Notebook", "category": "Редакторы кода"}, {"text": "brew install python3", "category": "Команды терминала"}]},
                ],
            },
            {
                "t": "Первая программа: Hello, World!",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Пишем первую программу", "markdown": "## Hello, World!\n\nТрадиционно первая программа на любом языке выводит приветствие.\n\n### Создайте файл `hello.py`:\n```python\nprint(\"Hello, World!\")\n```\n\n### Запустите в терминале:\n```bash\npython3 hello.py\n```\n\nРезультат:\n```\nHello, World!\n```\n\n### Разбор:\n- `print()` — встроенная функция, выводит текст на экран\n- `\"Hello, World!\"` — строка (текст в кавычках)\n- Кавычки могут быть одинарные `'...'` или двойные `\"...\"`\n\n### Комментарии:\n```python\n# Это комментарий — Python его игнорирует\nprint(\"Привет!\")  # Комментарий в конце строки\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите программу, которая выводит 'Hello, World!'", "correctOrder": ["print(\"Hello, World!\")"]},
                    {"type": "fill-blank", "sentence": "Функция ___ выводит текст на экран в Python.", "answer": "print"},
                    {"type": "quiz", "question": "Какой символ используется для однострочных комментариев в Python?", "options": [{"id": "a", "text": "//", "correct": False}, {"id": "b", "text": "#", "correct": True}, {"id": "c", "text": "/*", "correct": False}, {"id": "d", "text": "--", "correct": False}]},
                    {"type": "type-answer", "question": "Напишите команду, которая выведет слово Python на экран (без кавычек в ответе, только код).", "acceptedAnswers": ["print(\"Python\")", "print('Python')"]},
                ],
            },
            {
                "t": "Интерактивный режим REPL",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "REPL — интерактивная консоль Python", "markdown": "## REPL — Read-Eval-Print Loop\n\n**REPL** — интерактивный режим Python, где можно выполнять код построчно.\n\n### Запуск:\n```bash\npython3\n```\n\nПоявится приглашение `>>>`:\n```python\n>>> 2 + 2\n4\n>>> print(\"Привет!\")\nПривет!\n>>> 10 * 3\n30\n```\n\n### REPL расшифровывается:\n- **R**ead — читает введённый код\n- **E**val — вычисляет (выполняет) его\n- **P**rint — выводит результат\n- **L**oop — повторяет цикл\n\n### Выход из REPL:\n```python\n>>> exit()\n```\nИли нажмите `Ctrl+D` (macOS/Linux) / `Ctrl+Z` (Windows).\n\n### Зачем нужен REPL?\n- Быстро проверить идею\n- Экспериментировать с кодом\n- Изучать новые функции"},
                    {"type": "flashcards", "cards": [{"front": "R в REPL", "back": "Read — читает введённый код"}, {"front": "E в REPL", "back": "Eval — вычисляет (выполняет) код"}, {"front": "P в REPL", "back": "Print — выводит результат"}, {"front": "L в REPL", "back": "Loop — повторяет цикл"}]},
                    {"type": "quiz", "question": "Как выйти из REPL Python?", "options": [{"id": "a", "text": "quit", "correct": False}, {"id": "b", "text": "exit()", "correct": True}, {"id": "c", "text": "stop()", "correct": False}, {"id": "d", "text": "close()", "correct": False}]},
                    {"type": "true-false", "statement": "В REPL Python можно выполнять код только из файла.", "correct": False},
                ],
            },
            {
                "t": "Функция print() подробнее",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Возможности print()", "markdown": "## Функция print()\n\n### Вывод нескольких значений:\n```python\nprint(\"Имя:\", \"Алексей\", \"Возраст:\", 25)\n# Имя: Алексей Возраст: 25\n```\n\n### Параметр sep — разделитель:\n```python\nprint(\"Python\", \"Java\", \"C++\", sep=\" | \")\n# Python | Java | C++\n```\n\n### Параметр end — окончание строки:\n```python\nprint(\"Привет\", end=\" \")\nprint(\"мир!\")\n# Привет мир!\n```\n\nПо умолчанию `end=\"\\n\"` (перевод строки).\n\n### f-строки (форматирование):\n```python\nname = \"Анна\"\nage = 22\nprint(f\"Меня зовут {name}, мне {age} лет\")\n# Меня зовут Анна, мне 22 лет\n```\n\n### Экранирование:\n```python\nprint(\"Строка 1\\nСтрока 2\")  # \\n — перевод строки\nprint(\"Табуляция\\tздесь\")     # \\t — табуляция\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите код, который выведет числа через дефис: 1-2-3", "correctOrder": ["print(1, 2, 3, sep=\"-\")"]},
                    {"type": "fill-blank", "sentence": "Параметр ___ функции print() задаёт разделитель между значениями.", "answer": "sep"},
                    {"type": "multi-select", "question": "Какие параметры есть у функции print()?", "options": [{"id": "a", "text": "sep", "correct": True}, {"id": "b", "text": "end", "correct": True}, {"id": "c", "text": "start", "correct": False}, {"id": "d", "text": "file", "correct": True}, {"id": "e", "text": "format", "correct": False}]},
                    {"type": "type-answer", "question": "Какой символ по умолчанию стоит в параметре end у print()? (напишите символ в виде escape-последовательности)", "acceptedAnswers": ["\\n"]},
                ],
            },
        ],
    },
    # ==================== SECTION 2: Переменные и типы данных ====================
    {
        "title": "Переменные и типы данных",
        "pos": 1,
        "lessons": [
            {
                "t": "Переменные в Python",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Что такое переменные?", "markdown": "## Переменные\n\n**Переменная** — именованная область памяти для хранения данных.\n\n### Создание переменной:\n```python\nname = \"Алексей\"\nage = 25\nheight = 1.78\nis_student = True\n```\n\nВ Python **не нужно указывать тип** — он определяется автоматически.\n\n### Правила именования:\n- Начинается с буквы или `_`\n- Содержит буквы, цифры, `_`\n- **Регистр важен**: `Name` и `name` — разные переменные\n- Нельзя использовать ключевые слова: `if`, `for`, `class`, `return`...\n\n### Соглашения (PEP 8):\n```python\n# snake_case — для переменных и функций\nuser_name = \"Анна\"\nmax_score = 100\n\n# UPPER_CASE — для констант\nPI = 3.14159\nMAX_RETRIES = 3\n```\n\n### Множественное присваивание:\n```python\na, b, c = 1, 2, 3\nx = y = z = 0\n```"},
                    {"type": "quiz", "question": "Какое имя переменной корректно в Python?", "options": [{"id": "a", "text": "2name", "correct": False}, {"id": "b", "text": "my-var", "correct": False}, {"id": "c", "text": "user_name", "correct": True}, {"id": "d", "text": "class", "correct": False}]},
                    {"type": "category-sort", "categories": ["Корректные имена", "Некорректные имена"], "items": [{"text": "user_age", "category": "Корректные имена"}, {"text": "2nd_place", "category": "Некорректные имена"}, {"text": "_private", "category": "Корректные имена"}, {"text": "my-var", "category": "Некорректные имена"}, {"text": "MAX_SIZE", "category": "Корректные имена"}, {"text": "for", "category": "Некорректные имена"}]},
                    {"type": "true-false", "statement": "В Python переменные Name и name — это одна и та же переменная.", "correct": False},
                    {"type": "fill-blank", "sentence": "Стиль именования переменных в Python называется ___.", "answer": "snake_case"},
                ],
            },
            {
                "t": "Числа: int и float",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Числовые типы данных", "markdown": "## Числа в Python\n\n### int — целые числа:\n```python\na = 42\nb = -10\nc = 1_000_000  # подчёркивание для читаемости\n```\n\n### float — числа с плавающей точкой:\n```python\npi = 3.14\ntemp = -5.5\nscience = 2.5e3  # 2500.0\n```\n\n### Арифметические операции:\n```python\nprint(10 + 3)   # 13  — сложение\nprint(10 - 3)   # 7   — вычитание\nprint(10 * 3)   # 30  — умножение\nprint(10 / 3)   # 3.333... — деление (всегда float!)\nprint(10 // 3)  # 3   — целочисленное деление\nprint(10 % 3)   # 1   — остаток от деления\nprint(10 ** 3)  # 1000 — возведение в степень\n```\n\n### Преобразование типов:\n```python\nint(3.7)    # 3 — отбрасывает дробную часть\nfloat(5)    # 5.0\nint(\"42\")   # 42 — строка в число\n```"},
                    {"type": "matching", "pairs": [{"left": "+", "right": "Сложение"}, {"left": "//", "right": "Целочисленное деление"}, {"left": "%", "right": "Остаток от деления"}, {"left": "**", "right": "Возведение в степень"}]},
                    {"type": "type-answer", "question": "Чему равно 17 // 5 в Python? (напишите число)", "acceptedAnswers": ["3"]},
                    {"type": "quiz", "question": "Какой тип вернёт операция 10 / 2 в Python?", "options": [{"id": "a", "text": "int", "correct": False}, {"id": "b", "text": "float", "correct": True}, {"id": "c", "text": "str", "correct": False}, {"id": "d", "text": "bool", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите код, вычисляющий остаток от деления 17 на 5", "correctOrder": ["result = 17 % 5", "print(result)"]},
                ],
            },
            {
                "t": "Строки (str)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Строки в Python", "markdown": "## Строки (str)\n\nСтрока — последовательность символов в кавычках.\n\n### Создание строк:\n```python\ns1 = 'Одинарные кавычки'\ns2 = \"Двойные кавычки\"\ns3 = '''Многострочная\nстрока'''\n```\n\n### Операции со строками:\n```python\n# Конкатенация (склеивание)\nfirst = \"Привет\"\nlast = \"мир\"\nfull = first + \" \" + last  # \"Привет мир\"\n\n# Повторение\nprint(\"ha\" * 3)  # \"hahaha\"\n\n# Длина строки\nprint(len(\"Python\"))  # 6\n```\n\n### Индексация:\n```python\nword = \"Python\"\nprint(word[0])   # 'P' — первый символ\nprint(word[-1])  # 'n' — последний символ\n```\n\n### f-строки:\n```python\nname = \"Мария\"\nage = 30\nprint(f\"{name}, вам {age} лет\")\n```\n\n### Полезные методы:\n```python\n\"hello\".upper()       # \"HELLO\"\n\"HELLO\".lower()       # \"hello\"\n\" пробелы \".strip()   # \"пробелы\"\n\"hello world\".split() # [\"hello\", \"world\"]\n```"},
                    {"type": "fill-blank", "sentence": "Функция ___ возвращает длину строки.", "answer": "len"},
                    {"type": "type-answer", "question": "Что выведет \"Python\"[0]? (напишите один символ)", "acceptedAnswers": ["P"]},
                    {"type": "code-puzzle", "instructions": "Соберите код, который создаёт строку с именем и возрастом через f-строку", "correctOrder": ["name = \"Анна\"", "age = 25", "print(f\"{name}, {age} лет\")"]},
                    {"type": "multi-select", "question": "Какие из этих операций можно выполнять со строками?", "options": [{"id": "a", "text": "Конкатенация (+)", "correct": True}, {"id": "b", "text": "Повторение (*)", "correct": True}, {"id": "c", "text": "Деление (/)", "correct": False}, {"id": "d", "text": "Индексация ([])", "correct": True}, {"id": "e", "text": "Вычитание (-)", "correct": False}]},
                ],
            },
            {
                "t": "Логический тип bool",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Булевы значения", "markdown": "## Тип bool\n\nБулев тип имеет только два значения: `True` и `False`.\n\n### Операции сравнения:\n```python\nprint(5 > 3)    # True\nprint(5 == 3)   # False\nprint(5 != 3)   # True\nprint(5 >= 5)   # True\nprint(5 < 3)    # False\n```\n\n### Логические операторы:\n```python\nprint(True and False)  # False\nprint(True or False)   # True\nprint(not True)        # False\n```\n\n### Таблица истинности AND:\n| A | B | A and B |\n|---|---|---|\n| True | True | True |\n| True | False | False |\n| False | True | False |\n| False | False | False |\n\n### Что считается False:\n```python\nbool(0)      # False\nbool(\"\")     # False\nbool([])     # False\nbool(None)   # False\nbool(0.0)    # False\n```\n\nВсё остальное — `True`."},
                    {"type": "matching", "pairs": [{"left": "5 > 3", "right": "True"}, {"left": "5 == 3", "right": "False"}, {"left": "True and False", "right": "False"}, {"left": "not False", "right": "True"}]},
                    {"type": "true-false", "statement": "bool(\"\") возвращает True.", "correct": False},
                    {"type": "quiz", "question": "Что вернёт выражение True or False?", "options": [{"id": "a", "text": "True", "correct": True}, {"id": "b", "text": "False", "correct": False}, {"id": "c", "text": "None", "correct": False}, {"id": "d", "text": "Ошибку", "correct": False}]},
                ],
            },
            {
                "t": "Списки (list)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Списки в Python", "markdown": "## Списки (list)\n\nСписок — **упорядоченная изменяемая** коллекция элементов.\n\n### Создание:\n```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nnumbers = [1, 2, 3, 4, 5]\nmixed = [1, \"два\", 3.0, True]\nempty = []\n```\n\n### Индексация:\n```python\nprint(fruits[0])   # \"яблоко\"\nprint(fruits[-1])  # \"вишня\"\n```\n\n### Основные методы:\n```python\nfruits.append(\"груша\")      # Добавить в конец\nfruits.insert(1, \"манго\")   # Вставить по индексу\nfruits.remove(\"банан\")      # Удалить по значению\nfruits.pop()                # Удалить последний\nfruits.sort()               # Сортировать\nlen(fruits)                 # Длина списка\n```\n\n### Срезы:\n```python\nnums = [0, 1, 2, 3, 4, 5]\nprint(nums[1:4])   # [1, 2, 3]\nprint(nums[:3])    # [0, 1, 2]\nprint(nums[3:])    # [3, 4, 5]\nprint(nums[::2])   # [0, 2, 4]\n```\n\n### Проверка вхождения:\n```python\nprint(\"яблоко\" in fruits)  # True\n```"},
                    {"type": "drag-order", "items": ["fruits = [\"яблоко\", \"банан\"]", "fruits.append(\"вишня\")", "fruits.sort()", "print(fruits)"]},
                    {"type": "quiz", "question": "Какой метод добавляет элемент в конец списка?", "options": [{"id": "a", "text": "add()", "correct": False}, {"id": "b", "text": "append()", "correct": True}, {"id": "c", "text": "insert()", "correct": False}, {"id": "d", "text": "push()", "correct": False}]},
                    {"type": "type-answer", "question": "Что выведет [10, 20, 30][1]? (напишите число)", "acceptedAnswers": ["20"]},
                    {"type": "multi-select", "question": "Какие методы есть у списков?", "options": [{"id": "a", "text": "append()", "correct": True}, {"id": "b", "text": "remove()", "correct": True}, {"id": "c", "text": "trim()", "correct": False}, {"id": "d", "text": "sort()", "correct": True}, {"id": "e", "text": "push()", "correct": False}]},
                ],
            },
            {
                "t": "Словари (dict)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Словари в Python", "markdown": "## Словари (dict)\n\nСловарь — коллекция пар **ключ: значение**.\n\n### Создание:\n```python\nperson = {\n    \"name\": \"Алексей\",\n    \"age\": 25,\n    \"city\": \"Москва\"\n}\n```\n\n### Доступ к значениям:\n```python\nprint(person[\"name\"])       # \"Алексей\"\nprint(person.get(\"age\"))    # 25\nprint(person.get(\"phone\", \"нет\"))  # \"нет\" — значение по умолчанию\n```\n\n### Изменение и добавление:\n```python\nperson[\"age\"] = 26           # Изменить значение\nperson[\"email\"] = \"a@b.com\"  # Добавить новую пару\n```\n\n### Основные методы:\n```python\nperson.keys()    # dict_keys([\"name\", \"age\", \"city\"])\nperson.values()  # dict_values([\"Алексей\", 25, \"Москва\"])\nperson.items()   # dict_items([(...), (...)])\nperson.pop(\"city\")  # Удалить пару по ключу\n```\n\n### Перебор словаря:\n```python\nfor key, value in person.items():\n    print(f\"{key}: {value}\")\n```"},
                    {"type": "fill-blank", "sentence": "Метод ___ возвращает значение по ключу с возможностью указать значение по умолчанию.", "answer": "get"},
                    {"type": "matching", "pairs": [{"left": "keys()", "right": "Все ключи словаря"}, {"left": "values()", "right": "Все значения словаря"}, {"left": "items()", "right": "Пары ключ-значение"}, {"left": "pop()", "right": "Удалить пару по ключу"}]},
                    {"type": "code-puzzle", "instructions": "Соберите код создания словаря и вывода значения по ключу", "correctOrder": ["student = {\"name\": \"Анна\", \"grade\": 5}", "print(student[\"name\"])"]},
                    {"type": "true-false", "statement": "Ключи словаря в Python могут повторяться.", "correct": False},
                ],
            },
        ],
    },
    # ==================== SECTION 3: Условия и циклы ====================
    {
        "title": "Условия и циклы",
        "pos": 2,
        "lessons": [
            {
                "t": "Условный оператор if/elif/else",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Условные конструкции", "markdown": "## if / elif / else\n\nУсловные операторы позволяют выполнять код в зависимости от условия.\n\n### Простой if:\n```python\nage = 18\nif age >= 18:\n    print(\"Вы совершеннолетний\")\n```\n\n### if-else:\n```python\ntemp = 30\nif temp > 25:\n    print(\"Жарко!\")\nelse:\n    print(\"Нормально\")\n```\n\n### if-elif-else:\n```python\nscore = 75\nif score >= 90:\n    grade = \"Отлично\"\nelif score >= 70:\n    grade = \"Хорошо\"\nelif score >= 50:\n    grade = \"Удовлетворительно\"\nelse:\n    grade = \"Неудовлетворительно\"\nprint(grade)  # \"Хорошо\"\n```\n\n### Важно:\n- После условия ставится двоеточие `:`\n- Блок кода выделяется **отступом** (4 пробела)\n- Python использует отступы вместо фигурных скобок"},
                    {"type": "code-puzzle", "instructions": "Соберите конструкцию if-elif-else для проверки возраста", "correctOrder": ["age = 15", "if age >= 18:", "    print(\"Взрослый\")", "elif age >= 14:", "    print(\"Подросток\")", "else:", "    print(\"Ребёнок\")"]},
                    {"type": "fill-blank", "sentence": "После условия в Python ставится символ ___.", "answer": ":"},
                    {"type": "quiz", "question": "Что выведет код: if 0: print('да') else: print('нет')?", "options": [{"id": "a", "text": "да", "correct": False}, {"id": "b", "text": "нет", "correct": True}, {"id": "c", "text": "Ошибку", "correct": False}, {"id": "d", "text": "Ничего", "correct": False}]},
                    {"type": "drag-order", "items": ["if score >= 90:", "    print(\"Отлично\")", "elif score >= 70:", "    print(\"Хорошо\")", "else:", "    print(\"Плохо\")"]},
                ],
            },
            {
                "t": "Цикл for",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Цикл for в Python", "markdown": "## Цикл for\n\nЦикл `for` перебирает элементы последовательности.\n\n### Перебор списка:\n```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nfor fruit in fruits:\n    print(fruit)\n```\n\n### Перебор строки:\n```python\nfor char in \"Python\":\n    print(char)\n```\n\n### Перебор словаря:\n```python\nperson = {\"name\": \"Анна\", \"age\": 25}\nfor key, value in person.items():\n    print(f\"{key} = {value}\")\n```\n\n### Функция range():\n```python\nfor i in range(5):        # 0, 1, 2, 3, 4\n    print(i)\n\nfor i in range(2, 8):     # 2, 3, 4, 5, 6, 7\n    print(i)\n\nfor i in range(0, 10, 2): # 0, 2, 4, 6, 8\n    print(i)\n```\n\n### Функция enumerate():\n```python\ncolors = [\"красный\", \"зелёный\", \"синий\"]\nfor i, color in enumerate(colors):\n    print(f\"{i}: {color}\")\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите цикл, который выведет числа от 1 до 5", "correctOrder": ["for i in range(1, 6):", "    print(i)"]},
                    {"type": "type-answer", "question": "Сколько раз выполнится цикл for i in range(3)? (напишите число)", "acceptedAnswers": ["3"]},
                    {"type": "matching", "pairs": [{"left": "range(5)", "right": "0, 1, 2, 3, 4"}, {"left": "range(2, 5)", "right": "2, 3, 4"}, {"left": "range(0, 10, 3)", "right": "0, 3, 6, 9"}, {"left": "range(5, 0, -1)", "right": "5, 4, 3, 2, 1"}]},
                    {"type": "quiz", "question": "Какая функция позволяет получить индекс при переборе списка?", "options": [{"id": "a", "text": "index()", "correct": False}, {"id": "b", "text": "enumerate()", "correct": True}, {"id": "c", "text": "range()", "correct": False}, {"id": "d", "text": "count()", "correct": False}]},
                ],
            },
            {
                "t": "Цикл while",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Цикл while", "markdown": "## Цикл while\n\nЦикл `while` выполняется, **пока условие истинно**.\n\n### Пример:\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n# Выведет: 0 1 2 3 4\n```\n\n### Счётчик с условием:\n```python\ntotal = 0\nnum = 1\nwhile num <= 100:\n    total += num\n    num += 1\nprint(f\"Сумма: {total}\")  # 5050\n```\n\n### Бесконечный цикл:\n```python\nwhile True:\n    answer = input(\"Введите 'выход': \")\n    if answer == \"выход\":\n        break\n```\n\n### Важно!\n- Убедитесь, что условие **когда-нибудь станет False**, иначе цикл будет бесконечным\n- Используйте `while`, когда число итераций заранее неизвестно\n- Используйте `for`, когда число итераций известно"},
                    {"type": "code-puzzle", "instructions": "Соберите цикл while, считающий от 1 до 3", "correctOrder": ["n = 1", "while n <= 3:", "    print(n)", "    n += 1"]},
                    {"type": "true-false", "statement": "Цикл while True без break будет выполняться бесконечно.", "correct": True},
                    {"type": "quiz", "question": "Когда лучше использовать while вместо for?", "options": [{"id": "a", "text": "Когда перебираем список", "correct": False}, {"id": "b", "text": "Когда число итераций заранее неизвестно", "correct": True}, {"id": "c", "text": "Когда нужно использовать range()", "correct": False}, {"id": "d", "text": "Всегда", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Оператор ___ используется для принудительного выхода из цикла.", "answer": "break"},
                ],
            },
            {
                "t": "Функция range()",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Функция range() подробнее", "markdown": "## range() — генератор чисел\n\n### Три формы вызова:\n\n**1. range(stop):**\n```python\nlist(range(5))    # [0, 1, 2, 3, 4]\n```\n\n**2. range(start, stop):**\n```python\nlist(range(3, 8))  # [3, 4, 5, 6, 7]\n```\n\n**3. range(start, stop, step):**\n```python\nlist(range(0, 20, 5))   # [0, 5, 10, 15]\nlist(range(10, 0, -2))  # [10, 8, 6, 4, 2]\n```\n\n### Важные особенности:\n- **stop** не включается в результат\n- **step** может быть отрицательным (обратный отсчёт)\n- range() не создаёт список в памяти — это генератор\n\n### Практические примеры:\n```python\n# Чётные числа от 0 до 20\nfor n in range(0, 21, 2):\n    print(n)  # 0, 2, 4, ..., 20\n\n# Обратный отсчёт\nfor n in range(5, 0, -1):\n    print(n)  # 5, 4, 3, 2, 1\nprint(\"Старт!\")\n```"},
                    {"type": "type-answer", "question": "Чему равен list(range(3))? Напишите в формате [a, b, c]", "acceptedAnswers": ["[0, 1, 2]"]},
                    {"type": "matching", "pairs": [{"left": "range(4)", "right": "[0, 1, 2, 3]"}, {"left": "range(1, 4)", "right": "[1, 2, 3]"}, {"left": "range(0, 6, 2)", "right": "[0, 2, 4]"}, {"left": "range(3, 0, -1)", "right": "[3, 2, 1]"}]},
                    {"type": "quiz", "question": "Включается ли значение stop в результат range()?", "options": [{"id": "a", "text": "Да, всегда", "correct": False}, {"id": "b", "text": "Нет, никогда", "correct": True}, {"id": "c", "text": "Только при положительном step", "correct": False}, {"id": "d", "text": "Зависит от start", "correct": False}]},
                    {"type": "drag-order", "items": ["range(", "0", ", 10", ", 2", ")"]},
                ],
            },
            {
                "t": "break и continue",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Управление циклами", "markdown": "## break и continue\n\n### break — выход из цикла:\n```python\nfor i in range(10):\n    if i == 5:\n        break\n    print(i)\n# Выведет: 0 1 2 3 4\n```\n\n### continue — пропуск итерации:\n```python\nfor i in range(6):\n    if i == 3:\n        continue\n    print(i)\n# Выведет: 0 1 2 4 5  (3 пропущено)\n```\n\n### Практический пример с break:\n```python\n# Поиск первого отрицательного числа\nnumbers = [5, 3, 8, -2, 7, 1]\nfor num in numbers:\n    if num < 0:\n        print(f\"Найдено: {num}\")\n        break\n```\n\n### Практический пример с continue:\n```python\n# Вывести только чётные числа\nfor i in range(1, 11):\n    if i % 2 != 0:\n        continue\n    print(i)  # 2, 4, 6, 8, 10\n```\n\n### else в цикле:\n```python\nfor i in range(5):\n    if i == 10:\n        break\nelse:\n    print(\"Цикл завершился без break\")\n```"},
                    {"type": "category-sort", "categories": ["break", "continue"], "items": [{"text": "Полностью выходит из цикла", "category": "break"}, {"text": "Пропускает текущую итерацию", "category": "continue"}, {"text": "Код после него не выполняется в этой итерации", "category": "continue"}, {"text": "Цикл прекращает работу", "category": "break"}, {"text": "Цикл продолжает со следующей итерации", "category": "continue"}, {"text": "Используется для раннего выхода", "category": "break"}]},
                    {"type": "quiz", "question": "Что выведет: for i in range(5): if i==2: continue; print(i)?", "options": [{"id": "a", "text": "0 1", "correct": False}, {"id": "b", "text": "0 1 3 4", "correct": True}, {"id": "c", "text": "0 1 2", "correct": False}, {"id": "d", "text": "3 4", "correct": False}]},
                    {"type": "true-false", "statement": "Оператор continue полностью прерывает выполнение цикла.", "correct": False},
                ],
            },
            {
                "t": "Вложенные циклы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Вложенные циклы", "markdown": "## Вложенные циклы\n\nЦикл внутри цикла — это вложенный цикл.\n\n### Таблица умножения:\n```python\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(f\"{i} x {j} = {i*j}\")\n    print()  # Пустая строка между блоками\n```\n\nРезультат:\n```\n1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n\n2 x 1 = 2\n...\n```\n\n### Обход двумерного списка:\n```python\nmatrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nfor row in matrix:\n    for elem in row:\n        print(elem, end=\" \")\n    print()\n```\n\n### Паттерн — треугольник:\n```python\nfor i in range(1, 6):\n    print(\"*\" * i)\n```\n```\n*\n**\n***\n****\n*****\n```\n\n### Внимание к производительности:\nВложенные циклы увеличивают сложность. Два вложенных цикла — O(n^2)."},
                    {"type": "code-puzzle", "instructions": "Соберите вложенный цикл для вывода таблицы умножения 2x2", "correctOrder": ["for i in range(1, 3):", "    for j in range(1, 3):", "        print(f\"{i} x {j} = {i*j}\")"]},
                    {"type": "type-answer", "question": "Сколько раз выполнится print() в коде: for i in range(3): for j in range(4): print(i,j)?", "acceptedAnswers": ["12"]},
                    {"type": "quiz", "question": "Какова временная сложность двух вложенных циклов по n элементов?", "options": [{"id": "a", "text": "O(n)", "correct": False}, {"id": "b", "text": "O(n^2)", "correct": True}, {"id": "c", "text": "O(2n)", "correct": False}, {"id": "d", "text": "O(log n)", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Вложенный цикл", "back": "Цикл внутри другого цикла. Внутренний выполняется полностью на каждой итерации внешнего."}, {"front": "O(n^2)", "back": "Квадратичная сложность — два вложенных цикла по n элементов"}, {"front": "Двумерный список", "back": "Список списков — matrix = [[1,2],[3,4]]. Обходится двумя вложенными циклами."}]},
                ],
            },
        ],
    },
    # ==================== SECTION 4: Функции ====================
    {
        "title": "Функции",
        "pos": 3,
        "lessons": [
            {
                "t": "Определение функций (def)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Создание функций", "markdown": "## Функции в Python\n\nФункция — блок кода, который можно вызывать многократно.\n\n### Определение функции:\n```python\ndef greet():\n    print(\"Привет!\")\n\ngreet()  # Вызов функции\n```\n\n### Функция с параметрами:\n```python\ndef greet(name):\n    print(f\"Привет, {name}!\")\n\ngreet(\"Анна\")   # Привет, Анна!\ngreet(\"Борис\")  # Привет, Борис!\n```\n\n### Значения по умолчанию:\n```python\ndef greet(name, greeting=\"Привет\"):\n    print(f\"{greeting}, {name}!\")\n\ngreet(\"Анна\")              # Привет, Анна!\ngreet(\"Анна\", \"Здравствуй\") # Здравствуй, Анна!\n```\n\n### Зачем нужны функции?\n- **DRY** — Don't Repeat Yourself (не повторяйся)\n- Структурирование кода\n- Повторное использование\n- Читаемость и тестируемость"},
                    {"type": "code-puzzle", "instructions": "Соберите функцию, которая приветствует пользователя по имени", "correctOrder": ["def greet(name):", "    print(f\"Привет, {name}!\")", "", "greet(\"Мария\")"]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ используется для определения функции в Python.", "answer": "def"},
                    {"type": "quiz", "question": "Что означает принцип DRY?", "options": [{"id": "a", "text": "Do Repeat Yourself", "correct": False}, {"id": "b", "text": "Don't Repeat Yourself", "correct": True}, {"id": "c", "text": "Debug Run Yourself", "correct": False}, {"id": "d", "text": "Define Return Yield", "correct": False}]},
                    {"type": "drag-order", "items": ["def", "calculate_area", "(width, height)", ":", "    return width * height"]},
                ],
            },
            {
                "t": "Аргументы функций",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Типы аргументов", "markdown": "## Аргументы функций\n\n### Позиционные аргументы:\n```python\ndef power(base, exp):\n    return base ** exp\n\npower(2, 3)  # 8 — base=2, exp=3\n```\n\n### Именованные аргументы:\n```python\npower(exp=3, base=2)  # 8 — порядок не важен\n```\n\n### Значения по умолчанию:\n```python\ndef power(base, exp=2):\n    return base ** exp\n\npower(5)     # 25 — exp=2 по умолчанию\npower(5, 3)  # 125\n```\n\n### Правило:\nАргументы со значениями по умолчанию **всегда после** обычных:\n```python\n# Правильно:\ndef func(a, b, c=10): ...\n\n# Ошибка:\ndef func(a, c=10, b): ...  # SyntaxError!\n```\n\n### Аннотации типов (подсказки):\n```python\ndef add(a: int, b: int) -> int:\n    return a + b\n```"},
                    {"type": "category-sort", "categories": ["Позиционные", "Именованные"], "items": [{"text": "power(2, 3)", "category": "Позиционные"}, {"text": "power(base=2, exp=3)", "category": "Именованные"}, {"text": "greet(\"Анна\")", "category": "Позиционные"}, {"text": "greet(name=\"Анна\")", "category": "Именованные"}]},
                    {"type": "true-false", "statement": "Аргументы со значениями по умолчанию могут стоять перед обычными аргументами.", "correct": False},
                    {"type": "quiz", "question": "Что произойдёт при вызове power(exp=3, base=2)?", "options": [{"id": "a", "text": "Ошибка — неправильный порядок", "correct": False}, {"id": "b", "text": "Вернёт 8", "correct": True}, {"id": "c", "text": "Вернёт 9", "correct": False}, {"id": "d", "text": "Вернёт None", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите функцию с аргументом по умолчанию", "correctOrder": ["def greet(name, lang=\"ru\"):", "    if lang == \"ru\":", "        print(f\"Привет, {name}!\")", "    else:", "        print(f\"Hello, {name}!\")"]},
                ],
            },
            {
                "t": "Оператор return",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Возвращение значений", "markdown": "## Оператор return\n\n`return` возвращает значение из функции и завершает её выполнение.\n\n### Возврат одного значения:\n```python\ndef square(n):\n    return n ** 2\n\nresult = square(5)\nprint(result)  # 25\n```\n\n### Возврат нескольких значений:\n```python\ndef min_max(numbers):\n    return min(numbers), max(numbers)\n\nlo, hi = min_max([3, 1, 7, 2])\nprint(lo, hi)  # 1 7\n```\nФактически возвращается **кортеж** (tuple).\n\n### Функция без return:\n```python\ndef say_hello():\n    print(\"Привет!\")\n\nresult = say_hello()  # Выведет \"Привет!\"\nprint(result)          # None\n```\n\n### Ранний выход:\n```python\ndef divide(a, b):\n    if b == 0:\n        return None  # Ранний выход\n    return a / b\n```"},
                    {"type": "quiz", "question": "Что вернёт функция без оператора return?", "options": [{"id": "a", "text": "0", "correct": False}, {"id": "b", "text": "\"\"", "correct": False}, {"id": "c", "text": "None", "correct": True}, {"id": "d", "text": "Ошибку", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите функцию, возвращающую сумму двух чисел", "correctOrder": ["def add(a, b):", "    return a + b", "", "result = add(3, 5)", "print(result)"]},
                    {"type": "true-false", "statement": "Функция в Python может возвращать несколько значений через запятую.", "correct": True},
                    {"type": "fill-blank", "sentence": "Если функция не содержит return, она вернёт ___.", "answer": "None"},
                ],
            },
            {
                "t": "*args и **kwargs",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Произвольное число аргументов", "markdown": "## *args и **kwargs\n\n### *args — произвольное число позиционных аргументов:\n```python\ndef total(*args):\n    print(type(args))  # <class 'tuple'>\n    return sum(args)\n\nprint(total(1, 2, 3))      # 6\nprint(total(10, 20, 30, 40)) # 100\n```\n\n### **kwargs — произвольное число именованных аргументов:\n```python\ndef show_info(**kwargs):\n    print(type(kwargs))  # <class 'dict'>\n    for key, value in kwargs.items():\n        print(f\"{key}: {value}\")\n\nshow_info(name=\"Анна\", age=25, city=\"Москва\")\n```\n\n### Комбинирование:\n```python\ndef func(a, b, *args, **kwargs):\n    print(a, b)       # Обычные аргументы\n    print(args)       # Остальные позиционные\n    print(kwargs)     # Именованные\n\nfunc(1, 2, 3, 4, x=5, y=6)\n# 1 2\n# (3, 4)\n# {'x': 5, 'y': 6}\n```\n\n### Распаковка:\n```python\nnums = [1, 2, 3]\nprint(*nums)  # 1 2 3\n\ndata = {\"name\": \"Анна\", \"age\": 25}\nshow_info(**data)  # name: Анна, age: 25\n```"},
                    {"type": "matching", "pairs": [{"left": "*args", "right": "Кортеж позиционных аргументов"}, {"left": "**kwargs", "right": "Словарь именованных аргументов"}, {"left": "*list", "right": "Распаковка списка"}, {"left": "**dict", "right": "Распаковка словаря"}]},
                    {"type": "quiz", "question": "Какого типа переменная args внутри функции def f(*args)?", "options": [{"id": "a", "text": "list", "correct": False}, {"id": "b", "text": "tuple", "correct": True}, {"id": "c", "text": "dict", "correct": False}, {"id": "d", "text": "set", "correct": False}]},
                    {"type": "true-false", "statement": "**kwargs внутри функции является словарём (dict).", "correct": True},
                    {"type": "drag-order", "items": ["def func(", "a, b,", "*args,", "**kwargs", "):"]},
                ],
            },
            {
                "t": "Lambda-функции",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Анонимные функции", "markdown": "## Lambda-функции\n\nLambda — анонимная (безымянная) функция в одну строку.\n\n### Синтаксис:\n```python\nlambda аргументы: выражение\n```\n\n### Примеры:\n```python\n# Обычная функция\ndef square(x):\n    return x ** 2\n\n# То же самое через lambda\nsquare = lambda x: x ** 2\nprint(square(5))  # 25\n```\n\n### Где удобно использовать:\n\n**Сортировка:**\n```python\nstudents = [(\"Анна\", 85), (\"Борис\", 92), (\"Вика\", 78)]\nstudents.sort(key=lambda s: s[1])  # По оценке\n# [(\"Вика\", 78), (\"Анна\", 85), (\"Борис\", 92)]\n```\n\n**filter():**\n```python\nnums = [1, 2, 3, 4, 5, 6]\nevens = list(filter(lambda x: x % 2 == 0, nums))\n# [2, 4, 6]\n```\n\n**map():**\n```python\nnums = [1, 2, 3, 4]\nsquares = list(map(lambda x: x**2, nums))\n# [1, 4, 9, 16]\n```\n\n### Ограничения:\n- Только **одно выражение** (без if/for блоков)\n- Не стоит злоупотреблять — ухудшает читаемость"},
                    {"type": "code-puzzle", "instructions": "Соберите lambda для сортировки списка кортежей по второму элементу", "correctOrder": ["data = [(\"a\", 3), (\"b\", 1), (\"c\", 2)]", "data.sort(key=lambda x: x[1])", "print(data)"]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ создаёт анонимную функцию в Python.", "answer": "lambda"},
                    {"type": "quiz", "question": "Что вернёт (lambda x, y: x + y)(3, 4)?", "options": [{"id": "a", "text": "34", "correct": False}, {"id": "b", "text": "7", "correct": True}, {"id": "c", "text": "Ошибку", "correct": False}, {"id": "d", "text": "None", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "map()", "right": "Применить функцию к каждому элементу"}, {"left": "filter()", "right": "Отфильтровать элементы по условию"}, {"left": "sort(key=...)", "right": "Сортировка с ключом"}, {"left": "lambda", "right": "Анонимная функция"}]},
                ],
            },
            {
                "t": "Рекурсия",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Рекурсивные функции", "markdown": "## Рекурсия\n\n**Рекурсия** — когда функция вызывает саму себя.\n\n### Факториал:\n```python\ndef factorial(n):\n    if n <= 1:       # Базовый случай\n        return 1\n    return n * factorial(n - 1)  # Рекурсивный вызов\n\nprint(factorial(5))  # 120 (5*4*3*2*1)\n```\n\n### Как работает:\n```\nfactorial(5)\n = 5 * factorial(4)\n = 5 * 4 * factorial(3)\n = 5 * 4 * 3 * factorial(2)\n = 5 * 4 * 3 * 2 * factorial(1)\n = 5 * 4 * 3 * 2 * 1\n = 120\n```\n\n### Числа Фибоначчи:\n```python\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(7))  # 13\n```\n\n### Два обязательных компонента:\n1. **Базовый случай** — условие завершения\n2. **Рекурсивный шаг** — вызов с упрощённым аргументом\n\n### Ограничение:\nPython ограничивает глубину рекурсии до ~1000 вызовов (sys.setrecursionlimit)."},
                    {"type": "drag-order", "items": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"]},
                    {"type": "type-answer", "question": "Чему равен factorial(4)? (напишите число)", "acceptedAnswers": ["24"]},
                    {"type": "flashcards", "cards": [{"front": "Базовый случай рекурсии", "back": "Условие, при котором функция прекращает вызывать себя и возвращает значение"}, {"front": "Рекурсивный шаг", "back": "Вызов функцией самой себя с упрощённым аргументом"}, {"front": "Максимальная глубина рекурсии", "back": "По умолчанию ~1000 вызовов. Можно изменить через sys.setrecursionlimit()"}]},
                    {"type": "quiz", "question": "Что произойдёт, если в рекурсии нет базового случая?", "options": [{"id": "a", "text": "Функция вернёт 0", "correct": False}, {"id": "b", "text": "RecursionError — переполнение стека", "correct": True}, {"id": "c", "text": "Функция вернёт None", "correct": False}, {"id": "d", "text": "Python автоматически остановит выполнение", "correct": False}]},
                ],
            },
        ],
    },
    # ==================== SECTION 5: Работа со строками и списками ====================
    {
        "title": "Работа со строками и списками",
        "pos": 4,
        "lessons": [
            {
                "t": "Методы строк",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Полезные методы строк", "markdown": "## Методы строк\n\n### Изменение регистра:\n```python\ns = \"Hello World\"\ns.upper()      # \"HELLO WORLD\"\ns.lower()      # \"hello world\"\ns.capitalize() # \"Hello world\"\ns.title()      # \"Hello World\"\ns.swapcase()   # \"hELLO wORLD\"\n```\n\n### Поиск и замена:\n```python\ns = \"Python is great\"\ns.find(\"is\")      # 7 — индекс первого вхождения\ns.count(\"t\")      # 2 — количество вхождений\ns.replace(\"great\", \"awesome\")  # \"Python is awesome\"\ns.startswith(\"Py\") # True\ns.endswith(\"at\")   # True\n```\n\n### Проверки:\n```python\n\"123\".isdigit()    # True — только цифры\n\"abc\".isalpha()    # True — только буквы\n\"abc123\".isalnum() # True — буквы и цифры\n\"   \".isspace()    # True — только пробелы\n```\n\n### Разделение и соединение:\n```python\n\"a,b,c\".split(\",\")     # [\"a\", \"b\", \"c\"]\n\" \".join([\"Hello\", \"World\"])  # \"Hello World\"\n\"  пробелы  \".strip()  # \"пробелы\"\n```"},
                    {"type": "matching", "pairs": [{"left": "upper()", "right": "Все буквы в верхний регистр"}, {"left": "strip()", "right": "Убрать пробелы по краям"}, {"left": "split()", "right": "Разбить строку в список"}, {"left": "replace()", "right": "Заменить подстроку"}, {"left": "find()", "right": "Найти индекс подстроки"}]},
                    {"type": "type-answer", "question": "Что вернёт \"hello\".upper()? (напишите результат)", "acceptedAnswers": ["HELLO"]},
                    {"type": "multi-select", "question": "Какие методы проверяют содержимое строки?", "options": [{"id": "a", "text": "isdigit()", "correct": True}, {"id": "b", "text": "isalpha()", "correct": True}, {"id": "c", "text": "upper()", "correct": False}, {"id": "d", "text": "isspace()", "correct": True}, {"id": "e", "text": "split()", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите код, который разбивает строку CSV и выводит каждый элемент", "correctOrder": ["data = \"яблоко,банан,вишня\"", "items = data.split(\",\")", "for item in items:", "    print(item)"]},
                ],
            },
            {
                "t": "Срезы (slicing)",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Срезы строк и списков", "markdown": "## Срезы (Slicing)\n\nСрезы позволяют получить часть последовательности.\n\n### Синтаксис: `sequence[start:stop:step]`\n\n### Срезы строк:\n```python\ns = \"Python\"\ns[0:3]    # \"Pyt\" — с 0 по 2\ns[2:]     # \"thon\" — с 2 до конца\ns[:4]     # \"Pyth\" — с начала до 3\ns[-3:]    # \"hon\" — последние 3\ns[::2]    # \"Pto\" — каждый второй\ns[::-1]   # \"nohtyP\" — реверс\n```\n\n### Срезы списков:\n```python\nnums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nnums[2:5]     # [2, 3, 4]\nnums[::3]     # [0, 3, 6, 9]\nnums[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\nnums[1:7:2]   # [1, 3, 5]\n```\n\n### Изменение через срез:\n```python\nnums = [0, 1, 2, 3, 4]\nnums[1:3] = [10, 20]\nprint(nums)  # [0, 10, 20, 3, 4]\n```\n\n### Копирование:\n```python\ncopy = nums[:]  # Полная копия списка\n```"},
                    {"type": "type-answer", "question": "Что вернёт \"Python\"[::-1]? (напишите строку)", "acceptedAnswers": ["nohtyP"]},
                    {"type": "matching", "pairs": [{"left": "s[2:]", "right": "С индекса 2 до конца"}, {"left": "s[:3]", "right": "С начала до индекса 2"}, {"left": "s[::-1]", "right": "Реверс строки"}, {"left": "s[::2]", "right": "Каждый второй символ"}]},
                    {"type": "quiz", "question": "Как создать копию списка через срез?", "options": [{"id": "a", "text": "copy = list[:]", "correct": True}, {"id": "b", "text": "copy = list[0]", "correct": False}, {"id": "c", "text": "copy = list", "correct": False}, {"id": "d", "text": "copy = list[0:]", "correct": True}]},
                    {"type": "fill-blank", "sentence": "Чтобы развернуть строку, используют срез с шагом ___.", "answer": "-1"},
                ],
            },
            {
                "t": "List Comprehension",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Генераторы списков", "markdown": "## List Comprehension\n\nЭлегантный способ создания списков в одну строку.\n\n### Синтаксис:\n```python\n[выражение for элемент in итерируемое]\n```\n\n### Примеры:\n```python\n# Квадраты чисел\nsquares = [x**2 for x in range(6)]\n# [0, 1, 4, 9, 16, 25]\n\n# Длины слов\nwords = [\"Python\", \"Java\", \"C\"]\nlengths = [len(w) for w in words]\n# [6, 4, 1]\n```\n\n### С условием (фильтрация):\n```python\n# Только чётные\nevens = [x for x in range(10) if x % 2 == 0]\n# [0, 2, 4, 6, 8]\n\n# Положительные числа\nnums = [-3, -1, 0, 2, 5]\npositive = [x for x in nums if x > 0]\n# [2, 5]\n```\n\n### С преобразованием и условием:\n```python\n# Квадраты чётных\nresult = [x**2 for x in range(10) if x % 2 == 0]\n# [0, 4, 16, 36, 64]\n```\n\n### Вложенный comprehension:\n```python\nmatrix = [[1, 2], [3, 4], [5, 6]]\nflat = [x for row in matrix for x in row]\n# [1, 2, 3, 4, 5, 6]\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите list comprehension для квадратов чётных чисел от 0 до 8", "correctOrder": ["squares = [x**2 for x in range(9) if x % 2 == 0]", "print(squares)"]},
                    {"type": "type-answer", "question": "Что вернёт [x*2 for x in [1,2,3]]? Напишите в формате [a, b, c]", "acceptedAnswers": ["[2, 4, 6]"]},
                    {"type": "quiz", "question": "Где в list comprehension ставится условие фильтрации?", "options": [{"id": "a", "text": "В начале, перед выражением", "correct": False}, {"id": "b", "text": "После for...in...", "correct": True}, {"id": "c", "text": "Перед for", "correct": False}, {"id": "d", "text": "В отдельных скобках", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "List Comprehension — синтаксис", "back": "[выражение for элемент in итерируемое if условие]"}, {"front": "Dict Comprehension", "back": "{ключ: значение for x in итерируемое}"}, {"front": "Set Comprehension", "back": "{выражение for x in итерируемое}"}]},
                ],
            },
            {
                "t": "Сортировка",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Сортировка данных", "markdown": "## Сортировка в Python\n\n### sort() — изменяет список на месте:\n```python\nnums = [3, 1, 4, 1, 5, 9]\nnums.sort()\nprint(nums)  # [1, 1, 3, 4, 5, 9]\n\nnums.sort(reverse=True)\nprint(nums)  # [9, 5, 4, 3, 1, 1]\n```\n\n### sorted() — возвращает новый список:\n```python\nnums = [3, 1, 4, 1, 5]\nnew = sorted(nums)\nprint(nums)  # [3, 1, 4, 1, 5] — не изменился\nprint(new)   # [1, 1, 3, 4, 5]\n```\n\n### Сортировка с ключом:\n```python\nwords = [\"банан\", \"яблоко\", \"кот\"]\nwords.sort(key=len)  # По длине\n# [\"кот\", \"банан\", \"яблоко\"]\n\nstudents = [(\"Анна\", 85), (\"Борис\", 92), (\"Вика\", 78)]\nstudents.sort(key=lambda s: s[1])  # По оценке\n# [(\"Вика\", 78), (\"Анна\", 85), (\"Борис\", 92)]\n```\n\n### Различие sort() и sorted():\n| | sort() | sorted() |\n|---|---|---|\n| Возвращает | None | Новый список |\n| Изменяет оригинал | Да | Нет |\n| Работает с | Только list | Любой iterable |"},
                    {"type": "category-sort", "categories": ["sort()", "sorted()"], "items": [{"text": "Изменяет список на месте", "category": "sort()"}, {"text": "Возвращает новый список", "category": "sorted()"}, {"text": "Возвращает None", "category": "sort()"}, {"text": "Работает с любым iterable", "category": "sorted()"}, {"text": "Метод списка", "category": "sort()"}, {"text": "Встроенная функция", "category": "sorted()"}]},
                    {"type": "quiz", "question": "Что возвращает метод list.sort()?", "options": [{"id": "a", "text": "Отсортированный список", "correct": False}, {"id": "b", "text": "None", "correct": True}, {"id": "c", "text": "Копию списка", "correct": False}, {"id": "d", "text": "True/False", "correct": False}]},
                    {"type": "true-false", "statement": "Функция sorted() изменяет исходный список.", "correct": False},
                ],
            },
            {
                "t": "Продвинутая работа со словарями",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Словари — продвинутые приёмы", "markdown": "## Продвинутые словари\n\n### Dict Comprehension:\n```python\nsquares = {x: x**2 for x in range(6)}\n# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n\n# Фильтрация\nscores = {\"Анна\": 85, \"Борис\": 45, \"Вика\": 92}\npassed = {k: v for k, v in scores.items() if v >= 50}\n# {\"Анна\": 85, \"Вика\": 92}\n```\n\n### Метод setdefault():\n```python\ncounts = {}\nfor word in [\"кот\", \"пёс\", \"кот\", \"кот\", \"пёс\"]:\n    counts.setdefault(word, 0)\n    counts[word] += 1\n# {\"кот\": 3, \"пёс\": 2}\n```\n\n### Объединение словарей:\n```python\na = {\"x\": 1, \"y\": 2}\nb = {\"y\": 3, \"z\": 4}\n\n# Python 3.9+\nc = a | b  # {\"x\": 1, \"y\": 3, \"z\": 4}\n\n# Python 3.5+\nc = {**a, **b}\n```\n\n### collections.Counter:\n```python\nfrom collections import Counter\ntext = \"abracadabra\"\nCounter(text)\n# Counter({\"a\": 5, \"b\": 2, \"r\": 2, \"c\": 1, \"d\": 1})\n```\n\n### defaultdict:\n```python\nfrom collections import defaultdict\ndd = defaultdict(list)\ndd[\"fruits\"].append(\"яблоко\")\ndd[\"fruits\"].append(\"банан\")\n# {\"fruits\": [\"яблоко\", \"банан\"]}\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите dict comprehension для квадратов чисел от 1 до 5", "correctOrder": ["squares = {x: x**2 for x in range(1, 6)}", "print(squares)"]},
                    {"type": "matching", "pairs": [{"left": "setdefault()", "right": "Установить значение, если ключа нет"}, {"left": "Counter", "right": "Подсчёт элементов"}, {"left": "defaultdict", "right": "Словарь со значением по умолчанию"}, {"left": "a | b", "right": "Объединение словарей (3.9+)"}]},
                    {"type": "quiz", "question": "Что произойдёт при обращении к несуществующему ключу в defaultdict(int)?", "options": [{"id": "a", "text": "KeyError", "correct": False}, {"id": "b", "text": "Вернёт 0", "correct": True}, {"id": "c", "text": "Вернёт None", "correct": False}, {"id": "d", "text": "Вернёт пустую строку", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Класс ___ из модуля collections подсчитывает количество вхождений элементов.", "answer": "Counter"},
                ],
            },
        ],
    },
    # ==================== SECTION 6: Работа с файлами и исключения ====================
    {
        "title": "Работа с файлами и исключения",
        "pos": 5,
        "lessons": [
            {
                "t": "Чтение и запись файлов",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Работа с файлами", "markdown": "## Открытие файлов\n\n### Функция open():\n```python\nf = open(\"file.txt\", \"r\")  # Открыть для чтения\ncontent = f.read()          # Прочитать всё содержимое\nf.close()                   # Закрыть файл\n```\n\n### Режимы открытия:\n| Режим | Описание |\n|-------|----------|\n| `\"r\"` | Чтение (по умолчанию) |\n| `\"w\"` | Запись (перезаписывает файл) |\n| `\"a\"` | Дополнение (добавляет в конец) |\n| `\"x\"` | Создание (ошибка, если файл есть) |\n| `\"b\"` | Бинарный режим |\n\n### Чтение:\n```python\nf = open(\"data.txt\", \"r\", encoding=\"utf-8\")\n\n# Прочитать всё\ncontent = f.read()\n\n# Прочитать построчно\nlines = f.readlines()  # Список строк\n\n# Итерация по строкам\nfor line in f:\n    print(line.strip())\n```\n\n### Запись:\n```python\nf = open(\"output.txt\", \"w\", encoding=\"utf-8\")\nf.write(\"Привет, мир!\\n\")\nf.write(\"Вторая строка\\n\")\nf.close()\n```\n\n### Дополнение:\n```python\nf = open(\"log.txt\", \"a\", encoding=\"utf-8\")\nf.write(\"Новая запись\\n\")\nf.close()\n```"},
                    {"type": "matching", "pairs": [{"left": "\"r\"", "right": "Чтение"}, {"left": "\"w\"", "right": "Запись (перезапись)"}, {"left": "\"a\"", "right": "Дополнение в конец"}, {"left": "\"x\"", "right": "Создание нового файла"}]},
                    {"type": "quiz", "question": "Что произойдёт при открытии существующего файла в режиме 'w'?", "options": [{"id": "a", "text": "Данные добавятся в конец", "correct": False}, {"id": "b", "text": "Файл будет перезаписан", "correct": True}, {"id": "c", "text": "Возникнет ошибка", "correct": False}, {"id": "d", "text": "Ничего не произойдёт", "correct": False}]},
                    {"type": "drag-order", "items": ["f = open(\"data.txt\", \"r\", encoding=\"utf-8\")", "content = f.read()", "print(content)", "f.close()"]},
                    {"type": "fill-blank", "sentence": "Параметр ___ в функции open() задаёт кодировку файла.", "answer": "encoding"},
                ],
            },
            {
                "t": "Менеджер контекста with",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Конструкция with", "markdown": "## Менеджер контекста with\n\nКонструкция `with` автоматически закрывает файл, даже при ошибке.\n\n### Без with (плохо):\n```python\nf = open(\"file.txt\")\ntry:\n    content = f.read()\nfinally:\n    f.close()  # Нужно не забыть!\n```\n\n### С with (хорошо):\n```python\nwith open(\"file.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()\n# Файл автоматически закрыт\n```\n\n### Запись:\n```python\nwith open(\"output.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Строка 1\\n\")\n    f.write(\"Строка 2\\n\")\n```\n\n### Чтение построчно:\n```python\nwith open(\"data.txt\", encoding=\"utf-8\") as f:\n    for line in f:\n        print(line.strip())\n```\n\n### Несколько файлов:\n```python\nwith open(\"input.txt\") as fin, open(\"output.txt\", \"w\") as fout:\n    for line in fin:\n        fout.write(line.upper())\n```\n\n### Почему with лучше?\n- Автоматическое закрытие файла\n- Безопасность — файл закроется даже при ошибке\n- Чистый и понятный код"},
                    {"type": "code-puzzle", "instructions": "Соберите код чтения файла с использованием with", "correctOrder": ["with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:", "    content = f.read()", "print(content)"]},
                    {"type": "true-false", "statement": "При использовании with файл нужно закрывать вручную вызовом close().", "correct": False},
                    {"type": "quiz", "question": "Что произойдёт с файлом после выхода из блока with?", "options": [{"id": "a", "text": "Останется открытым", "correct": False}, {"id": "b", "text": "Автоматически закроется", "correct": True}, {"id": "c", "text": "Будет удалён", "correct": False}, {"id": "d", "text": "Зависит от режима", "correct": False}]},
                    {"type": "category-sort", "categories": ["Хорошая практика", "Плохая практика"], "items": [{"text": "with open() as f:", "category": "Хорошая практика"}, {"text": "f = open(); f.close()", "category": "Плохая практика"}, {"text": "encoding=\"utf-8\"", "category": "Хорошая практика"}, {"text": "Забыть вызвать close()", "category": "Плохая практика"}]},
                ],
            },
            {
                "t": "Обработка исключений try/except",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Обработка ошибок", "markdown": "## try / except\n\nИсключения — ошибки, возникающие при выполнении программы.\n\n### Базовый синтаксис:\n```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Деление на ноль!\")\n```\n\n### Несколько except:\n```python\ntry:\n    num = int(input(\"Число: \"))\n    result = 100 / num\nexcept ValueError:\n    print(\"Это не число!\")\nexcept ZeroDivisionError:\n    print(\"На ноль делить нельзя!\")\n```\n\n### else и finally:\n```python\ntry:\n    f = open(\"data.txt\")\n    content = f.read()\nexcept FileNotFoundError:\n    print(\"Файл не найден!\")\nelse:\n    print(f\"Прочитано {len(content)} символов\")\nfinally:\n    print(\"Этот блок выполнится всегда\")\n```\n\n### Частые исключения:\n| Исключение | Причина |\n|---|---|\n| `ValueError` | Неверное значение |\n| `TypeError` | Неверный тип |\n| `KeyError` | Ключ не найден |\n| `IndexError` | Индекс вне диапазона |\n| `FileNotFoundError` | Файл не найден |\n| `ZeroDivisionError` | Деление на ноль |"},
                    {"type": "matching", "pairs": [{"left": "ValueError", "right": "int(\"abc\")"}, {"left": "KeyError", "right": "dict[\"несуществующий\"]"}, {"left": "IndexError", "right": "list[999]"}, {"left": "ZeroDivisionError", "right": "10 / 0"}, {"left": "FileNotFoundError", "right": "open(\"нет.txt\")"}]},
                    {"type": "drag-order", "items": ["try:", "    result = int(input(\"Число: \"))", "except ValueError:", "    print(\"Ошибка ввода!\")", "else:", "    print(f\"Результат: {result}\")", "finally:", "    print(\"Конец\")"]},
                    {"type": "quiz", "question": "Какой блок выполняется ВСЕГДА, независимо от ошибок?", "options": [{"id": "a", "text": "try", "correct": False}, {"id": "b", "text": "except", "correct": False}, {"id": "c", "text": "else", "correct": False}, {"id": "d", "text": "finally", "correct": True}]},
                    {"type": "fill-blank", "sentence": "Блок ___ выполняется, только если в try не было ошибок.", "answer": "else"},
                ],
            },
            {
                "t": "Создание исключений (raise)",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Оператор raise и свои исключения", "markdown": "## raise — генерация исключений\n\n### Выброс исключения:\n```python\ndef set_age(age):\n    if age < 0:\n        raise ValueError(\"Возраст не может быть отрицательным\")\n    if age > 150:\n        raise ValueError(\"Нереальный возраст\")\n    return age\n\ntry:\n    set_age(-5)\nexcept ValueError as e:\n    print(f\"Ошибка: {e}\")\n# Ошибка: Возраст не может быть отрицательным\n```\n\n### Пользовательские исключения:\n```python\nclass InsufficientFundsError(Exception):\n    def __init__(self, balance, amount):\n        self.balance = balance\n        self.amount = amount\n        super().__init__(\n            f\"Недостаточно средств: баланс {balance}, запрошено {amount}\"\n        )\n\ndef withdraw(balance, amount):\n    if amount > balance:\n        raise InsufficientFundsError(balance, amount)\n    return balance - amount\n\ntry:\n    withdraw(100, 500)\nexcept InsufficientFundsError as e:\n    print(e)  # Недостаточно средств: баланс 100, запрошено 500\n```\n\n### Перевыброс исключения:\n```python\ntry:\n    risky_operation()\nexcept Exception as e:\n    log_error(e)\n    raise  # Пробросить дальше\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите функцию с проверкой и raise", "correctOrder": ["def divide(a, b):", "    if b == 0:", "        raise ValueError(\"Делитель не может быть нулём\")", "    return a / b"]},
                    {"type": "quiz", "question": "Как создать пользовательское исключение?", "options": [{"id": "a", "text": "class MyError(Exception): pass", "correct": True}, {"id": "b", "text": "def MyError(): raise", "correct": False}, {"id": "c", "text": "error MyError = Exception", "correct": False}, {"id": "d", "text": "new Exception(\"MyError\")", "correct": False}]},
                    {"type": "true-false", "statement": "Оператор raise без аргументов пробрасывает текущее исключение дальше.", "correct": True},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ используется для генерации исключения.", "answer": "raise"},
                ],
            },
            {
                "t": "Работа с JSON",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Модуль json", "markdown": "## Работа с JSON\n\nJSON (JavaScript Object Notation) — популярный формат обмена данными.\n\n### Импорт:\n```python\nimport json\n```\n\n### Python -> JSON (сериализация):\n```python\ndata = {\n    \"name\": \"Алексей\",\n    \"age\": 25,\n    \"hobbies\": [\"Python\", \"музыка\"],\n    \"active\": True\n}\n\n# В строку\njson_string = json.dumps(data, ensure_ascii=False, indent=2)\nprint(json_string)\n\n# В файл\nwith open(\"data.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n```\n\n### JSON -> Python (десериализация):\n```python\n# Из строки\ndata = json.loads('{\"name\": \"Анна\", \"age\": 30}')\nprint(data[\"name\"])  # Анна\n\n# Из файла\nwith open(\"data.json\", \"r\", encoding=\"utf-8\") as f:\n    data = json.load(f)\n```\n\n### Соответствие типов:\n| Python | JSON |\n|--------|------|\n| dict | object |\n| list | array |\n| str | string |\n| int/float | number |\n| True/False | true/false |\n| None | null |"},
                    {"type": "matching", "pairs": [{"left": "json.dumps()", "right": "Python -> JSON строка"}, {"left": "json.loads()", "right": "JSON строка -> Python"}, {"left": "json.dump()", "right": "Python -> JSON файл"}, {"left": "json.load()", "right": "JSON файл -> Python"}]},
                    {"type": "code-puzzle", "instructions": "Соберите код записи данных в JSON файл", "correctOrder": ["import json", "data = {\"name\": \"Анна\", \"age\": 25}", "with open(\"data.json\", \"w\", encoding=\"utf-8\") as f:", "    json.dump(data, f, ensure_ascii=False, indent=2)"]},
                    {"type": "quiz", "question": "Какой параметр json.dumps() отвечает за красивое форматирование?", "options": [{"id": "a", "text": "format", "correct": False}, {"id": "b", "text": "indent", "correct": True}, {"id": "c", "text": "pretty", "correct": False}, {"id": "d", "text": "spaces", "correct": False}]},
                    {"type": "category-sort", "categories": ["Python -> JSON", "JSON -> Python"], "items": [{"text": "json.dumps()", "category": "Python -> JSON"}, {"text": "json.loads()", "category": "JSON -> Python"}, {"text": "json.dump()", "category": "Python -> JSON"}, {"text": "json.load()", "category": "JSON -> Python"}]},
                ],
            },
        ],
    },
    # ==================== SECTION 7: ООП ====================
    {
        "title": "Объектно-ориентированное программирование",
        "pos": 6,
        "lessons": [
            {
                "t": "Классы и объекты",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Основы ООП", "markdown": "## Классы и объекты\n\n**Класс** — шаблон (чертёж) для создания объектов.\n**Объект** — экземпляр класса.\n\n### Создание класса:\n```python\nclass Dog:\n    species = \"Canis familiaris\"  # Атрибут класса\n\n    def __init__(self, name, age):\n        self.name = name  # Атрибут экземпляра\n        self.age = age\n\n    def bark(self):\n        return f\"{self.name} говорит: Гав!\"\n\n    def info(self):\n        return f\"{self.name}, {self.age} лет\"\n```\n\n### Создание объектов:\n```python\ndog1 = Dog(\"Бобик\", 3)\ndog2 = Dog(\"Шарик\", 5)\n\nprint(dog1.bark())   # Бобик говорит: Гав!\nprint(dog2.info())   # Шарик, 5 лет\nprint(dog1.species)  # Canis familiaris\n```\n\n### Ключевые понятия:\n- `__init__` — конструктор (инициализатор)\n- `self` — ссылка на текущий объект\n- **Атрибуты класса** — общие для всех экземпляров\n- **Атрибуты экземпляра** — уникальные для каждого объекта"},
                    {"type": "code-puzzle", "instructions": "Соберите класс Cat с именем и методом мяукания", "correctOrder": ["class Cat:", "    def __init__(self, name):", "        self.name = name", "    def meow(self):", "        return f\"{self.name}: Мяу!\""]},
                    {"type": "fill-blank", "sentence": "Метод ___ вызывается автоматически при создании объекта.", "answer": "__init__"},
                    {"type": "quiz", "question": "Что такое self в методах класса?", "options": [{"id": "a", "text": "Имя класса", "correct": False}, {"id": "b", "text": "Ссылка на текущий объект", "correct": True}, {"id": "c", "text": "Глобальная переменная", "correct": False}, {"id": "d", "text": "Ключевое слово Python", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Класс", "back": "Шаблон (чертёж) для создания объектов. Определяет атрибуты и методы."}, {"front": "Объект (экземпляр)", "back": "Конкретная реализация класса с собственными данными."}, {"front": "__init__", "back": "Конструктор — метод, вызываемый при создании объекта. Инициализирует атрибуты."}, {"front": "self", "back": "Ссылка на текущий экземпляр класса. Первый параметр каждого метода."}]},
                ],
            },
            {
                "t": "Метод __init__ и атрибуты",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Конструктор и атрибуты подробнее", "markdown": "## __init__ и атрибуты\n\n### Конструктор с валидацией:\n```python\nclass BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        if balance < 0:\n            raise ValueError(\"Баланс не может быть отрицательным\")\n        self._balance = balance  # Приватный атрибут (соглашение)\n\n    def deposit(self, amount):\n        if amount <= 0:\n            raise ValueError(\"Сумма должна быть положительной\")\n        self._balance += amount\n        return self._balance\n\n    def withdraw(self, amount):\n        if amount > self._balance:\n            raise ValueError(\"Недостаточно средств\")\n        self._balance -= amount\n        return self._balance\n\n    def get_balance(self):\n        return self._balance\n```\n\n### Использование:\n```python\nacc = BankAccount(\"Анна\", 1000)\nacc.deposit(500)       # 1500\nacc.withdraw(200)      # 1300\nprint(acc.get_balance()) # 1300\n```\n\n### Атрибуты класса vs экземпляра:\n```python\nclass Student:\n    school = \"Школа №1\"  # Атрибут класса — общий\n\n    def __init__(self, name):\n        self.name = name  # Атрибут экземпляра — индивидуальный\n\ns1 = Student(\"Анна\")\ns2 = Student(\"Борис\")\nprint(s1.school)  # Школа №1 — от класса\nprint(s1.name)    # Анна — свой\n```"},
                    {"type": "drag-order", "items": ["class Product:", "    def __init__(self, name, price):", "        self.name = name", "        self.price = price", "    def display(self):", "        print(f\"{self.name}: {self.price} руб.\")"]},
                    {"type": "category-sort", "categories": ["Атрибут класса", "Атрибут экземпляра"], "items": [{"text": "Общий для всех объектов", "category": "Атрибут класса"}, {"text": "Уникальный для каждого объекта", "category": "Атрибут экземпляра"}, {"text": "Определяется в __init__ через self", "category": "Атрибут экземпляра"}, {"text": "Определяется в теле класса", "category": "Атрибут класса"}]},
                    {"type": "quiz", "question": "Что означает подчёркивание в начале имени атрибута (_balance)?", "options": [{"id": "a", "text": "Атрибут защищён от изменения", "correct": False}, {"id": "b", "text": "Это соглашение — атрибут приватный", "correct": True}, {"id": "c", "text": "Атрибут доступен только для чтения", "correct": False}, {"id": "d", "text": "Это синтаксическая ошибка", "correct": False}]},
                    {"type": "true-false", "statement": "Атрибуты класса доступны всем экземплярам этого класса.", "correct": True},
                ],
            },
            {
                "t": "Наследование",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Наследование классов", "markdown": "## Наследование\n\nНаследование позволяет создавать новый класс на основе существующего.\n\n### Базовый пример:\n```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return \"...\"\n\n    def info(self):\n        return f\"{self.name}: {self.speak()}\"\n\nclass Dog(Animal):  # Наследует от Animal\n    def speak(self):\n        return \"Гав!\"\n\nclass Cat(Animal):\n    def speak(self):\n        return \"Мяу!\"\n```\n\n### Использование:\n```python\ndog = Dog(\"Бобик\")\ncat = Cat(\"Мурка\")\nprint(dog.info())  # Бобик: Гав!\nprint(cat.info())  # Мурка: Мяу!\n```\n\n### super() — вызов метода родителя:\n```python\nclass Puppy(Dog):\n    def __init__(self, name, tricks=None):\n        super().__init__(name)  # Вызов __init__ родителя\n        self.tricks = tricks or []\n\n    def learn(self, trick):\n        self.tricks.append(trick)\n```\n\n### Проверка наследования:\n```python\nprint(isinstance(dog, Dog))     # True\nprint(isinstance(dog, Animal))  # True\nprint(issubclass(Dog, Animal))  # True\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите класс-наследник с вызовом super()", "correctOrder": ["class Shape:", "    def __init__(self, color):", "        self.color = color", "", "class Circle(Shape):", "    def __init__(self, color, radius):", "        super().__init__(color)", "        self.radius = radius"]},
                    {"type": "fill-blank", "sentence": "Функция ___ вызывает метод родительского класса.", "answer": "super"},
                    {"type": "quiz", "question": "Что вернёт isinstance(dog, Animal), если Dog наследует Animal?", "options": [{"id": "a", "text": "True", "correct": True}, {"id": "b", "text": "False", "correct": False}, {"id": "c", "text": "Ошибку", "correct": False}, {"id": "d", "text": "None", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Родительский класс", "right": "Класс, от которого наследуют"}, {"left": "Дочерний класс", "right": "Класс, который наследует"}, {"left": "super()", "right": "Вызов метода родителя"}, {"left": "isinstance()", "right": "Проверка типа объекта"}]},
                ],
            },
            {
                "t": "Инкапсуляция",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Инкапсуляция и свойства", "markdown": "## Инкапсуляция\n\nИнкапсуляция — сокрытие внутренней реализации класса.\n\n### Уровни доступа (соглашения):\n```python\nclass MyClass:\n    def __init__(self):\n        self.public = \"Публичный\"        # Доступен всем\n        self._protected = \"Защищённый\"    # Только для класса и наследников\n        self.__private = \"Приватный\"      # Только для класса\n```\n\n### Name mangling (двойное подчёркивание):\n```python\nobj = MyClass()\nprint(obj.public)          # OK\nprint(obj._protected)       # OK (но не рекомендуется)\n# print(obj.__private)      # AttributeError!\nprint(obj._MyClass__private) # Можно, но не стоит\n```\n\n### Property — свойства:\n```python\nclass Temperature:\n    def __init__(self, celsius=0):\n        self._celsius = celsius\n\n    @property\n    def celsius(self):\n        return self._celsius\n\n    @celsius.setter\n    def celsius(self, value):\n        if value < -273.15:\n            raise ValueError(\"Ниже абсолютного нуля!\")\n        self._celsius = value\n\n    @property\n    def fahrenheit(self):\n        return self._celsius * 9/5 + 32\n```\n\n### Использование:\n```python\nt = Temperature(25)\nprint(t.celsius)     # 25\nprint(t.fahrenheit)  # 77.0\nt.celsius = 30       # Сеттер с проверкой\n```"},
                    {"type": "matching", "pairs": [{"left": "public", "right": "Нет подчёркивания — доступен всем"}, {"left": "_protected", "right": "Одно подчёркивание — соглашение о приватности"}, {"left": "__private", "right": "Name mangling — затруднён доступ извне"}, {"left": "@property", "right": "Декоратор для геттера свойства"}]},
                    {"type": "quiz", "question": "Как обратиться к атрибуту __secret объекта класса MyClass?", "options": [{"id": "a", "text": "obj.__secret", "correct": False}, {"id": "b", "text": "obj._MyClass__secret", "correct": True}, {"id": "c", "text": "obj.secret", "correct": False}, {"id": "d", "text": "Невозможно", "correct": False}]},
                    {"type": "true-false", "statement": "Декоратор @property позволяет обращаться к методу как к атрибуту.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Инкапсуляция", "back": "Принцип ООП — сокрытие внутренней реализации, доступ только через публичные методы"}, {"front": "@property", "back": "Декоратор, превращающий метод в свойство (геттер). Позволяет контролировать чтение и запись."}, {"front": "Name mangling", "back": "Python преобразует __attr в _ClassName__attr, затрудняя доступ извне класса"}]},
                ],
            },
            {
                "t": "Полиморфизм",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Полиморфизм в Python", "markdown": "## Полиморфизм\n\nПолиморфизм — способность объектов разных классов иметь одинаковый интерфейс.\n\n### Полиморфизм через наследование:\n```python\nclass Shape:\n    def area(self):\n        raise NotImplementedError\n\nclass Rectangle(Shape):\n    def __init__(self, w, h):\n        self.w = w\n        self.h = h\n    def area(self):\n        return self.w * self.h\n\nclass Circle(Shape):\n    def __init__(self, r):\n        self.r = r\n    def area(self):\n        return 3.14159 * self.r ** 2\n```\n\n### Единый интерфейс:\n```python\nshapes = [Rectangle(3, 4), Circle(5), Rectangle(2, 6)]\nfor shape in shapes:\n    print(f\"Площадь: {shape.area():.2f}\")\n# Площадь: 12.00\n# Площадь: 78.54\n# Площадь: 12.00\n```\n\n### Duck typing:\n```python\n# \"Если ходит как утка и крякает как утка — это утка\"\nclass Duck:\n    def quack(self): print(\"Кря!\")\n\nclass Person:\n    def quack(self): print(\"Я умею крякать!\")\n\ndef make_quack(thing):\n    thing.quack()  # Неважно, какой тип — важно, что есть метод\n\nmake_quack(Duck())    # Кря!\nmake_quack(Person())  # Я умею крякать!\n```"},
                    {"type": "quiz", "question": "Что такое полиморфизм?", "options": [{"id": "a", "text": "Создание копий объекта", "correct": False}, {"id": "b", "text": "Одинаковый интерфейс для разных типов", "correct": True}, {"id": "c", "text": "Скрытие данных внутри класса", "correct": False}, {"id": "d", "text": "Наследование от нескольких классов", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Принцип ___ typing: если объект имеет нужный метод, его тип не важен.", "answer": "duck"},
                    {"type": "code-puzzle", "instructions": "Соберите пример полиморфизма — вызов area() для разных фигур", "correctOrder": ["shapes = [Rectangle(3, 4), Circle(5)]", "for shape in shapes:", "    print(shape.area())"]},
                    {"type": "true-false", "statement": "В Python полиморфизм работает только через наследование.", "correct": False},
                ],
            },
            {
                "t": "Магические методы",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Магические (dunder) методы", "markdown": "## Магические методы\n\nМагические методы (dunder methods) — методы с двойным подчёркиванием.\n\n### __str__ и __repr__:\n```python\nclass Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __str__(self):\n        return f\"({self.x}, {self.y})\"  # Для пользователя\n\n    def __repr__(self):\n        return f\"Point({self.x}, {self.y})\"  # Для разработчика\n\np = Point(3, 4)\nprint(p)       # (3, 4) — вызывает __str__\nprint(repr(p)) # Point(3, 4) — вызывает __repr__\n```\n\n### Арифметические операторы:\n```python\nclass Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n\n    def __len__(self):\n        return int((self.x**2 + self.y**2) ** 0.5)\n\n    def __eq__(self, other):\n        return self.x == other.x and self.y == other.y\n\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nv3 = v1 + v2  # Вызывает __add__\nprint(v3.x, v3.y)  # 4 6\n```\n\n### Полезные магические методы:\n| Метод | Оператор/функция |\n|---|---|\n| `__add__` | `+` |\n| `__sub__` | `-` |\n| `__mul__` | `*` |\n| `__eq__` | `==` |\n| `__lt__` | `<` |\n| `__len__` | `len()` |\n| `__contains__` | `in` |"},
                    {"type": "matching", "pairs": [{"left": "__str__", "right": "print(obj) — для пользователя"}, {"left": "__repr__", "right": "repr(obj) — для разработчика"}, {"left": "__add__", "right": "Оператор +"}, {"left": "__eq__", "right": "Оператор =="}, {"left": "__len__", "right": "Функция len()"}]},
                    {"type": "code-puzzle", "instructions": "Соберите класс Money с магическим методом сложения", "correctOrder": ["class Money:", "    def __init__(self, amount):", "        self.amount = amount", "    def __add__(self, other):", "        return Money(self.amount + other.amount)", "    def __str__(self):", "        return f\"{self.amount} руб.\""]},
                    {"type": "quiz", "question": "Какой магический метод вызывается при print(obj)?", "options": [{"id": "a", "text": "__repr__", "correct": False}, {"id": "b", "text": "__str__", "correct": True}, {"id": "c", "text": "__print__", "correct": False}, {"id": "d", "text": "__display__", "correct": False}]},
                    {"type": "multi-select", "question": "Какие из этих методов являются магическими?", "options": [{"id": "a", "text": "__init__", "correct": True}, {"id": "b", "text": "__add__", "correct": True}, {"id": "c", "text": "calculate", "correct": False}, {"id": "d", "text": "__len__", "correct": True}, {"id": "e", "text": "get_name", "correct": False}]},
                ],
            },
        ],
    },
    # ==================== SECTION 8: Финальный проект ====================
    {
        "title": "Финальный проект",
        "pos": 7,
        "lessons": [
            {
                "t": "Модули и импорты",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Модульная система Python", "markdown": "## Модули\n\n**Модуль** — файл с Python-кодом (.py), который можно импортировать.\n\n### Встроенные модули:\n```python\nimport math\nprint(math.sqrt(16))   # 4.0\nprint(math.pi)          # 3.141592...\n\nimport random\nprint(random.randint(1, 10))  # Случайное число\n\nimport datetime\nnow = datetime.datetime.now()\nprint(now)  # 2024-01-15 14:30:00\n```\n\n### Способы импорта:\n```python\n# Импорт всего модуля\nimport math\nmath.sqrt(16)\n\n# Импорт конкретных функций\nfrom math import sqrt, pi\nsqrt(16)\n\n# Импорт с псевдонимом\nimport datetime as dt\ndt.datetime.now()\n\n# Импорт всего (не рекомендуется)\nfrom math import *\n```\n\n### Создание своего модуля:\n```python\n# utils.py\ndef greet(name):\n    return f\"Привет, {name}!\"\n\nPI = 3.14159\n```\n\n```python\n# main.py\nfrom utils import greet, PI\nprint(greet(\"Мир\"))  # Привет, Мир!\n```\n\n### __name__ == \"__main__\":\n```python\nif __name__ == \"__main__\":\n    # Этот код выполнится только при прямом запуске\n    print(\"Запущено напрямую\")\n```"},
                    {"type": "category-sort", "categories": ["Правильный импорт", "Не рекомендуется"], "items": [{"text": "import math", "category": "Правильный импорт"}, {"text": "from math import sqrt", "category": "Правильный импорт"}, {"text": "from math import *", "category": "Не рекомендуется"}, {"text": "import datetime as dt", "category": "Правильный импорт"}, {"text": "from os import *", "category": "Не рекомендуется"}]},
                    {"type": "quiz", "question": "Что делает конструкция if __name__ == '__main__'?", "options": [{"id": "a", "text": "Проверяет имя модуля", "correct": False}, {"id": "b", "text": "Выполняет код только при прямом запуске файла", "correct": True}, {"id": "c", "text": "Импортирует главный модуль", "correct": False}, {"id": "d", "text": "Создаёт точку входа программы", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ используется для импорта модулей в Python.", "answer": "import"},
                    {"type": "matching", "pairs": [{"left": "math", "right": "Математические функции"}, {"left": "random", "right": "Случайные числа"}, {"left": "datetime", "right": "Дата и время"}, {"left": "os", "right": "Работа с операционной системой"}, {"left": "json", "right": "Работа с JSON"}]},
                ],
            },
            {
                "t": "pip и установка пакетов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Менеджер пакетов pip", "markdown": "## pip — менеджер пакетов\n\n**pip** — инструмент для установки сторонних пакетов из PyPI.\n\n### Основные команды:\n```bash\n# Установка пакета\npip install requests\n\n# Установка конкретной версии\npip install requests==2.31.0\n\n# Обновление пакета\npip install --upgrade requests\n\n# Удаление пакета\npip uninstall requests\n\n# Список установленных пакетов\npip list\n\n# Информация о пакете\npip show requests\n```\n\n### requirements.txt:\n```bash\n# Сохранить зависимости\npip freeze > requirements.txt\n\n# Установить из файла\npip install -r requirements.txt\n```\n\nСодержимое requirements.txt:\n```\nrequests==2.31.0\nflask==3.0.0\nnumpy>=1.24.0\n```\n\n### Популярные пакеты:\n| Пакет | Назначение |\n|-------|----------|\n| requests | HTTP-запросы |\n| flask | Веб-фреймворк |\n| numpy | Научные вычисления |\n| pandas | Анализ данных |\n| pytest | Тестирование |\n| black | Форматирование кода |"},
                    {"type": "drag-order", "items": ["pip install requests", "import requests", "response = requests.get(\"https://api.example.com\")", "print(response.status_code)"]},
                    {"type": "matching", "pairs": [{"left": "pip install", "right": "Установить пакет"}, {"left": "pip uninstall", "right": "Удалить пакет"}, {"left": "pip freeze", "right": "Список пакетов с версиями"}, {"left": "pip list", "right": "Все установленные пакеты"}]},
                    {"type": "quiz", "question": "Как установить пакеты из файла requirements.txt?", "options": [{"id": "a", "text": "pip install requirements.txt", "correct": False}, {"id": "b", "text": "pip install -r requirements.txt", "correct": True}, {"id": "c", "text": "pip load requirements.txt", "correct": False}, {"id": "d", "text": "pip setup requirements.txt", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Команда pip ___ > requirements.txt сохраняет список установленных пакетов.", "answer": "freeze"},
                ],
            },
            {
                "t": "Виртуальные окружения",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Изоляция проектов", "markdown": "## Виртуальные окружения (venv)\n\n**Виртуальное окружение** — изолированная среда Python для каждого проекта.\n\n### Зачем нужно?\n- Проект A требует `requests==2.25`\n- Проект B требует `requests==2.31`\n- Без venv они конфликтуют!\n\n### Создание и использование:\n```bash\n# Создать виртуальное окружение\npython3 -m venv myenv\n\n# Активировать\n# macOS/Linux:\nsource myenv/bin/activate\n# Windows:\nmyenv\\Scripts\\activate\n\n# Деактивировать\ndeactivate\n```\n\n### Типичный workflow:\n```bash\n# 1. Создать проект\nmkdir my_project && cd my_project\n\n# 2. Создать venv\npython3 -m venv venv\n\n# 3. Активировать\nsource venv/bin/activate\n\n# 4. Установить зависимости\npip install flask requests\n\n# 5. Сохранить зависимости\npip freeze > requirements.txt\n\n# 6. Добавить venv в .gitignore\necho \"venv/\" >> .gitignore\n```\n\n### .gitignore:\n```\nvenv/\n__pycache__/\n*.pyc\n.env\n```\n\n### Важно!\nПапку `venv/` **никогда** не добавляйте в git!"},
                    {"type": "drag-order", "items": ["python3 -m venv venv", "source venv/bin/activate", "pip install flask", "pip freeze > requirements.txt", "deactivate"]},
                    {"type": "quiz", "question": "Зачем нужны виртуальные окружения?", "options": [{"id": "a", "text": "Ускоряют работу Python", "correct": False}, {"id": "b", "text": "Изолируют зависимости разных проектов", "correct": True}, {"id": "c", "text": "Защищают код от вирусов", "correct": False}, {"id": "d", "text": "Автоматически обновляют пакеты", "correct": False}]},
                    {"type": "true-false", "statement": "Папку venv следует добавлять в git-репозиторий.", "correct": False},
                    {"type": "fill-blank", "sentence": "Команда ___ деактивирует виртуальное окружение.", "answer": "deactivate"},
                ],
            },
            {
                "t": "Мини-проект: менеджер задач",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Пишем менеджер задач", "markdown": "## Мини-проект: Todo Manager\n\nОбъединим все знания в одном проекте — консольный менеджер задач.\n\n### Структура проекта:\n```\ntodo_app/\n    __init__.py\n    models.py\n    storage.py\n    app.py\nrequirements.txt\nREADME.md\n```\n\n### models.py:\n```python\nfrom datetime import datetime\n\nclass Task:\n    def __init__(self, title, priority=\"medium\"):\n        self.id = None\n        self.title = title\n        self.priority = priority  # low, medium, high\n        self.done = False\n        self.created_at = datetime.now()\n\n    def complete(self):\n        self.done = True\n\n    def to_dict(self):\n        return {\n            \"id\": self.id,\n            \"title\": self.title,\n            \"priority\": self.priority,\n            \"done\": self.done,\n            \"created_at\": self.created_at.isoformat()\n        }\n\n    @classmethod\n    def from_dict(cls, data):\n        task = cls(data[\"title\"], data[\"priority\"])\n        task.id = data[\"id\"]\n        task.done = data[\"done\"]\n        return task\n\n    def __str__(self):\n        status = \"done\" if self.done else \"todo\"\n        return f\"[{status}] {self.title} ({self.priority})\"\n```\n\n### storage.py:\n```python\nimport json\nfrom models import Task\n\nclass Storage:\n    def __init__(self, filename=\"tasks.json\"):\n        self.filename = filename\n\n    def save(self, tasks):\n        data = [t.to_dict() for t in tasks]\n        with open(self.filename, \"w\", encoding=\"utf-8\") as f:\n            json.dump(data, f, ensure_ascii=False, indent=2)\n\n    def load(self):\n        try:\n            with open(self.filename, encoding=\"utf-8\") as f:\n                return [Task.from_dict(d) for d in json.load(f)]\n        except FileNotFoundError:\n            return []\n```\n\nЭтот проект использует: классы, файлы, JSON, исключения, списки и словари."},
                    {"type": "code-puzzle", "instructions": "Соберите метод to_dict для класса Task", "correctOrder": ["def to_dict(self):", "    return {", "        \"title\": self.title,", "        \"priority\": self.priority,", "        \"done\": self.done", "    }"]},
                    {"type": "multi-select", "question": "Какие концепции Python используются в этом проекте?", "options": [{"id": "a", "text": "Классы и ООП", "correct": True}, {"id": "b", "text": "Работа с файлами", "correct": True}, {"id": "c", "text": "JSON сериализация", "correct": True}, {"id": "d", "text": "Обработка исключений", "correct": True}, {"id": "e", "text": "Машинное обучение", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "models.py", "right": "Класс Task — модель данных"}, {"left": "storage.py", "right": "Чтение и запись в JSON"}, {"left": "app.py", "right": "Основная логика приложения"}, {"left": "__init__.py", "right": "Делает папку пакетом Python"}]},
                    {"type": "flashcards", "cards": [{"front": "to_dict()", "back": "Сериализация: преобразование объекта в словарь для сохранения в JSON"}, {"front": "@classmethod from_dict()", "back": "Десериализация: создание объекта из словаря (фабричный метод)"}, {"front": "try/except FileNotFoundError", "back": "Обрабатываем случай, когда файл ещё не создан — возвращаем пустой список"}]},
                ],
            },
            {
                "t": "Итоговый тест",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Итоговый тест по курсу", "markdown": "## Финальная проверка знаний\n\nВы прошли весь курс **Python — с нуля до Junior**!\n\n### Что вы изучили:\n1. Основы Python — установка, REPL, print()\n2. Переменные и типы данных — int, float, str, bool, list, dict\n3. Условия и циклы — if/elif/else, for, while, break/continue\n4. Функции — def, return, *args/**kwargs, lambda, рекурсия\n5. Строки и списки — методы, срезы, comprehension, сортировка\n6. Файлы и исключения — open, with, try/except, JSON\n7. ООП — классы, наследование, инкапсуляция, полиморфизм\n8. Экосистема — модули, pip, venv, структура проекта\n\n### Следующие шаги:\n- Решайте задачи на **LeetCode**, **Codewars**, **HackerRank**\n- Изучите **Flask** или **Django** для веб-разработки\n- Попробуйте **pandas** и **numpy** для data science\n- Создайте свой проект и выложите на **GitHub**\n- Пройдите собеседование на позицию Junior Python Developer"},
                    {"type": "quiz", "question": "Какой тип данных вернёт выражение 10 / 3?", "options": [{"id": "a", "text": "int", "correct": False}, {"id": "b", "text": "float", "correct": True}, {"id": "c", "text": "str", "correct": False}, {"id": "d", "text": "Decimal", "correct": False}]},
                    {"type": "quiz", "question": "Что выведет [1, 2, 3][::-1]?", "options": [{"id": "a", "text": "[1, 2, 3]", "correct": False}, {"id": "b", "text": "[3, 2, 1]", "correct": True}, {"id": "c", "text": "[3, 2]", "correct": False}, {"id": "d", "text": "Ошибку", "correct": False}]},
                    {"type": "category-sort", "categories": ["Изменяемые (mutable)", "Неизменяемые (immutable)"], "items": [{"text": "list", "category": "Изменяемые (mutable)"}, {"text": "tuple", "category": "Неизменяемые (immutable)"}, {"text": "dict", "category": "Изменяемые (mutable)"}, {"text": "str", "category": "Неизменяемые (immutable)"}, {"text": "set", "category": "Изменяемые (mutable)"}, {"text": "int", "category": "Неизменяемые (immutable)"}]},
                    {"type": "multi-select", "question": "Какие принципы относятся к ООП?", "options": [{"id": "a", "text": "Инкапсуляция", "correct": True}, {"id": "b", "text": "Наследование", "correct": True}, {"id": "c", "text": "Полиморфизм", "correct": True}, {"id": "d", "text": "Рекурсия", "correct": False}, {"id": "e", "text": "Абстракция", "correct": True}]},
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
            slug="python-zero-to-junior-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Python",
            difficulty="Beginner",
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
                    edges.append({"id": f"e-{lc}", "source": nodes[-2]["id"], "target": nodes[-1]["id"]})
                lc += 1
                tl += 1

        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
