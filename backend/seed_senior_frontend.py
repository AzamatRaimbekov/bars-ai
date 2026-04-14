"""Seed: Senior Frontend Developer course with 8 sections, 40+ lessons, diverse step types."""
import asyncio
import uuid

from sqlalchemy import select

from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

# ---------------------------------------------------------------------------
# COURSE DATA
# ---------------------------------------------------------------------------

COURSE_TITLE = "Senior Frontend Developer"
COURSE_DESC = (
    "Углублённый курс для опытных фронтенд-разработчиков: продвинутый TypeScript, "
    "внутренности React, архитектура стейт-менеджмента, системы сборки, тестирование, "
    "веб-перформанс, безопасность и DevOps-практики."
)

SECTIONS = [
    # =====================================================================
    # SECTION 1: Advanced TypeScript Patterns
    # =====================================================================
    {
        "title": "Advanced TypeScript Patterns",
        "pos": 0,
        "lessons": [
            # Lesson 1-1
            {
                "t": "Conditional Types & Template Literals",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Условные типы и шаблонные литералы",
                        "content": (
                            "## Conditional Types\n\n"
                            "Условные типы в TypeScript позволяют описывать логику выбора типа на уровне системы типов. "
                            "Синтаксис `T extends U ? X : Y` работает аналогично тернарному оператору, но на уровне типов.\n\n"
                            "```typescript\n"
                            "type IsString<T> = T extends string ? true : false;\n"
                            "type A = IsString<'hello'>; // true\n"
                            "type B = IsString<42>;       // false\n"
                            "```\n\n"
                            "### Template Literal Types\n\n"
                            "TypeScript 4.1 добавил шаблонные литеральные типы, которые позволяют конструировать строковые типы "
                            "с помощью интерполяции:\n\n"
                            "```typescript\n"
                            "type EventName<T extends string> = `on${Capitalize<T>}`;\n"
                            "type ClickEvent = EventName<'click'>; // 'onClick'\n"
                            "```\n\n"
                            "Комбинация conditional types с template literals даёт мощный инструмент для типобезопасного "
                            "маппинга строк, например при работе с REST API endpoint-ами."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что вернёт тип `type R = 'hello' extends string ? true : false`?",
                        "options": [
                            {"id": "a", "text": "true", "correct": True},
                            {"id": "b", "text": "false", "correct": False},
                            {"id": "c", "text": "boolean", "correct": False},
                            {"id": "d", "text": "never", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Напишите условный тип",
                        "description": "Создайте тип `ExtractPromise<T>`, который извлекает внутренний тип из Promise. Если T не является Promise, верните T.",
                        "starterCode": (
                            "type ExtractPromise<T> = // ваш код\n\n"
                            "// Ожидаемый результат:\n"
                            "// ExtractPromise<Promise<string>> → string\n"
                            "// ExtractPromise<number> → number"
                        ),
                        "solution": "type ExtractPromise<T> = T extends Promise<infer U> ? U : T;",
                    },
                    {
                        "type": "type-answer",
                        "question": "Какое ключевое слово используется для извлечения типа из обобщённого параметра в conditional types?",
                        "answer": "infer",
                    },
                ],
            },
            # Lesson 1-2
            {
                "t": "Mapped Types & Key Remapping",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Mapped Types и ремаппинг ключей",
                        "content": (
                            "## Mapped Types\n\n"
                            "Mapped types позволяют трансформировать каждое свойство существующего типа. "
                            "Базовый синтаксис: `{ [K in keyof T]: NewType }`.\n\n"
                            "```typescript\n"
                            "type Readonly<T> = { readonly [K in keyof T]: T[K] };\n"
                            "type Optional<T> = { [K in keyof T]?: T[K] };\n"
                            "```\n\n"
                            "### Key Remapping (as clause)\n\n"
                            "TypeScript 4.1 добавил возможность переименовывать ключи через `as`:\n\n"
                            "```typescript\n"
                            "type Getters<T> = {\n"
                            "  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]\n"
                            "};\n\n"
                            "interface Person { name: string; age: number; }\n"
                            "type PersonGetters = Getters<Person>;\n"
                            "// { getName: () => string; getAge: () => number; }\n"
                            "```\n\n"
                            "Ремаппинг ключей позволяет фильтровать свойства, возвращая `never` для ненужных ключей."
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Соберите mapped type с фильтрацией",
                        "description": "Расположите фрагменты кода в правильном порядке, чтобы создать тип, извлекающий только строковые свойства.",
                        "fragments": [
                            "type StringProps<T> = {",
                            "  [K in keyof T",
                            "    as T[K] extends string ? K : never]",
                            "  : T[K]",
                            "};",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Что произойдёт, если mapped type вернёт `never` для ключа через `as` clause?",
                        "options": [
                            {"id": "a", "text": "Свойство будет иметь тип never", "correct": False},
                            {"id": "b", "text": "Свойство будет исключено из результата", "correct": True},
                            {"id": "c", "text": "Произойдёт ошибка компиляции", "correct": False},
                            {"id": "d", "text": "Свойство станет optional", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Создайте утилитарный тип",
                        "description": "Напишите тип `Mutable<T>`, который убирает модификатор readonly со всех свойств типа T.",
                        "starterCode": (
                            "type Mutable<T> = // ваш код\n\n"
                            "// Пример:\n"
                            "// type Frozen = { readonly x: number; readonly y: string };\n"
                            "// Mutable<Frozen> → { x: number; y: string }"
                        ),
                        "solution": "type Mutable<T> = { -readonly [K in keyof T]: T[K] };",
                    },
                ],
            },
            # Lesson 1-3
            {
                "t": "Type Guards & Narrowing",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Type Guards и сужение типов",
                        "content": (
                            "## Type Guards\n\n"
                            "Type guard — это выражение, которое сужает тип переменной в определённой ветке кода. "
                            "TypeScript поддерживает несколько видов type guards:\n\n"
                            "### typeof guards\n"
                            "```typescript\n"
                            "function process(x: string | number) {\n"
                            "  if (typeof x === 'string') {\n"
                            "    return x.toUpperCase(); // x: string\n"
                            "  }\n"
                            "  return x.toFixed(2); // x: number\n"
                            "}\n"
                            "```\n\n"
                            "### Пользовательские type guards (is)\n"
                            "```typescript\n"
                            "interface Fish { swim(): void; }\n"
                            "interface Bird { fly(): void; }\n\n"
                            "function isFish(pet: Fish | Bird): pet is Fish {\n"
                            "  return (pet as Fish).swim !== undefined;\n"
                            "}\n"
                            "```\n\n"
                            "### Discriminated Unions\n"
                            "Самый мощный паттерн — дискриминантные объединения. Общее поле-дискриминант "
                            "позволяет TypeScript автоматически сужать тип в switch/case."
                        ),
                    },
                    {
                        "type": "true-false",
                        "statement": "Оператор `in` может использоваться как type guard в TypeScript для проверки наличия свойства.",
                        "answer": True,
                        "explanation": "Да, `'swim' in pet` сужает тип до типа, содержащего свойство swim.",
                    },
                    {
                        "type": "code-editor",
                        "title": "Реализуйте type guard",
                        "description": "Напишите функцию-type guard `isError`, которая проверяет, является ли объект экземпляром Error с полем `code` типа number.",
                        "starterCode": (
                            "interface AppError extends Error {\n"
                            "  code: number;\n"
                            "}\n\n"
                            "function isAppError(err: unknown): // дополните сигнатуру {\n"
                            "  // ваш код\n"
                            "}"
                        ),
                        "solution": (
                            "function isAppError(err: unknown): err is AppError {\n"
                            "  return err instanceof Error && typeof (err as any).code === 'number';\n"
                            "}"
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Сопоставьте guard с механизмом",
                        "pairs": [
                            {"left": "typeof x === 'string'", "right": "Примитивный type guard"},
                            {"left": "x instanceof Date", "right": "Проверка по прототипу"},
                            {"left": "'kind' in obj", "right": "Проверка наличия свойства"},
                            {"left": "function isX(a): a is X", "right": "Пользовательский type guard"},
                        ],
                    },
                ],
            },
            # Lesson 1-4
            {
                "t": "Декораторы и Метаданные",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Декораторы в TypeScript",
                        "content": (
                            "## Декораторы (Stage 3)\n\n"
                            "Декораторы — это функции, которые модифицируют поведение классов, методов, свойств и параметров. "
                            "В TypeScript 5+ используется стандартный синтаксис ECMAScript декораторов.\n\n"
                            "```typescript\n"
                            "function logged(originalMethod: any, context: ClassMethodDecoratorContext) {\n"
                            "  return function (this: any, ...args: any[]) {\n"
                            "    console.log(`Calling ${String(context.name)}`);\n"
                            "    return originalMethod.call(this, ...args);\n"
                            "  };\n"
                            "}\n\n"
                            "class UserService {\n"
                            "  @logged\n"
                            "  getUser(id: string) { return db.find(id); }\n"
                            "}\n"
                            "```\n\n"
                            "### reflect-metadata\n"
                            "Библиотека `reflect-metadata` позволяет привязывать произвольные метаданные к классам и свойствам. "
                            "Это основа DI-контейнеров (InversifyJS, tsyringe) и ORM (TypeORM).\n\n"
                            "```typescript\n"
                            "import 'reflect-metadata';\n"
                            "Reflect.defineMetadata('role', 'admin', target, propertyKey);\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой тип декоратора выполняется первым при наличии нескольких декораторов на одном методе?",
                        "options": [
                            {"id": "a", "text": "Верхний (первый объявленный)", "correct": False},
                            {"id": "b", "text": "Нижний (ближайший к методу)", "correct": True},
                            {"id": "c", "text": "Порядок не определён", "correct": False},
                            {"id": "d", "text": "Все выполняются параллельно", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Соберите декоратор валидации",
                        "description": "Расположите фрагменты, чтобы создать декоратор, проверяющий что аргументы не undefined.",
                        "fragments": [
                            "function validate(",
                            "  originalMethod: any,",
                            "  context: ClassMethodDecoratorContext",
                            ") {",
                            "  return function (this: any, ...args: any[]) {",
                            "    if (args.some(a => a === undefined)) throw new Error('Invalid args');",
                            "    return originalMethod.call(this, ...args);",
                            "  };",
                            "}",
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Какая библиотека метаданных используется в TypeORM и NestJS для реализации dependency injection?",
                        "answer": "reflect-metadata",
                    },
                ],
            },
            # Lesson 1-5
            {
                "t": "Infer и рекурсивные типы",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Ключевое слово infer и рекурсия",
                        "content": (
                            "## infer в Conditional Types\n\n"
                            "`infer` объявляет переменную типа внутри условного типа, позволяя TypeScript «вывести» часть структуры:\n\n"
                            "```typescript\n"
                            "type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;\n"
                            "type Params<T> = T extends (...args: infer P) => any ? P : never;\n"
                            "```\n\n"
                            "### Рекурсивные типы\n\n"
                            "TypeScript 4.1+ поддерживает рекурсивные conditional types. Это позволяет рекурсивно "
                            "обрабатывать вложенные структуры:\n\n"
                            "```typescript\n"
                            "type DeepReadonly<T> = T extends object\n"
                            "  ? { readonly [K in keyof T]: DeepReadonly<T[K]> }\n"
                            "  : T;\n\n"
                            "type Flatten<T> = T extends Array<infer U> ? Flatten<U> : T;\n"
                            "type X = Flatten<number[][][]>; // number\n"
                            "```\n\n"
                            "Рекурсивные типы имеют ограничение глубины (~1000 уровней). При превышении TypeScript "
                            "выдаёт ошибку `Type instantiation is excessively deep`."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Рекурсивный тип DeepPartial",
                        "description": "Реализуйте тип `DeepPartial<T>`, который делает все свойства объекта (и вложенных объектов) необязательными.",
                        "starterCode": (
                            "type DeepPartial<T> = // ваш код\n\n"
                            "// Тест:\n"
                            "// interface Config {\n"
                            "//   db: { host: string; port: number; };\n"
                            "//   cache: { ttl: number; };\n"
                            "// }\n"
                            "// DeepPartial<Config> → все поля опциональны на любой глубине"
                        ),
                        "solution": (
                            "type DeepPartial<T> = T extends object\n"
                            "  ? { [K in keyof T]?: DeepPartial<T[K]> }\n"
                            "  : T;"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что вернёт тип `type T = string extends infer R ? R : never`?",
                        "options": [
                            {"id": "a", "text": "never", "correct": False},
                            {"id": "b", "text": "string", "correct": True},
                            {"id": "c", "text": "unknown", "correct": False},
                            {"id": "d", "text": "Ошибка компиляции", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "title": "Дополните тип",
                        "sentence": "type Head<T extends any[]> = T extends [___first, ...any[]] ? ___first : never;",
                        "blanks": [
                            {"id": "first", "answer": "infer"},
                            {"id": "first", "answer": "infer"},
                        ],
                    },
                ],
            },
            # Lesson 1-6
            {
                "t": "Практика: Типизация API клиента",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Типобезопасный API клиент",
                        "content": (
                            "## Паттерн типизации REST API\n\n"
                            "Типобезопасный API-клиент позволяет TypeScript проверять endpoint-ы, параметры и ответы "
                            "на этапе компиляции. Ключевая идея — описать маршруты как типы:\n\n"
                            "```typescript\n"
                            "interface ApiRoutes {\n"
                            "  '/users': { GET: { response: User[] }; POST: { body: CreateUser; response: User } };\n"
                            "  '/users/:id': { GET: { response: User }; DELETE: { response: void } };\n"
                            "}\n\n"
                            "type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';\n\n"
                            "async function api<\n"
                            "  P extends keyof ApiRoutes,\n"
                            "  M extends keyof ApiRoutes[P]\n"
                            ">(path: P, method: M, ...args: any[]): Promise<ApiRoutes[P][M]['response']> {\n"
                            "  // реализация\n"
                            "}\n"
                            "```\n\n"
                            "Этот паттерн используется в библиотеках типа `zodios`, `ts-rest`, `openapi-typescript`."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Типизация fetch-обёртки",
                        "description": "Создайте обобщённую функцию `typedFetch`, которая принимает URL и возвращает типизированный результат.",
                        "starterCode": (
                            "async function typedFetch<T>(url: string, init?: RequestInit): Promise<T> {\n"
                            "  // реализуйте функцию, которая:\n"
                            "  // 1. Делает fetch запрос\n"
                            "  // 2. Проверяет response.ok\n"
                            "  // 3. Парсит JSON и возвращает как T\n"
                            "}"
                        ),
                        "solution": (
                            "async function typedFetch<T>(url: string, init?: RequestInit): Promise<T> {\n"
                            "  const response = await fetch(url, init);\n"
                            "  if (!response.ok) throw new Error(`HTTP ${response.status}`);\n"
                            "  return response.json() as Promise<T>;\n"
                            "}"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Типизация path-параметров",
                        "description": "Напишите тип `ExtractParams<T>`, который извлекает параметры из строки пути (`:id`, `:slug`).",
                        "starterCode": (
                            "// ExtractParams<'/users/:id/posts/:postId'>\n"
                            "// → { id: string; postId: string }\n\n"
                            "type ExtractParams<T extends string> = // ваш код"
                        ),
                        "solution": (
                            "type ExtractParams<T extends string> =\n"
                            "  T extends `${string}:${infer Param}/${infer Rest}`\n"
                            "    ? { [K in Param]: string } & ExtractParams<Rest>\n"
                            "    : T extends `${string}:${infer Param}`\n"
                            "      ? { [K in Param]: string }\n"
                            "      : {};"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой утилитарный тип TypeScript извлекает тип возвращаемого значения функции?",
                        "options": [
                            {"id": "a", "text": "Parameters<T>", "correct": False},
                            {"id": "b", "text": "ReturnType<T>", "correct": True},
                            {"id": "c", "text": "InstanceType<T>", "correct": False},
                            {"id": "d", "text": "ThisType<T>", "correct": False},
                        ],
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 2: React Internals & Performance
    # =====================================================================
    {
        "title": "React Internals & Performance",
        "pos": 1,
        "lessons": [
            # Lesson 2-1
            {
                "t": "Virtual DOM и Fiber Architecture",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Virtual DOM и архитектура Fiber",
                        "content": (
                            "## Virtual DOM\n\n"
                            "Virtual DOM — это лёгкое представление реального DOM в виде JavaScript-объектов. "
                            "Каждый React-элемент — это объект `{ type, props, children }`. При обновлении React "
                            "создаёт новое дерево VDOM, сравнивает с предыдущим (diffing) и применяет минимальный "
                            "набор изменений к реальному DOM.\n\n"
                            "## Fiber Architecture (React 16+)\n\n"
                            "Fiber — это переписанный с нуля движок reconciliation. Ключевые отличия:\n\n"
                            "- **Incremental rendering**: рендеринг можно разбить на чанки и прервать\n"
                            "- **Priority-based scheduling**: обновления имеют приоритеты (user input > animation > data fetch)\n"
                            "- **Двойная буферизация**: React поддерживает два дерева Fiber — current и workInProgress\n\n"
                            "Каждый Fiber-узел содержит: `type`, `stateNode`, `child`, `sibling`, `return`, "
                            "`pendingProps`, `memoizedState`, `effectTag`."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какая основная проблема stack reconciler (React < 16), которую решает Fiber?",
                        "options": [
                            {"id": "a", "text": "Утечки памяти при рендеринге", "correct": False},
                            {"id": "b", "text": "Синхронный рендеринг блокирует main thread", "correct": True},
                            {"id": "c", "text": "Невозможность использовать JSX", "correct": False},
                            {"id": "d", "text": "Отсутствие поддержки серверного рендеринга", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "title": "Сопоставьте свойства Fiber-узла",
                        "pairs": [
                            {"left": "child", "right": "Первый дочерний элемент"},
                            {"left": "sibling", "right": "Следующий элемент на том же уровне"},
                            {"left": "return", "right": "Ссылка на родительский узел"},
                            {"left": "stateNode", "right": "Ссылка на DOM-элемент или экземпляр компонента"},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "В Fiber архитектуре React обходит дерево с помощью рекурсии, как и stack reconciler.",
                        "answer": False,
                        "explanation": "Fiber использует итеративный обход через linked list (child → sibling → return), что позволяет прервать и возобновить работу.",
                    },
                ],
            },
            # Lesson 2-2
            {
                "t": "Reconciliation алгоритм",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Алгоритм согласования (Reconciliation)",
                        "content": (
                            "## Reconciliation\n\n"
                            "React reconciliation — алгоритм сравнения двух деревьев VDOM для определения минимальных изменений. "
                            "Полное сравнение деревьев имеет сложность O(n³), поэтому React использует эвристики:\n\n"
                            "### Две ключевые эвристики:\n"
                            "1. **Разные типы элементов** → полная замена поддерева\n"
                            "2. **Ключи (key)** → стабильная идентификация элементов в списках\n\n"
                            "### Алгоритм для списков:\n"
                            "```\n"
                            "// Без key: React сравнивает по индексу → O(n) вставка в начало\n"
                            "// С key: React строит Map<key, fiber> → O(1) lookup\n"
                            "```\n\n"
                            "### Фазы Fiber reconciliation:\n"
                            "1. **Render phase** (прерываемая): обход дерева, вычисление изменений\n"
                            "2. **Commit phase** (синхронная): применение изменений к DOM\n\n"
                            "Commit phase состоит из: `beforeMutation` → `mutation` → `layout` этапов."
                        ),
                    },
                    {
                        "type": "timeline",
                        "title": "Эволюция рендеринга в React",
                        "items": [
                            {"label": "React 0.14", "description": "Stack reconciler, синхронный рендеринг"},
                            {"label": "React 16.0", "description": "Fiber architecture, Error Boundaries"},
                            {"label": "React 16.6", "description": "React.lazy, Suspense для code splitting"},
                            {"label": "React 18.0", "description": "Concurrent rendering, automatic batching"},
                            {"label": "React 19.0", "description": "React Compiler, Actions, use() hook"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Почему использование индекса массива как key — антипаттерн при перестановке элементов?",
                        "options": [
                            {"id": "a", "text": "Индексы не являются строками", "correct": False},
                            {"id": "b", "text": "React не может определить какой элемент переместился и пересоздаёт всё", "correct": True},
                            {"id": "c", "text": "Индексы вызывают утечки памяти", "correct": False},
                            {"id": "d", "text": "TypeScript не разрешает числа как key", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Как называется фаза Fiber reconciliation, в которой React применяет изменения к реальному DOM?",
                        "answer": "commit",
                    },
                ],
            },
            # Lesson 2-3
            {
                "t": "useMemo, useCallback и React.memo",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Мемоизация в React",
                        "content": (
                            "## Проблема лишних ре-рендеров\n\n"
                            "React по умолчанию рендерит все дочерние компоненты при обновлении родителя. "
                            "Три инструмента мемоизации:\n\n"
                            "### React.memo\n"
                            "HOC, который пропускает ре-рендер если props не изменились (shallow compare):\n"
                            "```typescript\n"
                            "const ExpensiveList = React.memo(({ items }: Props) => {\n"
                            "  return items.map(item => <Item key={item.id} {...item} />);\n"
                            "});\n"
                            "```\n\n"
                            "### useMemo\n"
                            "Кеширует результат вычислений:\n"
                            "```typescript\n"
                            "const sorted = useMemo(() => items.sort(compareFn), [items]);\n"
                            "```\n\n"
                            "### useCallback\n"
                            "Кеширует ссылку на функцию (эквивалент `useMemo(() => fn, deps)`):\n"
                            "```typescript\n"
                            "const handleClick = useCallback((id: string) => {\n"
                            "  setSelected(id);\n"
                            "}, []);\n"
                            "```\n\n"
                            "**Важно:** мемоизация не бесплатна. Используйте только когда стоимость ре-рендера > стоимости сравнения."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Оптимизация компонента",
                        "description": "Оптимизируйте компонент TodoList, чтобы он не перерендеривался при изменении unrelated state.",
                        "starterCode": (
                            "function TodoList({ todos, onToggle }) {\n"
                            "  const sorted = todos.sort((a, b) => a.text.localeCompare(b.text));\n"
                            "  return (\n"
                            "    <ul>\n"
                            "      {sorted.map(t => (\n"
                            "        <li key={t.id} onClick={() => onToggle(t.id)}>{t.text}</li>\n"
                            "      ))}\n"
                            "    </ul>\n"
                            "  );\n"
                            "}"
                        ),
                        "solution": (
                            "const TodoList = React.memo(function TodoList({ todos, onToggle }) {\n"
                            "  const sorted = useMemo(\n"
                            "    () => [...todos].sort((a, b) => a.text.localeCompare(b.text)),\n"
                            "    [todos]\n"
                            "  );\n"
                            "  return (\n"
                            "    <ul>\n"
                            "      {sorted.map(t => (\n"
                            "        <li key={t.id} onClick={() => onToggle(t.id)}>{t.text}</li>\n"
                            "      ))}\n"
                            "    </ul>\n"
                            "  );\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Когда React.memo НЕ поможет предотвратить ре-рендер?",
                        "options": [
                            {"id": "a", "text": "Когда props — примитивы", "correct": False},
                            {"id": "b", "text": "Когда компонент использует useContext, и контекст изменился", "correct": True},
                            {"id": "c", "text": "Когда компонент не имеет children", "correct": False},
                            {"id": "d", "text": "Когда компонент функциональный", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "useMemo гарантирует, что значение никогда не будет пересчитано, пока зависимости не изменятся.",
                        "answer": False,
                        "explanation": "React может сбросить кеш useMemo при нехватке памяти. Это семантический хинт, не гарантия.",
                    },
                ],
            },
            # Lesson 2-4
            {
                "t": "Concurrent Mode и Suspense",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Concurrent Rendering и Suspense",
                        "content": (
                            "## Concurrent Features (React 18+)\n\n"
                            "Concurrent rendering позволяет React прерывать рендеринг для обработки более приоритетных "
                            "обновлений. Ключевые API:\n\n"
                            "### useTransition\n"
                            "Помечает обновление как низкоприоритетное:\n"
                            "```typescript\n"
                            "const [isPending, startTransition] = useTransition();\n"
                            "startTransition(() => setSearchResults(filtered));\n"
                            "```\n\n"
                            "### useDeferredValue\n"
                            "Возвращает отложенную версию значения:\n"
                            "```typescript\n"
                            "const deferredQuery = useDeferredValue(query);\n"
                            "```\n\n"
                            "### Suspense\n"
                            "Компонент-обёртка для асинхронной загрузки:\n"
                            "```typescript\n"
                            "<Suspense fallback={<Skeleton />}>\n"
                            "  <AsyncComponent />\n"
                            "</Suspense>\n"
                            "```\n\n"
                            "Suspense работает с: `React.lazy()`, data fetching (через кеширующие библиотеки), "
                            "и server components."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой хук позволяет пометить обновление состояния как низкоприоритетное?",
                        "options": [
                            {"id": "a", "text": "useMemo", "correct": False},
                            {"id": "b", "text": "useTransition", "correct": True},
                            {"id": "c", "text": "useEffect", "correct": False},
                            {"id": "d", "text": "useReducer", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Соберите Suspense-обёртку",
                        "description": "Расположите фрагменты для корректного использования Suspense с React.lazy.",
                        "fragments": [
                            "const LazyDashboard = React.lazy(",
                            "  () => import('./Dashboard')",
                            ");",
                            "",
                            "<Suspense fallback={<Spinner />}>",
                            "  <LazyDashboard />",
                            "</Suspense>",
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "title": "Дополните код",
                        "sentence": "const [isPending, ___hook] = useTransition();",
                        "blanks": [
                            {"id": "hook", "answer": "startTransition"},
                        ],
                    },
                ],
            },
            # Lesson 2-5
            {
                "t": "Профилирование и оптимизация",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Инструменты профилирования React",
                        "content": (
                            "## React DevTools Profiler\n\n"
                            "Profiler записывает каждый коммит и показывает:\n"
                            "- Время рендеринга каждого компонента\n"
                            "- Причину ре-рендера (state, props, hooks, parent)\n"
                            "- Flamegraph и ranked view\n\n"
                            "### Программный Profiler API\n"
                            "```typescript\n"
                            "<Profiler id='Navigation' onRender={(id, phase, actualDuration) => {\n"
                            "  console.log(`${id} ${phase}: ${actualDuration}ms`);\n"
                            "}}>\n"
                            "  <Nav />\n"
                            "</Profiler>\n"
                            "```\n\n"
                            "### why-did-you-render\n"
                            "Библиотека, которая подключается к React и логирует «ненужные» ре-рендеры — "
                            "когда компонент перерендерился с идентичными props.\n\n"
                            "### Chrome Performance Tab\n"
                            "Для низкоуровневого анализа: Layout Shift, Long Tasks, Paint timing. "
                            "Используйте `performance.mark()` и `performance.measure()` для кастомных метрик."
                        ),
                    },
                    {
                        "type": "flashcards",
                        "title": "Карточки: инструменты перформанса",
                        "cards": [
                            {"front": "React.Profiler", "back": "Компонент для измерения времени рендеринга. Принимает onRender callback с actualDuration и baseDuration."},
                            {"front": "why-did-you-render", "back": "Monkey-patches React для отслеживания ненужных ре-рендеров. Показывает prevProps vs nextProps."},
                            {"front": "Chrome Lighthouse", "back": "Аудит перформанса: FCP, LCP, TBT, CLS. Даёт оценку 0-100 и рекомендации."},
                            {"front": "React DevTools Flamegraph", "back": "Визуализация дерева компонентов с цветовой кодировкой по времени рендеринга."},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой параметр onRender callback показывает время рендеринга БЕЗ мемоизации?",
                        "options": [
                            {"id": "a", "text": "actualDuration", "correct": False},
                            {"id": "b", "text": "baseDuration", "correct": True},
                            {"id": "c", "text": "commitTime", "correct": False},
                            {"id": "d", "text": "startTime", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Кастомный хук для метрик",
                        "description": "Напишите хук `useRenderCount`, который считает количество ре-рендеров компонента (для отладки).",
                        "starterCode": (
                            "function useRenderCount(componentName: string) {\n"
                            "  // Используйте useRef для подсчёта\n"
                            "  // Логируйте в console.log при каждом рендере\n"
                            "}"
                        ),
                        "solution": (
                            "function useRenderCount(componentName: string) {\n"
                            "  const count = useRef(0);\n"
                            "  count.current++;\n"
                            "  console.log(`${componentName} rendered: ${count.current} times`);\n"
                            "}"
                        ),
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 3: State Management Architecture
    # =====================================================================
    {
        "title": "State Management Architecture",
        "pos": 2,
        "lessons": [
            {
                "t": "Flux, Redux и современные альтернативы",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Эволюция стейт-менеджмента",
                        "content": (
                            "## От Flux к современности\n\n"
                            "### Flux (2014)\n"
                            "Паттерн однонаправленного потока данных от Facebook: Action → Dispatcher → Store → View.\n\n"
                            "### Redux (2015)\n"
                            "Единый store, чистые reducer-функции, middleware для side-effects. Проблемы: boilerplate, "
                            "сложность async логики.\n\n"
                            "### Redux Toolkit (2019)\n"
                            "Официальный стандарт: `createSlice`, `createAsyncThunk`, Immer для immutable updates, "
                            "RTK Query для data fetching.\n\n"
                            "### Современные альтернативы\n"
                            "- **Zustand** — минималистичный, без провайдеров, hooks-first\n"
                            "- **Jotai** — атомарный подход, bottom-up\n"
                            "- **Recoil** — атомарный, от Meta, graph-based\n"
                            "- **Valtio** — proxy-based, мутабельный синтаксис\n"
                            "- **MobX** — observable паттерн, декораторы\n\n"
                            "Тренд: от глобального store к атомарным единицам состояния."
                        ),
                    },
                    {
                        "type": "timeline",
                        "title": "Хронология стейт-менеджеров",
                        "items": [
                            {"label": "2014", "description": "Flux — однонаправленный поток данных от Facebook"},
                            {"label": "2015", "description": "Redux — единый store, чистые reducers, Dan Abramov"},
                            {"label": "2019", "description": "Redux Toolkit — createSlice, Immer, RTK Query"},
                            {"label": "2020", "description": "Zustand, Recoil — новые подходы к стейту"},
                            {"label": "2022", "description": "Jotai v1, Valtio — атомарный и proxy подходы"},
                        ],
                    },
                    {
                        "type": "matching",
                        "title": "Сопоставьте библиотеку и подход",
                        "pairs": [
                            {"left": "Redux", "right": "Единый store + reducers"},
                            {"left": "Zustand", "right": "Hooks-first, без провайдера"},
                            {"left": "Jotai", "right": "Атомарный, bottom-up"},
                            {"left": "MobX", "right": "Observable + декораторы"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какая библиотека из перечисленных использует Proxy API для реактивности?",
                        "options": [
                            {"id": "a", "text": "Redux Toolkit", "correct": False},
                            {"id": "b", "text": "Zustand", "correct": False},
                            {"id": "c", "text": "Valtio", "correct": True},
                            {"id": "d", "text": "Jotai", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Zustand: глубокое погружение",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Zustand: архитектура и паттерны",
                        "content": (
                            "## Zustand\n\n"
                            "Zustand (~1KB) — минималистичный стейт-менеджер. Основан на subscription-паттерне "
                            "с хуками React.\n\n"
                            "### Базовое использование\n"
                            "```typescript\n"
                            "import { create } from 'zustand';\n\n"
                            "interface BearStore {\n"
                            "  bears: number;\n"
                            "  increase: () => void;\n"
                            "}\n\n"
                            "const useBearStore = create<BearStore>((set) => ({\n"
                            "  bears: 0,\n"
                            "  increase: () => set((state) => ({ bears: state.bears + 1 })),\n"
                            "}));\n"
                            "```\n\n"
                            "### Middleware\n"
                            "- `persist` — сохранение в localStorage/AsyncStorage\n"
                            "- `devtools` — интеграция с Redux DevTools\n"
                            "- `immer` — мутабельный синтаксис обновлений\n"
                            "- `subscribeWithSelector` — подписка на часть стора\n\n"
                            "### Слайсы\n"
                            "Паттерн разделения стора на модули через composition."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Создайте Zustand store",
                        "description": "Создайте стор для корзины покупок с actions: addItem, removeItem, clearCart.",
                        "starterCode": (
                            "import { create } from 'zustand';\n\n"
                            "interface CartItem { id: string; name: string; price: number; qty: number; }\n\n"
                            "interface CartStore {\n"
                            "  items: CartItem[];\n"
                            "  addItem: (item: Omit<CartItem, 'qty'>) => void;\n"
                            "  removeItem: (id: string) => void;\n"
                            "  clearCart: () => void;\n"
                            "  total: () => number;\n"
                            "}\n\n"
                            "const useCartStore = create<CartStore>((set, get) => ({\n"
                            "  // реализуйте\n"
                            "}));"
                        ),
                        "solution": (
                            "const useCartStore = create<CartStore>((set, get) => ({\n"
                            "  items: [],\n"
                            "  addItem: (item) => set((state) => {\n"
                            "    const existing = state.items.find(i => i.id === item.id);\n"
                            "    if (existing) return { items: state.items.map(i => i.id === item.id ? { ...i, qty: i.qty + 1 } : i) };\n"
                            "    return { items: [...state.items, { ...item, qty: 1 }] };\n"
                            "  }),\n"
                            "  removeItem: (id) => set((state) => ({ items: state.items.filter(i => i.id !== id) })),\n"
                            "  clearCart: () => set({ items: [] }),\n"
                            "  total: () => get().items.reduce((sum, i) => sum + i.price * i.qty, 0),\n"
                            "}));"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Как Zustand определяет, нужно ли перерендерить компонент при обновлении стора?",
                        "options": [
                            {"id": "a", "text": "Deep equality проверка всего стора", "correct": False},
                            {"id": "b", "text": "Object.is сравнение выбранного selector-ом значения", "correct": True},
                            {"id": "c", "text": "Всегда перерендеривает при любом set()", "correct": False},
                            {"id": "d", "text": "Использует React context для отслеживания", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Соберите middleware persist",
                        "description": "Расположите фрагменты для создания Zustand store с persist middleware.",
                        "fragments": [
                            "import { create } from 'zustand';",
                            "import { persist } from 'zustand/middleware';",
                            "",
                            "const useStore = create(",
                            "  persist(",
                            "    (set) => ({ count: 0, inc: () => set(s => ({ count: s.count + 1 })) }),",
                            "    { name: 'counter-storage' }",
                            "  )",
                            ");",
                        ],
                    },
                ],
            },
            {
                "t": "Серверный стейт: React Query / TanStack",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "TanStack Query (React Query)",
                        "content": (
                            "## Серверный vs клиентский стейт\n\n"
                            "Серверный стейт имеет другую природу: он принадлежит серверу, может устареть, "
                            "требует синхронизации. TanStack Query решает:\n\n"
                            "- **Кеширование** — автоматическое, с настраиваемым staleTime и gcTime\n"
                            "- **Дедупликация** — одинаковые запросы объединяются\n"
                            "- **Background refetch** — данные обновляются при фокусе окна, переподключении\n"
                            "- **Optimistic updates** — мгновенная обратная связь с откатом при ошибке\n\n"
                            "```typescript\n"
                            "const { data, isLoading, error } = useQuery({\n"
                            "  queryKey: ['users', filters],\n"
                            "  queryFn: () => api.getUsers(filters),\n"
                            "  staleTime: 5 * 60 * 1000, // 5 минут\n"
                            "});\n"
                            "```\n\n"
                            "### Мутации\n"
                            "```typescript\n"
                            "const mutation = useMutation({\n"
                            "  mutationFn: api.createUser,\n"
                            "  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['users'] }),\n"
                            "});\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Optimistic update",
                        "description": "Реализуйте optimistic update для удаления элемента из списка.",
                        "starterCode": (
                            "const deleteMutation = useMutation({\n"
                            "  mutationFn: (id: string) => api.deleteItem(id),\n"
                            "  // Добавьте onMutate для optimistic update\n"
                            "  // Добавьте onError для отката\n"
                            "  // Добавьте onSettled для рефетча\n"
                            "});"
                        ),
                        "solution": (
                            "const deleteMutation = useMutation({\n"
                            "  mutationFn: (id: string) => api.deleteItem(id),\n"
                            "  onMutate: async (id) => {\n"
                            "    await queryClient.cancelQueries({ queryKey: ['items'] });\n"
                            "    const previous = queryClient.getQueryData(['items']);\n"
                            "    queryClient.setQueryData(['items'], (old: Item[]) => old.filter(i => i.id !== id));\n"
                            "    return { previous };\n"
                            "  },\n"
                            "  onError: (err, id, context) => {\n"
                            "    queryClient.setQueryData(['items'], context?.previous);\n"
                            "  },\n"
                            "  onSettled: () => {\n"
                            "    queryClient.invalidateQueries({ queryKey: ['items'] });\n"
                            "  },\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что произойдёт если staleTime = Infinity в useQuery?",
                        "options": [
                            {"id": "a", "text": "Запрос никогда не выполнится", "correct": False},
                            {"id": "b", "text": "Данные будут считаться всегда свежими и refetch не будет автоматическим", "correct": True},
                            {"id": "c", "text": "Кеш никогда не очистится", "correct": False},
                            {"id": "d", "text": "React Query выбросит ошибку", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "queryKey в TanStack Query используется только для уникальной идентификации запроса, он не влияет на кеширование.",
                        "answer": False,
                        "explanation": "queryKey — основа кеширования. Разные queryKey = разные записи в кеше. Совпадающие queryKey = общий кеш.",
                    },
                ],
            },
            {
                "t": "Finite State Machines (XState)",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Конечные автоматы и XState",
                        "content": (
                            "## Finite State Machines\n\n"
                            "FSM — формальная модель поведения системы. Состоит из:\n"
                            "- **States** — конечное множество состояний\n"
                            "- **Events** — входные сигналы\n"
                            "- **Transitions** — функция (state, event) → nextState\n"
                            "- **Actions** — побочные эффекты при переходах\n\n"
                            "### XState\n"
                            "```typescript\n"
                            "import { createMachine, assign } from 'xstate';\n\n"
                            "const fetchMachine = createMachine({\n"
                            "  id: 'fetch',\n"
                            "  initial: 'idle',\n"
                            "  context: { data: null, error: null },\n"
                            "  states: {\n"
                            "    idle: { on: { FETCH: 'loading' } },\n"
                            "    loading: {\n"
                            "      invoke: { src: 'fetchData', onDone: 'success', onError: 'failure' },\n"
                            "    },\n"
                            "    success: { entry: assign({ data: (_, e) => e.data }) },\n"
                            "    failure: { on: { RETRY: 'loading' } },\n"
                            "  },\n"
                            "});\n"
                            "```\n\n"
                            "XState помогает избежать «невозможных состояний» (isLoading && isError одновременно)."
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Терминология FSM",
                        "pairs": [
                            {"left": "State", "right": "Текущее состояние системы в определённый момент"},
                            {"left": "Event", "right": "Внешний сигнал, вызывающий переход"},
                            {"left": "Transition", "right": "Правило перехода из одного состояния в другое"},
                            {"left": "Guard", "right": "Условие, определяющее возможность перехода"},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Машина состояний для модалки",
                        "description": "Создайте XState машину для модального окна: closed → open (с анимацией) → closing → closed.",
                        "starterCode": (
                            "const modalMachine = createMachine({\n"
                            "  id: 'modal',\n"
                            "  initial: 'closed',\n"
                            "  states: {\n"
                            "    // определите состояния и переходы\n"
                            "  },\n"
                            "});"
                        ),
                        "solution": (
                            "const modalMachine = createMachine({\n"
                            "  id: 'modal',\n"
                            "  initial: 'closed',\n"
                            "  states: {\n"
                            "    closed: { on: { OPEN: 'opening' } },\n"
                            "    opening: { after: { 300: 'open' } },\n"
                            "    open: { on: { CLOSE: 'closing' } },\n"
                            "    closing: { after: { 300: 'closed' } },\n"
                            "  },\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какое преимущество FSM перед набором boolean флагов для UI-состояний?",
                        "options": [
                            {"id": "a", "text": "FSM работает быстрее", "correct": False},
                            {"id": "b", "text": "FSM исключает невозможные комбинации состояний", "correct": True},
                            {"id": "c", "text": "FSM использует меньше памяти", "correct": False},
                            {"id": "d", "text": "FSM не требует TypeScript", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Атомарный стейт: Jotai и Recoil",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Атомарный подход к состоянию",
                        "content": (
                            "## Jotai\n\n"
                            "Jotai — атомарный стейт-менеджер. Каждый атом — минимальная единица состояния. "
                            "Компонент подписывается только на нужные атомы.\n\n"
                            "```typescript\n"
                            "import { atom, useAtom } from 'jotai';\n\n"
                            "const countAtom = atom(0);\n"
                            "const doubleAtom = atom((get) => get(countAtom) * 2); // derived\n\n"
                            "function Counter() {\n"
                            "  const [count, setCount] = useAtom(countAtom);\n"
                            "  const double = useAtomValue(doubleAtom);\n"
                            "  return <button onClick={() => setCount(c => c + 1)}>{count} ({double})</button>;\n"
                            "}\n"
                            "```\n\n"
                            "### Jotai vs Recoil\n"
                            "- Jotai: нет Provider (опционально), меньший bundle, TypeScript-first\n"
                            "- Recoil: atom families, selectors, snapshots, React DevTools интеграция\n"
                            "- Оба: атомарный подход, derived state, async atoms"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Async atom в Jotai",
                        "description": "Создайте async atom, который загружает данные пользователя и derived atom для полного имени.",
                        "starterCode": (
                            "import { atom } from 'jotai';\n\n"
                            "const userIdAtom = atom(1);\n\n"
                            "// Создайте async atom userAtom\n"
                            "// Создайте derived atom fullNameAtom"
                        ),
                        "solution": (
                            "const userAtom = atom(async (get) => {\n"
                            "  const id = get(userIdAtom);\n"
                            "  const res = await fetch(`/api/users/${id}`);\n"
                            "  return res.json();\n"
                            "});\n\n"
                            "const fullNameAtom = atom(async (get) => {\n"
                            "  const user = await get(userAtom);\n"
                            "  return `${user.firstName} ${user.lastName}`;\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой подход к управлению состоянием использует Jotai?",
                        "options": [
                            {"id": "a", "text": "Top-down (единый store)", "correct": False},
                            {"id": "b", "text": "Bottom-up (атомарный)", "correct": True},
                            {"id": "c", "text": "Proxy-based (перехват мутаций)", "correct": False},
                            {"id": "d", "text": "Observable (потоки данных)", "correct": False},
                        ],
                    },
                    {
                        "type": "category-sort",
                        "title": "Классифицируйте стейт-менеджеры",
                        "categories": [
                            {"name": "Атомарный", "items": ["Jotai", "Recoil"]},
                            {"name": "Flux/Redux-подобный", "items": ["Redux Toolkit", "Zustand"]},
                            {"name": "Proxy-based", "items": ["Valtio", "MobX"]},
                        ],
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 4: Build Systems & Tooling
    # =====================================================================
    {
        "title": "Build Systems & Tooling",
        "pos": 3,
        "lessons": [
            {
                "t": "Webpack 5 Deep Dive",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Webpack 5: внутреннее устройство",
                        "content": (
                            "## Архитектура Webpack\n\n"
                            "Webpack трансформирует граф зависимостей в бандлы. Ключевые концепции:\n\n"
                            "### Tapable и Plugin API\n"
                            "Webpack построен на системе хуков (Tapable). Каждый плагин подключается к хукам "
                            "компилятора и компиляции:\n"
                            "```javascript\n"
                            "compiler.hooks.emit.tapAsync('MyPlugin', (compilation, cb) => {\n"
                            "  // модификация ассетов перед записью на диск\n"
                            "  cb();\n"
                            "});\n"
                            "```\n\n"
                            "### Webpack 5 нововведения\n"
                            "- **Module Federation** — шаринг модулей между приложениями\n"
                            "- **Persistent Caching** — файловый кеш для ускорения повторных сборок\n"
                            "- **Asset Modules** — встроенная обработка файлов (без file-loader/url-loader)\n"
                            "- **Tree Shaking** — улучшенный анализ side effects\n\n"
                            "### Оптимизация\n"
                            "- `splitChunks` — автоматическое разделение бандлов\n"
                            "- `contenthash` — хеши для cache busting\n"
                            "- `sideEffects: false` — агрессивный tree shaking"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой тип хеша Webpack гарантирует изменение только при изменении содержимого файла?",
                        "options": [
                            {"id": "a", "text": "[hash]", "correct": False},
                            {"id": "b", "text": "[chunkhash]", "correct": False},
                            {"id": "c", "text": "[contenthash]", "correct": True},
                            {"id": "d", "text": "[fullhash]", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Настройка splitChunks",
                        "description": "Настройте optimization.splitChunks для разделения vendor-кода и общих модулей.",
                        "starterCode": (
                            "module.exports = {\n"
                            "  optimization: {\n"
                            "    splitChunks: {\n"
                            "      // настройте cacheGroups для vendor и common\n"
                            "    },\n"
                            "  },\n"
                            "};"
                        ),
                        "solution": (
                            "module.exports = {\n"
                            "  optimization: {\n"
                            "    splitChunks: {\n"
                            "      chunks: 'all',\n"
                            "      cacheGroups: {\n"
                            "        vendor: {\n"
                            "          test: /[\\\\/]node_modules[\\\\/]/,\n"
                            "          name: 'vendors',\n"
                            "          chunks: 'all',\n"
                            "        },\n"
                            "        common: {\n"
                            "          minChunks: 2,\n"
                            "          priority: -10,\n"
                            "          reuseExistingChunk: true,\n"
                            "        },\n"
                            "      },\n"
                            "    },\n"
                            "  },\n"
                            "};"
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Webpack концепции",
                        "pairs": [
                            {"left": "Loader", "right": "Трансформирует отдельные файлы (ts → js, scss → css)"},
                            {"left": "Plugin", "right": "Работает на уровне всей компиляции (минификация, HTML генерация)"},
                            {"left": "Entry", "right": "Точка входа для построения графа зависимостей"},
                            {"left": "Chunk", "right": "Группа модулей, объединённых в один файл"},
                        ],
                    },
                ],
            },
            {
                "t": "Vite и Rollup",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Vite: архитектура и преимущества",
                        "content": (
                            "## Vite\n\n"
                            "Vite использует двухступенчатую архитектуру:\n\n"
                            "### Dev Server (ESBuild)\n"
                            "- **Native ESM** — браузер загружает модули по отдельности\n"
                            "- **ESBuild** для трансформации (10-100x быстрее Babel)\n"
                            "- **HMR** через WebSocket с мгновенным обновлением\n"
                            "- Зависимости pre-bundled с ESBuild (node_modules → ESM)\n\n"
                            "### Production Build (Rollup)\n"
                            "- **Rollup** для tree shaking и оптимизации\n"
                            "- Автоматический code splitting\n"
                            "- CSS extraction и минификация\n"
                            "- Asset hashing и compression\n\n"
                            "### Rollup Plugin API\n"
                            "Vite совместим с большинством Rollup плагинов. Добавляет свои хуки:\n"
                            "- `configureServer` — кастомный middleware для dev server\n"
                            "- `transformIndexHtml` — модификация HTML\n"
                            "- `handleHotUpdate` — кастомная логика HMR"
                        ),
                    },
                    {
                        "type": "true-false",
                        "statement": "Vite использует ESBuild для production бандлинга по умолчанию.",
                        "answer": False,
                        "explanation": "Vite использует ESBuild только для dev-трансформации и pre-bundling зависимостей. Production build выполняется Rollup.",
                    },
                    {
                        "type": "quiz",
                        "question": "Почему Vite dev server быстрее Webpack dev server?",
                        "options": [
                            {"id": "a", "text": "Vite использует Go вместо JavaScript", "correct": False},
                            {"id": "b", "text": "Vite не бандлит исходный код в dev-режиме, используя native ESM", "correct": True},
                            {"id": "c", "text": "Vite работает только с TypeScript", "correct": False},
                            {"id": "d", "text": "Vite кеширует всё в RAM", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Vite plugin",
                        "description": "Соберите минимальный Vite плагин, который добавляет виртуальный модуль.",
                        "fragments": [
                            "export default function myPlugin() {",
                            "  const virtualModuleId = 'virtual:my-module';",
                            "  const resolvedVirtualModuleId = '\\0' + virtualModuleId;",
                            "  return {",
                            "    name: 'my-plugin',",
                            "    resolveId(id) { if (id === virtualModuleId) return resolvedVirtualModuleId; },",
                            "    load(id) { if (id === resolvedVirtualModuleId) return 'export const msg = \"hello\"'; },",
                            "  };",
                            "}",
                        ],
                    },
                ],
            },
            {
                "t": "Module Federation",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Module Federation",
                        "content": (
                            "## Module Federation (Webpack 5)\n\n"
                            "Module Federation позволяет нескольким независимым приложениям шарить модули в рантайме. "
                            "Это основа микрофронтенд-архитектуры.\n\n"
                            "### Концепции\n"
                            "- **Host** — приложение, потребляющее remote модули\n"
                            "- **Remote** — приложение, экспортирующее модули\n"
                            "- **Shared** — общие зависимости (React, lodash)\n\n"
                            "```javascript\n"
                            "// Remote (app2)\n"
                            "new ModuleFederationPlugin({\n"
                            "  name: 'app2',\n"
                            "  filename: 'remoteEntry.js',\n"
                            "  exposes: { './Button': './src/Button' },\n"
                            "  shared: { react: { singleton: true } },\n"
                            "});\n\n"
                            "// Host (app1)\n"
                            "new ModuleFederationPlugin({\n"
                            "  name: 'app1',\n"
                            "  remotes: { app2: 'app2@http://localhost:3002/remoteEntry.js' },\n"
                            "  shared: { react: { singleton: true } },\n"
                            "});\n"
                            "```\n\n"
                            "Ключевой параметр `singleton: true` гарантирует одну копию React в памяти."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что произойдёт если два federated приложения используют разные major-версии React без singleton?",
                        "options": [
                            {"id": "a", "text": "Webpack автоматически выберет последнюю версию", "correct": False},
                            {"id": "b", "text": "Каждое приложение загрузит свою копию React, что приведёт к конфликтам хуков", "correct": True},
                            {"id": "c", "text": "Сборка упадёт с ошибкой", "correct": False},
                            {"id": "d", "text": "React обнаружит конфликт и предупредит в консоли", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Динамическая загрузка remote",
                        "description": "Реализуйте динамическую загрузку remote компонента с обработкой ошибок.",
                        "starterCode": (
                            "// Загрузите компонент 'Header' из remote 'app2'\n"
                            "// Оберните в ErrorBoundary и Suspense\n"
                            "const RemoteHeader = React.lazy(() => {\n"
                            "  // ваш код\n"
                            "});"
                        ),
                        "solution": (
                            "const RemoteHeader = React.lazy(() =>\n"
                            "  import('app2/Header').catch(() => ({\n"
                            "    default: () => <div>Header unavailable</div>\n"
                            "  }))\n"
                            ");\n\n"
                            "function App() {\n"
                            "  return (\n"
                            "    <ErrorBoundary fallback={<div>Error</div>}>\n"
                            "      <Suspense fallback={<div>Loading...</div>}>\n"
                            "        <RemoteHeader />\n"
                            "      </Suspense>\n"
                            "    </ErrorBoundary>\n"
                            "  );\n"
                            "}"
                        ),
                    },
                    {
                        "type": "fill-blank",
                        "title": "Дополните конфигурацию",
                        "sentence": "new ModuleFederationPlugin({ name: 'shell', ___prop: { dashboard: 'dashboard@http://cdn.example.com/___file' } });",
                        "blanks": [
                            {"id": "prop", "answer": "remotes"},
                            {"id": "file", "answer": "remoteEntry.js"},
                        ],
                    },
                ],
            },
            {
                "t": "Монорепо: Turborepo и Nx",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Монорепо инструменты",
                        "content": (
                            "## Монорепо\n\n"
                            "Монорепо — единый репозиторий для множества пакетов/приложений. Преимущества:\n"
                            "- Общий код без npm publish\n"
                            "- Единые линтер/тесты/CI конфигурации\n"
                            "- Atomic commits\n\n"
                            "### Turborepo\n"
                            "- **Task orchestration** — параллельный запуск задач с учётом зависимостей\n"
                            "- **Remote caching** — кеш CI артефактов в облаке\n"
                            "- **Pipeline** — декларативное описание зависимостей задач\n"
                            "```json\n"
                            "{ \"pipeline\": {\n"
                            "    \"build\": { \"dependsOn\": [\"^build\"], \"outputs\": [\"dist/**\"] },\n"
                            "    \"test\": { \"dependsOn\": [\"build\"] },\n"
                            "    \"lint\": {}\n"
                            "} }\n"
                            "```\n\n"
                            "### Nx\n"
                            "- **Computation caching** + **affected** — запуск только затронутых проектов\n"
                            "- **Генераторы** — scaffolding компонентов, библиотек\n"
                            "- **Module boundary** — правила зависимостей между пакетами\n"
                            "- **Плагины** — React, Angular, Node, Next.js"
                        ),
                    },
                    {
                        "type": "category-sort",
                        "title": "Возможности Turborepo vs Nx",
                        "categories": [
                            {"name": "Turborepo", "items": ["Простой pipeline DSL", "Remote caching", "Минимальная конфигурация"]},
                            {"name": "Nx", "items": ["Генераторы кода", "Module boundary rules", "Визуализация графа зависимостей"]},
                            {"name": "Оба", "items": ["Параллельный запуск задач", "Инкрементальные билды"]},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Что делает команда `turbo run build --filter=web...` (с тремя точками)?",
                        "options": [
                            {"id": "a", "text": "Собирает только пакет web", "correct": False},
                            {"id": "b", "text": "Собирает web и все его зависимости", "correct": True},
                            {"id": "c", "text": "Собирает все пакеты кроме web", "correct": False},
                            {"id": "d", "text": "Собирает web и все пакеты, зависящие от web", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Как называется механизм Nx, который запускает задачи только для изменённых проектов?",
                        "answer": "affected",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 5: Testing Strategies
    # =====================================================================
    {
        "title": "Testing Strategies",
        "pos": 4,
        "lessons": [
            {
                "t": "Пирамида тестирования",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Стратегии тестирования фронтенда",
                        "content": (
                            "## Пирамида тестирования\n\n"
                            "Классическая модель от Mike Cohn (снизу вверх):\n\n"
                            "1. **Unit тесты** (основа) — быстрые, изолированные, тестируют функции и хуки\n"
                            "2. **Integration тесты** — тестируют взаимодействие компонентов\n"
                            "3. **E2E тесты** (вершина) — полный пользовательский сценарий\n\n"
                            "### Testing Trophy (Kent C. Dodds)\n"
                            "Альтернативная модель для фронтенда:\n"
                            "- **Static** — TypeScript, ESLint\n"
                            "- **Unit** — чистые функции, утилиты\n"
                            "- **Integration** (основа!) — компоненты с моками API\n"
                            "- **E2E** — критические пользовательские пути\n\n"
                            "Ключевой принцип: «Чем больше тесты напоминают реальное использование, "
                            "тем больше уверенности они дают.»\n\n"
                            "### Соотношение для фронтенда\n"
                            "- 50% integration (React Testing Library)\n"
                            "- 30% unit (Vitest/Jest)\n"
                            "- 15% E2E (Playwright/Cypress)\n"
                            "- 5% visual regression"
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Тип теста → Инструмент",
                        "pairs": [
                            {"left": "Unit тесты", "right": "Vitest, Jest"},
                            {"left": "Компонентные тесты", "right": "React Testing Library"},
                            {"left": "E2E тесты", "right": "Playwright, Cypress"},
                            {"left": "Visual regression", "right": "Chromatic, Percy"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Согласно Testing Trophy от Kent C. Dodds, на каком уровне должно быть больше всего тестов для фронтенда?",
                        "options": [
                            {"id": "a", "text": "Unit", "correct": False},
                            {"id": "b", "text": "Integration", "correct": True},
                            {"id": "c", "text": "E2E", "correct": False},
                            {"id": "d", "text": "Static analysis", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Моки (mocks) в тестах всегда лучше реальных зависимостей, так как делают тесты быстрее.",
                        "answer": False,
                        "explanation": "Чрезмерное использование моков снижает уверенность в тестах. Integration-тесты с минимальным мокингом ценнее.",
                    },
                ],
            },
            {
                "t": "Unit тесты с Vitest",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Vitest: современный test runner",
                        "content": (
                            "## Vitest\n\n"
                            "Vitest — test runner от команды Vite. Преимущества:\n"
                            "- Нативная поддержка ESM, TypeScript, JSX\n"
                            "- Общая конфигурация с Vite (трансформеры, resolve aliases)\n"
                            "- Jest-совместимый API\n"
                            "- In-source testing (тесты в том же файле)\n"
                            "- Snapshot тесты\n\n"
                            "```typescript\n"
                            "import { describe, it, expect, vi } from 'vitest';\n\n"
                            "describe('formatPrice', () => {\n"
                            "  it('formats cents to dollars', () => {\n"
                            "    expect(formatPrice(1999)).toBe('$19.99');\n"
                            "  });\n\n"
                            "  it('handles zero', () => {\n"
                            "    expect(formatPrice(0)).toBe('$0.00');\n"
                            "  });\n"
                            "});\n"
                            "```\n\n"
                            "### Моки\n"
                            "```typescript\n"
                            "const fetchMock = vi.fn().mockResolvedValue({ ok: true, json: () => ({ id: 1 }) });\n"
                            "vi.stubGlobal('fetch', fetchMock);\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Напишите unit тест",
                        "description": "Напишите тест для функции `debounce`, проверяющий, что функция вызывается только через заданную задержку.",
                        "starterCode": (
                            "import { describe, it, expect, vi } from 'vitest';\n"
                            "import { debounce } from './utils';\n\n"
                            "describe('debounce', () => {\n"
                            "  // Напишите тесты:\n"
                            "  // 1. Функция не вызывается сразу\n"
                            "  // 2. Функция вызывается после задержки\n"
                            "  // 3. Повторный вызов сбрасывает таймер\n"
                            "});"
                        ),
                        "solution": (
                            "describe('debounce', () => {\n"
                            "  beforeEach(() => vi.useFakeTimers());\n"
                            "  afterEach(() => vi.useRealTimers());\n\n"
                            "  it('does not call immediately', () => {\n"
                            "    const fn = vi.fn();\n"
                            "    const debounced = debounce(fn, 300);\n"
                            "    debounced();\n"
                            "    expect(fn).not.toHaveBeenCalled();\n"
                            "  });\n\n"
                            "  it('calls after delay', () => {\n"
                            "    const fn = vi.fn();\n"
                            "    const debounced = debounce(fn, 300);\n"
                            "    debounced();\n"
                            "    vi.advanceTimersByTime(300);\n"
                            "    expect(fn).toHaveBeenCalledOnce();\n"
                            "  });\n\n"
                            "  it('resets timer on repeated calls', () => {\n"
                            "    const fn = vi.fn();\n"
                            "    const debounced = debounce(fn, 300);\n"
                            "    debounced();\n"
                            "    vi.advanceTimersByTime(200);\n"
                            "    debounced();\n"
                            "    vi.advanceTimersByTime(200);\n"
                            "    expect(fn).not.toHaveBeenCalled();\n"
                            "    vi.advanceTimersByTime(100);\n"
                            "    expect(fn).toHaveBeenCalledOnce();\n"
                            "  });\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какая функция Vitest позволяет контролировать течение времени в тестах?",
                        "options": [
                            {"id": "a", "text": "vi.mockTime()", "correct": False},
                            {"id": "b", "text": "vi.useFakeTimers()", "correct": True},
                            {"id": "c", "text": "vi.freezeTime()", "correct": False},
                            {"id": "d", "text": "vi.controlTime()", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Соберите мок модуля",
                        "description": "Расположите фрагменты для мокирования модуля axios в Vitest.",
                        "fragments": [
                            "vi.mock('axios', () => ({",
                            "  default: {",
                            "    get: vi.fn(),",
                            "    post: vi.fn(),",
                            "  },",
                            "}));",
                        ],
                    },
                ],
            },
            {
                "t": "Компонентные тесты: Testing Library",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "React Testing Library",
                        "content": (
                            "## Философия Testing Library\n\n"
                            "«The more your tests resemble the way your software is used, the more confidence they give you.»\n\n"
                            "### Принципы\n"
                            "- Тестируйте поведение, не реализацию\n"
                            "- Используйте доступные запросы (getByRole, getByLabelText)\n"
                            "- Не тестируйте implementation details (state, lifecycle)\n\n"
                            "### Приоритет запросов\n"
                            "1. `getByRole` — лучший выбор (ARIA роли)\n"
                            "2. `getByLabelText` — для форм\n"
                            "3. `getByPlaceholderText` — fallback для инпутов\n"
                            "4. `getByText` — для статического текста\n"
                            "5. `getByTestId` — последний resort\n\n"
                            "```typescript\n"
                            "import { render, screen, userEvent } from '@testing-library/react';\n\n"
                            "test('submits form with user data', async () => {\n"
                            "  const user = userEvent.setup();\n"
                            "  render(<LoginForm onSubmit={handleSubmit} />);\n"
                            "  await user.type(screen.getByLabelText('Email'), 'test@mail.com');\n"
                            "  await user.click(screen.getByRole('button', { name: /войти/i }));\n"
                            "  expect(handleSubmit).toHaveBeenCalledWith({ email: 'test@mail.com' });\n"
                            "});\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Тест компонента поиска",
                        "description": "Напишите тест для компонента SearchBar, проверяющий debounce-логику поиска.",
                        "starterCode": (
                            "test('calls onSearch after debounce', async () => {\n"
                            "  const onSearch = vi.fn();\n"
                            "  const user = userEvent.setup();\n"
                            "  render(<SearchBar onSearch={onSearch} debounceMs={300} />);\n"
                            "  \n"
                            "  // Напишите тест:\n"
                            "  // 1. Введите текст в поле поиска\n"
                            "  // 2. Проверьте что onSearch ещё не вызван\n"
                            "  // 3. Дождитесь debounce\n"
                            "  // 4. Проверьте вызов с правильным значением\n"
                            "});"
                        ),
                        "solution": (
                            "test('calls onSearch after debounce', async () => {\n"
                            "  vi.useFakeTimers();\n"
                            "  const onSearch = vi.fn();\n"
                            "  const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime });\n"
                            "  render(<SearchBar onSearch={onSearch} debounceMs={300} />);\n"
                            "  \n"
                            "  await user.type(screen.getByRole('searchbox'), 'react');\n"
                            "  expect(onSearch).not.toHaveBeenCalled();\n"
                            "  \n"
                            "  act(() => vi.advanceTimersByTime(300));\n"
                            "  expect(onSearch).toHaveBeenCalledWith('react');\n"
                            "  vi.useRealTimers();\n"
                            "});"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Почему getByRole предпочтительнее getByTestId в React Testing Library?",
                        "options": [
                            {"id": "a", "text": "getByRole работает быстрее", "correct": False},
                            {"id": "b", "text": "getByRole тестирует доступность и отражает восприятие пользователем", "correct": True},
                            {"id": "c", "text": "getByTestId не работает с React 18", "correct": False},
                            {"id": "d", "text": "getByRole не требует обновления при рефакторинге", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "title": "Дополните тест",
                        "sentence": "const button = screen.___method('button', { name: /submit/i });",
                        "blanks": [
                            {"id": "method", "answer": "getByRole"},
                        ],
                    },
                ],
            },
            {
                "t": "E2E: Playwright",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Playwright для E2E тестирования",
                        "content": (
                            "## Playwright\n\n"
                            "Playwright от Microsoft — E2E фреймворк для тестирования веб-приложений. "
                            "Поддерживает Chromium, Firefox, WebKit.\n\n"
                            "### Преимущества перед Cypress\n"
                            "- Multi-browser из коробки\n"
                            "- Auto-wait (не нужен cy.wait)\n"
                            "- Несколько вкладок/окон\n"
                            "- Network interception\n"
                            "- Параллельное выполнение\n\n"
                            "```typescript\n"
                            "import { test, expect } from '@playwright/test';\n\n"
                            "test('user can login', async ({ page }) => {\n"
                            "  await page.goto('/login');\n"
                            "  await page.getByLabel('Email').fill('user@test.com');\n"
                            "  await page.getByLabel('Password').fill('secret');\n"
                            "  await page.getByRole('button', { name: 'Sign in' }).click();\n"
                            "  await expect(page.getByText('Dashboard')).toBeVisible();\n"
                            "});\n"
                            "```\n\n"
                            "### Page Object Model\n"
                            "Паттерн для организации E2E тестов: каждая страница — класс с методами."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Page Object Model",
                        "description": "Реализуйте Page Object для страницы логина с методами login() и getErrorMessage().",
                        "starterCode": (
                            "import { Page, Locator } from '@playwright/test';\n\n"
                            "export class LoginPage {\n"
                            "  // Определите locators и методы\n"
                            "  constructor(private page: Page) {}\n"
                            "}"
                        ),
                        "solution": (
                            "export class LoginPage {\n"
                            "  private emailInput: Locator;\n"
                            "  private passwordInput: Locator;\n"
                            "  private submitButton: Locator;\n"
                            "  private errorAlert: Locator;\n\n"
                            "  constructor(private page: Page) {\n"
                            "    this.emailInput = page.getByLabel('Email');\n"
                            "    this.passwordInput = page.getByLabel('Password');\n"
                            "    this.submitButton = page.getByRole('button', { name: 'Sign in' });\n"
                            "    this.errorAlert = page.getByRole('alert');\n"
                            "  }\n\n"
                            "  async login(email: string, password: string) {\n"
                            "    await this.emailInput.fill(email);\n"
                            "    await this.passwordInput.fill(password);\n"
                            "    await this.submitButton.click();\n"
                            "  }\n\n"
                            "  async getErrorMessage() {\n"
                            "    return this.errorAlert.textContent();\n"
                            "  }\n"
                            "}"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Как Playwright решает проблему flaky тестов с ожиданием элементов?",
                        "options": [
                            {"id": "a", "text": "Фиксированные sleep() перед каждым действием", "correct": False},
                            {"id": "b", "text": "Auto-wait: автоматическое ожидание actionability элемента", "correct": True},
                            {"id": "c", "text": "Retry всего теста при неудаче", "correct": False},
                            {"id": "d", "text": "Снижение скорости выполнения", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Как называется паттерн организации E2E тестов, где каждая страница описана классом с методами?",
                        "answer": "Page Object Model",
                    },
                ],
            },
            {
                "t": "Visual Regression Testing",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Визуальное регрессионное тестирование",
                        "content": (
                            "## Visual Regression Testing\n\n"
                            "Визуальные тесты сравнивают скриншоты UI с эталонными изображениями, "
                            "выявляя непреднамеренные визуальные изменения.\n\n"
                            "### Инструменты\n"
                            "- **Chromatic** — облачный сервис для Storybook, попиксельное сравнение\n"
                            "- **Percy (BrowserStack)** — кросс-браузерные visual diffs\n"
                            "- **Playwright visual comparisons** — встроенный `toHaveScreenshot()`\n"
                            "- **Storybook test runner** — snapshot + interaction тесты\n\n"
                            "### Playwright скриншоты\n"
                            "```typescript\n"
                            "test('homepage visual', async ({ page }) => {\n"
                            "  await page.goto('/');\n"
                            "  await expect(page).toHaveScreenshot('homepage.png', {\n"
                            "    maxDiffPixelRatio: 0.01,\n"
                            "    animations: 'disabled',\n"
                            "  });\n"
                            "});\n"
                            "```\n\n"
                            "### Лучшие практики\n"
                            "- Отключайте анимации при скриншотировании\n"
                            "- Мокайте динамические данные (даты, аватары)\n"
                            "- Тестируйте компоненты изолированно в Storybook"
                        ),
                    },
                    {
                        "type": "flashcards",
                        "title": "Инструменты визуального тестирования",
                        "cards": [
                            {"front": "Chromatic", "back": "Cloud-сервис для Storybook. Автоматически скриншотит все stories и сравнивает с baseline."},
                            {"front": "Percy", "back": "Кросс-браузерный visual testing от BrowserStack. Интегрируется с Cypress, Playwright, Storybook."},
                            {"front": "toHaveScreenshot()", "back": "Встроенный метод Playwright для попиксельного сравнения скриншотов с эталонами."},
                            {"front": "Storybook", "back": "Среда для разработки UI компонентов изолированно. Основа для visual regression testing."},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Почему важно отключать CSS анимации при визуальном тестировании?",
                        "options": [
                            {"id": "a", "text": "Анимации замедляют тесты", "correct": False},
                            {"id": "b", "text": "Скриншот может быть сделан в середине анимации, давая ложное diff", "correct": True},
                            {"id": "c", "text": "Playwright не поддерживает анимации", "correct": False},
                            {"id": "d", "text": "Анимации не работают в headless режиме", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Visual regression тесты могут полностью заменить unit и integration тесты.",
                        "answer": False,
                        "explanation": "Visual тесты проверяют только внешний вид. Они не покрывают логику, edge cases и взаимодействие с API.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 6: Web Performance
    # =====================================================================
    {
        "title": "Web Performance",
        "pos": 5,
        "lessons": [
            {
                "t": "Core Web Vitals",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Core Web Vitals",
                        "content": (
                            "## Core Web Vitals (2024)\n\n"
                            "Google использует три метрики для оценки пользовательского опыта:\n\n"
                            "### LCP (Largest Contentful Paint)\n"
                            "Время отрисовки самого крупного видимого элемента. Цель: < 2.5с.\n"
                            "Влияющие факторы: серверное время, CSS blocking, загрузка изображений.\n\n"
                            "### INP (Interaction to Next Paint)\n"
                            "Заменил FID в 2024. Измеряет задержку ВСЕХ взаимодействий, а не только первого. Цель: < 200мс.\n"
                            "Влияющие факторы: тяжёлые JS-обработчики, long tasks, layout thrashing.\n\n"
                            "### CLS (Cumulative Layout Shift)\n"
                            "Суммарный сдвиг макета без действия пользователя. Цель: < 0.1.\n"
                            "Причины: изображения без размеров, динамический контент, web fonts.\n\n"
                            "### Измерение\n"
                            "```typescript\n"
                            "import { onLCP, onINP, onCLS } from 'web-vitals';\n"
                            "onLCP(metric => sendToAnalytics(metric));\n"
                            "```"
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Метрика → Что измеряет",
                        "pairs": [
                            {"left": "LCP", "right": "Время загрузки основного контента"},
                            {"left": "INP", "right": "Задержка при взаимодействии пользователя"},
                            {"left": "CLS", "right": "Визуальная стабильность макета"},
                            {"left": "TTFB", "right": "Время до первого байта от сервера"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какая метрика заменила First Input Delay (FID) в Core Web Vitals в 2024 году?",
                        "options": [
                            {"id": "a", "text": "TBT (Total Blocking Time)", "correct": False},
                            {"id": "b", "text": "INP (Interaction to Next Paint)", "correct": True},
                            {"id": "c", "text": "FCP (First Contentful Paint)", "correct": False},
                            {"id": "d", "text": "TTI (Time to Interactive)", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "CLS учитывает сдвиги макета, вызванные кликом пользователя.",
                        "answer": False,
                        "explanation": "CLS учитывает только неожиданные сдвиги. Сдвиги в течение 500мс после user input исключаются.",
                    },
                ],
            },
            {
                "t": "Critical Rendering Path",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Критический путь рендеринга",
                        "content": (
                            "## Critical Rendering Path\n\n"
                            "Последовательность шагов от получения HTML до отрисовки пикселей:\n\n"
                            "1. **HTML Parsing** → DOM Tree\n"
                            "2. **CSS Parsing** → CSSOM Tree\n"
                            "3. **JavaScript** — может блокировать parsing (если не defer/async)\n"
                            "4. **Render Tree** = DOM + CSSOM (только видимые элементы)\n"
                            "5. **Layout** — вычисление геометрии (позиция, размеры)\n"
                            "6. **Paint** — растеризация в пиксели\n"
                            "7. **Composite** — объединение слоёв (GPU)\n\n"
                            "### Оптимизации\n"
                            "- **Inline critical CSS** — встроить CSS для above-the-fold контента\n"
                            "- **defer/async скрипты** — не блокировать парсинг HTML\n"
                            "- **Preload/Prefetch** — `<link rel=\"preload\">` для критических ресурсов\n"
                            "- **Font display: swap** — показывать fallback шрифт до загрузки кастомного\n"
                            "- **Avoid layout thrashing** — batch DOM reads/writes"
                        ),
                    },
                    {
                        "type": "timeline",
                        "title": "Этапы Critical Rendering Path",
                        "items": [
                            {"label": "HTML Parsing", "description": "Браузер парсит HTML и строит DOM Tree"},
                            {"label": "CSS Parsing", "description": "Параллельно строится CSSOM из CSS-файлов"},
                            {"label": "JavaScript", "description": "Выполнение скриптов (может блокировать parsing)"},
                            {"label": "Render Tree", "description": "Объединение DOM + CSSOM, исключение display:none"},
                            {"label": "Layout → Paint → Composite", "description": "Вычисление геометрии, растеризация, GPU композитинг"},
                        ],
                    },
                    {
                        "type": "drag-order",
                        "title": "Порядок этапов рендеринга",
                        "description": "Расположите этапы в правильном порядке.",
                        "items": [
                            {"id": "1", "text": "HTML Parsing → DOM"},
                            {"id": "2", "text": "CSS Parsing → CSSOM"},
                            {"id": "3", "text": "Render Tree Construction"},
                            {"id": "4", "text": "Layout (Reflow)"},
                            {"id": "5", "text": "Paint"},
                            {"id": "6", "text": "Composite"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой атрибут `<script>` позволяет скрипту загружаться параллельно и выполняться после парсинга HTML?",
                        "options": [
                            {"id": "a", "text": "async", "correct": False},
                            {"id": "b", "text": "defer", "correct": True},
                            {"id": "c", "text": "module", "correct": False},
                            {"id": "d", "text": "lazy", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Code Splitting и Lazy Loading",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Code Splitting стратегии",
                        "content": (
                            "## Code Splitting\n\n"
                            "Разделение бандла на части, загружаемые по требованию.\n\n"
                            "### Route-based splitting\n"
                            "```typescript\n"
                            "const Dashboard = React.lazy(() => import('./pages/Dashboard'));\n"
                            "const Settings = React.lazy(() => import('./pages/Settings'));\n\n"
                            "<Routes>\n"
                            "  <Route path='/dashboard' element={\n"
                            "    <Suspense fallback={<Skeleton />}><Dashboard /></Suspense>\n"
                            "  } />\n"
                            "</Routes>\n"
                            "```\n\n"
                            "### Component-level splitting\n"
                            "Тяжёлые компоненты (графики, редакторы): `React.lazy(() => import('./Chart'))`\n\n"
                            "### Library splitting\n"
                            "Загрузка тяжёлых библиотек по требованию:\n"
                            "```typescript\n"
                            "const handleExport = async () => {\n"
                            "  const xlsx = await import('xlsx');\n"
                            "  xlsx.writeFile(data, 'export.xlsx');\n"
                            "};\n"
                            "```\n\n"
                            "### Prefetching\n"
                            "```typescript\n"
                            "// Webpack magic comment\n"
                            "const Settings = React.lazy(() => import(/* webpackPrefetch: true */ './Settings'));\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Lazy loading с prefetch on hover",
                        "description": "Реализуйте компонент навигации, который предзагружает страницу при наведении мыши.",
                        "starterCode": (
                            "const importMap = {\n"
                            "  dashboard: () => import('./Dashboard'),\n"
                            "  settings: () => import('./Settings'),\n"
                            "};\n\n"
                            "function NavLink({ to, children }) {\n"
                            "  // Реализуйте prefetch on hover\n"
                            "}"
                        ),
                        "solution": (
                            "function NavLink({ to, children }) {\n"
                            "  const handleMouseEnter = () => {\n"
                            "    importMap[to]?.(); // triggers dynamic import = prefetch\n"
                            "  };\n"
                            "  return (\n"
                            "    <Link to={`/${to}`} onMouseEnter={handleMouseEnter}>\n"
                            "      {children}\n"
                            "    </Link>\n"
                            "  );\n"
                            "}"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Чем отличается `prefetch` от `preload` для ресурсов?",
                        "options": [
                            {"id": "a", "text": "prefetch — низкий приоритет (для будущей навигации), preload — высокий (нужен на текущей странице)", "correct": True},
                            {"id": "b", "text": "prefetch загружает быстрее", "correct": False},
                            {"id": "c", "text": "preload работает только для скриптов", "correct": False},
                            {"id": "d", "text": "Они идентичны", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Intersection Observer lazy loading",
                        "description": "Соберите код для ленивой загрузки изображений через Intersection Observer.",
                        "fragments": [
                            "const observer = new IntersectionObserver((entries) => {",
                            "  entries.forEach(entry => {",
                            "    if (entry.isIntersecting) {",
                            "      const img = entry.target as HTMLImageElement;",
                            "      img.src = img.dataset.src!;",
                            "      observer.unobserve(img);",
                            "    }",
                            "  });",
                            "});",
                        ],
                    },
                ],
            },
            {
                "t": "Service Workers и Caching",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Service Workers и стратегии кеширования",
                        "content": (
                            "## Service Workers\n\n"
                            "Service Worker — скрипт-посредник между браузером и сетью. Работает в отдельном потоке, "
                            "перехватывает fetch-запросы, управляет кешем.\n\n"
                            "### Жизненный цикл\n"
                            "1. **Registration** — `navigator.serviceWorker.register('/sw.js')`\n"
                            "2. **Installation** — событие `install`, кеширование статических ресурсов\n"
                            "3. **Activation** — событие `activate`, очистка старых кешей\n"
                            "4. **Fetch** — перехват сетевых запросов\n\n"
                            "### Стратегии кеширования (Workbox)\n"
                            "- **Cache First** — сначала кеш, потом сеть (для статики: CSS, JS, изображения)\n"
                            "- **Network First** — сначала сеть, fallback на кеш (для API, HTML)\n"
                            "- **Stale While Revalidate** — кеш + фоновое обновление (баланс скорости и свежести)\n"
                            "- **Network Only** — всегда сеть (для аналитики, POST запросов)\n"
                            "- **Cache Only** — только кеш (для pre-cached ресурсов)\n\n"
                            "### Workbox\n"
                            "Библиотека от Google для упрощения работы с Service Workers."
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Настройка Workbox стратегий",
                        "description": "Настройте Workbox routing для разных типов ресурсов.",
                        "starterCode": (
                            "import { registerRoute } from 'workbox-routing';\n"
                            "import { CacheFirst, NetworkFirst, StaleWhileRevalidate } from 'workbox-strategies';\n\n"
                            "// Настройте стратегии для:\n"
                            "// 1. Статические ассеты (images, fonts) → CacheFirst\n"
                            "// 2. API запросы → NetworkFirst\n"
                            "// 3. CSS/JS файлы → StaleWhileRevalidate"
                        ),
                        "solution": (
                            "registerRoute(\n"
                            "  ({ request }) => request.destination === 'image' || request.destination === 'font',\n"
                            "  new CacheFirst({ cacheName: 'assets', expiration: { maxEntries: 100, maxAgeSeconds: 30 * 24 * 60 * 60 } })\n"
                            ");\n\n"
                            "registerRoute(\n"
                            "  ({ url }) => url.pathname.startsWith('/api'),\n"
                            "  new NetworkFirst({ cacheName: 'api', networkTimeoutSeconds: 5 })\n"
                            ");\n\n"
                            "registerRoute(\n"
                            "  ({ request }) => request.destination === 'style' || request.destination === 'script',\n"
                            "  new StaleWhileRevalidate({ cacheName: 'static-resources' })\n"
                            ");"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какая стратегия Workbox лучше всего подходит для API-ответов, которые должны быть свежими, но с offline-fallback?",
                        "options": [
                            {"id": "a", "text": "Cache First", "correct": False},
                            {"id": "b", "text": "Network First", "correct": True},
                            {"id": "c", "text": "Cache Only", "correct": False},
                            {"id": "d", "text": "Stale While Revalidate", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "title": "Регистрация Service Worker",
                        "sentence": "navigator.___obj.register('/sw.js').then(reg => console.log('SW registered:', reg.scope));",
                        "blanks": [
                            {"id": "obj", "answer": "serviceWorker"},
                        ],
                    },
                ],
            },
            {
                "t": "Image Optimization",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Оптимизация изображений",
                        "content": (
                            "## Форматы изображений\n\n"
                            "- **WebP** — на 25-35% меньше JPEG/PNG, поддержка прозрачности, 97% браузеров\n"
                            "- **AVIF** — на 50% меньше JPEG, лучшее качество, ~93% браузеров\n"
                            "- **SVG** — для иконок и иллюстраций (векторный)\n\n"
                            "### Responsive Images\n"
                            "```html\n"
                            "<picture>\n"
                            "  <source srcset='hero.avif' type='image/avif' />\n"
                            "  <source srcset='hero.webp' type='image/webp' />\n"
                            "  <img src='hero.jpg' alt='Hero' loading='lazy'\n"
                            "       width='800' height='400'\n"
                            "       srcset='hero-400.jpg 400w, hero-800.jpg 800w'\n"
                            "       sizes='(max-width: 600px) 400px, 800px' />\n"
                            "</picture>\n"
                            "```\n\n"
                            "### Ключевые оптимизации\n"
                            "- `loading=\"lazy\"` — нативная ленивая загрузка\n"
                            "- `width` и `height` — предотвращают CLS\n"
                            "- `fetchpriority=\"high\"` — для LCP изображения\n"
                            "- `decoding=\"async\"` — неблокирующее декодирование\n"
                            "- CDN с автоматической конвертацией (Cloudinary, imgproxy)"
                        ),
                    },
                    {
                        "type": "category-sort",
                        "title": "Классификация форматов изображений",
                        "categories": [
                            {"name": "Растровые с потерями", "items": ["JPEG", "WebP (lossy)", "AVIF (lossy)"]},
                            {"name": "Растровые без потерь", "items": ["PNG", "WebP (lossless)"]},
                            {"name": "Векторные", "items": ["SVG"]},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой атрибут HTML5 нужно добавить к LCP-изображению для ускорения его загрузки?",
                        "options": [
                            {"id": "a", "text": "loading='eager'", "correct": False},
                            {"id": "b", "text": "fetchpriority='high'", "correct": True},
                            {"id": "c", "text": "decoding='sync'", "correct": False},
                            {"id": "d", "text": "importance='critical'", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Какой формат изображений обеспечивает наилучшее сжатие (до 50% меньше JPEG) при сохранении высокого качества?",
                        "answer": "AVIF",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 7: Security & Architecture
    # =====================================================================
    {
        "title": "Security & Architecture",
        "pos": 6,
        "lessons": [
            {
                "t": "XSS, CSRF и Content Security Policy",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Веб-безопасность для фронтенда",
                        "content": (
                            "## XSS (Cross-Site Scripting)\n\n"
                            "Атака через внедрение вредоносного JavaScript:\n"
                            "- **Stored XSS** — скрипт сохраняется на сервере (комментарии, профили)\n"
                            "- **Reflected XSS** — скрипт в URL параметрах\n"
                            "- **DOM-based XSS** — манипуляция DOM через `innerHTML`, `document.write`\n\n"
                            "### Защита\n"
                            "- React автоматически экранирует JSX выражения\n"
                            "- Избегать `dangerouslySetInnerHTML` без санитизации\n"
                            "- Использовать `DOMPurify` для пользовательского HTML\n\n"
                            "## CSRF (Cross-Site Request Forgery)\n"
                            "Атака через поддельные запросы от имени авторизованного пользователя.\n"
                            "Защита: CSRF-токены, SameSite cookies, проверка Origin header.\n\n"
                            "## CSP (Content Security Policy)\n"
                            "HTTP заголовок, определяющий разрешённые источники контента:\n"
                            "```\n"
                            "Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com;\n"
                            "```"
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Атака → Метод защиты",
                        "pairs": [
                            {"left": "Stored XSS", "right": "Санитизация пользовательского ввода + CSP"},
                            {"left": "CSRF", "right": "SameSite cookies + CSRF токен"},
                            {"left": "Clickjacking", "right": "X-Frame-Options: DENY"},
                            {"left": "Man-in-the-Middle", "right": "HTTPS + HSTS"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Почему React по умолчанию защищает от XSS при рендеринге переменных в JSX?",
                        "options": [
                            {"id": "a", "text": "React использует CSP заголовки", "correct": False},
                            {"id": "b", "text": "React экранирует HTML-сущности в строках перед вставкой в DOM", "correct": True},
                            {"id": "c", "text": "React удаляет все теги из строк", "correct": False},
                            {"id": "d", "text": "React использует iframe sandbox", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Атрибут SameSite=Strict на cookies полностью предотвращает CSRF-атаки.",
                        "answer": True,
                        "explanation": "SameSite=Strict запрещает отправку cookies при cross-site запросах, полностью блокируя CSRF. Но может ломать легитимную навигацию по ссылкам.",
                    },
                ],
            },
            {
                "t": "OAuth 2.0 и JWT",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "OAuth 2.0 и JWT для фронтенда",
                        "content": (
                            "## OAuth 2.0 Flows\n\n"
                            "### Authorization Code Flow + PKCE\n"
                            "Рекомендованный flow для SPA (заменил Implicit Flow):\n\n"
                            "1. Генерация `code_verifier` (случайная строка) и `code_challenge` (SHA256)\n"
                            "2. Редирект на `/authorize?response_type=code&code_challenge=...`\n"
                            "3. Пользователь авторизуется, сервер возвращает `code`\n"
                            "4. Обмен `code` + `code_verifier` на токены\n\n"
                            "### JWT (JSON Web Token)\n"
                            "```\n"
                            "header.payload.signature\n"
                            "```\n"
                            "- **Access Token** — короткоживущий (15-30 мин), для API запросов\n"
                            "- **Refresh Token** — долгоживущий, для обновления access token\n\n"
                            "### Хранение токенов в SPA\n"
                            "- ❌ localStorage — уязвим для XSS\n"
                            "- ✅ httpOnly cookie — недоступен для JS\n"
                            "- ⚠️ memory (переменная) — теряется при обновлении страницы\n"
                            "- ✅ httpOnly cookie (refresh) + memory (access) — лучший баланс"
                        ),
                    },
                    {
                        "type": "timeline",
                        "title": "Эволюция аутентификации",
                        "items": [
                            {"label": "Basic Auth", "description": "Login:password в каждом запросе (Base64)"},
                            {"label": "Session Cookies", "description": "Server-side сессии с cookie ID"},
                            {"label": "OAuth 2.0 Implicit", "description": "Токен прямо в URL (deprecated для SPA)"},
                            {"label": "OAuth 2.0 + PKCE", "description": "Безопасный flow для SPA без client secret"},
                            {"label": "WebAuthn/Passkeys", "description": "Беспарольная аутентификация через биометрию"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Почему Implicit Flow (response_type=token) не рекомендуется для SPA?",
                        "options": [
                            {"id": "a", "text": "Он слишком медленный", "correct": False},
                            {"id": "b", "text": "Токен попадает в URL fragment и может утечь через browser history/referer", "correct": True},
                            {"id": "c", "text": "Он не поддерживает refresh tokens", "correct": False},
                            {"id": "d", "text": "Он требует client secret", "correct": False},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Interceptor для refresh token",
                        "description": "Реализуйте axios interceptor, который автоматически обновляет access token при 401 ошибке.",
                        "starterCode": (
                            "import axios from 'axios';\n\n"
                            "const api = axios.create({ baseURL: '/api' });\n\n"
                            "api.interceptors.response.use(\n"
                            "  response => response,\n"
                            "  async error => {\n"
                            "    // Реализуйте refresh логику\n"
                            "  }\n"
                            ");"
                        ),
                        "solution": (
                            "let isRefreshing = false;\n"
                            "let failedQueue: Array<{ resolve: Function; reject: Function }> = [];\n\n"
                            "api.interceptors.response.use(\n"
                            "  response => response,\n"
                            "  async error => {\n"
                            "    const originalRequest = error.config;\n"
                            "    if (error.response?.status === 401 && !originalRequest._retry) {\n"
                            "      if (isRefreshing) {\n"
                            "        return new Promise((resolve, reject) => {\n"
                            "          failedQueue.push({ resolve, reject });\n"
                            "        }).then(() => api(originalRequest));\n"
                            "      }\n"
                            "      originalRequest._retry = true;\n"
                            "      isRefreshing = true;\n"
                            "      try {\n"
                            "        await axios.post('/api/auth/refresh');\n"
                            "        failedQueue.forEach(p => p.resolve());\n"
                            "        return api(originalRequest);\n"
                            "      } catch (e) {\n"
                            "        failedQueue.forEach(p => p.reject(e));\n"
                            "        window.location.href = '/login';\n"
                            "      } finally {\n"
                            "        isRefreshing = false;\n"
                            "        failedQueue = [];\n"
                            "      }\n"
                            "    }\n"
                            "    return Promise.reject(error);\n"
                            "  }\n"
                            ");"
                        ),
                    },
                ],
            },
            {
                "t": "Микрофронтенды",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Микрофронтенд-архитектура",
                        "content": (
                            "## Микрофронтенды\n\n"
                            "Архитектурный подход: разделение фронтенда на независимые приложения, "
                            "разрабатываемые отдельными командами.\n\n"
                            "### Подходы к интеграции\n"
                            "- **Build-time** — npm пакеты (жёсткая связь, синхронный деплой)\n"
                            "- **Runtime via iframes** — полная изоляция, плохой UX\n"
                            "- **Runtime via JS** — Module Federation, single-spa\n"
                            "- **Server-side** — SSI, ESI, Nginx includes\n"
                            "- **Web Components** — Custom Elements как контейнеры\n\n"
                            "### single-spa\n"
                            "Фреймворк для оркестрации микрофронтендов:\n"
                            "```javascript\n"
                            "registerApplication({\n"
                            "  name: '@org/navbar',\n"
                            "  app: () => System.import('@org/navbar'),\n"
                            "  activeWhen: '/',\n"
                            "});\n"
                            "```\n\n"
                            "### Проблемы\n"
                            "- Общие зависимости (React, design system)\n"
                            "- Маршрутизация между микрофронтендами\n"
                            "- Общий стейт (event bus, custom events)"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой способ интеграции микрофронтендов обеспечивает полную изоляцию CSS и JS, но имеет худший UX?",
                        "options": [
                            {"id": "a", "text": "Module Federation", "correct": False},
                            {"id": "b", "text": "iframes", "correct": True},
                            {"id": "c", "text": "Web Components", "correct": False},
                            {"id": "d", "text": "npm пакеты", "correct": False},
                        ],
                    },
                    {
                        "type": "category-sort",
                        "title": "Build-time vs Runtime интеграция",
                        "categories": [
                            {"name": "Build-time", "items": ["npm packages", "Монорепо с shared libraries"]},
                            {"name": "Runtime (Client)", "items": ["Module Federation", "single-spa", "iframes"]},
                            {"name": "Runtime (Server)", "items": ["SSI/ESI", "Nginx sub_filter"]},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "title": "Custom Event для коммуникации",
                        "description": "Соберите код для коммуникации между микрофронтендами через Custom Events.",
                        "fragments": [
                            "// Отправка события из микрофронтенда A",
                            "window.dispatchEvent(",
                            "  new CustomEvent('user:selected', {",
                            "    detail: { userId: '123' }",
                            "  })",
                            ");",
                            "",
                            "// Подписка в микрофронтенде B",
                            "window.addEventListener('user:selected', (e: CustomEvent) => {",
                            "  loadUser(e.detail.userId);",
                            "});",
                        ],
                    },
                ],
            },
            {
                "t": "Design Patterns в React",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Паттерны проектирования React",
                        "content": (
                            "## Архитектурные паттерны\n\n"
                            "### Compound Components\n"
                            "Компоненты, работающие вместе через неявный контекст:\n"
                            "```typescript\n"
                            "<Select onChange={handleChange}>\n"
                            "  <Select.Trigger>Выберите...</Select.Trigger>\n"
                            "  <Select.Options>\n"
                            "    <Select.Option value='a'>Option A</Select.Option>\n"
                            "  </Select.Options>\n"
                            "</Select>\n"
                            "```\n\n"
                            "### Render Props\n"
                            "Передача функции для кастомного рендеринга:\n"
                            "```typescript\n"
                            "<DataFetcher url='/api/users' render={(data) => <UserList users={data} />} />\n"
                            "```\n\n"
                            "### Custom Hooks (Headless UI)\n"
                            "Логика без UI — самый современный подход:\n"
                            "```typescript\n"
                            "const { items, search, setSearch } = useAutocomplete({ data, filterFn });\n"
                            "```\n\n"
                            "### HOC (Higher-Order Components)\n"
                            "Обёртка компонента для добавления функциональности: `withAuth`, `withTheme`.\n"
                            "Устаревает в пользу хуков."
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Паттерн → Пример использования",
                        "pairs": [
                            {"left": "Compound Components", "right": "Tabs, Select, Accordion с подкомпонентами"},
                            {"left": "Custom Hooks", "right": "useForm, usePagination — логика без UI"},
                            {"left": "Render Props", "right": "Делегирование рендеринга потребителю"},
                            {"left": "Provider Pattern", "right": "Тема, аутентификация через Context API"},
                        ],
                    },
                    {
                        "type": "code-editor",
                        "title": "Compound Component",
                        "description": "Реализуйте compound component Accordion с подкомпонентами Item и Content.",
                        "starterCode": (
                            "const AccordionContext = React.createContext<any>(null);\n\n"
                            "function Accordion({ children }: { children: React.ReactNode }) {\n"
                            "  // Управляйте открытым элементом\n"
                            "}\n\n"
                            "Accordion.Item = function Item({ id, title, children }) {\n"
                            "  // Используйте контекст для toggle\n"
                            "};"
                        ),
                        "solution": (
                            "function Accordion({ children }: { children: React.ReactNode }) {\n"
                            "  const [openId, setOpenId] = useState<string | null>(null);\n"
                            "  const toggle = (id: string) => setOpenId(prev => prev === id ? null : id);\n"
                            "  return (\n"
                            "    <AccordionContext.Provider value={{ openId, toggle }}>\n"
                            "      <div>{children}</div>\n"
                            "    </AccordionContext.Provider>\n"
                            "  );\n"
                            "}\n\n"
                            "Accordion.Item = function Item({ id, title, children }) {\n"
                            "  const { openId, toggle } = useContext(AccordionContext);\n"
                            "  return (\n"
                            "    <div>\n"
                            "      <button onClick={() => toggle(id)}>{title}</button>\n"
                            "      {openId === id && <div>{children}</div>}\n"
                            "    </div>\n"
                            "  );\n"
                            "};"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой паттерн является предпочтительной альтернативой HOC в современном React?",
                        "options": [
                            {"id": "a", "text": "Render Props", "correct": False},
                            {"id": "b", "text": "Custom Hooks", "correct": True},
                            {"id": "c", "text": "Mixins", "correct": False},
                            {"id": "d", "text": "Class inheritance", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Clean Architecture для фронтенда",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Clean Architecture на фронтенде",
                        "content": (
                            "## Clean Architecture (Robert C. Martin)\n\n"
                            "Принцип: зависимости направлены внутрь, бизнес-логика не знает о UI и инфраструктуре.\n\n"
                            "### Слои для фронтенда\n\n"
                            "```\n"
                            "┌───────────────────────────┐\n"
                            "│  UI (React компоненты)    │  ← зависит от\n"
                            "├───────────────────────────┤\n"
                            "│  Adapters (API, Storage)  │  ← зависит от\n"
                            "├───────────────────────────┤\n"
                            "│  Use Cases (Application)  │  ← зависит от\n"
                            "├───────────────────────────┤\n"
                            "│  Entities (Domain)        │  ← не зависит ни от чего\n"
                            "└───────────────────────────┘\n"
                            "```\n\n"
                            "### Feature-Sliced Design (FSD)\n"
                            "Популярная архитектура для React:\n"
                            "- **app/** — провайдеры, роутинг\n"
                            "- **pages/** — композиция виджетов\n"
                            "- **widgets/** — автономные блоки UI\n"
                            "- **features/** — пользовательские сценарии\n"
                            "- **entities/** — бизнес-сущности\n"
                            "- **shared/** — утилиты, UI kit"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "title": "Порядок слоёв Clean Architecture",
                        "description": "Расположите слои от самого внешнего к внутреннему (от UI к Domain).",
                        "items": [
                            {"id": "1", "text": "UI / Presentation (React)"},
                            {"id": "2", "text": "Adapters (API clients, Storage)"},
                            {"id": "3", "text": "Use Cases / Application Logic"},
                            {"id": "4", "text": "Entities / Domain Models"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "В Feature-Sliced Design, какой слой содержит бизнес-сущности (User, Product)?",
                        "options": [
                            {"id": "a", "text": "features/", "correct": False},
                            {"id": "b", "text": "entities/", "correct": True},
                            {"id": "c", "text": "widgets/", "correct": False},
                            {"id": "d", "text": "shared/", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Как называется принцип Clean Architecture, согласно которому внутренние слои не должны знать о внешних?",
                        "answer": "Dependency Rule",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # SECTION 8: DevOps & CI/CD для фронтенда
    # =====================================================================
    {
        "title": "DevOps & CI/CD для фронтенда",
        "pos": 7,
        "lessons": [
            {
                "t": "Docker для фронтенд-разработчика",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Docker для фронтенда",
                        "content": (
                            "## Multi-stage Docker builds\n\n"
                            "Оптимальный Dockerfile для SPA использует multi-stage сборку:\n\n"
                            "```dockerfile\n"
                            "# Stage 1: Build\n"
                            "FROM node:20-alpine AS builder\n"
                            "WORKDIR /app\n"
                            "COPY package*.json ./\n"
                            "RUN npm ci\n"
                            "COPY . .\n"
                            "RUN npm run build\n\n"
                            "# Stage 2: Serve\n"
                            "FROM nginx:alpine\n"
                            "COPY --from=builder /app/dist /usr/share/nginx/html\n"
                            "COPY nginx.conf /etc/nginx/conf.d/default.conf\n"
                            "EXPOSE 80\n"
                            "```\n\n"
                            "### Оптимизации\n"
                            "- `.dockerignore` — исключить node_modules, .git\n"
                            "- `npm ci` вместо `npm install` — детерминированные зависимости\n"
                            "- Layer caching — COPY package.json перед COPY . для кеширования npm ci\n"
                            "- Alpine-образы — минимальный размер (nginx:alpine ~23MB)\n\n"
                            "### Docker Compose для development\n"
                            "```yaml\n"
                            "services:\n"
                            "  frontend:\n"
                            "    build: .\n"
                            "    volumes: ['./src:/app/src']  # hot reload\n"
                            "    ports: ['3000:3000']\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "Оптимизированный Dockerfile",
                        "description": "Напишите Dockerfile с multi-stage build для React SPA с nginx.",
                        "starterCode": (
                            "# Напишите Dockerfile:\n"
                            "# 1. Stage builder на node:20-alpine\n"
                            "# 2. npm ci + npm run build\n"
                            "# 3. Stage production на nginx:alpine\n"
                            "# 4. Копирование dist в nginx html"
                        ),
                        "solution": (
                            "FROM node:20-alpine AS builder\n"
                            "WORKDIR /app\n"
                            "COPY package*.json ./\n"
                            "RUN npm ci --frozen-lockfile\n"
                            "COPY . .\n"
                            "RUN npm run build\n\n"
                            "FROM nginx:alpine\n"
                            "COPY --from=builder /app/dist /usr/share/nginx/html\n"
                            "COPY nginx.conf /etc/nginx/conf.d/default.conf\n"
                            "EXPOSE 80\n"
                            "CMD [\"nginx\", \"-g\", \"daemon off;\"]"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Почему `COPY package*.json ./` и `RUN npm ci` идут перед `COPY . .` в Dockerfile?",
                        "options": [
                            {"id": "a", "text": "Для безопасности", "correct": False},
                            {"id": "b", "text": "Для кеширования Docker layer — npm ci не перевыполняется если package.json не изменился", "correct": True},
                            {"id": "c", "text": "Так требует Docker спецификация", "correct": False},
                            {"id": "d", "text": "Для уменьшения размера образа", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Multi-stage Docker build уменьшает размер финального образа, потому что node_modules не включаются в production stage.",
                        "answer": True,
                        "explanation": "Верно. В финальный образ копируется только результат сборки (dist/), а node_modules и исходники остаются в builder stage.",
                    },
                ],
            },
            {
                "t": "GitHub Actions и CI pipelines",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "CI/CD с GitHub Actions",
                        "content": (
                            "## GitHub Actions для фронтенда\n\n"
                            "### Типовой pipeline\n"
                            "```yaml\n"
                            "name: CI\n"
                            "on: [push, pull_request]\n"
                            "jobs:\n"
                            "  build:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "        with: { node-version: 20, cache: npm }\n"
                            "      - run: npm ci\n"
                            "      - run: npm run lint\n"
                            "      - run: npm run type-check\n"
                            "      - run: npm run test -- --coverage\n"
                            "      - run: npm run build\n"
                            "      - uses: actions/upload-artifact@v4\n"
                            "        with: { name: dist, path: dist/ }\n"
                            "```\n\n"
                            "### Оптимизации\n"
                            "- **Кеширование** — `actions/cache` для node_modules или встроенный `cache: npm`\n"
                            "- **Параллелизм** — отдельные jobs для lint, test, build\n"
                            "- **Matrix** — тестирование на нескольких версиях Node\n"
                            "- **Conditional deployment** — deploy только из main branch\n"
                            "- **Preview deployments** — Vercel/Netlify preview на PR"
                        ),
                    },
                    {
                        "type": "code-editor",
                        "title": "GitHub Actions workflow",
                        "description": "Напишите workflow с параллельными jobs для lint, test и build.",
                        "starterCode": (
                            "name: Frontend CI\n"
                            "on:\n"
                            "  pull_request:\n"
                            "    branches: [main]\n\n"
                            "# Создайте 3 параллельных job:\n"
                            "# lint, test, build\n"
                            "# Добавьте deploy job, зависящий от всех трёх"
                        ),
                        "solution": (
                            "name: Frontend CI\n"
                            "on:\n"
                            "  pull_request:\n"
                            "    branches: [main]\n"
                            "jobs:\n"
                            "  lint:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "        with: { node-version: 20, cache: npm }\n"
                            "      - run: npm ci\n"
                            "      - run: npm run lint && npm run type-check\n"
                            "  test:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "        with: { node-version: 20, cache: npm }\n"
                            "      - run: npm ci\n"
                            "      - run: npm run test -- --coverage\n"
                            "  build:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "        with: { node-version: 20, cache: npm }\n"
                            "      - run: npm ci && npm run build\n"
                            "  deploy:\n"
                            "    needs: [lint, test, build]\n"
                            "    runs-on: ubuntu-latest\n"
                            "    if: github.ref == 'refs/heads/main'\n"
                            "    steps:\n"
                            "      - run: echo 'Deploying...'"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой ключ в GitHub Actions определяет зависимость job от других jobs?",
                        "options": [
                            {"id": "a", "text": "depends_on", "correct": False},
                            {"id": "b", "text": "needs", "correct": True},
                            {"id": "c", "text": "requires", "correct": False},
                            {"id": "d", "text": "after", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "title": "GitHub Actions условие деплоя",
                        "sentence": "deploy:\n  needs: [lint, test, build]\n  ___keyword: github.ref == 'refs/heads/main'",
                        "blanks": [
                            {"id": "keyword", "answer": "if"},
                        ],
                    },
                ],
            },
            {
                "t": "Feature Flags и A/B тестирование",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Feature Flags и A/B тесты",
                        "content": (
                            "## Feature Flags\n\n"
                            "Feature flags — механизм включения/выключения функциональности без деплоя нового кода.\n\n"
                            "### Типы флагов\n"
                            "- **Release flags** — постепенный rollout (1% → 10% → 100%)\n"
                            "- **Experiment flags** — A/B тесты с метриками\n"
                            "- **Ops flags** — kill switch для деградации\n"
                            "- **Permission flags** — доступ для определённых пользователей\n\n"
                            "### Инструменты\n"
                            "- **LaunchDarkly** — enterprise, real-time, SDK для React\n"
                            "- **Unleash** — open-source, self-hosted\n"
                            "- **PostHog** — open-source, с аналитикой\n"
                            "- **Flagsmith** — open-source, remote config\n\n"
                            "### Реализация в React\n"
                            "```typescript\n"
                            "function App() {\n"
                            "  const showNewCheckout = useFeatureFlag('new-checkout');\n"
                            "  return showNewCheckout ? <NewCheckout /> : <OldCheckout />;\n"
                            "}\n"
                            "```\n\n"
                            "### A/B тестирование\n"
                            "Статистически значимое сравнение двух вариантов. Требует: гипотезу, метрику, "
                            "достаточный размер выборки, случайное разбиение."
                        ),
                    },
                    {
                        "type": "matching",
                        "title": "Тип флага → Сценарий",
                        "pairs": [
                            {"left": "Release flag", "right": "Постепенный rollout новой фичи 1% → 100%"},
                            {"left": "Experiment flag", "right": "A/B тест нового дизайна чекаута"},
                            {"left": "Ops flag", "right": "Kill switch для отключения тяжёлой фичи при нагрузке"},
                            {"left": "Permission flag", "right": "Beta-доступ только для premium-пользователей"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой главный риск при накоплении feature flags в проекте?",
                        "options": [
                            {"id": "a", "text": "Увеличение размера бандла", "correct": False},
                            {"id": "b", "text": "Technical debt: сложность кода растёт с комбинациями флагов", "correct": True},
                            {"id": "c", "text": "Замедление CI/CD pipeline", "correct": False},
                            {"id": "d", "text": "Проблемы с SEO", "correct": False},
                        ],
                    },
                    {
                        "type": "category-sort",
                        "title": "Классификация инструментов",
                        "categories": [
                            {"name": "Feature Flags", "items": ["LaunchDarkly", "Unleash", "Flagsmith"]},
                            {"name": "A/B Testing", "items": ["Google Optimize", "Optimizely", "VWO"]},
                            {"name": "Оба (flags + analytics)", "items": ["PostHog", "Amplitude Experiment"]},
                        ],
                    },
                ],
            },
            {
                "t": "Мониторинг: Sentry и Lighthouse CI",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Мониторинг фронтенда",
                        "content": (
                            "## Sentry — Error Tracking\n\n"
                            "Sentry перехватывает ошибки в production и предоставляет:\n"
                            "- Stack traces с source maps\n"
                            "- Breadcrumbs (последовательность действий до ошибки)\n"
                            "- Session replay (видео сессии пользователя)\n"
                            "- Performance monitoring (transactions, spans)\n\n"
                            "```typescript\n"
                            "import * as Sentry from '@sentry/react';\n\n"
                            "Sentry.init({\n"
                            "  dsn: 'https://...@sentry.io/...',\n"
                            "  integrations: [\n"
                            "    Sentry.browserTracingIntegration(),\n"
                            "    Sentry.replayIntegration(),\n"
                            "  ],\n"
                            "  tracesSampleRate: 0.1,\n"
                            "  replaysSessionSampleRate: 0.01,\n"
                            "});\n"
                            "```\n\n"
                            "## Lighthouse CI\n\n"
                            "Автоматический аудит перформанса в CI:\n"
                            "- Проверка Core Web Vitals на каждый PR\n"
                            "- Budget assertions (LCP < 2.5s, bundle < 200KB)\n"
                            "- Историческое сравнение метрик"
                        ),
                    },
                    {
                        "type": "flashcards",
                        "title": "Инструменты мониторинга",
                        "cards": [
                            {"front": "Sentry", "back": "Error tracking + performance monitoring. Source maps для читаемых stack traces в production."},
                            {"front": "Lighthouse CI", "back": "Автоматический аудит перформанса в CI. Assertions для бюджетов: bundle size, LCP, CLS."},
                            {"front": "Datadog RUM", "back": "Real User Monitoring: сбор метрик от реальных пользователей (LCP, FID, загрузка ресурсов)."},
                            {"front": "LogRocket", "back": "Session replay + error tracking. Записывает DOM, network, console для воспроизведения багов."},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Зачем загружать source maps в Sentry, а не деплоить их на production сервер?",
                        "options": [
                            {"id": "a", "text": "Source maps слишком большие для CDN", "correct": False},
                            {"id": "b", "text": "Чтобы показывать читаемые stack traces без раскрытия исходного кода пользователям", "correct": True},
                            {"id": "c", "text": "Sentry не может работать без source maps", "correct": False},
                            {"id": "d", "text": "Source maps улучшают перформанс приложения", "correct": False},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Как называется функция Sentry, которая записывает последовательность действий пользователя перед ошибкой?",
                        "answer": "breadcrumbs",
                    },
                ],
            },
        ],
    },
]


# ---------------------------------------------------------------------------
async def seed():
    async with async_session() as db:
        # Idempotency check
        existing = await db.execute(select(Course).where(Course.title == COURSE_TITLE))
        if existing.scalar_one_or_none():
            print(f"Course '{COURSE_TITLE}' already exists — skipping.")
            return

        # Get first user as author
        r = await db.execute(select(User).limit(1))
        user = r.scalar_one_or_none()
        if not user:
            from app.utils.security import hash_password
            user = User(
                id=uuid.uuid4(),
                email="admin@pathmind.com",
                name="PathMind Admin",
                password=hash_password("admin2026!"),
                direction="frontend",
                assessment_level="advanced",
                language="ru",
            )
            db.add(user)
            await db.flush()
            print("Created admin user: admin@pathmind.com / admin2026!")

        # Create course
        course = Course(
            id=uuid.uuid4(),
            title=COURSE_TITLE,
            slug="senior-frontend-developer-" + uuid.uuid4().hex[:6],
            description=COURSE_DESC,
            author_id=user.id,
            category="Frontend",
            difficulty="Advanced",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()

        positions = []
        gidx = 0
        total_lessons = 0

        for sec_data in SECTIONS:
            section = CourseSection(
                id=uuid.uuid4(),
                course_id=course.id,
                title=sec_data["title"],
                position=sec_data["pos"],
            )
            db.add(section)
            await db.flush()

            for i, lesson_data in enumerate(sec_data["lessons"]):
                lesson = CourseLesson(
                    id=uuid.uuid4(),
                    section_id=section.id,
                    title=lesson_data["t"],
                    position=i,
                    content_type="interactive",
                    content_markdown="",
                    xp_reward=lesson_data["xp"],
                    steps=lesson_data["steps"],
                )
                db.add(lesson)
                await db.flush()
                positions.append({
                    "id": str(lesson.id),
                    "x": SNAKE_X[gidx % 5] * CANVAS_W,
                    "y": V_PAD + gidx * ROW_H,
                })
                gidx += 1
                total_lessons += 1

        # Build roadmap edges
        edges = [
            {"id": f"e-{i}", "source": positions[i - 1]["id"], "target": positions[i]["id"]}
            for i in range(1, len(positions))
        ]
        course.roadmap_nodes = positions
        course.roadmap_edges = edges

        await db.commit()
        print(f"Created course '{COURSE_TITLE}': {len(SECTIONS)} sections, {total_lessons} lessons.")

    print("Seed complete!")


if __name__ == "__main__":
    asyncio.run(seed())
