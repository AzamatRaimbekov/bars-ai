import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_V2_SENIOR: Record<string, LessonContentV2> = {
  // ──────────────────────────────────────────────
  // Lesson 1 — TypeScript Fundamentals
  // ──────────────────────────────────────────────
  "fe-21-1": {
    id: "fe-21-1",
    title: {
      en: "TypeScript Fundamentals",
      ru: "Основы TypeScript",
    },
    slides: [
      {
        title: {
          en: "Basic Types & Type Annotations",
          ru: "Базовые типы и аннотации типов",
        },
        content: {
          en: "TypeScript adds static types on top of JavaScript. You can annotate variables, function parameters, and return values with types like string, number, boolean, null, undefined, and any. This lets the compiler catch mistakes before your code ever runs. Type inference means you don't always have to write types explicitly — TypeScript can figure them out from the value you assign.",
          ru: "TypeScript добавляет статическую типизацию поверх JavaScript. Вы можете аннотировать переменные, параметры функций и возвращаемые значения типами: string, number, boolean, null, undefined и any. Это позволяет компилятору находить ошибки до запуска кода. Вывод типов означает, что писать типы явно не всегда обязательно — TypeScript может определить их по присвоенному значению.",
        },
        code: {
          language: "typescript",
          code: `let name: string = "Alice";\nlet age: number = 25;\nlet isActive: boolean = true;\n\nfunction greet(user: string): string {\n  return \`Hello, \${user}!\`;\n}\n\n// Type inference — TS knows 'total' is number\nconst total = age + 10;`,
        },
      },
      {
        title: {
          en: "Interfaces, Type Aliases & Generics",
          ru: "Интерфейсы, псевдонимы типов и дженерики",
        },
        content: {
          en: "Interfaces describe the shape of objects and can be extended. Type aliases use the 'type' keyword and can represent unions, intersections, or any complex type. Generics let you write reusable code that works with different types while keeping type safety — you define a type parameter in angle brackets that gets replaced with a real type when the function or class is used.",
          ru: "Интерфейсы описывают форму объектов и могут быть расширены. Псевдонимы типов используют ключевое слово 'type' и могут представлять объединения, пересечения и любые сложные типы. Дженерики позволяют писать переиспользуемый код, который работает с разными типами, сохраняя типобезопасность — вы задаёте параметр типа в угловых скобках, который заменяется реальным типом при вызове.",
        },
        code: {
          language: "typescript",
          code: `interface User {\n  id: number;\n  name: string;\n  email?: string; // optional\n}\n\ntype Status = "active" | "inactive" | "banned";\n\ntype ApiResponse<T> = {\n  data: T;\n  error: string | null;\n};\n\nfunction getFirst<T>(items: T[]): T {\n  return items[0];\n}`,
        },
      },
      {
        title: {
          en: "Union Types & Type Narrowing",
          ru: "Объединённые типы и сужение типов",
        },
        content: {
          en: "Union types let a value be one of several types using the | operator. Type narrowing is how TypeScript figures out a more specific type inside a conditional block — using typeof, instanceof, the 'in' operator, or discriminated unions. This is essential for writing safe code when a value could be more than one type.",
          ru: "Объединённые типы позволяют значению быть одним из нескольких типов с помощью оператора |. Сужение типов — это механизм, с помощью которого TypeScript определяет более конкретный тип внутри условного блока, используя typeof, instanceof, оператор 'in' или дискриминируемые объединения. Это необходимо для написания безопасного кода, когда значение может быть нескольких типов.",
        },
        code: {
          language: "typescript",
          code: `type Shape =\n  | { kind: "circle"; radius: number }\n  | { kind: "rect"; width: number; height: number };\n\nfunction area(shape: Shape): number {\n  if (shape.kind === "circle") {\n    return Math.PI * shape.radius ** 2;\n  }\n  // TS knows it's a rect here\n  return shape.width * shape.height;\n}\n\nfunction print(val: string | number) {\n  if (typeof val === "string") {\n    console.log(val.toUpperCase());\n  } else {\n    console.log(val.toFixed(2));\n  }\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which TypeScript type represents a value that can be either a string or a number?",
          ru: "Какой тип TypeScript представляет значение, которое может быть строкой или числом?",
        },
        options: [
          { en: "string & number", ru: "string & number" },
          { en: "string | number", ru: "string | number" },
          { en: "string + number", ru: "string + number" },
          { en: "StringOrNumber", ru: "StringOrNumber" },
        ],
        correct: 1,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "In TypeScript, an interface can only describe objects and cannot be extended.",
          ru: "В TypeScript интерфейс может описывать только объекты и не может быть расширен.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each TypeScript concept to its description.",
          ru: "Сопоставьте каждое понятие TypeScript с его описанием.",
        },
        pairs: [
          {
            term: { en: "interface", ru: "interface" },
            definition: {
              en: "Describes the shape of an object",
              ru: "Описывает структуру объекта",
            },
          },
          {
            term: { en: "type alias", ru: "псевдоним типа" },
            definition: {
              en: "Creates a name for any type expression",
              ru: "Создаёт имя для любого выражения типа",
            },
          },
          {
            term: { en: "generic <T>", ru: "дженерик <T>" },
            definition: {
              en: "Parameterizes a type for reuse",
              ru: "Параметризует тип для переиспользования",
            },
          },
          {
            term: { en: "union |", ru: "объединение |" },
            definition: {
              en: "Allows a value to be one of several types",
              ru: "Позволяет значению быть одним из нескольких типов",
            },
          },
          {
            term: { en: "typeof guard", ru: "проверка typeof" },
            definition: {
              en: "Narrows the type at runtime",
              ru: "Сужает тип во время выполнения",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about TypeScript types.",
          ru: "Заполните пропуски о типах TypeScript.",
        },
        blanks: [
          {
            text: {
              en: "To mark a property as optional in an interface, add ___ after the property name.",
              ru: "Чтобы пометить свойство как необязательное в интерфейсе, добавьте ___ после имени свойства.",
            },
            options: [
              { en: "?", ru: "?" },
              { en: "!", ru: "!" },
              { en: "| undefined", ru: "| undefined" },
              { en: "*", ru: "*" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "A ___ lets you write functions that work with any type while preserving type info.",
              ru: "___ позволяет писать функции, работающие с любым типом, сохраняя информацию о типе.",
            },
            options: [
              { en: "generic", ru: "дженерик" },
              { en: "decorator", ru: "декоратор" },
              { en: "module", ru: "модуль" },
              { en: "promise", ru: "промис" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The operator ___ is used to create intersection types in TypeScript.",
              ru: "Оператор ___ используется для создания пересечённых типов в TypeScript.",
            },
            options: [
              { en: "&", ru: "&" },
              { en: "|", ru: "|" },
              { en: "+", ru: "+" },
              { en: "&&", ru: "&&" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to define and use a generic function in TypeScript.",
          ru: "Расположите шаги определения и использования дженерик-функции в TypeScript.",
        },
        items: [
          { en: "Write the function keyword and name", ru: "Написать ключевое слово function и имя" },
          { en: "Add a type parameter in angle brackets <T>", ru: "Добавить параметр типа в угловых скобках <T>" },
          { en: "Use T in the parameter list and return type", ru: "Использовать T в списке параметров и возвращаемом типе" },
          { en: "Implement the function body", ru: "Реализовать тело функции" },
          { en: "Call the function with a specific type or let TS infer it", ru: "Вызвать функцию с конкретным типом или позволить TS определить его" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a TypeScript interface and a function that uses it.",
          ru: "Расположите строки, чтобы создать интерфейс TypeScript и функцию, использующую его.",
        },
        items: [
          { en: "interface Product {", ru: "interface Product {" },
          { en: "  name: string;", ru: "  name: string;" },
          { en: "  price: number;", ru: "  price: number;" },
          { en: "}", ru: "}" },
          { en: "function formatPrice(p: Product): string {", ru: "function formatPrice(p: Product): string {" },
          { en: "  return `${p.name}: $${p.price}`;", ru: "  return `${p.name}: $${p.price}`;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What TypeScript keyword is used to check the runtime type of a primitive value (e.g., string, number)?",
          ru: "Какое ключевое слово TypeScript используется для проверки типа примитивного значения во время выполнения (например, string, number)?",
        },
        correctText: {
          en: "typeof",
          ru: "typeof",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key TypeScript terms.",
          ru: "Повторите ключевые термины TypeScript.",
        },
        pairs: [
          {
            term: { en: "Type Inference", ru: "Вывод типов" },
            definition: {
              en: "TypeScript automatically determines the type from the assigned value",
              ru: "TypeScript автоматически определяет тип по присвоенному значению",
            },
          },
          {
            term: { en: "Union Type", ru: "Объединённый тип" },
            definition: {
              en: "A type that can be one of several types, written with |",
              ru: "Тип, который может быть одним из нескольких типов, записывается через |",
            },
          },
          {
            term: { en: "Generic", ru: "Дженерик" },
            definition: {
              en: "A type parameter that makes code reusable for different types",
              ru: "Параметр типа, делающий код переиспользуемым для разных типов",
            },
          },
          {
            term: { en: "Type Narrowing", ru: "Сужение типов" },
            definition: {
              en: "Refining a broad type to a more specific one inside a conditional",
              ru: "Уточнение широкого типа до более конкретного внутри условия",
            },
          },
          {
            term: { en: "Discriminated Union", ru: "Дискриминируемое объединение" },
            definition: {
              en: "A union where each member has a common literal property for narrowing",
              ru: "Объединение, где каждый член имеет общее литеральное свойство для сужения",
            },
          },
        ],
      },
    ],
  },

  // ──────────────────────────────────────────────
  // Lesson 2 — Testing React Apps
  // ──────────────────────────────────────────────
  "fe-22-1": {
    id: "fe-22-1",
    title: {
      en: "Testing React Apps",
      ru: "Тестирование React-приложений",
    },
    slides: [
      {
        title: {
          en: "Jest Basics & Test Structure",
          ru: "Основы Jest и структура тестов",
        },
        content: {
          en: "Jest is the most popular JavaScript testing framework. Tests are organized with 'describe' blocks for grouping and 'it' or 'test' blocks for individual test cases. Jest provides matchers like toBe, toEqual, toContain, toBeTruthy, and toThrow. Each test should follow the Arrange-Act-Assert pattern: set up data, perform the action, and verify the result.",
          ru: "Jest — самый популярный фреймворк для тестирования JavaScript. Тесты организуются с помощью блоков 'describe' для группировки и блоков 'it' или 'test' для отдельных тест-кейсов. Jest предоставляет матчеры: toBe, toEqual, toContain, toBeTruthy и toThrow. Каждый тест следует паттерну Arrange-Act-Assert: подготовка данных, выполнение действия, проверка результата.",
        },
        code: {
          language: "typescript",
          code: `import { describe, it, expect } from "@jest/globals";\n\ndescribe("sum", () => {\n  it("adds two numbers correctly", () => {\n    const result = sum(2, 3);\n    expect(result).toBe(5);\n  });\n\n  it("returns 0 when both args are 0", () => {\n    expect(sum(0, 0)).toBe(0);\n  });\n});`,
        },
      },
      {
        title: {
          en: "React Testing Library — render, screen, fireEvent",
          ru: "React Testing Library — render, screen, fireEvent",
        },
        content: {
          en: "React Testing Library (RTL) encourages testing from the user's perspective. Use 'render' to mount a component, 'screen' to query the DOM (getByText, getByRole, getByTestId), and 'fireEvent' to simulate user actions like clicks and typing. Queries prioritize accessibility: getByRole is preferred over getByTestId because it mirrors how users and assistive technology find elements.",
          ru: "React Testing Library (RTL) поощряет тестирование с точки зрения пользователя. Используйте 'render' для монтирования компонента, 'screen' для запросов к DOM (getByText, getByRole, getByTestId) и 'fireEvent' для симуляции действий пользователя: кликов, ввода текста. Запросы приоритизируют доступность: getByRole предпочтительнее getByTestId, так как отражает то, как пользователи и вспомогательные технологии находят элементы.",
        },
        code: {
          language: "typescript",
          code: `import { render, screen, fireEvent } from "@testing-library/react";\nimport Counter from "./Counter";\n\ntest("increments counter on button click", () => {\n  render(<Counter />);\n  const button = screen.getByRole("button", { name: /increment/i });\n  fireEvent.click(button);\n  expect(screen.getByText("Count: 1")).toBeInTheDocument();\n});`,
        },
      },
      {
        title: {
          en: "Async Testing & Mocking",
          ru: "Асинхронное тестирование и моки",
        },
        content: {
          en: "Use 'waitFor' when testing asynchronous behaviour such as API calls or state updates that happen after a delay. For mocking, jest.fn() creates a mock function, and jest.mock() replaces entire modules. Mock functions let you verify how many times a function was called and with what arguments. This is essential for isolating your component from external dependencies like APIs.",
          ru: "Используйте 'waitFor' при тестировании асинхронного поведения: вызовов API или обновления состояния с задержкой. Для создания моков jest.fn() создаёт мок-функцию, а jest.mock() подменяет целые модули. Мок-функции позволяют проверить, сколько раз функция была вызвана и с какими аргументами. Это необходимо для изоляции компонента от внешних зависимостей вроде API.",
        },
        code: {
          language: "typescript",
          code: `import { render, screen, waitFor } from "@testing-library/react";\nimport UserList from "./UserList";\nimport * as api from "./api";\n\njest.mock("./api");\n\ntest("loads and displays users", async () => {\n  (api.fetchUsers as jest.Mock).mockResolvedValue([\n    { id: 1, name: "Alice" },\n  ]);\n  render(<UserList />);\n  await waitFor(() => {\n    expect(screen.getByText("Alice")).toBeInTheDocument();\n  });\n});`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which React Testing Library function is used to simulate a user clicking a button?",
          ru: "Какая функция React Testing Library используется для симуляции клика пользователя по кнопке?",
        },
        options: [
          { en: "screen.click()", ru: "screen.click()" },
          { en: "fireEvent.click()", ru: "fireEvent.click()" },
          { en: "userEvent.press()", ru: "userEvent.press()" },
          { en: "render.click()", ru: "render.click()" },
        ],
        correct: 1,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "In React Testing Library, getByTestId is the recommended first-choice query for finding elements.",
          ru: "В React Testing Library getByTestId является рекомендуемым запросом первого выбора для поиска элементов.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each testing concept to its description.",
          ru: "Сопоставьте каждое понятие тестирования с его описанием.",
        },
        pairs: [
          {
            term: { en: "render()", ru: "render()" },
            definition: {
              en: "Mounts a React component into a virtual DOM",
              ru: "Монтирует React-компонент в виртуальный DOM",
            },
          },
          {
            term: { en: "screen", ru: "screen" },
            definition: {
              en: "Object with queries to find elements in the rendered output",
              ru: "Объект с запросами для поиска элементов в отрендеренном выводе",
            },
          },
          {
            term: { en: "jest.fn()", ru: "jest.fn()" },
            definition: {
              en: "Creates a mock function to track calls",
              ru: "Создаёт мок-функцию для отслеживания вызовов",
            },
          },
          {
            term: { en: "waitFor()", ru: "waitFor()" },
            definition: {
              en: "Waits for async updates before making assertions",
              ru: "Ожидает асинхронных обновлений перед проверками",
            },
          },
          {
            term: { en: "expect().toBe()", ru: "expect().toBe()" },
            definition: {
              en: "Asserts strict equality of a value",
              ru: "Проверяет строгое равенство значения",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about testing React components.",
          ru: "Заполните пропуски о тестировании React-компонентов.",
        },
        blanks: [
          {
            text: {
              en: "To find an element by its accessible role, use screen.___.",
              ru: "Чтобы найти элемент по его роли доступности, используйте screen.___.",
            },
            options: [
              { en: "getByRole", ru: "getByRole" },
              { en: "getByClass", ru: "getByClass" },
              { en: "findByTag", ru: "findByTag" },
              { en: "queryByName", ru: "queryByName" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "jest.___() is used to replace an entire module with a mock implementation.",
              ru: "jest.___() используется для замены целого модуля мок-реализацией.",
            },
            options: [
              { en: "mock", ru: "mock" },
              { en: "spy", ru: "spy" },
              { en: "replace", ru: "replace" },
              { en: "stub", ru: "stub" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ pattern stands for: set up data, perform action, check result.",
              ru: "Паттерн ___ означает: подготовка данных, выполнение действия, проверка результата.",
            },
            options: [
              { en: "Arrange-Act-Assert", ru: "Arrange-Act-Assert" },
              { en: "Setup-Run-Verify", ru: "Setup-Run-Verify" },
              { en: "Given-When-Then", ru: "Given-When-Then" },
              { en: "Plan-Do-Check", ru: "Plan-Do-Check" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to write a React component test with RTL.",
          ru: "Расположите шаги написания теста React-компонента с RTL.",
        },
        items: [
          { en: "Import render, screen, and fireEvent from RTL", ru: "Импортировать render, screen и fireEvent из RTL" },
          { en: "Render the component with render(<Component />)", ru: "Отрендерить компонент с помощью render(<Component />)" },
          { en: "Query elements using screen.getByRole or screen.getByText", ru: "Найти элементы через screen.getByRole или screen.getByText" },
          { en: "Simulate user interaction with fireEvent", ru: "Симулировать действия пользователя через fireEvent" },
          { en: "Assert expected changes with expect()", ru: "Проверить ожидаемые изменения через expect()" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to write a test that checks a button click increments a counter.",
          ru: "Расположите строки, чтобы написать тест проверки увеличения счётчика по клику кнопки.",
        },
        items: [
          { en: "import { render, screen, fireEvent } from '@testing-library/react';", ru: "import { render, screen, fireEvent } from '@testing-library/react';" },
          { en: "import Counter from './Counter';", ru: "import Counter from './Counter';" },
          { en: "test('increments on click', () => {", ru: "test('increments on click', () => {" },
          { en: "  render(<Counter />);", ru: "  render(<Counter />);" },
          { en: "  fireEvent.click(screen.getByRole('button'));", ru: "  fireEvent.click(screen.getByRole('button'));" },
          { en: "  expect(screen.getByText('Count: 1')).toBeInTheDocument();", ru: "  expect(screen.getByText('Count: 1')).toBeInTheDocument();" },
          { en: "});", ru: "});" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What Jest function creates a mock function that you can track calls on?",
          ru: "Какая функция Jest создаёт мок-функцию, вызовы которой можно отслеживать?",
        },
        correctText: {
          en: "jest.fn()",
          ru: "jest.fn()",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key testing terms.",
          ru: "Повторите ключевые термины тестирования.",
        },
        pairs: [
          {
            term: { en: "Unit Test", ru: "Юнит-тест" },
            definition: {
              en: "A test that checks a single function or component in isolation",
              ru: "Тест, проверяющий отдельную функцию или компонент изолированно",
            },
          },
          {
            term: { en: "Mock", ru: "Мок" },
            definition: {
              en: "A fake implementation used to replace real dependencies in tests",
              ru: "Поддельная реализация, заменяющая реальные зависимости в тестах",
            },
          },
          {
            term: { en: "Matcher", ru: "Матчер" },
            definition: {
              en: "A Jest method like toBe or toEqual that checks a value",
              ru: "Метод Jest вроде toBe или toEqual, проверяющий значение",
            },
          },
          {
            term: { en: "waitFor", ru: "waitFor" },
            definition: {
              en: "Utility that retries assertions until they pass or timeout",
              ru: "Утилита, повторяющая проверки, пока они не пройдут или не истечёт время",
            },
          },
          {
            term: { en: "getByRole", ru: "getByRole" },
            definition: {
              en: "The preferred RTL query that finds elements by their ARIA role",
              ru: "Предпочтительный RTL-запрос, находящий элементы по их ARIA-роли",
            },
          },
        ],
      },
    ],
  },

  // ──────────────────────────────────────────────
  // Lesson 3 — Git Workflow
  // ──────────────────────────────────────────────
  "fe-23-1": {
    id: "fe-23-1",
    title: {
      en: "Git Workflow",
      ru: "Работа с Git",
    },
    slides: [
      {
        title: {
          en: "Git Basics — init, add, commit",
          ru: "Основы Git — init, add, commit",
        },
        content: {
          en: "Git is a distributed version control system that tracks changes to your code. 'git init' creates a new repository. 'git add' stages files for the next commit — you choose exactly what changes to include. 'git commit' saves a snapshot of staged changes with a message describing what was done. The .gitignore file tells Git which files to exclude from tracking, such as node_modules, .env files, and build outputs.",
          ru: "Git — распределённая система контроля версий, отслеживающая изменения в коде. 'git init' создаёт новый репозиторий. 'git add' индексирует файлы для следующего коммита — вы выбираете, какие изменения включить. 'git commit' сохраняет снимок проиндексированных изменений с сообщением о том, что было сделано. Файл .gitignore указывает Git, какие файлы исключить из отслеживания: node_modules, .env и результаты сборки.",
        },
        code: {
          language: "bash",
          code: `git init\ngit add index.html style.css\ngit commit -m "Initial commit: add HTML and CSS"\n\n# .gitignore example\nnode_modules/\n.env\ndist/\n.DS_Store`,
        },
      },
      {
        title: {
          en: "Branches & Merging",
          ru: "Ветки и слияние",
        },
        content: {
          en: "Branches let you work on features or fixes without affecting the main codebase. 'git branch feature-login' creates a branch, and 'git checkout feature-login' (or 'git switch') moves you to it. When work is done, you merge it back into the main branch. Merge conflicts happen when two branches change the same lines — Git marks the conflicting sections and you resolve them manually by choosing which changes to keep.",
          ru: "Ветки позволяют работать над функциями или исправлениями, не затрагивая основную кодовую базу. 'git branch feature-login' создаёт ветку, а 'git checkout feature-login' (или 'git switch') переключает на неё. После завершения работы ветку сливают обратно в основную. Конфликты слияния возникают, когда две ветки изменяют одни и те же строки — Git отмечает конфликтующие участки, и вы разрешаете их вручную, выбирая нужные изменения.",
        },
        code: {
          language: "bash",
          code: `git branch feature-login\ngit checkout feature-login\n# ... make changes and commit ...\ngit checkout main\ngit merge feature-login\n\n# If there's a conflict:\n<<<<<<< HEAD\nconsole.log("main version");\n=======\nconsole.log("feature version");\n>>>>>>> feature-login`,
        },
      },
      {
        title: {
          en: "Pull Requests & GitHub",
          ru: "Pull Request и GitHub",
        },
        content: {
          en: "GitHub hosts your remote repositories. After pushing a branch with 'git push -u origin feature-login', you create a Pull Request (PR) — a proposal to merge your branch into main. Team members review the code, leave comments, and approve or request changes. Once approved, the PR is merged. This workflow ensures code quality through collaboration and keeps the main branch stable.",
          ru: "GitHub хранит ваши удалённые репозитории. После отправки ветки через 'git push -u origin feature-login' вы создаёте Pull Request (PR) — предложение влить вашу ветку в main. Члены команды проверяют код, оставляют комментарии, одобряют или запрашивают изменения. После одобрения PR сливается. Этот процесс обеспечивает качество кода через сотрудничество и поддерживает стабильность основной ветки.",
        },
        code: {
          language: "bash",
          code: `# Push branch to remote\ngit push -u origin feature-login\n\n# After PR is merged, update local main\ngit checkout main\ngit pull origin main\n\n# Delete the merged branch\ngit branch -d feature-login`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does 'git add' do?",
          ru: "Что делает команда 'git add'?",
        },
        options: [
          { en: "Pushes changes to GitHub", ru: "Отправляет изменения на GitHub" },
          { en: "Stages files for the next commit", ru: "Индексирует файлы для следующего коммита" },
          { en: "Creates a new branch", ru: "Создаёт новую ветку" },
          { en: "Deletes tracked files", ru: "Удаляет отслеживаемые файлы" },
        ],
        correct: 1,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "A merge conflict occurs when the same lines are modified in two different branches.",
          ru: "Конфликт слияния возникает, когда одни и те же строки изменены в двух разных ветках.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each Git command to its purpose.",
          ru: "Сопоставьте каждую команду Git с её назначением.",
        },
        pairs: [
          {
            term: { en: "git init", ru: "git init" },
            definition: {
              en: "Initializes a new Git repository",
              ru: "Инициализирует новый Git-репозиторий",
            },
          },
          {
            term: { en: "git commit", ru: "git commit" },
            definition: {
              en: "Saves a snapshot of staged changes",
              ru: "Сохраняет снимок проиндексированных изменений",
            },
          },
          {
            term: { en: "git branch", ru: "git branch" },
            definition: {
              en: "Creates or lists branches",
              ru: "Создаёт или показывает список веток",
            },
          },
          {
            term: { en: "git merge", ru: "git merge" },
            definition: {
              en: "Combines changes from another branch",
              ru: "Объединяет изменения из другой ветки",
            },
          },
          {
            term: { en: "git push", ru: "git push" },
            definition: {
              en: "Uploads commits to a remote repository",
              ru: "Загружает коммиты в удалённый репозиторий",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about Git workflow.",
          ru: "Заполните пропуски о рабочем процессе Git.",
        },
        blanks: [
          {
            text: {
              en: "The file ___ tells Git which files and folders to ignore.",
              ru: "Файл ___ указывает Git, какие файлы и папки игнорировать.",
            },
            options: [
              { en: ".gitignore", ru: ".gitignore" },
              { en: ".gitconfig", ru: ".gitconfig" },
              { en: ".gitexclude", ru: ".gitexclude" },
              { en: ".gitkeep", ru: ".gitkeep" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To switch to an existing branch, use git ___ branch-name.",
              ru: "Чтобы переключиться на существующую ветку, используйте git ___ имя-ветки.",
            },
            options: [
              { en: "checkout", ru: "checkout" },
              { en: "change", ru: "change" },
              { en: "move", ru: "move" },
              { en: "go", ru: "go" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "A ___ is a proposal on GitHub to merge one branch into another.",
              ru: "___ — это предложение на GitHub влить одну ветку в другую.",
            },
            options: [
              { en: "Pull Request", ru: "Pull Request" },
              { en: "Merge Request", ru: "Merge Request" },
              { en: "Push Request", ru: "Push Request" },
              { en: "Code Review", ru: "Code Review" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps of a typical Git feature workflow.",
          ru: "Расположите шаги типичного Git-процесса работы над функцией.",
        },
        items: [
          { en: "Create a new branch from main", ru: "Создать новую ветку от main" },
          { en: "Make changes and stage them with git add", ru: "Внести изменения и проиндексировать их через git add" },
          { en: "Commit changes with a descriptive message", ru: "Закоммитить изменения с описательным сообщением" },
          { en: "Push the branch to the remote repository", ru: "Отправить ветку в удалённый репозиторий" },
          { en: "Open a Pull Request for code review", ru: "Открыть Pull Request для ревью кода" },
          { en: "Merge the PR into main after approval", ru: "Слить PR в main после одобрения" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the Git commands to create a feature branch, make a commit, and push it.",
          ru: "Расположите команды Git для создания ветки, коммита и отправки.",
        },
        items: [
          { en: "git checkout main", ru: "git checkout main" },
          { en: "git pull origin main", ru: "git pull origin main" },
          { en: "git checkout -b feature-header", ru: "git checkout -b feature-header" },
          { en: "git add src/Header.tsx", ru: "git add src/Header.tsx" },
          { en: "git commit -m \"feat: add Header component\"", ru: "git commit -m \"feat: add Header component\"" },
          { en: "git push -u origin feature-header", ru: "git push -u origin feature-header" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What Git command shows the current status of your working directory and staging area?",
          ru: "Какая команда Git показывает текущее состояние рабочей директории и области индексации?",
        },
        correctText: {
          en: "git status",
          ru: "git status",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key Git concepts.",
          ru: "Повторите ключевые концепции Git.",
        },
        pairs: [
          {
            term: { en: "Repository", ru: "Репозиторий" },
            definition: {
              en: "A directory tracked by Git containing your project and its history",
              ru: "Директория, отслеживаемая Git, содержащая проект и его историю",
            },
          },
          {
            term: { en: "Staging Area", ru: "Область индексации" },
            definition: {
              en: "An intermediate zone where changes are prepared before committing",
              ru: "Промежуточная зона, где изменения подготавливаются перед коммитом",
            },
          },
          {
            term: { en: "Merge Conflict", ru: "Конфликт слияния" },
            definition: {
              en: "When Git cannot auto-merge because the same lines were changed",
              ru: "Когда Git не может автоматически слить, потому что изменены одни и те же строки",
            },
          },
          {
            term: { en: "Pull Request", ru: "Pull Request" },
            definition: {
              en: "A request to review and merge a branch on GitHub",
              ru: "Запрос на проверку и слияние ветки на GitHub",
            },
          },
          {
            term: { en: ".gitignore", ru: ".gitignore" },
            definition: {
              en: "File listing patterns of files Git should not track",
              ru: "Файл с шаблонами файлов, которые Git не должен отслеживать",
            },
          },
        ],
      },
    ],
  },

  // ──────────────────────────────────────────────
  // Lesson 4 — Performance Optimization
  // ──────────────────────────────────────────────
  "fe-24-1": {
    id: "fe-24-1",
    title: {
      en: "Performance Optimization",
      ru: "Оптимизация производительности",
    },
    slides: [
      {
        title: {
          en: "React.memo, useMemo & useCallback",
          ru: "React.memo, useMemo и useCallback",
        },
        content: {
          en: "React re-renders a component whenever its parent re-renders. React.memo wraps a component so it only re-renders when its props actually change. useMemo memoizes an expensive computed value, recalculating only when its dependencies change. useCallback memoizes a function reference so child components that receive it as a prop won't re-render unnecessarily. Use these tools when profiling reveals actual performance problems — premature optimization adds complexity.",
          ru: "React перерисовывает компонент каждый раз, когда перерисовывается его родитель. React.memo оборачивает компонент, чтобы он перерисовывался только при реальном изменении пропсов. useMemo мемоизирует дорогое вычисленное значение, пересчитывая его только при изменении зависимостей. useCallback мемоизирует ссылку на функцию, чтобы дочерние компоненты, получающие её как проп, не перерисовывались напрасно. Используйте эти инструменты, когда профилирование выявляет реальные проблемы — преждевременная оптимизация усложняет код.",
        },
        code: {
          language: "typescript",
          code: `import { memo, useMemo, useCallback } from "react";\n\nconst ExpensiveList = memo(({ items, onSelect }: Props) => {\n  return items.map(item => (\n    <div key={item.id} onClick={() => onSelect(item.id)}>\n      {item.name}\n    </div>\n  ));\n});\n\nfunction Parent({ data }: { data: Item[] }) {\n  const sorted = useMemo(\n    () => [...data].sort((a, b) => a.name.localeCompare(b.name)),\n    [data]\n  );\n  const handleSelect = useCallback((id: string) => {\n    console.log("Selected:", id);\n  }, []);\n  return <ExpensiveList items={sorted} onSelect={handleSelect} />;\n}`,
        },
      },
      {
        title: {
          en: "Lazy Loading & Code Splitting",
          ru: "Ленивая загрузка и разделение кода",
        },
        content: {
          en: "By default, your entire app is bundled into one large JavaScript file. Code splitting breaks it into smaller chunks that load on demand. React.lazy lets you dynamically import components — they are only loaded when they're needed. Wrap lazy components in a Suspense boundary with a fallback UI. Route-based code splitting is the most common strategy: each page loads its own chunk only when the user navigates to it.",
          ru: "По умолчанию всё приложение собирается в один большой JavaScript-файл. Разделение кода разбивает его на небольшие чанки, загружаемые по требованию. React.lazy позволяет динамически импортировать компоненты — они загружаются только при необходимости. Оберните ленивые компоненты в Suspense с фолбэк-интерфейсом. Разделение по маршрутам — самая распространённая стратегия: каждая страница загружает свой чанк только при переходе пользователя.",
        },
        code: {
          language: "typescript",
          code: `import { lazy, Suspense } from "react";\nimport { Routes, Route } from "react-router-dom";\n\nconst Dashboard = lazy(() => import("./pages/Dashboard"));\nconst Settings = lazy(() => import("./pages/Settings"));\n\nfunction App() {\n  return (\n    <Suspense fallback={<div>Loading...</div>}>\n      <Routes>\n        <Route path="/" element={<Dashboard />} />\n        <Route path="/settings" element={<Settings />} />\n      </Routes>\n    </Suspense>\n  );\n}`,
        },
      },
      {
        title: {
          en: "Web Vitals & Lighthouse",
          ru: "Web Vitals и Lighthouse",
        },
        content: {
          en: "Core Web Vitals are Google's key metrics for user experience: LCP (Largest Contentful Paint) measures loading speed, INP (Interaction to Next Paint) measures responsiveness, and CLS (Cumulative Layout Shift) measures visual stability. Lighthouse is a tool built into Chrome DevTools that audits your page and scores performance, accessibility, SEO, and best practices. It gives actionable recommendations like compressing images, removing unused CSS, and reducing JavaScript payload.",
          ru: "Core Web Vitals — ключевые метрики Google для пользовательского опыта: LCP (Largest Contentful Paint) измеряет скорость загрузки, INP (Interaction to Next Paint) — отзывчивость, CLS (Cumulative Layout Shift) — визуальную стабильность. Lighthouse — встроенный в Chrome DevTools инструмент, который проверяет страницу и оценивает производительность, доступность, SEO и лучшие практики. Он даёт конкретные рекомендации: сжатие изображений, удаление неиспользуемого CSS, уменьшение объёма JavaScript.",
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does React.memo do?",
          ru: "Что делает React.memo?",
        },
        options: [
          { en: "Memoizes the return value of a function", ru: "Мемоизирует возвращаемое значение функции" },
          { en: "Prevents re-render when props haven't changed", ru: "Предотвращает перерисовку при неизменённых пропсах" },
          { en: "Caches API responses", ru: "Кэширует ответы API" },
          { en: "Stores component state between navigations", ru: "Сохраняет состояние компонента между переходами" },
        ],
        correct: 1,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "useMemo and useCallback should be used on every function and value to maximize performance.",
          ru: "useMemo и useCallback следует использовать для каждой функции и значения, чтобы максимизировать производительность.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each performance concept to its description.",
          ru: "Сопоставьте каждое понятие производительности с его описанием.",
        },
        pairs: [
          {
            term: { en: "React.lazy", ru: "React.lazy" },
            definition: {
              en: "Dynamically imports a component for code splitting",
              ru: "Динамически импортирует компонент для разделения кода",
            },
          },
          {
            term: { en: "Suspense", ru: "Suspense" },
            definition: {
              en: "Shows a fallback UI while lazy components load",
              ru: "Показывает фолбэк-интерфейс, пока ленивые компоненты загружаются",
            },
          },
          {
            term: { en: "LCP", ru: "LCP" },
            definition: {
              en: "Measures how fast the largest content element appears",
              ru: "Измеряет, как быстро появляется самый большой элемент контента",
            },
          },
          {
            term: { en: "CLS", ru: "CLS" },
            definition: {
              en: "Measures unexpected layout shifts during page load",
              ru: "Измеряет неожиданные сдвиги макета при загрузке страницы",
            },
          },
          {
            term: { en: "useCallback", ru: "useCallback" },
            definition: {
              en: "Memoizes a function reference to prevent child re-renders",
              ru: "Мемоизирует ссылку на функцию для предотвращения перерисовки дочерних компонентов",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about performance optimization.",
          ru: "Заполните пропуски об оптимизации производительности.",
        },
        blanks: [
          {
            text: {
              en: "The ___ hook memoizes an expensive computed value and recalculates only when dependencies change.",
              ru: "Хук ___ мемоизирует дорогое вычисленное значение и пересчитывает его только при изменении зависимостей.",
            },
            options: [
              { en: "useMemo", ru: "useMemo" },
              { en: "useState", ru: "useState" },
              { en: "useEffect", ru: "useEffect" },
              { en: "useRef", ru: "useRef" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "___ is a Chrome DevTools tool that audits page performance and gives a score out of 100.",
              ru: "___ — инструмент Chrome DevTools, который проверяет производительность страницы и даёт оценку из 100.",
            },
            options: [
              { en: "Lighthouse", ru: "Lighthouse" },
              { en: "Webpack", ru: "Webpack" },
              { en: "ESLint", ru: "ESLint" },
              { en: "Prettier", ru: "Prettier" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Route-based ___ loads each page's code only when the user navigates to that route.",
              ru: "Маршрутное ___ загружает код каждой страницы только при переходе пользователя на этот маршрут.",
            },
            options: [
              { en: "code splitting", ru: "разделение кода" },
              { en: "tree shaking", ru: "tree shaking" },
              { en: "minification", ru: "минификация" },
              { en: "bundling", ru: "сборка" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to implement lazy loading for a route in React.",
          ru: "Расположите шаги реализации ленивой загрузки для маршрута в React.",
        },
        items: [
          { en: "Import lazy and Suspense from React", ru: "Импортировать lazy и Suspense из React" },
          { en: "Create a lazy component with React.lazy(() => import(...))", ru: "Создать ленивый компонент через React.lazy(() => import(...))" },
          { en: "Wrap routes with a Suspense component", ru: "Обернуть маршруты компонентом Suspense" },
          { en: "Provide a fallback prop with a loading indicator", ru: "Указать проп fallback с индикатором загрузки" },
          { en: "Use the lazy component in a Route element", ru: "Использовать ленивый компонент в элементе Route" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a memoized component with useCallback.",
          ru: "Расположите строки для создания мемоизированного компонента с useCallback.",
        },
        items: [
          { en: "import { memo, useCallback } from 'react';", ru: "import { memo, useCallback } from 'react';" },
          { en: "const Button = memo(({ onClick, label }: Props) => {", ru: "const Button = memo(({ onClick, label }: Props) => {" },
          { en: "  return <button onClick={onClick}>{label}</button>;", ru: "  return <button onClick={onClick}>{label}</button>;" },
          { en: "});", ru: "});" },
          { en: "function Parent() {", ru: "function Parent() {" },
          { en: "  const handleClick = useCallback(() => { console.log('clicked'); }, []);", ru: "  const handleClick = useCallback(() => { console.log('clicked'); }, []);" },
          { en: "  return <Button onClick={handleClick} label=\"Click me\" />;", ru: "  return <Button onClick={handleClick} label=\"Click me\" />;" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What Core Web Vital metric measures visual stability by tracking unexpected layout shifts?",
          ru: "Какая метрика Core Web Vitals измеряет визуальную стабильность, отслеживая неожиданные сдвиги макета?",
        },
        correctText: {
          en: "CLS",
          ru: "CLS",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key performance concepts.",
          ru: "Повторите ключевые концепции производительности.",
        },
        pairs: [
          {
            term: { en: "Code Splitting", ru: "Разделение кода" },
            definition: {
              en: "Breaking a bundle into smaller chunks that load on demand",
              ru: "Разбиение бандла на маленькие чанки, загружаемые по требованию",
            },
          },
          {
            term: { en: "React.memo", ru: "React.memo" },
            definition: {
              en: "HOC that skips re-rendering when props are the same",
              ru: "HOC, пропускающий перерисовку при неизменённых пропсах",
            },
          },
          {
            term: { en: "useMemo", ru: "useMemo" },
            definition: {
              en: "Hook that caches an expensive computed value between renders",
              ru: "Хук, кэширующий дорогое вычисленное значение между рендерами",
            },
          },
          {
            term: { en: "Lighthouse", ru: "Lighthouse" },
            definition: {
              en: "Automated tool that audits web page quality and performance",
              ru: "Автоматизированный инструмент для аудита качества и производительности веб-страницы",
            },
          },
          {
            term: { en: "LCP", ru: "LCP" },
            definition: {
              en: "Largest Contentful Paint — time until the biggest visible element renders",
              ru: "Largest Contentful Paint — время до отрисовки самого большого видимого элемента",
            },
          },
        ],
      },
    ],
  },

  // ──────────────────────────────────────────────
  // Lesson 5 — Build & Deploy
  // ──────────────────────────────────────────────
  "fe-25-1": {
    id: "fe-25-1",
    title: {
      en: "Build & Deploy",
      ru: "Сборка и деплой",
    },
    slides: [
      {
        title: {
          en: "npm Scripts & Vite Build",
          ru: "npm-скрипты и сборка Vite",
        },
        content: {
          en: "npm scripts in package.json let you define common tasks: 'dev' starts the development server, 'build' creates a production bundle, and 'preview' serves the built files locally. Vite is a modern build tool that uses native ES modules during development for instant hot module replacement (HMR). For production, Vite uses Rollup under the hood to create optimized, minified bundles with tree shaking that removes unused code.",
          ru: "npm-скрипты в package.json позволяют задать типичные задачи: 'dev' запускает сервер разработки, 'build' создаёт продакшн-сборку, 'preview' раздаёт собранные файлы локально. Vite — современный инструмент сборки, использующий нативные ES-модули при разработке для мгновенной горячей замены модулей (HMR). Для продакшна Vite использует Rollup для создания оптимизированных, минифицированных бандлов с tree shaking, удаляющим неиспользуемый код.",
        },
        code: {
          language: "json",
          code: `{\n  "scripts": {\n    "dev": "vite",\n    "build": "tsc && vite build",\n    "preview": "vite preview",\n    "lint": "eslint src --ext .ts,.tsx",\n    "test": "vitest"\n  }\n}`,
        },
      },
      {
        title: {
          en: "Environment Variables",
          ru: "Переменные окружения",
        },
        content: {
          en: "Environment variables store configuration that changes between environments — like API URLs, feature flags, or API keys. In Vite, variables must be prefixed with VITE_ to be exposed to the client. Create .env files for different environments: .env for defaults, .env.local for local overrides, .env.production for production values. Access them in code with import.meta.env.VITE_API_URL. Never commit secrets to Git — add .env.local to .gitignore.",
          ru: "Переменные окружения хранят конфигурацию, которая меняется между средами — URL API, фича-флаги или ключи API. В Vite переменные должны иметь префикс VITE_, чтобы быть доступными на клиенте. Создавайте .env-файлы для разных сред: .env для значений по умолчанию, .env.local для локальных переопределений, .env.production для продакшн-значений. Доступ в коде через import.meta.env.VITE_API_URL. Никогда не коммитьте секреты в Git — добавьте .env.local в .gitignore.",
        },
        code: {
          language: "bash",
          code: `# .env\nVITE_APP_TITLE=My App\nVITE_API_URL=http://localhost:3001/api\n\n# .env.production\nVITE_API_URL=https://api.myapp.com\n\n# In your code:\nconst apiUrl = import.meta.env.VITE_API_URL;`,
        },
      },
      {
        title: {
          en: "Deploy to Vercel/Netlify & CI/CD Basics",
          ru: "Деплой на Vercel/Netlify и основы CI/CD",
        },
        content: {
          en: "Vercel and Netlify are platforms that deploy frontend apps directly from a Git repository. Connect your GitHub repo, set the build command (e.g., npm run build) and output directory (dist), and every push to main triggers an automatic deploy. Pull requests get preview deployments with unique URLs. CI/CD (Continuous Integration / Continuous Deployment) automates testing and deployment: a pipeline runs linting, tests, builds, and deploys on every push, ensuring code quality before it reaches production.",
          ru: "Vercel и Netlify — платформы, деплоящие фронтенд-приложения прямо из Git-репозитория. Подключите GitHub-репозиторий, укажите команду сборки (например, npm run build) и директорию вывода (dist) — и каждый push в main автоматически запускает деплой. Pull Request получают превью-деплои с уникальными URL. CI/CD (непрерывная интеграция / непрерывный деплой) автоматизирует тестирование и развёртывание: пайплайн запускает линтинг, тесты, сборку и деплой при каждом push, гарантируя качество кода перед попаданием в продакшн.",
        },
        code: {
          language: "yaml",
          code: `# .github/workflows/ci.yml\nname: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-node@v4\n        with:\n          node-version: 20\n      - run: npm ci\n      - run: npm run lint\n      - run: npm run test\n      - run: npm run build`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "In Vite, what prefix must environment variables have to be accessible in client code?",
          ru: "Какой префикс должны иметь переменные окружения в Vite для доступа из клиентского кода?",
        },
        options: [
          { en: "REACT_APP_", ru: "REACT_APP_" },
          { en: "VITE_", ru: "VITE_" },
          { en: "PUBLIC_", ru: "PUBLIC_" },
          { en: "NEXT_PUBLIC_", ru: "NEXT_PUBLIC_" },
        ],
        correct: 1,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "Vercel and Netlify can automatically deploy your app every time you push to the main branch.",
          ru: "Vercel и Netlify могут автоматически деплоить ваше приложение при каждом push в ветку main.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each build/deploy concept to its description.",
          ru: "Сопоставьте каждое понятие сборки/деплоя с его описанием.",
        },
        pairs: [
          {
            term: { en: "npm run build", ru: "npm run build" },
            definition: {
              en: "Creates an optimized production bundle",
              ru: "Создаёт оптимизированную продакшн-сборку",
            },
          },
          {
            term: { en: ".env file", ru: "Файл .env" },
            definition: {
              en: "Stores environment-specific configuration values",
              ru: "Хранит конфигурационные значения для конкретной среды",
            },
          },
          {
            term: { en: "CI/CD pipeline", ru: "CI/CD пайплайн" },
            definition: {
              en: "Automates testing and deployment on every code push",
              ru: "Автоматизирует тестирование и деплой при каждом push кода",
            },
          },
          {
            term: { en: "Preview deployment", ru: "Превью-деплой" },
            definition: {
              en: "A temporary deploy created for a pull request",
              ru: "Временный деплой, создаваемый для pull request",
            },
          },
          {
            term: { en: "Tree shaking", ru: "Tree shaking" },
            definition: {
              en: "Removes unused code from the final bundle",
              ru: "Удаляет неиспользуемый код из итогового бандла",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about building and deploying.",
          ru: "Заполните пропуски о сборке и деплое.",
        },
        blanks: [
          {
            text: {
              en: "Vite uses ___ under the hood to create optimized production bundles.",
              ru: "Vite использует ___ для создания оптимизированных продакшн-сборок.",
            },
            options: [
              { en: "Rollup", ru: "Rollup" },
              { en: "Webpack", ru: "Webpack" },
              { en: "Parcel", ru: "Parcel" },
              { en: "esbuild", ru: "esbuild" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The output directory for a Vite build is ___ by default.",
              ru: "Директория вывода для сборки Vite по умолчанию — ___.",
            },
            options: [
              { en: "dist", ru: "dist" },
              { en: "build", ru: "build" },
              { en: "out", ru: "out" },
              { en: "public", ru: "public" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "In Vite, you access environment variables using import.meta.___.",
              ru: "В Vite доступ к переменным окружения осуществляется через import.meta.___.",
            },
            options: [
              { en: "env", ru: "env" },
              { en: "config", ru: "config" },
              { en: "vars", ru: "vars" },
              { en: "process", ru: "process" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps of a CI/CD pipeline for a frontend project.",
          ru: "Расположите шаги CI/CD пайплайна для фронтенд-проекта.",
        },
        items: [
          { en: "Push code to the repository", ru: "Отправить код в репозиторий" },
          { en: "CI server installs dependencies (npm ci)", ru: "CI-сервер устанавливает зависимости (npm ci)" },
          { en: "Run linting to check code style", ru: "Запустить линтинг для проверки стиля кода" },
          { en: "Run tests to verify correctness", ru: "Запустить тесты для проверки корректности" },
          { en: "Build the production bundle", ru: "Собрать продакшн-сборку" },
          { en: "Deploy to hosting platform", ru: "Задеплоить на хостинг-платформу" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a basic GitHub Actions CI workflow.",
          ru: "Расположите строки для создания базового CI-процесса в GitHub Actions.",
        },
        items: [
          { en: "name: CI", ru: "name: CI" },
          { en: "on: [push, pull_request]", ru: "on: [push, pull_request]" },
          { en: "jobs:", ru: "jobs:" },
          { en: "  build:", ru: "  build:" },
          { en: "    runs-on: ubuntu-latest", ru: "    runs-on: ubuntu-latest" },
          { en: "    steps:", ru: "    steps:" },
          { en: "      - run: npm ci && npm run build", ru: "      - run: npm ci && npm run build" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What npm command installs dependencies from package-lock.json for a clean, reproducible install in CI?",
          ru: "Какая команда npm устанавливает зависимости из package-lock.json для чистой, воспроизводимой установки в CI?",
        },
        correctText: {
          en: "npm ci",
          ru: "npm ci",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key build and deploy terms.",
          ru: "Повторите ключевые термины сборки и деплоя.",
        },
        pairs: [
          {
            term: { en: "Vite", ru: "Vite" },
            definition: {
              en: "A fast build tool using ES modules in dev and Rollup for production",
              ru: "Быстрый инструмент сборки, использующий ES-модули при разработке и Rollup для продакшна",
            },
          },
          {
            term: { en: "HMR", ru: "HMR" },
            definition: {
              en: "Hot Module Replacement — updates code in the browser without a full reload",
              ru: "Hot Module Replacement — обновляет код в браузере без полной перезагрузки",
            },
          },
          {
            term: { en: "CI/CD", ru: "CI/CD" },
            definition: {
              en: "Continuous Integration and Continuous Deployment — automated test and deploy pipeline",
              ru: "Непрерывная интеграция и непрерывный деплой — автоматизированный пайплайн тестирования и развёртывания",
            },
          },
          {
            term: { en: "Environment Variable", ru: "Переменная окружения" },
            definition: {
              en: "A configuration value that changes between development and production",
              ru: "Конфигурационное значение, которое отличается между разработкой и продакшном",
            },
          },
          {
            term: { en: "Preview Deploy", ru: "Превью-деплой" },
            definition: {
              en: "A temporary deployment for a PR that lets reviewers test changes live",
              ru: "Временный деплой для PR, позволяющий ревьюерам тестировать изменения вживую",
            },
          },
        ],
      },
    ],
  },
};
