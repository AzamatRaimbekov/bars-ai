"""Seed: Python — с нуля до Junior — 8 sections, 27 lessons with video + coding exercises."""
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
                    {"type": "video", "title": "Python для начинающих — print и переменные", "url": "https://www.youtube.com/watch?v=LFCq-mNF96c"},
                    {"type": "info", "title": "Функция print()", "markdown": "## Функция print()\n\nВ Python для вывода текста на экран используется встроенная функция `print()`.\n\n```python\nprint(\"Привет, мир!\")\n```\n\n### Как это работает?\n1. `print` — имя функции (от англ. *print* — печатать)\n2. `()` — круглые скобки обязательны\n3. Внутри скобок — то, что нужно вывести\n\n### Строки и кавычки\nТекст (строка) заключается в кавычки — двойные `\"\"` или одинарные `''`:\n```python\nprint(\"Привет!\")   # двойные кавычки\nprint('Привет!')   # одинарные — тот же результат\n```\n\n### Несколько print()\nКаждый вызов `print()` выводит текст с **новой строки**:\n```python\nprint(\"Строка 1\")\nprint(\"Строка 2\")\n```\nРезультат:\n```\nСтрока 1\nСтрока 2\n```\n\n### Вывод чисел\nЧисла пишутся **без** кавычек:\n```python\nprint(42)\nprint(3.14)\n```"},
                    {"type": "python-coding", "prompt": "Используя функцию print(), выведите на экран текст: Привет, мир!\n\nВ Python текст (строку) нужно заключить в кавычки внутри print(). Ожидаемый результат:\nПривет, мир!", "starterCode": "# Напишите print() с текстом \"Привет, мир!\"\n", "expectedOutput": "Привет, мир!", "hint": "Напишите: print(\"Привет, мир!\") — текст в двойных кавычках внутри скобок"},
                    {"type": "python-coding", "prompt": "Напишите программу, которая выводит ДВЕ строки (каждая с нового print):\nЯ учу Python\nЭто весело!\n\nКаждый вызов print() выводит текст с новой строки. Вам нужно два вызова print().", "starterCode": "# Первая строка — print(\"Я учу Python\")\n\n# Вторая строка — print(\"Это весело!\")\n", "expectedOutput": "Я учу Python\nЭто весело!", "hint": "Используйте два отдельных print():\nprint(\"Я учу Python\")\nprint(\"Это весело!\")"},
                    {"type": "python-coding", "prompt": "Выведите число 2025 (без кавычек — это число, не строка). В Python числа пишутся без кавычек:\nprint(42) выведет 42\n\nОжидаемый результат: 2025", "starterCode": "# Выведите число 2025\n", "expectedOutput": "2025", "hint": "print(2025) — числа пишутся без кавычек"},
                    {"type": "quiz", "question": "Какая функция выводит текст на экран в Python?", "options": [{"id": "a", "text": "echo()", "correct": False}, {"id": "b", "text": "print()", "correct": True}, {"id": "c", "text": "write()", "correct": False}, {"id": "d", "text": "console.log()", "correct": False}]}
                ]
            },
            {
                "title": "Комментарии в коде",
                "xp": 15,
                "steps": [
                    {"type": "video", "title": "Python за 1 час — основы", "url": "https://www.youtube.com/watch?v=34Rp6KVGIEM"},
                    {"type": "info", "title": "Комментарии в Python", "markdown": "## Комментарии\n\nКомментарии — это заметки для программиста. Python их **полностью игнорирует** при выполнении.\n\n### Однострочный комментарий\nНачинается с символа `#`:\n```python\n# Это комментарий — Python его не выполнит\nprint(\"Привет\")  # Комментарий после кода тоже работает\n```\n\n### Зачем нужны комментарии?\n- Объясняют **зачем** написан код (не *что* он делает, а *почему*)\n- Помогают другим разработчикам понять вашу логику\n- Помогают вам вспомнить код через месяц\n- Позволяют временно «выключить» строку кода\n\n### Закомментировать код\nМожно «выключить» строку, добавив `#` в начало:\n```python\n# print(\"Эта строка НЕ выведется\")\nprint(\"А эта выведется\")\n```\n\n### Многострочные комментарии\nPython не имеет специального синтаксиса для многострочных комментариев, но можно использовать `#` на каждой строке:\n```python\n# Это первая строка комментария\n# Это вторая строка комментария\n```"},
                    {"type": "python-coding", "prompt": "Напишите комментарий на первой строке: # Моя первая программа\nА на второй строке выведите слово Hello с помощью print().\n\nКомментарий начинается с # и Python его проигнорирует. Выполнится только print().\n\nОжидаемый вывод: Hello", "starterCode": "# Напишите комментарий и print ниже\n", "expectedOutput": "Hello", "hint": "Первая строка: # Моя первая программа\nВторая строка: print(\"Hello\")"},
                    {"type": "python-coding", "prompt": "Перед вами две строки с print(). Закомментируйте ПЕРВЫЙ print (добавьте # в начало строки), чтобы вывелось только слово: Мир\n\nЗакомментировать = поставить # перед строкой, тогда Python её пропустит.\n\nОжидаемый вывод: Мир", "starterCode": "print(\"Привет\")\nprint(\"Мир\")\n", "expectedOutput": "Мир", "hint": "Добавьте # перед первым print:\n# print(\"Привет\")\nprint(\"Мир\")"},
                    {"type": "quiz", "question": "Как начинается однострочный комментарий в Python?", "options": [{"id": "a", "text": "//", "correct": False}, {"id": "b", "text": "#", "correct": True}, {"id": "c", "text": "/*", "correct": False}, {"id": "d", "text": "--", "correct": False}]},
                    {"type": "python-coding", "prompt": "Напишите программу из 3 строк:\n1. Комментарий: # Вычисление\n2. print(2 + 2)\n3. Комментарий: # Результат: 4\n\nPython выполнит только строку с print(), комментарии будут пропущены.\n\nОжидаемый вывод: 4", "starterCode": "# Напишите 3 строки: комментарий, print, комментарий\n", "expectedOutput": "4", "hint": "# Вычисление\nprint(2 + 2)\n# Результат: 4"}
                ]
            },
            {
                "title": "Вычисления в print()",
                "xp": 20,
                "steps": [
                    {"type": "video", "title": "Python для начинающих — полный курс", "url": "https://www.youtube.com/watch?v=wDmPgXhlDIg"},
                    {"type": "info", "title": "Математика в Python", "markdown": "## Вычисления в print()\n\nPython — отличный калькулятор! Арифметические выражения можно писать прямо в `print()`:\n\n```python\nprint(2 + 3)   # Сложение → 5\nprint(10 - 4)  # Вычитание → 6\nprint(3 * 7)   # Умножение → 21\nprint(15 // 3) # Целочисленное деление → 5\n```\n\n### Все арифметические операторы\n| Оператор | Действие | Пример | Результат |\n|----------|----------|--------|-----------|\n| `+` | Сложение | `2 + 3` | `5` |\n| `-` | Вычитание | `7 - 2` | `5` |\n| `*` | Умножение | `4 * 3` | `12` |\n| `/` | Деление (дробное) | `7 / 2` | `3.5` |\n| `//` | Целочисленное деление | `7 // 2` | `3` |\n| `%` | Остаток от деления | `7 % 2` | `1` |\n| `**` | Возведение в степень | `2 ** 3` | `8` |\n\n### Порядок операций\nPython соблюдает математический приоритет:\n1. `**` (степень)\n2. `*`, `/`, `//`, `%` (умножение/деление)\n3. `+`, `-` (сложение/вычитание)\n\nСкобки `()` меняют порядок:\n```python\nprint(2 + 3 * 4)    # 14 (сначала умножение)\nprint((2 + 3) * 4)  # 20 (сначала скобки)\n```"},
                    {"type": "python-coding", "prompt": "Используя функцию print(), вычислите и выведите результат сложения 7 + 3.\n\nВ Python арифметические операции можно писать прямо внутри print(). Python вычислит выражение и выведет результат.\n\nОжидаемый результат: 10", "starterCode": "# Выведите результат сложения 7 + 3\n", "expectedOutput": "10", "hint": "Напишите: print(7 + 3)"},
                    {"type": "python-coding", "prompt": "Вычислите 2 в степени 10 (два в десятой степени) и выведите результат.\n\nОператор возведения в степень в Python — это ** (две звёздочки):\nprint(основание ** показатель)\n\nОжидаемый результат: 1024", "starterCode": "# Оператор возведения в степень: **\n# Пример: 3 ** 2 = 9\n", "expectedOutput": "1024", "hint": "print(2 ** 10) — два в десятой степени равно 1024"},
                    {"type": "python-coding", "prompt": "Найдите остаток от деления 17 на 5.\n\nОператор % (процент) даёт остаток от деления:\n10 % 3 = 1 (потому что 10 = 3*3 + 1)\n\n17 делится на 5: 17 = 5*3 + 2, значит остаток = 2\n\nОжидаемый результат: 2", "starterCode": "# Оператор остатка от деления: %\n", "expectedOutput": "2", "hint": "print(17 % 5) — остаток от деления 17 на 5"},
                    {"type": "python-coding", "prompt": "Выведите результат выражения: (10 + 5) * 2\n\nСкобки меняют порядок вычислений — сначала выполняется то, что в скобках (10+5=15), а потом умножение (15*2=30).\n\nОжидаемый результат: 30", "starterCode": "# Скобки меняют порядок вычислений\n", "expectedOutput": "30", "hint": "print((10 + 5) * 2)"},
                    {"type": "quiz", "question": "Что выведет print(7 // 2)?", "options": [{"id": "a", "text": "3.5", "correct": False}, {"id": "b", "text": "3", "correct": True}, {"id": "c", "text": "4", "correct": False}, {"id": "d", "text": "2", "correct": False}]}
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
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Типы данных Python", "url": "https://www.youtube.com/watch?v=DZvNZ9l9NT4"},
                    {"type": "info", "title": "Переменные в Python", "markdown": "## Переменные\n\nПеременная — это **имя**, которое ссылается на значение в памяти.\n\n```python\nname = \"Алиса\"\nage = 25\nprint(name)  # Алиса\nprint(age)   # 25\n```\n\n### Правила именования\n- Начинается с буквы или `_`\n- Содержит буквы, цифры, `_`\n- **Регистр важен**: `Name` и `name` — разные переменные\n- Нельзя использовать зарезервированные слова (`if`, `for`, `print` и т.д.)\n\n### Присваивание\nЗнак `=` — это оператор **присваивания** (не равенства!):\n```python\nx = 10       # создаём переменную x со значением 10\nx = 20       # перезаписываем — теперь x = 20\ny = x + 5    # y = 25\n```\n\n### Множественное присваивание\n```python\na, b, c = 1, 2, 3\nprint(a)  # 1\nprint(b)  # 2\n```\n\n### Вывод переменных\n```python\ncity = \"Москва\"\nprint(city)         # Москва\nprint(\"Город:\", city)  # Город: Москва\n```"},
                    {"type": "python-coding", "prompt": "Создайте переменную name со значением \"Python\" и выведите её с помощью print().\n\nШаги:\n1. Напишите: name = \"Python\" (присвоить значение)\n2. Напишите: print(name) (вывести значение переменной)\n\nОбратите внимание: при выводе переменной кавычки НЕ нужны — print(name), а не print(\"name\").\n\nОжидаемый вывод: Python", "starterCode": "# Создайте переменную name\n\n# Выведите её значение\n", "expectedOutput": "Python", "hint": "name = \"Python\"\nprint(name)"},
                    {"type": "python-coding", "prompt": "Создайте две переменные:\n- a = 15\n- b = 7\n\nВыведите их сумму с помощью print(a + b).\n\nPython подставит значения переменных и вычислит результат: 15 + 7 = 22\n\nОжидаемый вывод: 22", "starterCode": "# Создайте переменные a и b\n\n\n# Выведите их сумму\n", "expectedOutput": "22", "hint": "a = 15\nb = 7\nprint(a + b)"},
                    {"type": "python-coding", "prompt": "Создайте переменную price = 100, затем переменную quantity = 3.\nВычислите total = price * quantity и выведите total.\n\nОжидаемый вывод: 300", "starterCode": "# Цена и количество\n\n\n# Вычислите итого\n\n# Выведите результат\n", "expectedOutput": "300", "hint": "price = 100\nquantity = 3\ntotal = price * quantity\nprint(total)"},
                    {"type": "quiz", "question": "Что выведет код?\nx = 5\nx = x + 3\nprint(x)", "options": [{"id": "a", "text": "5", "correct": False}, {"id": "b", "text": "3", "correct": False}, {"id": "c", "text": "8", "correct": True}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            },
            {
                "title": "Типы данных: int, float, str",
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Типы данных Python", "url": "https://www.youtube.com/watch?v=DZvNZ9l9NT4"},
                    {"type": "info", "title": "Основные типы данных", "markdown": "## Типы данных в Python\n\nКаждое значение в Python имеет **тип**. Основные типы:\n\n### int — целое число\n```python\nage = 25\nyear = 2025\nnegative = -10\n```\n\n### float — дробное число (с точкой)\n```python\npi = 3.14\ntemperature = -2.5\nprice = 99.0  # тоже float, хоть и «целое»\n```\n\n### str — строка (текст)\n```python\nname = \"Алиса\"\ngreeting = 'Привет!'\nempty = \"\"  # пустая строка\n```\n\n### bool — логический тип\n```python\nis_active = True\nis_empty = False\n```\n\n### Проверка типа — type()\n```python\nprint(type(42))       # <class 'int'>\nprint(type(3.14))     # <class 'float'>\nprint(type(\"Hi\"))     # <class 'str'>\nprint(type(True))     # <class 'bool'>\n```\n\n### Преобразование типов\n```python\nint(\"5\")     # строка → число: 5\nstr(42)      # число → строка: \"42\"\nfloat(7)     # целое → дробное: 7.0\n```"},
                    {"type": "python-coding", "prompt": "Создайте три переменные разных типов:\n- age = 20 (целое число int)\n- height = 175 (целое число)\n- name = \"Студент\" (строка str)\n\nВыведите тип переменной age с помощью print(type(age)).\n\nФункция type() возвращает тип данных значения.\n\nОжидаемый вывод: <class 'int'>", "starterCode": "# Создайте переменные\n\n\n\n# Выведите тип age\n", "expectedOutput": "<class 'int'>", "hint": "age = 20\nheight = 175\nname = \"Студент\"\nprint(type(age))"},
                    {"type": "python-coding", "prompt": "Преобразуйте строку \"123\" в число и прибавьте к нему 7. Выведите результат.\n\nФункция int() преобразует строку в целое число:\nint(\"123\") → 123\n\nЗатем можно складывать: int(\"123\") + 7\n\nОжидаемый вывод: 130", "starterCode": "# Преобразуйте строку в число и прибавьте 7\ntext = \"123\"\n\n", "expectedOutput": "130", "hint": "text = \"123\"\nprint(int(text) + 7)"},
                    {"type": "python-coding", "prompt": "Создайте переменную x = 7. Выведите результат x * 3 через print().\n\nОжидаемый вывод: 21", "starterCode": "# Создайте x и выведите x * 3\n", "expectedOutput": "21", "hint": "x = 7\nprint(x * 3)"},
                    {"type": "quiz", "question": "Какой тип у значения \"100\"?", "options": [{"id": "a", "text": "int", "correct": False}, {"id": "b", "text": "float", "correct": False}, {"id": "c", "text": "str", "correct": True}, {"id": "d", "text": "bool", "correct": False}]}
                ]
            },
            {
                "title": "Ввод данных — input()",
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Python для начинающих — print и переменные", "url": "https://www.youtube.com/watch?v=LFCq-mNF96c"},
                    {"type": "info", "title": "Функция input()", "markdown": "## Ввод данных с клавиатуры\n\nФункция `input()` позволяет пользователю ввести данные:\n```python\nname = input(\"Как вас зовут? \")\nprint(\"Привет,\", name)\n```\n\n### Важно: input() всегда возвращает строку!\n```python\nage = input(\"Возраст: \")  # age — это строка \"25\", не число 25\nprint(type(age))  # <class 'str'>\n```\n\n### Преобразование ввода в число\n```python\nage = int(input(\"Возраст: \"))    # строку → в целое число\nweight = float(input(\"Вес: \"))   # строку → в дробное число\n```\n\n### Пример программы\n```python\nnum1 = int(input(\"Первое число: \"))\nnum2 = int(input(\"Второе число: \"))\nprint(\"Сумма:\", num1 + num2)\n```\n\n### f-строки для красивого вывода\n```python\nname = \"Мир\"\nprint(f\"Привет, {name}!\")  # Привет, Мир!\n\nage = 20\nprint(f\"Мне {age} лет\")   # Мне 20 лет\n```"},
                    {"type": "python-coding", "prompt": "Используя f-строку (f-string), выведите сообщение с переменной.\n\nСоздайте переменную language = \"Python\" и выведите:\nЯ изучаю Python\n\nF-строка: print(f\"Я изучаю {language}\")\nВнутри {} подставляется значение переменной.\n\nОжидаемый вывод: Я изучаю Python", "starterCode": "# Создайте переменную language\n\n# Выведите с помощью f-строки\n", "expectedOutput": "Я изучаю Python", "hint": "language = \"Python\"\nprint(f\"Я изучаю {language}\")"},
                    {"type": "python-coding", "prompt": "Создайте две переменные: a = 10 и b = 3.\nВыведите строку: 10 + 3 = 13\n\nИспользуйте f-строку: print(f\"{a} + {b} = {a + b}\")\nВнутри {} можно писать выражения!\n\nОжидаемый вывод: 10 + 3 = 13", "starterCode": "# Создайте переменные a и b\n\n\n# Выведите с помощью f-строки\n", "expectedOutput": "10 + 3 = 13", "hint": "a = 10\nb = 3\nprint(f\"{a} + {b} = {a + b}\")"},
                    {"type": "python-coding", "prompt": "Создайте переменные:\nname = \"Алиса\"\nage = 20\n\nВыведите: Алиса, 20 лет\n\nИспользуйте f-строку с двумя переменными.\n\nОжидаемый вывод: Алиса, 20 лет", "starterCode": "# Переменные\n\n\n# Вывод с f-строкой\n", "expectedOutput": "Алиса, 20 лет", "hint": "name = \"Алиса\"\nage = 20\nprint(f\"{name}, {age} лет\")"},
                    {"type": "quiz", "question": "Что возвращает input() в Python?", "options": [{"id": "a", "text": "Всегда число (int)", "correct": False}, {"id": "b", "text": "Всегда строку (str)", "correct": True}, {"id": "c", "text": "Зависит от ввода пользователя", "correct": False}, {"id": "d", "text": "Логическое значение (bool)", "correct": False}]}
                ]
            },
            {
                "title": "Операции со строками",
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Строки в Python", "url": "https://www.youtube.com/watch?v=8q2-MBQf58o"},
                    {"type": "info", "title": "Строковые операции", "markdown": "## Операции со строками\n\n### Конкатенация (склеивание)\nОператор `+` соединяет строки:\n```python\nfirst = \"Привет\"\nsecond = \" мир\"\nresult = first + second\nprint(result)  # Привет мир\n```\n\n### Повторение строки\nОператор `*` повторяет строку:\n```python\nprint(\"Ха\" * 3)   # ХаХаХа\nprint(\"-\" * 20)    # --------------------\n```\n\n### Длина строки — len()\n```python\nword = \"Python\"\nprint(len(word))  # 6\n```\n\n### Индексация (доступ к символу)\nСимволы нумеруются с 0:\n```python\nword = \"Python\"\nprint(word[0])   # P\nprint(word[1])   # y\nprint(word[-1])  # n (последний символ)\n```\n\n### Срезы (slicing)\n```python\nword = \"Python\"\nprint(word[0:3])  # Pyt (символы 0, 1, 2)\nprint(word[2:])   # thon (от 2 до конца)\nprint(word[:4])   # Pyth (от начала до 3)\n```\n\n### Методы строк\n```python\ntext = \"hello world\"\nprint(text.upper())       # HELLO WORLD\nprint(text.capitalize())  # Hello world\nprint(text.count(\"l\"))    # 3\n```"},
                    {"type": "python-coding", "prompt": "Создайте переменную word = \"Python\" и выведите её длину с помощью len().\n\nФункция len() возвращает количество символов в строке:\nlen(\"Hello\") = 5\n\nОжидаемый вывод: 6", "starterCode": "# Создайте переменную word\n\n# Выведите её длину\n", "expectedOutput": "6", "hint": "word = \"Python\"\nprint(len(word))"},
                    {"type": "python-coding", "prompt": "Используя оператор * повторите строку \"Ha\" 4 раза и выведите результат.\n\nОператор * повторяет строку: \"Ab\" * 3 даст \"AbAbAb\"\n\nОжидаемый вывод: HaHaHaHa", "starterCode": "# Повторите строку \"Ha\" четыре раза\n", "expectedOutput": "HaHaHaHa", "hint": "print(\"Ha\" * 4)"},
                    {"type": "python-coding", "prompt": "Создайте переменную text = \"Hello, World!\" и выведите первый символ (индекс 0).\n\nИндексация: text[0] — первый символ, text[1] — второй и т.д.\n\nОжидаемый вывод: H", "starterCode": "# Создайте text и выведите первый символ\n", "expectedOutput": "H", "hint": "text = \"Hello, World!\"\nprint(text[0])"},
                    {"type": "python-coding", "prompt": "Создайте greeting = \"hello\" и выведите greeting.upper() — строку в верхнем регистре.\n\nМетод .upper() возвращает новую строку, где все буквы заглавные.\n\nОжидаемый вывод: HELLO", "starterCode": "# Создайте greeting и выведите в верхнем регистре\n", "expectedOutput": "HELLO", "hint": "greeting = \"hello\"\nprint(greeting.upper())"},
                    {"type": "quiz", "question": "Что выведет print(\"abc\"[1])?", "options": [{"id": "a", "text": "a", "correct": False}, {"id": "b", "text": "b", "correct": True}, {"id": "c", "text": "c", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 3: Условия — if/elif/else ====================
    {
        "title": "Условия: if / elif / else",
        "lessons": [
            {
                "title": "Логические выражения",
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Условия if/else Python", "url": "https://www.youtube.com/watch?v=jBP8RY2-m74"},
                    {"type": "info", "title": "Сравнения и логика", "markdown": "## Логические выражения\n\nЛогическое выражение — это выражение, результат которого `True` (истина) или `False` (ложь).\n\n### Операторы сравнения\n| Оператор | Значение | Пример | Результат |\n|----------|----------|--------|-----------|\n| `==` | Равно | `5 == 5` | `True` |\n| `!=` | Не равно | `5 != 3` | `True` |\n| `>` | Больше | `7 > 3` | `True` |\n| `<` | Меньше | `2 < 1` | `False` |\n| `>=` | Больше или равно | `5 >= 5` | `True` |\n| `<=` | Меньше или равно | `3 <= 2` | `False` |\n\n### Логические операторы\n```python\nprint(True and True)   # True — оба True\nprint(True and False)  # False — один False\nprint(True or False)   # True — хотя бы один True\nprint(not True)        # False — отрицание\n```\n\n### Примеры\n```python\nage = 18\nprint(age >= 18)          # True\nprint(age > 18)           # False\nprint(age == 18 and True) # True\n```"},
                    {"type": "python-coding", "prompt": "Выведите результат сравнения 10 > 5 с помощью print().\n\nОператор > проверяет, больше ли левое число правого. Результат — True или False.\n\nОжидаемый вывод: True", "starterCode": "# Выведите результат сравнения 10 > 5\n", "expectedOutput": "True", "hint": "print(10 > 5)"},
                    {"type": "python-coding", "prompt": "Выведите результат выражения: 5 == 5 and 3 > 1\n\n== проверяет равенство (5 == 5 → True)\n> проверяет «больше» (3 > 1 → True)\nand — оба должны быть True, чтобы результат был True.\n\nTrue and True = True\n\nОжидаемый вывод: True", "starterCode": "# Выведите результат логического выражения\n", "expectedOutput": "True", "hint": "print(5 == 5 and 3 > 1)"},
                    {"type": "python-coding", "prompt": "Выведите результат: not (10 < 5)\n\n10 < 5 = False (10 не меньше 5)\nnot False = True (отрицание)\n\nОжидаемый вывод: True", "starterCode": "# Оператор not — отрицание\n", "expectedOutput": "True", "hint": "print(not (10 < 5))"},
                    {"type": "quiz", "question": "Что выведет print(3 != 3)?", "options": [{"id": "a", "text": "True", "correct": False}, {"id": "b", "text": "False", "correct": True}, {"id": "c", "text": "None", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            },
            {
                "title": "Конструкция if/else",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Условия if/else Python", "url": "https://www.youtube.com/watch?v=jBP8RY2-m74"},
                    {"type": "info", "title": "Ветвление: if / else", "markdown": "## Условная конструкция if/else\n\nПозволяет выполнять разный код в зависимости от условия.\n\n### Простой if\n```python\nage = 18\nif age >= 18:\n    print(\"Доступ разрешён\")\n```\nЕсли условие `True` — блок внутри `if` выполняется.\n\n### if/else\n```python\nage = 15\nif age >= 18:\n    print(\"Взрослый\")\nelse:\n    print(\"Несовершеннолетний\")\n```\n`else` — это «иначе», выполняется когда условие `False`.\n\n### if/elif/else\n```python\nscore = 85\nif score >= 90:\n    print(\"Отлично\")\nelif score >= 70:\n    print(\"Хорошо\")\nelif score >= 50:\n    print(\"Удовлетворительно\")\nelse:\n    print(\"Неудовлетворительно\")\n```\n\n### Важно: отступы!\nPython использует **отступы** (4 пробела) для обозначения блоков кода:\n```python\nif True:\n    print(\"Этот код внутри if\")  # 4 пробела\nprint(\"Этот код вне if\")         # без отступа\n```"},
                    {"type": "python-coding", "prompt": "Напишите программу: создайте переменную age = 20.\nЕсли age >= 18, выведите: Доступ разрешён\n\nСтруктура:\nif условие:\n    действие (с отступом 4 пробела)\n\nОжидаемый вывод: Доступ разрешён", "starterCode": "age = 20\n# Напишите условие if\n", "expectedOutput": "Доступ разрешён", "hint": "age = 20\nif age >= 18:\n    print(\"Доступ разрешён\")"},
                    {"type": "python-coding", "prompt": "Создайте переменную number = 7. Проверьте: если number чётное (number % 2 == 0) — выведите \"Чётное\", иначе — \"Нечётное\".\n\nОператор % даёт остаток от деления. Если остаток от деления на 2 равен 0 — число чётное.\n7 % 2 = 1 (не равно 0), значит 7 — нечётное.\n\nОжидаемый вывод: Нечётное", "starterCode": "number = 7\n# Проверьте чётность\n", "expectedOutput": "Нечётное", "hint": "number = 7\nif number % 2 == 0:\n    print(\"Чётное\")\nelse:\n    print(\"Нечётное\")"},
                    {"type": "python-coding", "prompt": "Создайте переменную score = 85.\nИспользуйте if/elif/else:\n- score >= 90 → \"Отлично\"\n- score >= 70 → \"Хорошо\"\n- иначе → \"Нужно подтянуть\"\n\n85 >= 90? Нет. 85 >= 70? Да! Значит выводим \"Хорошо\".\n\nОжидаемый вывод: Хорошо", "starterCode": "score = 85\n# Определите оценку\n", "expectedOutput": "Хорошо", "hint": "score = 85\nif score >= 90:\n    print(\"Отлично\")\nelif score >= 70:\n    print(\"Хорошо\")\nelse:\n    print(\"Нужно подтянуть\")"},
                    {"type": "quiz", "question": "Какой отступ используется в Python для блоков кода?", "options": [{"id": "a", "text": "2 пробела", "correct": False}, {"id": "b", "text": "4 пробела", "correct": True}, {"id": "c", "text": "Табуляция обязательно", "correct": False}, {"id": "d", "text": "Фигурные скобки {}", "correct": False}]}
                ]
            },
            {
                "title": "Вложенные условия и тернарный оператор",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Условия if/else Python", "url": "https://www.youtube.com/watch?v=jBP8RY2-m74"},
                    {"type": "info", "title": "Продвинутые условия", "markdown": "## Вложенные условия\n\nМожно вкладывать `if` внутрь другого `if`:\n```python\nage = 20\nhas_ticket = True\n\nif age >= 18:\n    if has_ticket:\n        print(\"Проходите\")\n    else:\n        print(\"Купите билет\")\nelse:\n    print(\"Вход с 18 лет\")\n```\n\n## Тернарный оператор (условное выражение)\nКороткая запись if/else **в одну строку**:\n```python\nage = 20\nstatus = \"взрослый\" if age >= 18 else \"ребёнок\"\nprint(status)  # взрослый\n```\n\nСинтаксис: `значение_если_true if условие else значение_если_false`\n\n## Оператор in\nПроверяет, есть ли элемент в коллекции:\n```python\nfruits = [\"яблоко\", \"банан\", \"груша\"]\nprint(\"банан\" in fruits)  # True\nprint(\"киви\" in fruits)   # False\n```\n\nРаботает и со строками:\n```python\nprint(\"Py\" in \"Python\")  # True\n```"},
                    {"type": "python-coding", "prompt": "Используя тернарный оператор, создайте переменную result:\n- Если 10 > 5, то result = \"Да\"\n- Иначе result = \"Нет\"\n\nЗатем выведите result.\n\nТернарный оператор: переменная = значение1 if условие else значение2\n\nОжидаемый вывод: Да", "starterCode": "# Тернарный оператор\n\n# Выведите result\n", "expectedOutput": "Да", "hint": "result = \"Да\" if 10 > 5 else \"Нет\"\nprint(result)"},
                    {"type": "python-coding", "prompt": "Проверьте, содержит ли строка \"Python is great\" подстроку \"Python\".\nВыведите результат оператора in.\n\nОператор in проверяет вхождение: \"abc\" in \"abcdef\" → True\n\nОжидаемый вывод: True", "starterCode": "# Проверьте вхождение подстроки\ntext = \"Python is great\"\n", "expectedOutput": "True", "hint": "text = \"Python is great\"\nprint(\"Python\" in text)"},
                    {"type": "python-coding", "prompt": "Создайте переменную x = 15.\nВыведите \"Подросток\" если x >= 13 и x <= 19 (используйте and), иначе \"Не подросток\".\n\n15 >= 13? Да. 15 <= 19? Да. Оба True → and даёт True.\n\nОжидаемый вывод: Подросток", "starterCode": "x = 15\n# Используйте if с оператором and\n", "expectedOutput": "Подросток", "hint": "x = 15\nif x >= 13 and x <= 19:\n    print(\"Подросток\")\nelse:\n    print(\"Не подросток\")"},
                    {"type": "quiz", "question": "Что выведет: print(\"YES\" if 3 > 5 else \"NO\")?", "options": [{"id": "a", "text": "YES", "correct": False}, {"id": "b", "text": "NO", "correct": True}, {"id": "c", "text": "True", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 4: Циклы — for и while ====================
    {
        "title": "Циклы: for и while",
        "lessons": [
            {
                "title": "Цикл for и range()",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Циклы for и while Python", "url": "https://www.youtube.com/watch?v=sZ0EIwgLblY"},
                    {"type": "info", "title": "Цикл for", "markdown": "## Цикл for\n\nЦикл `for` перебирает элементы последовательности:\n\n```python\nfor i in range(5):\n    print(i)\n# Выведет: 0, 1, 2, 3, 4 (каждое на новой строке)\n```\n\n### range() — генератор чисел\n```python\nrange(5)       # 0, 1, 2, 3, 4\nrange(2, 7)    # 2, 3, 4, 5, 6\nrange(0, 10, 2) # 0, 2, 4, 6, 8 (шаг 2)\n```\n\n### Перебор строки\n```python\nfor char in \"Hi\":\n    print(char)\n# H\n# i\n```\n\n### Перебор списка\n```python\nfruits = [\"яблоко\", \"банан\", \"груша\"]\nfor fruit in fruits:\n    print(fruit)\n```\n\n### Пример: сумма чисел\n```python\ntotal = 0\nfor i in range(1, 6):  # 1, 2, 3, 4, 5\n    total = total + i\nprint(total)  # 15\n```"},
                    {"type": "python-coding", "prompt": "Используя цикл for и range(5), выведите числа от 0 до 4, каждое на новой строке.\n\nrange(5) генерирует числа: 0, 1, 2, 3, 4\nfor i in range(5): — переменная i будет по очереди принимать эти значения.\n\nОжидаемый вывод:\n0\n1\n2\n3\n4", "starterCode": "# Цикл for с range(5)\n", "expectedOutput": "0\n1\n2\n3\n4", "hint": "for i in range(5):\n    print(i)"},
                    {"type": "python-coding", "prompt": "Вычислите сумму чисел от 1 до 5 используя цикл for.\n\nАлгоритм:\n1. Создайте переменную total = 0\n2. В цикле for i in range(1, 6): прибавляйте i к total\n3. После цикла выведите total\n\nrange(1, 6) даёт: 1, 2, 3, 4, 5\nСумма: 1+2+3+4+5 = 15\n\nОжидаемый вывод: 15", "starterCode": "# Вычислите сумму 1+2+3+4+5\ntotal = 0\n\n\n", "expectedOutput": "15", "hint": "total = 0\nfor i in range(1, 6):\n    total = total + i\nprint(total)"},
                    {"type": "python-coding", "prompt": "Выведите все чётные числа от 2 до 10 включительно.\n\nИспользуйте range(2, 11, 2) — начало 2, конец 11 (не включительно), шаг 2.\nЭто даст: 2, 4, 6, 8, 10\n\nОжидаемый вывод:\n2\n4\n6\n8\n10", "starterCode": "# Чётные числа от 2 до 10\n", "expectedOutput": "2\n4\n6\n8\n10", "hint": "for i in range(2, 11, 2):\n    print(i)"},
                    {"type": "quiz", "question": "Сколько раз выполнится цикл for i in range(3)?", "options": [{"id": "a", "text": "2 раза", "correct": False}, {"id": "b", "text": "3 раза", "correct": True}, {"id": "c", "text": "4 раза", "correct": False}, {"id": "d", "text": "1 раз", "correct": False}]}
                ]
            },
            {
                "title": "Цикл while",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Циклы for и while Python", "url": "https://www.youtube.com/watch?v=sZ0EIwgLblY"},
                    {"type": "info", "title": "Цикл while", "markdown": "## Цикл while\n\nЦикл `while` выполняется, **пока условие True**:\n\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1  # увеличиваем на 1\n# Выведет: 0, 1, 2, 3, 4\n```\n\n### Важно: не забудьте изменять условие!\nИначе получится **бесконечный цикл**:\n```python\n# ПЛОХО — бесконечный цикл!\nwhile True:\n    print(\"Помогите!\")\n```\n\n### break — прервать цикл\n```python\ni = 0\nwhile True:\n    if i >= 3:\n        break  # выход из цикла\n    print(i)\n    i += 1\n# Выведет: 0, 1, 2\n```\n\n### continue — пропустить итерацию\n```python\nfor i in range(5):\n    if i == 2:\n        continue  # пропустить 2\n    print(i)\n# Выведет: 0, 1, 3, 4\n```\n\n### while vs for\n- `for` — когда знаете сколько раз повторять\n- `while` — когда повторяете до выполнения условия"},
                    {"type": "python-coding", "prompt": "Используя цикл while, выведите числа от 1 до 5.\n\nАлгоритм:\n1. i = 1\n2. Пока i <= 5: выводим i, увеличиваем i на 1\n\nОжидаемый вывод:\n1\n2\n3\n4\n5", "starterCode": "# Цикл while от 1 до 5\ni = 1\n", "expectedOutput": "1\n2\n3\n4\n5", "hint": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1"},
                    {"type": "python-coding", "prompt": "Используя цикл for и оператор continue, выведите числа от 0 до 4, ПРОПУСКАЯ число 2.\n\ncontinue пропускает текущую итерацию и переходит к следующей.\n\nОжидаемый вывод:\n0\n1\n3\n4", "starterCode": "# Пропустите число 2 с помощью continue\n", "expectedOutput": "0\n1\n3\n4", "hint": "for i in range(5):\n    if i == 2:\n        continue\n    print(i)"},
                    {"type": "python-coding", "prompt": "Используя while и break, выводите числа начиная с 1. Остановитесь (break) когда число станет больше 4.\n\nАлгоритм:\n1. i = 1\n2. while True:\n3.   если i > 4: break\n4.   print(i)\n5.   i += 1\n\nОжидаемый вывод:\n1\n2\n3\n4", "starterCode": "# Цикл с break\ni = 1\n", "expectedOutput": "1\n2\n3\n4", "hint": "i = 1\nwhile True:\n    if i > 4:\n        break\n    print(i)\n    i += 1"},
                    {"type": "quiz", "question": "Что делает оператор break?", "options": [{"id": "a", "text": "Пропускает итерацию", "correct": False}, {"id": "b", "text": "Завершает программу", "correct": False}, {"id": "c", "text": "Прерывает цикл", "correct": True}, {"id": "d", "text": "Перезапускает цикл", "correct": False}]}
                ]
            },
            {
                "title": "Вложенные циклы и patterns",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Циклы for и while Python", "url": "https://www.youtube.com/watch?v=sZ0EIwgLblY"},
                    {"type": "info", "title": "Вложенные циклы", "markdown": "## Вложенные циклы\n\nЦикл внутри цикла — это вложенный цикл:\n\n```python\nfor i in range(3):      # внешний цикл\n    for j in range(3):  # внутренний цикл\n        print(f\"{i},{j}\", end=\" \")\n    print()  # новая строка после внутреннего цикла\n```\nРезультат:\n```\n0,0 0,1 0,2 \n1,0 1,1 1,2 \n2,0 2,1 2,2 \n```\n\n### Таблица умножения\n```python\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(i * j, end=\"\\t\")\n    print()\n```\nРезультат:\n```\n1\t2\t3\n2\t4\t6\n3\t6\t9\n```\n\n### Параметр end в print()\n```python\nprint(\"A\", end=\"\")   # не переводит строку\nprint(\"B\", end=\" \")  # добавляет пробел вместо \\n\nprint(\"C\")           # обычный перевод строки\n# Результат: AB C\n```\n\n### Паттерн: треугольник из звёзд\n```python\nfor i in range(1, 5):\n    print(\"*\" * i)\n# *\n# **\n# ***\n# ****\n```"},
                    {"type": "python-coding", "prompt": "Выведите треугольник из звёздочек (*) высотой 5 строк:\n*\n**\n***\n****\n*****\n\nИспользуйте цикл for i in range(1, 6): и оператор * для повторения строки.\n\"*\" * 3 даёт \"***\"\n\nОжидаемый вывод:\n*\n**\n***\n****\n*****", "starterCode": "# Треугольник из звёзд\n", "expectedOutput": "*\n**\n***\n****\n*****", "hint": "for i in range(1, 6):\n    print(\"*\" * i)"},
                    {"type": "python-coding", "prompt": "Выведите таблицу умножения на 3 (от 3*1 до 3*5), каждое произведение на новой строке.\n\nИспользуйте цикл for i in range(1, 6): и выводите 3 * i.\n\nОжидаемый вывод:\n3\n6\n9\n12\n15", "starterCode": "# Таблица умножения на 3\n", "expectedOutput": "3\n6\n9\n12\n15", "hint": "for i in range(1, 6):\n    print(3 * i)"},
                    {"type": "python-coding", "prompt": "Выведите числа от 10 до 1 в обратном порядке (каждое на новой строке).\n\nИспользуйте range(10, 0, -1) — начало 10, конец 0 (не включительно), шаг -1.\n\nОжидаемый вывод:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1", "starterCode": "# Обратный отсчёт от 10 до 1\n", "expectedOutput": "10\n9\n8\n7\n6\n5\n4\n3\n2\n1", "hint": "for i in range(10, 0, -1):\n    print(i)"},
                    {"type": "quiz", "question": "Что выведет print(\"AB\" * 3)?", "options": [{"id": "a", "text": "AB3", "correct": False}, {"id": "b", "text": "ABABAB", "correct": True}, {"id": "c", "text": "AABBCC", "correct": False}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            },
            {
                "title": "enumerate и zip",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Циклы for и while Python", "url": "https://www.youtube.com/watch?v=sZ0EIwgLblY"},
                    {"type": "info", "title": "enumerate() и zip()", "markdown": "## enumerate() — индекс + элемент\n\nКогда в цикле нужен и индекс, и значение:\n```python\nfruits = [\"яблоко\", \"банан\", \"груша\"]\nfor i, fruit in enumerate(fruits):\n    print(f\"{i}: {fruit}\")\n# 0: яблоко\n# 1: банан\n# 2: груша\n```\n\n### Начать с другого числа\n```python\nfor i, fruit in enumerate(fruits, start=1):\n    print(f\"{i}. {fruit}\")\n# 1. яблоко\n# 2. банан\n# 3. груша\n```\n\n## zip() — параллельный перебор\n\nОбъединяет несколько списков:\n```python\nnames = [\"Алиса\", \"Боб\", \"Карл\"]\nages = [25, 30, 28]\n\nfor name, age in zip(names, ages):\n    print(f\"{name}: {age}\")\n# Алиса: 25\n# Боб: 30\n# Карл: 28\n```\n\n### zip останавливается по короткому списку\n```python\na = [1, 2, 3]\nb = [10, 20]\nprint(list(zip(a, b)))  # [(1, 10), (2, 20)]\n```"},
                    {"type": "python-coding", "prompt": "Используя enumerate(), выведите элементы списка с их индексами.\n\ncolors = [\"red\", \"green\", \"blue\"]\n\nВыведите:\n0: red\n1: green\n2: blue\n\nИспользуйте f-строку: print(f\"{i}: {color}\")\n\nОжидаемый вывод:\n0: red\n1: green\n2: blue", "starterCode": "colors = [\"red\", \"green\", \"blue\"]\n# Используйте enumerate\n", "expectedOutput": "0: red\n1: green\n2: blue", "hint": "colors = [\"red\", \"green\", \"blue\"]\nfor i, color in enumerate(colors):\n    print(f\"{i}: {color}\")"},
                    {"type": "python-coding", "prompt": "Используя zip(), объедините два списка и выведите пары.\n\nkeys = [\"a\", \"b\", \"c\"]\nvalues = [1, 2, 3]\n\nВыведите каждую пару в формате: a = 1\n\nОжидаемый вывод:\na = 1\nb = 2\nc = 3", "starterCode": "keys = [\"a\", \"b\", \"c\"]\nvalues = [1, 2, 3]\n# Используйте zip\n", "expectedOutput": "a = 1\nb = 2\nc = 3", "hint": "keys = [\"a\", \"b\", \"c\"]\nvalues = [1, 2, 3]\nfor k, v in zip(keys, values):\n    print(f\"{k} = {v}\")"},
                    {"type": "python-coding", "prompt": "Используя enumerate() с start=1, пронумеруйте список задач:\ntasks = [\"Купить молоко\", \"Позвонить маме\", \"Сделать ДЗ\"]\n\nВыведите:\n1. Купить молоко\n2. Позвонить маме\n3. Сделать ДЗ\n\nОжидаемый вывод:\n1. Купить молоко\n2. Позвонить маме\n3. Сделать ДЗ", "starterCode": "tasks = [\"Купить молоко\", \"Позвонить маме\", \"Сделать ДЗ\"]\n# Пронумеруйте с 1\n", "expectedOutput": "1. Купить молоко\n2. Позвонить маме\n3. Сделать ДЗ", "hint": "tasks = [\"Купить молоко\", \"Позвонить маме\", \"Сделать ДЗ\"]\nfor i, task in enumerate(tasks, start=1):\n    print(f\"{i}. {task}\")"},
                    {"type": "quiz", "question": "Что делает zip() когда списки разной длины?", "options": [{"id": "a", "text": "Вызывает ошибку", "correct": False}, {"id": "b", "text": "Дополняет None", "correct": False}, {"id": "c", "text": "Останавливается по самому короткому", "correct": True}, {"id": "d", "text": "Останавливается по самому длинному", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 5: Списки и кортежи ====================
    {
        "title": "Списки и кортежи",
        "lessons": [
            {
                "title": "Создание и индексация списков",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Списки Python", "url": "https://www.youtube.com/watch?v=-X2ubBdP2Ak"},
                    {"type": "info", "title": "Списки (list)", "markdown": "## Списки в Python\n\nСписок — это упорядоченная коллекция элементов.\n\n### Создание списка\n```python\nnumbers = [1, 2, 3, 4, 5]\nfruits = [\"яблоко\", \"банан\", \"груша\"]\nmixed = [1, \"hello\", True, 3.14]\nempty = []\n```\n\n### Индексация (доступ по номеру)\nНумерация с 0:\n```python\nfruits = [\"яблоко\", \"банан\", \"груша\"]\nprint(fruits[0])   # яблоко\nprint(fruits[1])   # банан\nprint(fruits[-1])  # груша (последний)\n```\n\n### Длина списка\n```python\nprint(len(fruits))  # 3\n```\n\n### Изменение элемента\n```python\nfruits[0] = \"манго\"\nprint(fruits)  # ['манго', 'банан', 'груша']\n```\n\n### Срезы\n```python\nnumbers = [10, 20, 30, 40, 50]\nprint(numbers[1:4])   # [20, 30, 40]\nprint(numbers[:3])    # [10, 20, 30]\nprint(numbers[2:])    # [30, 40, 50]\n```\n\n### Проверка наличия\n```python\nprint(\"банан\" in fruits)  # True\nprint(\"киви\" in fruits)   # False\n```"},
                    {"type": "python-coding", "prompt": "Создайте список numbers = [10, 20, 30, 40, 50] и выведите его длину с помощью len().\n\nlen() возвращает количество элементов в списке.\n\nОжидаемый вывод: 5", "starterCode": "# Создайте список и выведите длину\n", "expectedOutput": "5", "hint": "numbers = [10, 20, 30, 40, 50]\nprint(len(numbers))"},
                    {"type": "python-coding", "prompt": "Создайте список fruits = [\"яблоко\", \"банан\", \"груша\", \"манго\"] и выведите второй элемент (индекс 1).\n\nПомните: индексация начинается с 0!\nfruits[0] = \"яблоко\"\nfruits[1] = \"банан\"\n\nОжидаемый вывод: банан", "starterCode": "# Создайте список и выведите элемент с индексом 1\n", "expectedOutput": "банан", "hint": "fruits = [\"яблоко\", \"банан\", \"груша\", \"манго\"]\nprint(fruits[1])"},
                    {"type": "python-coding", "prompt": "Создайте список nums = [5, 10, 15, 20, 25]. Выведите сумму всех элементов с помощью функции sum().\n\nsum(список) — встроенная функция, которая считает сумму всех чисел.\n5 + 10 + 15 + 20 + 25 = 75\n\nОжидаемый вывод: 75", "starterCode": "# Создайте список и выведите сумму\n", "expectedOutput": "75", "hint": "nums = [5, 10, 15, 20, 25]\nprint(sum(nums))"},
                    {"type": "quiz", "question": "Что выведет: print([1,2,3][-1])?", "options": [{"id": "a", "text": "1", "correct": False}, {"id": "b", "text": "2", "correct": False}, {"id": "c", "text": "3", "correct": True}, {"id": "d", "text": "Ошибка", "correct": False}]}
                ]
            },
            {
                "title": "Методы списков",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Списки Python", "url": "https://www.youtube.com/watch?v=-X2ubBdP2Ak"},
                    {"type": "info", "title": "Методы списков", "markdown": "## Методы списков\n\n### Добавление элементов\n```python\nfruits = [\"яблоко\", \"банан\"]\n\nfruits.append(\"груша\")      # в конец\nprint(fruits)  # ['яблоко', 'банан', 'груша']\n\nfruits.insert(1, \"манго\")   # на позицию 1\nprint(fruits)  # ['яблоко', 'манго', 'банан', 'груша']\n```\n\n### Удаление элементов\n```python\nfruits = [\"яблоко\", \"банан\", \"груша\"]\n\nfruits.remove(\"банан\")    # по значению\nprint(fruits)  # ['яблоко', 'груша']\n\nlast = fruits.pop()       # удалить последний\nprint(last)    # груша\n```\n\n### Сортировка\n```python\nnumbers = [3, 1, 4, 1, 5]\nnumbers.sort()\nprint(numbers)  # [1, 1, 3, 4, 5]\n\nnumbers.sort(reverse=True)\nprint(numbers)  # [5, 4, 3, 1, 1]\n```\n\n### Другие полезные методы\n```python\nnums = [1, 2, 3, 2, 1]\nprint(nums.count(2))    # 2 (сколько раз встречается)\nprint(nums.index(3))    # 2 (индекс первого вхождения)\nnums.reverse()          # развернуть список\nprint(nums)             # [1, 2, 3, 2, 1]\n```"},
                    {"type": "python-coding", "prompt": "Создайте пустой список items = []. Добавьте в него три элемента: \"ручка\", \"тетрадь\", \"книга\" (используя append три раза). Выведите длину списка.\n\n.append(элемент) добавляет элемент в конец списка.\n\nОжидаемый вывод: 3", "starterCode": "items = []\n# Добавьте 3 элемента с помощью append\n\n\n\n# Выведите длину\n", "expectedOutput": "3", "hint": "items = []\nitems.append(\"ручка\")\nitems.append(\"тетрадь\")\nitems.append(\"книга\")\nprint(len(items))"},
                    {"type": "python-coding", "prompt": "Создайте список numbers = [3, 1, 4, 1, 5, 9]. Отсортируйте его методом .sort() и выведите список.\n\n.sort() сортирует список по возрастанию (изменяет сам список).\n\nОжидаемый вывод: [1, 1, 3, 4, 5, 9]", "starterCode": "numbers = [3, 1, 4, 1, 5, 9]\n# Отсортируйте и выведите\n", "expectedOutput": "[1, 1, 3, 4, 5, 9]", "hint": "numbers = [3, 1, 4, 1, 5, 9]\nnumbers.sort()\nprint(numbers)"},
                    {"type": "python-coding", "prompt": "Создайте список colors = [\"красный\", \"синий\", \"зелёный\"]. Удалите \"синий\" с помощью .remove() и выведите оставшийся список.\n\n.remove(значение) удаляет первое вхождение элемента.\n\nОжидаемый вывод: ['красный', 'зелёный']", "starterCode": "colors = [\"красный\", \"синий\", \"зелёный\"]\n# Удалите \"синий\" и выведите список\n", "expectedOutput": "['красный', 'зелёный']", "hint": "colors = [\"красный\", \"синий\", \"зелёный\"]\ncolors.remove(\"синий\")\nprint(colors)"},
                    {"type": "quiz", "question": "Какой метод добавляет элемент в конец списка?", "options": [{"id": "a", "text": "add()", "correct": False}, {"id": "b", "text": "append()", "correct": True}, {"id": "c", "text": "insert()", "correct": False}, {"id": "d", "text": "push()", "correct": False}]}
                ]
            },
            {
                "title": "List comprehension и кортежи",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Списки Python", "url": "https://www.youtube.com/watch?v=-X2ubBdP2Ak"},
                    {"type": "info", "title": "List comprehension и кортежи", "markdown": "## List Comprehension (генераторы списков)\n\nКомпактный способ создания списков:\n\n```python\n# Обычный способ\nsquares = []\nfor i in range(5):\n    squares.append(i ** 2)\n\n# List comprehension — то же самое в одну строку!\nsquares = [i ** 2 for i in range(5)]\nprint(squares)  # [0, 1, 4, 9, 16]\n```\n\n### С условием (фильтрация)\n```python\n# Только чётные\nevens = [i for i in range(10) if i % 2 == 0]\nprint(evens)  # [0, 2, 4, 6, 8]\n```\n\n### С преобразованием строк\n```python\nwords = [\"hello\", \"world\"]\nupper_words = [w.upper() for w in words]\nprint(upper_words)  # ['HELLO', 'WORLD']\n```\n\n## Кортежи (tuple)\n\nКортеж — как список, но **неизменяемый**:\n```python\npoint = (3, 5)\ncolors = (\"red\", \"green\", \"blue\")\n\nprint(point[0])    # 3 — индексация работает\n# point[0] = 10   # ОШИБКА! Нельзя изменять\n```\n\n### Распаковка кортежа\n```python\nx, y = (10, 20)\nprint(x)  # 10\nprint(y)  # 20\n```"},
                    {"type": "python-coding", "prompt": "Создайте список квадратов чисел от 1 до 5 с помощью list comprehension:\nsquares = [i ** 2 for i in range(1, 6)]\n\nЭто создаст: [1, 4, 9, 16, 25]\nВыведите этот список.\n\nОжидаемый вывод: [1, 4, 9, 16, 25]", "starterCode": "# List comprehension: квадраты от 1 до 5\n\n", "expectedOutput": "[1, 4, 9, 16, 25]", "hint": "squares = [i ** 2 for i in range(1, 6)]\nprint(squares)"},
                    {"type": "python-coding", "prompt": "Используя list comprehension с условием, создайте список чётных чисел от 1 до 10.\n\nСинтаксис: [выражение for переменная in range() if условие]\nЧётное число: i % 2 == 0\n\nОжидаемый вывод: [2, 4, 6, 8, 10]", "starterCode": "# Чётные числа от 1 до 10 через list comprehension\n", "expectedOutput": "[2, 4, 6, 8, 10]", "hint": "evens = [i for i in range(1, 11) if i % 2 == 0]\nprint(evens)"},
                    {"type": "python-coding", "prompt": "Создайте кортеж point = (5, 10). Распакуйте его в переменные x и y. Выведите сумму x + y.\n\nРаспаковка: x, y = (5, 10) — x станет 5, y станет 10.\n\nОжидаемый вывод: 15", "starterCode": "# Создайте кортеж и распакуйте\n", "expectedOutput": "15", "hint": "point = (5, 10)\nx, y = point\nprint(x + y)"},
                    {"type": "quiz", "question": "Чем кортеж (tuple) отличается от списка (list)?", "options": [{"id": "a", "text": "Кортеж может содержать только числа", "correct": False}, {"id": "b", "text": "Кортеж неизменяемый (immutable)", "correct": True}, {"id": "c", "text": "Кортеж не поддерживает индексацию", "correct": False}, {"id": "d", "text": "Кортеж не может быть пустым", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 6: Функции ====================
    {
        "title": "Функции",
        "lessons": [
            {
                "title": "Создание функций — def",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Функции Python", "url": "https://www.youtube.com/watch?v=DJAlfolEv9A"},
                    {"type": "info", "title": "Функции в Python", "markdown": "## Функции\n\nФункция — это именованный блок кода, который можно вызывать многократно.\n\n### Создание функции\n```python\ndef greet():\n    print(\"Привет!\")\n\ngreet()  # вызов функции → Привет!\ngreet()  # можно вызывать сколько угодно раз\n```\n\n### Функция с параметрами\n```python\ndef greet(name):\n    print(f\"Привет, {name}!\")\n\ngreet(\"Алиса\")  # Привет, Алиса!\ngreet(\"Боб\")    # Привет, Боб!\n```\n\n### Несколько параметров\n```python\ndef add(a, b):\n    print(a + b)\n\nadd(3, 5)   # 8\nadd(10, 20) # 30\n```\n\n### Значения по умолчанию\n```python\ndef greet(name, greeting=\"Привет\"):\n    print(f\"{greeting}, {name}!\")\n\ngreet(\"Мир\")              # Привет, Мир!\ngreet(\"Мир\", \"Здравствуй\") # Здравствуй, Мир!\n```\n\n### Зачем нужны функции?\n- **DRY** (Don't Repeat Yourself) — не повторяться\n- Читаемость кода\n- Переиспользование\n- Тестирование"},
                    {"type": "python-coding", "prompt": "Создайте функцию say_hello(), которая выводит \"Привет, мир!\". Вызовите её.\n\nСтруктура:\ndef имя_функции():\n    тело функции (с отступом)\n\nимя_функции()  # вызов\n\nОжидаемый вывод: Привет, мир!", "starterCode": "# Создайте функцию say_hello\n\n\n# Вызовите функцию\n", "expectedOutput": "Привет, мир!", "hint": "def say_hello():\n    print(\"Привет, мир!\")\n\nsay_hello()"},
                    {"type": "python-coding", "prompt": "Создайте функцию double(n), которая выводит число n умноженное на 2.\nВызовите её с аргументом 7.\n\ndef double(n):\n    print(n * 2)\n\n7 * 2 = 14\n\nОжидаемый вывод: 14", "starterCode": "# Функция double(n)\n\n\n# Вызов с аргументом 7\n", "expectedOutput": "14", "hint": "def double(n):\n    print(n * 2)\n\ndouble(7)"},
                    {"type": "python-coding", "prompt": "Создайте функцию repeat_text(text, times), которая выводит text повторённый times раз.\nВызовите: repeat_text(\"Ля\", 3)\n\nОператор * повторяет строку: \"Ля\" * 3 = \"ЛяЛяЛя\"\n\nОжидаемый вывод: ЛяЛяЛя", "starterCode": "# Функция repeat_text\n\n\n# Вызов\n", "expectedOutput": "ЛяЛяЛя", "hint": "def repeat_text(text, times):\n    print(text * times)\n\nrepeat_text(\"Ля\", 3)"},
                    {"type": "quiz", "question": "Как правильно определить функцию в Python?", "options": [{"id": "a", "text": "function greet():", "correct": False}, {"id": "b", "text": "def greet():", "correct": True}, {"id": "c", "text": "func greet():", "correct": False}, {"id": "d", "text": "define greet():", "correct": False}]}
                ]
            },
            {
                "title": "return — возврат значения",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Функции Python", "url": "https://www.youtube.com/watch?v=DJAlfolEv9A"},
                    {"type": "info", "title": "Возврат значения — return", "markdown": "## Оператор return\n\n`return` возвращает значение из функции:\n\n```python\ndef add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8\n```\n\n### Разница между print и return\n```python\ndef add_print(a, b):\n    print(a + b)  # только выводит\n\ndef add_return(a, b):\n    return a + b  # возвращает значение\n\nx = add_return(3, 5)  # x = 8\ny = add_print(3, 5)   # выведет 8, но y = None!\n```\n\n### return останавливает функцию\n```python\ndef check(n):\n    if n > 0:\n        return \"Положительное\"\n    return \"Не положительное\"\n    print(\"Эта строка никогда не выполнится\")\n```\n\n### Множественный return\n```python\ndef min_max(numbers):\n    return min(numbers), max(numbers)\n\nlow, high = min_max([3, 1, 7, 2])\nprint(low, high)  # 1 7\n```\n\n### Функция без return возвращает None\n```python\ndef nothing():\n    pass  # ничего не делает\n\nresult = nothing()\nprint(result)  # None\n```"},
                    {"type": "python-coding", "prompt": "Создайте функцию square(n), которая ВОЗВРАЩАЕТ n ** 2 (квадрат числа).\nВызовите её с аргументом 6 и выведите результат.\n\nВажно: используйте return, а не print внутри функции!\n\nОжидаемый вывод: 36", "starterCode": "# Функция square с return\n\n\n# Вызов и вывод результата\n", "expectedOutput": "36", "hint": "def square(n):\n    return n ** 2\n\nprint(square(6))"},
                    {"type": "python-coding", "prompt": "Создайте функцию is_even(n), которая возвращает True если число чётное, иначе False.\nВыведите результат вызова is_even(4).\n\nЧётное число: n % 2 == 0\n\nОжидаемый вывод: True", "starterCode": "# Функция is_even\n\n\n# Проверьте число 4\n", "expectedOutput": "True", "hint": "def is_even(n):\n    return n % 2 == 0\n\nprint(is_even(4))"},
                    {"type": "python-coding", "prompt": "Создайте функцию max_of_three(a, b, c), которая возвращает максимальное из трёх чисел.\nИспользуйте встроенную функцию max().\n\nВызовите: print(max_of_three(10, 25, 7))\n\nОжидаемый вывод: 25", "starterCode": "# Функция max_of_three\n\n\n# Вызов\n", "expectedOutput": "25", "hint": "def max_of_three(a, b, c):\n    return max(a, b, c)\n\nprint(max_of_three(10, 25, 7))"},
                    {"type": "quiz", "question": "Что возвращает функция без оператора return?", "options": [{"id": "a", "text": "0", "correct": False}, {"id": "b", "text": "\"\"", "correct": False}, {"id": "c", "text": "None", "correct": True}, {"id": "d", "text": "False", "correct": False}]}
                ]
            },
            {
                "title": "Лямбда-функции и map/filter",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Функции Python", "url": "https://www.youtube.com/watch?v=DJAlfolEv9A"},
                    {"type": "info", "title": "Lambda, map, filter", "markdown": "## Лямбда-функции\n\nАнонимная функция в одну строку:\n```python\n# Обычная функция\ndef double(x):\n    return x * 2\n\n# Лямбда — эквивалент\ndouble = lambda x: x * 2\n\nprint(double(5))  # 10\n```\n\nСинтаксис: `lambda параметры: выражение`\n\n### map() — применить функцию к каждому элементу\n```python\nnumbers = [1, 2, 3, 4, 5]\ndoubled = list(map(lambda x: x * 2, numbers))\nprint(doubled)  # [2, 4, 6, 8, 10]\n```\n\n### filter() — отфильтровать элементы\n```python\nnumbers = [1, 2, 3, 4, 5, 6]\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)  # [2, 4, 6]\n```\n\n### sorted() с key\n```python\nwords = [\"banana\", \"apple\", \"cherry\"]\nby_length = sorted(words, key=lambda w: len(w))\nprint(by_length)  # ['apple', 'banana', 'cherry']\n```\n\n### Когда использовать lambda?\n- Для коротких одноразовых функций\n- В map(), filter(), sorted()\n- Когда полноценная def — избыточна"},
                    {"type": "python-coding", "prompt": "Используя map() и lambda, удвойте каждый элемент списка [1, 2, 3, 4, 5].\n\nmap(функция, список) применяет функцию к каждому элементу.\nlist() преобразует результат в список.\n\nlambda x: x * 2 — анонимная функция, удваивающая число.\n\nОжидаемый вывод: [2, 4, 6, 8, 10]", "starterCode": "numbers = [1, 2, 3, 4, 5]\n# Используйте map + lambda\n", "expectedOutput": "[2, 4, 6, 8, 10]", "hint": "numbers = [1, 2, 3, 4, 5]\nresult = list(map(lambda x: x * 2, numbers))\nprint(result)"},
                    {"type": "python-coding", "prompt": "Используя filter() и lambda, отберите из списка [1, 2, 3, 4, 5, 6, 7, 8] только числа больше 4.\n\nfilter(функция, список) оставляет элементы, для которых функция вернула True.\n\nОжидаемый вывод: [5, 6, 7, 8]", "starterCode": "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\n# Используйте filter + lambda\n", "expectedOutput": "[5, 6, 7, 8]", "hint": "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\nresult = list(filter(lambda x: x > 4, numbers))\nprint(result)"},
                    {"type": "python-coding", "prompt": "Отсортируйте список слов по длине (от короткого к длинному) с помощью sorted() и key=lambda.\n\nwords = [\"python\", \"go\", \"javascript\", \"c\"]\n\nsorted(список, key=функция) — сортирует по результату функции.\nlen(\"go\") = 2, len(\"c\") = 1, len(\"python\") = 6, len(\"javascript\") = 10\n\nОжидаемый вывод: ['c', 'go', 'python', 'javascript']", "starterCode": "words = [\"python\", \"go\", \"javascript\", \"c\"]\n# Отсортируйте по длине\n", "expectedOutput": "['c', 'go', 'python', 'javascript']", "hint": "words = [\"python\", \"go\", \"javascript\", \"c\"]\nprint(sorted(words, key=lambda w: len(w)))"},
                    {"type": "quiz", "question": "Что делает filter()?", "options": [{"id": "a", "text": "Преобразует каждый элемент", "correct": False}, {"id": "b", "text": "Сортирует список", "correct": False}, {"id": "c", "text": "Оставляет элементы по условию", "correct": True}, {"id": "d", "text": "Удаляет дубликаты", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 7: Словари и множества ====================
    {
        "title": "Словари и множества",
        "lessons": [
            {
                "title": "Словари — dict",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Словари Python", "url": "https://www.youtube.com/watch?v=W2oO1Y-QDzo"},
                    {"type": "info", "title": "Словари (dict)", "markdown": "## Словари в Python\n\nСловарь — это коллекция пар **ключ: значение**.\n\n### Создание словаря\n```python\nperson = {\n    \"name\": \"Алиса\",\n    \"age\": 25,\n    \"city\": \"Москва\"\n}\n```\n\n### Доступ к значению по ключу\n```python\nprint(person[\"name\"])  # Алиса\nprint(person[\"age\"])   # 25\n```\n\n### Метод get() — безопасный доступ\n```python\nprint(person.get(\"name\"))     # Алиса\nprint(person.get(\"phone\"))    # None (нет ключа)\nprint(person.get(\"phone\", \"Не указан\"))  # Не указан\n```\n\n### Изменение и добавление\n```python\nperson[\"age\"] = 26           # изменить\nperson[\"email\"] = \"a@b.com\"  # добавить новый ключ\n```\n\n### Удаление\n```python\ndel person[\"city\"]           # удалить ключ\nremoved = person.pop(\"age\")  # удалить и получить значение\n```\n\n### Перебор словаря\n```python\nfor key in person:\n    print(key, person[key])\n\nfor key, value in person.items():\n    print(f\"{key}: {value}\")\n```\n\n### Полезные методы\n```python\nprint(person.keys())    # все ключи\nprint(person.values())  # все значения\nprint(len(person))      # количество пар\n```"},
                    {"type": "python-coding", "prompt": "Создайте словарь student с ключами \"name\" и \"grade\":\nstudent = {\"name\": \"Иван\", \"grade\": 5}\n\nВыведите значение по ключу \"name\".\n\nОжидаемый вывод: Иван", "starterCode": "# Создайте словарь student\n\n# Выведите имя\n", "expectedOutput": "Иван", "hint": "student = {\"name\": \"Иван\", \"grade\": 5}\nprint(student[\"name\"])"},
                    {"type": "python-coding", "prompt": "Создайте словарь ages = {\"Алиса\": 25, \"Боб\": 30, \"Карл\": 28}.\nВыведите количество элементов с помощью len().\n\nlen() для словаря возвращает количество пар ключ-значение.\n\nОжидаемый вывод: 3", "starterCode": "# Создайте словарь ages\n\n# Выведите количество элементов\n", "expectedOutput": "3", "hint": "ages = {\"Алиса\": 25, \"Боб\": 30, \"Карл\": 28}\nprint(len(ages))"},
                    {"type": "python-coding", "prompt": "Создайте словарь fruit_colors = {\"яблоко\": \"красный\", \"банан\": \"жёлтый\"}.\nДобавьте новую пару: \"груша\": \"зелёный\".\nВыведите весь словарь.\n\nДобавление: словарь[\"новый_ключ\"] = \"значение\"\n\nОжидаемый вывод: {'яблоко': 'красный', 'банан': 'жёлтый', 'груша': 'зелёный'}", "starterCode": "# Создайте словарь\n\n# Добавьте грушу\n\n# Выведите словарь\n", "expectedOutput": "{'яблоко': 'красный', 'банан': 'жёлтый', 'груша': 'зелёный'}", "hint": "fruit_colors = {\"яблоко\": \"красный\", \"банан\": \"жёлтый\"}\nfruit_colors[\"груша\"] = \"зелёный\"\nprint(fruit_colors)"},
                    {"type": "quiz", "question": "Как получить значение из словаря по ключу?", "options": [{"id": "a", "text": "dict.key", "correct": False}, {"id": "b", "text": "dict[key]", "correct": True}, {"id": "c", "text": "dict(key)", "correct": False}, {"id": "d", "text": "dict->key", "correct": False}]}
                ]
            },
            {
                "title": "Перебор и вложенные словари",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Словари Python", "url": "https://www.youtube.com/watch?v=W2oO1Y-QDzo"},
                    {"type": "info", "title": "Перебор словарей", "markdown": "## Перебор словаря\n\n### Перебор ключей\n```python\nages = {\"Алиса\": 25, \"Боб\": 30}\nfor name in ages:\n    print(name)\n# Алиса\n# Боб\n```\n\n### Перебор пар (ключ, значение)\n```python\nfor name, age in ages.items():\n    print(f\"{name}: {age} лет\")\n# Алиса: 25 лет\n# Боб: 30 лет\n```\n\n### Перебор только значений\n```python\nfor age in ages.values():\n    print(age)\n# 25\n# 30\n```\n\n## Вложенные словари\n```python\nstudents = {\n    \"Алиса\": {\"age\": 20, \"grade\": \"A\"},\n    \"Боб\": {\"age\": 22, \"grade\": \"B\"}\n}\n\nprint(students[\"Алиса\"][\"grade\"])  # A\n```\n\n## Dict comprehension\n```python\nsquares = {x: x**2 for x in range(1, 6)}\nprint(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n```"},
                    {"type": "python-coding", "prompt": "Создайте словарь scores = {\"math\": 90, \"english\": 85, \"science\": 92}.\nИспользуя цикл for и .values(), вычислите и выведите сумму всех значений.\n\nМожно использовать sum(scores.values()) или цикл.\n90 + 85 + 92 = 267\n\nОжидаемый вывод: 267", "starterCode": "scores = {\"math\": 90, \"english\": 85, \"science\": 92}\n# Выведите сумму значений\n", "expectedOutput": "267", "hint": "scores = {\"math\": 90, \"english\": 85, \"science\": 92}\nprint(sum(scores.values()))"},
                    {"type": "python-coding", "prompt": "Создайте dict comprehension: словарь, где ключи — числа от 1 до 5, а значения — их кубы (x**3).\n\ncubes = {x: x**3 for x in range(1, 6)}\n\nОжидаемый вывод: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}", "starterCode": "# Dict comprehension: числа и их кубы\n", "expectedOutput": "{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}", "hint": "cubes = {x: x**3 for x in range(1, 6)}\nprint(cubes)"},
                    {"type": "python-coding", "prompt": "Создайте словарь data = {\"a\": 1, \"b\": 2, \"c\": 3}.\nВыведите все ключи словаря используя list(data.keys()).\n\nОжидаемый вывод: ['a', 'b', 'c']", "starterCode": "# Создайте словарь и выведите ключи\n", "expectedOutput": "['a', 'b', 'c']", "hint": "data = {\"a\": 1, \"b\": 2, \"c\": 3}\nprint(list(data.keys()))"},
                    {"type": "quiz", "question": "Что возвращает метод .items() словаря?", "options": [{"id": "a", "text": "Список ключей", "correct": False}, {"id": "b", "text": "Список значений", "correct": False}, {"id": "c", "text": "Пары (ключ, значение)", "correct": True}, {"id": "d", "text": "Количество элементов", "correct": False}]}
                ]
            },
            {
                "title": "Множества — set",
                "xp": 25,
                "steps": [
                    {"type": "video", "title": "Словари Python", "url": "https://www.youtube.com/watch?v=W2oO1Y-QDzo"},
                    {"type": "info", "title": "Множества (set)", "markdown": "## Множества в Python\n\nМножество — неупорядоченная коллекция **уникальных** элементов.\n\n### Создание\n```python\nfruits = {\"яблоко\", \"банан\", \"груша\"}\nnumbers = set([1, 2, 2, 3, 3, 3])\nprint(numbers)  # {1, 2, 3} — дубликаты удалены!\n```\n\n### Операции с множествами\n```python\na = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\n\nprint(a | b)  # Объединение: {1, 2, 3, 4, 5, 6}\nprint(a & b)  # Пересечение: {3, 4}\nprint(a - b)  # Разность: {1, 2}\n```\n\n### Добавление и удаление\n```python\nfruits = {\"яблоко\", \"банан\"}\nfruits.add(\"груша\")\nfruits.discard(\"банан\")\n```\n\n### Удаление дубликатов из списка\n```python\nmy_list = [1, 2, 2, 3, 3, 3]\nunique = list(set(my_list))\nprint(sorted(unique))  # [1, 2, 3]\n```\n\n### Проверка принадлежности (быстро!)\n```python\nprint(\"яблоко\" in fruits)  # True — O(1) по скорости\n```"},
                    {"type": "python-coding", "prompt": "Создайте список с дубликатами: numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]\nПреобразуйте в множество, затем обратно в отсортированный список и выведите.\n\nset() удаляет дубликаты, sorted() сортирует.\n\nОжидаемый вывод: [1, 2, 3, 4]", "starterCode": "numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]\n# Удалите дубликаты и отсортируйте\n", "expectedOutput": "[1, 2, 3, 4]", "hint": "numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]\nprint(sorted(set(numbers)))"},
                    {"type": "python-coding", "prompt": "Найдите пересечение двух множеств:\na = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n\nПересечение (& или .intersection()) — элементы, которые есть в обоих множествах.\nВыведите отсортированный список пересечения.\n\nОжидаемый вывод: [4, 5]", "starterCode": "a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n# Найдите пересечение\n", "expectedOutput": "[4, 5]", "hint": "a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\nprint(sorted(a & b))"},
                    {"type": "python-coding", "prompt": "Создайте множество vowels = {\"a\", \"e\", \"i\", \"o\", \"u\"}.\nПроверьте, есть ли буква \"e\" в множестве, и выведите результат.\n\nОператор in проверяет принадлежность к множеству.\n\nОжидаемый вывод: True", "starterCode": "# Создайте множество гласных\n\n# Проверьте наличие \"e\"\n", "expectedOutput": "True", "hint": "vowels = {\"a\", \"e\", \"i\", \"o\", \"u\"}\nprint(\"e\" in vowels)"},
                    {"type": "quiz", "question": "Что произойдёт при добавлении дубликата в множество?", "options": [{"id": "a", "text": "Ошибка", "correct": False}, {"id": "b", "text": "Элемент добавится дважды", "correct": False}, {"id": "c", "text": "Ничего — дубликат будет проигнорирован", "correct": True}, {"id": "d", "text": "Старый элемент заменится", "correct": False}]}
                ]
            }
        ]
    },
    # ==================== SECTION 8: Работа с файлами и модулями ====================
    {
        "title": "Файлы и модули",
        "lessons": [
            {
                "title": "Чтение и запись файлов",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Python для начинающих — полный курс", "url": "https://www.youtube.com/watch?v=wDmPgXhlDIg"},
                    {"type": "info", "title": "Работа с файлами", "markdown": "## Файлы в Python\n\n### Открытие файла\n```python\nfile = open(\"data.txt\", \"r\")  # r = чтение\ncontent = file.read()\nfile.close()\n```\n\n### Менеджер контекста (рекомендуется!)\n```python\nwith open(\"data.txt\", \"r\") as file:\n    content = file.read()\n# файл автоматически закроется\n```\n\n### Режимы открытия\n| Режим | Описание |\n|-------|----------|\n| `\"r\"` | Чтение (файл должен существовать) |\n| `\"w\"` | Запись (создаёт/перезаписывает) |\n| `\"a\"` | Дополнение (добавляет в конец) |\n| `\"r+\"` | Чтение и запись |\n\n### Чтение\n```python\nwith open(\"file.txt\") as f:\n    # Весь файл как строка\n    content = f.read()\n    \n    # Построчно в список\n    lines = f.readlines()\n    \n    # Построчно в цикле\n    for line in f:\n        print(line.strip())\n```\n\n### Запись\n```python\nwith open(\"output.txt\", \"w\") as f:\n    f.write(\"Первая строка\\n\")\n    f.write(\"Вторая строка\\n\")\n```\n\n### Запись списка строк\n```python\nlines = [\"строка 1\\n\", \"строка 2\\n\", \"строка 3\\n\"]\nwith open(\"output.txt\", \"w\") as f:\n    f.writelines(lines)\n```"},
                    {"type": "python-coding", "prompt": "Напишите программу, которая создаёт строку из 3 строк и выводит количество строк.\n\nИспользуйте многострочную строку и метод .splitlines():\ntext = \"Строка 1\\nСтрока 2\\nСтрока 3\"\nlines = text.splitlines()\nprint(len(lines))\n\n.splitlines() разбивает текст на список строк.\n\nОжидаемый вывод: 3", "starterCode": "# Создайте многострочную строку и посчитайте строки\n", "expectedOutput": "3", "hint": "text = \"Строка 1\\nСтрока 2\\nСтрока 3\"\nlines = text.splitlines()\nprint(len(lines))"},
                    {"type": "python-coding", "prompt": "Используя метод .split(), разбейте строку \"Python Java C++ Go Rust\" по пробелам и выведите количество слов.\n\n.split() без аргументов разбивает по пробелам.\n\nОжидаемый вывод: 5", "starterCode": "text = \"Python Java C++ Go Rust\"\n# Разбейте на слова и выведите количество\n", "expectedOutput": "5", "hint": "text = \"Python Java C++ Go Rust\"\nwords = text.split()\nprint(len(words))"},
                    {"type": "python-coding", "prompt": "Используя метод .join(), соедините список слов [\"Hello\", \"World\", \"Python\"] через пробел и выведите результат.\n\n\" \".join(список) — соединяет элементы списка через пробел.\n\nОжидаемый вывод: Hello World Python", "starterCode": "words = [\"Hello\", \"World\", \"Python\"]\n# Соедините через пробел\n", "expectedOutput": "Hello World Python", "hint": "words = [\"Hello\", \"World\", \"Python\"]\nprint(\" \".join(words))"},
                    {"type": "quiz", "question": "Какой менеджер контекста рекомендуется для работы с файлами?", "options": [{"id": "a", "text": "try/except", "correct": False}, {"id": "b", "text": "with open() as f:", "correct": True}, {"id": "c", "text": "file.open()", "correct": False}, {"id": "d", "text": "import file", "correct": False}]}
                ]
            },
            {
                "title": "Модули и импорт",
                "xp": 30,
                "steps": [
                    {"type": "video", "title": "Python за 1 час — основы", "url": "https://www.youtube.com/watch?v=34Rp6KVGIEM"},
                    {"type": "info", "title": "Модули Python", "markdown": "## Модули\n\nМодуль — это файл с Python-кодом, который можно импортировать.\n\n### Импорт модуля\n```python\nimport math\nprint(math.pi)      # 3.141592653589793\nprint(math.sqrt(16))  # 4.0\n```\n\n### Импорт конкретных функций\n```python\nfrom math import sqrt, pi\nprint(sqrt(25))  # 5.0\nprint(pi)        # 3.14159...\n```\n\n### Импорт с псевдонимом\n```python\nimport math as m\nprint(m.pi)  # 3.14159...\n```\n\n### Популярные встроенные модули\n| Модуль | Назначение |\n|--------|------------|\n| `math` | Математические функции |\n| `random` | Случайные числа |\n| `datetime` | Дата и время |\n| `os` | Работа с ОС |\n| `json` | Работа с JSON |\n\n### Модуль random\n```python\nimport random\nprint(random.randint(1, 10))  # случайное от 1 до 10\nprint(random.choice([\"a\", \"b\", \"c\"]))  # случайный элемент\n```\n\n### Модуль datetime\n```python\nfrom datetime import datetime\nnow = datetime.now()\nprint(now.year)  # текущий год\n```"},
                    {"type": "python-coding", "prompt": "Импортируйте модуль math и выведите значение math.pi округлённое до 2 знаков.\n\nround(число, знаков) — округляет число.\nmath.pi ≈ 3.141592653589793\nround(math.pi, 2) = 3.14\n\nОжидаемый вывод: 3.14", "starterCode": "# Импортируйте math и выведите pi\n", "expectedOutput": "3.14", "hint": "import math\nprint(round(math.pi, 2))"},
                    {"type": "python-coding", "prompt": "Импортируйте функцию sqrt из модуля math и вычислите квадратный корень из 144.\n\nfrom math import sqrt\nsqrt(144) = 12.0\n\nВыведите целое число: int(sqrt(144))\n\nОжидаемый вывод: 12", "starterCode": "# Импортируйте sqrt и вычислите корень из 144\n", "expectedOutput": "12", "hint": "from math import sqrt\nprint(int(sqrt(144)))"},
                    {"type": "python-coding", "prompt": "Импортируйте модуль math и вычислите факториал числа 5.\n\nmath.factorial(5) = 5! = 5*4*3*2*1 = 120\n\nОжидаемый вывод: 120", "starterCode": "# Импортируйте math и вычислите факториал 5\n", "expectedOutput": "120", "hint": "import math\nprint(math.factorial(5))"},
                    {"type": "quiz", "question": "Как импортировать только функцию sqrt из модуля math?", "options": [{"id": "a", "text": "import sqrt from math", "correct": False}, {"id": "b", "text": "from math import sqrt", "correct": True}, {"id": "c", "text": "import math.sqrt", "correct": False}, {"id": "d", "text": "using math.sqrt", "correct": False}]}
                ]
            },
            {
                "title": "Обработка ошибок — try/except",
                "xp": 35,
                "steps": [
                    {"type": "video", "title": "Python для начинающих — полный курс", "url": "https://www.youtube.com/watch?v=wDmPgXhlDIg"},
                    {"type": "info", "title": "Обработка исключений", "markdown": "## Try / Except\n\nОшибки (исключения) можно перехватывать, чтобы программа не падала:\n\n```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Деление на ноль!\")\n```\n\n### Несколько типов ошибок\n```python\ntry:\n    number = int(\"abc\")\nexcept ValueError:\n    print(\"Невозможно преобразовать в число\")\nexcept TypeError:\n    print(\"Неверный тип\")\n```\n\n### Общий except\n```python\ntry:\n    # опасный код\n    x = 1 / 0\nexcept Exception as e:\n    print(f\"Ошибка: {e}\")\n```\n\n### else и finally\n```python\ntry:\n    result = 10 / 2\nexcept ZeroDivisionError:\n    print(\"Ошибка!\")\nelse:\n    print(f\"Результат: {result}\")  # если НЕ было ошибки\nfinally:\n    print(\"Выполняется всегда\")  # в любом случае\n```\n\n### Типичные исключения\n| Исключение | Причина |\n|------------|----------|\n| `ZeroDivisionError` | Деление на 0 |\n| `ValueError` | Неверное значение |\n| `TypeError` | Неверный тип |\n| `IndexError` | Индекс за пределами |\n| `KeyError` | Ключ не найден |\n| `FileNotFoundError` | Файл не найден |"},
                    {"type": "python-coding", "prompt": "Напишите try/except, который пытается преобразовать строку \"hello\" в число с помощью int().\nПри ошибке ValueError выведите: Ошибка преобразования\n\nint(\"hello\") вызовет ValueError, потому что \"hello\" — не число.\n\nОжидаемый вывод: Ошибка преобразования", "starterCode": "# Попробуйте преобразовать \"hello\" в число\n", "expectedOutput": "Ошибка преобразования", "hint": "try:\n    number = int(\"hello\")\nexcept ValueError:\n    print(\"Ошибка преобразования\")"},
                    {"type": "python-coding", "prompt": "Напишите try/except для деления 100 на 0.\nПри ZeroDivisionError выведите: Нельзя делить на ноль\n\n100 / 0 вызовет ZeroDivisionError.\n\nОжидаемый вывод: Нельзя делить на ноль", "starterCode": "# Попробуйте разделить 100 на 0\n", "expectedOutput": "Нельзя делить на ноль", "hint": "try:\n    result = 100 / 0\nexcept ZeroDivisionError:\n    print(\"Нельзя делить на ноль\")"},
                    {"type": "python-coding", "prompt": "Напишите try/except/else:\n- try: вычислите result = 50 // 5\n- except: выведите \"Ошибка\"\n- else: выведите значение result\n\n50 // 5 = 10 (ошибки нет, выполнится блок else)\n\nОжидаемый вывод: 10", "starterCode": "# try/except/else\n", "expectedOutput": "10", "hint": "try:\n    result = 50 // 5\nexcept ZeroDivisionError:\n    print(\"Ошибка\")\nelse:\n    print(result)"},
                    {"type": "quiz", "question": "Какой блок выполняется только если НЕ было исключения?", "options": [{"id": "a", "text": "except", "correct": False}, {"id": "b", "text": "finally", "correct": False}, {"id": "c", "text": "else", "correct": True}, {"id": "d", "text": "try", "correct": False}]}
                ]
            },
            {
                "title": "Финальный проект — всё вместе",
                "xp": 50,
                "steps": [
                    {"type": "video", "title": "Python за 1 час — программирование для начинающих", "url": "https://www.youtube.com/watch?v=34Rp6KVGIEM"},
                    {"type": "info", "title": "Финальный проект", "markdown": "## Поздравляем!\n\nВы изучили все основы Python:\n- print() и комментарии\n- Переменные и типы данных\n- Условия if/elif/else\n- Циклы for и while\n- Списки и кортежи\n- Функции и lambda\n- Словари и множества\n- Файлы и модули\n- Обработка ошибок\n\n## Теперь давайте объединим всё!\n\nФинальные задания проверят ваше понимание всех тем. Каждое задание использует несколько концепций одновременно.\n\n### Советы:\n- Разбивайте задачу на шаги\n- Используйте функции для организации кода\n- Не забывайте про обработку ошибок\n- Тестируйте код мысленно перед запуском"},
                    {"type": "python-coding", "prompt": "Создайте функцию count_vowels(text), которая считает количество гласных (a, e, i, o, u) в строке.\nВызовите: print(count_vowels(\"Hello World\"))\n\nАлгоритм:\n1. Создайте переменную count = 0\n2. Переберите каждый символ строки в цикле for\n3. Если символ.lower() в множестве гласных — увеличьте count\n4. Верните count\n\n\"Hello World\" содержит: e, o, o = 3 гласных\n\nОжидаемый вывод: 3", "starterCode": "# Функция подсчёта гласных\n\n\n\n# Тест\n", "expectedOutput": "3", "hint": "def count_vowels(text):\n    count = 0\n    vowels = \"aeiou\"\n    for char in text:\n        if char.lower() in vowels:\n            count += 1\n    return count\n\nprint(count_vowels(\"Hello World\"))"},
                    {"type": "python-coding", "prompt": "Создайте функцию fizzbuzz(n), которая для каждого числа от 1 до n:\n- Если делится на 3 и 5 — выводит \"FizzBuzz\"\n- Если только на 3 — выводит \"Fizz\"\n- Если только на 5 — выводит \"Buzz\"\n- Иначе — выводит само число\n\nВызовите fizzbuzz(15). Последние 5 строк вывода будут:\n11\nFizz\n13\n14\nFizzBuzz\n\nОжидаемый вывод:\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz", "starterCode": "# Функция FizzBuzz\n\n\n\n# Запуск\n", "expectedOutput": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz", "hint": "def fizzbuzz(n):\n    for i in range(1, n + 1):\n        if i % 3 == 0 and i % 5 == 0:\n            print(\"FizzBuzz\")\n        elif i % 3 == 0:\n            print(\"Fizz\")\n        elif i % 5 == 0:\n            print(\"Buzz\")\n        else:\n            print(i)\n\nfizzbuzz(15)"},
                    {"type": "python-coding", "prompt": "Создайте функцию reverse_words(text), которая переворачивает порядок слов в строке.\n\nАлгоритм:\n1. Разбейте строку на слова: text.split()\n2. Переверните список: [::-1] или .reverse()\n3. Соедините обратно: \" \".join()\n\nВызовите: print(reverse_words(\"Hello World Python\"))\n\nОжидаемый вывод: Python World Hello", "starterCode": "# Функция переворота слов\n\n\n\n# Тест\n", "expectedOutput": "Python World Hello", "hint": "def reverse_words(text):\n    words = text.split()\n    return \" \".join(words[::-1])\n\nprint(reverse_words(\"Hello World Python\"))"},
                    {"type": "quiz", "question": "Что проверяет оператор x % 3 == 0?", "options": [{"id": "a", "text": "x равно 3", "correct": False}, {"id": "b", "text": "x больше 3", "correct": False}, {"id": "c", "text": "x делится на 3 без остатка", "correct": True}, {"id": "d", "text": "x не равно 3", "correct": False}]}
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
            description="Полный курс Python с видео-уроками и интерактивными coding-упражнениями. Смотрите видео, изучайте теорию, пишите и запускайте код прямо в браузере!",
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
