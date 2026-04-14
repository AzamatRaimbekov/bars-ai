import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_V2_MIDDLE_JS: Record<string, LessonContentV2> = {
  /* ═══════════════════════════════════════════════════════════════
     fe-10-1  — Variables & Types
     ═══════════════════════════════════════════════════════════════ */
  "fe-10-1": {
    id: "fe-10-1",
    title: {
      en: "Variables & Types",
      ru: "Переменные и типы данных",
    },
    slides: [
      {
        title: {
          en: "Declaring Variables: let, const, var",
          ru: "Объявление переменных: let, const, var",
        },
        content: {
          en: "JavaScript offers three keywords for declaring variables. `var` is function-scoped and hoisted — it was the only option before ES6. `let` is block-scoped and can be reassigned. `const` is also block-scoped but cannot be reassigned after initialization. Modern code avoids `var` in favor of `const` by default and `let` when reassignment is needed.",
          ru: "JavaScript предлагает три ключевых слова для объявления переменных. `var` имеет функциональную область видимости и поднимается (hoisting) — до ES6 это был единственный вариант. `let` имеет блочную область видимости и допускает переприсваивание. `const` тоже имеет блочную область видимости, но не допускает переприсваивание после инициализации. В современном коде вместо `var` предпочитают `const` по умолчанию, а `let` — когда нужно переприсваивание.",
        },
        code: {
          language: "javascript",
          code: `var oldWay = "hoisted, function-scoped";\nlet counter = 0;\ncounter = 1; // OK — let allows reassignment\n\nconst API_URL = "https://api.example.com";\n// API_URL = "other"; // TypeError — const cannot be reassigned`,
        },
      },
      {
        title: {
          en: "Primitive Types",
          ru: "Примитивные типы",
        },
        content: {
          en: "JavaScript has seven primitive types: string, number, boolean, null, undefined, symbol, and bigint. Strings represent text and can use single quotes, double quotes, or backticks. Numbers cover both integers and floats (there is no separate int type). Booleans are true or false. null is an intentional absence of value, while undefined means a variable has been declared but not assigned.",
          ru: "В JavaScript семь примитивных типов: string, number, boolean, null, undefined, symbol и bigint. Строки (string) представляют текст и могут использовать одинарные, двойные кавычки или обратные апострофы. Числа (number) охватывают целые и дробные (отдельного типа int нет). Boolean — это true или false. null означает намеренное отсутствие значения, а undefined — что переменная объявлена, но не инициализирована.",
        },
        code: {
          language: "javascript",
          code: `const name = "Alice";      // string\nconst age = 25;            // number\nconst pi = 3.14;           // number (same type)\nconst isOnline = true;     // boolean\nconst nothing = null;      // null\nlet score;                 // undefined\nconsole.log(typeof name);  // "string"\nconsole.log(typeof age);   // "number"\nconsole.log(typeof nothing); // "object" (historical bug)`,
        },
      },
      {
        title: {
          en: "The typeof Operator",
          ru: "Оператор typeof",
        },
        content: {
          en: "The `typeof` operator returns a string indicating the type of its operand. It works on any value and is especially useful for runtime type checks. Be aware of two quirks: `typeof null` returns \"object\" (a well-known JS bug kept for backward compatibility), and `typeof` for an undeclared variable returns \"undefined\" instead of throwing an error.",
          ru: "Оператор `typeof` возвращает строку, указывающую тип операнда. Он работает с любым значением и особенно полезен для проверки типов во время выполнения. Учтите две особенности: `typeof null` возвращает \"object\" (известный баг JS, сохранённый для обратной совместимости), а `typeof` для необъявленной переменной возвращает \"undefined\" вместо ошибки.",
        },
        code: {
          language: "javascript",
          code: `console.log(typeof "hello");   // "string"\nconsole.log(typeof 42);        // "number"\nconsole.log(typeof true);      // "boolean"\nconsole.log(typeof undefined); // "undefined"\nconsole.log(typeof null);      // "object"  ← quirk!\nconsole.log(typeof {});        // "object"\nconsole.log(typeof []);        // "object"\nconsole.log(typeof function(){}); // "function"`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which keyword declares a block-scoped variable that cannot be reassigned?",
          ru: "Какое ключевое слово объявляет переменную с блочной областью видимости, которую нельзя переприсвоить?",
        },
        options: [
          { en: "var", ru: "var" },
          { en: "let", ru: "let" },
          { en: "const", ru: "const" },
          { en: "static", ru: "static" },
        ],
        correct: 2,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "typeof null returns \"null\" in JavaScript.",
          ru: "typeof null возвращает \"null\" в JavaScript.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each value to its typeof result.",
          ru: "Сопоставьте каждое значение с результатом typeof.",
        },
        pairs: [
          {
            term: { en: '"hello"', ru: '"hello"' },
            definition: { en: '"string"', ru: '"string"' },
          },
          {
            term: { en: "42", ru: "42" },
            definition: { en: '"number"', ru: '"number"' },
          },
          {
            term: { en: "true", ru: "true" },
            definition: { en: '"boolean"', ru: '"boolean"' },
          },
          {
            term: { en: "undefined", ru: "undefined" },
            definition: { en: '"undefined"', ru: '"undefined"' },
          },
          {
            term: { en: "null", ru: "null" },
            definition: { en: '"object"', ru: '"object"' },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about variable declarations.",
          ru: "Заполните пропуски о способах объявления переменных.",
        },
        blanks: [
          {
            text: {
              en: "___ is function-scoped and hoisted.",
              ru: "___ имеет функциональную область видимости и поднимается.",
            },
            options: [
              { en: "var", ru: "var" },
              { en: "let", ru: "let" },
              { en: "const", ru: "const" },
              { en: "def", ru: "def" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "___ is block-scoped and allows reassignment.",
              ru: "___ имеет блочную область видимости и допускает переприсваивание.",
            },
            options: [
              { en: "var", ru: "var" },
              { en: "let", ru: "let" },
              { en: "const", ru: "const" },
              { en: "set", ru: "set" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "A variable declared but not assigned has the value ___.",
              ru: "Переменная, объявленная, но не инициализированная, имеет значение ___.",
            },
            options: [
              { en: "null", ru: "null" },
              { en: "0", ru: "0" },
              { en: "undefined", ru: "undefined" },
              { en: '""', ru: '""' },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order these steps to correctly declare and use a constant:",
          ru: "Расположите шаги для правильного объявления и использования константы:",
        },
        items: [
          { en: "Choose the const keyword", ru: "Выбрать ключевое слово const" },
          { en: "Give the variable a name", ru: "Дать переменной имя" },
          { en: "Use the = assignment operator", ru: "Использовать оператор присваивания =" },
          { en: "Provide the initial value", ru: "Указать начальное значение" },
          { en: "Use the constant in expressions", ru: "Использовать константу в выражениях" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to declare variables and log their types:",
          ru: "Расположите строки кода для объявления переменных и вывода их типов:",
        },
        items: [
          { en: 'const name = "Alice";', ru: 'const name = "Alice";' },
          { en: "let age = 25;", ru: "let age = 25;" },
          { en: "const isActive = true;", ru: "const isActive = true;" },
          { en: "console.log(typeof name);", ru: "console.log(typeof name);" },
          { en: "console.log(typeof age);", ru: "console.log(typeof age);" },
          { en: "console.log(typeof isActive);", ru: "console.log(typeof isActive);" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What does typeof [] return in JavaScript? (one word, in quotes)",
          ru: "Что возвращает typeof [] в JavaScript? (одно слово, в кавычках)",
        },
        correctText: { en: '"object"', ru: '"object"' },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key concepts about JavaScript variables and types.",
          ru: "Повторите ключевые понятия о переменных и типах данных JavaScript.",
        },
        pairs: [
          {
            term: { en: "var", ru: "var" },
            definition: {
              en: "Function-scoped variable declaration, hoisted to the top",
              ru: "Объявление переменной с функциональной областью видимости, поднимается наверх",
            },
          },
          {
            term: { en: "let", ru: "let" },
            definition: {
              en: "Block-scoped variable that can be reassigned",
              ru: "Переменная с блочной областью видимости, допускает переприсваивание",
            },
          },
          {
            term: { en: "const", ru: "const" },
            definition: {
              en: "Block-scoped variable that cannot be reassigned",
              ru: "Переменная с блочной областью видимости, не допускает переприсваивание",
            },
          },
          {
            term: { en: "typeof", ru: "typeof" },
            definition: {
              en: "Operator that returns the type of a value as a string",
              ru: "Оператор, возвращающий тип значения в виде строки",
            },
          },
          {
            term: { en: "undefined", ru: "undefined" },
            definition: {
              en: "Default value of a declared but unassigned variable",
              ru: "Значение по умолчанию для объявленной, но не инициализированной переменной",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-10-2  — Control Flow
     ═══════════════════════════════════════════════════════════════ */
  "fe-10-2": {
    id: "fe-10-2",
    title: {
      en: "Control Flow",
      ru: "Управление потоком выполнения",
    },
    slides: [
      {
        title: {
          en: "Conditional Statements: if / else / switch",
          ru: "Условные конструкции: if / else / switch",
        },
        content: {
          en: "Conditional statements let your code make decisions. `if` executes a block when a condition is truthy. You can chain `else if` for multiple branches and `else` as a fallback. The `switch` statement compares a value against multiple `case` labels using strict equality (===). Always include `break` in each case to prevent fall-through, and use `default` as a catch-all.",
          ru: "Условные конструкции позволяют коду принимать решения. `if` выполняет блок, когда условие истинно. Можно выстроить цепочку `else if` для нескольких ветвей, а `else` — как запасной вариант. Оператор `switch` сравнивает значение с несколькими метками `case` через строгое равенство (===). Всегда добавляйте `break` в каждом case, чтобы избежать «проваливания», и используйте `default` как вариант по умолчанию.",
        },
        code: {
          language: "javascript",
          code: `const role = "admin";\n\nif (role === "admin") {\n  console.log("Full access");\n} else if (role === "editor") {\n  console.log("Edit access");\n} else {\n  console.log("Read-only");\n}\n\nswitch (role) {\n  case "admin":  console.log("Full");  break;\n  case "editor": console.log("Edit");  break;\n  default:       console.log("Read");\n}`,
        },
      },
      {
        title: {
          en: "Loops: for, while, for...of",
          ru: "Циклы: for, while, for...of",
        },
        content: {
          en: "Loops repeat a block of code. The classic `for` loop uses an initializer, condition, and increment. `while` runs as long as its condition is true — be sure the condition eventually becomes false or you'll get an infinite loop. `for...of` iterates over iterable objects like arrays and strings, giving you each value directly without needing an index.",
          ru: "Циклы повторяют блок кода. Классический цикл `for` использует инициализатор, условие и инкремент. `while` выполняется, пока условие истинно — убедитесь, что условие в конечном итоге станет ложным, иначе получите бесконечный цикл. `for...of` перебирает итерируемые объекты, такие как массивы и строки, сразу давая каждое значение без необходимости в индексе.",
        },
        code: {
          language: "javascript",
          code: `// Classic for loop\nfor (let i = 0; i < 5; i++) {\n  console.log(i); // 0, 1, 2, 3, 4\n}\n\n// while loop\nlet n = 3;\nwhile (n > 0) {\n  console.log(n); // 3, 2, 1\n  n--;\n}\n\n// for...of loop\nconst colors = ["red", "green", "blue"];\nfor (const color of colors) {\n  console.log(color);\n}`,
        },
      },
      {
        title: {
          en: "The Ternary Operator",
          ru: "Тернарный оператор",
        },
        content: {
          en: "The ternary operator `condition ? valueIfTrue : valueIfFalse` is a compact alternative to if/else for simple expressions. It returns one of two values based on a condition. It is great for inline assignments and template strings. Avoid nesting ternaries — if logic gets complex, use if/else for readability.",
          ru: "Тернарный оператор `условие ? значениеЕслиTrue : значениеЕслиFalse` — компактная альтернатива if/else для простых выражений. Он возвращает одно из двух значений в зависимости от условия. Отлично подходит для встроенных присваиваний и шаблонных строк. Избегайте вложенных тернарных операторов — если логика сложная, используйте if/else для читаемости.",
        },
        code: {
          language: "javascript",
          code: `const age = 20;\nconst status = age >= 18 ? "adult" : "minor";\nconsole.log(status); // "adult"\n\n// Useful in template strings\nconst user = { name: "Bob", isAdmin: false };\nconsole.log(\`Role: \${user.isAdmin ? "Admin" : "User"}\`);`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What comparison does the switch statement use in JavaScript?",
          ru: "Какое сравнение использует оператор switch в JavaScript?",
        },
        options: [
          { en: "Loose equality (==)", ru: "Нестрогое равенство (==)" },
          { en: "Strict equality (===)", ru: "Строгое равенство (===)" },
          { en: "Object.is()", ru: "Object.is()" },
          { en: "Deep equality", ru: "Глубокое равенство" },
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
          en: "A for...of loop gives you the index of each element in an array.",
          ru: "Цикл for...of даёт индекс каждого элемента массива.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each control flow construct to its description.",
          ru: "Сопоставьте каждую конструкцию управления потоком с её описанием.",
        },
        pairs: [
          {
            term: { en: "if / else", ru: "if / else" },
            definition: {
              en: "Executes code blocks based on a boolean condition",
              ru: "Выполняет блоки кода в зависимости от логического условия",
            },
          },
          {
            term: { en: "switch", ru: "switch" },
            definition: {
              en: "Compares a value against multiple case labels",
              ru: "Сравнивает значение с несколькими метками case",
            },
          },
          {
            term: { en: "for", ru: "for" },
            definition: {
              en: "Loop with initializer, condition, and increment",
              ru: "Цикл с инициализатором, условием и инкрементом",
            },
          },
          {
            term: { en: "for...of", ru: "for...of" },
            definition: {
              en: "Iterates over values of an iterable object",
              ru: "Перебирает значения итерируемого объекта",
            },
          },
          {
            term: { en: "ternary ?:", ru: "тернарный ?:" },
            definition: {
              en: "Inline conditional expression returning one of two values",
              ru: "Встроенное условное выражение, возвращающее одно из двух значений",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about loops.",
          ru: "Заполните пропуски о циклах.",
        },
        blanks: [
          {
            text: {
              en: "A ___ loop runs as long as its condition is true.",
              ru: "Цикл ___ выполняется, пока его условие истинно.",
            },
            options: [
              { en: "while", ru: "while" },
              { en: "for...of", ru: "for...of" },
              { en: "switch", ru: "switch" },
              { en: "if", ru: "if" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "In a switch statement, you must use ___ to prevent fall-through.",
              ru: "В операторе switch нужно использовать ___, чтобы избежать проваливания.",
            },
            options: [
              { en: "return", ru: "return" },
              { en: "break", ru: "break" },
              { en: "continue", ru: "continue" },
              { en: "stop", ru: "stop" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "The ___ operator is a shorthand for if/else that returns a value.",
              ru: "Оператор ___ — это сокращённая форма if/else, возвращающая значение.",
            },
            options: [
              { en: "spread", ru: "spread" },
              { en: "typeof", ru: "typeof" },
              { en: "ternary", ru: "тернарный" },
              { en: "void", ru: "void" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the parts of a classic for loop:",
          ru: "Расположите части классического цикла for по порядку:",
        },
        items: [
          { en: "for keyword", ru: "ключевое слово for" },
          { en: "Initializer (let i = 0)", ru: "Инициализатор (let i = 0)" },
          { en: "Condition (i < 10)", ru: "Условие (i < 10)" },
          { en: "Increment (i++)", ru: "Инкремент (i++)" },
          { en: "Loop body { ... }", ru: "Тело цикла { ... }" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to iterate over an array and log only even numbers:",
          ru: "Расположите строки кода для перебора массива и вывода только чётных чисел:",
        },
        items: [
          { en: "const nums = [1, 2, 3, 4, 5, 6];", ru: "const nums = [1, 2, 3, 4, 5, 6];" },
          { en: "for (const n of nums) {", ru: "for (const n of nums) {" },
          { en: "  if (n % 2 === 0) {", ru: "  if (n % 2 === 0) {" },
          { en: "    console.log(n);", ru: "    console.log(n);" },
          { en: "  }", ru: "  }" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What keyword creates the fallback branch in a switch statement?",
          ru: "Какое ключевое слово создаёт ветку по умолчанию в операторе switch?",
        },
        correctText: { en: "default", ru: "default" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review control flow concepts.",
          ru: "Повторите понятия управления потоком выполнения.",
        },
        pairs: [
          {
            term: { en: "if / else", ru: "if / else" },
            definition: {
              en: "Branching based on a truthy/falsy condition",
              ru: "Ветвление на основе истинности/ложности условия",
            },
          },
          {
            term: { en: "switch / case", ru: "switch / case" },
            definition: {
              en: "Multi-branch comparison using strict equality",
              ru: "Многовариантное сравнение с использованием строгого равенства",
            },
          },
          {
            term: { en: "for loop", ru: "цикл for" },
            definition: {
              en: "Counter-based loop: init; condition; update",
              ru: "Цикл со счётчиком: инициализация; условие; обновление",
            },
          },
          {
            term: { en: "for...of", ru: "for...of" },
            definition: {
              en: "Iterates directly over values in arrays, strings, etc.",
              ru: "Перебирает значения массивов, строк и других итерируемых объектов",
            },
          },
          {
            term: { en: "Ternary operator", ru: "Тернарный оператор" },
            definition: {
              en: "condition ? trueValue : falseValue — inline conditional",
              ru: "условие ? значениеTrue : значениеFalse — встроенное условие",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-11-1  — Functions & Closures
     ═══════════════════════════════════════════════════════════════ */
  "fe-11-1": {
    id: "fe-11-1",
    title: {
      en: "Functions & Closures",
      ru: "Функции и замыкания",
    },
    slides: [
      {
        title: {
          en: "Function Declarations and Expressions",
          ru: "Объявления и выражения функций",
        },
        content: {
          en: "A function declaration uses the `function` keyword and is hoisted — you can call it before it appears in code. A function expression assigns a function to a variable; it is not hoisted. Arrow functions (`=>`) provide shorter syntax, do not have their own `this`, and are always expressions. Use arrow functions for callbacks and short helpers.",
          ru: "Объявление функции (function declaration) использует ключевое слово `function` и поднимается — её можно вызвать до места объявления в коде. Функциональное выражение (function expression) присваивает функцию переменной; оно не поднимается. Стрелочные функции (`=>`) обеспечивают более короткий синтаксис, не имеют собственного `this` и всегда являются выражениями. Используйте стрелочные функции для колбэков и коротких вспомогательных функций.",
        },
        code: {
          language: "javascript",
          code: `// Declaration — hoisted\nfunction greet(name) {\n  return "Hello, " + name;\n}\n\n// Expression — NOT hoisted\nconst add = function(a, b) {\n  return a + b;\n};\n\n// Arrow function\nconst multiply = (a, b) => a * b;\nconst square = x => x * x; // single param, no parens needed`,
        },
      },
      {
        title: {
          en: "Closures & Scope Chain",
          ru: "Замыкания и цепочка областей видимости",
        },
        content: {
          en: "A closure is a function that remembers variables from its outer (lexical) scope even after the outer function has returned. Every function in JavaScript forms a closure. The scope chain is the hierarchy of scopes the engine checks when resolving a variable — starting from the local scope, moving outward to enclosing functions, and finally to the global scope.",
          ru: "Замыкание — это функция, которая запоминает переменные из своей внешней (лексической) области видимости, даже после того как внешняя функция завершилась. Каждая функция в JavaScript формирует замыкание. Цепочка областей видимости — это иерархия областей, которые движок проверяет при разрешении переменной: от локальной, через внешние функции, до глобальной.",
        },
        code: {
          language: "javascript",
          code: `function createCounter() {\n  let count = 0; // enclosed variable\n  return {\n    increment: () => ++count,\n    getCount: () => count,\n  };\n}\n\nconst counter = createCounter();\ncounter.increment();\ncounter.increment();\nconsole.log(counter.getCount()); // 2\n// count is not accessible directly — it's private via closure`,
        },
      },
      {
        title: {
          en: "IIFE (Immediately Invoked Function Expression)",
          ru: "IIFE (немедленно вызываемое функциональное выражение)",
        },
        content: {
          en: "An IIFE is a function that runs immediately after it is defined. It creates an isolated scope, preventing variable leaks into the global scope. The pattern wraps the function in parentheses and then calls it: `(function() { ... })()`. Before ES6 modules, IIFEs were the main way to create private scopes. They are still useful for one-time initialization logic.",
          ru: "IIFE — это функция, которая выполняется сразу после определения. Она создаёт изолированную область видимости, предотвращая утечку переменных в глобальную область. Шаблон оборачивает функцию в скобки и затем вызывает её: `(function() { ... })()`. До модулей ES6 IIFE были основным способом создания приватных областей видимости. Они по-прежнему полезны для одноразовой инициализации.",
        },
        code: {
          language: "javascript",
          code: `// Classic IIFE\n(function() {\n  const secret = "hidden";\n  console.log(secret); // "hidden"\n})();\n// console.log(secret); // ReferenceError\n\n// Arrow IIFE\n(() => {\n  const config = { debug: false };\n  console.log("App initialized");\n})();`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which type of function does NOT have its own `this` context?",
          ru: "Какой тип функции НЕ имеет собственного контекста `this`?",
        },
        options: [
          { en: "Function declaration", ru: "Объявление функции" },
          { en: "Function expression", ru: "Функциональное выражение" },
          { en: "Arrow function", ru: "Стрелочная функция" },
          { en: "Generator function", ru: "Функция-генератор" },
        ],
        correct: 2,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "Function declarations are hoisted, so you can call them before they appear in the code.",
          ru: "Объявления функций поднимаются, поэтому их можно вызвать до места появления в коде.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each concept to its description.",
          ru: "Сопоставьте каждое понятие с его описанием.",
        },
        pairs: [
          {
            term: { en: "Closure", ru: "Замыкание" },
            definition: {
              en: "Function that remembers variables from its outer scope",
              ru: "Функция, запоминающая переменные из внешней области видимости",
            },
          },
          {
            term: { en: "Scope chain", ru: "Цепочка областей видимости" },
            definition: {
              en: "Hierarchy of scopes checked when resolving a variable",
              ru: "Иерархия областей, проверяемых при разрешении переменной",
            },
          },
          {
            term: { en: "IIFE", ru: "IIFE" },
            definition: {
              en: "Function that runs immediately after definition",
              ru: "Функция, выполняемая сразу после определения",
            },
          },
          {
            term: { en: "Arrow function", ru: "Стрелочная функция" },
            definition: {
              en: "Shorter syntax, inherits this from enclosing scope",
              ru: "Короткий синтаксис, наследует this из объемлющей области",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about functions and closures.",
          ru: "Заполните пропуски о функциях и замыканиях.",
        },
        blanks: [
          {
            text: {
              en: "A ___ remembers variables from its outer scope even after the outer function returns.",
              ru: "___ запоминает переменные из внешней области видимости даже после завершения внешней функции.",
            },
            options: [
              { en: "closure", ru: "замыкание" },
              { en: "prototype", ru: "прототип" },
              { en: "constructor", ru: "конструктор" },
              { en: "module", ru: "модуль" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Arrow functions do not have their own ___ context.",
              ru: "Стрелочные функции не имеют собственного контекста ___.",
            },
            options: [
              { en: "this", ru: "this" },
              { en: "scope", ru: "scope" },
              { en: "var", ru: "var" },
              { en: "return", ru: "return" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "An IIFE creates an ___ scope that prevents variable leaks.",
              ru: "IIFE создаёт ___ область видимости, предотвращающую утечку переменных.",
            },
            options: [
              { en: "global", ru: "глобальную" },
              { en: "isolated", ru: "изолированную" },
              { en: "async", ru: "асинхронную" },
              { en: "static", ru: "статическую" },
            ],
            correctIndex: 1,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order these scope levels from innermost to outermost:",
          ru: "Расположите уровни области видимости от внутреннего к внешнему:",
        },
        items: [
          { en: "Local (function) scope", ru: "Локальная (функциональная) область" },
          { en: "Enclosing function scope", ru: "Область объемлющей функции" },
          { en: "Module scope", ru: "Область модуля" },
          { en: "Global scope", ru: "Глобальная область" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to create a counter using a closure:",
          ru: "Расположите строки для создания счётчика с помощью замыкания:",
        },
        items: [
          { en: "function makeCounter() {", ru: "function makeCounter() {" },
          { en: "  let count = 0;", ru: "  let count = 0;" },
          { en: "  return () => ++count;", ru: "  return () => ++count;" },
          { en: "}", ru: "}" },
          { en: "const counter = makeCounter();", ru: "const counter = makeCounter();" },
          { en: "console.log(counter());", ru: "console.log(counter());" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What does IIFE stand for? (full phrase)",
          ru: "Как расшифровывается IIFE? (полная фраза на английском)",
        },
        correctText: {
          en: "Immediately Invoked Function Expression",
          ru: "Immediately Invoked Function Expression",
        },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review functions and closures.",
          ru: "Повторите понятия о функциях и замыканиях.",
        },
        pairs: [
          {
            term: { en: "Function declaration", ru: "Объявление функции" },
            definition: {
              en: "Hoisted; can be called before the line where it's defined",
              ru: "Поднимается; можно вызвать до строки определения",
            },
          },
          {
            term: { en: "Function expression", ru: "Функциональное выражение" },
            definition: {
              en: "Assigned to a variable; NOT hoisted",
              ru: "Присваивается переменной; НЕ поднимается",
            },
          },
          {
            term: { en: "Arrow function", ru: "Стрелочная функция" },
            definition: {
              en: "Concise syntax with () => {}; inherits this from outer scope",
              ru: "Краткий синтаксис () => {}; наследует this из внешней области",
            },
          },
          {
            term: { en: "Closure", ru: "Замыкание" },
            definition: {
              en: "Inner function retaining access to outer function's variables",
              ru: "Внутренняя функция сохраняет доступ к переменным внешней функции",
            },
          },
          {
            term: { en: "IIFE", ru: "IIFE" },
            definition: {
              en: "(function() { ... })() — runs immediately, creates isolated scope",
              ru: "(function() { ... })() — запускается сразу, создаёт изолированную область",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-12-1  — Array Methods
     ═══════════════════════════════════════════════════════════════ */
  "fe-12-1": {
    id: "fe-12-1",
    title: {
      en: "Array Methods",
      ru: "Методы массивов",
    },
    slides: [
      {
        title: {
          en: "Transforming Arrays: map, filter, reduce",
          ru: "Преобразование массивов: map, filter, reduce",
        },
        content: {
          en: "`map` creates a new array by transforming each element with a callback. `filter` creates a new array with only elements that pass a test. `reduce` accumulates all elements into a single value using a callback and an initial accumulator. All three return a new value — the original array is not mutated.",
          ru: "`map` создаёт новый массив, преобразуя каждый элемент с помощью колбэка. `filter` создаёт новый массив, оставляя только элементы, прошедшие проверку. `reduce` накапливает все элементы в одно значение с помощью колбэка и начального аккумулятора. Все три метода возвращают новое значение — исходный массив не изменяется.",
        },
        code: {
          language: "javascript",
          code: `const nums = [1, 2, 3, 4, 5];\n\nconst doubled = nums.map(n => n * 2);\n// [2, 4, 6, 8, 10]\n\nconst evens = nums.filter(n => n % 2 === 0);\n// [2, 4]\n\nconst sum = nums.reduce((acc, n) => acc + n, 0);\n// 15`,
        },
      },
      {
        title: {
          en: "Searching & Testing: find, some, every",
          ru: "Поиск и проверка: find, some, every",
        },
        content: {
          en: "`find` returns the first element that satisfies a test, or undefined if none match. `some` returns true if at least one element passes the test. `every` returns true only if all elements pass. These methods short-circuit — they stop iterating as soon as the result is determined. `forEach` simply executes a function for each element and returns undefined.",
          ru: "`find` возвращает первый элемент, удовлетворяющий условию, или undefined, если ничего не найдено. `some` возвращает true, если хотя бы один элемент проходит проверку. `every` возвращает true, только если все элементы проходят. Эти методы выполняют «короткое замыкание» — прекращают перебор, как только результат определён. `forEach` просто выполняет функцию для каждого элемента и возвращает undefined.",
        },
        code: {
          language: "javascript",
          code: `const users = [\n  { name: "Alice", age: 25 },\n  { name: "Bob", age: 17 },\n  { name: "Carol", age: 30 },\n];\n\nconst bob = users.find(u => u.name === "Bob");\n// { name: "Bob", age: 17 }\n\nconst hasMinor = users.some(u => u.age < 18);  // true\nconst allAdults = users.every(u => u.age >= 18); // false\n\nusers.forEach(u => console.log(u.name));`,
        },
      },
      {
        title: {
          en: "Sorting & Slicing: sort, slice, splice",
          ru: "Сортировка и нарезка: sort, slice, splice",
        },
        content: {
          en: "`sort` sorts an array in-place. By default it converts elements to strings and compares UTF-16 code units, so always pass a comparator for numbers: `(a, b) => a - b`. `slice(start, end)` returns a shallow copy of a portion of an array without modifying the original. `splice(start, deleteCount, ...items)` modifies the original array by removing/inserting elements.",
          ru: "`sort` сортирует массив на месте. По умолчанию он преобразует элементы в строки и сравнивает по кодам UTF-16, поэтому для чисел всегда передавайте компаратор: `(a, b) => a - b`. `slice(start, end)` возвращает неглубокую копию части массива без изменения оригинала. `splice(start, deleteCount, ...items)` изменяет исходный массив, удаляя/вставляя элементы.",
        },
        code: {
          language: "javascript",
          code: `const arr = [3, 1, 4, 1, 5];\n\n// sort mutates the original\narr.sort((a, b) => a - b); // [1, 1, 3, 4, 5]\n\n// slice does NOT mutate\nconst mid = arr.slice(1, 3); // [1, 3]\n\n// splice mutates — remove 1 element at index 2, insert 99\narr.splice(2, 1, 99); // arr is now [1, 1, 99, 4, 5]`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which array method returns a single accumulated value?",
          ru: "Какой метод массива возвращает единственное накопленное значение?",
        },
        options: [
          { en: "map", ru: "map" },
          { en: "filter", ru: "filter" },
          { en: "reduce", ru: "reduce" },
          { en: "find", ru: "find" },
        ],
        correct: 2,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "The slice() method modifies the original array.",
          ru: "Метод slice() изменяет исходный массив.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each array method to what it returns.",
          ru: "Сопоставьте каждый метод массива с тем, что он возвращает.",
        },
        pairs: [
          {
            term: { en: "map", ru: "map" },
            definition: {
              en: "New array with transformed elements",
              ru: "Новый массив с преобразованными элементами",
            },
          },
          {
            term: { en: "filter", ru: "filter" },
            definition: {
              en: "New array with elements that pass a test",
              ru: "Новый массив с элементами, прошедшими проверку",
            },
          },
          {
            term: { en: "find", ru: "find" },
            definition: {
              en: "First element matching a condition, or undefined",
              ru: "Первый элемент, соответствующий условию, или undefined",
            },
          },
          {
            term: { en: "some", ru: "some" },
            definition: {
              en: "Boolean: true if at least one element matches",
              ru: "Boolean: true, если хотя бы один элемент соответствует",
            },
          },
          {
            term: { en: "every", ru: "every" },
            definition: {
              en: "Boolean: true only if all elements match",
              ru: "Boolean: true, только если все элементы соответствуют",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about array methods.",
          ru: "Заполните пропуски о методах массивов.",
        },
        blanks: [
          {
            text: {
              en: "___ creates a new array by applying a function to each element.",
              ru: "___ создаёт новый массив, применяя функцию к каждому элементу.",
            },
            options: [
              { en: "map", ru: "map" },
              { en: "forEach", ru: "forEach" },
              { en: "reduce", ru: "reduce" },
              { en: "find", ru: "find" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To sort numbers correctly you must pass a ___ function.",
              ru: "Для правильной сортировки чисел нужно передать функцию ___.",
            },
            options: [
              { en: "callback", ru: "обратного вызова" },
              { en: "comparator", ru: "компаратор" },
              { en: "reducer", ru: "редьюсер" },
              { en: "mapper", ru: "маппер" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "___ modifies the original array by removing or inserting elements.",
              ru: "___ изменяет исходный массив, удаляя или вставляя элементы.",
            },
            options: [
              { en: "slice", ru: "slice" },
              { en: "concat", ru: "concat" },
              { en: "splice", ru: "splice" },
              { en: "map", ru: "map" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to calculate the sum of prices over $10:",
          ru: "Расположите шаги для подсчёта суммы цен свыше $10:",
        },
        items: [
          { en: "Start with an array of products", ru: "Начать с массива товаров" },
          { en: "Filter products with price > 10", ru: "Отфильтровать товары с ценой > 10" },
          { en: "Map to extract the price values", ru: "Применить map для извлечения цен" },
          { en: "Reduce to sum all prices", ru: "Применить reduce для суммирования всех цен" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to get names of users older than 18:",
          ru: "Расположите строки для получения имён пользователей старше 18:",
        },
        items: [
          { en: "const users = [", ru: "const users = [" },
          {
            en: '  { name: "Alice", age: 25 }, { name: "Bob", age: 16 },',
            ru: '  { name: "Alice", age: 25 }, { name: "Bob", age: 16 },',
          },
          { en: "];", ru: "];" },
          { en: "const adultNames = users", ru: "const adultNames = users" },
          { en: "  .filter(u => u.age > 18)", ru: "  .filter(u => u.age > 18)" },
          { en: "  .map(u => u.name);", ru: "  .map(u => u.name);" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What does [1,2,3].filter(n => n > 1) return? (write the array)",
          ru: "Что вернёт [1,2,3].filter(n => n > 1)? (напишите массив)",
        },
        correctText: { en: "[2, 3]", ru: "[2, 3]" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review array methods.",
          ru: "Повторите методы массивов.",
        },
        pairs: [
          {
            term: { en: "map()", ru: "map()" },
            definition: {
              en: "Transforms each element; returns a new array of the same length",
              ru: "Преобразует каждый элемент; возвращает новый массив той же длины",
            },
          },
          {
            term: { en: "filter()", ru: "filter()" },
            definition: {
              en: "Returns a new array of elements that pass a test",
              ru: "Возвращает новый массив элементов, прошедших проверку",
            },
          },
          {
            term: { en: "reduce()", ru: "reduce()" },
            definition: {
              en: "Accumulates all elements into a single value",
              ru: "Накапливает все элементы в одно значение",
            },
          },
          {
            term: { en: "splice()", ru: "splice()" },
            definition: {
              en: "Mutates the array: removes and/or inserts elements in place",
              ru: "Изменяет массив: удаляет и/или вставляет элементы на месте",
            },
          },
          {
            term: { en: "slice()", ru: "slice()" },
            definition: {
              en: "Returns a shallow copy of a portion of the array (non-mutating)",
              ru: "Возвращает неглубокую копию части массива (без изменения оригинала)",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-12-2  — Object Patterns
     ═══════════════════════════════════════════════════════════════ */
  "fe-12-2": {
    id: "fe-12-2",
    title: {
      en: "Object Patterns",
      ru: "Паттерны работы с объектами",
    },
    slides: [
      {
        title: {
          en: "Object Literals & Destructuring",
          ru: "Литералы объектов и деструктуризация",
        },
        content: {
          en: "Object literals let you create objects with key-value pairs using curly braces. ES6 added shorthand property names (when variable name matches the key) and shorthand methods. Destructuring extracts properties into separate variables in one statement. You can rename properties and provide default values during destructuring.",
          ru: "Литералы объектов позволяют создавать объекты с парами ключ-значение с помощью фигурных скобок. ES6 добавил сокращённые имена свойств (когда имя переменной совпадает с ключом) и сокращённые методы. Деструктуризация извлекает свойства в отдельные переменные за одно выражение. При деструктуризации можно переименовывать свойства и задавать значения по умолчанию.",
        },
        code: {
          language: "javascript",
          code: `// Shorthand property names\nconst name = "Alice";\nconst age = 25;\nconst user = { name, age }; // same as { name: name, age: age }\n\n// Destructuring\nconst { name: userName, age: userAge } = user;\nconsole.log(userName); // "Alice"\n\n// Default values\nconst { role = "viewer" } = user;\nconsole.log(role); // "viewer"`,
        },
      },
      {
        title: {
          en: "Spread Operator & Computed Properties",
          ru: "Оператор spread и вычисляемые свойства",
        },
        content: {
          en: "The spread operator (`...`) copies all enumerable properties from one object into another. It is commonly used to create shallow copies or merge objects — later properties overwrite earlier ones. Computed property names use square brackets to dynamically set a key from an expression or variable.",
          ru: "Оператор spread (`...`) копирует все перечисляемые свойства из одного объекта в другой. Его часто используют для создания неглубоких копий или слияния объектов — более поздние свойства перезаписывают более ранние. Вычисляемые имена свойств используют квадратные скобки для динамической установки ключа из выражения или переменной.",
        },
        code: {
          language: "javascript",
          code: "const defaults = { theme: \"light\", lang: \"en\" };\nconst overrides = { lang: \"ru\", debug: true };\nconst config = { ...defaults, ...overrides };\n// { theme: \"light\", lang: \"ru\", debug: true }\n\n// Computed property names\nconst field = \"email\";\nconst formData = {\n  [field]: \"alice@example.com\",\n  [field + \"Confirmed\"]: true,\n};\n// { email: \"alice@example.com\", emailConfirmed: true }",
        },
      },
      {
        title: {
          en: "Object.keys, Object.values, Object.entries",
          ru: "Object.keys, Object.values, Object.entries",
        },
        content: {
          en: "`Object.keys(obj)` returns an array of the object's own enumerable property names. `Object.values(obj)` returns an array of their values. `Object.entries(obj)` returns an array of [key, value] pairs — perfect for iterating with for...of or transforming with array methods. These static methods work only on own properties, not inherited ones.",
          ru: "`Object.keys(obj)` возвращает массив имён собственных перечисляемых свойств объекта. `Object.values(obj)` возвращает массив их значений. `Object.entries(obj)` возвращает массив пар [ключ, значение] — идеально для перебора через for...of или преобразования методами массивов. Эти статические методы работают только с собственными свойствами, а не унаследованными.",
        },
        code: {
          language: "javascript",
          code: `const product = { name: "Laptop", price: 999, inStock: true };\n\nObject.keys(product);    // ["name", "price", "inStock"]\nObject.values(product);  // ["Laptop", 999, true]\nObject.entries(product); // [["name","Laptop"], ["price",999], ["inStock",true]]\n\n// Practical: convert to query string\nconst qs = Object.entries(product)\n  .map(([k, v]) => \`\${k}=\${v}\`)\n  .join("&");\n// "name=Laptop&price=999&inStock=true"`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does Object.entries() return?",
          ru: "Что возвращает Object.entries()?",
        },
        options: [
          { en: "An array of keys", ru: "Массив ключей" },
          { en: "An array of values", ru: "Массив значений" },
          { en: "An array of [key, value] pairs", ru: "Массив пар [ключ, значение]" },
          { en: "A new object", ru: "Новый объект" },
        ],
        correct: 2,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "The spread operator (...) creates a deep copy of an object.",
          ru: "Оператор spread (...) создаёт глубокую копию объекта.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each object technique to its description.",
          ru: "Сопоставьте каждый приём работы с объектами с его описанием.",
        },
        pairs: [
          {
            term: { en: "Destructuring", ru: "Деструктуризация" },
            definition: {
              en: "Extract properties into individual variables",
              ru: "Извлечь свойства в отдельные переменные",
            },
          },
          {
            term: { en: "Spread (...)", ru: "Spread (...)" },
            definition: {
              en: "Copy/merge object properties into a new object",
              ru: "Копировать/объединить свойства в новый объект",
            },
          },
          {
            term: { en: "Computed properties", ru: "Вычисляемые свойства" },
            definition: {
              en: "Use an expression in brackets as a property key",
              ru: "Использовать выражение в скобках как ключ свойства",
            },
          },
          {
            term: { en: "Shorthand properties", ru: "Сокращённые свойства" },
            definition: {
              en: "Use variable name as both key and value",
              ru: "Использовать имя переменной как ключ и значение",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about object patterns.",
          ru: "Заполните пропуски о паттернах объектов.",
        },
        blanks: [
          {
            text: {
              en: "Object.___(obj) returns an array of the object's keys.",
              ru: "Object.___(obj) возвращает массив ключей объекта.",
            },
            options: [
              { en: "keys", ru: "keys" },
              { en: "values", ru: "values" },
              { en: "entries", ru: "entries" },
              { en: "assign", ru: "assign" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "In destructuring, you can rename a property using a ___.",
              ru: "При деструктуризации можно переименовать свойство с помощью ___.",
            },
            options: [
              { en: "colon (:)", ru: "двоеточия (:)" },
              { en: "equals (=)", ru: "знака равенства (=)" },
              { en: "comma (,)", ru: "запятой (,)" },
              { en: "dot (.)", ru: "точки (.)" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The spread operator creates a ___ copy of an object.",
              ru: "Оператор spread создаёт ___ копию объекта.",
            },
            options: [
              { en: "deep", ru: "глубокую" },
              { en: "shallow", ru: "неглубокую" },
              { en: "frozen", ru: "замороженную" },
              { en: "sealed", ru: "запечатанную" },
            ],
            correctIndex: 1,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to merge two objects and destructure the result:",
          ru: "Расположите шаги для слияния двух объектов и деструктуризации результата:",
        },
        items: [
          { en: "Define the first object", ru: "Определить первый объект" },
          { en: "Define the second object", ru: "Определить второй объект" },
          { en: "Spread both into a new object", ru: "Развернуть оба в новый объект" },
          { en: "Destructure the merged result", ru: "Деструктуризировать результат слияния" },
          { en: "Use the extracted variables", ru: "Использовать извлечённые переменные" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to destructure a user and log their info:",
          ru: "Расположите строки для деструктуризации пользователя и вывода информации:",
        },
        items: [
          { en: "const user = {", ru: "const user = {" },
          {
            en: '  name: "Alice", age: 25, role: "admin"',
            ru: '  name: "Alice", age: 25, role: "admin"',
          },
          { en: "};", ru: "};" },
          { en: "const { name, role } = user;", ru: "const { name, role } = user;" },
          {
            en: "console.log(`${name} is ${role}`);",
            ru: "console.log(`${name} is ${role}`);",
          },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: 'What does Object.keys({ a: 1, b: 2 }) return? (write the array)',
          ru: 'Что вернёт Object.keys({ a: 1, b: 2 })? (напишите массив)',
        },
        correctText: { en: '["a", "b"]', ru: '["a", "b"]' },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review object patterns.",
          ru: "Повторите паттерны работы с объектами.",
        },
        pairs: [
          {
            term: { en: "Object literal", ru: "Литерал объекта" },
            definition: {
              en: "Create objects with { key: value } syntax",
              ru: "Создание объектов с синтаксисом { ключ: значение }",
            },
          },
          {
            term: { en: "Destructuring", ru: "Деструктуризация" },
            definition: {
              en: "const { a, b } = obj — extract properties into variables",
              ru: "const { a, b } = obj — извлечение свойств в переменные",
            },
          },
          {
            term: { en: "Spread", ru: "Spread" },
            definition: {
              en: "{ ...obj } — shallow-copy or merge objects",
              ru: "{ ...obj } — неглубокое копирование или слияние объектов",
            },
          },
          {
            term: { en: "Object.entries()", ru: "Object.entries()" },
            definition: {
              en: "Returns array of [key, value] pairs from an object",
              ru: "Возвращает массив пар [ключ, значение] из объекта",
            },
          },
          {
            term: { en: "Computed properties", ru: "Вычисляемые свойства" },
            definition: {
              en: "{ [expression]: value } — dynamic keys from variables",
              ru: "{ [выражение]: значение } — динамические ключи из переменных",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-13-1  — DOM API
     ═══════════════════════════════════════════════════════════════ */
  "fe-13-1": {
    id: "fe-13-1",
    title: {
      en: "DOM API",
      ru: "DOM API",
    },
    slides: [
      {
        title: {
          en: "Selecting & Creating Elements",
          ru: "Выбор и создание элементов",
        },
        content: {
          en: "`document.querySelector(selector)` returns the first element matching a CSS selector. `document.querySelectorAll(selector)` returns a NodeList of all matches. `document.createElement(tag)` creates a new element in memory — you must append it to the DOM for it to appear. Use `parentNode.appendChild(el)` or `parent.append(el)` to attach it.",
          ru: "`document.querySelector(selector)` возвращает первый элемент, соответствующий CSS-селектору. `document.querySelectorAll(selector)` возвращает NodeList всех совпадений. `document.createElement(tag)` создаёт новый элемент в памяти — его нужно добавить в DOM, чтобы он появился на странице. Используйте `parentNode.appendChild(el)` или `parent.append(el)` для присоединения.",
        },
        code: {
          language: "javascript",
          code: `// Select existing elements\nconst title = document.querySelector("h1");\nconst items = document.querySelectorAll(".list-item");\n\n// Create and append a new element\nconst btn = document.createElement("button");\nbtn.textContent = "Click me";\ndocument.body.appendChild(btn);`,
        },
      },
      {
        title: {
          en: "Event Listeners & classList",
          ru: "Обработчики событий и classList",
        },
        content: {
          en: "`element.addEventListener(event, handler)` attaches an event listener without overwriting existing ones. Common events: 'click', 'input', 'submit', 'keydown'. The `classList` property provides methods to manipulate CSS classes: `add`, `remove`, `toggle`, and `contains`. This is the modern replacement for manually editing `className` strings.",
          ru: "`element.addEventListener(event, handler)` прикрепляет обработчик события, не перезаписывая существующие. Распространённые события: 'click', 'input', 'submit', 'keydown'. Свойство `classList` предоставляет методы для управления CSS-классами: `add`, `remove`, `toggle` и `contains`. Это современная замена ручному редактированию строк `className`.",
        },
        code: {
          language: "javascript",
          code: `const btn = document.querySelector("#myBtn");\n\nbtn.addEventListener("click", () => {\n  btn.classList.toggle("active");\n  console.log("Clicked!");\n});\n\n// Multiple classes at once\nbtn.classList.add("primary", "large");\nbtn.classList.remove("disabled");\nconsole.log(btn.classList.contains("active")); // true or false`,
        },
      },
      {
        title: {
          en: "Content: textContent vs innerHTML",
          ru: "Контент: textContent vs innerHTML",
        },
        content: {
          en: "`textContent` gets or sets the text content of a node — it is safe from XSS because HTML is not parsed. `innerHTML` gets or sets the HTML markup inside an element — it parses HTML, so never insert user input directly. `parentNode` gives access to an element's parent for traversal. Use these properties together to dynamically update the page.",
          ru: "`textContent` получает или задаёт текстовое содержимое узла — это безопасно от XSS, так как HTML не парсится. `innerHTML` получает или задаёт HTML-разметку внутри элемента — HTML парсится, поэтому никогда не вставляйте пользовательский ввод напрямую. `parentNode` даёт доступ к родителю элемента для навигации. Используйте эти свойства вместе для динамического обновления страницы.",
        },
        code: {
          language: "javascript",
          code: `const el = document.querySelector("#info");\n\n// Safe — only text\nel.textContent = "Hello, <b>World</b>";\n// Renders as literal text: Hello, <b>World</b>\n\n// Parses HTML — use carefully\nel.innerHTML = "<strong>Bold text</strong>";\n// Renders: Bold text\n\n// Navigate to parent\nconst parent = el.parentNode;\nparent.classList.add("highlight");`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which method returns ALL elements matching a CSS selector?",
          ru: "Какой метод возвращает ВСЕ элементы, соответствующие CSS-селектору?",
        },
        options: [
          { en: "querySelector", ru: "querySelector" },
          { en: "querySelectorAll", ru: "querySelectorAll" },
          { en: "getElementById", ru: "getElementById" },
          { en: "createElement", ru: "createElement" },
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
          en: "textContent parses HTML tags inserted into it.",
          ru: "textContent парсит HTML-теги, вставленные в него.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each DOM method/property to its purpose.",
          ru: "Сопоставьте каждый метод/свойство DOM с его назначением.",
        },
        pairs: [
          {
            term: { en: "querySelector", ru: "querySelector" },
            definition: {
              en: "Returns the first element matching a selector",
              ru: "Возвращает первый элемент, соответствующий селектору",
            },
          },
          {
            term: { en: "createElement", ru: "createElement" },
            definition: {
              en: "Creates a new DOM element in memory",
              ru: "Создаёт новый DOM-элемент в памяти",
            },
          },
          {
            term: { en: "addEventListener", ru: "addEventListener" },
            definition: {
              en: "Attaches an event handler to an element",
              ru: "Прикрепляет обработчик события к элементу",
            },
          },
          {
            term: { en: "classList.toggle", ru: "classList.toggle" },
            definition: {
              en: "Adds a class if absent, removes if present",
              ru: "Добавляет класс, если отсутствует; удаляет, если присутствует",
            },
          },
          {
            term: { en: "parentNode", ru: "parentNode" },
            definition: {
              en: "Reference to the element's parent in the DOM tree",
              ru: "Ссылка на родительский элемент в дереве DOM",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about the DOM API.",
          ru: "Заполните пропуски о DOM API.",
        },
        blanks: [
          {
            text: {
              en: 'document.___("button") creates a new button element.',
              ru: 'document.___("button") создаёт новый элемент button.',
            },
            options: [
              { en: "createElement", ru: "createElement" },
              { en: "querySelector", ru: "querySelector" },
              { en: "appendChild", ru: "appendChild" },
              { en: "getElementById", ru: "getElementById" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "___ is safe from XSS because it does not parse HTML.",
              ru: "___ безопасен от XSS, потому что не парсит HTML.",
            },
            options: [
              { en: "innerHTML", ru: "innerHTML" },
              { en: "textContent", ru: "textContent" },
              { en: "outerHTML", ru: "outerHTML" },
              { en: "innerText", ru: "innerText" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "classList.___(\"active\") adds the class if missing, removes if present.",
              ru: "classList.___(\"active\") добавляет класс, если его нет, и удаляет, если есть.",
            },
            options: [
              { en: "add", ru: "add" },
              { en: "remove", ru: "remove" },
              { en: "toggle", ru: "toggle" },
              { en: "contains", ru: "contains" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to create a button, style it, and add a click handler:",
          ru: "Расположите шаги для создания кнопки, стилизации и добавления обработчика клика:",
        },
        items: [
          { en: "Create the element with createElement", ru: "Создать элемент с помощью createElement" },
          { en: "Set textContent for the button label", ru: "Задать textContent для текста кнопки" },
          { en: "Add CSS classes with classList.add", ru: "Добавить CSS-классы через classList.add" },
          { en: "Attach a click listener with addEventListener", ru: "Прикрепить обработчик клика через addEventListener" },
          { en: "Append the button to the DOM", ru: "Добавить кнопку в DOM" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to create a list item and add it to a <ul>:",
          ru: "Расположите строки для создания элемента списка и добавления его в <ul>:",
        },
        items: [
          { en: 'const ul = document.querySelector("#myList");', ru: 'const ul = document.querySelector("#myList");' },
          { en: 'const li = document.createElement("li");', ru: 'const li = document.createElement("li");' },
          { en: 'li.textContent = "New item";', ru: 'li.textContent = "New item";' },
          { en: 'li.classList.add("list-item");', ru: 'li.classList.add("list-item");' },
          { en: "ul.appendChild(li);", ru: "ul.appendChild(li);" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "Which property gives access to an element's parent in the DOM?",
          ru: "Какое свойство даёт доступ к родителю элемента в DOM?",
        },
        correctText: { en: "parentNode", ru: "parentNode" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review DOM API concepts.",
          ru: "Повторите понятия DOM API.",
        },
        pairs: [
          {
            term: { en: "querySelector", ru: "querySelector" },
            definition: {
              en: "Selects the first element matching a CSS selector",
              ru: "Выбирает первый элемент, соответствующий CSS-селектору",
            },
          },
          {
            term: { en: "createElement", ru: "createElement" },
            definition: {
              en: "Creates a new HTML element in memory (not yet in DOM)",
              ru: "Создаёт новый HTML-элемент в памяти (ещё не в DOM)",
            },
          },
          {
            term: { en: "addEventListener", ru: "addEventListener" },
            definition: {
              en: "Registers an event handler without overwriting existing ones",
              ru: "Регистрирует обработчик без перезаписи существующих",
            },
          },
          {
            term: { en: "textContent", ru: "textContent" },
            definition: {
              en: "Gets/sets plain text of a node — safe from XSS",
              ru: "Получает/задаёт текст узла — безопасно от XSS",
            },
          },
          {
            term: { en: "innerHTML", ru: "innerHTML" },
            definition: {
              en: "Gets/sets HTML markup — parses HTML, beware of XSS",
              ru: "Получает/задаёт HTML-разметку — парсит HTML, осторожно с XSS",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-14-1  — Promises & Async/Await
     ═══════════════════════════════════════════════════════════════ */
  "fe-14-1": {
    id: "fe-14-1",
    title: {
      en: "Promises & Async/Await",
      ru: "Промисы и Async/Await",
    },
    slides: [
      {
        title: {
          en: "The Promise Constructor & .then/.catch",
          ru: "Конструктор Promise и .then/.catch",
        },
        content: {
          en: "A Promise represents a value that may not be available yet. You create one with `new Promise((resolve, reject) => { ... })`. Call `resolve(value)` on success, `reject(error)` on failure. Chain `.then(callback)` to handle the resolved value, and `.catch(callback)` to handle errors. Promises are always asynchronous — callbacks run after the current call stack clears.",
          ru: "Promise представляет значение, которое может быть ещё недоступно. Создаётся через `new Promise((resolve, reject) => { ... })`. Вызовите `resolve(value)` при успехе, `reject(error)` при ошибке. Цепочка `.then(callback)` обрабатывает успешное значение, а `.catch(callback)` — ошибки. Промисы всегда асинхронны — колбэки выполняются после очистки текущего стека вызовов.",
        },
        code: {
          language: "javascript",
          code: `const fetchUser = new Promise((resolve, reject) => {\n  setTimeout(() => {\n    const success = true;\n    if (success) {\n      resolve({ name: "Alice", age: 25 });\n    } else {\n      reject(new Error("User not found"));\n    }\n  }, 1000);\n});\n\nfetchUser\n  .then(user => console.log(user.name)) // "Alice"\n  .catch(err => console.error(err.message));`,
        },
      },
      {
        title: {
          en: "Async/Await Syntax",
          ru: "Синтаксис Async/Await",
        },
        content: {
          en: "`async` functions always return a Promise. Inside them, `await` pauses execution until a Promise resolves, making asynchronous code look synchronous. Use `try/catch` around `await` for error handling. This is the preferred modern pattern — it is easier to read and debug than long `.then()` chains.",
          ru: "Функции с `async` всегда возвращают Promise. Внутри них `await` приостанавливает выполнение до разрешения промиса, что делает асинхронный код похожим на синхронный. Используйте `try/catch` вокруг `await` для обработки ошибок. Это предпочтительный современный паттерн — его легче читать и отлаживать, чем длинные цепочки `.then()`.",
        },
        code: {
          language: "javascript",
          code: `async function loadProfile(userId) {\n  try {\n    const response = await fetch(\`/api/users/\${userId}\`);\n    const data = await response.json();\n    console.log(data.name);\n    return data;\n  } catch (error) {\n    console.error("Failed to load:", error.message);\n  }\n}\n\nloadProfile(42);`,
        },
      },
      {
        title: {
          en: "Promise.all & Concurrent Requests",
          ru: "Promise.all и параллельные запросы",
        },
        content: {
          en: "`Promise.all(iterable)` takes an array of Promises and returns a single Promise that resolves when ALL input promises resolve. The result is an array of values in the same order. If any promise rejects, Promise.all rejects immediately with that error. Use it when you need multiple independent async operations to complete before proceeding.",
          ru: "`Promise.all(iterable)` принимает массив промисов и возвращает один промис, который разрешается, когда ВСЕ входные промисы разрешены. Результат — массив значений в том же порядке. Если какой-либо промис отклоняется, Promise.all немедленно отклоняется с этой ошибкой. Используйте его, когда нужно завершить несколько независимых асинхронных операций перед продолжением.",
        },
        code: {
          language: "javascript",
          code: `async function loadDashboard() {\n  try {\n    const [user, posts, stats] = await Promise.all([\n      fetch("/api/user").then(r => r.json()),\n      fetch("/api/posts").then(r => r.json()),\n      fetch("/api/stats").then(r => r.json()),\n    ]);\n    console.log(user, posts, stats);\n  } catch (error) {\n    console.error("One request failed:", error);\n  }\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What happens when one promise in Promise.all() rejects?",
          ru: "Что произойдёт, если один из промисов в Promise.all() будет отклонён?",
        },
        options: [
          { en: "It waits for all to finish, then rejects", ru: "Ждёт завершения всех, затем отклоняется" },
          { en: "It rejects immediately with that error", ru: "Немедленно отклоняется с этой ошибкой" },
          { en: "It ignores the rejected promise", ru: "Игнорирует отклонённый промис" },
          { en: "It returns null for that promise", ru: "Возвращает null для этого промиса" },
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
          en: "An async function always returns a Promise, even if you return a plain value.",
          ru: "Функция async всегда возвращает Promise, даже если вы возвращаете обычное значение.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each async concept to its description.",
          ru: "Сопоставьте каждое асинхронное понятие с его описанием.",
        },
        pairs: [
          {
            term: { en: "resolve()", ru: "resolve()" },
            definition: {
              en: "Marks a promise as successfully completed",
              ru: "Отмечает промис как успешно завершённый",
            },
          },
          {
            term: { en: "reject()", ru: "reject()" },
            definition: {
              en: "Marks a promise as failed with an error",
              ru: "Отмечает промис как завершённый с ошибкой",
            },
          },
          {
            term: { en: "await", ru: "await" },
            definition: {
              en: "Pauses async function until a promise settles",
              ru: "Приостанавливает async-функцию до разрешения промиса",
            },
          },
          {
            term: { en: "Promise.all()", ru: "Promise.all()" },
            definition: {
              en: "Resolves when all promises in the array resolve",
              ru: "Разрешается, когда все промисы в массиве разрешены",
            },
          },
          {
            term: { en: ".catch()", ru: ".catch()" },
            definition: {
              en: "Handles errors from a promise chain",
              ru: "Обрабатывает ошибки из цепочки промисов",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about Promises.",
          ru: "Заполните пропуски о промисах.",
        },
        blanks: [
          {
            text: {
              en: "A promise is created with new ___((resolve, reject) => { }).",
              ru: "Промис создаётся через new ___((resolve, reject) => { }).",
            },
            options: [
              { en: "Promise", ru: "Promise" },
              { en: "Async", ru: "Async" },
              { en: "Await", ru: "Await" },
              { en: "Callback", ru: "Callback" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Inside an async function, use ___ to pause until a promise resolves.",
              ru: "Внутри async-функции используйте ___ для ожидания разрешения промиса.",
            },
            options: [
              { en: "yield", ru: "yield" },
              { en: "await", ru: "await" },
              { en: "then", ru: "then" },
              { en: "resolve", ru: "resolve" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "Use ___ / catch around await for error handling.",
              ru: "Используйте ___ / catch вокруг await для обработки ошибок.",
            },
            options: [
              { en: "if", ru: "if" },
              { en: "switch", ru: "switch" },
              { en: "try", ru: "try" },
              { en: "while", ru: "while" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the lifecycle of a Promise:",
          ru: "Расположите этапы жизненного цикла промиса:",
        },
        items: [
          { en: "Promise is created (pending state)", ru: "Промис создан (состояние pending)" },
          { en: "Async operation runs", ru: "Выполняется асинхронная операция" },
          { en: "resolve() or reject() is called", ru: "Вызывается resolve() или reject()" },
          { en: "Promise settles (fulfilled or rejected)", ru: "Промис завершается (fulfilled или rejected)" },
          { en: ".then() or .catch() callback fires", ru: "Срабатывает колбэк .then() или .catch()" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to fetch data with async/await and error handling:",
          ru: "Расположите строки для получения данных с async/await и обработкой ошибок:",
        },
        items: [
          { en: "async function getUser() {", ru: "async function getUser() {" },
          { en: "  try {", ru: "  try {" },
          { en: '    const res = await fetch("/api/user");', ru: '    const res = await fetch("/api/user");' },
          { en: "    const data = await res.json();", ru: "    const data = await res.json();" },
          { en: "    return data;", ru: "    return data;" },
          { en: "  } catch (e) { console.error(e); }", ru: "  } catch (e) { console.error(e); }" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What keyword must appear before a function so you can use await inside it?",
          ru: "Какое ключевое слово должно стоять перед функцией, чтобы внутри неё можно было использовать await?",
        },
        correctText: { en: "async", ru: "async" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review Promises and async/await.",
          ru: "Повторите промисы и async/await.",
        },
        pairs: [
          {
            term: { en: "Promise", ru: "Promise" },
            definition: {
              en: "Object representing an eventual completion or failure of an async operation",
              ru: "Объект, представляющий возможное завершение или провал асинхронной операции",
            },
          },
          {
            term: { en: "async", ru: "async" },
            definition: {
              en: "Keyword that makes a function return a Promise",
              ru: "Ключевое слово, которое заставляет функцию возвращать Promise",
            },
          },
          {
            term: { en: "await", ru: "await" },
            definition: {
              en: "Pauses execution until the Promise resolves",
              ru: "Приостанавливает выполнение до разрешения промиса",
            },
          },
          {
            term: { en: "Promise.all()", ru: "Promise.all()" },
            definition: {
              en: "Runs promises concurrently; resolves when all succeed",
              ru: "Запускает промисы параллельно; разрешается, когда все успешны",
            },
          },
          {
            term: { en: "try / catch", ru: "try / catch" },
            definition: {
              en: "Error handling pattern for synchronous code and await",
              ru: "Паттерн обработки ошибок для синхронного кода и await",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-14-2  — Fetch API
     ═══════════════════════════════════════════════════════════════ */
  "fe-14-2": {
    id: "fe-14-2",
    title: {
      en: "Fetch API",
      ru: "Fetch API",
    },
    slides: [
      {
        title: {
          en: "Basic Fetch: GET Requests",
          ru: "Базовый Fetch: GET-запросы",
        },
        content: {
          en: "`fetch(url)` sends a GET request by default and returns a Promise that resolves to a Response object. The response has a `ok` property (true for 200-299 status codes) and methods like `.json()`, `.text()`, `.blob()` to parse the body. Note that fetch does NOT reject on HTTP errors (404, 500) — it only rejects on network failures. Always check `response.ok`.",
          ru: "`fetch(url)` по умолчанию отправляет GET-запрос и возвращает Promise, который разрешается в объект Response. У ответа есть свойство `ok` (true для кодов 200-299) и методы `.json()`, `.text()`, `.blob()` для парсинга тела. Обратите внимание, что fetch НЕ отклоняется при HTTP-ошибках (404, 500) — он отклоняется только при сетевых сбоях. Всегда проверяйте `response.ok`.",
        },
        code: {
          language: "javascript",
          code: `async function getUsers() {\n  const response = await fetch("https://api.example.com/users");\n\n  if (!response.ok) {\n    throw new Error(\`HTTP \${response.status}\`);\n  }\n\n  const users = await response.json();\n  console.log(users);\n}`,
        },
      },
      {
        title: {
          en: "POST Requests & Headers",
          ru: "POST-запросы и заголовки",
        },
        content: {
          en: "To send data, pass an options object with `method`, `headers`, and `body`. For JSON data, set the Content-Type header to \"application/json\" and stringify the body with `JSON.stringify()`. The server reads the body and typically responds with the created resource. Other methods (PUT, PATCH, DELETE) work the same way.",
          ru: "Для отправки данных передайте объект настроек с `method`, `headers` и `body`. Для JSON-данных установите заголовок Content-Type в \"application/json\" и преобразуйте тело с помощью `JSON.stringify()`. Сервер читает тело и обычно отвечает созданным ресурсом. Другие методы (PUT, PATCH, DELETE) работают аналогично.",
        },
        code: {
          language: "javascript",
          code: `async function createUser(userData) {\n  const response = await fetch("https://api.example.com/users", {\n    method: "POST",\n    headers: {\n      "Content-Type": "application/json",\n      "Authorization": "Bearer token123",\n    },\n    body: JSON.stringify(userData),\n  });\n\n  if (!response.ok) throw new Error("Create failed");\n  return response.json();\n}\n\ncreateUser({ name: "Alice", email: "alice@test.com" });`,
        },
      },
      {
        title: {
          en: "AbortController & Error Handling",
          ru: "AbortController и обработка ошибок",
        },
        content: {
          en: "`AbortController` lets you cancel fetch requests. Create a controller, pass its `signal` to fetch, and call `controller.abort()` when needed — for example, when a component unmounts or a user navigates away. The fetch promise rejects with an AbortError. Always wrap fetch in try/catch to handle both network errors and abort errors gracefully.",
          ru: "`AbortController` позволяет отменять fetch-запросы. Создайте контроллер, передайте его `signal` в fetch и вызовите `controller.abort()`, когда нужно — например, при размонтировании компонента или уходе пользователя. Промис fetch отклоняется с ошибкой AbortError. Всегда оборачивайте fetch в try/catch для корректной обработки и сетевых ошибок, и ошибок отмены.",
        },
        code: {
          language: "javascript",
          code: `const controller = new AbortController();\n\nasync function fetchWithTimeout(url, ms = 5000) {\n  const timer = setTimeout(() => controller.abort(), ms);\n\n  try {\n    const res = await fetch(url, { signal: controller.signal });\n    clearTimeout(timer);\n    return await res.json();\n  } catch (err) {\n    if (err.name === "AbortError") {\n      console.log("Request was cancelled");\n    } else {\n      console.error("Network error:", err);\n    }\n  }\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "When does fetch() reject its promise?",
          ru: "Когда fetch() отклоняет свой промис?",
        },
        options: [
          { en: "On 404 Not Found", ru: "При 404 Not Found" },
          { en: "On 500 Server Error", ru: "При 500 Server Error" },
          { en: "On network failure only", ru: "Только при сетевом сбое" },
          { en: "On any non-200 status", ru: "При любом статусе, отличном от 200" },
        ],
        correct: 2,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "You must call JSON.stringify() on the body when sending JSON data with fetch.",
          ru: "При отправке JSON-данных через fetch нужно вызвать JSON.stringify() для тела запроса.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each Fetch concept to its description.",
          ru: "Сопоставьте каждое понятие Fetch с его описанием.",
        },
        pairs: [
          {
            term: { en: "response.ok", ru: "response.ok" },
            definition: {
              en: "true if status is in the 200-299 range",
              ru: "true, если статус в диапазоне 200-299",
            },
          },
          {
            term: { en: "response.json()", ru: "response.json()" },
            definition: {
              en: "Parses the response body as JSON",
              ru: "Парсит тело ответа как JSON",
            },
          },
          {
            term: { en: "AbortController", ru: "AbortController" },
            definition: {
              en: "Allows cancelling fetch requests via signal",
              ru: "Позволяет отменять fetch-запросы через signal",
            },
          },
          {
            term: { en: "Content-Type header", ru: "Заголовок Content-Type" },
            definition: {
              en: "Tells the server the format of the request body",
              ru: "Сообщает серверу формат тела запроса",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about the Fetch API.",
          ru: "Заполните пропуски о Fetch API.",
        },
        blanks: [
          {
            text: {
              en: "fetch() sends a ___ request by default.",
              ru: "fetch() по умолчанию отправляет ___-запрос.",
            },
            options: [
              { en: "GET", ru: "GET" },
              { en: "POST", ru: "POST" },
              { en: "PUT", ru: "PUT" },
              { en: "HEAD", ru: "HEAD" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To cancel a fetch, call ___() on the AbortController.",
              ru: "Для отмены fetch вызовите ___() у AbortController.",
            },
            options: [
              { en: "stop", ru: "stop" },
              { en: "abort", ru: "abort" },
              { en: "cancel", ru: "cancel" },
              { en: "close", ru: "close" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "When a request is aborted, the error name is ___.",
              ru: "При отмене запроса имя ошибки — ___.",
            },
            options: [
              { en: "NetworkError", ru: "NetworkError" },
              { en: "TimeoutError", ru: "TimeoutError" },
              { en: "AbortError", ru: "AbortError" },
              { en: "FetchError", ru: "FetchError" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to make a POST request with fetch:",
          ru: "Расположите шаги для выполнения POST-запроса через fetch:",
        },
        items: [
          { en: "Prepare the data object", ru: "Подготовить объект данных" },
          { en: "Call fetch with URL and options", ru: "Вызвать fetch с URL и настройками" },
          { en: "Set method to POST and Content-Type header", ru: "Установить метод POST и заголовок Content-Type" },
          { en: "Stringify the body with JSON.stringify", ru: "Сериализовать тело через JSON.stringify" },
          { en: "Check response.ok and parse JSON", ru: "Проверить response.ok и распарсить JSON" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to make a POST request:",
          ru: "Расположите строки для выполнения POST-запроса:",
        },
        items: [
          { en: 'const res = await fetch("/api/items", {', ru: 'const res = await fetch("/api/items", {' },
          { en: '  method: "POST",', ru: '  method: "POST",' },
          { en: '  headers: { "Content-Type": "application/json" },', ru: '  headers: { "Content-Type": "application/json" },' },
          { en: '  body: JSON.stringify({ name: "Item" }),', ru: '  body: JSON.stringify({ name: "Item" }),' },
          { en: "});", ru: "});" },
          { en: "const data = await res.json();", ru: "const data = await res.json();" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What Response property is true when the status code is 200-299?",
          ru: "Какое свойство Response равно true, когда код статуса 200-299?",
        },
        correctText: { en: "ok", ru: "ok" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review the Fetch API.",
          ru: "Повторите Fetch API.",
        },
        pairs: [
          {
            term: { en: "fetch()", ru: "fetch()" },
            definition: {
              en: "Browser API for making HTTP requests; returns a Promise",
              ru: "Браузерный API для HTTP-запросов; возвращает Promise",
            },
          },
          {
            term: { en: "response.ok", ru: "response.ok" },
            definition: {
              en: "Boolean: true if HTTP status is 200-299",
              ru: "Boolean: true, если HTTP-статус 200-299",
            },
          },
          {
            term: { en: "JSON.stringify()", ru: "JSON.stringify()" },
            definition: {
              en: "Converts a JS object to a JSON string for the request body",
              ru: "Преобразует JS-объект в JSON-строку для тела запроса",
            },
          },
          {
            term: { en: "AbortController", ru: "AbortController" },
            definition: {
              en: "Creates a signal to cancel pending fetch requests",
              ru: "Создаёт signal для отмены ожидающих fetch-запросов",
            },
          },
          {
            term: { en: "response.json()", ru: "response.json()" },
            definition: {
              en: "Async method that parses the response body as JSON",
              ru: "Асинхронный метод для парсинга тела ответа как JSON",
            },
          },
        ],
      },
    ],
  },

  /* ═══════════════════════════════════════════════════════════════
     fe-15-1  — Modern JS Features
     ═══════════════════════════════════════════════════════════════ */
  "fe-15-1": {
    id: "fe-15-1",
    title: {
      en: "Modern JS Features",
      ru: "Современные возможности JS",
    },
    slides: [
      {
        title: {
          en: "Template Literals & Destructuring",
          ru: "Шаблонные литералы и деструктуризация",
        },
        content: {
          en: "Template literals use backticks (`) and allow embedded expressions with `${expression}`. They also support multi-line strings without concatenation. Destructuring works on both arrays and objects. Array destructuring uses position: `const [a, b] = arr`. You can skip elements with commas and use rest syntax to collect remaining items.",
          ru: "Шаблонные литералы используют обратные апострофы (`) и позволяют встраивать выражения через `${expression}`. Они также поддерживают многострочные строки без конкатенации. Деструктуризация работает с массивами и объектами. Деструктуризация массива использует позицию: `const [a, b] = arr`. Можно пропускать элементы запятыми и использовать rest-синтаксис для сбора оставшихся элементов.",
        },
        code: {
          language: "javascript",
          code: `// Template literals\nconst name = "Alice";\nconst greeting = \`Hello, \${name}!\nWelcome to the platform.\`;\n\n// Array destructuring\nconst [first, , third] = [10, 20, 30];\nconsole.log(first, third); // 10 30\n\n// Rest in destructuring\nconst [head, ...tail] = [1, 2, 3, 4];\nconsole.log(tail); // [2, 3, 4]`,
        },
      },
      {
        title: {
          en: "Spread/Rest & Modules",
          ru: "Spread/Rest и модули",
        },
        content: {
          en: "The spread operator (`...`) expands iterables in arrays/objects or function calls. The rest parameter (`...args`) collects remaining function arguments into an array. ES modules use `export` to expose values and `import` to consume them. Named exports allow multiple exports per file; default exports provide a single main export.",
          ru: "Оператор spread (`...`) раскрывает итерируемые объекты в массивах/объектах или вызовах функций. Rest-параметр (`...args`) собирает оставшиеся аргументы функции в массив. ES-модули используют `export` для экспорта значений и `import` для их использования. Именованные экспорты позволяют экспортировать несколько значений из файла; экспорт по умолчанию предоставляет один главный экспорт.",
        },
        code: {
          language: "javascript",
          code: `// Spread in function call\nconst nums = [3, 1, 4];\nMath.max(...nums); // 4\n\n// Rest parameter\nfunction sum(...numbers) {\n  return numbers.reduce((a, b) => a + b, 0);\n}\nsum(1, 2, 3); // 6\n\n// ES Modules\n// utils.js\nexport const API_URL = "/api";\nexport function formatDate(d) { /* ... */ }\n\n// app.js\nimport { API_URL, formatDate } from "./utils.js";`,
        },
      },
      {
        title: {
          en: "Optional Chaining & Nullish Coalescing",
          ru: "Опциональная цепочка и оператор нулевого слияния",
        },
        content: {
          en: "Optional chaining (`?.`) short-circuits to `undefined` if a property in the chain is null or undefined, instead of throwing an error. It works on properties (`obj?.prop`), methods (`obj?.method()`), and array indices (`arr?.[0]`). The nullish coalescing operator (`??`) returns the right-hand value only when the left is `null` or `undefined` — unlike `||`, which also triggers on `0`, `\"\"`, and `false`.",
          ru: "Опциональная цепочка (`?.`) возвращает `undefined`, если свойство в цепочке равно null или undefined, вместо выброса ошибки. Работает со свойствами (`obj?.prop`), методами (`obj?.method()`) и индексами массивов (`arr?.[0]`). Оператор нулевого слияния (`??`) возвращает правое значение, только когда левое — `null` или `undefined` — в отличие от `||`, который также срабатывает на `0`, `\"\"` и `false`.",
        },
        code: {
          language: "javascript",
          code: `const user = { profile: { name: "Alice" } };\n\n// Optional chaining\nconsole.log(user.profile?.name);    // "Alice"\nconsole.log(user.settings?.theme);  // undefined (no error)\nconsole.log(user.getName?.());      // undefined (no error)\n\n// Nullish coalescing\nconst port = 0;\nconsole.log(port || 3000);  // 3000 (0 is falsy!)\nconsole.log(port ?? 3000);  // 0    (?? only checks null/undefined)\n\nconst label = null;\nconsole.log(label ?? "default"); // "default"`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does the nullish coalescing operator (??) check for?",
          ru: "Что проверяет оператор нулевого слияния (??)?",
        },
        options: [
          { en: "Any falsy value", ru: "Любое ложное значение" },
          { en: "null or undefined only", ru: "Только null или undefined" },
          { en: "null only", ru: "Только null" },
          { en: "undefined only", ru: "Только undefined" },
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
          en: "Optional chaining (?.) throws an error when the property is undefined.",
          ru: "Опциональная цепочка (?.) выбрасывает ошибку, когда свойство равно undefined.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each modern JS feature to its syntax or purpose.",
          ru: "Сопоставьте каждую современную возможность JS с её синтаксисом или назначением.",
        },
        pairs: [
          {
            term: { en: "Template literal", ru: "Шаблонный литерал" },
            definition: {
              en: "Backtick string with ${} for embedded expressions",
              ru: "Строка в обратных апострофах с ${} для встроенных выражений",
            },
          },
          {
            term: { en: "Rest parameter", ru: "Rest-параметр" },
            definition: {
              en: "...args collects remaining arguments into an array",
              ru: "...args собирает оставшиеся аргументы в массив",
            },
          },
          {
            term: { en: "Optional chaining", ru: "Опциональная цепочка" },
            definition: {
              en: "obj?.prop — safe access, returns undefined if null",
              ru: "obj?.prop — безопасный доступ, возвращает undefined при null",
            },
          },
          {
            term: { en: "Nullish coalescing", ru: "Нулевое слияние" },
            definition: {
              en: "a ?? b — fallback only for null/undefined",
              ru: "a ?? b — запасное значение только для null/undefined",
            },
          },
          {
            term: { en: "Named export", ru: "Именованный экспорт" },
            definition: {
              en: "export { x, y } — multiple exports per module",
              ru: "export { x, y } — несколько экспортов из модуля",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about modern JavaScript features.",
          ru: "Заполните пропуски о современных возможностях JavaScript.",
        },
        blanks: [
          {
            text: {
              en: "Template literals use ___ (backticks) instead of quotes.",
              ru: "Шаблонные литералы используют ___ (обратные апострофы) вместо кавычек.",
            },
            options: [
              { en: "` (backtick)", ru: "` (обратный апостроф)" },
              { en: "' (single quote)", ru: "' (одинарная кавычка)" },
              { en: "\" (double quote)", ru: "\" (двойная кавычка)" },
              { en: "# (hash)", ru: "# (решётка)" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ operator safely accesses nested properties without errors.",
              ru: "Оператор ___ безопасно обращается к вложенным свойствам без ошибок.",
            },
            options: [
              { en: "||", ru: "||" },
              { en: "?.", ru: "?." },
              { en: "&&", ru: "&&" },
              { en: "??", ru: "??" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "To bring values from another module, use the ___ keyword.",
              ru: "Для получения значений из другого модуля используйте ключевое слово ___.",
            },
            options: [
              { en: "require", ru: "require" },
              { en: "include", ru: "include" },
              { en: "import", ru: "import" },
              { en: "load", ru: "load" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to safely read a deeply nested property with a fallback:",
          ru: "Расположите шаги для безопасного чтения глубоко вложенного свойства с запасным значением:",
        },
        items: [
          { en: "Start with the root object", ru: "Начать с корневого объекта" },
          { en: "Use ?. to access the nested property", ru: "Использовать ?. для доступа к вложенному свойству" },
          { en: "Chain additional ?. for deeper levels", ru: "Добавить ещё ?. для более глубоких уровней" },
          { en: "Apply ?? to provide a fallback value", ru: "Применить ?? для указания запасного значения" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange lines to export and import a utility function:",
          ru: "Расположите строки для экспорта и импорта утилитарной функции:",
        },
        items: [
          { en: "// utils.js", ru: "// utils.js" },
          { en: "export function capitalize(str) {", ru: "export function capitalize(str) {" },
          { en: "  return str[0].toUpperCase() + str.slice(1);", ru: "  return str[0].toUpperCase() + str.slice(1);" },
          { en: "}", ru: "}" },
          { en: "// app.js", ru: "// app.js" },
          { en: 'import { capitalize } from "./utils.js";', ru: 'import { capitalize } from "./utils.js";' },
          { en: 'console.log(capitalize("hello"));', ru: 'console.log(capitalize("hello"));' },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What does 0 ?? 42 return?",
          ru: "Что вернёт 0 ?? 42?",
        },
        correctText: { en: "0", ru: "0" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review modern JavaScript features.",
          ru: "Повторите современные возможности JavaScript.",
        },
        pairs: [
          {
            term: { en: "Template literal", ru: "Шаблонный литерал" },
            definition: {
              en: "`string with ${expressions}` — supports multi-line and interpolation",
              ru: "`строка с ${выражениями}` — поддерживает многострочность и интерполяцию",
            },
          },
          {
            term: { en: "Spread / Rest", ru: "Spread / Rest" },
            definition: {
              en: "... expands iterables (spread) or collects args (rest)",
              ru: "... раскрывает итерируемые (spread) или собирает аргументы (rest)",
            },
          },
          {
            term: { en: "Optional chaining (?.)", ru: "Опциональная цепочка (?.)" },
            definition: {
              en: "Short-circuits to undefined instead of throwing on null access",
              ru: "Возвращает undefined вместо выброса ошибки при доступе к null",
            },
          },
          {
            term: { en: "Nullish coalescing (??)", ru: "Нулевое слияние (??)" },
            definition: {
              en: "Fallback only when left side is null or undefined",
              ru: "Запасное значение только когда левая часть — null или undefined",
            },
          },
          {
            term: { en: "ES Modules", ru: "ES-модули" },
            definition: {
              en: "import/export syntax for sharing code between files",
              ru: "Синтаксис import/export для обмена кодом между файлами",
            },
          },
        ],
      },
    ],
  },
};
