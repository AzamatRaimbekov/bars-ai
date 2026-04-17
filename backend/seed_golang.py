"""Seed: Golang для разработчиков — 7 sections, ~40 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Golang для разработчиков"
DESC = (
    "Курс по Go: от синтаксиса до микросервисов. Горутины, каналы, интерфейсы, "
    "REST API, gRPC, тестирование, Docker, production-ready код."
)

S = [
    # ==================== SECTION 1: Введение в Go ====================
    {
        "title": "Введение в Go",
        "pos": 0,
        "lessons": [
            {
                "t": "Зачем изучать Go?",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Почему Go?", "markdown": "## Зачем изучать Go?\n\n**Go (Golang)** — язык программирования, созданный в **Google** в 2009 году инженерами **Робертом Грисемером, Робом Пайком и Кеном Томпсоном**.\n\n### Преимущества Go:\n- **Простой синтаксис** — легко читать и писать\n- **Быстрая компиляция** — программы компилируются за секунды\n- **Встроенная конкурентность** — горутины и каналы из коробки\n- **Статическая типизация** — ошибки ловятся на этапе компиляции\n- **Единый бинарник** — нет зависимостей при деплое\n\n### Где используется Go?\n- **Docker** — контейнеризация\n- **Kubernetes** — оркестрация контейнеров\n- **Uber** — высоконагруженные микросервисы\n- **Twitch** — стриминговая платформа\n- **Cloudflare** — CDN и безопасность\n\n### Go идеален для:\n- Микросервисов и API\n- CLI-утилит\n- Облачной инфраструктуры\n- Высоконагруженных систем"},
                    {"type": "quiz", "question": "Кто создал язык Go?", "options": [{"id": "a", "text": "Линус Торвальдс", "correct": False}, {"id": "b", "text": "Инженеры Google (Пайк, Томпсон, Грисемер)", "correct": True}, {"id": "c", "text": "Гвидо ван Россум", "correct": False}, {"id": "d", "text": "Брендан Эйх", "correct": False}]},
                    {"type": "true-false", "statement": "Go — интерпретируемый язык программирования.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "Docker", "right": "Контейнеризация"}, {"left": "Kubernetes", "right": "Оркестрация"}, {"left": "Uber", "right": "Микросервисы"}, {"left": "Cloudflare", "right": "CDN и безопасность"}]},
                ],
            },
            {
                "t": "Установка Go",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Установка Go на компьютер", "markdown": "## Установка Go\n\n### Windows:\n1. Скачайте установщик с [go.dev/dl](https://go.dev/dl)\n2. Запустите `.msi` файл\n3. Следуйте инструкциям установщика\n4. Проверьте: `go version`\n\n### macOS:\n```bash\nbrew install go\n```\n\n### Linux:\n```bash\nwget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz\nsudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz\nexport PATH=$PATH:/usr/local/go/bin\n```\n\n### Проверка установки:\n```bash\ngo version\n# go version go1.22.0 linux/amd64\n```\n\n### Переменные окружения:\n- `GOPATH` — рабочая директория Go\n- `GOROOT` — директория установки Go\n- `GOBIN` — директория для бинарников\n\n### Редакторы:\n- **VS Code** + расширение Go\n- **GoLand** (JetBrains)\n- **Vim/Neovim** + gopls"},
                    {"type": "drag-order", "items": ["Скачать Go с go.dev/dl", "Запустить установщик", "Настроить переменные окружения", "Проверить: go version", "Установить расширение Go для VS Code"]},
                    {"type": "quiz", "question": "Какой командой проверить установку Go?", "options": [{"id": "a", "text": "go --version", "correct": False}, {"id": "b", "text": "go version", "correct": True}, {"id": "c", "text": "golang -v", "correct": False}, {"id": "d", "text": "which go", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "GOPATH", "back": "Рабочая директория Go (по умолчанию ~/go)"}, {"front": "GOROOT", "back": "Директория установки Go"}, {"front": "GOBIN", "back": "Директория для скомпилированных бинарников"}]},
                ],
            },
            {
                "t": "Hello World на Go",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Первая программа на Go", "markdown": "## Hello, World!\n\n### Создайте файл `main.go`:\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}\n```\n\n### Запуск:\n```bash\ngo run main.go\n```\n\n### Разбор:\n- `package main` — объявление пакета; `main` — точка входа\n- `import \"fmt\"` — импорт пакета форматированного ввода/вывода\n- `func main()` — главная функция, запускается при старте\n- `fmt.Println()` — вывод строки с переносом\n\n### Компиляция:\n```bash\ngo build -o myapp main.go\n./myapp\n```\n\n### go mod init:\n```bash\ngo mod init myproject\n```\nСоздаёт файл `go.mod` для управления зависимостями."},
                    {"type": "code-puzzle", "instructions": "Соберите программу Hello World на Go", "correctOrder": ["package main", "import \"fmt\"", "func main() {", "    fmt.Println(\"Hello, World!\")", "}"]},
                    {"type": "fill-blank", "sentence": "Точка входа в Go-программу — функция ___ в пакете main.", "answer": "main"},
                    {"type": "quiz", "question": "Какой пакет используется для вывода текста в Go?", "options": [{"id": "a", "text": "io", "correct": False}, {"id": "b", "text": "fmt", "correct": True}, {"id": "c", "text": "os", "correct": False}, {"id": "d", "text": "log", "correct": False}]},
                    {"type": "type-answer", "question": "Какой командой запустить Go-файл без компиляции?", "acceptedAnswers": ["go run main.go", "go run"]},
                ],
            },
            {
                "t": "Типы данных в Go",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Основные типы данных", "markdown": "## Типы данных Go\n\n### Целые числа:\n```go\nvar a int = 42\nvar b int8 = 127       // -128 до 127\nvar c int16 = 32767\nvar d int32 = 2147483647\nvar e int64 = 9223372036854775807\n```\n\n### Беззнаковые целые:\n```go\nvar u uint = 42\nvar u8 uint8 = 255     // 0 до 255 (byte)\n```\n\n### Дробные числа:\n```go\nvar f float32 = 3.14\nvar g float64 = 3.141592653589793\n```\n\n### Строки и символы:\n```go\nvar s string = \"Привет, Go!\"\nvar r rune = 'A'       // int32, символ Unicode\nvar b byte = 'Z'       // uint8\n```\n\n### Логический тип:\n```go\nvar isReady bool = true\nvar isEmpty bool = false\n```\n\n### Нулевые значения (zero values):\n- `int` → `0`\n- `float64` → `0.0`\n- `string` → `\"\"`\n- `bool` → `false`"},
                    {"type": "matching", "pairs": [{"left": "int", "right": "0"}, {"left": "string", "right": "\"\" (пустая строка)"}, {"left": "bool", "right": "false"}, {"left": "float64", "right": "0.0"}]},
                    {"type": "multi-select", "question": "Какие из этих типов есть в Go?", "options": [{"id": "a", "text": "int64", "correct": True}, {"id": "b", "text": "rune", "correct": True}, {"id": "c", "text": "char", "correct": False}, {"id": "d", "text": "byte", "correct": True}, {"id": "e", "text": "double", "correct": False}]},
                    {"type": "true-false", "statement": "Нулевое значение типа bool в Go — true.", "correct": False},
                    {"type": "fill-blank", "sentence": "Тип ___ в Go — это псевдоним для int32 и представляет символ Unicode.", "answer": "rune"},
                ],
            },
            {
                "t": "Переменные и константы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Объявление переменных", "markdown": "## Переменные в Go\n\n### Полное объявление:\n```go\nvar name string = \"Алексей\"\nvar age int = 30\n```\n\n### Вывод типа (type inference):\n```go\nvar name = \"Алексей\"   // Go определит тип сам\n```\n\n### Короткое объявление (:=):\n```go\nname := \"Алексей\"      // только внутри функций\nage := 30\n```\n\n### Множественное объявление:\n```go\nvar (\n    name   = \"Go\"\n    version = 1.22\n    stable  = true\n)\n```\n\n### Константы:\n```go\nconst Pi = 3.14159\nconst (\n    StatusOK    = 200\n    StatusError = 500\n)\n```\n\n### iota — автоинкремент для констант:\n```go\nconst (\n    Red   = iota  // 0\n    Green         // 1\n    Blue          // 2\n)\n```\n\n### Важно:\n- Неиспользуемые переменные — **ошибка компиляции**\n- Константы нельзя объявить через `:=`"},
                    {"type": "quiz", "question": "Как объявить переменную коротким способом внутри функции?", "options": [{"id": "a", "text": "var x = 5", "correct": False}, {"id": "b", "text": "x := 5", "correct": True}, {"id": "c", "text": "let x = 5", "correct": False}, {"id": "d", "text": "x = 5", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Объявите константу Pi и выведите её", "correctOrder": ["package main", "import \"fmt\"", "const Pi = 3.14159", "func main() {", "    fmt.Println(Pi)", "}"]},
                    {"type": "true-false", "statement": "В Go неиспользуемые переменные вызывают ошибку компиляции.", "correct": True},
                    {"type": "type-answer", "question": "Какое ключевое слово используется для автоинкремента констант в Go?", "acceptedAnswers": ["iota"]},
                ],
            },
            {
                "t": "Пакет fmt и форматирование",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Форматированный вывод", "markdown": "## Пакет fmt\n\n### Основные функции вывода:\n```go\nfmt.Print(\"без переноса\")\nfmt.Println(\"с переносом строки\")\nfmt.Printf(\"форматированный: %s\\n\", \"текст\")\n```\n\n### Глаголы форматирования (verbs):\n```go\nname := \"Go\"\nver := 1.22\n\nfmt.Printf(\"Язык: %s\\n\", name)    // строка\nfmt.Printf(\"Версия: %f\\n\", ver)   // float\nfmt.Printf(\"Версия: %.1f\\n\", ver) // 1.2 — 1 знак\nfmt.Printf(\"Тип: %T\\n\", name)     // string\nfmt.Printf(\"Значение: %v\\n\", ver) // любое значение\nfmt.Printf(\"Число: %d\\n\", 42)     // целое\nfmt.Printf(\"Булево: %t\\n\", true)  // bool\n```\n\n### Sprintf — возвращает строку:\n```go\ns := fmt.Sprintf(\"Привет, %s!\", \"мир\")\n```\n\n### Ввод данных:\n```go\nvar name string\nfmt.Print(\"Имя: \")\nfmt.Scan(&name)\nfmt.Println(\"Привет,\", name)\n```\n\n### Errorf — форматированная ошибка:\n```go\nerr := fmt.Errorf(\"файл %s не найден\", filename)\n```"},
                    {"type": "matching", "pairs": [{"left": "%s", "right": "Строка"}, {"left": "%d", "right": "Целое число"}, {"left": "%f", "right": "Дробное число"}, {"left": "%T", "right": "Тип значения"}, {"left": "%v", "right": "Любое значение"}]},
                    {"type": "fill-blank", "sentence": "Функция fmt.___ возвращает форматированную строку, а не выводит её.", "answer": "Sprintf"},
                    {"type": "quiz", "question": "Какой глагол форматирования выводит тип переменной?", "options": [{"id": "a", "text": "%v", "correct": False}, {"id": "b", "text": "%s", "correct": False}, {"id": "c", "text": "%T", "correct": True}, {"id": "d", "text": "%t", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Выведите имя и возраст с помощью Printf", "correctOrder": ["name := \"Анна\"", "age := 25", "fmt.Printf(\"%s, %d лет\\n\", name, age)"]},
                ],
            },
        ],
    },
    # ==================== SECTION 2: Управляющие конструкции ====================
    {
        "title": "Управляющие конструкции",
        "pos": 1,
        "lessons": [
            {
                "t": "Условия: if / else",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Условные конструкции", "markdown": "## if / else в Go\n\n### Базовый синтаксис:\n```go\nage := 18\nif age >= 18 {\n    fmt.Println(\"Совершеннолетний\")\n} else {\n    fmt.Println(\"Несовершеннолетний\")\n}\n```\n\n### if / else if / else:\n```go\nscore := 85\nif score >= 90 {\n    fmt.Println(\"Отлично\")\n} else if score >= 70 {\n    fmt.Println(\"Хорошо\")\n} else {\n    fmt.Println(\"Нужно подтянуть\")\n}\n```\n\n### if с инициализацией (уникальная фича Go):\n```go\nif num := 42; num > 0 {\n    fmt.Println(\"Положительное:\", num)\n}\n// num здесь уже не доступен!\n```\n\n### Важные отличия от других языков:\n- **Скобки `()` вокруг условия не нужны**\n- **Фигурные скобки `{}` обязательны** даже для одной строки\n- Открывающая `{` должна быть на той же строке, что и `if`"},
                    {"type": "quiz", "question": "Нужны ли круглые скобки вокруг условия в Go?", "options": [{"id": "a", "text": "Да, обязательно", "correct": False}, {"id": "b", "text": "Нет, не нужны", "correct": True}, {"id": "c", "text": "Только для сложных условий", "correct": False}, {"id": "d", "text": "Зависит от компилятора", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите if с инициализацией переменной", "correctOrder": ["if x := 10; x > 5 {", "    fmt.Println(\"больше пяти\")", "}"]},
                    {"type": "true-false", "statement": "В Go фигурные скобки в if/else обязательны даже для одной строки.", "correct": True},
                    {"type": "fill-blank", "sentence": "В Go if может содержать ___ перед условием, разделённую точкой с запятой.", "answer": "инициализацию"},
                ],
            },
            {
                "t": "Оператор switch",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "switch в Go", "markdown": "## switch\n\n### Базовый switch:\n```go\nday := \"понедельник\"\nswitch day {\ncase \"понедельник\":\n    fmt.Println(\"Начало недели\")\ncase \"пятница\":\n    fmt.Println(\"Конец рабочей недели\")\ncase \"суббота\", \"воскресенье\":\n    fmt.Println(\"Выходной\")\ndefault:\n    fmt.Println(\"Рабочий день\")\n}\n```\n\n### Важно: в Go нет fallthrough по умолчанию!\nКаждый case автоматически завершается break.\n\n### switch без выражения (замена if/else):\n```go\nscore := 85\nswitch {\ncase score >= 90:\n    fmt.Println(\"A\")\ncase score >= 80:\n    fmt.Println(\"B\")\ncase score >= 70:\n    fmt.Println(\"C\")\ndefault:\n    fmt.Println(\"F\")\n}\n```\n\n### switch по типу (type switch):\n```go\nvar i interface{} = \"hello\"\nswitch v := i.(type) {\ncase string:\n    fmt.Println(\"Строка:\", v)\ncase int:\n    fmt.Println(\"Число:\", v)\n}\n```\n\n### fallthrough — явный переход:\n```go\nswitch 1 {\ncase 1:\n    fmt.Println(\"один\")\n    fallthrough\ncase 2:\n    fmt.Println(\"два\")\n}\n// Выведет: один два\n```"},
                    {"type": "true-false", "statement": "В Go switch по умолчанию имеет fallthrough (проваливание) как в C/Java.", "correct": False},
                    {"type": "quiz", "question": "Как в switch указать несколько значений для одного case?", "options": [{"id": "a", "text": "case 1 || 2:", "correct": False}, {"id": "b", "text": "case 1, 2:", "correct": True}, {"id": "c", "text": "case 1 | 2:", "correct": False}, {"id": "d", "text": "case [1, 2]:", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "switch без выражения", "back": "Замена цепочки if/else if — условия проверяются в каждом case"}, {"front": "type switch", "back": "switch v := i.(type) — проверка типа интерфейса"}, {"front": "fallthrough", "back": "Явный переход к следующему case (не по умолчанию в Go)"}]},
                    {"type": "fill-blank", "sentence": "Ключевое слово ___ явно переходит к следующему case в Go switch.", "answer": "fallthrough"},
                ],
            },
            {
                "t": "Цикл for",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Единственный цикл в Go", "markdown": "## Цикл for\n\nВ Go **for — единственный цикл**. Нет while или do-while.\n\n### Классический for:\n```go\nfor i := 0; i < 5; i++ {\n    fmt.Println(i)\n}\n```\n\n### for как while:\n```go\nn := 1\nfor n < 100 {\n    n *= 2\n}\n```\n\n### Бесконечный цикл:\n```go\nfor {\n    fmt.Println(\"бесконечно\")\n    break // выход из цикла\n}\n```\n\n### break и continue:\n```go\nfor i := 0; i < 10; i++ {\n    if i == 3 {\n        continue // пропустить итерацию\n    }\n    if i == 7 {\n        break // выйти из цикла\n    }\n    fmt.Println(i)\n}\n```\n\n### Метки (labels) для вложенных циклов:\n```go\nouter:\nfor i := 0; i < 3; i++ {\n    for j := 0; j < 3; j++ {\n        if i == 1 && j == 1 {\n            break outer\n        }\n    }\n}\n```"},
                    {"type": "true-false", "statement": "В Go есть цикл while.", "correct": False},
                    {"type": "code-puzzle", "instructions": "Напишите бесконечный цикл с выходом по break", "correctOrder": ["for {", "    fmt.Println(\"работает\")", "    break", "}"]},
                    {"type": "quiz", "question": "Как написать аналог while(n < 100) в Go?", "options": [{"id": "a", "text": "while n < 100 {}", "correct": False}, {"id": "b", "text": "for n < 100 {}", "correct": True}, {"id": "c", "text": "loop n < 100 {}", "correct": False}, {"id": "d", "text": "do { } while n < 100", "correct": False}]},
                    {"type": "multi-select", "question": "Какие формы цикла for доступны в Go?", "options": [{"id": "a", "text": "Классический (init; cond; post)", "correct": True}, {"id": "b", "text": "Как while (только условие)", "correct": True}, {"id": "c", "text": "Бесконечный (без условия)", "correct": True}, {"id": "d", "text": "do-while", "correct": False}, {"id": "e", "text": "for-range", "correct": True}]},
                ],
            },
            {
                "t": "range — перебор коллекций",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "for range", "markdown": "## for range\n\n`range` — итерация по слайсам, массивам, строкам, картам и каналам.\n\n### Перебор слайса:\n```go\nnums := []int{10, 20, 30}\nfor i, v := range nums {\n    fmt.Printf(\"index=%d value=%d\\n\", i, v)\n}\n```\n\n### Только значения (индекс не нужен):\n```go\nfor _, v := range nums {\n    fmt.Println(v)\n}\n```\n\n### Только индексы:\n```go\nfor i := range nums {\n    fmt.Println(i)\n}\n```\n\n### Перебор строки (по рунам):\n```go\nfor i, ch := range \"Привет\" {\n    fmt.Printf(\"%d: %c\\n\", i, ch)\n}\n```\n\n### Перебор map:\n```go\nm := map[string]int{\"a\": 1, \"b\": 2}\nfor key, val := range m {\n    fmt.Printf(\"%s=%d\\n\", key, val)\n}\n```\n\n### Важно:\n- Порядок обхода map **не гарантирован**\n- `_` (blank identifier) — игнорировать значение"},
                    {"type": "quiz", "question": "Как игнорировать индекс при переборе слайса через range?", "options": [{"id": "a", "text": "for v := range nums", "correct": False}, {"id": "b", "text": "for _, v := range nums", "correct": True}, {"id": "c", "text": "for v, _ := range nums", "correct": False}, {"id": "d", "text": "for range nums into v", "correct": False}]},
                    {"type": "true-false", "statement": "Порядок обхода map через range в Go всегда одинаковый.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "for i, v := range slice", "right": "Индекс и значение"}, {"left": "for _, v := range slice", "right": "Только значение"}, {"left": "for i := range slice", "right": "Только индекс"}, {"left": "for k, v := range m", "right": "Ключ и значение map"}]},
                    {"type": "fill-blank", "sentence": "Символ ___ в Go используется как blank identifier для игнорирования значения.", "answer": "_"},
                ],
            },
            {
                "t": "defer, panic и recover",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "defer, panic, recover", "markdown": "## defer\n\nОткладывает выполнение функции до выхода из текущей функции.\n\n```go\nfunc main() {\n    defer fmt.Println(\"мир\")  // выполнится последним\n    fmt.Println(\"привет\")\n}\n// привет\n// мир\n```\n\n### defer — стек (LIFO):\n```go\nfor i := 0; i < 3; i++ {\n    defer fmt.Println(i)\n}\n// 2, 1, 0\n```\n\n### Типичное использование:\n```go\nf, err := os.Open(\"file.txt\")\nif err != nil {\n    log.Fatal(err)\n}\ndefer f.Close()  // гарантированное закрытие\n```\n\n## panic\n\nАварийная остановка программы:\n```go\npanic(\"что-то пошло не так\")\n```\n\n## recover\n\nПерехват panic (только внутри defer):\n```go\nfunc safeDiv(a, b int) (result int) {\n    defer func() {\n        if r := recover(); r != nil {\n            fmt.Println(\"Перехвачена паника:\", r)\n            result = 0\n        }\n    }()\n    return a / b\n}\n```\n\n### Правила:\n- `defer` — для очистки ресурсов\n- `panic` — только для неисправимых ошибок\n- `recover` — только внутри defer-функции"},
                    {"type": "drag-order", "items": ["defer добавляет функцию в стек", "Основная функция выполняется", "При выходе defer-функции вызываются в порядке LIFO", "Если произошла panic — defer всё равно выполнится", "recover внутри defer может перехватить panic"]},
                    {"type": "quiz", "question": "В каком порядке выполняются defer-вызовы?", "options": [{"id": "a", "text": "FIFO (первый добавленный — первый выполненный)", "correct": False}, {"id": "b", "text": "LIFO (последний добавленный — первый выполненный)", "correct": True}, {"id": "c", "text": "Случайный порядок", "correct": False}, {"id": "d", "text": "Параллельно", "correct": False}]},
                    {"type": "true-false", "statement": "recover может перехватить panic только внутри defer-функции.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "defer", "back": "Откладывает выполнение функции до выхода из текущей функции (LIFO)"}, {"front": "panic", "back": "Аварийная остановка программы (только для неисправимых ошибок)"}, {"front": "recover", "back": "Перехватывает panic; работает только внутри defer"}]},
                ],
            },
        ],
    },
    # ==================== SECTION 3: Функции и структуры ====================
    {
        "title": "Функции и структуры",
        "pos": 2,
        "lessons": [
            {
                "t": "Функции в Go",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Объявление функций", "markdown": "## Функции\n\n### Базовая функция:\n```go\nfunc greet(name string) {\n    fmt.Println(\"Привет,\", name)\n}\n```\n\n### Функция с возвратом:\n```go\nfunc add(a, b int) int {\n    return a + b\n}\n```\n\n### Параметры одного типа:\n```go\nfunc multiply(a, b int) int {  // оба int\n    return a * b\n}\n```\n\n### Вариативные функции (variadic):\n```go\nfunc sum(nums ...int) int {\n    total := 0\n    for _, n := range nums {\n        total += n\n    }\n    return total\n}\n// sum(1, 2, 3) → 6\n```\n\n### Функции — значения первого класса:\n```go\nadd := func(a, b int) int {\n    return a + b\n}\nfmt.Println(add(3, 4))  // 7\n```\n\n### Функция как параметр:\n```go\nfunc apply(fn func(int, int) int, a, b int) int {\n    return fn(a, b)\n}\n```"},
                    {"type": "quiz", "question": "Как объявить вариативную функцию в Go?", "options": [{"id": "a", "text": "func f(args []int)", "correct": False}, {"id": "b", "text": "func f(args ...int)", "correct": True}, {"id": "c", "text": "func f(*args int)", "correct": False}, {"id": "d", "text": "func f(args int...)", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите функцию сложения двух чисел", "correctOrder": ["func add(a, b int) int {", "    return a + b", "}"]},
                    {"type": "true-false", "statement": "В Go функции являются значениями первого класса и могут быть присвоены переменным.", "correct": True},
                    {"type": "fill-blank", "sentence": "Оператор ___ перед типом параметра делает функцию вариативной.", "answer": "..."},
                ],
            },
            {
                "t": "Множественный возврат",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Несколько возвращаемых значений", "markdown": "## Множественный возврат\n\nGo позволяет возвращать несколько значений из функции.\n\n### Базовый пример:\n```go\nfunc divide(a, b float64) (float64, error) {\n    if b == 0 {\n        return 0, fmt.Errorf(\"деление на ноль\")\n    }\n    return a / b, nil\n}\n\nresult, err := divide(10, 3)\nif err != nil {\n    log.Fatal(err)\n}\nfmt.Println(result)\n```\n\n### Именованные возвращаемые значения:\n```go\nfunc rect(w, h float64) (area, perimeter float64) {\n    area = w * h\n    perimeter = 2 * (w + h)\n    return  // naked return\n}\n```\n\n### Паттерн (value, error):\nЭто **идиоматический** Go — вместо исключений:\n```go\nf, err := os.Open(\"file.txt\")\nif err != nil {\n    // обработка ошибки\n}\n// работа с f\n```\n\n### Игнорирование значения:\n```go\nresult, _ := divide(10, 3)  // ошибку игнорируем\n```"},
                    {"type": "quiz", "question": "Какой паттерн обработки ошибок идиоматичен для Go?", "options": [{"id": "a", "text": "try/catch", "correct": False}, {"id": "b", "text": "(value, error)", "correct": True}, {"id": "c", "text": "throw/catch", "correct": False}, {"id": "d", "text": "Result<T, E>", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Напишите вызов функции с обработкой ошибки", "correctOrder": ["result, err := divide(10, 0)", "if err != nil {", "    fmt.Println(\"Ошибка:\", err)", "    return", "}", "fmt.Println(result)"]},
                    {"type": "true-false", "statement": "В Go naked return можно использовать только с именованными возвращаемыми значениями.", "correct": True},
                    {"type": "fill-blank", "sentence": "В Go вместо исключений используется паттерн возврата (value, ___).", "answer": "error"},
                ],
            },
            {
                "t": "Указатели",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Указатели в Go", "markdown": "## Указатели\n\nУказатель хранит **адрес** переменной в памяти.\n\n### Создание указателя:\n```go\nx := 42\np := &x       // p — указатель на x\nfmt.Println(*p) // 42 — разыменование\n*p = 100\nfmt.Println(x)  // 100 — x изменился!\n```\n\n### Операторы:\n- `&` — взять адрес переменной\n- `*` — разыменовать указатель (получить значение)\n\n### Указатели в функциях:\n```go\nfunc increment(n *int) {\n    *n++\n}\n\nval := 5\nincrement(&val)\nfmt.Println(val) // 6\n```\n\n### new() — создание указателя:\n```go\np := new(int)   // *int, значение 0\n*p = 42\n```\n\n### Важно:\n- В Go **нет арифметики указателей** (в отличие от C)\n- Указатели безопаснее благодаря сборщику мусора\n- Используются для передачи больших структур без копирования"},
                    {"type": "matching", "pairs": [{"left": "&x", "right": "Получить адрес переменной x"}, {"left": "*p", "right": "Разыменовать указатель p"}, {"left": "*int", "right": "Тип: указатель на int"}, {"left": "new(int)", "right": "Создать указатель на новый int"}]},
                    {"type": "quiz", "question": "Что делает оператор & в Go?", "options": [{"id": "a", "text": "Логическое И", "correct": False}, {"id": "b", "text": "Берёт адрес переменной", "correct": True}, {"id": "c", "text": "Разыменовывает указатель", "correct": False}, {"id": "d", "text": "Побитовое И", "correct": False}]},
                    {"type": "true-false", "statement": "В Go поддерживается арифметика указателей, как в C.", "correct": False},
                    {"type": "code-puzzle", "instructions": "Передайте переменную по указателю в функцию", "correctOrder": ["func double(n *int) {", "    *n *= 2", "}", "val := 5", "double(&val)"]},
                ],
            },
            {
                "t": "Структуры (struct)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Структуры", "markdown": "## Структуры (struct)\n\nСтруктура — пользовательский тип с именованными полями.\n\n### Объявление:\n```go\ntype User struct {\n    Name  string\n    Email string\n    Age   int\n}\n```\n\n### Создание экземпляра:\n```go\n// Именованные поля\nu1 := User{Name: \"Алексей\", Email: \"a@b.com\", Age: 30}\n\n// Порядок полей\nu2 := User{\"Мария\", \"m@b.com\", 25}\n\n// Нулевая структура\nvar u3 User  // все поля = zero values\n```\n\n### Доступ к полям:\n```go\nfmt.Println(u1.Name)  // Алексей\nu1.Age = 31\n```\n\n### Указатели на структуры:\n```go\np := &u1\np.Name = \"Борис\"  // автоматическое разыменование\n```\n\n### Вложенные структуры:\n```go\ntype Address struct {\n    City, Street string\n}\ntype Person struct {\n    Name    string\n    Address Address\n}\n```\n\n### Анонимное встраивание:\n```go\ntype Employee struct {\n    Person        // встроенная структура\n    Position string\n}\ne := Employee{Person: Person{Name: \"Иван\"}, Position: \"Dev\"}\nfmt.Println(e.Name)  // доступ напрямую\n```"},
                    {"type": "quiz", "question": "Как объявить структуру в Go?", "options": [{"id": "a", "text": "class User {}", "correct": False}, {"id": "b", "text": "struct User {}", "correct": False}, {"id": "c", "text": "type User struct {}", "correct": True}, {"id": "d", "text": "def User():", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Создайте структуру и экземпляр", "correctOrder": ["type User struct {", "    Name string", "    Age  int", "}", "u := User{Name: \"Go\", Age: 15}"]},
                    {"type": "true-false", "statement": "При доступе к полю через указатель на структуру нужно явно разыменовывать указатель.", "correct": False},
                    {"type": "fill-blank", "sentence": "Анонимное ___ позволяет встраивать одну структуру в другую и обращаться к полям напрямую.", "answer": "встраивание"},
                ],
            },
            {
                "t": "Методы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Методы структур", "markdown": "## Методы\n\nМетод — функция с **получателем** (receiver).\n\n### Метод со значением-получателем:\n```go\ntype Circle struct {\n    Radius float64\n}\n\nfunc (c Circle) Area() float64 {\n    return 3.14159 * c.Radius * c.Radius\n}\n\nc := Circle{Radius: 5}\nfmt.Println(c.Area())  // 78.53975\n```\n\n### Метод с указателем-получателем:\n```go\nfunc (c *Circle) Scale(factor float64) {\n    c.Radius *= factor  // изменяет оригинал\n}\n\nc.Scale(2)\nfmt.Println(c.Radius)  // 10\n```\n\n### Когда использовать *T:\n- Нужно **изменять** поля структуры\n- Структура **большая** (избежать копирования)\n- **Консистентность** — если хоть один метод на *T, все лучше на *T\n\n### Когда использовать T:\n- Не нужно менять структуру\n- Структура маленькая (int, string)\n- Нужна неизменяемость"},
                    {"type": "quiz", "question": "Какой получатель позволяет изменять поля структуры?", "options": [{"id": "a", "text": "Получатель по значению (T)", "correct": False}, {"id": "b", "text": "Получатель по указателю (*T)", "correct": True}, {"id": "c", "text": "Оба варианта", "correct": False}, {"id": "d", "text": "Ни один", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Напишите метод Area для структуры Rectangle", "correctOrder": ["func (r Rectangle) Area() float64 {", "    return r.Width * r.Height", "}"]},
                    {"type": "true-false", "statement": "Если структура большая, лучше использовать получатель по значению для экономии памяти.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "func (c Circle) Area()", "right": "Получатель по значению"}, {"left": "func (c *Circle) Scale()", "right": "Получатель по указателю"}, {"left": "Маленькая структура", "right": "Можно передавать по значению"}, {"left": "Нужно менять поля", "right": "Только указатель-получатель"}]},
                ],
            },
            {
                "t": "Интерфейсы",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Интерфейсы в Go", "markdown": "## Интерфейсы\n\nИнтерфейс — набор сигнатур методов. В Go интерфейсы реализуются **неявно**.\n\n### Объявление:\n```go\ntype Shape interface {\n    Area() float64\n    Perimeter() float64\n}\n```\n\n### Неявная реализация:\n```go\ntype Circle struct { Radius float64 }\n\nfunc (c Circle) Area() float64 {\n    return 3.14 * c.Radius * c.Radius\n}\nfunc (c Circle) Perimeter() float64 {\n    return 2 * 3.14 * c.Radius\n}\n// Circle автоматически реализует Shape!\n```\n\n### Использование:\n```go\nfunc printInfo(s Shape) {\n    fmt.Printf(\"Area: %.2f\\n\", s.Area())\n}\nprintInfo(Circle{Radius: 5})\n```\n\n### Пустой интерфейс:\n```go\nvar x interface{}  // или any (Go 1.18+)\nx = 42\nx = \"строка\"\nx = true\n```\n\n### Type assertion:\n```go\nvar i interface{} = \"hello\"\ns, ok := i.(string)\nif ok {\n    fmt.Println(s)  // hello\n}\n```\n\n### Популярные интерфейсы стандартной библиотеки:\n- `io.Reader` — `Read(p []byte) (n int, err error)`\n- `io.Writer` — `Write(p []byte) (n int, err error)`\n- `fmt.Stringer` — `String() string`\n- `error` — `Error() string`"},
                    {"type": "quiz", "question": "Как реализуются интерфейсы в Go?", "options": [{"id": "a", "text": "Через ключевое слово implements", "correct": False}, {"id": "b", "text": "Неявно — достаточно реализовать все методы", "correct": True}, {"id": "c", "text": "Через наследование", "correct": False}, {"id": "d", "text": "Через аннотации", "correct": False}]},
                    {"type": "flashcards", "cards": [{"front": "io.Reader", "back": "Read(p []byte) (n int, err error)"}, {"front": "io.Writer", "back": "Write(p []byte) (n int, err error)"}, {"front": "fmt.Stringer", "back": "String() string"}, {"front": "error", "back": "Error() string"}]},
                    {"type": "true-false", "statement": "Пустой интерфейс interface{} может хранить значение любого типа.", "correct": True},
                    {"type": "fill-blank", "sentence": "Начиная с Go 1.18, вместо interface{} можно писать ___.", "answer": "any"},
                    {"type": "multi-select", "question": "Какие интерфейсы есть в стандартной библиотеке Go?", "options": [{"id": "a", "text": "io.Reader", "correct": True}, {"id": "b", "text": "fmt.Stringer", "correct": True}, {"id": "c", "text": "Comparable", "correct": False}, {"id": "d", "text": "error", "correct": True}, {"id": "e", "text": "Serializable", "correct": False}]},
                ],
            },
        ],
    },
    # ==================== SECTION 4: Конкурентность ====================
    {
        "title": "Конкурентность",
        "pos": 3,
        "lessons": [
            {
                "t": "Горутины (goroutines)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Горутины", "markdown": "## Горутины\n\nГорутина — легковесный поток выполнения, управляемый рантаймом Go.\n\n### Запуск горутины:\n```go\nfunc sayHello() {\n    fmt.Println(\"Hello из горутины!\")\n}\n\nfunc main() {\n    go sayHello()           // запуск горутины\n    go func() {             // анонимная горутина\n        fmt.Println(\"Анонимная!\")\n    }()\n    time.Sleep(time.Second) // ждём завершения\n}\n```\n\n### Характеристики:\n- Начальный стек — **2 КБ** (vs 1-8 МБ для потока ОС)\n- Можно запускать **тысячи** горутин одновременно\n- Планирование — кооперативное, рантаймом Go (M:N модель)\n- Ключевое слово `go` перед вызовом функции\n\n### Важно:\n- `main()` — тоже горутина\n- Когда `main()` завершается, все горутины умирают\n- `time.Sleep` — **плохой** способ ждать (используйте WaitGroup/каналы)\n\n### Сколько можно создать?\n```go\nfor i := 0; i < 100_000; i++ {\n    go func(n int) {\n        // каждая горутина занимает ~2КБ\n    }(i)\n}\n```"},
                    {"type": "quiz", "question": "Какой начальный размер стека горутины?", "options": [{"id": "a", "text": "1 МБ", "correct": False}, {"id": "b", "text": "2 КБ", "correct": True}, {"id": "c", "text": "8 КБ", "correct": False}, {"id": "d", "text": "64 КБ", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Запустите функцию как горутину", "correctOrder": ["go func() {", "    fmt.Println(\"горутина\")", "}()"]},
                    {"type": "true-false", "statement": "Когда функция main() завершается, все горутины продолжают работать.", "correct": False},
                    {"type": "fill-blank", "sentence": "Для запуска горутины используется ключевое слово ___.", "answer": "go"},
                ],
            },
            {
                "t": "Каналы (channels)",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Каналы", "markdown": "## Каналы\n\nКаналы — механизм коммуникации между горутинами.\n\n### Создание канала:\n```go\nch := make(chan int)          // небуферизированный\nbch := make(chan string, 10)  // буферизированный (ёмкость 10)\n```\n\n### Отправка и получение:\n```go\nch <- 42       // отправить в канал\nval := <-ch    // получить из канала\n```\n\n### Пример:\n```go\nfunc worker(ch chan string) {\n    ch <- \"результат\"  // отправляем\n}\n\nfunc main() {\n    ch := make(chan string)\n    go worker(ch)\n    msg := <-ch  // ждём и получаем\n    fmt.Println(msg)\n}\n```\n\n### Буферизированные каналы:\n```go\nch := make(chan int, 3)\nch <- 1  // не блокирует\nch <- 2  // не блокирует\nch <- 3  // не блокирует\n// ch <- 4  // блокирует — буфер полон!\n```\n\n### Закрытие канала:\n```go\nclose(ch)\n\n// Проверка закрытия:\nval, ok := <-ch\nif !ok {\n    fmt.Println(\"канал закрыт\")\n}\n```\n\n### range по каналу:\n```go\nfor val := range ch {\n    fmt.Println(val)\n}\n```"},
                    {"type": "matching", "pairs": [{"left": "ch <- 42", "right": "Отправить в канал"}, {"left": "<-ch", "right": "Получить из канала"}, {"left": "make(chan int)", "right": "Небуферизированный канал"}, {"left": "make(chan int, 10)", "right": "Буферизированный канал"}, {"left": "close(ch)", "right": "Закрыть канал"}]},
                    {"type": "quiz", "question": "Что произойдёт при отправке в небуферизированный канал без получателя?", "options": [{"id": "a", "text": "Значение потеряется", "correct": False}, {"id": "b", "text": "Горутина заблокируется", "correct": True}, {"id": "c", "text": "Программа завершится с ошибкой", "correct": False}, {"id": "d", "text": "Значение встанет в очередь", "correct": False}]},
                    {"type": "true-false", "statement": "Буферизированный канал блокирует отправку только когда буфер полон.", "correct": True},
                    {"type": "fill-blank", "sentence": "Функция ___ закрывает канал в Go.", "answer": "close"},
                ],
            },
            {
                "t": "select — мультиплексор каналов",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "select", "markdown": "## select\n\n`select` — позволяет ждать операции на нескольких каналах одновременно.\n\n### Базовый пример:\n```go\nselect {\ncase msg := <-ch1:\n    fmt.Println(\"ch1:\", msg)\ncase msg := <-ch2:\n    fmt.Println(\"ch2:\", msg)\ncase ch3 <- 42:\n    fmt.Println(\"отправлено в ch3\")\ndefault:\n    fmt.Println(\"ни один канал не готов\")\n}\n```\n\n### Таймаут:\n```go\nselect {\ncase res := <-ch:\n    fmt.Println(res)\ncase <-time.After(3 * time.Second):\n    fmt.Println(\"таймаут!\")\n}\n```\n\n### Бесконечный цикл с select:\n```go\nfor {\n    select {\n    case msg := <-messages:\n        fmt.Println(msg)\n    case <-done:\n        fmt.Println(\"завершение\")\n        return\n    }\n}\n```\n\n### Правила:\n- Если готовы несколько case — выбирается **случайный**\n- `default` — выполняется если ни один case не готов\n- Без `default` — select блокируется до готовности case"},
                    {"type": "quiz", "question": "Что произойдёт, если в select готовы два case одновременно?", "options": [{"id": "a", "text": "Выполнится первый по порядку", "correct": False}, {"id": "b", "text": "Выполнятся оба", "correct": False}, {"id": "c", "text": "Будет выбран случайный", "correct": True}, {"id": "d", "text": "Произойдёт ошибка", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Напишите select с таймаутом", "correctOrder": ["select {", "case res := <-ch:", "    fmt.Println(res)", "case <-time.After(3 * time.Second):", "    fmt.Println(\"таймаут\")", "}"]},
                    {"type": "true-false", "statement": "select без default блокируется до готовности хотя бы одного case.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "select с default", "back": "Неблокирующий — default выполнится если ни один канал не готов"}, {"front": "select без default", "back": "Блокирующий — ждёт готовности хотя бы одного case"}, {"front": "time.After", "back": "Возвращает канал, который получит значение через заданное время"}]},
                ],
            },
            {
                "t": "sync.WaitGroup",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "WaitGroup", "markdown": "## sync.WaitGroup\n\nWaitGroup — ожидание завершения группы горутин.\n\n### Пример:\n```go\nimport \"sync\"\n\nfunc main() {\n    var wg sync.WaitGroup\n\n    for i := 0; i < 5; i++ {\n        wg.Add(1)  // +1 горутина\n        go func(n int) {\n            defer wg.Done()  // -1 при завершении\n            fmt.Println(\"Worker\", n)\n        }(i)\n    }\n\n    wg.Wait()  // ждём все горутины\n    fmt.Println(\"Все завершены\")\n}\n```\n\n### Методы:\n- `Add(n)` — увеличить счётчик на n\n- `Done()` — уменьшить счётчик на 1 (обычно через defer)\n- `Wait()` — блокироваться до обнуления счётчика\n\n### Правила:\n- `Add()` вызывайте **до** запуска горутины\n- `Done()` вызывайте через `defer` в начале горутины\n- **Не копируйте** WaitGroup — передавайте по указателю"},
                    {"type": "drag-order", "items": ["Создать var wg sync.WaitGroup", "Вызвать wg.Add(1) перед запуском горутины", "Запустить горутину с defer wg.Done()", "Вызвать wg.Wait() для ожидания всех горутин"]},
                    {"type": "quiz", "question": "Что делает метод wg.Done()?", "options": [{"id": "a", "text": "Завершает горутину", "correct": False}, {"id": "b", "text": "Уменьшает счётчик на 1", "correct": True}, {"id": "c", "text": "Ждёт завершения всех горутин", "correct": False}, {"id": "d", "text": "Обнуляет счётчик", "correct": False}]},
                    {"type": "true-false", "statement": "WaitGroup можно безопасно копировать и передавать по значению.", "correct": False},
                    {"type": "fill-blank", "sentence": "Метод ___ блокирует выполнение до обнуления счётчика WaitGroup.", "answer": "Wait"},
                ],
            },
            {
                "t": "sync.Mutex",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Мьютексы", "markdown": "## sync.Mutex\n\nМьютекс — механизм взаимного исключения для защиты общих данных.\n\n### Проблема без мьютекса (гонка данных):\n```go\ncounter := 0\nfor i := 0; i < 1000; i++ {\n    go func() {\n        counter++  // ГОНКА ДАННЫХ!\n    }()\n}\n```\n\n### Решение с мьютексом:\n```go\nvar (\n    counter int\n    mu      sync.Mutex\n)\n\nfor i := 0; i < 1000; i++ {\n    go func() {\n        mu.Lock()\n        counter++\n        mu.Unlock()\n    }()\n}\n```\n\n### Идиоматичный паттерн:\n```go\nmu.Lock()\ndefer mu.Unlock()\n// критическая секция\n```\n\n### sync.RWMutex:\n```go\nvar rw sync.RWMutex\n\n// Множество читателей одновременно:\nrw.RLock()\nval := data[\"key\"]\nrw.RUnlock()\n\n// Только один писатель:\nrw.Lock()\ndata[\"key\"] = \"value\"\nrw.Unlock()\n```\n\n### Детектор гонок:\n```bash\ngo run -race main.go\n```"},
                    {"type": "quiz", "question": "Какой флаг включает детектор гонок данных?", "options": [{"id": "a", "text": "-debug", "correct": False}, {"id": "b", "text": "-race", "correct": True}, {"id": "c", "text": "-mutex", "correct": False}, {"id": "d", "text": "-safe", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "sync.Mutex", "right": "Один читатель ИЛИ один писатель"}, {"left": "sync.RWMutex", "right": "Много читателей ИЛИ один писатель"}, {"left": "Lock()/Unlock()", "right": "Захват и освобождение мьютекса"}, {"left": "RLock()/RUnlock()", "right": "Захват и освобождение на чтение"}]},
                    {"type": "true-false", "statement": "sync.RWMutex позволяет нескольким горутинам одновременно читать данные.", "correct": True},
                    {"type": "code-puzzle", "instructions": "Защитите инкремент мьютексом", "correctOrder": ["mu.Lock()", "defer mu.Unlock()", "counter++"]},
                ],
            },
            {
                "t": "Паттерны конкурентности",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Паттерны конкурентности Go", "markdown": "## Паттерны конкурентности\n\n### 1. Fan-Out / Fan-In:\n```go\n// Fan-Out: несколько горутин читают из одного канала\nfunc worker(jobs <-chan int, results chan<- int) {\n    for j := range jobs {\n        results <- j * 2\n    }\n}\n\n// Fan-In: собираем результаты\nfor i := 0; i < numWorkers; i++ {\n    go worker(jobs, results)\n}\n```\n\n### 2. Pipeline:\n```go\nfunc gen(nums ...int) <-chan int {\n    out := make(chan int)\n    go func() {\n        for _, n := range nums {\n            out <- n\n        }\n        close(out)\n    }()\n    return out\n}\n\nfunc square(in <-chan int) <-chan int {\n    out := make(chan int)\n    go func() {\n        for n := range in {\n            out <- n * n\n        }\n        close(out)\n    }()\n    return out\n}\n```\n\n### 3. Done-канал (отмена):\n```go\ndone := make(chan struct{})\ngo func() {\n    // работа...\n    select {\n    case <-done:\n        return  // отмена\n    case result <- res:\n    }\n}()\nclose(done)  // отменяет все горутины\n```\n\n### 4. Worker Pool:\n```go\nfunc pool(numWorkers int, jobs <-chan Job, results chan<- Result) {\n    var wg sync.WaitGroup\n    for i := 0; i < numWorkers; i++ {\n        wg.Add(1)\n        go func() {\n            defer wg.Done()\n            for job := range jobs {\n                results <- process(job)\n            }\n        }()\n    }\n    wg.Wait()\n    close(results)\n}\n```\n\n### Принцип Go:\n> \"Не общайтесь через разделяемую память; разделяйте память через общение.\""},
                    {"type": "matching", "pairs": [{"left": "Fan-Out", "right": "Несколько горутин читают из одного канала"}, {"left": "Fan-In", "right": "Результаты собираются в один канал"}, {"left": "Pipeline", "right": "Цепочка стадий обработки через каналы"}, {"left": "Worker Pool", "right": "Фиксированное количество воркеров обрабатывают задачи"}]},
                    {"type": "quiz", "question": "Какой паттерн использует цепочку каналов для последовательной обработки?", "options": [{"id": "a", "text": "Fan-Out", "correct": False}, {"id": "b", "text": "Worker Pool", "correct": False}, {"id": "c", "text": "Pipeline", "correct": True}, {"id": "d", "text": "Semaphore", "correct": False}]},
                    {"type": "true-false", "statement": "Принцип Go: общайтесь через разделяемую память, а не через каналы.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "Fan-Out / Fan-In", "back": "Распараллеливание работы и сбор результатов через каналы"}, {"front": "Pipeline", "back": "Цепочка стадий: gen → square → print, каждая через канал"}, {"front": "Done-канал", "back": "close(done) — сигнал отмены всем горутинам через пустую структуру"}, {"front": "Worker Pool", "back": "N воркеров + WaitGroup + каналы jobs/results"}]},
                ],
            },
        ],
    },
    # ==================== SECTION 5: Стандартная библиотека ====================
    {
        "title": "Стандартная библиотека",
        "pos": 4,
        "lessons": [
            {
                "t": "Пакет strings",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Работа со строками", "markdown": "## Пакет strings\n\n### Поиск:\n```go\nstrings.Contains(\"Hello Go\", \"Go\")   // true\nstrings.HasPrefix(\"Hello\", \"He\")     // true\nstrings.HasSuffix(\"Hello\", \"lo\")     // true\nstrings.Index(\"Hello\", \"ll\")         // 2\n```\n\n### Преобразование:\n```go\nstrings.ToUpper(\"hello\")     // \"HELLO\"\nstrings.ToLower(\"HELLO\")     // \"hello\"\nstrings.TrimSpace(\" hi \")    // \"hi\"\nstrings.Trim(\"--hi--\", \"-\")  // \"hi\"\n```\n\n### Разделение и объединение:\n```go\nstrings.Split(\"a,b,c\", \",\")       // [\"a\", \"b\", \"c\"]\nstrings.Join([]string{\"a\",\"b\"}, \"-\") // \"a-b\"\n```\n\n### Замена:\n```go\nstrings.Replace(\"aaa\", \"a\", \"b\", 2)  // \"bba\"\nstrings.ReplaceAll(\"aaa\", \"a\", \"b\")  // \"bbb\"\n```\n\n### strings.Builder (эффективная конкатенация):\n```go\nvar b strings.Builder\nfor i := 0; i < 100; i++ {\n    b.WriteString(\"Go\")\n}\nresult := b.String()\n```"},
                    {"type": "matching", "pairs": [{"left": "strings.Split", "right": "Разделить строку на слайс"}, {"left": "strings.Join", "right": "Объединить слайс в строку"}, {"left": "strings.Contains", "right": "Проверить наличие подстроки"}, {"left": "strings.Builder", "right": "Эффективная конкатенация строк"}]},
                    {"type": "quiz", "question": "Какой тип использовать для эффективной конкатенации многих строк?", "options": [{"id": "a", "text": "fmt.Sprintf", "correct": False}, {"id": "b", "text": "Оператор +", "correct": False}, {"id": "c", "text": "strings.Builder", "correct": True}, {"id": "d", "text": "[]byte", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Функция strings.___ разделяет строку на слайс по разделителю.", "answer": "Split"},
                    {"type": "type-answer", "question": "Какая функция проверяет, начинается ли строка с заданного префикса?", "acceptedAnswers": ["strings.HasPrefix", "HasPrefix"]},
                ],
            },
            {
                "t": "Пакеты io и os",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Ввод-вывод и файловая система", "markdown": "## Пакеты io и os\n\n### Чтение файла:\n```go\ndata, err := os.ReadFile(\"config.txt\")\nif err != nil {\n    log.Fatal(err)\n}\nfmt.Println(string(data))\n```\n\n### Запись файла:\n```go\nerr := os.WriteFile(\"out.txt\", []byte(\"Привет\"), 0644)\n```\n\n### Открытие файла:\n```go\nf, err := os.Open(\"data.txt\")  // только чтение\ndefer f.Close()\n\nscanner := bufio.NewScanner(f)\nfor scanner.Scan() {\n    fmt.Println(scanner.Text())\n}\n```\n\n### Создание/запись:\n```go\nf, err := os.Create(\"log.txt\")\ndefer f.Close()\nf.WriteString(\"Запись в файл\\n\")\n```\n\n### io.Reader и io.Writer:\n```go\n// Копирование из Reader в Writer\nio.Copy(os.Stdout, resp.Body)\n```\n\n### Переменные окружения:\n```go\nport := os.Getenv(\"PORT\")\nif port == \"\" {\n    port = \"8080\"\n}\n```\n\n### Аргументы командной строки:\n```go\nargs := os.Args[1:]  // без имени программы\n```"},
                    {"type": "quiz", "question": "Какая функция читает весь файл в []byte?", "options": [{"id": "a", "text": "os.Open", "correct": False}, {"id": "b", "text": "os.ReadFile", "correct": True}, {"id": "c", "text": "io.ReadAll", "correct": False}, {"id": "d", "text": "bufio.Read", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Прочитайте файл и выведите содержимое", "correctOrder": ["data, err := os.ReadFile(\"config.txt\")", "if err != nil {", "    log.Fatal(err)", "}", "fmt.Println(string(data))"]},
                    {"type": "true-false", "statement": "os.Open открывает файл для чтения и записи.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "os.ReadFile", "back": "Читает весь файл в []byte"}, {"front": "os.WriteFile", "back": "Записывает []byte в файл с указанными правами"}, {"front": "os.Create", "back": "Создаёт файл (или перезаписывает существующий)"}, {"front": "os.Getenv", "back": "Получить значение переменной окружения"}]},
                ],
            },
            {
                "t": "HTTP-клиент (net/http)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "HTTP в Go", "markdown": "## Пакет net/http\n\n### Простой GET-запрос:\n```go\nresp, err := http.Get(\"https://api.example.com/data\")\nif err != nil {\n    log.Fatal(err)\n}\ndefer resp.Body.Close()\n\nbody, err := io.ReadAll(resp.Body)\nfmt.Println(string(body))\n```\n\n### POST-запрос:\n```go\njsonData := []byte(`{\"name\": \"Go\"}`)\nresp, err := http.Post(\n    \"https://api.example.com/items\",\n    \"application/json\",\n    bytes.NewBuffer(jsonData),\n)\n```\n\n### Кастомный клиент:\n```go\nclient := &http.Client{\n    Timeout: 10 * time.Second,\n}\n\nreq, _ := http.NewRequest(\"GET\", url, nil)\nreq.Header.Set(\"Authorization\", \"Bearer token\")\n\nresp, err := client.Do(req)\n```\n\n### Простой HTTP-сервер:\n```go\nhttp.HandleFunc(\"/hello\", func(w http.ResponseWriter, r *http.Request) {\n    fmt.Fprintf(w, \"Hello, %s!\", r.URL.Query().Get(\"name\"))\n})\n\nlog.Fatal(http.ListenAndServe(\":8080\", nil))\n```"},
                    {"type": "quiz", "question": "Почему важно вызывать defer resp.Body.Close()?", "options": [{"id": "a", "text": "Для красоты кода", "correct": False}, {"id": "b", "text": "Чтобы освободить сетевое соединение", "correct": True}, {"id": "c", "text": "Чтобы записать данные", "correct": False}, {"id": "d", "text": "Это необязательно", "correct": False}]},
                    {"type": "drag-order", "items": ["Выполнить http.Get(url)", "Проверить err != nil", "Добавить defer resp.Body.Close()", "Прочитать тело: io.ReadAll(resp.Body)", "Обработать данные"]},
                    {"type": "true-false", "statement": "http.ListenAndServe блокирует выполнение до остановки сервера.", "correct": True},
                    {"type": "fill-blank", "sentence": "Для настройки таймаутов HTTP-запросов используют кастомный ___.", "answer": "Client"},
                ],
            },
            {
                "t": "JSON (encoding/json)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Работа с JSON", "markdown": "## Пакет encoding/json\n\n### Маршалинг (struct → JSON):\n```go\ntype User struct {\n    Name  string `json:\"name\"`\n    Email string `json:\"email\"`\n    Age   int    `json:\"age,omitempty\"`\n}\n\nu := User{Name: \"Go\", Email: \"go@dev.com\"}\ndata, _ := json.Marshal(u)\n// {\"name\":\"Go\",\"email\":\"go@dev.com\"}\n```\n\n### Анмаршалинг (JSON → struct):\n```go\njsonStr := `{\"name\":\"Go\",\"email\":\"go@dev.com\"}`\nvar u User\njson.Unmarshal([]byte(jsonStr), &u)\nfmt.Println(u.Name)  // Go\n```\n\n### Теги структуры:\n```go\ntype Config struct {\n    Host string `json:\"host\"`\n    Port int    `json:\"port\"`\n    Debug bool  `json:\"-\"`           // исключить\n    TTL  int    `json:\"ttl,omitempty\"` // пропустить если 0\n}\n```\n\n### json.Decoder (потоковый):\n```go\ndecoder := json.NewDecoder(resp.Body)\nvar result map[string]interface{}\ndecoder.Decode(&result)\n```\n\n### json.MarshalIndent (красивый вывод):\n```go\ndata, _ := json.MarshalIndent(u, \"\", \"  \")\n```"},
                    {"type": "matching", "pairs": [{"left": "json.Marshal", "right": "struct → JSON bytes"}, {"left": "json.Unmarshal", "right": "JSON bytes → struct"}, {"left": "json:\"-\"", "right": "Исключить поле из JSON"}, {"left": "omitempty", "right": "Пропустить если zero value"}]},
                    {"type": "quiz", "question": "Какой тег исключает поле из JSON?", "options": [{"id": "a", "text": "json:\"skip\"", "correct": False}, {"id": "b", "text": "json:\"-\"", "correct": True}, {"id": "c", "text": "json:\"omitempty\"", "correct": False}, {"id": "d", "text": "json:\"ignore\"", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Декодируйте JSON в структуру", "correctOrder": ["jsonStr := `{\"name\":\"Go\"}`", "var u User", "json.Unmarshal([]byte(jsonStr), &u)", "fmt.Println(u.Name)"]},
                    {"type": "fill-blank", "sentence": "Теги структуры указываются в обратных кавычках после типа поля, например `json:\"___\"`.", "answer": "name"},
                ],
            },
            {
                "t": "Тестирование (testing)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Пакет testing", "markdown": "## Тестирование в Go\n\nGo имеет встроенную систему тестирования.\n\n### Файл: `math_test.go`\n```go\npackage math\n\nimport \"testing\"\n\nfunc TestAdd(t *testing.T) {\n    result := Add(2, 3)\n    if result != 5 {\n        t.Errorf(\"Add(2,3) = %d; want 5\", result)\n    }\n}\n```\n\n### Запуск:\n```bash\ngo test ./...\ngo test -v          # подробный вывод\ngo test -run TestAdd # конкретный тест\ngo test -cover       # покрытие\n```\n\n### Table-driven тесты:\n```go\nfunc TestAdd(t *testing.T) {\n    tests := []struct {\n        a, b, want int\n    }{\n        {1, 2, 3},\n        {0, 0, 0},\n        {-1, 1, 0},\n    }\n    for _, tt := range tests {\n        got := Add(tt.a, tt.b)\n        if got != tt.want {\n            t.Errorf(\"Add(%d,%d) = %d; want %d\",\n                tt.a, tt.b, got, tt.want)\n        }\n    }\n}\n```\n\n### Подтесты:\n```go\nt.Run(\"positive\", func(t *testing.T) {\n    // ...\n})\n```\n\n### Бенчмарки:\n```go\nfunc BenchmarkAdd(b *testing.B) {\n    for i := 0; i < b.N; i++ {\n        Add(1, 2)\n    }\n}\n// go test -bench=.\n```"},
                    {"type": "quiz", "question": "Как должен называться файл с тестами в Go?", "options": [{"id": "a", "text": "test_math.go", "correct": False}, {"id": "b", "text": "math_test.go", "correct": True}, {"id": "c", "text": "math.test.go", "correct": False}, {"id": "d", "text": "math_spec.go", "correct": False}]},
                    {"type": "true-false", "statement": "Имена тестовых функций в Go должны начинаться с Test.", "correct": True},
                    {"type": "matching", "pairs": [{"left": "go test ./...", "right": "Запуск всех тестов"}, {"left": "go test -v", "right": "Подробный вывод"}, {"left": "go test -cover", "right": "Показать покрытие кода"}, {"left": "go test -bench=.", "right": "Запуск бенчмарков"}]},
                    {"type": "flashcards", "cards": [{"front": "Table-driven тесты", "back": "Массив структур с входными данными и ожидаемым результатом"}, {"front": "t.Run()", "back": "Создание подтестов с отдельными именами"}, {"front": "BenchmarkXxx", "back": "Бенчмарк-функция, принимает *testing.B, цикл b.N"}]},
                ],
            },
            {
                "t": "Пакет context",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "context — управление временем жизни", "markdown": "## Пакет context\n\ncontext — управление временем жизни операций, отменой и передачей значений.\n\n### context.Background():\n```go\nctx := context.Background()  // корневой контекст\n```\n\n### context.WithCancel:\n```go\nctx, cancel := context.WithCancel(context.Background())\ndefer cancel()\n\ngo func(ctx context.Context) {\n    select {\n    case <-ctx.Done():\n        fmt.Println(\"отменено\")\n        return\n    case <-time.After(5 * time.Second):\n        fmt.Println(\"готово\")\n    }\n}(ctx)\n\ncancel()  // отменяем\n```\n\n### context.WithTimeout:\n```go\nctx, cancel := context.WithTimeout(ctx, 3*time.Second)\ndefer cancel()\n\nreq, _ := http.NewRequestWithContext(ctx, \"GET\", url, nil)\nresp, err := client.Do(req)  // отменится через 3 сек\n```\n\n### context.WithValue:\n```go\nctx = context.WithValue(ctx, \"userID\", 42)\nid := ctx.Value(\"userID\").(int)\n```\n\n### Правила:\n- Передавайте context **первым параметром** функции\n- Всегда вызывайте `cancel()` через defer\n- Не храните context в структурах"},
                    {"type": "quiz", "question": "Какой контекст является корневым?", "options": [{"id": "a", "text": "context.TODO()", "correct": False}, {"id": "b", "text": "context.Background()", "correct": True}, {"id": "c", "text": "context.Root()", "correct": False}, {"id": "d", "text": "context.New()", "correct": False}]},
                    {"type": "drag-order", "items": ["Создать контекст с таймаутом: context.WithTimeout", "Добавить defer cancel()", "Передать ctx в функцию/запрос", "Проверять ctx.Done() в горутине", "cancel() вызовется автоматически при завершении"]},
                    {"type": "true-false", "statement": "context рекомендуется передавать первым параметром функции.", "correct": True},
                    {"type": "fill-blank", "sentence": "Метод ctx.___() возвращает канал, который закрывается при отмене контекста.", "answer": "Done"},
                ],
            },
        ],
    },
    # ==================== SECTION 6: Web-разработка ====================
    {
        "title": "Web-разработка",
        "pos": 5,
        "lessons": [
            {
                "t": "REST API на Go",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Создание REST API", "markdown": "## REST API на чистом net/http\n\n### Простой сервер:\n```go\npackage main\n\nimport (\n    \"encoding/json\"\n    \"net/http\"\n)\n\ntype Item struct {\n    ID   int    `json:\"id\"`\n    Name string `json:\"name\"`\n}\n\nvar items = []Item{\n    {1, \"Go Book\"},\n    {2, \"Go Course\"},\n}\n\nfunc getItems(w http.ResponseWriter, r *http.Request) {\n    w.Header().Set(\"Content-Type\", \"application/json\")\n    json.NewEncoder(w).Encode(items)\n}\n\nfunc main() {\n    http.HandleFunc(\"/api/items\", getItems)\n    http.ListenAndServe(\":8080\", nil)\n}\n```\n\n### HTTP-методы:\n```go\nfunc handler(w http.ResponseWriter, r *http.Request) {\n    switch r.Method {\n    case http.MethodGet:\n        // GET logic\n    case http.MethodPost:\n        // POST logic\n    default:\n        http.Error(w, \"Method not allowed\", 405)\n    }\n}\n```\n\n### Чтение тела запроса:\n```go\nvar item Item\njson.NewDecoder(r.Body).Decode(&item)\n```\n\n### Статус-коды:\n```go\nw.WriteHeader(http.StatusCreated)     // 201\nhttp.Error(w, \"Not found\", http.StatusNotFound) // 404\n```"},
                    {"type": "quiz", "question": "Какой метод устанавливает HTTP статус-код ответа?", "options": [{"id": "a", "text": "w.SetStatus()", "correct": False}, {"id": "b", "text": "w.WriteHeader()", "correct": True}, {"id": "c", "text": "w.StatusCode()", "correct": False}, {"id": "d", "text": "http.SetStatus()", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Верните JSON-ответ с данными", "correctOrder": ["w.Header().Set(\"Content-Type\", \"application/json\")", "json.NewEncoder(w).Encode(items)"]},
                    {"type": "true-false", "statement": "http.HandleFunc может автоматически маршрутизировать по HTTP-методу.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "http.StatusOK", "right": "200"}, {"left": "http.StatusCreated", "right": "201"}, {"left": "http.StatusNotFound", "right": "404"}, {"left": "http.StatusInternalServerError", "right": "500"}]},
                ],
            },
            {
                "t": "Роутинг: chi и gin",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "HTTP-роутеры", "markdown": "## Роутеры: chi и gin\n\n### chi — легковесный роутер:\n```go\nimport \"github.com/go-chi/chi/v5\"\n\nr := chi.NewRouter()\n\nr.Get(\"/api/users\", listUsers)\nr.Post(\"/api/users\", createUser)\nr.Get(\"/api/users/{id}\", getUser)\nr.Put(\"/api/users/{id}\", updateUser)\nr.Delete(\"/api/users/{id}\", deleteUser)\n\n// Параметр маршрута:\nfunc getUser(w http.ResponseWriter, r *http.Request) {\n    id := chi.URLParam(r, \"id\")\n}\n\nhttp.ListenAndServe(\":8080\", r)\n```\n\n### chi — группы маршрутов:\n```go\nr.Route(\"/api/v1\", func(r chi.Router) {\n    r.Get(\"/users\", listUsers)\n    r.Post(\"/users\", createUser)\n})\n```\n\n### gin — популярный фреймворк:\n```go\nimport \"github.com/gin-gonic/gin\"\n\nr := gin.Default()\n\nr.GET(\"/api/users\", func(c *gin.Context) {\n    c.JSON(200, users)\n})\n\nr.GET(\"/api/users/:id\", func(c *gin.Context) {\n    id := c.Param(\"id\")\n    c.JSON(200, gin.H{\"id\": id})\n})\n\nr.Run(\":8080\")\n```\n\n### Сравнение:\n- **chi** — совместим с net/http, легковесный\n- **gin** — быстрый, больше фич из коробки"},
                    {"type": "quiz", "question": "Как получить параметр URL в chi?", "options": [{"id": "a", "text": "r.URL.Query().Get(\"id\")", "correct": False}, {"id": "b", "text": "chi.URLParam(r, \"id\")", "correct": True}, {"id": "c", "text": "r.Param(\"id\")", "correct": False}, {"id": "d", "text": "mux.Vars(r)[\"id\"]", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "chi", "right": "Совместим с net/http, легковесный"}, {"left": "gin", "right": "Быстрый, больше фич из коробки"}, {"left": "{id} в chi", "right": "Параметр маршрута"}, {"left": ":id в gin", "right": "Параметр маршрута"}]},
                    {"type": "true-false", "statement": "chi полностью совместим со стандартным net/http.", "correct": True},
                    {"type": "fill-blank", "sentence": "В gin для возврата JSON используется метод c.___().", "answer": "JSON"},
                ],
            },
            {
                "t": "Middleware",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Middleware в Go", "markdown": "## Middleware\n\nMiddleware — функция, оборачивающая обработчик.\n\n### Паттерн middleware:\n```go\nfunc Logger(next http.Handler) http.Handler {\n    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n        start := time.Now()\n        next.ServeHTTP(w, r)\n        log.Printf(\"%s %s %v\", r.Method, r.URL.Path, time.Since(start))\n    })\n}\n```\n\n### Использование с chi:\n```go\nr := chi.NewRouter()\nr.Use(middleware.Logger)         // встроенный логгер\nr.Use(middleware.Recoverer)      // перехват panic\nr.Use(middleware.RequestID)      // ID запроса\nr.Use(middleware.RealIP)         // реальный IP\nr.Use(middleware.Timeout(60 * time.Second))\n```\n\n### CORS middleware:\n```go\nr.Use(cors.Handler(cors.Options{\n    AllowedOrigins: []string{\"https://example.com\"},\n    AllowedMethods: []string{\"GET\", \"POST\", \"PUT\", \"DELETE\"},\n    AllowedHeaders: []string{\"Authorization\", \"Content-Type\"},\n}))\n```\n\n### Middleware для аутентификации:\n```go\nfunc AuthMiddleware(next http.Handler) http.Handler {\n    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n        token := r.Header.Get(\"Authorization\")\n        if token == \"\" {\n            http.Error(w, \"Unauthorized\", 401)\n            return\n        }\n        // проверка токена...\n        next.ServeHTTP(w, r)\n    })\n}\n```"},
                    {"type": "quiz", "question": "Что делает middleware.Recoverer в chi?", "options": [{"id": "a", "text": "Логирует запросы", "correct": False}, {"id": "b", "text": "Перехватывает panic и возвращает 500", "correct": True}, {"id": "c", "text": "Добавляет CORS-заголовки", "correct": False}, {"id": "d", "text": "Проверяет авторизацию", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Подключите middleware к роутеру chi", "correctOrder": ["r := chi.NewRouter()", "r.Use(middleware.Logger)", "r.Use(middleware.Recoverer)", "r.Get(\"/api/data\", handler)"]},
                    {"type": "true-false", "statement": "Middleware в Go оборачивает http.Handler и возвращает новый http.Handler.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "middleware.Logger", "back": "Логирует метод, URL и время обработки запроса"}, {"front": "middleware.Recoverer", "back": "Перехватывает panic, возвращает 500 вместо краша"}, {"front": "middleware.RequestID", "back": "Добавляет уникальный ID к каждому запросу"}, {"front": "CORS middleware", "back": "Управляет кросс-доменными запросами (AllowedOrigins, Methods, Headers)"}]},
                ],
            },
            {
                "t": "PostgreSQL с pgx",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "PostgreSQL в Go", "markdown": "## PostgreSQL с pgx\n\n### Установка:\n```bash\ngo get github.com/jackc/pgx/v5\n```\n\n### Подключение:\n```go\nimport \"github.com/jackc/pgx/v5/pgxpool\"\n\npool, err := pgxpool.New(ctx,\n    \"postgres://user:pass@localhost:5432/mydb\")\ndefer pool.Close()\n```\n\n### SELECT:\n```go\nrows, err := pool.Query(ctx,\n    \"SELECT id, name, email FROM users WHERE age > $1\", 18)\ndefer rows.Close()\n\nfor rows.Next() {\n    var u User\n    rows.Scan(&u.ID, &u.Name, &u.Email)\n    fmt.Println(u)\n}\n```\n\n### SELECT одной строки:\n```go\nvar u User\nerr := pool.QueryRow(ctx,\n    \"SELECT id, name FROM users WHERE id = $1\", id,\n).Scan(&u.ID, &u.Name)\n```\n\n### INSERT:\n```go\n_, err := pool.Exec(ctx,\n    \"INSERT INTO users (name, email) VALUES ($1, $2)\",\n    \"Go Dev\", \"go@dev.com\")\n```\n\n### Транзакции:\n```go\ntx, err := pool.Begin(ctx)\ndefer tx.Rollback(ctx)\n\ntx.Exec(ctx, \"UPDATE accounts SET balance = balance - $1 WHERE id = $2\", 100, fromID)\ntx.Exec(ctx, \"UPDATE accounts SET balance = balance + $1 WHERE id = $2\", 100, toID)\n\ntx.Commit(ctx)\n```"},
                    {"type": "quiz", "question": "Какой плейсхолдер использует pgx для параметров?", "options": [{"id": "a", "text": "?", "correct": False}, {"id": "b", "text": "$1, $2, ...", "correct": True}, {"id": "c", "text": ":name", "correct": False}, {"id": "d", "text": "%s", "correct": False}]},
                    {"type": "drag-order", "items": ["Создать пул: pgxpool.New(ctx, connString)", "Выполнить запрос: pool.Query(ctx, sql, args)", "Итерировать: for rows.Next()", "Считать данные: rows.Scan(&fields...)", "Закрыть rows: defer rows.Close()"]},
                    {"type": "true-false", "statement": "pgxpool автоматически управляет пулом соединений к PostgreSQL.", "correct": True},
                    {"type": "fill-blank", "sentence": "Для отмены транзакции используется метод tx.___().", "answer": "Rollback"},
                ],
            },
            {
                "t": "Миграции базы данных",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Миграции", "markdown": "## Миграции БД\n\n### golang-migrate:\n```bash\ngo install -tags postgres github.com/golang-migrate/migrate/v4/cmd/migrate@latest\n```\n\n### Создание миграции:\n```bash\nmigrate create -ext sql -dir migrations -seq create_users\n```\n\nСоздаст:\n- `000001_create_users.up.sql`\n- `000001_create_users.down.sql`\n\n### up.sql:\n```sql\nCREATE TABLE users (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(255) NOT NULL,\n    email VARCHAR(255) UNIQUE NOT NULL,\n    created_at TIMESTAMP DEFAULT NOW()\n);\n```\n\n### down.sql:\n```sql\nDROP TABLE IF EXISTS users;\n```\n\n### Применение:\n```bash\nmigrate -path migrations -database $DB_URL up\nmigrate -path migrations -database $DB_URL down 1\nmigrate -path migrations -database $DB_URL version\n```\n\n### Из кода:\n```go\nimport \"github.com/golang-migrate/migrate/v4\"\n\nm, err := migrate.New(\"file://migrations\", dbURL)\nm.Up()  // применить все\n```"},
                    {"type": "quiz", "question": "Какая команда применяет все миграции?", "options": [{"id": "a", "text": "migrate run", "correct": False}, {"id": "b", "text": "migrate -path migrations -database $DB_URL up", "correct": True}, {"id": "c", "text": "migrate apply", "correct": False}, {"id": "d", "text": "migrate execute", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "up.sql", "right": "Применение миграции (создание)"}, {"left": "down.sql", "right": "Откат миграции (удаление)"}, {"left": "migrate up", "right": "Применить все миграции"}, {"left": "migrate down 1", "right": "Откатить последнюю миграцию"}]},
                    {"type": "true-false", "statement": "Каждая миграция состоит из двух файлов: up и down.", "correct": True},
                    {"type": "fill-blank", "sentence": "Файл ___.sql содержит SQL для отката миграции.", "answer": "down"},
                ],
            },
            {
                "t": "JWT-аутентификация",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "JWT Auth в Go", "markdown": "## JWT-аутентификация\n\n### Установка:\n```bash\ngo get github.com/golang-jwt/jwt/v5\n```\n\n### Генерация токена:\n```go\nimport \"github.com/golang-jwt/jwt/v5\"\n\ntype Claims struct {\n    UserID int    `json:\"user_id\"`\n    Email  string `json:\"email\"`\n    jwt.RegisteredClaims\n}\n\nfunc GenerateToken(userID int, email string) (string, error) {\n    claims := Claims{\n        UserID: userID,\n        Email:  email,\n        RegisteredClaims: jwt.RegisteredClaims{\n            ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),\n            IssuedAt:  jwt.NewNumericDate(time.Now()),\n        },\n    }\n    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)\n    return token.SignedString([]byte(\"secret-key\"))\n}\n```\n\n### Валидация токена:\n```go\nfunc ValidateToken(tokenStr string) (*Claims, error) {\n    token, err := jwt.ParseWithClaims(tokenStr, &Claims{},\n        func(t *jwt.Token) (interface{}, error) {\n            return []byte(\"secret-key\"), nil\n        })\n    if err != nil {\n        return nil, err\n    }\n    claims, ok := token.Claims.(*Claims)\n    if !ok || !token.Valid {\n        return nil, fmt.Errorf(\"invalid token\")\n    }\n    return claims, nil\n}\n```\n\n### Middleware:\n```go\nfunc JWTAuth(next http.Handler) http.Handler {\n    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n        header := r.Header.Get(\"Authorization\")\n        tokenStr := strings.TrimPrefix(header, \"Bearer \")\n        claims, err := ValidateToken(tokenStr)\n        if err != nil {\n            http.Error(w, \"Unauthorized\", 401)\n            return\n        }\n        ctx := context.WithValue(r.Context(), \"claims\", claims)\n        next.ServeHTTP(w, r.WithContext(ctx))\n    })\n}\n```"},
                    {"type": "quiz", "question": "Какой алгоритм подписи JWT чаще всего используют в Go?", "options": [{"id": "a", "text": "RS256", "correct": False}, {"id": "b", "text": "HS256", "correct": True}, {"id": "c", "text": "ES256", "correct": False}, {"id": "d", "text": "PS256", "correct": False}]},
                    {"type": "drag-order", "items": ["Создать Claims с UserID и ExpiresAt", "Создать токен: jwt.NewWithClaims(HS256, claims)", "Подписать: token.SignedString(secretKey)", "Клиент отправляет токен в заголовке Authorization", "Middleware парсит и валидирует токен"]},
                    {"type": "true-false", "statement": "JWT-токен хранит данные в зашифрованном виде на сервере.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "JWT (JSON Web Token)", "back": "Самодостаточный токен: Header.Payload.Signature (Base64)"}, {"front": "Claims", "back": "Данные внутри токена: UserID, Email, ExpiresAt"}, {"front": "SignedString", "back": "Метод подписи токена секретным ключом"}, {"front": "ParseWithClaims", "back": "Парсинг и валидация токена с извлечением Claims"}]},
                ],
            },
        ],
    },
    # ==================== SECTION 7: Продвинутый Go ====================
    {
        "title": "Продвинутый Go",
        "pos": 6,
        "lessons": [
            {
                "t": "gRPC",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "gRPC в Go", "markdown": "## gRPC\n\ngRPC — высокопроизводительный RPC-фреймворк от Google.\n\n### Установка:\n```bash\ngo install google.golang.org/protobuf/cmd/protoc-gen-go@latest\ngo install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest\n```\n\n### Proto-файл (user.proto):\n```protobuf\nsyntax = \"proto3\";\n\npackage user;\noption go_package = \"./pb\";\n\nservice UserService {\n    rpc GetUser (GetUserRequest) returns (UserResponse);\n    rpc ListUsers (Empty) returns (stream UserResponse);\n}\n\nmessage GetUserRequest {\n    int32 id = 1;\n}\n\nmessage UserResponse {\n    int32 id = 1;\n    string name = 2;\n    string email = 3;\n}\n```\n\n### Генерация кода:\n```bash\nprotoc --go_out=. --go-grpc_out=. user.proto\n```\n\n### Сервер:\n```go\ntype server struct {\n    pb.UnimplementedUserServiceServer\n}\n\nfunc (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.UserResponse, error) {\n    return &pb.UserResponse{Id: req.Id, Name: \"Go Dev\"}, nil\n}\n\nlis, _ := net.Listen(\"tcp\", \":50051\")\ngrpcServer := grpc.NewServer()\npb.RegisterUserServiceServer(grpcServer, &server{})\ngrpcServer.Serve(lis)\n```\n\n### Клиент:\n```go\nconn, _ := grpc.Dial(\"localhost:50051\", grpc.WithInsecure())\nclient := pb.NewUserServiceClient(conn)\nresp, _ := client.GetUser(ctx, &pb.GetUserRequest{Id: 1})\n```"},
                    {"type": "quiz", "question": "Какой формат сериализации использует gRPC?", "options": [{"id": "a", "text": "JSON", "correct": False}, {"id": "b", "text": "Protocol Buffers (protobuf)", "correct": True}, {"id": "c", "text": "XML", "correct": False}, {"id": "d", "text": "MessagePack", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "protoc", "right": "Компилятор Proto-файлов"}, {"left": "proto3", "right": "Версия синтаксиса protobuf"}, {"left": "stream", "right": "Потоковая передача данных"}, {"left": "UnimplementedServer", "right": "Базовая структура для совместимости"}]},
                    {"type": "true-false", "statement": "gRPC работает только с протоколом HTTP/1.1.", "correct": False},
                    {"type": "fill-blank", "sentence": "gRPC использует протокол HTTP/___ для передачи данных.", "answer": "2"},
                ],
            },
            {
                "t": "Docker для Go-приложений",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Контейнеризация Go", "markdown": "## Docker для Go\n\n### Multi-stage Dockerfile:\n```dockerfile\n# Стадия сборки\nFROM golang:1.22-alpine AS builder\nWORKDIR /app\nCOPY go.mod go.sum ./\nRUN go mod download\nCOPY . .\nRUN CGO_ENABLED=0 GOOS=linux go build -o server ./cmd/server\n\n# Финальный образ\nFROM alpine:3.19\nRUN apk --no-cache add ca-certificates\nWORKDIR /app\nCOPY --from=builder /app/server .\nEXPOSE 8080\nCMD [\"./server\"]\n```\n\n### Scratch-образ (минимальный):\n```dockerfile\nFROM scratch\nCOPY --from=builder /app/server /server\nENTRYPOINT [\"/server\"]\n```\n\n### docker-compose.yml:\n```yaml\nservices:\n  app:\n    build: .\n    ports:\n      - \"8080:8080\"\n    environment:\n      - DATABASE_URL=postgres://user:pass@db:5432/mydb\n    depends_on:\n      - db\n  db:\n    image: postgres:16-alpine\n    environment:\n      POSTGRES_PASSWORD: pass\n    volumes:\n      - pgdata:/var/lib/postgresql/data\nvolumes:\n  pgdata:\n```\n\n### Размер образа:\n- `golang:1.22` — ~800 МБ\n- `golang:1.22-alpine` — ~250 МБ\n- `alpine` + бинарник — ~15 МБ\n- `scratch` + бинарник — ~8 МБ"},
                    {"type": "quiz", "question": "Какой базовый образ даёт минимальный размер для Go?", "options": [{"id": "a", "text": "golang:latest", "correct": False}, {"id": "b", "text": "alpine", "correct": False}, {"id": "c", "text": "scratch", "correct": True}, {"id": "d", "text": "ubuntu", "correct": False}]},
                    {"type": "drag-order", "items": ["FROM golang:alpine AS builder", "COPY go.mod go.sum и go mod download", "COPY исходный код и go build", "FROM scratch (финальный образ)", "COPY --from=builder бинарник"]},
                    {"type": "true-false", "statement": "CGO_ENABLED=0 нужно для статической компиляции без зависимости от libc.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Multi-stage build", "back": "Несколько FROM: первый для сборки, последний для запуска — минимальный образ"}, {"front": "scratch", "back": "Пустой образ Docker — только бинарник, ~8 МБ"}, {"front": "CGO_ENABLED=0", "back": "Отключает CGo — статически линкованный бинарник"}, {"front": "GOOS=linux", "back": "Кросс-компиляция под Linux (для Docker)"}]},
                ],
            },
            {
                "t": "CI/CD для Go",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "CI/CD пайплайн", "markdown": "## CI/CD для Go\n\n### GitHub Actions:\n```yaml\nname: Go CI\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\n\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-go@v5\n        with:\n          go-version: '1.22'\n\n      - name: Install deps\n        run: go mod download\n\n      - name: Lint\n        uses: golangci/golangci-lint-action@v4\n\n      - name: Test\n        run: go test -race -coverprofile=coverage.out ./...\n\n      - name: Build\n        run: go build -o server ./cmd/server\n\n  deploy:\n    needs: test\n    runs-on: ubuntu-latest\n    if: github.ref == 'refs/heads/main'\n    steps:\n      - uses: actions/checkout@v4\n      - name: Build & Push Docker\n        run: |\n          docker build -t myapp:latest .\n          docker push myapp:latest\n```\n\n### golangci-lint (линтер):\n```bash\ngolangci-lint run ./...\n```\n\n### Makefile:\n```makefile\n.PHONY: build test lint\n\nbuild:\n\tgo build -o bin/server ./cmd/server\n\ntest:\n\tgo test -race -v ./...\n\nlint:\n\tgolangci-lint run\n```"},
                    {"type": "quiz", "question": "Какой линтер рекомендуется для Go-проектов?", "options": [{"id": "a", "text": "eslint", "correct": False}, {"id": "b", "text": "golangci-lint", "correct": True}, {"id": "c", "text": "pylint", "correct": False}, {"id": "d", "text": "gofmt", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "go test -race", "right": "Тесты с детектором гонок"}, {"left": "go test -cover", "right": "Покрытие кода тестами"}, {"left": "golangci-lint", "right": "Статический анализ кода"}, {"left": "go build", "right": "Компиляция бинарника"}]},
                    {"type": "true-false", "statement": "golangci-lint объединяет множество линтеров в один инструмент.", "correct": True},
                    {"type": "fill-blank", "sentence": "Флаг -race при запуске тестов включает детектор ___ данных.", "answer": "гонок"},
                ],
            },
            {
                "t": "Профилирование и оптимизация",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Профилирование Go", "markdown": "## Профилирование\n\nGo имеет встроенные инструменты профилирования.\n\n### pprof — HTTP-эндпоинт:\n```go\nimport _ \"net/http/pprof\"\n\ngo func() {\n    http.ListenAndServe(\":6060\", nil)\n}()\n```\n\n### Доступные профили:\n- `http://localhost:6060/debug/pprof/` — индекс\n- `/debug/pprof/heap` — память\n- `/debug/pprof/goroutine` — горутины\n- `/debug/pprof/profile` — CPU (30 сек)\n\n### go tool pprof:\n```bash\ngo tool pprof http://localhost:6060/debug/pprof/heap\n(pprof) top 10\n(pprof) web       # визуализация в браузере\n```\n\n### Бенчмарки + профилирование:\n```bash\ngo test -bench=. -cpuprofile=cpu.prof\ngo tool pprof cpu.prof\n```\n\n### trace — трассировка:\n```bash\ncurl -o trace.out http://localhost:6060/debug/pprof/trace?seconds=5\ngo tool trace trace.out\n```\n\n### Советы по оптимизации:\n- Используйте `sync.Pool` для переиспользования объектов\n- Избегайте аллокаций в горячих путях\n- Используйте `bytes.Buffer` вместо конкатенации строк\n- Предвыделяйте слайсы: `make([]T, 0, capacity)`"},
                    {"type": "quiz", "question": "Какой инструмент Go используется для профилирования?", "options": [{"id": "a", "text": "go debug", "correct": False}, {"id": "b", "text": "go tool pprof", "correct": True}, {"id": "c", "text": "go profile", "correct": False}, {"id": "d", "text": "go analyze", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "/debug/pprof/heap", "right": "Профиль памяти"}, {"left": "/debug/pprof/profile", "right": "Профиль CPU"}, {"left": "/debug/pprof/goroutine", "right": "Список горутин"}, {"left": "go tool trace", "back": "Трассировка выполнения"}]},
                    {"type": "multi-select", "question": "Какие советы помогут оптимизировать Go-код?", "options": [{"id": "a", "text": "Предвыделять ёмкость слайсов", "correct": True}, {"id": "b", "text": "Использовать sync.Pool", "correct": True}, {"id": "c", "text": "Избегать горутин", "correct": False}, {"id": "d", "text": "Использовать bytes.Buffer вместо +", "correct": True}, {"id": "e", "text": "Всегда использовать interface{}", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для переиспользования объектов без повторной аллокации используют sync.___.", "answer": "Pool"},
                ],
            },
            {
                "t": "Итоговый проект: микросервис",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Итоговый проект", "markdown": "## Итоговый проект: REST-микросервис\n\nСоберём всё вместе — production-ready микросервис.\n\n### Структура проекта:\n```\nmyservice/\n  cmd/server/main.go     # точка входа\n  internal/\n    handler/             # HTTP-обработчики\n    service/             # бизнес-логика\n    repository/          # работа с БД\n    model/               # структуры данных\n  migrations/            # SQL-миграции\n  pkg/                   # общие утилиты\n  Dockerfile\n  docker-compose.yml\n  Makefile\n  go.mod\n```\n\n### Чеклист production-ready:\n- [x] Структурированное логирование (slog/zerolog)\n- [x] Graceful shutdown\n- [x] Health-check эндпоинт\n- [x] Конфигурация из env-переменных\n- [x] Docker multi-stage build\n- [x] Миграции БД\n- [x] JWT-аутентификация\n- [x] Middleware (logger, recover, CORS)\n- [x] Тесты (unit + integration)\n- [x] CI/CD пайплайн\n- [x] Документация API (Swagger)\n\n### Graceful Shutdown:\n```go\nsrv := &http.Server{Addr: \":8080\", Handler: r}\n\ngo func() {\n    if err := srv.ListenAndServe(); err != nil {\n        log.Println(\"server stopped\")\n    }\n}()\n\nquit := make(chan os.Signal, 1)\nsignal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)\n<-quit\n\nctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)\ndefer cancel()\nsrv.Shutdown(ctx)\n```\n\n### Поздравляем!\nВы освоили Go от основ до production-ready микросервисов!"},
                    {"type": "flashcards", "cards": [{"front": "cmd/", "back": "Точки входа приложений (main.go)"}, {"front": "internal/", "back": "Приватный код — не импортируется другими модулями"}, {"front": "pkg/", "back": "Общие утилиты — могут импортироваться извне"}, {"front": "Graceful Shutdown", "back": "Корректное завершение: ждём обработки текущих запросов, потом останавливаем сервер"}]},
                    {"type": "quiz", "question": "Зачем нужен Graceful Shutdown?", "options": [{"id": "a", "text": "Для быстрого перезапуска", "correct": False}, {"id": "b", "text": "Чтобы дождаться обработки текущих запросов перед остановкой", "correct": True}, {"id": "c", "text": "Для экономии памяти", "correct": False}, {"id": "d", "text": "Для логирования", "correct": False}]},
                    {"type": "drag-order", "items": ["Определить структуру проекта (cmd, internal, migrations)", "Настроить роутер и middleware", "Реализовать handler → service → repository", "Добавить JWT-аутентификацию", "Написать тесты", "Создать Dockerfile и docker-compose", "Настроить CI/CD пайплайн"]},
                    {"type": "multi-select", "question": "Что должно быть в production-ready Go-сервисе?", "options": [{"id": "a", "text": "Graceful Shutdown", "correct": True}, {"id": "b", "text": "Health-check эндпоинт", "correct": True}, {"id": "c", "text": "Глобальные переменные для состояния", "correct": False}, {"id": "d", "text": "Структурированное логирование", "correct": True}, {"id": "e", "text": "panic вместо обработки ошибок", "correct": False}]},
                    {"type": "true-false", "statement": "Пакет internal/ в Go может быть импортирован любым внешним модулем.", "correct": False},
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
            slug="golang-developers-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Go",
            difficulty="Intermediate",
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
