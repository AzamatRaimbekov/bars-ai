"""Seed: SQL и базы данных — 7 sections, ~40 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "SQL и базы данных"
DESC = (
    "Полный курс по SQL: от SELECT до оптимизации запросов. PostgreSQL, проектирование БД, "
    "индексы, транзакции, нормализация. Практика на реальных примерах."
)

S = [
    # ==================== SECTION 1: Введение в базы данных ====================
    {
        "title": "Введение в базы данных",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое база данных?",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Знакомство с базами данных", "markdown": "## Что такое база данных?\n\n**База данных (БД)** — организованная коллекция данных, хранящаяся и доступная в электронном виде.\n\n### Зачем нужны базы данных?\n- **Хранение** — надёжное сохранение больших объёмов данных\n- **Поиск** — быстрый доступ к нужной информации\n- **Целостность** — данные остаются корректными и непротиворечивыми\n- **Многопользовательский доступ** — несколько пользователей работают одновременно\n\n### Примеры баз данных в реальной жизни:\n- **Интернет-магазин** — товары, заказы, пользователи\n- **Банк** — счета, транзакции, клиенты\n- **Социальная сеть** — профили, посты, друзья\n- **Больница** — пациенты, диагнозы, назначения\n\n### Системы управления базами данных (СУБД):\nСУБД — программа для создания, управления и доступа к базам данных.\n\nПопулярные СУБД:\n- **PostgreSQL** — мощная, бесплатная, open-source\n- **MySQL** — самая распространённая\n- **SQLite** — встроенная, без сервера\n- **Microsoft SQL Server** — корпоративная\n- **Oracle** — для крупных предприятий"},
                    {"type": "quiz", "question": "Что такое СУБД?", "options": [{"id": "a", "text": "Язык программирования", "correct": False}, {"id": "b", "text": "Программа для управления базами данных", "correct": True}, {"id": "c", "text": "Операционная система", "correct": False}, {"id": "d", "text": "Текстовый редактор", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Интернет-магазин", "right": "Товары, заказы, пользователи"}, {"left": "Банк", "right": "Счета, транзакции, клиенты"}, {"left": "Соцсеть", "right": "Профили, посты, друзья"}, {"left": "Больница", "right": "Пациенты, диагнозы"}]},
                    {"type": "true-false", "statement": "База данных — это просто текстовый файл на компьютере.", "correct": False},
                ],
            },
            {
                "t": "Реляционные базы данных",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Реляционная модель", "markdown": "## Реляционные базы данных\n\n**Реляционная БД** хранит данные в виде **таблиц** (отношений), связанных между собой.\n\n### Основные понятия:\n- **Таблица (Table)** — набор данных одного типа\n- **Строка (Row / Record)** — одна запись в таблице\n- **Столбец (Column / Field)** — одно свойство данных\n- **Первичный ключ (Primary Key)** — уникальный идентификатор строки\n- **Внешний ключ (Foreign Key)** — ссылка на строку в другой таблице\n\n### Пример таблицы `users`:\n```\n| id | name     | email            | age |\n|----|----------|------------------|-----|\n| 1  | Алексей  | alex@mail.ru     | 25  |\n| 2  | Мария    | maria@gmail.com  | 30  |\n| 3  | Иван     | ivan@yandex.ru   | 22  |\n```\n\n- `id` — первичный ключ (уникален для каждой строки)\n- Каждая строка — один пользователь\n- Каждый столбец — одно свойство\n\n### Преимущества реляционных БД:\n- Строгая структура данных\n- Мощный язык запросов (SQL)\n- Поддержка связей между таблицами\n- Гарантия целостности данных"},
                    {"type": "flashcards", "cards": [{"front": "Table (Таблица)", "back": "Набор данных одного типа, состоящий из строк и столбцов"}, {"front": "Row (Строка)", "back": "Одна запись в таблице, представляющая один объект"}, {"front": "Column (Столбец)", "back": "Одно свойство данных, одинаковое для всех строк"}, {"front": "Primary Key", "back": "Уникальный идентификатор строки в таблице"}, {"front": "Foreign Key", "back": "Ссылка на строку в другой таблице"}]},
                    {"type": "quiz", "question": "Что является уникальным идентификатором строки в таблице?", "options": [{"id": "a", "text": "Foreign Key", "correct": False}, {"id": "b", "text": "Primary Key", "correct": True}, {"id": "c", "text": "Index", "correct": False}, {"id": "d", "text": "Column", "correct": False}]},
                    {"type": "category-sort", "categories": ["Реляционные СУБД", "Нереляционные СУБД"], "items": [{"text": "PostgreSQL", "category": "Реляционные СУБД"}, {"text": "MongoDB", "category": "Нереляционные СУБД"}, {"text": "MySQL", "category": "Реляционные СУБД"}, {"text": "Redis", "category": "Нереляционные СУБД"}, {"text": "SQLite", "category": "Реляционные СУБД"}, {"text": "Cassandra", "category": "Нереляционные СУБД"}]},
                ],
            },
            {
                "t": "SQL vs NoSQL",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Сравнение SQL и NoSQL", "markdown": "## SQL vs NoSQL\n\n### SQL (реляционные БД):\n- Данные хранятся в **таблицах** со строгой схемой\n- Используют язык **SQL** для запросов\n- **ACID-транзакции** гарантируют надёжность\n- Примеры: PostgreSQL, MySQL, SQLite\n\n### NoSQL (нереляционные БД):\n- Гибкая структура данных (документы, ключ-значение, графы)\n- Нет строгой схемы — можно добавлять поля на лету\n- Горизонтальное масштабирование\n- Примеры: MongoDB, Redis, Cassandra\n\n### Когда использовать SQL:\n- Сложные связи между данными\n- Финансовые транзакции\n- Чёткая, предсказуемая структура\n- Нужна целостность данных\n\n### Когда использовать NoSQL:\n- Большие объёмы неструктурированных данных\n- Быстрое прототипирование\n- Кэширование (Redis)\n- Реальное время (чаты, IoT)\n\n### ACID:\n- **A**tomicity — атомарность (всё или ничего)\n- **C**onsistency — согласованность\n- **I**solation — изолированность\n- **D**urability — долговечность"},
                    {"type": "flashcards", "cards": [{"front": "Atomicity (Атомарность)", "back": "Транзакция выполняется целиком или не выполняется вовсе"}, {"front": "Consistency (Согласованность)", "back": "БД переходит из одного корректного состояния в другое"}, {"front": "Isolation (Изолированность)", "back": "Параллельные транзакции не влияют друг на друга"}, {"front": "Durability (Долговечность)", "back": "Результат транзакции сохраняется даже при сбоях"}]},
                    {"type": "true-false", "statement": "NoSQL базы данных всегда лучше SQL.", "correct": False},
                    {"type": "multi-select", "question": "Какие из этих БД относятся к NoSQL?", "options": [{"id": "a", "text": "MongoDB", "correct": True}, {"id": "b", "text": "PostgreSQL", "correct": False}, {"id": "c", "text": "Redis", "correct": True}, {"id": "d", "text": "MySQL", "correct": False}, {"id": "e", "text": "Cassandra", "correct": True}]},
                ],
            },
            {
                "t": "Установка PostgreSQL",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Установка и настройка PostgreSQL", "markdown": "## Установка PostgreSQL\n\n### Windows:\n1. Скачайте установщик с [postgresql.org](https://www.postgresql.org/download/)\n2. Запустите и следуйте инструкциям\n3. Запомните пароль для пользователя `postgres`\n4. Порт по умолчанию: **5432**\n\n### macOS:\n```bash\nbrew install postgresql@16\nbrew services start postgresql@16\n```\n\n### Linux (Ubuntu):\n```bash\nsudo apt update\nsudo apt install postgresql postgresql-contrib\nsudo systemctl start postgresql\n```\n\n### Проверка установки:\n```bash\npsql --version\n```\nВывод: `psql (PostgreSQL) 16.x`\n\n### Подключение к PostgreSQL:\n```bash\n# Вход под пользователем postgres\nsudo -u postgres psql\n\n# Или с указанием хоста\npsql -h localhost -U postgres\n```\n\n### Графические клиенты:\n- **pgAdmin** — официальный, бесплатный\n- **DBeaver** — универсальный, поддерживает многие СУБД\n- **DataGrip** — от JetBrains, платный"},
                    {"type": "drag-order", "items": ["Скачать установщик PostgreSQL", "Запустить установку", "Задать пароль для postgres", "Выбрать порт 5432", "Проверить: psql --version"]},
                    {"type": "quiz", "question": "Какой порт по умолчанию использует PostgreSQL?", "options": [{"id": "a", "text": "3306", "correct": False}, {"id": "b", "text": "5432", "correct": True}, {"id": "c", "text": "27017", "correct": False}, {"id": "d", "text": "8080", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для подключения к PostgreSQL из терминала используется команда ___.", "answer": "psql"},
                ],
            },
            {
                "t": "Первые SQL-команды",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Базовые команды SQL и psql", "markdown": "## Первые команды\n\n### Команды psql (начинаются с \\):\n```sql\n\\l          -- список баз данных\n\\dt         -- список таблиц\n\\d users    -- структура таблицы users\n\\c mydb     -- подключиться к базе mydb\n\\q          -- выход из psql\n```\n\n### Создание базы данных:\n```sql\nCREATE DATABASE myshop;\n```\n\n### Подключение к базе:\n```sql\n\\c myshop\n```\n\n### Создание таблицы:\n```sql\nCREATE TABLE users (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    email VARCHAR(255) UNIQUE,\n    age INTEGER\n);\n```\n\n### Вставка данных:\n```sql\nINSERT INTO users (name, email, age)\nVALUES ('Алексей', 'alex@mail.ru', 25);\n```\n\n### Просмотр данных:\n```sql\nSELECT * FROM users;\n```\n\nSQL-команды заканчиваются точкой с запятой `;`"},
                    {"type": "code-puzzle", "instructions": "Соберите SQL-запрос для создания базы данных myshop", "correctOrder": ["CREATE DATABASE myshop;"]},
                    {"type": "matching", "pairs": [{"left": "\\l", "right": "Список баз данных"}, {"left": "\\dt", "right": "Список таблиц"}, {"left": "\\c mydb", "right": "Подключиться к базе"}, {"left": "\\q", "right": "Выход из psql"}]},
                    {"type": "true-false", "statement": "SQL-команды не обязательно заканчивать точкой с запятой.", "correct": False},
                    {"type": "fill-blank", "sentence": "Команда CREATE ___ создаёт новую базу данных.", "answer": "DATABASE"},
                ],
            },
        ],
    },
    # ==================== SECTION 2: SELECT и фильтрация ====================
    {
        "title": "SELECT и фильтрация",
        "pos": 1,
        "lessons": [
            {
                "t": "Оператор SELECT",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Основы SELECT", "markdown": "## Оператор SELECT\n\n**SELECT** — основной оператор для чтения данных из таблицы.\n\n### Выбрать все столбцы:\n```sql\nSELECT * FROM users;\n```\n\n### Выбрать конкретные столбцы:\n```sql\nSELECT name, email FROM users;\n```\n\n### Псевдонимы столбцов (AS):\n```sql\nSELECT name AS имя, age AS возраст\nFROM users;\n```\n\n### Уникальные значения (DISTINCT):\n```sql\nSELECT DISTINCT city FROM users;\n```\n\n### Вычисления в SELECT:\n```sql\nSELECT name, age, age * 12 AS age_months\nFROM users;\n```\n\n### Порядок выполнения запроса:\n1. `FROM` — откуда берём данные\n2. `WHERE` — фильтрация (позже)\n3. `SELECT` — какие столбцы показать\n4. `ORDER BY` — сортировка (позже)\n5. `LIMIT` — ограничение (позже)"},
                    {"type": "code-puzzle", "instructions": "Соберите запрос для выбора имён и email из таблицы users", "correctOrder": ["SELECT name, email", "FROM users;"]},
                    {"type": "quiz", "question": "Что делает ключевое слово DISTINCT?", "options": [{"id": "a", "text": "Сортирует результаты", "correct": False}, {"id": "b", "text": "Убирает дубликаты", "correct": True}, {"id": "c", "text": "Ограничивает количество строк", "correct": False}, {"id": "d", "text": "Переименовывает столбец", "correct": False}]},
                    {"type": "fill-blank", "sentence": "SELECT * FROM users выбирает ___ столбцы из таблицы.", "answer": "все"},
                ],
            },
            {
                "t": "WHERE — фильтрация строк",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Фильтрация с WHERE", "markdown": "## WHERE — фильтрация строк\n\n**WHERE** позволяет выбрать только строки, удовлетворяющие условию.\n\n### Операторы сравнения:\n```sql\nSELECT * FROM users WHERE age > 25;\nSELECT * FROM users WHERE age >= 18;\nSELECT * FROM users WHERE name = 'Алексей';\nSELECT * FROM users WHERE age != 30;\n-- Или: age <> 30\n```\n\n### Логические операторы:\n```sql\n-- AND — оба условия должны быть истинны\nSELECT * FROM users\nWHERE age >= 18 AND city = 'Москва';\n\n-- OR — хотя бы одно условие истинно\nSELECT * FROM users\nWHERE city = 'Москва' OR city = 'Питер';\n\n-- NOT — отрицание\nSELECT * FROM users\nWHERE NOT city = 'Москва';\n```\n\n### BETWEEN — диапазон:\n```sql\nSELECT * FROM users\nWHERE age BETWEEN 18 AND 30;\n```\n\n### IN — список значений:\n```sql\nSELECT * FROM users\nWHERE city IN ('Москва', 'Питер', 'Казань');\n```\n\n### IS NULL / IS NOT NULL:\n```sql\nSELECT * FROM users WHERE email IS NULL;\nSELECT * FROM users WHERE email IS NOT NULL;\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: пользователи старше 18 из Москвы", "correctOrder": ["SELECT * FROM users", "WHERE age > 18", "AND city = 'Москва';"]},
                    {"type": "matching", "pairs": [{"left": "AND", "right": "Оба условия истинны"}, {"left": "OR", "right": "Хотя бы одно истинно"}, {"left": "BETWEEN", "right": "Значение в диапазоне"}, {"left": "IN", "right": "Значение из списка"}, {"left": "IS NULL", "right": "Значение пустое"}]},
                    {"type": "true-false", "statement": "Для проверки на NULL нужно использовать оператор = NULL.", "correct": False},
                    {"type": "multi-select", "question": "Какие операторы можно использовать в WHERE?", "options": [{"id": "a", "text": "AND", "correct": True}, {"id": "b", "text": "BETWEEN", "correct": True}, {"id": "c", "text": "AS", "correct": False}, {"id": "d", "text": "IN", "correct": True}, {"id": "e", "text": "DISTINCT", "correct": False}]},
                ],
            },
            {
                "t": "ORDER BY — сортировка",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Сортировка результатов", "markdown": "## ORDER BY — сортировка\n\n**ORDER BY** упорядочивает результаты запроса.\n\n### По возрастанию (ASC — по умолчанию):\n```sql\nSELECT * FROM users\nORDER BY age ASC;\n\n-- ASC можно опустить\nSELECT * FROM users\nORDER BY age;\n```\n\n### По убыванию (DESC):\n```sql\nSELECT * FROM users\nORDER BY age DESC;\n```\n\n### Сортировка по нескольким столбцам:\n```sql\nSELECT * FROM users\nORDER BY city ASC, age DESC;\n```\nСначала сортирует по городу (А-Я), при одинаковых городах — по возрасту (убывание).\n\n### Сортировка по номеру столбца:\n```sql\nSELECT name, age, city FROM users\nORDER BY 3, 2 DESC;\n-- 3 = city, 2 = age\n```\n\n### Сортировка строк:\nСтроки сортируются в алфавитном порядке с учётом локали."},
                    {"type": "quiz", "question": "Какое направление сортировки используется по умолчанию?", "options": [{"id": "a", "text": "DESC — по убыванию", "correct": False}, {"id": "b", "text": "ASC — по возрастанию", "correct": True}, {"id": "c", "text": "RANDOM — случайное", "correct": False}, {"id": "d", "text": "Без сортировки", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: отсортировать пользователей по возрасту по убыванию", "correctOrder": ["SELECT * FROM users", "ORDER BY age DESC;"]},
                    {"type": "fill-blank", "sentence": "Для сортировки по убыванию используется ключевое слово ___.", "answer": "DESC"},
                ],
            },
            {
                "t": "LIMIT и OFFSET",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Ограничение результатов", "markdown": "## LIMIT и OFFSET\n\n### LIMIT — ограничить количество строк:\n```sql\n-- Первые 10 пользователей\nSELECT * FROM users LIMIT 10;\n```\n\n### OFFSET — пропустить строки:\n```sql\n-- Пропустить 10, взять следующие 10\nSELECT * FROM users\nLIMIT 10 OFFSET 10;\n```\n\n### Пагинация:\n```sql\n-- Страница 1 (записи 1-10)\nSELECT * FROM users\nORDER BY id LIMIT 10 OFFSET 0;\n\n-- Страница 2 (записи 11-20)\nSELECT * FROM users\nORDER BY id LIMIT 10 OFFSET 10;\n\n-- Страница 3 (записи 21-30)\nSELECT * FROM users\nORDER BY id LIMIT 10 OFFSET 20;\n```\n\n### Формула пагинации:\n```\nOFFSET = (номер_страницы - 1) * количество_на_странице\n```\n\n### Топ-N запросы:\n```sql\n-- Три самых молодых пользователя\nSELECT name, age FROM users\nORDER BY age ASC\nLIMIT 3;\n```"},
                    {"type": "type-answer", "question": "Какой OFFSET нужен для 4-й страницы при 10 записях на страницу?", "acceptedAnswers": ["30"]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: топ-5 самых старших пользователей", "correctOrder": ["SELECT name, age FROM users", "ORDER BY age DESC", "LIMIT 5;"]},
                    {"type": "true-false", "statement": "OFFSET без LIMIT вызовет ошибку в PostgreSQL.", "correct": False},
                ],
            },
            {
                "t": "LIKE — поиск по шаблону",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Поиск по шаблону с LIKE", "markdown": "## LIKE — поиск по шаблону\n\n**LIKE** позволяет искать строки по шаблону.\n\n### Спецсимволы:\n- `%` — любое количество любых символов (включая 0)\n- `_` — ровно один любой символ\n\n### Примеры:\n```sql\n-- Имена, начинающиеся на 'А'\nSELECT * FROM users WHERE name LIKE 'А%';\n\n-- Имена, заканчивающиеся на 'ей'\nSELECT * FROM users WHERE name LIKE '%ей';\n\n-- Email содержит 'gmail'\nSELECT * FROM users WHERE email LIKE '%gmail%';\n\n-- Имена ровно из 4 букв\nSELECT * FROM users WHERE name LIKE '____';\n\n-- Второй символ 'а'\nSELECT * FROM users WHERE name LIKE '_а%';\n```\n\n### ILIKE — без учёта регистра (PostgreSQL):\n```sql\nSELECT * FROM users WHERE name ILIKE 'алексей';\n-- Найдёт: Алексей, АЛЕКСЕЙ, алексей\n```\n\n### NOT LIKE:\n```sql\nSELECT * FROM users WHERE email NOT LIKE '%gmail%';\n```"},
                    {"type": "matching", "pairs": [{"left": "%", "right": "Любое кол-во символов"}, {"left": "_", "right": "Ровно один символ"}, {"left": "LIKE 'А%'", "right": "Начинается на А"}, {"left": "LIKE '%ей'", "right": "Заканчивается на ей"}]},
                    {"type": "quiz", "question": "Что найдёт шаблон LIKE '____'?", "options": [{"id": "a", "text": "Строки длиной 4 символа", "correct": True}, {"id": "b", "text": "Любые строки", "correct": False}, {"id": "c", "text": "Пустые строки", "correct": False}, {"id": "d", "text": "Строки из 4 слов", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Оператор ___ в PostgreSQL позволяет искать без учёта регистра.", "answer": "ILIKE"},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: найти всех с email на gmail.com", "correctOrder": ["SELECT * FROM users", "WHERE email LIKE '%@gmail.com';"]},
                ],
            },
            {
                "t": "Агрегатные функции",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "COUNT, SUM, AVG, MIN, MAX", "markdown": "## Агрегатные функции\n\nАгрегатные функции обрабатывают набор строк и возвращают **одно значение**.\n\n### Основные функции:\n```sql\n-- COUNT — количество строк\nSELECT COUNT(*) FROM users;\nSELECT COUNT(email) FROM users; -- не считает NULL\n\n-- SUM — сумма\nSELECT SUM(salary) FROM employees;\n\n-- AVG — среднее значение\nSELECT AVG(age) FROM users;\n\n-- MIN и MAX\nSELECT MIN(age), MAX(age) FROM users;\n```\n\n### GROUP BY — группировка:\n```sql\n-- Количество пользователей по городам\nSELECT city, COUNT(*) AS total\nFROM users\nGROUP BY city;\n\n-- Средний возраст по городам\nSELECT city, AVG(age) AS avg_age\nFROM users\nGROUP BY city;\n```\n\n### HAVING — фильтрация групп:\n```sql\n-- Города с более чем 5 пользователями\nSELECT city, COUNT(*) AS total\nFROM users\nGROUP BY city\nHAVING COUNT(*) > 5;\n```\n\n### WHERE vs HAVING:\n- `WHERE` фильтрует **строки** до группировки\n- `HAVING` фильтрует **группы** после группировки"},
                    {"type": "matching", "pairs": [{"left": "COUNT", "right": "Количество строк"}, {"left": "SUM", "right": "Сумма значений"}, {"left": "AVG", "right": "Среднее значение"}, {"left": "MIN", "right": "Минимальное значение"}, {"left": "MAX", "right": "Максимальное значение"}]},
                    {"type": "quiz", "question": "В чём разница между WHERE и HAVING?", "options": [{"id": "a", "text": "Никакой разницы", "correct": False}, {"id": "b", "text": "WHERE — до группировки, HAVING — после", "correct": True}, {"id": "c", "text": "HAVING — для числовых, WHERE — для строковых", "correct": False}, {"id": "d", "text": "WHERE работает только с JOIN", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: количество пользователей по городам, где больше 3", "correctOrder": ["SELECT city, COUNT(*) AS total", "FROM users", "GROUP BY city", "HAVING COUNT(*) > 3;"]},
                    {"type": "type-answer", "question": "Какая агрегатная функция считает среднее значение?", "acceptedAnswers": ["AVG", "avg"]},
                    {"type": "true-false", "statement": "COUNT(email) считает строки, где email равен NULL.", "correct": False},
                ],
            },
        ],
    },
    # ==================== SECTION 3: JOIN и связи ====================
    {
        "title": "JOIN и связи таблиц",
        "pos": 2,
        "lessons": [
            {
                "t": "Типы связей между таблицами",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Связи в реляционных БД", "markdown": "## Типы связей между таблицами\n\nВ реляционных БД таблицы связаны через **внешние ключи** (Foreign Keys).\n\n### Один-к-одному (1:1):\nОдна запись в таблице A связана с одной записью в таблице B.\n```\nusers → user_profiles\nОдин пользователь — один профиль.\n```\n\n### Один-ко-многим (1:N):\nОдна запись в таблице A связана с несколькими в B.\n```\nauthors → books\nОдин автор — много книг.\n```\n```sql\nCREATE TABLE books (\n    id SERIAL PRIMARY KEY,\n    title VARCHAR(200),\n    author_id INTEGER REFERENCES authors(id)\n);\n```\n\n### Многие-ко-многим (M:N):\nМного записей в A связано с многими в B. Нужна **промежуточная таблица**.\n```\nstudents ↔ courses\nМного студентов — много курсов.\n```\n```sql\nCREATE TABLE student_courses (\n    student_id INTEGER REFERENCES students(id),\n    course_id INTEGER REFERENCES courses(id),\n    PRIMARY KEY (student_id, course_id)\n);\n```"},
                    {"type": "flashcards", "cards": [{"front": "Один-к-одному (1:1)", "back": "Одна запись в A связана с одной записью в B (user → profile)"}, {"front": "Один-ко-многим (1:N)", "back": "Одна запись в A связана с несколькими в B (author → books)"}, {"front": "Многие-ко-многим (M:N)", "back": "Много записей в A связано с многими в B через промежуточную таблицу"}]},
                    {"type": "quiz", "question": "Какая связь между таблицами students и courses?", "options": [{"id": "a", "text": "Один-к-одному", "correct": False}, {"id": "b", "text": "Один-ко-многим", "correct": False}, {"id": "c", "text": "Многие-ко-многим", "correct": True}, {"id": "d", "text": "Нет связи", "correct": False}]},
                    {"type": "category-sort", "categories": ["1:1", "1:N", "M:N"], "items": [{"text": "user → profile", "category": "1:1"}, {"text": "author → books", "category": "1:N"}, {"text": "students ↔ courses", "category": "M:N"}, {"text": "country → capital", "category": "1:1"}, {"text": "category → products", "category": "1:N"}, {"text": "actors ↔ movies", "category": "M:N"}]},
                ],
            },
            {
                "t": "INNER JOIN",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "INNER JOIN — внутреннее соединение", "markdown": "## INNER JOIN\n\n**INNER JOIN** возвращает только строки, для которых есть совпадение в **обеих** таблицах.\n\n### Синтаксис:\n```sql\nSELECT columns\nFROM table_a\nINNER JOIN table_b ON table_a.key = table_b.key;\n```\n\n### Пример:\nТаблицы:\n```\nusers:  | id | name    |\n        | 1  | Алексей |\n        | 2  | Мария   |\n        | 3  | Иван    |\n\norders: | id | user_id | product   |\n        | 1  | 1       | Ноутбук   |\n        | 2  | 1       | Мышка     |\n        | 3  | 2       | Клавиатура|\n```\n\n```sql\nSELECT users.name, orders.product\nFROM users\nINNER JOIN orders ON users.id = orders.user_id;\n```\n\nРезультат:\n```\n| name    | product    |\n| Алексей | Ноутбук    |\n| Алексей | Мышка      |\n| Мария   | Клавиатура |\n```\n\nИван (id=3) **не попал** в результат — у него нет заказов.\n\n### Псевдонимы таблиц:\n```sql\nSELECT u.name, o.product\nFROM users u\nINNER JOIN orders o ON u.id = o.user_id;\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите INNER JOIN запрос: имена пользователей и их заказы", "correctOrder": ["SELECT u.name, o.product", "FROM users u", "INNER JOIN orders o", "ON u.id = o.user_id;"]},
                    {"type": "true-false", "statement": "INNER JOIN вернёт строки, даже если нет совпадения в одной из таблиц.", "correct": False},
                    {"type": "quiz", "question": "Что произойдёт с пользователем без заказов при INNER JOIN?", "options": [{"id": "a", "text": "Появится с NULL-значениями", "correct": False}, {"id": "b", "text": "Не попадёт в результат", "correct": True}, {"id": "c", "text": "Вызовет ошибку", "correct": False}, {"id": "d", "text": "Появится с пустой строкой", "correct": False}]},
                    {"type": "fill-blank", "sentence": "INNER JOIN возвращает только строки с совпадениями в ___ таблицах.", "answer": "обеих"},
                ],
            },
            {
                "t": "LEFT и RIGHT JOIN",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "LEFT JOIN и RIGHT JOIN", "markdown": "## LEFT JOIN и RIGHT JOIN\n\n### LEFT JOIN (LEFT OUTER JOIN):\nВозвращает **все** строки из левой таблицы + совпадения из правой. Если совпадения нет — NULL.\n\n```sql\nSELECT u.name, o.product\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id;\n```\n\nРезультат:\n```\n| name    | product    |\n| Алексей | Ноутбук    |\n| Алексей | Мышка      |\n| Мария   | Клавиатура |\n| Иван    | NULL       |  ← нет заказов\n```\n\n### RIGHT JOIN (RIGHT OUTER JOIN):\nВозвращает **все** строки из правой таблицы + совпадения из левой.\n\n```sql\nSELECT u.name, o.product\nFROM users u\nRIGHT JOIN orders o ON u.id = o.user_id;\n```\n\n### Найти записи без связи:\n```sql\n-- Пользователи без заказов\nSELECT u.name\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id\nWHERE o.id IS NULL;\n```\n\n### На практике:\n- **LEFT JOIN** используется очень часто\n- **RIGHT JOIN** редко — можно всегда переписать как LEFT JOIN, поменяв таблицы местами"},
                    {"type": "quiz", "question": "Что будет в правых столбцах LEFT JOIN, если нет совпадения?", "options": [{"id": "a", "text": "Пустая строка", "correct": False}, {"id": "b", "text": "0", "correct": False}, {"id": "c", "text": "NULL", "correct": True}, {"id": "d", "text": "Ошибка", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: найти пользователей без заказов", "correctOrder": ["SELECT u.name", "FROM users u", "LEFT JOIN orders o ON u.id = o.user_id", "WHERE o.id IS NULL;"]},
                    {"type": "true-false", "statement": "RIGHT JOIN можно всегда переписать как LEFT JOIN, поменяв таблицы.", "correct": True},
                    {"type": "category-sort", "categories": ["INNER JOIN", "LEFT JOIN"], "items": [{"text": "Только совпадения", "category": "INNER JOIN"}, {"text": "Все строки левой таблицы", "category": "LEFT JOIN"}, {"text": "NULL при отсутствии совпадения", "category": "LEFT JOIN"}, {"text": "Записи без пары исключены", "category": "INNER JOIN"}]},
                ],
            },
            {
                "t": "FULL OUTER JOIN",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "FULL OUTER JOIN", "markdown": "## FULL OUTER JOIN\n\n**FULL OUTER JOIN** возвращает **все** строки из обеих таблиц. Если совпадения нет — NULL с соответствующей стороны.\n\n```sql\nSELECT u.name, o.product\nFROM users u\nFULL OUTER JOIN orders o ON u.id = o.user_id;\n```\n\nПредположим есть заказ без пользователя (user_id=99):\n```\n| name    | product    |\n| Алексей | Ноутбук    |\n| Алексей | Мышка      |\n| Мария   | Клавиатура |\n| Иван    | NULL       |  ← нет заказов\n| NULL    | Монитор    |  ← нет пользователя\n```\n\n### CROSS JOIN — декартово произведение:\nКаждая строка A с каждой строкой B.\n```sql\nSELECT colors.name, sizes.name\nFROM colors\nCROSS JOIN sizes;\n```\n3 цвета × 4 размера = 12 строк.\n\n### Сводная таблица JOIN-ов:\n| JOIN | Левая | Правая | Совпадения |\n|------|-------|--------|------------|\n| INNER | нет | нет | да |\n| LEFT | все | нет | да |\n| RIGHT | нет | все | да |\n| FULL | все | все | да |\n| CROSS | все×все | все×все | - |"},
                    {"type": "matching", "pairs": [{"left": "INNER JOIN", "right": "Только совпадения"}, {"left": "LEFT JOIN", "right": "Все из левой + совпадения"}, {"left": "RIGHT JOIN", "right": "Все из правой + совпадения"}, {"left": "FULL OUTER JOIN", "right": "Все из обеих таблиц"}, {"left": "CROSS JOIN", "right": "Декартово произведение"}]},
                    {"type": "type-answer", "question": "Сколько строк даст CROSS JOIN 5 строк на 4 строки?", "acceptedAnswers": ["20"]},
                    {"type": "true-false", "statement": "FULL OUTER JOIN возвращает только строки без совпадений.", "correct": False},
                ],
            },
            {
                "t": "Подзапросы (Subqueries)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Вложенные запросы", "markdown": "## Подзапросы (Subqueries)\n\n**Подзапрос** — SQL-запрос внутри другого запроса.\n\n### В WHERE:\n```sql\n-- Пользователи старше среднего возраста\nSELECT name, age FROM users\nWHERE age > (SELECT AVG(age) FROM users);\n```\n\n### С IN:\n```sql\n-- Пользователи, сделавшие заказы\nSELECT name FROM users\nWHERE id IN (SELECT user_id FROM orders);\n```\n\n### С EXISTS:\n```sql\n-- Пользователи с хотя бы одним заказом\nSELECT name FROM users u\nWHERE EXISTS (\n    SELECT 1 FROM orders o\n    WHERE o.user_id = u.id\n);\n```\n\n### В FROM (производная таблица):\n```sql\n-- Средний чек по городам\nSELECT city, AVG(total) AS avg_total\nFROM (\n    SELECT u.city, SUM(o.amount) AS total\n    FROM users u\n    JOIN orders o ON u.id = o.user_id\n    GROUP BY u.city, u.id\n) AS user_totals\nGROUP BY city;\n```\n\n### В SELECT:\n```sql\nSELECT name,\n    (SELECT COUNT(*) FROM orders o\n     WHERE o.user_id = u.id) AS order_count\nFROM users u;\n```"},
                    {"type": "quiz", "question": "Где можно использовать подзапрос?", "options": [{"id": "a", "text": "Только в WHERE", "correct": False}, {"id": "b", "text": "В WHERE, FROM и SELECT", "correct": True}, {"id": "c", "text": "Только в FROM", "correct": False}, {"id": "d", "text": "Подзапросы запрещены в SQL", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: пользователи старше среднего возраста", "correctOrder": ["SELECT name, age FROM users", "WHERE age > (", "SELECT AVG(age) FROM users", ");"]},
                    {"type": "fill-blank", "sentence": "Оператор ___ проверяет, вернул ли подзапрос хотя бы одну строку.", "answer": "EXISTS"},
                    {"type": "true-false", "statement": "Подзапрос может возвращать несколько столбцов при использовании с IN.", "correct": False},
                ],
            },
            {
                "t": "UNION и объединение результатов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "UNION, INTERSECT, EXCEPT", "markdown": "## UNION — объединение результатов\n\n**UNION** объединяет результаты двух запросов в один набор.\n\n### UNION (без дубликатов):\n```sql\nSELECT name FROM employees\nUNION\nSELECT name FROM contractors;\n```\n\n### UNION ALL (с дубликатами):\n```sql\nSELECT name FROM employees\nUNION ALL\nSELECT name FROM contractors;\n```\n\n### Правила UNION:\n- Одинаковое количество столбцов\n- Совместимые типы данных\n- Имена столбцов берутся из первого запроса\n\n### INTERSECT — пересечение:\n```sql\n-- Имена, которые есть в обеих таблицах\nSELECT name FROM employees\nINTERSECT\nSELECT name FROM contractors;\n```\n\n### EXCEPT — разность:\n```sql\n-- Сотрудники, которые не являются подрядчиками\nSELECT name FROM employees\nEXCEPT\nSELECT name FROM contractors;\n```\n\n### Порядок операций:\n- `INTERSECT` выполняется первым\n- `UNION` и `EXCEPT` — слева направо\n- Используйте скобки для явного порядка"},
                    {"type": "matching", "pairs": [{"left": "UNION", "right": "Объединение без дубликатов"}, {"left": "UNION ALL", "right": "Объединение с дубликатами"}, {"left": "INTERSECT", "right": "Пересечение (общие)"}, {"left": "EXCEPT", "right": "Разность (только в первом)"}]},
                    {"type": "quiz", "question": "В чём разница между UNION и UNION ALL?", "options": [{"id": "a", "text": "UNION ALL быстрее, не удаляет дубликаты", "correct": True}, {"id": "b", "text": "UNION ALL работает с разным числом столбцов", "correct": False}, {"id": "c", "text": "Нет разницы", "correct": False}, {"id": "d", "text": "UNION ALL объединяет по горизонтали", "correct": False}]},
                    {"type": "true-false", "statement": "UNION требует одинакового количества столбцов в обоих запросах.", "correct": True},
                    {"type": "multi-select", "question": "Какие операции объединения поддерживает SQL?", "options": [{"id": "a", "text": "UNION", "correct": True}, {"id": "b", "text": "INTERSECT", "correct": True}, {"id": "c", "text": "MERGE", "correct": False}, {"id": "d", "text": "EXCEPT", "correct": True}, {"id": "e", "text": "COMBINE", "correct": False}]},
                ],
            },
        ],
    },
    # ==================== SECTION 4: Создание и изменение ====================
    {
        "title": "Создание и изменение данных",
        "pos": 3,
        "lessons": [
            {
                "t": "CREATE TABLE",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Создание таблиц", "markdown": "## CREATE TABLE\n\n### Синтаксис:\n```sql\nCREATE TABLE table_name (\n    column_name data_type constraints,\n    ...\n);\n```\n\n### Пример — таблица товаров:\n```sql\nCREATE TABLE products (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(200) NOT NULL,\n    description TEXT,\n    price DECIMAL(10, 2) NOT NULL,\n    quantity INTEGER DEFAULT 0,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n```\n\n### Ограничения (Constraints):\n- `PRIMARY KEY` — первичный ключ\n- `NOT NULL` — обязательное поле\n- `UNIQUE` — уникальное значение\n- `DEFAULT` — значение по умолчанию\n- `CHECK` — условие проверки\n- `REFERENCES` — внешний ключ\n\n### С внешним ключом:\n```sql\nCREATE TABLE orders (\n    id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL REFERENCES users(id),\n    product_id INTEGER NOT NULL REFERENCES products(id),\n    quantity INTEGER CHECK (quantity > 0),\n    total DECIMAL(10, 2) NOT NULL\n);\n```\n\n### IF NOT EXISTS:\n```sql\nCREATE TABLE IF NOT EXISTS users (...);\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите CREATE TABLE для таблицы products с id, name и price", "correctOrder": ["CREATE TABLE products (", "id SERIAL PRIMARY KEY,", "name VARCHAR(200) NOT NULL,", "price DECIMAL(10, 2) NOT NULL", ");"]},
                    {"type": "matching", "pairs": [{"left": "PRIMARY KEY", "right": "Уникальный идентификатор"}, {"left": "NOT NULL", "right": "Обязательное поле"}, {"left": "UNIQUE", "right": "Без дубликатов"}, {"left": "DEFAULT", "right": "Значение по умолчанию"}, {"left": "CHECK", "right": "Условие проверки"}]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ позволяет создать таблицу только если она не существует.", "answer": "IF NOT EXISTS"},
                ],
            },
            {
                "t": "Типы данных в PostgreSQL",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Основные типы данных", "markdown": "## Типы данных в PostgreSQL\n\n### Числовые:\n| Тип | Описание |\n|-----|----------|\n| `INTEGER` / `INT` | Целое число (-2 млрд...+2 млрд) |\n| `BIGINT` | Большое целое число |\n| `SMALLINT` | Маленькое целое (-32768...32767) |\n| `SERIAL` | Автоинкремент (INTEGER) |\n| `DECIMAL(p,s)` | Точное число (p цифр, s после точки) |\n| `NUMERIC` | Аналог DECIMAL |\n| `REAL` | Число с плавающей точкой (4 байта) |\n| `DOUBLE PRECISION` | Число с плавающей точкой (8 байт) |\n\n### Строковые:\n| Тип | Описание |\n|-----|----------|\n| `VARCHAR(n)` | Строка до n символов |\n| `CHAR(n)` | Строка ровно n символов |\n| `TEXT` | Строка неограниченной длины |\n\n### Дата и время:\n| Тип | Описание |\n|-----|----------|\n| `DATE` | Дата (2024-01-15) |\n| `TIME` | Время (14:30:00) |\n| `TIMESTAMP` | Дата + время |\n| `INTERVAL` | Промежуток времени |\n\n### Логический:\n| Тип | Описание |\n|-----|----------|\n| `BOOLEAN` | true / false / null |\n\n### Специальные (PostgreSQL):\n- `JSON` / `JSONB` — JSON-данные\n- `UUID` — уникальный идентификатор\n- `ARRAY` — массив значений"},
                    {"type": "category-sort", "categories": ["Числовые", "Строковые", "Дата и время"], "items": [{"text": "INTEGER", "category": "Числовые"}, {"text": "VARCHAR", "category": "Строковые"}, {"text": "TIMESTAMP", "category": "Дата и время"}, {"text": "DECIMAL", "category": "Числовые"}, {"text": "TEXT", "category": "Строковые"}, {"text": "DATE", "category": "Дата и время"}]},
                    {"type": "quiz", "question": "Какой тип данных лучше для хранения денежных сумм?", "options": [{"id": "a", "text": "REAL", "correct": False}, {"id": "b", "text": "DECIMAL", "correct": True}, {"id": "c", "text": "INTEGER", "correct": False}, {"id": "d", "text": "TEXT", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Тип ___ в PostgreSQL обеспечивает автоматическое увеличение числа при каждой вставке.", "answer": "SERIAL"},
                    {"type": "true-false", "statement": "VARCHAR и TEXT в PostgreSQL имеют одинаковую производительность.", "correct": True},
                ],
            },
            {
                "t": "INSERT — вставка данных",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Вставка записей", "markdown": "## INSERT — вставка данных\n\n### Вставка одной строки:\n```sql\nINSERT INTO users (name, email, age)\nVALUES ('Алексей', 'alex@mail.ru', 25);\n```\n\n### Вставка нескольких строк:\n```sql\nINSERT INTO users (name, email, age) VALUES\n('Мария', 'maria@gmail.com', 30),\n('Иван', 'ivan@yandex.ru', 22),\n('Анна', 'anna@mail.ru', 28);\n```\n\n### INSERT с RETURNING:\n```sql\nINSERT INTO users (name, email, age)\nVALUES ('Пётр', 'petr@mail.ru', 35)\nRETURNING id, name;\n```\nВернёт: `id = 5, name = Пётр`\n\n### INSERT из другой таблицы:\n```sql\nINSERT INTO archived_users (name, email)\nSELECT name, email FROM users\nWHERE last_login < '2023-01-01';\n```\n\n### ON CONFLICT (UPSERT):\n```sql\nINSERT INTO users (email, name)\nVALUES ('alex@mail.ru', 'Алексей Новый')\nON CONFLICT (email)\nDO UPDATE SET name = EXCLUDED.name;\n```\nЕсли email уже существует — обновит имя."},
                    {"type": "code-puzzle", "instructions": "Соберите INSERT для добавления пользователя", "correctOrder": ["INSERT INTO users (name, email, age)", "VALUES ('Мария', 'maria@gmail.com', 30);"]},
                    {"type": "quiz", "question": "Что делает RETURNING в INSERT?", "options": [{"id": "a", "text": "Отменяет вставку", "correct": False}, {"id": "b", "text": "Возвращает значения вставленной строки", "correct": True}, {"id": "c", "text": "Возвращает все строки таблицы", "correct": False}, {"id": "d", "text": "Проверяет уникальность", "correct": False}]},
                    {"type": "fill-blank", "sentence": "ON CONFLICT позволяет выполнить ___ при конфликте уникальности.", "answer": "UPSERT"},
                    {"type": "true-false", "statement": "INSERT может вставить данные из результата SELECT-запроса.", "correct": True},
                ],
            },
            {
                "t": "UPDATE — обновление данных",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Обновление записей", "markdown": "## UPDATE — обновление данных\n\n### Базовый синтаксис:\n```sql\nUPDATE users\nSET age = 26\nWHERE name = 'Алексей';\n```\n\n### Обновление нескольких столбцов:\n```sql\nUPDATE users\nSET name = 'Алексей Петров',\n    email = 'alexey.new@mail.ru',\n    age = 26\nWHERE id = 1;\n```\n\n### UPDATE с вычислением:\n```sql\n-- Увеличить возраст всем на 1\nUPDATE users SET age = age + 1;\n\n-- Скидка 10% на все товары\nUPDATE products SET price = price * 0.9;\n```\n\n### UPDATE с подзапросом:\n```sql\nUPDATE orders\nSET status = 'archived'\nWHERE user_id IN (\n    SELECT id FROM users\n    WHERE last_login < '2023-01-01'\n);\n```\n\n### UPDATE с RETURNING:\n```sql\nUPDATE users SET age = 30\nWHERE name = 'Мария'\nRETURNING id, name, age;\n```\n\n### ВАЖНО:\n**Без WHERE обновятся ВСЕ строки!**\n```sql\n-- ОПАСНО! Обновит всех!\nUPDATE users SET age = 0;\n```"},
                    {"type": "quiz", "question": "Что произойдёт, если выполнить UPDATE без WHERE?", "options": [{"id": "a", "text": "Ошибка синтаксиса", "correct": False}, {"id": "b", "text": "Обновится только первая строка", "correct": False}, {"id": "c", "text": "Обновятся ВСЕ строки", "correct": True}, {"id": "d", "text": "Ничего не произойдёт", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос: увеличить цену товаров на 15%", "correctOrder": ["UPDATE products", "SET price = price * 1.15;"]},
                    {"type": "true-false", "statement": "UPDATE может использовать подзапросы в WHERE.", "correct": True},
                    {"type": "drag-order", "items": ["UPDATE table_name", "SET column = value", "WHERE condition", "RETURNING columns"]},
                ],
            },
            {
                "t": "DELETE — удаление данных",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Удаление записей", "markdown": "## DELETE — удаление данных\n\n### Удалить конкретные строки:\n```sql\nDELETE FROM users WHERE id = 5;\n```\n\n### Удалить по условию:\n```sql\nDELETE FROM orders\nWHERE created_at < '2023-01-01';\n```\n\n### DELETE с подзапросом:\n```sql\nDELETE FROM orders\nWHERE user_id IN (\n    SELECT id FROM users WHERE status = 'deleted'\n);\n```\n\n### DELETE с RETURNING:\n```sql\nDELETE FROM users WHERE age < 18\nRETURNING id, name;\n```\n\n### TRUNCATE — удалить все строки:\n```sql\n-- Быстрее DELETE для всех строк\nTRUNCATE TABLE orders;\n\n-- С каскадным удалением зависимых\nTRUNCATE TABLE users CASCADE;\n\n-- Сбросить счётчик SERIAL\nTRUNCATE TABLE users RESTART IDENTITY;\n```\n\n### DELETE vs TRUNCATE:\n| | DELETE | TRUNCATE |\n|--|--------|----------|\n| WHERE | Да | Нет |\n| Скорость | Медленнее | Быстрее |\n| Триггеры | Запускает | Нет |\n| Откат | Да | Да (PostgreSQL) |"},
                    {"type": "matching", "pairs": [{"left": "DELETE", "right": "Удаление строк по условию"}, {"left": "TRUNCATE", "right": "Быстрое удаление всех строк"}, {"left": "DELETE без WHERE", "right": "Удаление всех строк медленно"}, {"left": "TRUNCATE CASCADE", "right": "Удаление с зависимостями"}]},
                    {"type": "quiz", "question": "Что быстрее для удаления всех строк из таблицы?", "options": [{"id": "a", "text": "DELETE FROM table", "correct": False}, {"id": "b", "text": "TRUNCATE TABLE table", "correct": True}, {"id": "c", "text": "DROP TABLE table", "correct": False}, {"id": "d", "text": "Одинаково", "correct": False}]},
                    {"type": "true-false", "statement": "TRUNCATE запускает триггеры на каждую удалённую строку.", "correct": False},
                ],
            },
            {
                "t": "ALTER TABLE — изменение структуры",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Изменение таблиц", "markdown": "## ALTER TABLE\n\n### Добавить столбец:\n```sql\nALTER TABLE users\nADD COLUMN phone VARCHAR(20);\n```\n\n### Удалить столбец:\n```sql\nALTER TABLE users\nDROP COLUMN phone;\n```\n\n### Переименовать столбец:\n```sql\nALTER TABLE users\nRENAME COLUMN name TO full_name;\n```\n\n### Изменить тип столбца:\n```sql\nALTER TABLE users\nALTER COLUMN age TYPE BIGINT;\n```\n\n### Добавить/удалить NOT NULL:\n```sql\n-- Добавить\nALTER TABLE users\nALTER COLUMN email SET NOT NULL;\n\n-- Удалить\nALTER TABLE users\nALTER COLUMN email DROP NOT NULL;\n```\n\n### Добавить ограничение:\n```sql\nALTER TABLE users\nADD CONSTRAINT age_check CHECK (age >= 0);\n\nALTER TABLE orders\nADD CONSTRAINT fk_user\nFOREIGN KEY (user_id) REFERENCES users(id);\n```\n\n### Переименовать таблицу:\n```sql\nALTER TABLE users RENAME TO customers;\n```\n\n### Удалить таблицу:\n```sql\nDROP TABLE IF EXISTS old_table CASCADE;\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите ALTER TABLE: добавить столбец phone в users", "correctOrder": ["ALTER TABLE users", "ADD COLUMN phone VARCHAR(20);"]},
                    {"type": "quiz", "question": "Как изменить тип столбца age на BIGINT?", "options": [{"id": "a", "text": "ALTER TABLE users CHANGE age BIGINT", "correct": False}, {"id": "b", "text": "ALTER TABLE users ALTER COLUMN age TYPE BIGINT", "correct": True}, {"id": "c", "text": "UPDATE TABLE users SET TYPE age BIGINT", "correct": False}, {"id": "d", "text": "MODIFY TABLE users age BIGINT", "correct": False}]},
                    {"type": "drag-order", "items": ["ALTER TABLE users", "ADD CONSTRAINT age_check", "CHECK (age >= 0);"]},
                    {"type": "multi-select", "question": "Что можно сделать с ALTER TABLE?", "options": [{"id": "a", "text": "Добавить столбец", "correct": True}, {"id": "b", "text": "Удалить столбец", "correct": True}, {"id": "c", "text": "Вставить данные", "correct": False}, {"id": "d", "text": "Переименовать таблицу", "correct": True}, {"id": "e", "text": "Добавить ограничение", "correct": True}]},
                ],
            },
        ],
    },
    # ==================== SECTION 5: Проектирование БД ====================
    {
        "title": "Проектирование базы данных",
        "pos": 4,
        "lessons": [
            {
                "t": "Нормализация: 1NF, 2NF, 3NF",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Нормальные формы", "markdown": "## Нормализация базы данных\n\n**Нормализация** — процесс организации данных для уменьшения избыточности и аномалий.\n\n### 1NF (Первая нормальная форма):\n- Каждая ячейка содержит **одно** атомарное значение\n- Нет повторяющихся групп\n\n❌ Нарушение:\n```\n| id | name    | phones                  |\n| 1  | Алексей | +7-999-111, +7-999-222  |\n```\n\n✅ Решение:\n```\n| id | name    | phone       |\n| 1  | Алексей | +7-999-111  |\n| 1  | Алексей | +7-999-222  |\n```\nИли отдельная таблица phones.\n\n### 2NF (Вторая НФ):\n- Соответствует 1NF\n- Каждый неключевой столбец зависит от **всего** первичного ключа\n\n❌ Нарушение (составной ключ student_id + course_id):\n```\n| student_id | course_id | course_name | grade |\n```\n`course_name` зависит только от `course_id`, а не от всего ключа.\n\n### 3NF (Третья НФ):\n- Соответствует 2NF\n- Нет **транзитивных** зависимостей\n\n❌ Нарушение:\n```\n| id | name | city_id | city_name |\n```\n`city_name` зависит от `city_id`, а не напрямую от `id`.\n\n✅ Решение: вынести города в отдельную таблицу."},
                    {"type": "flashcards", "cards": [{"front": "1NF", "back": "Атомарные значения, нет повторяющихся групп"}, {"front": "2NF", "back": "1NF + неключевые столбцы зависят от всего первичного ключа"}, {"front": "3NF", "back": "2NF + нет транзитивных зависимостей"}]},
                    {"type": "drag-order", "items": ["1NF: атомарные значения", "2NF: зависимость от всего ключа", "3NF: нет транзитивных зависимостей"]},
                    {"type": "quiz", "question": "Какую НФ нарушает хранение нескольких телефонов в одной ячейке?", "options": [{"id": "a", "text": "1NF", "correct": True}, {"id": "b", "text": "2NF", "correct": False}, {"id": "c", "text": "3NF", "correct": False}, {"id": "d", "text": "Никакую", "correct": False}]},
                    {"type": "true-false", "statement": "Третья нормальная форма требует соответствия 1NF и 2NF.", "correct": True},
                ],
            },
            {
                "t": "ER-диаграммы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Entity-Relationship диаграммы", "markdown": "## ER-диаграммы\n\n**ER-диаграмма** (Entity-Relationship) — визуальное представление структуры БД.\n\n### Элементы ER-диаграммы:\n- **Сущность (Entity)** — таблица (прямоугольник)\n- **Атрибут** — столбец (овал)\n- **Связь (Relationship)** — линия между сущностями\n\n### Обозначения связей:\n```\n1 ─── 1    Один к одному\n1 ─── *    Один ко многим\n* ─── *    Многие ко многим\n```\n\n### Пример: интернет-магазин\n```\n[users] 1──* [orders] *──* [products]\n   |                          |\n   └── id, name, email        └── id, name, price\n```\n\n### Инструменты для ER-диаграмм:\n- **dbdiagram.io** — онлайн, бесплатный\n- **draw.io** — универсальный\n- **pgModeler** — специально для PostgreSQL\n- **DataGrip** — встроенный визуализатор\n\n### DBML — язык описания схемы:\n```\nTable users {\n  id integer [pk]\n  name varchar\n  email varchar [unique]\n}\n\nTable orders {\n  id integer [pk]\n  user_id integer [ref: > users.id]\n  total decimal\n}\n```"},
                    {"type": "matching", "pairs": [{"left": "Сущность (Entity)", "right": "Таблица — прямоугольник"}, {"left": "Атрибут", "right": "Столбец — овал"}, {"left": "Связь", "right": "Линия между сущностями"}, {"left": "PK", "right": "Первичный ключ (подчёркнут)"}]},
                    {"type": "quiz", "question": "Какой инструмент специально создан для ER-диаграмм баз данных?", "options": [{"id": "a", "text": "Figma", "correct": False}, {"id": "b", "text": "dbdiagram.io", "correct": True}, {"id": "c", "text": "Photoshop", "correct": False}, {"id": "d", "text": "VS Code", "correct": False}]},
                    {"type": "category-sort", "categories": ["Элементы ER-диаграммы", "Инструменты"], "items": [{"text": "Сущность (прямоугольник)", "category": "Элементы ER-диаграммы"}, {"text": "dbdiagram.io", "category": "Инструменты"}, {"text": "Связь (линия)", "category": "Элементы ER-диаграммы"}, {"text": "pgModeler", "category": "Инструменты"}, {"text": "Атрибут (овал)", "category": "Элементы ER-диаграммы"}, {"text": "draw.io", "category": "Инструменты"}]},
                ],
            },
            {
                "t": "Первичные и внешние ключи",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "PRIMARY KEY и FOREIGN KEY", "markdown": "## Ключи в реляционных БД\n\n### Первичный ключ (PRIMARY KEY):\nУникально идентифицирует каждую строку.\n\n```sql\n-- Автоинкрементный ключ\nCREATE TABLE users (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(100)\n);\n\n-- UUID ключ\nCREATE TABLE users (\n    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n    name VARCHAR(100)\n);\n\n-- Составной ключ\nCREATE TABLE student_courses (\n    student_id INTEGER,\n    course_id INTEGER,\n    PRIMARY KEY (student_id, course_id)\n);\n```\n\n### Внешний ключ (FOREIGN KEY):\nСсылка на первичный ключ другой таблицы.\n\n```sql\nCREATE TABLE orders (\n    id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL,\n    FOREIGN KEY (user_id) REFERENCES users(id)\n        ON DELETE CASCADE\n        ON UPDATE CASCADE\n);\n```\n\n### Действия при удалении/обновлении:\n| Действие | Описание |\n|----------|----------|\n| `CASCADE` | Удалить/обновить связанные записи |\n| `SET NULL` | Установить NULL |\n| `SET DEFAULT` | Установить значение по умолчанию |\n| `RESTRICT` | Запретить (ошибка) |\n| `NO ACTION` | Аналог RESTRICT (по умолчанию) |"},
                    {"type": "matching", "pairs": [{"left": "CASCADE", "right": "Удалить связанные записи"}, {"left": "SET NULL", "right": "Установить NULL"}, {"left": "RESTRICT", "right": "Запретить удаление"}, {"left": "NO ACTION", "right": "По умолчанию, аналог RESTRICT"}]},
                    {"type": "quiz", "question": "Что произойдёт с заказами при ON DELETE CASCADE, если удалить пользователя?", "options": [{"id": "a", "text": "Останутся с NULL", "correct": False}, {"id": "b", "text": "Удалятся вместе с пользователем", "correct": True}, {"id": "c", "text": "Ошибка при удалении", "correct": False}, {"id": "d", "text": "Ничего", "correct": False}]},
                    {"type": "true-false", "statement": "Составной первичный ключ состоит из двух или более столбцов.", "correct": True},
                    {"type": "fill-blank", "sentence": "Внешний ключ создаётся с помощью ключевого слова FOREIGN KEY ... ___.", "answer": "REFERENCES"},
                ],
            },
            {
                "t": "Constraints — ограничения",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Ограничения целостности", "markdown": "## Constraints — ограничения\n\n### NOT NULL:\n```sql\nCREATE TABLE users (\n    name VARCHAR(100) NOT NULL\n);\n```\n\n### UNIQUE:\n```sql\nCREATE TABLE users (\n    email VARCHAR(255) UNIQUE\n);\n\n-- Составной UNIQUE\nALTER TABLE student_courses\nADD CONSTRAINT unique_enrollment\nUNIQUE (student_id, course_id);\n```\n\n### CHECK:\n```sql\nCREATE TABLE products (\n    price DECIMAL CHECK (price >= 0),\n    quantity INTEGER CHECK (quantity >= 0),\n    discount DECIMAL CHECK (discount BETWEEN 0 AND 100)\n);\n\n-- Именованное ограничение\nALTER TABLE users\nADD CONSTRAINT valid_age CHECK (age BETWEEN 0 AND 150);\n```\n\n### DEFAULT:\n```sql\nCREATE TABLE posts (\n    status VARCHAR(20) DEFAULT 'draft',\n    created_at TIMESTAMP DEFAULT NOW(),\n    views INTEGER DEFAULT 0\n);\n```\n\n### Удаление ограничения:\n```sql\nALTER TABLE users\nDROP CONSTRAINT valid_age;\n```\n\n### Просмотр ограничений:\n```sql\nSELECT constraint_name, constraint_type\nFROM information_schema.table_constraints\nWHERE table_name = 'users';\n```"},
                    {"type": "category-sort", "categories": ["Ограничения данных", "Ограничения ключей"], "items": [{"text": "NOT NULL", "category": "Ограничения данных"}, {"text": "PRIMARY KEY", "category": "Ограничения ключей"}, {"text": "CHECK", "category": "Ограничения данных"}, {"text": "FOREIGN KEY", "category": "Ограничения ключей"}, {"text": "DEFAULT", "category": "Ограничения данных"}, {"text": "UNIQUE", "category": "Ограничения ключей"}]},
                    {"type": "code-puzzle", "instructions": "Соберите CHECK-ограничение для возраста от 0 до 150", "correctOrder": ["ALTER TABLE users", "ADD CONSTRAINT valid_age", "CHECK (age BETWEEN 0 AND 150);"]},
                    {"type": "true-false", "statement": "UNIQUE позволяет хранить несколько NULL-значений в PostgreSQL.", "correct": True},
                ],
            },
            {
                "t": "Миграции базы данных",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Управление миграциями", "markdown": "## Миграции базы данных\n\n**Миграция** — версионированное изменение структуры БД.\n\n### Зачем нужны миграции?\n- Отслеживание изменений схемы\n- Синхронизация БД между разработчиками\n- Безопасное обновление продакшена\n- Возможность отката (rollback)\n\n### Инструменты миграций:\n- **Alembic** (Python/SQLAlchemy)\n- **Flyway** (Java, универсальный)\n- **Liquibase** (универсальный)\n- **Knex.js** (Node.js)\n- **Django Migrations** (Python/Django)\n\n### Пример с Alembic:\n```bash\n# Создать миграцию\nalembic revision --autogenerate -m \"add phone to users\"\n\n# Применить\nalembic upgrade head\n\n# Откатить\nalembic downgrade -1\n```\n\n### Файл миграции:\n```python\ndef upgrade():\n    op.add_column('users',\n        sa.Column('phone', sa.String(20))\n    )\n\ndef downgrade():\n    op.drop_column('users', 'phone')\n```\n\n### Правила миграций:\n- Никогда не редактируйте применённые миграции\n- Всегда пишите `downgrade`\n- Тестируйте миграции на копии БД\n- В продакшене — бэкап перед миграцией"},
                    {"type": "quiz", "question": "Что делает команда alembic downgrade -1?", "options": [{"id": "a", "text": "Удаляет базу данных", "correct": False}, {"id": "b", "text": "Откатывает последнюю миграцию", "correct": True}, {"id": "c", "text": "Применяет одну миграцию", "correct": False}, {"id": "d", "text": "Создаёт новую миграцию", "correct": False}]},
                    {"type": "drag-order", "items": ["Создать файл миграции", "Описать upgrade и downgrade", "Протестировать на копии БД", "Сделать бэкап продакшена", "Применить миграцию"]},
                    {"type": "true-false", "statement": "Можно безопасно редактировать уже применённые миграции.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "Alembic", "right": "Python / SQLAlchemy"}, {"left": "Flyway", "right": "Java / универсальный"}, {"left": "Django Migrations", "right": "Python / Django"}, {"left": "Knex.js", "right": "Node.js"}]},
                ],
            },
        ],
    },
    # ==================== SECTION 6: Продвинутый SQL ====================
    {
        "title": "Продвинутый SQL",
        "pos": 5,
        "lessons": [
            {
                "t": "Индексы",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Индексы в PostgreSQL", "markdown": "## Индексы\n\n**Индекс** — структура данных, ускоряющая поиск в таблице (аналог алфавитного указателя в книге).\n\n### Создание индекса:\n```sql\nCREATE INDEX idx_users_email ON users(email);\n```\n\n### Уникальный индекс:\n```sql\nCREATE UNIQUE INDEX idx_users_email\nON users(email);\n```\n\n### Составной индекс:\n```sql\nCREATE INDEX idx_orders_user_date\nON orders(user_id, created_at);\n```\n\n### Типы индексов в PostgreSQL:\n- **B-tree** — по умолчанию, для =, <, >, BETWEEN\n- **Hash** — только для =\n- **GiST** — для полнотекстового поиска, геоданных\n- **GIN** — для JSONB, массивов, полнотекстового поиска\n\n### Когда индексы НЕ помогают:\n- Маленькие таблицы (< 1000 строк)\n- Столбцы, которые редко используются в WHERE\n- Столбцы с малым количеством уникальных значений\n\n### Удаление индекса:\n```sql\nDROP INDEX idx_users_email;\n```\n\n### Просмотр индексов:\n```sql\n\\di  -- в psql\nSELECT * FROM pg_indexes WHERE tablename = 'users';\n```"},
                    {"type": "quiz", "question": "Какой тип индекса используется по умолчанию в PostgreSQL?", "options": [{"id": "a", "text": "Hash", "correct": False}, {"id": "b", "text": "B-tree", "correct": True}, {"id": "c", "text": "GIN", "correct": False}, {"id": "d", "text": "GiST", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Создайте индекс на столбец email таблицы users", "correctOrder": ["CREATE INDEX idx_users_email", "ON users(email);"]},
                    {"type": "category-sort", "categories": ["Индекс помогает", "Индекс не помогает"], "items": [{"text": "WHERE email = '...'", "category": "Индекс помогает"}, {"text": "Таблица из 50 строк", "category": "Индекс не помогает"}, {"text": "ORDER BY created_at", "category": "Индекс помогает"}, {"text": "Столбец gender (M/F)", "category": "Индекс не помогает"}, {"text": "JOIN по user_id", "category": "Индекс помогает"}]},
                    {"type": "true-false", "statement": "Индексы ускоряют чтение, но замедляют запись.", "correct": True},
                ],
            },
            {
                "t": "EXPLAIN — анализ запросов",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Анализ плана выполнения", "markdown": "## EXPLAIN — план выполнения запроса\n\n**EXPLAIN** показывает, как PostgreSQL будет выполнять запрос.\n\n### Базовое использование:\n```sql\nEXPLAIN SELECT * FROM users WHERE age > 25;\n```\n\n### EXPLAIN ANALYZE — с реальным выполнением:\n```sql\nEXPLAIN ANALYZE\nSELECT * FROM users WHERE age > 25;\n```\n\n### Вывод:\n```\nSeq Scan on users  (cost=0.00..1.50 rows=10 width=64)\n  (actual time=0.012..0.015 rows=8 loops=1)\n  Filter: (age > 25)\n  Rows Removed by Filter: 2\nPlanning Time: 0.050 ms\nExecution Time: 0.030 ms\n```\n\n### Типы сканирования:\n| Тип | Описание |\n|-----|----------|\n| `Seq Scan` | Последовательное чтение всей таблицы |\n| `Index Scan` | Чтение через индекс |\n| `Index Only Scan` | Данные только из индекса |\n| `Bitmap Index Scan` | Индекс + фильтрация |\n\n### Чтение cost:\n- `cost=0.00..1.50` — стоимость (условные единицы)\n- `rows=10` — ожидаемое количество строк\n- `actual time` — реальное время (мс)\n\n### Ключевые метрики:\n- **Seq Scan на большой таблице** — нужен индекс\n- **Execution Time > 100ms** — стоит оптимизировать"},
                    {"type": "flashcards", "cards": [{"front": "Seq Scan", "back": "Последовательное чтение всей таблицы — медленно для больших таблиц"}, {"front": "Index Scan", "back": "Чтение через индекс — быстро для выборки малого количества строк"}, {"front": "Index Only Scan", "back": "Все данные берутся из индекса — самый быстрый вариант"}, {"front": "cost", "back": "Условная стоимость запроса (меньше = лучше)"}]},
                    {"type": "quiz", "question": "Какой тип сканирования говорит о необходимости добавить индекс?", "options": [{"id": "a", "text": "Index Scan", "correct": False}, {"id": "b", "text": "Seq Scan на большой таблице", "correct": True}, {"id": "c", "text": "Index Only Scan", "correct": False}, {"id": "d", "text": "Bitmap Scan", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для реального выполнения и замера времени используют EXPLAIN ___.", "answer": "ANALYZE"},
                    {"type": "true-false", "statement": "EXPLAIN ANALYZE только показывает план, но не выполняет запрос.", "correct": False},
                ],
            },
            {
                "t": "Транзакции",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Транзакции в SQL", "markdown": "## Транзакции\n\n**Транзакция** — группа операций, выполняемых как единое целое.\n\n### Синтаксис:\n```sql\nBEGIN;  -- начало транзакции\n\nUPDATE accounts SET balance = balance - 1000\nWHERE id = 1;\n\nUPDATE accounts SET balance = balance + 1000\nWHERE id = 2;\n\nCOMMIT;  -- подтверждение\n```\n\n### Откат транзакции:\n```sql\nBEGIN;\n\nDELETE FROM orders WHERE id = 100;\n\n-- Ой, ошиблись!\nROLLBACK;  -- отмена всех изменений\n```\n\n### SAVEPOINT — точки сохранения:\n```sql\nBEGIN;\n\nINSERT INTO users (name) VALUES ('Алексей');\nSAVEPOINT sp1;\n\nINSERT INTO users (name) VALUES ('Ошибка');\nROLLBACK TO sp1;  -- откат до sp1\n\nINSERT INTO users (name) VALUES ('Мария');\nCOMMIT;  -- сохранены: Алексей, Мария\n```\n\n### Уровни изоляции:\n| Уровень | Описание |\n|---------|----------|\n| `READ UNCOMMITTED` | Видит незакоммиченные данные |\n| `READ COMMITTED` | По умолчанию в PostgreSQL |\n| `REPEATABLE READ` | Стабильное чтение |\n| `SERIALIZABLE` | Максимальная изоляция |\n\n```sql\nSET TRANSACTION ISOLATION LEVEL REPEATABLE READ;\n```"},
                    {"type": "drag-order", "items": ["BEGIN (начало транзакции)", "Выполнение SQL-операций", "Проверка результата", "COMMIT или ROLLBACK"]},
                    {"type": "matching", "pairs": [{"left": "BEGIN", "right": "Начать транзакцию"}, {"left": "COMMIT", "right": "Подтвердить изменения"}, {"left": "ROLLBACK", "right": "Отменить изменения"}, {"left": "SAVEPOINT", "right": "Точка сохранения"}]},
                    {"type": "quiz", "question": "Какой уровень изоляции по умолчанию в PostgreSQL?", "options": [{"id": "a", "text": "READ UNCOMMITTED", "correct": False}, {"id": "b", "text": "READ COMMITTED", "correct": True}, {"id": "c", "text": "REPEATABLE READ", "correct": False}, {"id": "d", "text": "SERIALIZABLE", "correct": False}]},
                    {"type": "true-false", "statement": "После ROLLBACK все изменения транзакции отменяются.", "correct": True},
                ],
            },
            {
                "t": "Views — представления",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Представления (Views)", "markdown": "## Views — представления\n\n**View** — виртуальная таблица, основанная на SQL-запросе.\n\n### Создание View:\n```sql\nCREATE VIEW active_users AS\nSELECT id, name, email\nFROM users\nWHERE status = 'active';\n```\n\n### Использование:\n```sql\nSELECT * FROM active_users;\n\nSELECT name FROM active_users\nWHERE name LIKE 'А%';\n```\n\n### Сложный View:\n```sql\nCREATE VIEW user_order_stats AS\nSELECT\n    u.name,\n    COUNT(o.id) AS total_orders,\n    SUM(o.amount) AS total_spent,\n    AVG(o.amount) AS avg_order\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id\nGROUP BY u.id, u.name;\n```\n\n### Обновление View:\n```sql\nCREATE OR REPLACE VIEW active_users AS\nSELECT id, name, email, created_at\nFROM users\nWHERE status = 'active';\n```\n\n### Materialized View — кэширование:\n```sql\nCREATE MATERIALIZED VIEW mv_stats AS\nSELECT city, COUNT(*) AS user_count\nFROM users GROUP BY city;\n\n-- Обновить данные\nREFRESH MATERIALIZED VIEW mv_stats;\n```\n\n### Удаление:\n```sql\nDROP VIEW IF EXISTS active_users;\n```"},
                    {"type": "quiz", "question": "В чём разница между View и Materialized View?", "options": [{"id": "a", "text": "View хранит данные, Materialized — нет", "correct": False}, {"id": "b", "text": "Materialized View кэширует результат, View — нет", "correct": True}, {"id": "c", "text": "Никакой разницы", "correct": False}, {"id": "d", "text": "Materialized View нельзя обновить", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Создайте View для активных пользователей", "correctOrder": ["CREATE VIEW active_users AS", "SELECT id, name, email", "FROM users", "WHERE status = 'active';"]},
                    {"type": "fill-blank", "sentence": "Для обновления данных Materialized View используется команда ___ MATERIALIZED VIEW.", "answer": "REFRESH"},
                ],
            },
            {
                "t": "Хранимые процедуры и функции",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Функции и процедуры", "markdown": "## Хранимые процедуры и функции\n\n### Функция (возвращает значение):\n```sql\nCREATE FUNCTION get_user_orders(uid INTEGER)\nRETURNS INTEGER AS $$\n    SELECT COUNT(*)\n    FROM orders\n    WHERE user_id = uid;\n$$ LANGUAGE sql;\n\n-- Использование:\nSELECT name, get_user_orders(id)\nFROM users;\n```\n\n### PL/pgSQL функция:\n```sql\nCREATE FUNCTION calculate_discount(\n    total DECIMAL,\n    user_level VARCHAR\n) RETURNS DECIMAL AS $$\nBEGIN\n    IF user_level = 'gold' THEN\n        RETURN total * 0.20;\n    ELSIF user_level = 'silver' THEN\n        RETURN total * 0.10;\n    ELSE\n        RETURN total * 0.05;\n    END IF;\nEND;\n$$ LANGUAGE plpgsql;\n```\n\n### Процедура (без возвращаемого значения):\n```sql\nCREATE PROCEDURE archive_old_orders()\nLANGUAGE plpgsql AS $$\nBEGIN\n    INSERT INTO archived_orders\n    SELECT * FROM orders\n    WHERE created_at < NOW() - INTERVAL '1 year';\n\n    DELETE FROM orders\n    WHERE created_at < NOW() - INTERVAL '1 year';\nEND;\n$$;\n\n-- Вызов:\nCALL archive_old_orders();\n```\n\n### Триггеры:\n```sql\nCREATE FUNCTION update_timestamp()\nRETURNS TRIGGER AS $$\nBEGIN\n    NEW.updated_at = NOW();\n    RETURN NEW;\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE TRIGGER set_updated_at\nBEFORE UPDATE ON users\nFOR EACH ROW\nEXECUTE FUNCTION update_timestamp();\n```"},
                    {"type": "quiz", "question": "Как вызвать хранимую процедуру в PostgreSQL?", "options": [{"id": "a", "text": "EXEC procedure_name()", "correct": False}, {"id": "b", "text": "CALL procedure_name()", "correct": True}, {"id": "c", "text": "RUN procedure_name()", "correct": False}, {"id": "d", "text": "SELECT procedure_name()", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "FUNCTION", "right": "Возвращает значение"}, {"left": "PROCEDURE", "right": "Не возвращает значение"}, {"left": "TRIGGER", "right": "Автоматически при событии"}, {"left": "PL/pgSQL", "right": "Процедурный язык PostgreSQL"}]},
                    {"type": "true-false", "statement": "Триггер выполняется автоматически при определённых событиях (INSERT, UPDATE, DELETE).", "correct": True},
                    {"type": "fill-blank", "sentence": "Для вызова хранимой процедуры используется команда ___.", "answer": "CALL"},
                ],
            },
            {
                "t": "Оконные функции",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Window Functions", "markdown": "## Оконные функции (Window Functions)\n\nОконные функции выполняют вычисления по **набору строк**, связанных с текущей строкой, **не группируя** результат.\n\n### Синтаксис:\n```sql\nfunction() OVER (\n    PARTITION BY column\n    ORDER BY column\n)\n```\n\n### ROW_NUMBER — нумерация строк:\n```sql\nSELECT name, city, age,\n    ROW_NUMBER() OVER (ORDER BY age DESC) AS rank\nFROM users;\n```\n\n### RANK и DENSE_RANK:\n```sql\nSELECT name, score,\n    RANK() OVER (ORDER BY score DESC) AS rank,\n    DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank\nFROM students;\n```\n- `RANK` — пропускает позиции при дубликатах (1, 2, 2, 4)\n- `DENSE_RANK` — не пропускает (1, 2, 2, 3)\n\n### PARTITION BY — оконные по группам:\n```sql\n-- Ранг внутри каждого города\nSELECT name, city, age,\n    ROW_NUMBER() OVER (\n        PARTITION BY city\n        ORDER BY age DESC\n    ) AS city_rank\nFROM users;\n```\n\n### LAG и LEAD — предыдущая/следующая строка:\n```sql\nSELECT date, revenue,\n    LAG(revenue) OVER (ORDER BY date) AS prev_revenue,\n    revenue - LAG(revenue) OVER (ORDER BY date) AS growth\nFROM sales;\n```\n\n### Накопительная сумма:\n```sql\nSELECT date, amount,\n    SUM(amount) OVER (ORDER BY date) AS running_total\nFROM payments;\n```"},
                    {"type": "matching", "pairs": [{"left": "ROW_NUMBER()", "right": "Уникальный порядковый номер"}, {"left": "RANK()", "right": "Ранг с пропуском при дубликатах"}, {"left": "DENSE_RANK()", "right": "Ранг без пропуска"}, {"left": "LAG()", "right": "Значение предыдущей строки"}, {"left": "LEAD()", "right": "Значение следующей строки"}]},
                    {"type": "quiz", "question": "Чем RANK отличается от DENSE_RANK при одинаковых значениях?", "options": [{"id": "a", "text": "RANK пропускает позиции, DENSE_RANK нет", "correct": True}, {"id": "b", "text": "DENSE_RANK пропускает позиции, RANK нет", "correct": False}, {"id": "c", "text": "Ничем", "correct": False}, {"id": "d", "text": "RANK работает только с числами", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите запрос с накопительной суммой платежей", "correctOrder": ["SELECT date, amount,", "SUM(amount) OVER (ORDER BY date)", "AS running_total", "FROM payments;"]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ BY разделяет данные на группы для оконной функции.", "answer": "PARTITION"},
                ],
            },
        ],
    },
    # ==================== SECTION 7: Практика и карьера ====================
    {
        "title": "Практика и карьера",
        "pos": 6,
        "lessons": [
            {
                "t": "Оптимизация запросов",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Как ускорить SQL-запросы", "markdown": "## Оптимизация запросов\n\n### 1. Используйте индексы правильно:\n```sql\n-- Создайте индексы на столбцы в WHERE и JOIN\nCREATE INDEX idx_orders_user_id ON orders(user_id);\nCREATE INDEX idx_orders_date ON orders(created_at);\n```\n\n### 2. Выбирайте только нужные столбцы:\n```sql\n-- Плохо\nSELECT * FROM users;\n\n-- Хорошо\nSELECT name, email FROM users;\n```\n\n### 3. Используйте EXPLAIN ANALYZE:\n```sql\nEXPLAIN ANALYZE\nSELECT u.name, COUNT(o.id)\nFROM users u\nJOIN orders o ON u.id = o.user_id\nGROUP BY u.id, u.name;\n```\n\n### 4. Избегайте N+1 запросов:\n```sql\n-- Плохо: запрос в цикле\n-- Для каждого пользователя: SELECT * FROM orders WHERE user_id = ?\n\n-- Хорошо: один JOIN\nSELECT u.*, o.*\nFROM users u\nJOIN orders o ON u.id = o.user_id;\n```\n\n### 5. Правила оптимизации:\n- LIMIT для больших таблиц\n- Избегайте `LIKE '%text%'` — не использует индекс\n- Используйте `EXISTS` вместо `IN` для подзапросов\n- `WHERE` перед `HAVING` (WHERE быстрее)\n- Используйте prepared statements"},
                    {"type": "drag-order", "items": ["Анализировать запрос с EXPLAIN ANALYZE", "Определить узкие места (Seq Scan)", "Создать подходящие индексы", "Переписать запрос при необходимости", "Проверить улучшение повторным EXPLAIN"]},
                    {"type": "multi-select", "question": "Какие приёмы оптимизации SQL-запросов верны?", "options": [{"id": "a", "text": "Выбирать только нужные столбцы", "correct": True}, {"id": "b", "text": "Всегда использовать SELECT *", "correct": False}, {"id": "c", "text": "Создавать индексы на часто фильтруемые столбцы", "correct": True}, {"id": "d", "text": "Использовать EXPLAIN ANALYZE", "correct": True}, {"id": "e", "text": "Избегать JOIN (делать запросы в цикле)", "correct": False}]},
                    {"type": "true-false", "statement": "LIKE '%text%' эффективно использует B-tree индекс.", "correct": False},
                ],
            },
            {
                "t": "Бэкапы и восстановление",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Резервное копирование", "markdown": "## Бэкапы PostgreSQL\n\n### pg_dump — бэкап одной БД:\n```bash\n# SQL-формат (текстовый)\npg_dump -U postgres mydb > backup.sql\n\n# Custom-формат (сжатый, рекомендуется)\npg_dump -U postgres -Fc mydb > backup.dump\n\n# Только структура (без данных)\npg_dump -U postgres --schema-only mydb > schema.sql\n\n# Только данные\npg_dump -U postgres --data-only mydb > data.sql\n```\n\n### pg_dumpall — бэкап всего сервера:\n```bash\npg_dumpall -U postgres > all_databases.sql\n```\n\n### Восстановление:\n```bash\n# Из SQL-файла\npsql -U postgres mydb < backup.sql\n\n# Из custom-формата\npg_restore -U postgres -d mydb backup.dump\n\n# Создать БД и восстановить\npg_restore -U postgres -C -d postgres backup.dump\n```\n\n### Автоматизация (cron):\n```bash\n# Бэкап каждый день в 3:00\n0 3 * * * pg_dump -U postgres -Fc mydb > /backups/mydb_$(date +\\%Y\\%m\\%d).dump\n```\n\n### Правила бэкапов:\n- **3-2-1**: 3 копии, 2 носителя, 1 удалённый\n- Тестируйте восстановление!\n- Храните бэкапы зашифрованными\n- Логируйте процесс бэкапов"},
                    {"type": "matching", "pairs": [{"left": "pg_dump", "right": "Бэкап одной базы данных"}, {"left": "pg_dumpall", "right": "Бэкап всех баз сервера"}, {"left": "pg_restore", "right": "Восстановление из custom-формата"}, {"left": "psql < file.sql", "right": "Восстановление из SQL-файла"}]},
                    {"type": "quiz", "question": "Какой формат бэкапа рекомендуется для PostgreSQL?", "options": [{"id": "a", "text": "SQL (текстовый)", "correct": False}, {"id": "b", "text": "Custom (-Fc)", "correct": True}, {"id": "c", "text": "CSV", "correct": False}, {"id": "d", "text": "JSON", "correct": False}]},
                    {"type": "drag-order", "items": ["Создать бэкап с pg_dump", "Сохранить на удалённый сервер", "Проверить целостность бэкапа", "Протестировать восстановление"]},
                    {"type": "true-false", "statement": "Правило 3-2-1 означает: 3 копии, 2 носителя, 1 удалённый.", "correct": True},
                ],
            },
            {
                "t": "Безопасность SQL",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Безопасность базы данных", "markdown": "## Безопасность SQL\n\n### SQL-инъекции:\nСамая распространённая уязвимость!\n\n❌ Опасно:\n```python\n# НИКОГДА так не делайте!\nquery = f\"SELECT * FROM users WHERE name = '{user_input}'\"\n```\n\nЕсли `user_input = \"'; DROP TABLE users; --\"`:\n```sql\nSELECT * FROM users WHERE name = ''; DROP TABLE users; --'\n```\n\n✅ Безопасно — параметризованные запросы:\n```python\n# Python + psycopg2\ncursor.execute(\n    \"SELECT * FROM users WHERE name = %s\",\n    (user_input,)\n)\n\n# SQLAlchemy\ndb.execute(\n    text(\"SELECT * FROM users WHERE name = :name\"),\n    {\"name\": user_input}\n)\n```\n\n### Управление пользователями:\n```sql\n-- Создать пользователя\nCREATE USER app_user WITH PASSWORD 'strong_password';\n\n-- Дать права на чтение\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO app_user;\n\n-- Дать полные права на одну таблицу\nGRANT ALL ON users TO app_user;\n\n-- Забрать права\nREVOKE DELETE ON users FROM app_user;\n```\n\n### Правила безопасности:\n- Используйте параметризованные запросы\n- Принцип наименьших привилегий\n- Не используйте root/postgres в приложении\n- Шифруйте соединение (SSL)\n- Регулярно обновляйте PostgreSQL"},
                    {"type": "quiz", "question": "Как защититься от SQL-инъекций?", "options": [{"id": "a", "text": "Проверять длину ввода", "correct": False}, {"id": "b", "text": "Использовать параметризованные запросы", "correct": True}, {"id": "c", "text": "Запретить символ кавычки", "correct": False}, {"id": "d", "text": "Использовать только SELECT", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите безопасный запрос на Python (psycopg2)", "correctOrder": ["cursor.execute(", "\"SELECT * FROM users WHERE name = %s\",", "(user_input,)", ")"]},
                    {"type": "true-false", "statement": "Конкатенация пользовательского ввода в SQL-запрос безопасна, если проверить длину строки.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "GRANT", "right": "Дать права пользователю"}, {"left": "REVOKE", "right": "Забрать права"}, {"left": "CREATE USER", "right": "Создать пользователя БД"}, {"left": "Параметризованные запросы", "right": "Защита от SQL-инъекций"}]},
                ],
            },
            {
                "t": "ORM — объектно-реляционное отображение",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Работа с БД через ORM", "markdown": "## ORM — Object-Relational Mapping\n\n**ORM** позволяет работать с БД через объекты языка программирования вместо SQL.\n\n### Python — SQLAlchemy:\n```python\nfrom sqlalchemy import Column, Integer, String\nfrom sqlalchemy.orm import DeclarativeBase\n\nclass Base(DeclarativeBase):\n    pass\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    name = Column(String(100), nullable=False)\n    email = Column(String(255), unique=True)\n```\n\n### CRUD через ORM:\n```python\n# Create\nuser = User(name='Алексей', email='alex@mail.ru')\ndb.add(user)\nawait db.commit()\n\n# Read\nresult = await db.execute(\n    select(User).where(User.age > 25)\n)\nusers = result.scalars().all()\n\n# Update\nuser.name = 'Алексей Новый'\nawait db.commit()\n\n# Delete\nawait db.delete(user)\nawait db.commit()\n```\n\n### Популярные ORM:\n| Язык | ORM |\n|------|-----|\n| Python | SQLAlchemy, Django ORM |\n| JavaScript | Prisma, TypeORM, Sequelize |\n| Java | Hibernate |\n| Go | GORM |\n| Ruby | ActiveRecord |\n\n### SQL vs ORM:\n- **SQL** — полный контроль, максимальная производительность\n- **ORM** — быстрая разработка, безопасность, миграции\n- На практике — комбинируют оба подхода"},
                    {"type": "category-sort", "categories": ["Плюсы ORM", "Минусы ORM"], "items": [{"text": "Быстрая разработка", "category": "Плюсы ORM"}, {"text": "Потеря производительности", "category": "Минусы ORM"}, {"text": "Безопасность от инъекций", "category": "Плюсы ORM"}, {"text": "Сложные запросы неудобны", "category": "Минусы ORM"}, {"text": "Автоматические миграции", "category": "Плюсы ORM"}, {"text": "Абстракция скрывает SQL", "category": "Минусы ORM"}]},
                    {"type": "matching", "pairs": [{"left": "SQLAlchemy", "right": "Python"}, {"left": "Prisma", "right": "JavaScript/TypeScript"}, {"left": "Hibernate", "right": "Java"}, {"left": "ActiveRecord", "right": "Ruby"}]},
                    {"type": "quiz", "question": "Что делает ORM?", "options": [{"id": "a", "text": "Заменяет базу данных", "correct": False}, {"id": "b", "text": "Отображает таблицы на объекты языка", "correct": True}, {"id": "c", "text": "Ускоряет SQL-запросы", "correct": False}, {"id": "d", "text": "Создаёт графический интерфейс", "correct": False}]},
                ],
            },
            {
                "t": "Введение в NoSQL",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "NoSQL базы данных", "markdown": "## Обзор NoSQL\n\n### Типы NoSQL баз данных:\n\n#### 1. Документные (MongoDB):\nХранят JSON-подобные документы.\n```json\n{\n  \"name\": \"Алексей\",\n  \"age\": 25,\n  \"orders\": [\n    {\"product\": \"Ноутбук\", \"price\": 50000},\n    {\"product\": \"Мышка\", \"price\": 1500}\n  ]\n}\n```\n\n#### 2. Ключ-значение (Redis):\nПростейшая модель — ключ и значение.\n```\nSET user:1:name \"Алексей\"\nGET user:1:name  → \"Алексей\"\n```\nИспользуется для кэширования, сессий.\n\n#### 3. Колоночные (Cassandra):\nДанные хранятся по столбцам, а не по строкам.\nИдеально для аналитики больших данных.\n\n#### 4. Графовые (Neo4j):\nДанные в виде узлов и связей.\nИдеально для социальных сетей, рекомендаций.\n\n### PostgreSQL + JSON:\nPostgreSQL поддерживает JSON/JSONB!\n```sql\nCREATE TABLE events (\n    id SERIAL PRIMARY KEY,\n    data JSONB NOT NULL\n);\n\nINSERT INTO events (data) VALUES\n('{\"type\": \"click\", \"page\": \"/home\"}');\n\nSELECT data->>'type' FROM events;\nSELECT * FROM events\nWHERE data @> '{\"type\": \"click\"}';\n```"},
                    {"type": "category-sort", "categories": ["Документные", "Ключ-значение", "Графовые"], "items": [{"text": "MongoDB", "category": "Документные"}, {"text": "Redis", "category": "Ключ-значение"}, {"text": "Neo4j", "category": "Графовые"}, {"text": "CouchDB", "category": "Документные"}, {"text": "Memcached", "category": "Ключ-значение"}, {"text": "ArangoDB", "category": "Графовые"}]},
                    {"type": "quiz", "question": "Какой тип NoSQL лучше всего подходит для кэширования?", "options": [{"id": "a", "text": "Документный", "correct": False}, {"id": "b", "text": "Ключ-значение", "correct": True}, {"id": "c", "text": "Графовый", "correct": False}, {"id": "d", "text": "Колоночный", "correct": False}]},
                    {"type": "true-false", "statement": "PostgreSQL не поддерживает хранение JSON-данных.", "correct": False},
                ],
            },
            {
                "t": "Итоговый проект: база данных интернет-магазина",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Проектируем базу интернет-магазина", "markdown": "## Итоговый проект: интернет-магазин\n\n### Схема базы данных:\n\n```sql\n-- Пользователи\nCREATE TABLE users (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    email VARCHAR(255) UNIQUE NOT NULL,\n    password_hash VARCHAR(255) NOT NULL,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- Категории товаров\nCREATE TABLE categories (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    parent_id INTEGER REFERENCES categories(id)\n);\n\n-- Товары\nCREATE TABLE products (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(200) NOT NULL,\n    description TEXT,\n    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),\n    stock INTEGER DEFAULT 0 CHECK (stock >= 0),\n    category_id INTEGER REFERENCES categories(id),\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- Заказы\nCREATE TABLE orders (\n    id SERIAL PRIMARY KEY,\n    user_id INTEGER NOT NULL REFERENCES users(id),\n    status VARCHAR(20) DEFAULT 'pending',\n    total DECIMAL(10,2) NOT NULL,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n\n-- Позиции заказа\nCREATE TABLE order_items (\n    id SERIAL PRIMARY KEY,\n    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,\n    product_id INTEGER NOT NULL REFERENCES products(id),\n    quantity INTEGER NOT NULL CHECK (quantity > 0),\n    price DECIMAL(10,2) NOT NULL\n);\n```\n\n### Индексы:\n```sql\nCREATE INDEX idx_products_category ON products(category_id);\nCREATE INDEX idx_orders_user ON orders(user_id);\nCREATE INDEX idx_order_items_order ON order_items(order_id);\n```\n\n### Полезные запросы:\n```sql\n-- Топ-5 популярных товаров\nSELECT p.name, SUM(oi.quantity) AS total_sold\nFROM products p\nJOIN order_items oi ON p.id = oi.product_id\nGROUP BY p.id, p.name\nORDER BY total_sold DESC\nLIMIT 5;\n\n-- Выручка по месяцам\nSELECT\n    DATE_TRUNC('month', created_at) AS month,\n    SUM(total) AS revenue,\n    COUNT(*) AS order_count\nFROM orders\nWHERE status = 'completed'\nGROUP BY month\nORDER BY month;\n```"},
                    {"type": "drag-order", "items": ["Определить сущности (users, products, orders)", "Спроектировать связи между таблицами", "Написать CREATE TABLE с ограничениями", "Создать индексы на часто используемые столбцы", "Написать и протестировать SQL-запросы"]},
                    {"type": "quiz", "question": "Какой тип связи между orders и order_items?", "options": [{"id": "a", "text": "Один к одному", "correct": False}, {"id": "b", "text": "Один ко многим", "correct": True}, {"id": "c", "text": "Многие ко многим", "correct": False}, {"id": "d", "text": "Нет связи", "correct": False}]},
                    {"type": "multi-select", "question": "Какие ограничения использованы в проекте?", "options": [{"id": "a", "text": "PRIMARY KEY", "correct": True}, {"id": "b", "text": "CHECK", "correct": True}, {"id": "c", "text": "FOREIGN KEY", "correct": True}, {"id": "d", "text": "UNIQUE", "correct": True}, {"id": "e", "text": "TRIGGER", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Что вы изучили: SELECT", "back": "Чтение данных, фильтрация, сортировка, агрегация"}, {"front": "Что вы изучили: JOIN", "back": "INNER, LEFT, RIGHT, FULL JOIN, подзапросы, UNION"}, {"front": "Что вы изучили: DDL", "back": "CREATE TABLE, ALTER TABLE, типы данных, ограничения"}, {"front": "Что вы изучили: DML", "back": "INSERT, UPDATE, DELETE, транзакции"}, {"front": "Что вы изучили: Продвинутое", "back": "Индексы, EXPLAIN, Views, оконные функции, процедуры"}]},
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
            slug="sql-databases-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Database",
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
                    edges.append(
                        {"id": f"e-{lc}", "source": nodes[-2]["id"], "target": nodes[-1]["id"]}
                    )
                lc += 1
                tl += 1
        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
