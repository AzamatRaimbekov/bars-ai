"""Seed: Data Science и аналитика данных — 7 sections, ~40 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Data Science и аналитика данных"
DESC = (
    "Полный курс по Data Science — от статистики и Pandas до машинного обучения "
    "и реальных проектов. Научитесь анализировать данные, строить модели и "
    "визуализировать результаты на Python."
)

S = [
    # ===== SECTION 1: Введение в Data Science =====
    {
        "title": "Введение в Data Science",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое Data Science",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Data Science — наука о данных", "markdown": "## Что такое Data Science?\n\n**Data Science** (наука о данных) — это междисциплинарная область, которая использует научные методы, алгоритмы и системы для извлечения знаний из данных.\n\n### Три столпа Data Science:\n1. **Математика и статистика** — основа анализа\n2. **Программирование** — инструмент обработки\n3. **Доменная экспертиза** — понимание бизнеса\n\n### Зачем нужен Data Science?\n- Прогнозирование продаж и спроса\n- Рекомендательные системы (Netflix, Spotify)\n- Обнаружение мошенничества\n- Медицинская диагностика\n- Автономные автомобили\n\n### Типичный процесс:\n```\nДанные → Очистка → Анализ → Моделирование → Визуализация → Решение\n```"},
                    {"type": "quiz", "question": "Какие три столпа составляют Data Science?", "options": [{"id": "a", "text": "Математика, программирование, доменная экспертиза", "correct": True}, {"id": "b", "text": "Python, SQL, Excel", "correct": False}, {"id": "c", "text": "Статистика, дизайн, маркетинг", "correct": False}, {"id": "d", "text": "Алгоритмы, базы данных, облака", "correct": False}]},
                    {"type": "true-false", "statement": "Data Science используется только в IT-компаниях и не применяется в медицине или финансах.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Data Science", "back": "Междисциплинарная область, извлекающая знания из данных"}, {"front": "Доменная экспертиза", "back": "Глубокое понимание конкретной отрасли/бизнеса"}, {"front": "ETL", "back": "Extract, Transform, Load — процесс обработки данных"}, {"front": "Инсайт", "back": "Ценное наблюдение, полученное из анализа данных"}]},
                ],
            },
            {
                "t": "Роли в Data Science",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Кто есть кто в мире данных", "markdown": "## Роли в Data Science\n\n### Аналитик данных (Data Analyst)\n- Анализирует данные, строит отчёты и дашборды\n- Инструменты: SQL, Excel, Tableau, Power BI\n- Зарплата: средняя\n\n### Data Scientist\n- Строит предсказательные модели\n- Инструменты: Python, scikit-learn, TensorFlow\n- Зарплата: выше средней\n\n### ML Engineer\n- Деплоит модели в продакшн\n- Инструменты: Docker, MLflow, Kubernetes\n- Зарплата: высокая\n\n### Data Engineer\n- Строит пайплайны данных (ETL)\n- Инструменты: Spark, Airflow, dbt\n- Зарплата: высокая\n\n### Пример задач:\n```\nАналитик: «Продажи упали на 15% в Q3»\nDS: «Модель предсказывает рост в Q4 на 8%»\nML Engineer: «Модель задеплоена, API готов»\nData Engineer: «Пайплайн обновляет данные каждый час»\n```"},
                    {"type": "matching", "pairs": [{"left": "Data Analyst", "right": "Отчёты, дашборды, SQL"}, {"left": "Data Scientist", "right": "Предсказательные модели, Python"}, {"left": "ML Engineer", "right": "Деплой моделей, Docker, MLflow"}, {"left": "Data Engineer", "right": "ETL-пайплайны, Spark, Airflow"}]},
                    {"type": "quiz", "question": "Кто отвечает за деплой ML-моделей в продакшн?", "options": [{"id": "a", "text": "Data Analyst", "correct": False}, {"id": "b", "text": "Data Scientist", "correct": False}, {"id": "c", "text": "ML Engineer", "correct": True}, {"id": "d", "text": "UX Designer", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Data Analyst", "items": ["SQL-запросы", "Построение дашбордов"]}, {"name": "Data Scientist", "items": ["Обучение моделей", "Статистический анализ"]}, {"name": "Data Engineer", "items": ["ETL-пайплайны", "Настройка Spark"]}]},
                ],
            },
            {
                "t": "Инструменты Data Scientist",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Набор инструментов DS", "markdown": "## Основные инструменты\n\n### Языки программирования:\n- **Python** — главный язык DS (90% вакансий)\n- **R** — статистика и академия\n- **SQL** — работа с базами данных\n\n### Python-библиотеки:\n```python\nimport numpy as np        # Числовые вычисления\nimport pandas as pd       # Работа с таблицами\nimport matplotlib.pyplot as plt  # Графики\nimport seaborn as sns     # Красивые графики\nimport sklearn            # Машинное обучение\n```\n\n### Среды разработки:\n- **Jupyter Notebook** — интерактивные блокноты\n- **Google Colab** — Jupyter в облаке (бесплатно)\n- **VS Code** — полноценная IDE\n\n### Платформы:\n- **Kaggle** — соревнования и датасеты\n- **GitHub** — хранение кода\n- **Hugging Face** — модели NLP"},
                    {"type": "multi-select", "question": "Какие из этих библиотек используются в Data Science на Python?", "options": [{"id": "a", "text": "pandas", "correct": True}, {"id": "b", "text": "numpy", "correct": True}, {"id": "c", "text": "React", "correct": False}, {"id": "d", "text": "scikit-learn", "correct": True}, {"id": "e", "text": "Express.js", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "pandas", "right": "Работа с таблицами данных"}, {"left": "numpy", "right": "Числовые вычисления и массивы"}, {"left": "matplotlib", "right": "Построение графиков"}, {"left": "scikit-learn", "right": "Машинное обучение"}]},
                    {"type": "true-false", "statement": "Python используется в более чем 90% вакансий Data Scientist.", "correct": True},
                ],
            },
            {
                "t": "Python для Data Science",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Основы Python для DS", "markdown": "## Python — язык Data Science\n\n### Переменные и типы данных:\n```python\nname = \"Датасет\"          # строка\nrows = 1000               # целое число\naccuracy = 0.95           # дробное число\nis_clean = True           # булево\nfeatures = [\"age\", \"salary\", \"city\"]  # список\n```\n\n### Списки и словари:\n```python\n# Список\nscores = [85, 92, 78, 96, 88]\nmean_score = sum(scores) / len(scores)  # 87.8\n\n# Словарь\nstudent = {\n    \"name\": \"Алия\",\n    \"score\": 92,\n    \"passed\": True\n}\nprint(student[\"name\"])  # Алия\n```\n\n### List comprehension:\n```python\n# Все чётные числа от 0 до 20\nevens = [x for x in range(21) if x % 2 == 0]\n# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n```\n\n### Функции:\n```python\ndef calculate_mean(data):\n    return sum(data) / len(data)\n\nresult = calculate_mean([10, 20, 30])  # 20.0\n```"},
                    {"type": "code-puzzle", "instructions": "Составьте функцию, которая вычисляет среднее значение списка:", "correctOrder": ["def calculate_mean(data):", "    total = sum(data)", "    count = len(data)", "    return total / count"]},
                    {"type": "fill-blank", "sentence": "Для создания списка из чётных чисел в Python используется ___ comprehension.", "answer": "list"},
                    {"type": "type-answer", "question": "Какой встроенной функцией Python можно узнать длину списка?", "acceptedAnswers": ["len", "len()"]},
                ],
            },
            {
                "t": "Jupyter Notebook",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Jupyter — интерактивная среда", "markdown": "## Jupyter Notebook\n\nJupyter — это интерактивная среда, где код, текст и графики живут вместе.\n\n### Установка:\n```bash\npip install jupyter\njupyter notebook\n```\n\n### Или через Google Colab:\n1. Зайдите на [colab.research.google.com](https://colab.research.google.com)\n2. Создайте новый блокнот\n3. Бесплатный GPU!\n\n### Типы ячеек:\n- **Code** — код Python\n- **Markdown** — текст, заголовки, формулы\n\n### Горячие клавиши:\n| Клавиша | Действие |\n|---------|----------|\n| Shift+Enter | Запустить ячейку |\n| A | Добавить ячейку сверху |\n| B | Добавить ячейку снизу |\n| DD | Удалить ячейку |\n| M | Переключить на Markdown |\n\n### Пример:\n```python\nimport pandas as pd\ndf = pd.read_csv(\"data.csv\")\ndf.head()  # покажет первые 5 строк прямо в блокноте\n```"},
                    {"type": "quiz", "question": "Как запустить ячейку в Jupyter Notebook?", "options": [{"id": "a", "text": "Ctrl+C", "correct": False}, {"id": "b", "text": "Shift+Enter", "correct": True}, {"id": "c", "text": "Alt+F4", "correct": False}, {"id": "d", "text": "F5", "correct": False}]},
                    {"type": "drag-order", "items": ["Установить Jupyter (pip install jupyter)", "Запустить сервер (jupyter notebook)", "Создать новый блокнот", "Написать код в ячейке", "Нажать Shift+Enter для выполнения"]},
                    {"type": "true-false", "statement": "Google Colab — это бесплатная облачная версия Jupyter Notebook с доступом к GPU.", "correct": True},
                ],
            },
        ],
    },
    # ===== SECTION 2: Статистика и математика =====
    {
        "title": "Статистика и математика",
        "pos": 1,
        "lessons": [
            {
                "t": "Среднее, медиана, мода",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Меры центральной тенденции", "markdown": "## Меры центральной тенденции\n\n### Среднее (Mean)\nСумма всех значений / количество значений.\n```python\nimport numpy as np\ndata = [10, 20, 30, 40, 50]\nmean = np.mean(data)  # 30.0\n```\n\n### Медиана (Median)\nЗначение посередине отсортированного ряда.\n```python\ndata = [10, 20, 30, 40, 1000]\nmedian = np.median(data)  # 30.0  (не чувствительна к выбросам!)\nmean = np.mean(data)      # 220.0 (выброс 1000 сильно влияет)\n```\n\n### Мода (Mode)\nСамое частое значение.\n```python\nfrom scipy import stats\ndata = [1, 2, 2, 3, 3, 3, 4]\nmode = stats.mode(data)  # 3 (встречается 3 раза)\n```\n\n### Когда что использовать?\n| Мера | Когда |\n|------|-------|\n| Среднее | Данные без выбросов, нормальное распределение |\n| Медиана | Есть выбросы (зарплаты, цены жилья) |\n| Мода | Категориальные данные |"},
                    {"type": "quiz", "question": "Данные: [10, 20, 30, 40, 1000]. Какая мера лучше отражает центр?", "options": [{"id": "a", "text": "Среднее (220)", "correct": False}, {"id": "b", "text": "Медиана (30)", "correct": True}, {"id": "c", "text": "Мода", "correct": False}, {"id": "d", "text": "Максимум", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Вычислите медиану массива с помощью numpy:", "correctOrder": ["import numpy as np", "data = [15, 22, 8, 42, 31]", "median = np.median(data)", "print(median)"]},
                    {"type": "category-sort", "categories": [{"name": "Среднее", "items": ["Данные без выбросов", "Нормальное распределение"]}, {"name": "Медиана", "items": ["Зарплаты", "Цены на жильё"]}, {"name": "Мода", "items": ["Любимый цвет", "Категории товаров"]}]},
                ],
            },
            {
                "t": "Распределения данных",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Нормальное и другие распределения", "markdown": "## Распределения данных\n\n### Нормальное распределение (гауссово)\nКолоколообразная кривая — самое важное распределение в статистике.\n```python\nimport numpy as np\nimport matplotlib.pyplot as plt\n\ndata = np.random.normal(loc=100, scale=15, size=10000)\nplt.hist(data, bins=50)\nplt.title('Нормальное распределение')\nplt.show()\n```\n\n### Правило 68-95-99.7:\n- **68%** данных в пределах ±1σ от среднего\n- **95%** данных в пределах ±2σ\n- **99.7%** данных в пределах ±3σ\n\n### Стандартное отклонение (σ):\n```python\ndata = [10, 12, 14, 16, 18]\nstd = np.std(data)  # 2.83\n```\n\n### Другие распределения:\n- **Равномерное** — все значения равновероятны\n- **Биномиальное** — да/нет события (орёл/решка)\n- **Пуассоново** — редкие события (звонки в колл-центр)"},
                    {"type": "quiz", "question": "Сколько процентов данных попадает в ±2σ при нормальном распределении?", "options": [{"id": "a", "text": "68%", "correct": False}, {"id": "b", "text": "95%", "correct": True}, {"id": "c", "text": "99.7%", "correct": False}, {"id": "d", "text": "50%", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Нормальное распределение также называют ___ распределением.", "answer": "гауссовым"},
                    {"type": "matching", "pairs": [{"left": "68%", "right": "±1 стандартное отклонение"}, {"left": "95%", "right": "±2 стандартных отклонения"}, {"left": "99.7%", "right": "±3 стандартных отклонения"}, {"left": "σ (сигма)", "right": "Стандартное отклонение"}]},
                    {"type": "true-false", "statement": "При нормальном распределении среднее, медиана и мода совпадают.", "correct": True},
                ],
            },
            {
                "t": "Корреляция",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Корреляция — связь между переменными", "markdown": "## Корреляция\n\nКорреляция показывает, как связаны две переменные.\n\n### Коэффициент корреляции Пирсона (r):\n- **r = 1** — идеальная положительная связь\n- **r = 0** — нет связи\n- **r = -1** — идеальная отрицательная связь\n\n```python\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'рост': [160, 170, 175, 180, 185],\n    'вес': [55, 65, 70, 80, 85]\n})\n\ncorr = df['рост'].corr(df['вес'])  # ~0.99\nprint(f'Корреляция: {corr:.2f}')\n```\n\n### Корреляционная матрица:\n```python\ndf.corr()  # матрица всех пар\nimport seaborn as sns\nsns.heatmap(df.corr(), annot=True, cmap='coolwarm')\n```\n\n### Важно!\n**Корреляция ≠ причинность!**\nПример: продажи мороженого коррелируют с количеством утоплений. Причина — жаркая погода, а не мороженое."},
                    {"type": "quiz", "question": "Коэффициент корреляции r = -0.85 означает:", "options": [{"id": "a", "text": "Сильная отрицательная связь", "correct": True}, {"id": "b", "text": "Слабая связь", "correct": False}, {"id": "c", "text": "Нет связи", "correct": False}, {"id": "d", "text": "Идеальная положительная связь", "correct": False}]},
                    {"type": "true-false", "statement": "Если две переменные коррелируют, значит одна является причиной другой.", "correct": False},
                    {"type": "fill-blank", "sentence": "Коэффициент корреляции Пирсона принимает значения от ___ до 1.", "answer": "-1"},
                ],
            },
            {
                "t": "Проверка гипотез",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Гипотезы и статистические тесты", "markdown": "## Проверка гипотез\n\n### Что такое гипотеза?\n- **H₀ (нулевая)** — «ничего не изменилось», эффекта нет\n- **H₁ (альтернативная)** — «есть эффект/различие»\n\n### Пример:\nЛекарство снижает давление?\n- H₀: Лекарство не влияет на давление\n- H₁: Лекарство снижает давление\n\n### Алгоритм:\n1. Сформулировать H₀ и H₁\n2. Выбрать уровень значимости α (обычно 0.05)\n3. Провести тест\n4. Если p-value < α → отвергаем H₀\n\n### t-тест в Python:\n```python\nfrom scipy import stats\n\ngroup_a = [120, 118, 115, 122, 119]  # контроль\ngroup_b = [110, 108, 112, 105, 109]  # лекарство\n\nt_stat, p_value = stats.ttest_ind(group_a, group_b)\nprint(f'p-value: {p_value:.4f}')\n\nif p_value < 0.05:\n    print('Отвергаем H₀ — эффект есть!')\nelse:\n    print('Не отвергаем H₀')\n```"},
                    {"type": "drag-order", "items": ["Сформулировать H₀ и H₁", "Выбрать уровень значимости α", "Собрать данные", "Провести статистический тест", "Сравнить p-value с α и сделать вывод"]},
                    {"type": "quiz", "question": "Что означает p-value = 0.03 при α = 0.05?", "options": [{"id": "a", "text": "Отвергаем нулевую гипотезу", "correct": True}, {"id": "b", "text": "Не отвергаем нулевую гипотезу", "correct": False}, {"id": "c", "text": "Нужно больше данных", "correct": False}, {"id": "d", "text": "Тест невалиден", "correct": False}]},
                    {"type": "true-false", "statement": "Нулевая гипотеза (H₀) обычно утверждает, что эффекта или различия нет.", "correct": True},
                ],
            },
            {
                "t": "P-value и уровень значимости",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "P-value — вероятность ошибки", "markdown": "## P-value\n\n**P-value** — вероятность получить такие же (или более экстремальные) результаты, если нулевая гипотеза верна.\n\n### Интерпретация:\n- **p < 0.01** — очень сильные доказательства против H₀\n- **p < 0.05** — сильные доказательства (стандартный порог)\n- **p < 0.10** — слабые доказательства\n- **p ≥ 0.10** — нет доказательств\n\n### Ошибки:\n| | H₀ верна | H₀ ложна |\n|---|---|---|\n| Отвергли H₀ | **Ошибка I рода (α)** | Верно! |\n| Не отвергли H₀ | Верно! | **Ошибка II рода (β)** |\n\n### Пример:\n```python\nfrom scipy import stats\n\n# Средний рост студентов = 170 см?\nsample = [168, 172, 175, 169, 171, 173, 167, 174]\nt_stat, p_value = stats.ttest_1samp(sample, 170)\nprint(f'p-value: {p_value:.4f}')  # > 0.05 → не отвергаем\n```\n\n### Важно:\nP-value **НЕ** показывает вероятность того, что гипотеза верна!"},
                    {"type": "category-sort", "categories": [{"name": "Ошибка I рода", "items": ["Отвергли H₀, хотя она верна", "Ложная тревога"]}, {"name": "Ошибка II рода", "items": ["Не отвергли H₀, хотя она ложна", "Пропустили реальный эффект"]}]},
                    {"type": "quiz", "question": "Стандартный порог p-value для отвержения H₀:", "options": [{"id": "a", "text": "0.05", "correct": True}, {"id": "b", "text": "0.5", "correct": False}, {"id": "c", "text": "1.0", "correct": False}, {"id": "d", "text": "0.005", "correct": False}]},
                    {"type": "fill-blank", "sentence": "P-value — это вероятность получить наблюдаемый результат, если ___ гипотеза верна.", "answer": "нулевая"},
                ],
            },
            {
                "t": "A/B-тестирование",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "A/B-тесты на практике", "markdown": "## A/B-тестирование\n\nA/B-тест — это эксперимент, где сравниваются две версии (A и B) чего-либо.\n\n### Пример: конверсия лендинга\n```python\nimport numpy as np\nfrom scipy import stats\n\n# Группа A: старый дизайн\nvisitors_a = 1000\nconversions_a = 50  # 5%\n\n# Группа B: новый дизайн\nvisitors_b = 1000\nconversions_b = 65  # 6.5%\n\n# Z-тест для пропорций\nfrom statsmodels.stats.proportion import proportions_ztest\n\ncount = np.array([conversions_a, conversions_b])\nnobs = np.array([visitors_a, visitors_b])\n\nz_stat, p_value = proportions_ztest(count, nobs)\nprint(f'p-value: {p_value:.4f}')\n\nif p_value < 0.05:\n    print('Новый дизайн статистически лучше!')\nelse:\n    print('Разница не значима')\n```\n\n### Правила хорошего A/B-теста:\n1. **Одна переменная** — меняйте только одну вещь\n2. **Случайное разделение** — пользователи рандомно попадают в A или B\n3. **Достаточный размер выборки** — минимум сотни наблюдений\n4. **Достаточное время** — не останавливайте тест рано\n5. **Заранее определите метрику** — конверсия, CTR, выручка"},
                    {"type": "drag-order", "items": ["Определить метрику и гипотезу", "Рассчитать необходимый размер выборки", "Разделить пользователей на группы A и B", "Провести эксперимент достаточное время", "Проанализировать результаты и принять решение"]},
                    {"type": "multi-select", "question": "Какие из этих правил важны для A/B-теста?", "options": [{"id": "a", "text": "Менять только одну переменную", "correct": True}, {"id": "b", "text": "Случайное разделение на группы", "correct": True}, {"id": "c", "text": "Остановить тест сразу при первом результате", "correct": False}, {"id": "d", "text": "Достаточный размер выборки", "correct": True}]},
                    {"type": "type-answer", "question": "Как называется тест, в котором сравниваются две версии (A и B) продукта?", "acceptedAnswers": ["A/B-тест", "AB тест", "A/B тест", "A/B-тестирование", "ab тест"]},
                ],
            },
        ],
    },
    # ===== SECTION 3: Pandas и обработка данных =====
    {
        "title": "Pandas и обработка данных",
        "pos": 2,
        "lessons": [
            {
                "t": "DataFrame — основная структура",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Pandas DataFrame", "markdown": "## Pandas DataFrame\n\nDataFrame — это таблица данных с именованными столбцами.\n\n### Создание DataFrame:\n```python\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'имя': ['Алия', 'Бекзат', 'Дана'],\n    'возраст': [25, 30, 28],\n    'город': ['Алматы', 'Астана', 'Бишкек']\n})\nprint(df)\n```\n\n| | имя | возраст | город |\n|---|---|---|---|\n| 0 | Алия | 25 | Алматы |\n| 1 | Бекзат | 30 | Астана |\n| 2 | Дана | 28 | Бишкек |\n\n### Основные атрибуты:\n```python\ndf.shape     # (3, 3) — строки, столбцы\ndf.columns   # ['имя', 'возраст', 'город']\ndf.dtypes    # типы данных\ndf.info()    # сводная информация\ndf.describe()  # статистика числовых столбцов\n```\n\n### Доступ к данным:\n```python\ndf['имя']           # один столбец (Series)\ndf[['имя','город']] # несколько столбцов\ndf.iloc[0]          # первая строка по индексу\ndf.loc[0, 'имя']    # конкретное значение\n```"},
                    {"type": "code-puzzle", "instructions": "Создайте DataFrame с колонками 'товар' и 'цена':", "correctOrder": ["import pandas as pd", "df = pd.DataFrame({", "    'товар': ['Яблоко', 'Банан'],", "    'цена': [150, 200]", "})", "print(df)"]},
                    {"type": "quiz", "question": "Как получить количество строк и столбцов DataFrame?", "options": [{"id": "a", "text": "df.shape", "correct": True}, {"id": "b", "text": "df.size()", "correct": False}, {"id": "c", "text": "df.count()", "correct": False}, {"id": "d", "text": "len(df.columns)", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для доступа к строке по числовому индексу используется df.___[0].", "answer": "iloc"},
                ],
            },
            {
                "t": "Загрузка и сохранение данных",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Чтение CSV и других форматов", "markdown": "## Загрузка данных\n\n### CSV — самый популярный формат:\n```python\nimport pandas as pd\n\n# Чтение\ndf = pd.read_csv('sales.csv')\ndf = pd.read_csv('sales.csv', sep=';', encoding='utf-8')\n\n# Первые/последние строки\ndf.head()    # первые 5\ndf.tail(3)   # последние 3\n```\n\n### Другие форматы:\n```python\n# Excel\ndf = pd.read_excel('data.xlsx', sheet_name='Sheet1')\n\n# JSON\ndf = pd.read_json('data.json')\n\n# SQL\nimport sqlite3\nconn = sqlite3.connect('database.db')\ndf = pd.read_sql('SELECT * FROM users', conn)\n\n# Из интернета\nurl = 'https://example.com/data.csv'\ndf = pd.read_csv(url)\n```\n\n### Сохранение:\n```python\ndf.to_csv('output.csv', index=False)\ndf.to_excel('output.xlsx', index=False)\ndf.to_json('output.json', orient='records')\n```"},
                    {"type": "matching", "pairs": [{"left": "pd.read_csv()", "right": "Чтение CSV-файла"}, {"left": "pd.read_excel()", "right": "Чтение Excel-файла"}, {"left": "df.to_csv()", "right": "Сохранение в CSV"}, {"left": "df.head()", "right": "Первые 5 строк таблицы"}]},
                    {"type": "type-answer", "question": "Какой функцией pandas загрузить CSV-файл?", "acceptedAnswers": ["pd.read_csv", "read_csv", "pd.read_csv()"]},
                    {"type": "true-false", "statement": "Pandas может читать данные напрямую из URL в интернете.", "correct": True},
                ],
            },
            {
                "t": "Фильтрация данных",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Фильтрация и выборка", "markdown": "## Фильтрация данных в Pandas\n\n### Фильтрация по условию:\n```python\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'товар': ['Ноутбук', 'Телефон', 'Планшет', 'Наушники'],\n    'цена': [150000, 80000, 60000, 15000],\n    'категория': ['Техника', 'Техника', 'Техника', 'Аксессуары']\n})\n\n# Одно условие\ncheap = df[df['цена'] < 70000]\n\n# Несколько условий (AND)\nfiltered = df[(df['цена'] > 50000) & (df['категория'] == 'Техника')]\n\n# Несколько условий (OR)\nfiltered = df[(df['цена'] < 20000) | (df['товар'] == 'Ноутбук')]\n```\n\n### Полезные методы:\n```python\ndf['товар'].isin(['Ноутбук', 'Телефон'])  # входит ли в список\ndf['цена'].between(50000, 100000)          # в диапазоне\ndf.query('цена > 50000 and категория == \"Техника\"')  # SQL-подобный синтаксис\ndf.nlargest(3, 'цена')    # топ-3 по цене\ndf.nsmallest(2, 'цена')   # 2 самых дешёвых\n```"},
                    {"type": "code-puzzle", "instructions": "Отфильтруйте товары дороже 50000:", "correctOrder": ["import pandas as pd", "df = pd.read_csv('products.csv')", "expensive = df[df['цена'] > 50000]", "print(expensive)"]},
                    {"type": "quiz", "question": "Как правильно задать два условия фильтрации (AND) в Pandas?", "options": [{"id": "a", "text": "df[(условие1) & (условие2)]", "correct": True}, {"id": "b", "text": "df[условие1 and условие2]", "correct": False}, {"id": "c", "text": "df.filter(условие1, условие2)", "correct": False}, {"id": "d", "text": "df[условие1 + условие2]", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Метод df.query() позволяет фильтровать данные с помощью ___-подобного синтаксиса.", "answer": "SQL"},
                ],
            },
            {
                "t": "Группировка данных (groupby)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "GroupBy — агрегация данных", "markdown": "## Группировка данных\n\n### groupby — мощный инструмент агрегации:\n```python\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'город': ['Алматы', 'Астана', 'Алматы', 'Астана', 'Бишкек'],\n    'категория': ['Еда', 'Еда', 'Техника', 'Еда', 'Техника'],\n    'продажи': [1000, 1500, 5000, 2000, 3000]\n})\n\n# Среднее по городам\ndf.groupby('город')['продажи'].mean()\n\n# Несколько агрегаций\ndf.groupby('город')['продажи'].agg(['sum', 'mean', 'count'])\n\n# Группировка по двум столбцам\ndf.groupby(['город', 'категория'])['продажи'].sum()\n```\n\n### Результат:\n```\nгород     категория\nАлматы    Еда          1000\n          Техника      5000\nАстана    Еда          3500\nБишкек    Техника      3000\n```\n\n### Полезные агрегации:\n```python\n.sum()    # сумма\n.mean()   # среднее\n.count()  # количество\n.min()    # минимум\n.max()    # максимум\n.std()    # стандартное отклонение\n```"},
                    {"type": "code-puzzle", "instructions": "Найдите суммарные продажи по городам:", "correctOrder": ["import pandas as pd", "df = pd.read_csv('sales.csv')", "result = df.groupby('город')['продажи'].sum()", "print(result)"]},
                    {"type": "multi-select", "question": "Какие агрегатные функции можно использовать с groupby?", "options": [{"id": "a", "text": "sum()", "correct": True}, {"id": "b", "text": "mean()", "correct": True}, {"id": "c", "text": "plot()", "correct": False}, {"id": "d", "text": "count()", "correct": True}, {"id": "e", "text": "read_csv()", "correct": False}]},
                    {"type": "type-answer", "question": "Какой метод pandas используется для группировки данных?", "acceptedAnswers": ["groupby", "groupby()", "df.groupby"]},
                ],
            },
            {
                "t": "Merge и join таблиц",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Объединение таблиц", "markdown": "## Merge — объединение таблиц\n\n### Пример: таблицы заказов и клиентов\n```python\nimport pandas as pd\n\norders = pd.DataFrame({\n    'order_id': [1, 2, 3],\n    'client_id': [101, 102, 101],\n    'сумма': [5000, 3000, 7000]\n})\n\nclients = pd.DataFrame({\n    'client_id': [101, 102, 103],\n    'имя': ['Алия', 'Бекзат', 'Дана']\n})\n\n# INNER JOIN (только совпадения)\nresult = pd.merge(orders, clients, on='client_id')\n\n# LEFT JOIN (все из левой + совпадения из правой)\nresult = pd.merge(orders, clients, on='client_id', how='left')\n\n# RIGHT JOIN\nresult = pd.merge(orders, clients, on='client_id', how='right')\n\n# OUTER JOIN (все из обеих)\nresult = pd.merge(orders, clients, on='client_id', how='outer')\n```\n\n### concat — склейка таблиц:\n```python\n# Вертикально (друг под другом)\ndf_all = pd.concat([df_jan, df_feb, df_mar])\n\n# Горизонтально\ndf_wide = pd.concat([df1, df2], axis=1)\n```"},
                    {"type": "matching", "pairs": [{"left": "inner", "right": "Только совпадающие строки"}, {"left": "left", "right": "Все из левой таблицы"}, {"left": "right", "right": "Все из правой таблицы"}, {"left": "outer", "right": "Все строки из обеих таблиц"}]},
                    {"type": "quiz", "question": "Какой тип merge вернёт все строки из обеих таблиц?", "options": [{"id": "a", "text": "inner", "correct": False}, {"id": "b", "text": "left", "correct": False}, {"id": "c", "text": "right", "correct": False}, {"id": "d", "text": "outer", "correct": True}]},
                    {"type": "code-puzzle", "instructions": "Объедините таблицы orders и clients по client_id (LEFT JOIN):", "correctOrder": ["import pandas as pd", "result = pd.merge(", "    orders, clients,", "    on='client_id',", "    how='left'", ")"]},
                ],
            },
            {
                "t": "Очистка данных",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Грязные данные — главный враг", "markdown": "## Очистка данных\n\n80% работы Data Scientist — это очистка данных!\n\n### Пропущенные значения (NaN):\n```python\nimport pandas as pd\nimport numpy as np\n\ndf = pd.DataFrame({\n    'имя': ['Алия', 'Бекзат', None, 'Дана'],\n    'возраст': [25, np.nan, 28, 30],\n    'зарплата': [500000, 700000, np.nan, 600000]\n})\n\n# Найти пропуски\ndf.isnull().sum()\n\n# Удалить строки с пропусками\ndf_clean = df.dropna()\n\n# Заполнить пропуски\ndf['возраст'].fillna(df['возраст'].mean(), inplace=True)\ndf['имя'].fillna('Неизвестно', inplace=True)\n```\n\n### Дубликаты:\n```python\ndf.duplicated().sum()      # количество дубликатов\ndf.drop_duplicates()       # удалить дубликаты\n```\n\n### Типы данных:\n```python\ndf['дата'] = pd.to_datetime(df['дата'])\ndf['цена'] = df['цена'].astype(float)\n```\n\n### Выбросы:\n```python\nQ1 = df['зарплата'].quantile(0.25)\nQ3 = df['зарплата'].quantile(0.75)\nIQR = Q3 - Q1\ndf_no_outliers = df[\n    (df['зарплата'] >= Q1 - 1.5*IQR) &\n    (df['зарплата'] <= Q3 + 1.5*IQR)\n]\n```"},
                    {"type": "drag-order", "items": ["Загрузить данные (pd.read_csv)", "Проверить пропуски (isnull().sum())", "Обработать пропуски (fillna / dropna)", "Удалить дубликаты (drop_duplicates)", "Исправить типы данных (astype)", "Обработать выбросы (IQR-метод)"]},
                    {"type": "quiz", "question": "Как заполнить пропуски средним значением столбца 'age'?", "options": [{"id": "a", "text": "df['age'].fillna(df['age'].mean())", "correct": True}, {"id": "b", "text": "df['age'].dropna()", "correct": False}, {"id": "c", "text": "df['age'].replace(0)", "correct": False}, {"id": "d", "text": "df['age'].clean()", "correct": False}]},
                    {"type": "true-false", "statement": "По оценкам экспертов, около 80% работы Data Scientist уходит на очистку данных.", "correct": True},
                    {"type": "fill-blank", "sentence": "Для удаления дубликатов в pandas используется метод ___.", "answer": "drop_duplicates"},
                ],
            },
        ],
    },
    # ===== SECTION 4: Визуализация =====
    {
        "title": "Визуализация данных",
        "pos": 3,
        "lessons": [
            {
                "t": "Matplotlib — основы графиков",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Matplotlib — фундамент визуализации", "markdown": "## Matplotlib\n\nMatplotlib — базовая библиотека для графиков в Python.\n\n### Линейный график:\n```python\nimport matplotlib.pyplot as plt\n\nmonths = ['Янв', 'Фев', 'Мар', 'Апр', 'Май']\nsales = [100, 120, 115, 135, 150]\n\nplt.figure(figsize=(10, 6))\nplt.plot(months, sales, marker='o', color='blue')\nplt.title('Продажи по месяцам')\nplt.xlabel('Месяц')\nplt.ylabel('Продажи')\nplt.grid(True)\nplt.show()\n```\n\n### Столбчатый график:\n```python\nplt.bar(months, sales, color='skyblue')\nplt.title('Продажи по месяцам')\nplt.show()\n```\n\n### Круговая диаграмма:\n```python\ncategories = ['Еда', 'Транспорт', 'Жильё', 'Другое']\nexpenses = [30, 20, 35, 15]\nplt.pie(expenses, labels=categories, autopct='%1.1f%%')\nplt.title('Расходы')\nplt.show()\n```\n\n### Scatter (точечный):\n```python\nplt.scatter(df['рост'], df['вес'], alpha=0.5)\nplt.xlabel('Рост')\nplt.ylabel('Вес')\nplt.show()\n```"},
                    {"type": "matching", "pairs": [{"left": "plt.plot()", "right": "Линейный график"}, {"left": "plt.bar()", "right": "Столбчатый график"}, {"left": "plt.pie()", "right": "Круговая диаграмма"}, {"left": "plt.scatter()", "right": "Точечный график"}]},
                    {"type": "quiz", "question": "Какой тип графика лучше для показа тренда по времени?", "options": [{"id": "a", "text": "Линейный (plot)", "correct": True}, {"id": "b", "text": "Круговая диаграмма (pie)", "correct": False}, {"id": "c", "text": "Гистограмма (hist)", "correct": False}, {"id": "d", "text": "Точечный (scatter)", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для отображения графика в Matplotlib вызывается метод plt.___().", "answer": "show"},
                ],
            },
            {
                "t": "Seaborn — красивые графики",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Seaborn — продвинутая визуализация", "markdown": "## Seaborn\n\nSeaborn — надстройка над Matplotlib с красивыми стилями.\n\n### Установка:\n```python\npip install seaborn\nimport seaborn as sns\nsns.set_theme()  # включить красивый стиль\n```\n\n### Гистограмма с KDE:\n```python\nsns.histplot(df['возраст'], kde=True, bins=20)\nplt.title('Распределение возраста')\nplt.show()\n```\n\n### Box plot (ящик с усами):\n```python\nsns.boxplot(x='город', y='зарплата', data=df)\nplt.title('Зарплаты по городам')\nplt.show()\n```\n\n### Heatmap (тепловая карта):\n```python\ncorr = df.corr()\nsns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')\nplt.title('Корреляционная матрица')\nplt.show()\n```\n\n### Pairplot — все пары:\n```python\nsns.pairplot(df, hue='категория')\nplt.show()\n```\n\nPairplot автоматически строит scatter для всех пар числовых столбцов — отличный способ быстро исследовать данные!"},
                    {"type": "quiz", "question": "Какой график Seaborn показывает корреляцию между всеми переменными?", "options": [{"id": "a", "text": "sns.pairplot()", "correct": True}, {"id": "b", "text": "sns.barplot()", "correct": False}, {"id": "c", "text": "sns.lineplot()", "correct": False}, {"id": "d", "text": "sns.catplot()", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "sns.histplot()", "right": "Гистограмма распределения"}, {"left": "sns.boxplot()", "right": "Ящик с усами (квартили, выбросы)"}, {"left": "sns.heatmap()", "right": "Тепловая карта корреляций"}, {"left": "sns.pairplot()", "right": "Графики всех пар переменных"}]},
                    {"type": "true-false", "statement": "Seaborn — это отдельная библиотека, не связанная с Matplotlib.", "correct": False},
                ],
            },
            {
                "t": "Выбор типа графика",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Какой график когда использовать", "markdown": "## Выбор правильного графика\n\n### Тренд по времени → Линейный\n```python\nplt.plot(dates, values)\n```\nПродажи, температура, курс валют.\n\n### Сравнение категорий → Столбчатый\n```python\nplt.bar(categories, values)\n```\nДоход по отделам, оценки по предметам.\n\n### Распределение → Гистограмма / Box plot\n```python\nsns.histplot(data)     # гистограмма\nsns.boxplot(data)      # квартили + выбросы\n```\nВозраст клиентов, зарплаты.\n\n### Связь двух переменных → Scatter\n```python\nplt.scatter(x, y)\n```\nРост vs вес, расходы на рекламу vs продажи.\n\n### Доли целого → Круговая\n```python\nplt.pie(values, labels=labels)\n```\nДоля рынка, структура расходов.\n\n### Корреляция → Heatmap\n```python\nsns.heatmap(df.corr())\n```\nВзаимосвязь всех числовых переменных."},
                    {"type": "category-sort", "categories": [{"name": "Линейный график", "items": ["Продажи по месяцам", "Курс валют"]}, {"name": "Столбчатый график", "items": ["Сравнение отделов", "Оценки по предметам"]}, {"name": "Scatter", "items": ["Рост vs вес", "Реклама vs продажи"]}, {"name": "Круговая диаграмма", "items": ["Доля рынка", "Структура бюджета"]}]},
                    {"type": "quiz", "question": "Какой график лучше для поиска выбросов?", "options": [{"id": "a", "text": "Box plot", "correct": True}, {"id": "b", "text": "Круговая диаграмма", "correct": False}, {"id": "c", "text": "Линейный график", "correct": False}, {"id": "d", "text": "Столбчатый график", "correct": False}]},
                    {"type": "true-false", "statement": "Круговая диаграмма хорошо подходит для сравнения большого количества категорий (более 7).", "correct": False},
                ],
            },
            {
                "t": "Дашборды и интерактивные графики",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Plotly и Streamlit", "markdown": "## Интерактивная визуализация\n\n### Plotly — интерактивные графики:\n```python\nimport plotly.express as px\n\ndf = px.data.gapminder()\nfig = px.scatter(\n    df[df['year']==2007],\n    x='gdpPercap', y='lifeExp',\n    size='pop', color='continent',\n    hover_name='country',\n    title='ВВП vs Продолжительность жизни'\n)\nfig.show()\n```\n\n### Streamlit — дашборды за минуты:\n```python\n# app.py\nimport streamlit as st\nimport pandas as pd\n\nst.title('Мой дашборд')\n\ndf = pd.read_csv('sales.csv')\nst.dataframe(df)\n\ncity = st.selectbox('Город', df['город'].unique())\nfiltered = df[df['город'] == city]\nst.bar_chart(filtered.set_index('месяц')['продажи'])\n\nst.metric('Всего продаж', f\"{filtered['продажи'].sum():,} ₸\")\n```\n\n### Запуск:\n```bash\npip install streamlit\nstreamlit run app.py\n```\n\nStreamlit — самый быстрый способ превратить анализ в веб-приложение!"},
                    {"type": "matching", "pairs": [{"left": "Plotly", "right": "Интерактивные графики в Jupyter"}, {"left": "Streamlit", "right": "Веб-дашборды на Python"}, {"left": "Tableau", "right": "Коммерческий BI-инструмент"}, {"left": "Power BI", "right": "BI-инструмент Microsoft"}]},
                    {"type": "quiz", "question": "Какой инструмент позволяет быстро создать веб-дашборд на Python?", "options": [{"id": "a", "text": "Streamlit", "correct": True}, {"id": "b", "text": "NumPy", "correct": False}, {"id": "c", "text": "scikit-learn", "correct": False}, {"id": "d", "text": "BeautifulSoup", "correct": False}]},
                    {"type": "type-answer", "question": "Какой командой запустить Streamlit-приложение из файла app.py?", "acceptedAnswers": ["streamlit run app.py", "streamlit run app.py"]},
                ],
            },
            {
                "t": "Storytelling с данными",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Как рассказывать истории данными", "markdown": "## Data Storytelling\n\nДанные без истории — просто числа. Storytelling превращает анализ в убедительное повествование.\n\n### Структура data story:\n1. **Контекст** — почему это важно?\n2. **Проблема** — что мы обнаружили?\n3. **Данные** — доказательства (графики)\n4. **Инсайт** — что это значит?\n5. **Действие** — что делать дальше?\n\n### Пример:\n> ❌ «Конверсия лендинга — 2.3%»\n>\n> ✅ «Конверсия нашего лендинга (2.3%) в 2 раза ниже\n> среднего по индустрии (4.5%). A/B-тест показал, что\n> изменение CTA-кнопки с \"Узнать\" на \"Начать бесплатно\"\n> поднимет конверсию на 40%. Рекомендация: внедрить\n> новый CTA на следующей неделе.»\n\n### Правила хороших графиков:\n- **Один график — одна мысль**\n- Убирайте лишнее (chartjunk)\n- Подписывайте оси\n- Используйте правильные масштабы\n- Добавляйте заголовок-вывод, а не описание"},
                    {"type": "drag-order", "items": ["Определить контекст и аудиторию", "Сформулировать проблему/вопрос", "Подкрепить данными и графиками", "Сделать инсайт (что это значит)", "Дать рекомендацию к действию"]},
                    {"type": "quiz", "question": "Какой заголовок графика лучше для data storytelling?", "options": [{"id": "a", "text": "Продажи выросли на 25% после запуска рекламы", "correct": True}, {"id": "b", "text": "График продаж за 2025 год", "correct": False}, {"id": "c", "text": "Данные", "correct": False}, {"id": "d", "text": "Рис. 1", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "Chartjunk", "back": "Лишние визуальные элементы, не несущие информации"}, {"front": "Data-ink ratio", "back": "Доля «чернил» на графике, несущих информацию (чем выше — тем лучше)"}, {"front": "Инсайт", "back": "Неочевидный вывод, полученный из анализа данных"}, {"front": "CTA", "back": "Call to Action — призыв к действию"}]},
                ],
            },
        ],
    },
    # ===== SECTION 5: Machine Learning — основы =====
    {
        "title": "Machine Learning — основы",
        "pos": 4,
        "lessons": [
            {
                "t": "Supervised vs Unsupervised",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Два типа машинного обучения", "markdown": "## Типы машинного обучения\n\n### Supervised Learning (обучение с учителем)\nМодель учится на данных с **правильными ответами** (метками).\n\n**Примеры:**\n- Спам / не спам (есть метки)\n- Цена квартиры (есть исторические цены)\n- Диагноз по снимку (есть диагнозы врачей)\n\n```\nВходные данные → [Модель] → Предсказание\n     +\nПравильные ответы (labels)\n```\n\n### Unsupervised Learning (обучение без учителя)\nМодель **сама** находит закономерности в данных.\n\n**Примеры:**\n- Сегментация клиентов\n- Обнаружение аномалий\n- Снижение размерности (PCA)\n\n```\nВходные данные → [Модель] → Группы/Паттерны\n     (без меток)\n```\n\n### Reinforcement Learning (обучение с подкреплением)\nАгент учится через **награды и штрафы**.\n- Игры (AlphaGo)\n- Робототехника\n- Торговые стратегии"},
                    {"type": "category-sort", "categories": [{"name": "Supervised Learning", "items": ["Определение спама", "Предсказание цены", "Классификация изображений"]}, {"name": "Unsupervised Learning", "items": ["Сегментация клиентов", "Обнаружение аномалий", "Кластеризация"]}]},
                    {"type": "quiz", "question": "Если у нас есть данные клиентов без меток и мы хотим найти группы — какой тип ML?", "options": [{"id": "a", "text": "Unsupervised Learning", "correct": True}, {"id": "b", "text": "Supervised Learning", "correct": False}, {"id": "c", "text": "Reinforcement Learning", "correct": False}, {"id": "d", "text": "Transfer Learning", "correct": False}]},
                    {"type": "true-false", "statement": "Supervised Learning требует данных с правильными ответами (метками).", "correct": True},
                ],
            },
            {
                "t": "Линейная регрессия",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Предсказание числовых значений", "markdown": "## Линейная регрессия\n\nПростейшая модель для предсказания числовых значений.\n\n### Формула:\n```\ny = w₁·x₁ + w₂·x₂ + ... + b\n```\n\n### Пример: предсказание цены квартиры\n```python\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nimport pandas as pd\n\n# Данные\ndf = pd.DataFrame({\n    'площадь': [30, 45, 60, 75, 90, 100, 120],\n    'комнаты': [1, 1, 2, 2, 3, 3, 4],\n    'цена': [3.5, 5.0, 7.0, 8.5, 10.0, 11.0, 14.0]  # млн\n})\n\n# Разделение на train/test\nX = df[['площадь', 'комнаты']]\ny = df['цена']\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42\n)\n\n# Обучение\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\n\n# Предсказание\npred = model.predict([[80, 3]])  # 80 м², 3 комнаты\nprint(f'Предсказанная цена: {pred[0]:.1f} млн')\n\n# Оценка\nprint(f'R² score: {model.score(X_test, y_test):.2f}')\n```"},
                    {"type": "drag-order", "items": ["Подготовить данные (X, y)", "Разделить на train и test", "Создать модель (LinearRegression)", "Обучить модель (model.fit)", "Сделать предсказание (model.predict)"]},
                    {"type": "code-puzzle", "instructions": "Обучите линейную регрессию:", "correctOrder": ["from sklearn.linear_model import LinearRegression", "model = LinearRegression()", "model.fit(X_train, y_train)", "predictions = model.predict(X_test)"]},
                    {"type": "fill-blank", "sentence": "Метрика R² показывает, какую долю ___ в данных объясняет модель.", "answer": "дисперсии"},
                ],
            },
            {
                "t": "Классификация",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Предсказание категорий", "markdown": "## Классификация\n\nКлассификация — предсказание **категории** (класса).\n\n### Примеры:\n- Спам / не спам\n- Кошка / собака\n- Заболел / здоров\n\n### Логистическая регрессия:\n```python\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import accuracy_score\n\n# Данные: одобрение кредита\nimport pandas as pd\ndf = pd.DataFrame({\n    'доход': [30, 50, 70, 40, 90, 60, 80, 35],\n    'возраст': [22, 35, 45, 28, 50, 33, 42, 25],\n    'одобрен': [0, 1, 1, 0, 1, 1, 1, 0]  # 0=нет, 1=да\n})\n\nX = df[['доход', 'возраст']]\ny = df['одобрен']\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42\n)\n\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\n\ny_pred = model.predict(X_test)\nprint(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')\n```\n\n### Бинарная vs мультиклассовая:\n- **Бинарная:** да/нет, спам/не спам\n- **Мультиклассовая:** кошка/собака/птица"},
                    {"type": "quiz", "question": "Какая задача является задачей классификации?", "options": [{"id": "a", "text": "Определить спам или не спам", "correct": True}, {"id": "b", "text": "Предсказать цену квартиры", "correct": False}, {"id": "c", "text": "Найти группы клиентов", "correct": False}, {"id": "d", "text": "Уменьшить количество признаков", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Регрессия", "right": "Предсказание числа (цена, температура)"}, {"left": "Бинарная классификация", "right": "Да/нет (спам/не спам)"}, {"left": "Мультиклассовая", "right": "Несколько категорий (кошка/собака/птица)"}, {"left": "Accuracy", "right": "Доля правильных предсказаний"}]},
                    {"type": "type-answer", "question": "Как называется метрика, показывающая долю правильных предсказаний?", "acceptedAnswers": ["accuracy", "Accuracy", "точность"]},
                ],
            },
            {
                "t": "Деревья решений",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Decision Tree — интуитивная модель", "markdown": "## Деревья решений\n\nДерево решений задаёт вопросы по признакам и делит данные.\n\n### Как работает:\n```\n                  Доход > 50K?\n                 /           \\\n              Да               Нет\n           /                      \\\n    Возраст > 30?           Отказ в кредите\n    /         \\\n  Да           Нет\nОдобрен    Проверка доп.\n```\n\n### Код:\n```python\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.tree import plot_tree\nimport matplotlib.pyplot as plt\n\nmodel = DecisionTreeClassifier(max_depth=3, random_state=42)\nmodel.fit(X_train, y_train)\n\n# Визуализация дерева\nplt.figure(figsize=(15, 8))\nplot_tree(model, feature_names=X.columns,\n          class_names=['Отказ', 'Одобрен'],\n          filled=True, rounded=True)\nplt.show()\n\n# Важность признаков\nfor name, imp in zip(X.columns, model.feature_importances_):\n    print(f'{name}: {imp:.3f}')\n```\n\n### Плюсы:\n- Легко интерпретировать\n- Работает с категориальными данными\n- Не требует масштабирования\n\n### Минусы:\n- Склонность к переобучению\n- Нестабильность (малые изменения → другое дерево)"},
                    {"type": "quiz", "question": "Какой параметр ограничивает глубину дерева решений?", "options": [{"id": "a", "text": "max_depth", "correct": True}, {"id": "b", "text": "n_estimators", "correct": False}, {"id": "c", "text": "learning_rate", "correct": False}, {"id": "d", "text": "kernel", "correct": False}]},
                    {"type": "multi-select", "question": "Какие преимущества деревьев решений?", "options": [{"id": "a", "text": "Легко интерпретировать", "correct": True}, {"id": "b", "text": "Работают с категориальными данными", "correct": True}, {"id": "c", "text": "Никогда не переобучаются", "correct": False}, {"id": "d", "text": "Не требуют масштабирования", "correct": True}]},
                    {"type": "true-false", "statement": "Деревья решений склонны к переобучению, особенно без ограничения глубины.", "correct": True},
                ],
            },
            {
                "t": "Метрики качества моделей",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Как оценить модель", "markdown": "## Метрики качества\n\n### Для классификации:\n\n**Accuracy** — доля правильных ответов:\n```python\nfrom sklearn.metrics import accuracy_score\naccuracy_score(y_test, y_pred)  # 0.85 = 85%\n```\n\n**Precision** — из всех предсказанных «да», сколько реально «да»:\n```python\nfrom sklearn.metrics import precision_score\nprecision_score(y_test, y_pred)  # 0.90\n```\n\n**Recall** — из всех реальных «да», сколько мы нашли:\n```python\nfrom sklearn.metrics import recall_score\nrecall_score(y_test, y_pred)  # 0.80\n```\n\n**F1-score** — среднее гармоническое Precision и Recall:\n```python\nfrom sklearn.metrics import f1_score\nf1_score(y_test, y_pred)  # 0.85\n```\n\n### Для регрессии:\n```python\nfrom sklearn.metrics import mean_squared_error, r2_score\n\nmse = mean_squared_error(y_test, y_pred)  # MSE\nrmse = mse ** 0.5                          # RMSE\nr2 = r2_score(y_test, y_pred)              # R²\n```\n\n### Confusion Matrix:\n```python\nfrom sklearn.metrics import confusion_matrix\nimport seaborn as sns\n\ncm = confusion_matrix(y_test, y_pred)\nsns.heatmap(cm, annot=True, fmt='d')\n```"},
                    {"type": "matching", "pairs": [{"left": "Accuracy", "right": "Доля правильных предсказаний"}, {"left": "Precision", "right": "Точность среди предсказанных положительных"}, {"left": "Recall", "right": "Полнота: сколько положительных нашли"}, {"left": "F1-score", "right": "Гармоническое среднее Precision и Recall"}]},
                    {"type": "quiz", "question": "При диагностике рака важнее не пропустить больного. Какая метрика приоритетна?", "options": [{"id": "a", "text": "Recall (полнота)", "correct": True}, {"id": "b", "text": "Precision (точность)", "correct": False}, {"id": "c", "text": "Accuracy", "correct": False}, {"id": "d", "text": "MSE", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Метрики классификации", "items": ["Accuracy", "Precision", "Recall", "F1-score"]}, {"name": "Метрики регрессии", "items": ["MSE", "RMSE", "R²"]}]},
                ],
            },
            {
                "t": "Переобучение (Overfitting)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Overfitting — главная проблема ML", "markdown": "## Переобучение (Overfitting)\n\nМодель **запоминает** обучающие данные вместо того, чтобы **обобщать**.\n\n### Признаки:\n- Высокий score на train → низкий на test\n- Модель слишком сложная для объёма данных\n\n### Пример:\n```python\nfrom sklearn.tree import DecisionTreeClassifier\n\n# Переобучение — неограниченное дерево\nmodel_overfit = DecisionTreeClassifier()  # max_depth=None\nmodel_overfit.fit(X_train, y_train)\nprint(f'Train: {model_overfit.score(X_train, y_train):.2f}')  # 1.00\nprint(f'Test:  {model_overfit.score(X_test, y_test):.2f}')    # 0.65\n\n# Хорошая модель — ограниченное дерево\nmodel_good = DecisionTreeClassifier(max_depth=3)\nmodel_good.fit(X_train, y_train)\nprint(f'Train: {model_good.score(X_train, y_train):.2f}')  # 0.88\nprint(f'Test:  {model_good.score(X_test, y_test):.2f}')    # 0.85\n```\n\n### Как бороться:\n1. **Больше данных** — лучшее лекарство\n2. **Упрощение модели** — меньше параметров\n3. **Регуляризация** — штраф за сложность\n4. **Cross-validation** — несколько разбиений\n5. **Early stopping** — остановка обучения вовремя\n\n### Cross-validation:\n```python\nfrom sklearn.model_selection import cross_val_score\n\nscores = cross_val_score(model, X, y, cv=5)\nprint(f'Mean: {scores.mean():.2f} ± {scores.std():.2f}')\n```"},
                    {"type": "quiz", "question": "Модель даёт 99% на train и 60% на test. Что происходит?", "options": [{"id": "a", "text": "Переобучение (overfitting)", "correct": True}, {"id": "b", "text": "Недообучение (underfitting)", "correct": False}, {"id": "c", "text": "Модель идеальна", "correct": False}, {"id": "d", "text": "Ошибка в данных", "correct": False}]},
                    {"type": "drag-order", "items": ["Обучить модель на train-данных", "Проверить score на train и test", "Обнаружить переобучение (train >> test)", "Применить регуляризацию или упростить модель", "Использовать cross-validation для оценки"]},
                    {"type": "multi-select", "question": "Какие методы помогают бороться с переобучением?", "options": [{"id": "a", "text": "Больше данных", "correct": True}, {"id": "b", "text": "Регуляризация", "correct": True}, {"id": "c", "text": "Cross-validation", "correct": True}, {"id": "d", "text": "Увеличить сложность модели", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 6: Продвинутый ML =====
    {
        "title": "Продвинутый ML",
        "pos": 5,
        "lessons": [
            {
                "t": "Random Forest",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Ансамбль деревьев", "markdown": "## Random Forest\n\nRandom Forest — **ансамбль** из множества деревьев решений.\n\n### Идея:\n- Обучить 100-500 деревьев на случайных подвыборках\n- Каждое дерево голосует за свой ответ\n- Финальный ответ — большинство голосов\n\n### Почему работает:\n> «Множество слабых моделей вместе → одна сильная модель»\n\n### Код:\n```python\nfrom sklearn.ensemble import RandomForestClassifier\n\nmodel = RandomForestClassifier(\n    n_estimators=100,    # количество деревьев\n    max_depth=10,        # макс глубина\n    random_state=42\n)\nmodel.fit(X_train, y_train)\n\nprint(f'Accuracy: {model.score(X_test, y_test):.2f}')\n\n# Важность признаков\nimport pandas as pd\nfeature_imp = pd.Series(\n    model.feature_importances_,\n    index=X.columns\n).sort_values(ascending=False)\nprint(feature_imp)\n```\n\n### Плюсы:\n- Лучше одиночного дерева\n- Меньше переобучения\n- Показывает важность признаков\n\n### Минусы:\n- Медленнее одиночного дерева\n- Менее интерпретируемый"},
                    {"type": "quiz", "question": "Сколько деревьев обычно в Random Forest?", "options": [{"id": "a", "text": "100-500", "correct": True}, {"id": "b", "text": "1-3", "correct": False}, {"id": "c", "text": "Ровно 10", "correct": False}, {"id": "d", "text": "Более 10000", "correct": False}]},
                    {"type": "true-false", "statement": "Random Forest менее подвержен переобучению, чем одиночное дерево решений.", "correct": True},
                    {"type": "fill-blank", "sentence": "Параметр n_estimators задаёт количество ___ в Random Forest.", "answer": "деревьев"},
                ],
            },
            {
                "t": "Gradient Boosting",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "XGBoost и LightGBM", "markdown": "## Gradient Boosting\n\nGradient Boosting — модели строятся **последовательно**, каждая исправляет ошибки предыдущей.\n\n### Отличие от Random Forest:\n- RF: деревья **параллельно**, голосование\n- GB: деревья **последовательно**, каждое учится на ошибках\n\n### XGBoost — чемпион Kaggle:\n```python\nfrom xgboost import XGBClassifier\n\nmodel = XGBClassifier(\n    n_estimators=200,\n    max_depth=6,\n    learning_rate=0.1,\n    random_state=42\n)\nmodel.fit(X_train, y_train)\nprint(f'Accuracy: {model.score(X_test, y_test):.2f}')\n```\n\n### LightGBM — быстрее XGBoost:\n```python\nfrom lightgbm import LGBMClassifier\n\nmodel = LGBMClassifier(\n    n_estimators=200,\n    max_depth=6,\n    learning_rate=0.1\n)\nmodel.fit(X_train, y_train)\n```\n\n### Когда что использовать:\n| Модель | Когда |\n|--------|-------|\n| Random Forest | Быстро, базовый вариант |\n| XGBoost | Соревнования, структурированные данные |\n| LightGBM | Большие датасеты, скорость |"},
                    {"type": "matching", "pairs": [{"left": "Random Forest", "right": "Деревья параллельно, голосование"}, {"left": "Gradient Boosting", "right": "Деревья последовательно, исправление ошибок"}, {"left": "XGBoost", "right": "Популярен на Kaggle, высокая точность"}, {"left": "LightGBM", "right": "Быстрый, для больших датасетов"}]},
                    {"type": "quiz", "question": "В чём главное отличие Gradient Boosting от Random Forest?", "options": [{"id": "a", "text": "Деревья строятся последовательно, каждое исправляет ошибки", "correct": True}, {"id": "b", "text": "Использует только одно дерево", "correct": False}, {"id": "c", "text": "Не использует деревья вообще", "correct": False}, {"id": "d", "text": "Работает только с текстовыми данными", "correct": False}]},
                    {"type": "type-answer", "question": "Какая библиотека gradient boosting часто побеждает на Kaggle?", "acceptedAnswers": ["XGBoost", "xgboost", "XGB"]},
                ],
            },
            {
                "t": "Кластеризация (K-Means)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Группировка без меток", "markdown": "## Кластеризация K-Means\n\nK-Means группирует данные в K кластеров без меток.\n\n### Алгоритм:\n1. Выбрать K случайных центроидов\n2. Каждую точку отнести к ближайшему центроиду\n3. Пересчитать центроиды (среднее кластера)\n4. Повторять шаги 2-3 до сходимости\n\n### Код:\n```python\nfrom sklearn.cluster import KMeans\nimport matplotlib.pyplot as plt\n\n# Сегментация клиентов\nmodel = KMeans(n_clusters=3, random_state=42)\nmodel.fit(X)\n\n# Метки кластеров\nlabels = model.labels_\ndf['cluster'] = labels\n\n# Визуализация\nplt.scatter(df['доход'], df['траты'],\n            c=labels, cmap='viridis')\nplt.xlabel('Доход')\nplt.ylabel('Траты')\nplt.title('Сегменты клиентов')\nplt.show()\n```\n\n### Метод локтя (Elbow Method):\n```python\ninertias = []\nfor k in range(1, 11):\n    model = KMeans(n_clusters=k, random_state=42)\n    model.fit(X)\n    inertias.append(model.inertia_)\n\nplt.plot(range(1, 11), inertias, marker='o')\nplt.xlabel('Количество кластеров')\nplt.ylabel('Inertia')\nplt.title('Метод локтя')\nplt.show()\n```"},
                    {"type": "drag-order", "items": ["Выбрать K случайных центроидов", "Отнести каждую точку к ближайшему центроиду", "Пересчитать центроиды как среднее кластера", "Повторять до сходимости"]},
                    {"type": "quiz", "question": "Как выбрать оптимальное количество кластеров?", "options": [{"id": "a", "text": "Метод локтя (Elbow Method)", "correct": True}, {"id": "b", "text": "Всегда выбирать K=2", "correct": False}, {"id": "c", "text": "K = количество строк в данных", "correct": False}, {"id": "d", "text": "Выбирать случайно", "correct": False}]},
                    {"type": "true-false", "statement": "K-Means — это алгоритм supervised learning, требующий метки.", "correct": False},
                ],
            },
            {
                "t": "PCA — снижение размерности",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Principal Component Analysis", "markdown": "## PCA — метод главных компонент\n\nPCA сокращает количество признаков, сохраняя максимум информации.\n\n### Зачем:\n- Данные с 100+ признаками тяжело анализировать\n- Убрать шум\n- Визуализация многомерных данных\n\n### Код:\n```python\nfrom sklearn.decomposition import PCA\nfrom sklearn.preprocessing import StandardScaler\nimport matplotlib.pyplot as plt\n\n# Важно! Масштабируем данные\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\n\n# PCA: 100 признаков → 2\npca = PCA(n_components=2)\nX_pca = pca.fit_transform(X_scaled)\n\n# Визуализация\nplt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')\nplt.xlabel('PC1')\nplt.ylabel('PC2')\nplt.title('PCA: 2D проекция данных')\nplt.show()\n\n# Объяснённая дисперсия\nprint(pca.explained_variance_ratio_)\n# [0.72, 0.18] → PC1 объясняет 72%, PC2 — 18%\n```\n\n### Правило:\nОставляем столько компонент, чтобы суммарная объяснённая дисперсия была ≥ 90-95%."},
                    {"type": "quiz", "question": "Перед PCA нужно обязательно:", "options": [{"id": "a", "text": "Масштабировать данные (StandardScaler)", "correct": True}, {"id": "b", "text": "Удалить все столбцы", "correct": False}, {"id": "c", "text": "Обучить Random Forest", "correct": False}, {"id": "d", "text": "Перевести в JSON", "correct": False}]},
                    {"type": "fill-blank", "sentence": "PCA расшифровывается как Principal ___ Analysis.", "answer": "Component"},
                    {"type": "true-false", "statement": "PCA может уменьшить 100 признаков до 2-3 главных компонент для визуализации.", "correct": True},
                ],
            },
            {
                "t": "Основы NLP",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Обработка естественного языка", "markdown": "## NLP — Natural Language Processing\n\n### Задачи NLP:\n- Анализ тональности (позитивный/негативный отзыв)\n- Классификация текстов (спам, тема)\n- Машинный перевод\n- Чат-боты и Q&A\n\n### Bag of Words:\n```python\nfrom sklearn.feature_extraction.text import CountVectorizer\n\ntexts = [\n    'отличный товар рекомендую',\n    'ужасное качество не рекомендую',\n    'хороший товар доволен'\n]\n\nvectorizer = CountVectorizer()\nX = vectorizer.fit_transform(texts)\nprint(vectorizer.get_feature_names_out())\n```\n\n### TF-IDF:\n```python\nfrom sklearn.feature_extraction.text import TfidfVectorizer\n\ntfidf = TfidfVectorizer()\nX = tfidf.fit_transform(texts)\n```\n\n### Анализ тональности:\n```python\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.linear_model import LogisticRegression\n\npipeline = Pipeline([\n    ('tfidf', TfidfVectorizer()),\n    ('clf', LogisticRegression())\n])\n\npipeline.fit(train_texts, train_labels)\npredictions = pipeline.predict(['замечательный продукт!'])\n```\n\n### Современные подходы:\n- **Transformers** (BERT, GPT)\n- **Hugging Face** — библиотека с предобученными моделями"},
                    {"type": "matching", "pairs": [{"left": "Bag of Words", "right": "Подсчёт частоты слов в документе"}, {"left": "TF-IDF", "right": "Учёт важности слова в коллекции"}, {"left": "Анализ тональности", "right": "Определение эмоции текста"}, {"left": "BERT", "right": "Предобученная transformer-модель"}]},
                    {"type": "quiz", "question": "Какой метод учитывает не только частоту слова, но и его редкость в коллекции?", "options": [{"id": "a", "text": "TF-IDF", "correct": True}, {"id": "b", "text": "Bag of Words", "correct": False}, {"id": "c", "text": "One-Hot Encoding", "correct": False}, {"id": "d", "text": "PCA", "correct": False}]},
                    {"type": "type-answer", "question": "Как расшифровывается NLP?", "acceptedAnswers": ["Natural Language Processing", "natural language processing"]},
                ],
            },
            {
                "t": "Нейросети — введение",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Нейронные сети — основы", "markdown": "## Нейронные сети\n\n### Что это:\nМатематическая модель, вдохновлённая мозгом — слои нейронов, передающих сигналы.\n\n### Структура:\n```\nВход → [Скрытый слой 1] → [Скрытый слой 2] → Выход\n  x₁ →    h₁, h₂, h₃    →    h₄, h₅       →   ŷ\n  x₂ →\n  x₃ →\n```\n\n### Простая нейросеть на PyTorch:\n```python\nimport torch\nimport torch.nn as nn\n\nclass SimpleNet(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.fc1 = nn.Linear(10, 64)   # вход: 10 признаков\n        self.fc2 = nn.Linear(64, 32)\n        self.fc3 = nn.Linear(32, 1)    # выход: 1 (регрессия)\n        self.relu = nn.ReLU()\n\n    def forward(self, x):\n        x = self.relu(self.fc1(x))\n        x = self.relu(self.fc2(x))\n        return self.fc3(x)\n\nmodel = SimpleNet()\n```\n\n### Когда использовать:\n| Задача | Нейросеть |\n|--------|----------|\n| Табличные данные | XGBoost лучше! |\n| Изображения | CNN (свёрточные) |\n| Текст | Transformer (BERT, GPT) |\n| Звук | RNN, Transformer |\n\n### Фреймворки:\n- **PyTorch** — гибкий, популярен в Research\n- **TensorFlow/Keras** — популярен в продакшне"},
                    {"type": "category-sort", "categories": [{"name": "Нейросети лучше", "items": ["Распознавание изображений", "Обработка текста", "Генерация музыки"]}, {"name": "Классический ML лучше", "items": ["Табличные данные", "Малый датасет", "Нужна интерпретируемость"]}]},
                    {"type": "matching", "pairs": [{"left": "PyTorch", "right": "Гибкий фреймворк, популярен в Research"}, {"left": "TensorFlow", "right": "Фреймворк Google, популярен в продакшне"}, {"left": "CNN", "right": "Свёрточные сети для изображений"}, {"left": "Transformer", "right": "Архитектура для текста (BERT, GPT)"}]},
                    {"type": "quiz", "question": "Для табличных данных обычно лучше работает:", "options": [{"id": "a", "text": "XGBoost / LightGBM", "correct": True}, {"id": "b", "text": "Глубокая нейросеть", "correct": False}, {"id": "c", "text": "CNN", "correct": False}, {"id": "d", "text": "Transformer", "correct": False}]},
                    {"type": "true-false", "statement": "Нейросети всегда лучше классического ML для любых задач.", "correct": False},
                ],
            },
        ],
    },
    # ===== SECTION 7: Проекты и карьера =====
    {
        "title": "Проекты и карьера",
        "pos": 6,
        "lessons": [
            {
                "t": "Kaggle — платформа соревнований",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Kaggle — школа Data Science", "markdown": "## Kaggle\n\n**Сайт:** [kaggle.com](https://kaggle.com)\n\n### Что есть на Kaggle:\n\n#### 1. Соревнования (Competitions)\n- Компании публикуют задачи с призами ($1000 — $1M)\n- Вы строите модель, загружаете предсказания\n- Лидерборд показывает вашу позицию\n\n#### 2. Датасеты (Datasets)\n- Тысячи бесплатных датасетов\n- Удобный поиск и превью\n\n#### 3. Notebooks\n- Jupyter-блокноты других участников\n- Отличный способ учиться\n\n#### 4. Курсы\n- Бесплатные курсы по ML, pandas, визуализации\n\n### С чего начать:\n1. Зарегистрируйтесь\n2. Пройдите курс «Intro to Machine Learning»\n3. Попробуйте Titanic Competition (для начинающих)\n4. Изучайте ноутбуки лидеров\n\n### Titanic — ваш первый проект:\n```python\nimport pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\ntrain = pd.read_csv('train.csv')\ntest = pd.read_csv('test.csv')\n\n# Простая модель\nfeatures = ['Pclass', 'Sex', 'Age', 'Fare']\ntrain['Sex'] = train['Sex'].map({'male': 0, 'female': 1})\ntrain['Age'].fillna(train['Age'].median(), inplace=True)\n\nmodel = RandomForestClassifier(n_estimators=100)\nmodel.fit(train[features], train['Survived'])\n```"},
                    {"type": "drag-order", "items": ["Зарегистрироваться на Kaggle", "Пройти бесплатный курс Intro to ML", "Участвовать в Titanic Competition", "Изучать ноутбуки лидеров", "Участвовать в реальных соревнованиях"]},
                    {"type": "quiz", "question": "Какое соревнование на Kaggle лучше для первого проекта?", "options": [{"id": "a", "text": "Titanic: Machine Learning from Disaster", "correct": True}, {"id": "b", "text": "Соревнование с призом $1M", "correct": False}, {"id": "c", "text": "Любое из топ-10", "correct": False}, {"id": "d", "text": "Kaggle не для начинающих", "correct": False}]},
                    {"type": "true-false", "statement": "На Kaggle есть бесплатные курсы и датасеты для обучения.", "correct": True},
                ],
            },
            {
                "t": "Портфолио Data Scientist",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Создаём портфолио", "markdown": "## Портфолио DS\n\nПортфолио важнее диплома! Покажите, что умеете.\n\n### Что включить (3-5 проектов):\n\n#### 1. EDA-проект (Exploratory Data Analysis)\n- Возьмите датасет с Kaggle\n- Очистите данные\n- Визуализируйте инсайты\n- Расскажите историю данных\n\n#### 2. ML-проект (предсказательная модель)\n- Предсказание цен, классификация\n- Показать метрики: accuracy, F1\n- Сравнить несколько моделей\n\n#### 3. NLP/CV-проект\n- Анализ тональности отзывов\n- Или классификация изображений\n\n#### 4. Дашборд\n- Streamlit или Plotly Dash\n- Интерактивная визуализация\n\n### Где публиковать:\n- **GitHub** — код с README\n- **Kaggle** — ноутбуки\n- **Medium / Habr** — статьи\n- **LinkedIn** — описание проектов\n\n### Структура проекта на GitHub:\n```\nproject/\n├── README.md          # Описание, результаты\n├── notebooks/\n│   └── analysis.ipynb # Jupyter ноутбук\n├── src/\n│   └── model.py       # Код модели\n├── data/\n│   └── README.md      # Описание данных\n└── requirements.txt\n```"},
                    {"type": "multi-select", "question": "Что стоит включить в портфолио DS?", "options": [{"id": "a", "text": "EDA-проект с визуализацией", "correct": True}, {"id": "b", "text": "ML-проект с метриками", "correct": True}, {"id": "c", "text": "Скриншоты из Excel", "correct": False}, {"id": "d", "text": "Дашборд на Streamlit", "correct": True}]},
                    {"type": "flashcards", "cards": [{"front": "EDA", "back": "Exploratory Data Analysis — исследовательский анализ данных"}, {"front": "README.md", "back": "Файл описания проекта на GitHub"}, {"front": "requirements.txt", "back": "Список Python-зависимостей проекта"}, {"front": "Habr", "back": "Русскоязычная платформа для технических статей"}]},
                    {"type": "quiz", "question": "Сколько проектов рекомендуется иметь в портфолио?", "options": [{"id": "a", "text": "3-5 качественных", "correct": True}, {"id": "b", "text": "50+ любых", "correct": False}, {"id": "c", "text": "Только 1 идеальный", "correct": False}, {"id": "d", "text": "Портфолио не нужно", "correct": False}]},
                ],
            },
            {
                "t": "SQL для Data Science",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "SQL — язык данных", "markdown": "## SQL для DS\n\nSQL — обязательный навык для любого Data Scientist.\n\n### Основные команды:\n```sql\n-- Выборка\nSELECT name, age, salary\nFROM employees\nWHERE department = 'Data Science'\nORDER BY salary DESC\nLIMIT 10;\n\n-- Агрегация\nSELECT department,\n       COUNT(*) as count,\n       AVG(salary) as avg_salary,\n       MAX(salary) as max_salary\nFROM employees\nGROUP BY department\nHAVING AVG(salary) > 100000;\n\n-- JOIN\nSELECT o.order_id, c.name, o.amount\nFROM orders o\nJOIN customers c ON o.customer_id = c.id\nWHERE o.amount > 5000;\n\n-- Подзапросы\nSELECT name, salary\nFROM employees\nWHERE salary > (\n    SELECT AVG(salary) FROM employees\n);\n\n-- Window функции\nSELECT name, department, salary,\n       RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank\nFROM employees;\n```\n\n### SQL в Python:\n```python\nimport pandas as pd\nimport sqlite3\n\nconn = sqlite3.connect('company.db')\ndf = pd.read_sql('SELECT * FROM employees', conn)\n```"},
                    {"type": "code-puzzle", "instructions": "Напишите SQL-запрос для средней зарплаты по отделам:", "correctOrder": ["SELECT department,", "       AVG(salary) as avg_salary", "FROM employees", "GROUP BY department", "ORDER BY avg_salary DESC;"]},
                    {"type": "quiz", "question": "Какой SQL-оператор используется для фильтрации после GROUP BY?", "options": [{"id": "a", "text": "HAVING", "correct": True}, {"id": "b", "text": "WHERE", "correct": False}, {"id": "c", "text": "FILTER", "correct": False}, {"id": "d", "text": "GROUP WHERE", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "WHERE", "right": "Фильтрация строк до группировки"}, {"left": "HAVING", "right": "Фильтрация после GROUP BY"}, {"left": "JOIN", "right": "Объединение таблиц"}, {"left": "RANK() OVER", "right": "Оконная функция для ранжирования"}]},
                ],
            },
            {
                "t": "ETL и пайплайны данных",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "ETL — обработка данных", "markdown": "## ETL: Extract, Transform, Load\n\n### Extract (Извлечение):\nДанные из разных источников:\n- Базы данных (PostgreSQL, MySQL)\n- API (REST, GraphQL)\n- Файлы (CSV, JSON, Excel)\n- Веб-скрапинг\n\n### Transform (Преобразование):\n```python\nimport pandas as pd\n\n# Загрузка\ndf = pd.read_csv('raw_data.csv')\n\n# Очистка\ndf.dropna(subset=['email'], inplace=True)\ndf['дата'] = pd.to_datetime(df['дата'])\ndf['город'] = df['город'].str.strip().str.title()\n\n# Обогащение\ndf['год'] = df['дата'].dt.year\ndf['месяц'] = df['дата'].dt.month\n\n# Агрегация\nmonthly = df.groupby(['год', 'месяц']).agg(\n    продажи=('сумма', 'sum'),\n    клиенты=('client_id', 'nunique')\n).reset_index()\n```\n\n### Load (Загрузка):\n```python\n# В базу данных\nfrom sqlalchemy import create_engine\nengine = create_engine('postgresql://user:pass@localhost/db')\nmonthly.to_sql('monthly_sales', engine, if_exists='replace')\n\n# В файл\nmonthly.to_csv('monthly_sales.csv', index=False)\n```\n\n### Инструменты:\n- **Apache Airflow** — оркестрация пайплайнов\n- **dbt** — трансформация SQL\n- **Prefect** — современная альтернатива Airflow"},
                    {"type": "drag-order", "items": ["Extract: загрузить данные из источников", "Transform: очистить и преобразовать", "Transform: обогатить и агрегировать", "Load: сохранить в базу данных/хранилище"]},
                    {"type": "matching", "pairs": [{"left": "Extract", "right": "Извлечение данных из источников"}, {"left": "Transform", "right": "Очистка, преобразование, агрегация"}, {"left": "Load", "right": "Загрузка в целевое хранилище"}, {"left": "Apache Airflow", "right": "Оркестрация ETL-пайплайнов"}]},
                    {"type": "fill-blank", "sentence": "ETL расшифровывается как Extract, Transform, ___.", "answer": "Load"},
                ],
            },
            {
                "t": "Собеседование Data Scientist",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Как пройти собеседование DS", "markdown": "## Собеседование Data Scientist\n\n### Типичные этапы:\n1. **Скрининг HR** — мотивация, опыт\n2. **SQL-задачи** — запросы, оконные функции\n3. **Статистика** — гипотезы, A/B-тесты\n4. **ML** — алгоритмы, метрики, feature engineering\n5. **Кейс** — бизнес-задача с данными\n6. **Код** — Python, pandas\n\n### Топ вопросов:\n\n**Статистика:**\n- Разница между Type I и Type II ошибками?\n- Когда использовать медиану вместо среднего?\n- Как проверить нормальность распределения?\n\n**ML:**\n- Разница между bagging и boosting?\n- Как бороться с переобучением?\n- Объясните bias-variance tradeoff\n\n**Кейс:**\n- Как построить рекомендательную систему?\n- Метрика конверсии упала на 5% — что делать?\n- Как определить мошеннические транзакции?\n\n### Подготовка:\n- **LeetCode** — SQL и Python задачи\n- **Kaggle** — реальные проекты\n- **Книга:** «Cracking the Data Science Interview»\n- **Практика:** mock-интервью с друзьями"},
                    {"type": "flashcards", "cards": [{"front": "Bias-Variance Tradeoff", "back": "Баланс между ошибкой из-за упрощения (bias) и ошибкой из-за чувствительности к данным (variance)"}, {"front": "Bagging", "back": "Параллельное обучение моделей на подвыборках (Random Forest)"}, {"front": "Boosting", "back": "Последовательное обучение, каждая модель исправляет ошибки предыдущей (XGBoost)"}, {"front": "Feature Engineering", "back": "Создание новых признаков из существующих данных"}]},
                    {"type": "quiz", "question": "Что лучше всего подготовит к собеседованию DS?", "options": [{"id": "a", "text": "Реальные проекты + практика задач", "correct": True}, {"id": "b", "text": "Только чтение книг", "correct": False}, {"id": "c", "text": "Просмотр видео без практики", "correct": False}, {"id": "d", "text": "Изучение только теории", "correct": False}]},
                    {"type": "multi-select", "question": "Какие темы часто спрашивают на собеседовании DS?", "options": [{"id": "a", "text": "SQL-запросы", "correct": True}, {"id": "b", "text": "A/B-тестирование", "correct": True}, {"id": "c", "text": "Вёрстка HTML", "correct": False}, {"id": "d", "text": "Bias-Variance Tradeoff", "correct": True}]},
                ],
            },
            {
                "t": "Итоговый проект: анализ данных",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Собираем всё вместе", "markdown": "## Итоговый проект\n\nПостройте полный проект Data Science от начала до конца.\n\n### Задание: Анализ и предсказание\n\n#### Шаг 1: Данные\nСкачайте датасет с Kaggle (рекомендации):\n- House Prices\n- Titanic\n- Customer Churn\n\n#### Шаг 2: EDA\n```python\nimport pandas as pd\nimport seaborn as sns\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv('data.csv')\nprint(df.shape)\nprint(df.describe())\nprint(df.isnull().sum())\n\nsns.heatmap(df.corr(), annot=True)\nplt.show()\n```\n\n#### Шаг 3: Очистка и Feature Engineering\n```python\ndf.fillna(df.median(), inplace=True)\ndf = pd.get_dummies(df, drop_first=True)\n```\n\n#### Шаг 4: Моделирование\n```python\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.ensemble import RandomForestClassifier\nfrom xgboost import XGBClassifier\n\nmodels = {\n    'RF': RandomForestClassifier(n_estimators=100),\n    'XGB': XGBClassifier(n_estimators=200)\n}\n\nfor name, model in models.items():\n    scores = cross_val_score(model, X, y, cv=5, scoring='f1')\n    print(f'{name}: F1 = {scores.mean():.3f} ± {scores.std():.3f}')\n```\n\n#### Шаг 5: Презентация\n- README.md с описанием\n- Jupyter Notebook с визуализациями\n- Выводы и рекомендации\n\nПоздравляем! Вы прошли курс Data Science!"},
                    {"type": "drag-order", "items": ["Скачать и загрузить датасет", "Провести EDA и визуализацию", "Очистить данные и создать признаки", "Обучить и сравнить модели", "Оформить и презентовать результат"]},
                    {"type": "quiz", "question": "Какой этап занимает больше всего времени в DS-проекте?", "options": [{"id": "a", "text": "Очистка и подготовка данных", "correct": True}, {"id": "b", "text": "Обучение модели", "correct": False}, {"id": "c", "text": "Выбор алгоритма", "correct": False}, {"id": "d", "text": "Презентация", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "EDA", "back": "Исследовательский анализ — describe(), визуализации, поиск паттернов"}, {"front": "Feature Engineering", "back": "Создание новых признаков: get_dummies(), трансформации"}, {"front": "Cross-Validation", "back": "Оценка модели на нескольких разбиениях (cv=5)"}, {"front": "F1-score", "back": "Гармоническое среднее Precision и Recall — балансированная метрика"}]},
                    {"type": "true-false", "statement": "В реальных проектах Data Science важно не только построить модель, но и презентовать результаты.", "correct": True},
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
            slug="data-science-analytics-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Data Science",
            difficulty="Intermediate",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()
        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(
                course_id=course.id, title=sd["title"], position=sd["pos"]
            )
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
