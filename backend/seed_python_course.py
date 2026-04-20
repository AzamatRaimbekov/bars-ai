"""Seed: Python — с нуля до Junior — 8 sections, 27 lessons with coding exercises."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSE_TITLE = "Python — с нуля до Junior"

SECTIONS = [
    # ==================== SECTION 1: Основы — print() и комментарии ====================
    {
        "title": "Основы: print() и комментарии",
        "lessons": [
            {
                "title": "Привет, мир!",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Функция print()", "markdown": "## Функция print()\n\nВ Python для вывода текста на экран используется функция `print()`.\n\n```python\nprint(\"Привет, мир!\")\n```\n\nТекст (строка) заключается в кавычки — двойные `\"\"` или одинарные `''`.\n\n### Несколько print()\nКаждый `print()` выводит текст с новой строки:\n```python\nprint(\"Строка 1\")\nprint(\"Строка 2\")\n```\n\nРезультат:\n```\nСтрока 1\nСтрока 2\n```"},
                    {"type": "python-coding", "prompt": "Напишите программу, которая выводит: Привет, мир!", "starterCode": "# Напишите print() с текстом \"Привет, мир!\"\n", "expectedOutput": "Привет, мир!", "hint": "Используйте print(\"Привет, мир!\")"},
                    {"type": "python-coding", "prompt": "Выведите две строки:\nЯ учу Python\nЭто весело!", "starterCode": "# Первая строка\n\n# Вторая строка\n", "expectedOutput": "Я учу Python\nЭто весело!", "hint": "Используйте два вызова print() — по одному на каждую строку"},
                    {"type": "quiz", "question": "Какая функция выводит текст на экран в Python?", "options": [{"id": "a", "text": "echo()", "correct": False}, {"id": "b", "text": "print()", "correct": True}, {"id": "c", "text": "write()", "correct": False}, {"id": "d", "text": "console.log()", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите своё имя (любое) на экран", "starterCode": "# Выведите своё имя\n", "expectedOutput": "", "hint": "print(\"Ваше имя\") — подставьте любое имя в кавычках"}
                ]
            },
            {
                "title": "Комментарии",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Комментарии в Python", "markdown": "## Комментарии\n\nКомментарии — это заметки для программиста. Python их **игнорирует**.\n\n### Однострочный комментарий\nНачинается с символа `#`:\n```python\n# Это комментарий\nprint(\"Привет\")  # Комментарий после кода\n```\n\n### Зачем нужны комментарии?\n- Объясняют **зачем** написан код\n- Помогают другим разработчикам\n- Помогают вам вспомнить логику через месяц\n\n### Важно\nКомментарий не выполняется:\n```python\n# print(\"Эта строка не выведется\")\nprint(\"А эта выведется\")\n```"},
                    {"type": "python-coding", "prompt": "Напишите комментарий '# Моя первая программа' и затем print(\"Hello\")", "starterCode": "# Напишите комментарий и print ниже\n", "expectedOutput": "Hello", "hint": "Комментарий начинается с #, затем на следующей строке print(\"Hello\")"},
                    {"type": "quiz", "question": "Как начинается однострочный комментарий в Python?", "options": [{"id": "a", "text": "//", "correct": False}, {"id": "b", "text": "#", "correct": True}, {"id": "c", "text": "/*", "correct": False}, {"id": "d", "text": "--", "correct": False}]},
                    {"type": "python-coding", "prompt": "Закомментируйте первый print, чтобы вывелось только 'Мир'", "starterCode": "print(\"Привет\")\nprint(\"Мир\")\n", "expectedOutput": "Мир", "hint": "Поставьте # перед первым print(\"Привет\")"}
                ]
            },
            {
                "title": "Вычисления в print()",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Математика в print()", "markdown": "## Вычисления в print()\n\nPython умеет считать! Можно писать математические выражения прямо в `print()`:\n\n```python\nprint(2 + 3)   # 5\nprint(10 - 4)  # 6\nprint(3 * 7)   # 21\nprint(15 / 3)  # 5.0\n```\n\n### Операторы\n| Оператор | Действие | Пример |\n|----------|----------|--------|\n| `+` | Сложение | `2 + 3` → `5` |\n| `-` | Вычитание | `7 - 2` → `5` |\n| `*` | Умножение | `4 * 3` → `12` |\n| `/` | Деление | `10 / 2` → `5.0` |\n| `//` | Целочисленное деление | `7 // 2` → `3` |\n| `%` | Остаток от деления | `7 % 2` → `1` |\n| `**` | Возведение в степень | `2 ** 3` → `8` |"},
                    {"type": "python-coding", "prompt": "Вычислите и выведите результат: 7 + 3", "starterCode": "# Выведите результат сложения 7 + 3\n", "expectedOutput": "10", "hint": "print(7 + 3)"},
                    {"type": "python-coding", "prompt": "Вычислите 2 в степени 10 и выведите результат", "starterCode": "# Оператор возведения в степень: **\n", "expectedOutput": "1024", "hint": "Используйте print(2 ** 10)"},
                    {"type": "python-coding", "prompt": "Найдите остаток от деления 17 на 5", "starterCode": "# Оператор остатка: %\n", "expectedOutput": "2", "hint": "print(17 % 5) — остаток от деления 17 на 5 равен 2"},
                    {"type": "quiz", "question": "Что выведет print(7 // 2)?", "options": [{"id": "a", "text": "3.5", "correct": False}, {"id": "b", "text": "3", "correct": True}, {"id": "c", "text": "4", "correct": False}, {"id": "d", "text": "2", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите результат выражения: (10 + 5) * 2", "starterCode": "# Скобки меняют порядок вычислений\n", "expectedOutput": "30", "hint": "print((10 + 5) * 2)"}
                ]
            }
        ]
    },
    # ==================== SECTION 2: Переменные и типы данных ====================
    {
        "title": "Переменные и типы данных",
        "lessons": [
            {
                "title": "Переменные",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Что такое переменные", "markdown": "## Переменные\n\nПеременная — это **имя**, которое ссылается на значение в памяти.\n\n```python\nname = \"Алиса\"\nage = 25\nprint(name)  # Алиса\nprint(age)   # 25\n```\n\n### Правила именования\n- Начинается с буквы или `_`\n- Содержит буквы, цифры, `_`\n- Регистр важен: `Name` ≠ `name`\n- Нельзя использовать ключевые слова (`if`, `for`, `class`...)\n\n### Присваивание\nЗнак `=` присваивает значение переменной:\n```python\nx = 10\nx = 20  # Теперь x равен 20\n```"},
                    {"type": "python-coding", "prompt": "Создайте переменную city со значением \"Москва\" и выведите её", "starterCode": "# Создайте переменную city\n\n# Выведите её\n", "expectedOutput": "Москва", "hint": "city = \"Москва\" и затем print(city)"},
                    {"type": "python-coding", "prompt": "Создайте две переменные: a = 5, b = 3. Выведите их сумму.", "starterCode": "a = 5\nb = 3\n# Выведите a + b\n", "expectedOutput": "8", "hint": "print(a + b)"},
                    {"type": "quiz", "question": "Какое имя переменной НЕ допустимо в Python?", "options": [{"id": "a", "text": "my_var", "correct": False}, {"id": "b", "text": "_count", "correct": False}, {"id": "c", "text": "2name", "correct": True}, {"id": "d", "text": "firstName", "correct": False}]},
                    {"type": "python-coding", "prompt": "Создайте переменную x = 10, затем присвойте ей значение x + 5 и выведите результат", "starterCode": "x = 10\n# Увеличьте x на 5\n\n# Выведите x\n", "expectedOutput": "15", "hint": "x = x + 5 (или x += 5), затем print(x)"}
                ]
            },
            {
                "title": "Числа — int и float",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Целые и дробные числа", "markdown": "## Типы чисел\n\n### int — целые числа\n```python\nage = 25\ncount = -3\nbig = 1_000_000  # Подчёркивание для читаемости\n```\n\n### float — дробные числа\n```python\npi = 3.14\ntemperature = -2.5\nprice = 99.99\n```\n\n### Арифметика\n```python\nprint(10 / 3)   # 3.3333... (float)\nprint(10 // 3)  # 3 (int)\nprint(type(5))    # <class 'int'>\nprint(type(5.0))  # <class 'float'>\n```\n\nДеление `/` всегда возвращает `float`, даже если результат целый: `4 / 2` → `2.0`"},
                    {"type": "python-coding", "prompt": "Создайте переменную price = 99.99 и quantity = 3. Выведите общую стоимость (price * quantity).", "starterCode": "price = 99.99\nquantity = 3\n# Вычислите и выведите итого\n", "expectedOutput": "299.97", "hint": "print(price * quantity)"},
                    {"type": "python-coding", "prompt": "Выведите результат целочисленного деления 25 на 4", "starterCode": "# Целочисленное деление: //\n", "expectedOutput": "6", "hint": "print(25 // 4)"},
                    {"type": "quiz", "question": "Какой тип у результата выражения 10 / 2?", "options": [{"id": "a", "text": "int", "correct": False}, {"id": "b", "text": "float", "correct": True}, {"id": "c", "text": "str", "correct": False}, {"id": "d", "text": "bool", "correct": False}]},
                    {"type": "python-coding", "prompt": "Вычислите площадь круга с радиусом 7 (формула: 3.14 * r ** 2) и выведите результат", "starterCode": "r = 7\n# Вычислите площадь: 3.14 * r ** 2\n", "expectedOutput": "153.86", "hint": "print(3.14 * r ** 2)"}
                ]
            },
            {
                "title": "Строки",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Строки в Python", "markdown": "## Строки (str)\n\nСтрока — последовательность символов в кавычках:\n```python\nname = \"Python\"\ngreeting = 'Привет'\n```\n\n### Конкатенация (сложение строк)\n```python\nfirst = \"Привет\"\nsecond = \" мир\"\nprint(first + second)  # Привет мир\n```\n\n### f-строки (форматирование)\n```python\nname = \"Анна\"\nage = 22\nprint(f\"Меня зовут {name}, мне {age} лет\")\n```\n\n### Длина строки\n```python\nword = \"Python\"\nprint(len(word))  # 6\n```"},
                    {"type": "python-coding", "prompt": "Создайте переменные first_name = \"Иван\" и last_name = \"Петров\". Выведите полное имя через конкатенацию (с пробелом между ними).", "starterCode": "first_name = \"Иван\"\nlast_name = \"Петров\"\n# Выведите полное имя\n", "expectedOutput": "Иван Петров", "hint": "print(first_name + \" \" + last_name)"},
                    {"type": "python-coding", "prompt": "Используя f-строку, выведите: У меня 3 кота (число 3 должно быть в переменной count)", "starterCode": "count = 3\n# Используйте f-строку\n", "expectedOutput": "У меня 3 кота", "hint": "print(f\"У меня {count} кота\")"},
                    {"type": "python-coding", "prompt": "Найдите и выведите длину строки \"Программирование\"", "starterCode": "word = \"Программирование\"\n# Выведите длину\n", "expectedOutput": "16", "hint": "print(len(word))"},
                    {"type": "quiz", "question": "Что выведет print(\"Ha\" * 3)?", "options": [{"id": "a", "text": "Ha Ha Ha", "correct": False}, {"id": "b", "text": "HaHaHa", "correct": True}, {"id": "c", "text": "Ha3", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите строку \"Python\" повторённую 4 раза (используя оператор *)", "starterCode": "# Повторение строки: строка * число\n", "expectedOutput": "PythonPythonPythonPython", "hint": "print(\"Python\" * 4)"}
                ]
            },
            {
                "title": "Преобразование типов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Преобразование типов", "markdown": "## Преобразование типов\n\nИногда нужно превратить одно значение в другой тип:\n\n```python\n# str → int\nage_str = \"25\"\nage = int(age_str)  # 25 (число)\n\n# int → str\ncount = 10\ntext = str(count)  # \"10\" (строка)\n\n# str → float\nprice = float(\"9.99\")  # 9.99\n```\n\n### Функция type()\n```python\nprint(type(42))      # <class 'int'>\nprint(type(\"Hi\"))    # <class 'str'>\nprint(type(3.14))    # <class 'float'>\n```\n\n### Частая ошибка\n```python\nage = 25\n# print(\"Мне \" + age + \" лет\")  # ОШИБКА!\nprint(\"Мне \" + str(age) + \" лет\")  # OK\n```"},
                    {"type": "python-coding", "prompt": "Преобразуйте строку \"42\" в число, прибавьте 8 и выведите результат", "starterCode": "s = \"42\"\n# Преобразуйте в int, прибавьте 8, выведите\n", "expectedOutput": "50", "hint": "print(int(s) + 8)"},
                    {"type": "python-coding", "prompt": "Выведите тип значения 3.14 с помощью функции type()", "starterCode": "# Используйте type()\n", "expectedOutput": "<class 'float'>", "hint": "print(type(3.14))"},
                    {"type": "quiz", "question": "Что вернёт int(\"7.5\")?", "options": [{"id": "a", "text": "7", "correct": False}, {"id": "b", "text": "7.5", "correct": False}, {"id": "c", "text": "Ошибку (ValueError)", "correct": True}, {"id": "d", "text": "8", "correct": False}]},
                    {"type": "python-coding", "prompt": "Создайте переменную num = 100. Выведите строку: \"Результат: 100\" используя конкатенацию и str()", "starterCode": "num = 100\n# Выведите \"Результат: 100\" через конкатенацию\n", "expectedOutput": "Результат: 100", "hint": "print(\"Результат: \" + str(num))"}
                ]
            }
        ]
    },
    # ==================== SECTION 3: Строки подробнее ====================
    {
        "title": "Строки подробнее",
        "lessons": [
            {
                "title": "Методы строк",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Методы строк", "markdown": "## Методы строк\n\nМетод — это функция, которая вызывается через точку:\n\n```python\ntext = \"Hello World\"\n\nprint(text.upper())    # HELLO WORLD\nprint(text.lower())    # hello world\nprint(text.title())    # Hello World\n```\n\n### Полезные методы\n| Метод | Действие |\n|-------|----------|\n| `.upper()` | Все в верхний регистр |\n| `.lower()` | Все в нижний регистр |\n| `.strip()` | Убрать пробелы по краям |\n| `.replace(a, b)` | Заменить a на b |\n| `.count(x)` | Сколько раз x встречается |\n| `.startswith(x)` | Начинается ли с x |\n\n```python\nemail = \"  user@mail.ru  \"\nprint(email.strip())  # user@mail.ru\n\ntext = \"Привет мир\"\nprint(text.replace(\"мир\", \"Python\"))  # Привет Python\n```"},
                    {"type": "python-coding", "prompt": "Переведите строку \"python\" в верхний регистр и выведите", "starterCode": "lang = \"python\"\n# Выведите в верхнем регистре\n", "expectedOutput": "PYTHON", "hint": "print(lang.upper())"},
                    {"type": "python-coding", "prompt": "Уберите лишние пробелы из строки \"  Hello  \" и выведите результат", "starterCode": "text = \"  Hello  \"\n# Используйте .strip()\n", "expectedOutput": "Hello", "hint": "print(text.strip())"},
                    {"type": "python-coding", "prompt": "Замените слово \"Java\" на \"Python\" в строке \"Я учу Java\" и выведите", "starterCode": "text = \"Я учу Java\"\n# Используйте .replace()\n", "expectedOutput": "Я учу Python", "hint": "print(text.replace(\"Java\", \"Python\"))"},
                    {"type": "quiz", "question": "Что вернёт \"hello world\".title()?", "options": [{"id": "a", "text": "HELLO WORLD", "correct": False}, {"id": "b", "text": "Hello World", "correct": True}, {"id": "c", "text": "hello world", "correct": False}, {"id": "d", "text": "Hello world", "correct": False}]},
                    {"type": "python-coding", "prompt": "Посчитайте, сколько раз буква 'о' встречается в строке \"молоко\" и выведите число", "starterCode": "word = \"молоко\"\n# Используйте .count()\n", "expectedOutput": "3", "hint": "print(word.count(\"о\"))"}
                ]
            },
            {
                "title": "Индексация и срезы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Индексация и срезы", "markdown": "## Индексация строк\n\nКаждый символ имеет номер (индекс), начиная с 0:\n```\n P  y  t  h  o  n\n 0  1  2  3  4  5\n-6 -5 -4 -3 -2 -1\n```\n\n```python\ns = \"Python\"\nprint(s[0])   # P\nprint(s[-1])  # n\n```\n\n## Срезы\n```python\ns = \"Python\"\nprint(s[0:3])   # Pyt (с 0 до 3, не включая 3)\nprint(s[2:])    # thon (с 2 до конца)\nprint(s[:2])    # Py (с начала до 2)\nprint(s[::2])   # Pto (каждый второй символ)\nprint(s[::-1])  # nohtyP (реверс)\n```"},
                    {"type": "python-coding", "prompt": "Выведите первый символ строки \"Привет\"", "starterCode": "word = \"Привет\"\n# Выведите первый символ\n", "expectedOutput": "П", "hint": "print(word[0])"},
                    {"type": "python-coding", "prompt": "Выведите последний символ строки \"Python\"", "starterCode": "word = \"Python\"\n# Выведите последний символ\n", "expectedOutput": "n", "hint": "print(word[-1])"},
                    {"type": "python-coding", "prompt": "Выведите первые 3 символа строки \"Программа\"", "starterCode": "word = \"Программа\"\n# Используйте срез [:3]\n", "expectedOutput": "Про", "hint": "print(word[:3])"},
                    {"type": "quiz", "question": "Что выведет print(\"Hello\"[1:4])?", "options": [{"id": "a", "text": "Hel", "correct": False}, {"id": "b", "text": "ell", "correct": True}, {"id": "c", "text": "ello", "correct": False}, {"id": "d", "text": "Hell", "correct": False}]},
                    {"type": "python-coding", "prompt": "Переверните строку \"абвгд\" с помощью среза и выведите", "starterCode": "s = \"абвгд\"\n# Переверните строку\n", "expectedOutput": "дгвба", "hint": "print(s[::-1])"}
                ]
            },
            {
                "title": "Форматирование строк",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "f-строки и .format()", "markdown": "## Форматирование строк\n\n### f-строки (Python 3.6+) — рекомендуемый способ\n```python\nname = \"Мария\"\nage = 30\nprint(f\"{name}, возраст: {age}\")  # Мария, возраст: 30\n```\n\nВнутри `{}` можно писать выражения:\n```python\na = 5\nb = 3\nprint(f\"{a} + {b} = {a + b}\")  # 5 + 3 = 8\n```\n\n### Метод .format()\n```python\nprint(\"Привет, {}!\".format(\"мир\"))  # Привет, мир!\nprint(\"{0} и {1}\".format(\"кошка\", \"собака\"))  # кошка и собака\n```\n\n### Форматирование чисел\n```python\npi = 3.14159\nprint(f\"Пи: {pi:.2f}\")  # Пи: 3.14\n```"},
                    {"type": "python-coding", "prompt": "Используя f-строку, выведите: 5 + 3 = 8 (числа 5 и 3 должны быть в переменных)", "starterCode": "a = 5\nb = 3\n# Выведите f-строку\n", "expectedOutput": "5 + 3 = 8", "hint": "print(f\"{a} + {b} = {a + b}\")"},
                    {"type": "python-coding", "prompt": "Отформатируйте число 3.14159 до 2 знаков после запятой и выведите: Пи: 3.14", "starterCode": "pi = 3.14159\n# Используйте f\"{pi:.2f}\"\n", "expectedOutput": "Пи: 3.14", "hint": "print(f\"Пи: {pi:.2f}\")"},
                    {"type": "quiz", "question": "Какой результат f\"{2 ** 10}\"?", "options": [{"id": "a", "text": "\"2 ** 10\"", "correct": False}, {"id": "b", "text": "\"1024\"", "correct": True}, {"id": "c", "text": "Ошибка", "correct": False}, {"id": "d", "text": "\"210\"", "correct": False}]},
                    {"type": "python-coding", "prompt": "Используя .format(), выведите: Привет, Python!", "starterCode": "lang = \"Python\"\n# Используйте \"Привет, {}!\".format(...)\n", "expectedOutput": "Привет, Python!", "hint": "print(\"Привет, {}!\".format(lang))"},
                    {"type": "python-coding", "prompt": "Создайте переменные name = \"Алекс\" и score = 95. Выведите: Алекс набрал 95 баллов", "starterCode": "name = \"Алекс\"\nscore = 95\n# Выведите с помощью f-строки\n", "expectedOutput": "Алекс набрал 95 баллов", "hint": "print(f\"{name} набрал {score} баллов\")"}
                ]
            }
        ]
    },
    # ==================== SECTION 4: Условия ====================
    {
        "title": "Условия",
        "lessons": [
            {
                "title": "if / else",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Условный оператор if", "markdown": "## Оператор if / else\n\nПозволяет выполнять код **по условию**:\n```python\nage = 18\nif age >= 18:\n    print(\"Взрослый\")\nelse:\n    print(\"Несовершеннолетний\")\n```\n\n### Операторы сравнения\n| Оператор | Значение |\n|----------|----------|\n| `==` | Равно |\n| `!=` | Не равно |\n| `>` | Больше |\n| `<` | Меньше |\n| `>=` | Больше или равно |\n| `<=` | Меньше или равно |\n\n### Важно: отступы!\nТело `if` и `else` должно быть с отступом в 4 пробела:\n```python\nif True:\n    print(\"Да\")  # 4 пробела\n```"},
                    {"type": "python-coding", "prompt": "Переменная x = 10. Если x > 5, выведите \"Больше пяти\", иначе \"Не больше пяти\"", "starterCode": "x = 10\n# Напишите if/else\n", "expectedOutput": "Больше пяти", "hint": "if x > 5:\\n    print(\"Больше пяти\")\\nelse:\\n    print(\"Не больше пяти\")"},
                    {"type": "python-coding", "prompt": "Проверьте, равна ли переменная password строке \"secret\". Если да — выведите \"Доступ разрешён\", иначе \"Доступ запрещён\"", "starterCode": "password = \"secret\"\n# Проверьте password\n", "expectedOutput": "Доступ разрешён", "hint": "if password == \"secret\":\\n    print(\"Доступ разрешён\")"},
                    {"type": "quiz", "question": "Что произойдёт, если в if нет отступа у тела?", "options": [{"id": "a", "text": "Код работает нормально", "correct": False}, {"id": "b", "text": "IndentationError", "correct": True}, {"id": "c", "text": "Условие игнорируется", "correct": False}, {"id": "d", "text": "SyntaxWarning", "correct": False}]},
                    {"type": "python-coding", "prompt": "Число n = 7. Определите, чётное оно или нечётное. Выведите \"Нечётное\"", "starterCode": "n = 7\n# Если n % 2 == 0 — чётное, иначе нечётное\n", "expectedOutput": "Нечётное", "hint": "if n % 2 == 0:\\n    print(\"Чётное\")\\nelse:\\n    print(\"Нечётное\")"}
                ]
            },
            {
                "title": "elif — множественные условия",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Конструкция elif", "markdown": "## elif — несколько условий\n\nКогда вариантов больше двух, используйте `elif`:\n```python\nscore = 85\n\nif score >= 90:\n    print(\"Отлично\")\nelif score >= 70:\n    print(\"Хорошо\")\nelif score >= 50:\n    print(\"Удовлетворительно\")\nelse:\n    print(\"Неудовлетворительно\")\n```\n\n### Порядок важен!\nPython проверяет условия **сверху вниз** и выполняет **первое** истинное:\n```python\nx = 15\nif x > 5:    # True — выполнится это\n    print(\"A\")\nelif x > 10:  # Тоже True, но уже не проверяется\n    print(\"B\")\n```\nВыведет: `A`"},
                    {"type": "python-coding", "prompt": "Переменная temp = 25. Если temp > 30 — выведите \"Жарко\", если temp > 20 — \"Тепло\", если temp > 10 — \"Прохладно\", иначе \"Холодно\"", "starterCode": "temp = 25\n# Напишите if/elif/else\n", "expectedOutput": "Тепло", "hint": "if temp > 30: ... elif temp > 20: print(\"Тепло\") ..."},
                    {"type": "python-coding", "prompt": "Переменная grade = 4. Выведите оценку словами: 5→\"Отлично\", 4→\"Хорошо\", 3→\"Удовлетворительно\", иначе \"Плохо\"", "starterCode": "grade = 4\n# Определите оценку словами\n", "expectedOutput": "Хорошо", "hint": "if grade == 5: ... elif grade == 4: print(\"Хорошо\") ..."},
                    {"type": "quiz", "question": "Сколько блоков elif может быть в одной конструкции?", "options": [{"id": "a", "text": "Только 1", "correct": False}, {"id": "b", "text": "Максимум 3", "correct": False}, {"id": "c", "text": "Сколько угодно", "correct": True}, {"id": "d", "text": "Максимум 10", "correct": False}]},
                    {"type": "python-coding", "prompt": "Определите время суток по часу hour = 14: 6-11 → \"Утро\", 12-17 → \"День\", 18-22 → \"Вечер\", иначе → \"Ночь\"", "starterCode": "hour = 14\n# Определите время суток\n", "expectedOutput": "День", "hint": "if hour >= 6 and hour <= 11: ... elif hour >= 12 and hour <= 17: print(\"День\") ..."}
                ]
            },
            {
                "title": "Логические операторы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "and, or, not", "markdown": "## Логические операторы\n\n### and — обе условия истинны\n```python\nage = 25\nif age >= 18 and age <= 65:\n    print(\"Работоспособный возраст\")\n```\n\n### or — хотя бы одно условие истинно\n```python\nday = \"суббота\"\nif day == \"суббота\" or day == \"воскресенье\":\n    print(\"Выходной!\")\n```\n\n### not — отрицание\n```python\nis_raining = False\nif not is_raining:\n    print(\"Можно гулять\")\n```\n\n### Приоритет: not → and → or\n```python\n# True or False and False\n# = True or (False and False)\n# = True or False\n# = True\n```"},
                    {"type": "python-coding", "prompt": "Переменная age = 25. Проверьте, что age >= 18 AND age <= 60. Выведите \"Подходит\"", "starterCode": "age = 25\n# Проверьте два условия одновременно\n", "expectedOutput": "Подходит", "hint": "if age >= 18 and age <= 60:\\n    print(\"Подходит\")"},
                    {"type": "python-coding", "prompt": "Переменная day = \"суббота\". Если day == \"суббота\" или day == \"воскресенье\", выведите \"Выходной\"", "starterCode": "day = \"суббота\"\n# Используйте or\n", "expectedOutput": "Выходной", "hint": "if day == \"суббота\" or day == \"воскресенье\":\\n    print(\"Выходной\")"},
                    {"type": "quiz", "question": "Что вернёт выражение: not True and False?", "options": [{"id": "a", "text": "True", "correct": False}, {"id": "b", "text": "False", "correct": True}, {"id": "c", "text": "Ошибка", "correct": False}, {"id": "d", "text": "None", "correct": False}]},
                    {"type": "python-coding", "prompt": "Переменная x = 15. Проверьте, что x делится на 3 И на 5 одновременно. Если да — выведите \"FizzBuzz\"", "starterCode": "x = 15\n# Проверьте делимость на 3 и на 5\n", "expectedOutput": "FizzBuzz", "hint": "if x % 3 == 0 and x % 5 == 0:\\n    print(\"FizzBuzz\")"}
                ]
            }
        ]
    },
    # ==================== SECTION 5: Циклы ====================
    {
        "title": "Циклы",
        "lessons": [
            {
                "title": "for + range()",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Цикл for и range()", "markdown": "## Цикл for\n\nЦикл `for` повторяет блок кода заданное число раз:\n```python\nfor i in range(5):\n    print(i)\n# Выведет: 0, 1, 2, 3, 4\n```\n\n### range() — генератор чисел\n```python\nrange(5)        # 0, 1, 2, 3, 4\nrange(1, 6)     # 1, 2, 3, 4, 5\nrange(0, 10, 2) # 0, 2, 4, 6, 8\n```\n\n### Параметры range(start, stop, step)\n- `start` — начало (по умолчанию 0)\n- `stop` — конец (не включается!)\n- `step` — шаг (по умолчанию 1)"},
                    {"type": "python-coding", "prompt": "Выведите числа от 1 до 5, каждое на новой строке", "starterCode": "# Используйте for и range()\n", "expectedOutput": "1\n2\n3\n4\n5", "hint": "for i in range(1, 6):\\n    print(i)"},
                    {"type": "python-coding", "prompt": "Выведите чётные числа от 2 до 10 включительно", "starterCode": "# Используйте range с шагом 2\n", "expectedOutput": "2\n4\n6\n8\n10", "hint": "for i in range(2, 11, 2):\\n    print(i)"},
                    {"type": "python-coding", "prompt": "Вычислите сумму чисел от 1 до 100 и выведите результат", "starterCode": "total = 0\n# Пройдите циклом от 1 до 100\n\nprint(total)\n", "expectedOutput": "5050", "hint": "for i in range(1, 101):\\n    total += i"},
                    {"type": "quiz", "question": "Сколько раз выполнится тело цикла for i in range(3, 8)?", "options": [{"id": "a", "text": "3", "correct": False}, {"id": "b", "text": "5", "correct": True}, {"id": "c", "text": "6", "correct": False}, {"id": "d", "text": "8", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите таблицу умножения на 3 (3*1=3, 3*2=6, ..., 3*5=15), каждое произведение на отдельной строке", "starterCode": "# Выведите 3, 6, 9, 12, 15\n", "expectedOutput": "3\n6\n9\n12\n15", "hint": "for i in range(1, 6):\\n    print(3 * i)"}
                ]
            },
            {
                "title": "for по спискам и строкам",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Итерация по коллекциям", "markdown": "## for по спискам\n\n```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nfor fruit in fruits:\n    print(fruit)\n```\n\n## for по строкам\nСтрока — это последовательность символов:\n```python\nfor char in \"Python\":\n    print(char)\n# P, y, t, h, o, n\n```\n\n## enumerate() — с индексом\n```python\ncolors = [\"красный\", \"зелёный\", \"синий\"]\nfor i, color in enumerate(colors):\n    print(f\"{i}: {color}\")\n# 0: красный\n# 1: зелёный\n# 2: синий\n```"},
                    {"type": "python-coding", "prompt": "Выведите каждый элемент списка [10, 20, 30, 40] на отдельной строке", "starterCode": "numbers = [10, 20, 30, 40]\n# Пройдите циклом по списку\n", "expectedOutput": "10\n20\n30\n40", "hint": "for n in numbers:\\n    print(n)"},
                    {"type": "python-coding", "prompt": "Посчитайте количество букв 'о' в строке \"молоко\" с помощью цикла и выведите результат", "starterCode": "word = \"молоко\"\ncount = 0\n# Пройдите по каждому символу\n\nprint(count)\n", "expectedOutput": "3", "hint": "for char in word:\\n    if char == \"о\":\\n        count += 1"},
                    {"type": "quiz", "question": "Что выведет for x in \"Hi\": print(x) ?", "options": [{"id": "a", "text": "Hi", "correct": False}, {"id": "b", "text": "H и i на отдельных строках", "correct": True}, {"id": "c", "text": "['H', 'i']", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]},
                    {"type": "python-coding", "prompt": "Используя enumerate, выведите элементы списка [\"a\", \"b\", \"c\"] в формате \"0: a\", \"1: b\", \"2: c\" — каждый на новой строке", "starterCode": "items = [\"a\", \"b\", \"c\"]\n# Используйте enumerate()\n", "expectedOutput": "0: a\n1: b\n2: c", "hint": "for i, item in enumerate(items):\\n    print(f\"{i}: {item}\")"}
                ]
            },
            {
                "title": "while — циклы с условием",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Цикл while", "markdown": "## Цикл while\n\nВыполняется, **пока условие истинно**:\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n# 0, 1, 2, 3, 4\n```\n\n### Осторожно: бесконечный цикл!\n```python\n# while True:  # Никогда не остановится!\n#     print(\"...\") \n```\n\nВсегда убедитесь, что условие когда-нибудь станет `False`.\n\n### while vs for\n- `for` — когда знаем количество итераций\n- `while` — когда не знаем, сколько раз повторять"},
                    {"type": "python-coding", "prompt": "С помощью while выведите числа от 1 до 5", "starterCode": "n = 1\n# Пока n <= 5, выводите n и увеличивайте\n", "expectedOutput": "1\n2\n3\n4\n5", "hint": "while n <= 5:\\n    print(n)\\n    n += 1"},
                    {"type": "python-coding", "prompt": "Найдите первую степень двойки, которая больше 1000, и выведите её", "starterCode": "n = 1\n# Умножайте n на 2, пока n <= 1000\n\nprint(n)\n", "expectedOutput": "1024", "hint": "while n <= 1000:\\n    n *= 2"},
                    {"type": "quiz", "question": "Что произойдёт, если условие while сразу False?", "options": [{"id": "a", "text": "Тело выполнится 1 раз", "correct": False}, {"id": "b", "text": "Тело не выполнится ни разу", "correct": True}, {"id": "c", "text": "Ошибка", "correct": False}, {"id": "d", "text": "Бесконечный цикл", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите обратный отсчёт от 5 до 1 с помощью while", "starterCode": "n = 5\n# Пока n >= 1, выводите и уменьшайте\n", "expectedOutput": "5\n4\n3\n2\n1", "hint": "while n >= 1:\\n    print(n)\\n    n -= 1"}
                ]
            },
            {
                "title": "break и continue",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "break и continue", "markdown": "## break — прерывает цикл\n\n```python\nfor i in range(10):\n    if i == 5:\n        break\n    print(i)\n# 0, 1, 2, 3, 4\n```\n\n## continue — пропускает итерацию\n\n```python\nfor i in range(5):\n    if i == 2:\n        continue\n    print(i)\n# 0, 1, 3, 4\n```\n\n### Пример с while\n```python\nwhile True:\n    command = input(\">>> \")\n    if command == \"exit\":\n        break\n    print(f\"Вы ввели: {command}\")\n```"},
                    {"type": "python-coding", "prompt": "Выведите числа от 1 до 10, но остановитесь (break), когда число равно 6", "starterCode": "for i in range(1, 11):\n    # Остановитесь на 6\n    pass\n", "expectedOutput": "1\n2\n3\n4\n5", "hint": "if i == 6:\\n    break\\nprint(i)"},
                    {"type": "python-coding", "prompt": "Выведите числа от 1 до 5, но пропустите (continue) число 3", "starterCode": "for i in range(1, 6):\n    # Пропустите 3\n    pass\n", "expectedOutput": "1\n2\n4\n5", "hint": "if i == 3:\\n    continue\\nprint(i)"},
                    {"type": "quiz", "question": "Чем отличается break от continue?", "options": [{"id": "a", "text": "break завершает цикл, continue пропускает одну итерацию", "correct": True}, {"id": "b", "text": "Они делают одно и то же", "correct": False}, {"id": "c", "text": "continue завершает цикл", "correct": False}, {"id": "d", "text": "break пропускает итерацию", "correct": False}]},
                    {"type": "python-coding", "prompt": "Найдите первое число от 1 до 20, которое делится и на 3, и на 4. Выведите его и остановите цикл.", "starterCode": "for i in range(1, 21):\n    # Если делится на 3 и на 4 — выведите и break\n    pass\n", "expectedOutput": "12", "hint": "if i % 3 == 0 and i % 4 == 0:\\n    print(i)\\n    break"}
                ]
            }
        ]
    },
    # ==================== SECTION 6: Списки ====================
    {
        "title": "Списки",
        "lessons": [
            {
                "title": "Создание и доступ",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Списки в Python", "markdown": "## Списки (list)\n\nСписок — упорядоченная коллекция элементов:\n```python\nnumbers = [1, 2, 3, 4, 5]\nnames = [\"Анна\", \"Борис\", \"Вера\"]\nmixed = [1, \"два\", 3.0, True]\n```\n\n### Доступ по индексу\n```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nprint(fruits[0])   # яблоко\nprint(fruits[-1])  # вишня\nprint(len(fruits)) # 3\n```\n\n### Изменение элементов\n```python\nfruits[1] = \"апельсин\"\nprint(fruits)  # ['яблоко', 'апельсин', 'вишня']\n```\n\n### Срезы (как у строк)\n```python\nnums = [10, 20, 30, 40, 50]\nprint(nums[1:3])  # [20, 30]\nprint(nums[:2])   # [10, 20]\n```"},
                    {"type": "python-coding", "prompt": "Создайте список colors = [\"красный\", \"зелёный\", \"синий\"]. Выведите второй элемент.", "starterCode": "# Создайте список\n\n# Выведите второй элемент (индекс 1)\n", "expectedOutput": "зелёный", "hint": "colors = [\"красный\", \"зелёный\", \"синий\"]\\nprint(colors[1])"},
                    {"type": "python-coding", "prompt": "Выведите длину списка [10, 20, 30, 40, 50]", "starterCode": "nums = [10, 20, 30, 40, 50]\n# Выведите длину\n", "expectedOutput": "5", "hint": "print(len(nums))"},
                    {"type": "python-coding", "prompt": "Измените третий элемент (индекс 2) списка на \"Python\" и выведите весь список", "starterCode": "langs = [\"Java\", \"C++\", \"JavaScript\"]\n# Замените третий элемент\n\nprint(langs)\n", "expectedOutput": "['Java', 'C++', 'Python']", "hint": "langs[2] = \"Python\""},
                    {"type": "quiz", "question": "Что вернёт len([1, [2, 3], 4])?", "options": [{"id": "a", "text": "4", "correct": False}, {"id": "b", "text": "3", "correct": True}, {"id": "c", "text": "5", "correct": False}, {"id": "d", "text": "2", "correct": False}]},
                    {"type": "python-coding", "prompt": "Выведите последние два элемента списка [5, 10, 15, 20, 25] используя срез", "starterCode": "nums = [5, 10, 15, 20, 25]\n# Выведите последние 2 элемента\n", "expectedOutput": "[20, 25]", "hint": "print(nums[-2:])"}
                ]
            },
            {
                "title": "Методы списков",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Методы списков", "markdown": "## Основные методы\n\n```python\nnums = [3, 1, 4]\n\nnums.append(5)     # Добавить в конец → [3, 1, 4, 5]\nnums.insert(0, 9)  # Вставить по индексу → [9, 3, 1, 4, 5]\nnums.pop()         # Удалить последний → [9, 3, 1, 4]\nnums.pop(0)        # Удалить по индексу → [3, 1, 4]\nnums.remove(1)     # Удалить по значению → [3, 4]\n```\n\n### Сортировка и переворот\n```python\nnums = [3, 1, 4, 1, 5]\nnums.sort()        # [1, 1, 3, 4, 5] — на месте\nnums.reverse()     # [5, 4, 3, 1, 1] — на месте\n\n# Или без изменения оригинала:\nsorted_nums = sorted([3, 1, 2])  # [1, 2, 3]\n```\n\n### Другие полезные методы\n```python\nnums = [1, 2, 2, 3]\nprint(nums.count(2))  # 2\nprint(nums.index(3))  # 3\n```"},
                    {"type": "python-coding", "prompt": "Создайте пустой список, добавьте в него числа 10, 20, 30 с помощью append и выведите список", "starterCode": "nums = []\n# Добавьте 10, 20, 30\n\nprint(nums)\n", "expectedOutput": "[10, 20, 30]", "hint": "nums.append(10)\\nnums.append(20)\\nnums.append(30)"},
                    {"type": "python-coding", "prompt": "Отсортируйте список [5, 2, 8, 1, 9] и выведите его", "starterCode": "nums = [5, 2, 8, 1, 9]\n# Отсортируйте\n\nprint(nums)\n", "expectedOutput": "[1, 2, 5, 8, 9]", "hint": "nums.sort()"},
                    {"type": "python-coding", "prompt": "Удалите последний элемент из списка [\"a\", \"b\", \"c\", \"d\"] и выведите список", "starterCode": "letters = [\"a\", \"b\", \"c\", \"d\"]\n# Удалите последний элемент\n\nprint(letters)\n", "expectedOutput": "['a', 'b', 'c']", "hint": "letters.pop()"},
                    {"type": "quiz", "question": "Чем отличается sort() от sorted()?", "options": [{"id": "a", "text": "sort() меняет список на месте, sorted() возвращает новый", "correct": True}, {"id": "b", "text": "Они идентичны", "correct": False}, {"id": "c", "text": "sorted() быстрее", "correct": False}, {"id": "d", "text": "sort() работает только с числами", "correct": False}]},
                    {"type": "python-coding", "prompt": "Переверните список [1, 2, 3, 4, 5] и выведите его", "starterCode": "nums = [1, 2, 3, 4, 5]\n# Переверните список\n\nprint(nums)\n", "expectedOutput": "[5, 4, 3, 2, 1]", "hint": "nums.reverse()"}
                ]
            },
            {
                "title": "Списковые включения",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "List Comprehension", "markdown": "## Списковые включения (List Comprehension)\n\nКомпактный способ создать список:\n```python\n# Обычный способ\nsquares = []\nfor x in range(5):\n    squares.append(x ** 2)\n\n# List comprehension\nsquares = [x ** 2 for x in range(5)]\n# [0, 1, 4, 9, 16]\n```\n\n### С условием\n```python\n# Только чётные\nevens = [x for x in range(10) if x % 2 == 0]\n# [0, 2, 4, 6, 8]\n```\n\n### Преобразование\n```python\nwords = [\"hello\", \"world\"]\nupper_words = [w.upper() for w in words]\n# ['HELLO', 'WORLD']\n```"},
                    {"type": "python-coding", "prompt": "Создайте список квадратов чисел от 1 до 5 с помощью list comprehension и выведите его", "starterCode": "# [x**2 for x in range(...)]\n", "expectedOutput": "[1, 4, 9, 16, 25]", "hint": "squares = [x**2 for x in range(1, 6)]\\nprint(squares)"},
                    {"type": "python-coding", "prompt": "Создайте список чётных чисел от 1 до 20 используя list comprehension с условием", "starterCode": "# Используйте if x % 2 == 0\n", "expectedOutput": "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]", "hint": "evens = [x for x in range(1, 21) if x % 2 == 0]\\nprint(evens)"},
                    {"type": "quiz", "question": "Что вернёт [x*2 for x in [1,2,3]]?", "options": [{"id": "a", "text": "[1, 2, 3, 1, 2, 3]", "correct": False}, {"id": "b", "text": "[2, 4, 6]", "correct": True}, {"id": "c", "text": "[1, 4, 9]", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]},
                    {"type": "python-coding", "prompt": "Преобразуйте список [\"python\", \"java\", \"go\"] в верхний регистр с помощью list comprehension", "starterCode": "langs = [\"python\", \"java\", \"go\"]\n# Преобразуйте в верхний регистр\n", "expectedOutput": "['PYTHON', 'JAVA', 'GO']", "hint": "result = [lang.upper() for lang in langs]\\nprint(result)"},
                    {"type": "python-coding", "prompt": "Из списка [1, -2, 3, -4, 5] оставьте только положительные числа", "starterCode": "nums = [1, -2, 3, -4, 5]\n# Отфильтруйте положительные\n", "expectedOutput": "[1, 3, 5]", "hint": "positive = [x for x in nums if x > 0]\\nprint(positive)"}
                ]
            }
        ]
    },
    # ==================== SECTION 7: Функции ====================
    {
        "title": "Функции",
        "lessons": [
            {
                "title": "def и return",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Создание функций", "markdown": "## Функции\n\nФункция — блок кода, который можно вызывать многократно:\n```python\ndef greet():\n    print(\"Привет!\")\n\ngreet()  # Привет!\ngreet()  # Привет!\n```\n\n### return — возврат значения\n```python\ndef add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8\n```\n\n### Важно\n- `def` — ключевое слово для создания функции\n- Тело функции с отступом\n- `return` возвращает результат и завершает функцию\n- Без `return` функция возвращает `None`"},
                    {"type": "python-coding", "prompt": "Создайте функцию hello(), которая выводит \"Привет, мир!\". Вызовите её.", "starterCode": "# Определите функцию\n\n# Вызовите её\n", "expectedOutput": "Привет, мир!", "hint": "def hello():\\n    print(\"Привет, мир!\")\\nhello()"},
                    {"type": "python-coding", "prompt": "Создайте функцию square(n), которая возвращает n ** 2. Выведите square(7).", "starterCode": "# Определите функцию square\n\n# Вызовите и выведите результат\n", "expectedOutput": "49", "hint": "def square(n):\\n    return n ** 2\\nprint(square(7))"},
                    {"type": "python-coding", "prompt": "Создайте функцию is_even(n), которая возвращает True если n чётное, иначе False. Выведите is_even(4) и is_even(7).", "starterCode": "# Определите функцию is_even\n\nprint(is_even(4))\nprint(is_even(7))\n", "expectedOutput": "True\nFalse", "hint": "def is_even(n):\\n    return n % 2 == 0"},
                    {"type": "quiz", "question": "Что вернёт функция без оператора return?", "options": [{"id": "a", "text": "0", "correct": False}, {"id": "b", "text": "\"\"", "correct": False}, {"id": "c", "text": "None", "correct": True}, {"id": "d", "text": "Ошибку", "correct": False}]},
                    {"type": "python-coding", "prompt": "Создайте функцию max_of_two(a, b), которая возвращает большее из двух чисел. Выведите max_of_two(10, 25).", "starterCode": "# Определите функцию\n\nprint(max_of_two(10, 25))\n", "expectedOutput": "25", "hint": "def max_of_two(a, b):\\n    if a > b:\\n        return a\\n    return b"}
                ]
            },
            {
                "title": "Параметры и аргументы",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Параметры функций", "markdown": "## Параметры и аргументы\n\n**Параметр** — переменная в определении функции.\n**Аргумент** — значение при вызове.\n\n```python\ndef greet(name):       # name — параметр\n    print(f\"Привет, {name}!\")\n\ngreet(\"Мария\")          # \"Мария\" — аргумент\n```\n\n### Несколько параметров\n```python\ndef power(base, exp):\n    return base ** exp\n\nprint(power(2, 10))  # 1024\n```\n\n### Именованные аргументы\n```python\ndef info(name, age):\n    print(f\"{name}, {age} лет\")\n\ninfo(age=30, name=\"Борис\")  # Порядок не важен\n```"},
                    {"type": "python-coding", "prompt": "Создайте функцию greet(name), которая выводит \"Привет, {name}!\". Вызовите с аргументом \"Анна\".", "starterCode": "# Определите функцию\n\n# Вызовите\n", "expectedOutput": "Привет, Анна!", "hint": "def greet(name):\\n    print(f\"Привет, {name}!\")\\ngreet(\"Анна\")"},
                    {"type": "python-coding", "prompt": "Создайте функцию multiply(a, b), которая возвращает произведение. Выведите multiply(6, 7).", "starterCode": "# Определите функцию\n\nprint(multiply(6, 7))\n", "expectedOutput": "42", "hint": "def multiply(a, b):\\n    return a * b"},
                    {"type": "python-coding", "prompt": "Создайте функцию full_name(first, last), которая возвращает строку \"{first} {last}\". Выведите full_name(\"Иван\", \"Сидоров\").", "starterCode": "# Определите функцию\n\nprint(full_name(\"Иван\", \"Сидоров\"))\n", "expectedOutput": "Иван Сидоров", "hint": "def full_name(first, last):\\n    return f\"{first} {last}\""},
                    {"type": "quiz", "question": "Можно ли передать аргументы в другом порядке?", "options": [{"id": "a", "text": "Нет, только в порядке определения", "correct": False}, {"id": "b", "text": "Да, используя именованные аргументы", "correct": True}, {"id": "c", "text": "Только если параметров 2", "correct": False}, {"id": "d", "text": "Да, Python сам разберётся", "correct": False}]},
                    {"type": "python-coding", "prompt": "Создайте функцию describe(name, age, city), которая выводит \"{name}, {age} лет, г. {city}\". Вызовите с именованными аргументами.", "starterCode": "# Определите функцию\n\ndescribe(city=\"Москва\", name=\"Олег\", age=28)\n", "expectedOutput": "Олег, 28 лет, г. Москва", "hint": "def describe(name, age, city):\\n    print(f\"{name}, {age} лет, г. {city}\")"}
                ]
            },
            {
                "title": "Значения по умолчанию и *args",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Значения по умолчанию", "markdown": "## Значения по умолчанию\n\nПараметр может иметь значение по умолчанию:\n```python\ndef greet(name=\"мир\"):\n    print(f\"Привет, {name}!\")\n\ngreet()         # Привет, мир!\ngreet(\"Алиса\")  # Привет, Алиса!\n```\n\n### *args — произвольное число аргументов\n```python\ndef sum_all(*args):\n    return sum(args)\n\nprint(sum_all(1, 2, 3))       # 6\nprint(sum_all(10, 20, 30, 40))  # 100\n```\n\n`*args` собирает все позиционные аргументы в кортеж (tuple).\n\n### Комбинирование\n```python\ndef log(message, *values):\n    print(f\"{message}: {values}\")\n\nlog(\"Числа\", 1, 2, 3)  # Числа: (1, 2, 3)\n```"},
                    {"type": "python-coding", "prompt": "Создайте функцию power(base, exp=2), которая возвращает base**exp. Выведите power(5) и power(2, 10).", "starterCode": "# Определите функцию с параметром по умолчанию\n\nprint(power(5))\nprint(power(2, 10))\n", "expectedOutput": "25\n1024", "hint": "def power(base, exp=2):\\n    return base ** exp"},
                    {"type": "python-coding", "prompt": "Создайте функцию sum_all(*args), которая возвращает сумму всех аргументов. Выведите sum_all(1, 2, 3, 4, 5).", "starterCode": "# Определите функцию с *args\n\nprint(sum_all(1, 2, 3, 4, 5))\n", "expectedOutput": "15", "hint": "def sum_all(*args):\\n    return sum(args)"},
                    {"type": "quiz", "question": "Какой тип имеет *args внутри функции?", "options": [{"id": "a", "text": "list", "correct": False}, {"id": "b", "text": "tuple", "correct": True}, {"id": "c", "text": "dict", "correct": False}, {"id": "d", "text": "set", "correct": False}]},
                    {"type": "python-coding", "prompt": "Создайте функцию repeat(text, times=3), которая возвращает text повторённый times раз. Выведите repeat(\"Ха\").", "starterCode": "# Определите функцию\n\nprint(repeat(\"Ха\"))\n", "expectedOutput": "ХаХаХа", "hint": "def repeat(text, times=3):\\n    return text * times"},
                    {"type": "python-coding", "prompt": "Создайте функцию find_max(*args), которая возвращает максимум из переданных чисел (без использования встроенной max). Выведите find_max(3, 7, 2, 9, 1).", "starterCode": "def find_max(*args):\n    # Найдите максимум перебором\n    pass\n\nprint(find_max(3, 7, 2, 9, 1))\n", "expectedOutput": "9", "hint": "result = args[0]\\nfor x in args:\\n    if x > result:\\n        result = x\\nreturn result"}
                ]
            },
            {
                "title": "Лямбда-функции",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Лямбда-функции", "markdown": "## lambda — анонимные функции\n\nОднострочная функция без имени:\n```python\n# Обычная функция\ndef double(x):\n    return x * 2\n\n# Лямбда-эквивалент\ndouble = lambda x: x * 2\nprint(double(5))  # 10\n```\n\n### Применение\nЧаще всего lambda используются с `sorted()`, `map()`, `filter()`:\n```python\n# Сортировка по второму элементу\npairs = [(1, 'b'), (2, 'a'), (3, 'c')]\nsorted_pairs = sorted(pairs, key=lambda p: p[1])\n# [(2, 'a'), (1, 'b'), (3, 'c')]\n```\n\n```python\n# map — применить функцию к каждому элементу\nnums = [1, 2, 3, 4]\nsquares = list(map(lambda x: x**2, nums))\n# [1, 4, 9, 16]\n```"},
                    {"type": "python-coding", "prompt": "Создайте лямбда-функцию add, которая принимает два числа и возвращает их сумму. Выведите add(3, 4).", "starterCode": "# add = lambda ...\n\nprint(add(3, 4))\n", "expectedOutput": "7", "hint": "add = lambda a, b: a + b"},
                    {"type": "python-coding", "prompt": "Отсортируйте список слов [\"банан\", \"яблоко\", \"вишня\"] по длине (используя sorted и lambda). Выведите результат.", "starterCode": "words = [\"банан\", \"яблоко\", \"вишня\"]\n# Отсортируйте по длине слова\n", "expectedOutput": "['банан', 'вишня', 'яблоко']", "hint": "print(sorted(words, key=lambda w: len(w)))"},
                    {"type": "python-coding", "prompt": "Используя map и lambda, удвойте каждый элемент списка [1, 2, 3, 4, 5]. Выведите результат как список.", "starterCode": "nums = [1, 2, 3, 4, 5]\n# Используйте map() и lambda\n", "expectedOutput": "[2, 4, 6, 8, 10]", "hint": "print(list(map(lambda x: x * 2, nums)))"},
                    {"type": "quiz", "question": "Сколько выражений может содержать тело lambda?", "options": [{"id": "a", "text": "Сколько угодно", "correct": False}, {"id": "b", "text": "Только одно", "correct": True}, {"id": "c", "text": "Максимум 3", "correct": False}, {"id": "d", "text": "Ни одного", "correct": False}]},
                    {"type": "python-coding", "prompt": "Используя filter и lambda, оставьте только чётные числа из списка [1, 2, 3, 4, 5, 6, 7, 8]. Выведите результат.", "starterCode": "nums = [1, 2, 3, 4, 5, 6, 7, 8]\n# Используйте filter() и lambda\n", "expectedOutput": "[2, 4, 6, 8]", "hint": "print(list(filter(lambda x: x % 2 == 0, nums)))"}
                ]
            }
        ]
    },
    # ==================== SECTION 8: Словари и финал ====================
    {
        "title": "Словари и финал",
        "lessons": [
            {
                "title": "Словари",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Словари (dict)", "markdown": "## Словари\n\nСловарь хранит пары **ключ: значение**:\n```python\nperson = {\n    \"name\": \"Алиса\",\n    \"age\": 25,\n    \"city\": \"Москва\"\n}\n\nprint(person[\"name\"])  # Алиса\n```\n\n### Основные операции\n```python\n# Добавить/изменить\nperson[\"email\"] = \"alice@mail.ru\"\nperson[\"age\"] = 26\n\n# Удалить\ndel person[\"email\"]\n\n# Проверить наличие ключа\nprint(\"name\" in person)  # True\n```\n\n### Методы\n```python\nprint(person.keys())    # dict_keys(['name', 'age', 'city'])\nprint(person.values())  # dict_values(['Алиса', 26, 'Москва'])\nprint(person.items())   # пары (ключ, значение)\nprint(person.get(\"phone\", \"Нет\"))  # Нет (безопасный доступ)\n```"},
                    {"type": "python-coding", "prompt": "Создайте словарь car с ключами: brand=\"Toyota\", year=2020, color=\"белый\". Выведите значение по ключу \"brand\".", "starterCode": "# Создайте словарь\n\n# Выведите brand\n", "expectedOutput": "Toyota", "hint": "car = {\"brand\": \"Toyota\", \"year\": 2020, \"color\": \"белый\"}\\nprint(car[\"brand\"])"},
                    {"type": "python-coding", "prompt": "Добавьте к словарю student = {\"name\": \"Иван\"} ключ \"grade\" со значением 5. Выведите словарь.", "starterCode": "student = {\"name\": \"Иван\"}\n# Добавьте ключ grade\n\nprint(student)\n", "expectedOutput": "{'name': 'Иван', 'grade': 5}", "hint": "student[\"grade\"] = 5"},
                    {"type": "python-coding", "prompt": "Выведите все ключи словаря {\"a\": 1, \"b\": 2, \"c\": 3} с помощью цикла for, каждый на новой строке", "starterCode": "d = {\"a\": 1, \"b\": 2, \"c\": 3}\n# Пройдите по ключам\n", "expectedOutput": "a\nb\nc", "hint": "for key in d:\\n    print(key)"},
                    {"type": "quiz", "question": "Что произойдёт при обращении к несуществующему ключу через []?", "options": [{"id": "a", "text": "Вернёт None", "correct": False}, {"id": "b", "text": "KeyError", "correct": True}, {"id": "c", "text": "Вернёт 0", "correct": False}, {"id": "d", "text": "Создаст ключ", "correct": False}]},
                    {"type": "python-coding", "prompt": "Используя .get(), получите значение по ключу \"phone\" из словаря {\"name\": \"Вера\"}, если ключа нет — верните \"Не указан\". Выведите результат.", "starterCode": "person = {\"name\": \"Вера\"}\n# Используйте .get() с значением по умолчанию\n", "expectedOutput": "Не указан", "hint": "print(person.get(\"phone\", \"Не указан\"))"}
                ]
            },
            {
                "title": "Вложенные структуры",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Вложенные структуры", "markdown": "## Списки в словарях\n\n```python\nstudent = {\n    \"name\": \"Борис\",\n    \"grades\": [5, 4, 5, 3, 5]\n}\nprint(student[\"grades\"][0])  # 5\nprint(sum(student[\"grades\"]) / len(student[\"grades\"]))  # 4.4\n```\n\n## Словари в списках\n```python\nusers = [\n    {\"name\": \"Анна\", \"age\": 22},\n    {\"name\": \"Борис\", \"age\": 30},\n    {\"name\": \"Вера\", \"age\": 25}\n]\nfor user in users:\n    print(f\"{user['name']}: {user['age']}\")\n```\n\n## Словари в словарях\n```python\ncompany = {\n    \"ceo\": {\"name\": \"Иван\", \"age\": 45},\n    \"cto\": {\"name\": \"Мария\", \"age\": 38}\n}\nprint(company[\"cto\"][\"name\"])  # Мария\n```"},
                    {"type": "python-coding", "prompt": "Создайте словарь student с ключами name=\"Мария\" и grades=[5, 4, 5, 5, 4]. Выведите третью оценку.", "starterCode": "# Создайте словарь\n\n# Выведите третью оценку (индекс 2)\n", "expectedOutput": "5", "hint": "student = {\"name\": \"Мария\", \"grades\": [5, 4, 5, 5, 4]}\\nprint(student[\"grades\"][2])"},
                    {"type": "python-coding", "prompt": "Дан список users. Выведите имя каждого пользователя на отдельной строке.", "starterCode": "users = [\n    {\"name\": \"Анна\", \"age\": 22},\n    {\"name\": \"Борис\", \"age\": 30},\n    {\"name\": \"Вера\", \"age\": 25}\n]\n# Выведите имена\n", "expectedOutput": "Анна\nБорис\nВера", "hint": "for user in users:\\n    print(user[\"name\"])"},
                    {"type": "quiz", "question": "Как получить значение company[\"cto\"][\"name\"] если ключа \"cto\" может не быть?", "options": [{"id": "a", "text": "company.get(\"cto\", {})[\"name\"]", "correct": False}, {"id": "b", "text": "company.get(\"cto\", {}).get(\"name\", \"\")", "correct": True}, {"id": "c", "text": "company[\"cto\"].get(\"name\")", "correct": False}, {"id": "d", "text": "try/except", "correct": False}]},
                    {"type": "python-coding", "prompt": "Посчитайте общее количество оценок 5 у всех студентов и выведите число.", "starterCode": "students = [\n    {\"name\": \"Аня\", \"grades\": [5, 4, 5]},\n    {\"name\": \"Боря\", \"grades\": [3, 5, 5, 5]},\n    {\"name\": \"Вова\", \"grades\": [4, 4, 5]}\n]\ncount = 0\n# Посчитайте пятёрки\n\nprint(count)\n", "expectedOutput": "5", "hint": "for s in students:\\n    count += s[\"grades\"].count(5)"}
                ]
            },
            {
                "title": "Финальный проект",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Финальный проект", "markdown": "## Финальный проект: Телефонная книга\n\nОбъединим всё изученное:\n- Словари (хранение контактов)\n- Списки (коллекция контактов)\n- Функции (логика приложения)\n- Циклы и условия (меню)\n- Строки (вывод данных)\n\n### Задача\nРеализуйте набор функций для работы с телефонной книгой:\n1. Создание контакта\n2. Поиск контакта по имени\n3. Вывод всех контактов\n\nВы уже знаете всё необходимое!"},
                    {"type": "python-coding", "prompt": "Создайте функцию create_contact(name, phone), которая возвращает словарь с ключами \"name\" и \"phone\". Выведите create_contact(\"Анна\", \"+7-999-123-4567\").", "starterCode": "def create_contact(name, phone):\n    # Верните словарь\n    pass\n\nprint(create_contact(\"Анна\", \"+7-999-123-4567\"))\n", "expectedOutput": "{'name': 'Анна', 'phone': '+7-999-123-4567'}", "hint": "return {\"name\": name, \"phone\": phone}"},
                    {"type": "python-coding", "prompt": "Создайте функцию find_contact(contacts, name), которая ищет контакт по имени. Если нашла — возвращает телефон, иначе \"Не найден\".", "starterCode": "def find_contact(contacts, name):\n    # Пройдите по списку и найдите контакт\n    pass\n\nbook = [\n    {\"name\": \"Анна\", \"phone\": \"111\"},\n    {\"name\": \"Борис\", \"phone\": \"222\"},\n    {\"name\": \"Вера\", \"phone\": \"333\"}\n]\nprint(find_contact(book, \"Борис\"))\nprint(find_contact(book, \"Денис\"))\n", "expectedOutput": "222\nНе найден", "hint": "for c in contacts:\\n    if c[\"name\"] == name:\\n        return c[\"phone\"]\\nreturn \"Не найден\""},
                    {"type": "python-coding", "prompt": "Создайте функцию print_contacts(contacts), которая выводит все контакты в формате \"Имя: телефон\". Протестируйте на 3 контактах.", "starterCode": "def print_contacts(contacts):\n    # Выведите каждый контакт\n    pass\n\nbook = [\n    {\"name\": \"Анна\", \"phone\": \"111\"},\n    {\"name\": \"Борис\", \"phone\": \"222\"},\n    {\"name\": \"Вера\", \"phone\": \"333\"}\n]\nprint_contacts(book)\n", "expectedOutput": "Анна: 111\nБорис: 222\nВера: 333", "hint": "for c in contacts:\\n    print(f\"{c['name']}: {c['phone']}\")"},
                    {"type": "quiz", "question": "Какая структура данных лучше всего подходит для хранения контакта (имя + телефон)?", "options": [{"id": "a", "text": "Список", "correct": False}, {"id": "b", "text": "Словарь", "correct": True}, {"id": "c", "text": "Строка", "correct": False}, {"id": "d", "text": "Число", "correct": False}]},
                    {"type": "python-coding", "prompt": "Объедините всё: создайте 3 контакта с помощью create_contact, добавьте в список book, затем выведите контакты с помощью print_contacts.", "starterCode": "def create_contact(name, phone):\n    return {\"name\": name, \"phone\": phone}\n\ndef print_contacts(contacts):\n    for c in contacts:\n        print(f\"{c['name']}: {c['phone']}\")\n\nbook = []\n# Добавьте 3 контакта в book с помощью append и create_contact\n\n# Выведите все контакты\n", "expectedOutput": "Алиса: +7-111\nБорис: +7-222\nВера: +7-333", "hint": "book.append(create_contact(\"Алиса\", \"+7-111\"))\\nbook.append(create_contact(\"Борис\", \"+7-222\"))\\nbook.append(create_contact(\"Вера\", \"+7-333\"))\\nprint_contacts(book)"},
                    {"type": "info", "title": "Поздравляем!", "markdown": "## Курс завершён!\n\nВы изучили основы Python:\n\n- **print()** и комментарии\n- **Переменные** и типы данных\n- **Строки** — методы, срезы, форматирование\n- **Условия** — if/elif/else, логические операторы\n- **Циклы** — for, while, break, continue\n- **Списки** — методы, list comprehension\n- **Функции** — def, return, *args, lambda\n- **Словари** — вложенные структуры\n\n### Что дальше?\n- Работа с файлами\n- Обработка исключений (try/except)\n- Объектно-ориентированное программирование (ООП)\n- Библиотеки: requests, pandas, flask\n\nУдачи в дальнейшем обучении! 🐍"}
                ]
            }
        ]
    }
]


async def main():
    async with async_session() as db:
        # Find first user (admin)
        r = await db.execute(select(User).limit(1))
        user = r.scalar_one_or_none()
        if not user:
            print("No users found, run seed_production.py first")
            return

        # Check if course exists — delete to recreate
        r = await db.execute(select(Course).where(Course.title == COURSE_TITLE))
        existing = r.scalar_one_or_none()
        if existing:
            await db.delete(existing)
            await db.flush()

        course = Course(
            id=uuid.uuid4(), title=COURSE_TITLE,
            slug="python-junior-" + uuid.uuid4().hex[:6],
            description="Полный курс Python с интерактивными coding-упражнениями. Пишите и запускайте код прямо в браузере!",
            author_id=user.id, category="Programming", difficulty="Beginner",
            price=0, currency="USD", status="published",
            thumbnail_url="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=800&q=80"
        )
        db.add(course)
        await db.flush()

        positions, gidx = [], 0
        total_steps = 0
        for si, section_data in enumerate(SECTIONS):
            sec = CourseSection(id=uuid.uuid4(), course_id=course.id, title=section_data["title"], position=si)
            db.add(sec)
            await db.flush()

            for li, lesson_data in enumerate(section_data["lessons"]):
                total_steps += len(lesson_data["steps"])
                lesson = CourseLesson(
                    id=uuid.uuid4(), section_id=sec.id, title=lesson_data["title"],
                    position=li, content_type="interactive",
                    xp_reward=lesson_data["xp"], steps=lesson_data["steps"]
                )
                db.add(lesson)
                await db.flush()
                positions.append({"id": str(lesson.id), "x": SNAKE_X[gidx % 5] * CANVAS_W, "y": V_PAD + gidx * ROW_H})
                gidx += 1

        edges = [{"id": f"e-{i}", "source": positions[i-1]["id"], "target": positions[i]["id"]} for i in range(1, len(positions))]
        course.roadmap_nodes = positions
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{COURSE_TITLE}': {len(SECTIONS)} sections, {gidx} lessons, {total_steps} steps")


if __name__ == "__main__":
    asyncio.run(main())
