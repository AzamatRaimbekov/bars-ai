import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_V2_MIDDLE_REACT: Record<string, LessonContentV2> = {
  "fe-16-1": {
    id: "fe-16-1",
    title: {
      en: "JSX & Components",
      ru: "JSX и компоненты",
    },
    slides: [
      {
        title: {
          en: "What is JSX?",
          ru: "Что такое JSX?",
        },
        content: {
          en: "JSX (JavaScript XML) is a syntax extension for JavaScript that lets you write HTML-like markup inside JavaScript. Under the hood, JSX gets compiled by tools like Babel into React.createElement() calls. JSX expressions must have a single root element — you can wrap siblings in a <div> or use a Fragment (<>...</>).",
          ru: "JSX (JavaScript XML) — это расширение синтаксиса JavaScript, позволяющее писать HTML-подобную разметку прямо в JavaScript-коде. Под капотом JSX компилируется инструментами вроде Babel в вызовы React.createElement(). JSX-выражения должны иметь один корневой элемент — можно обернуть соседние элементы в <div> или использовать Fragment (<>...</>).",
        },
        code: {
          language: "tsx",
          code: `// JSX compiles to React.createElement\nconst element = <h1 className="title">Hello!</h1>;\n\n// Using Fragment to avoid extra wrapper\nconst greeting = (\n  <>\n    <h1>Hello</h1>\n    <p>Welcome to React</p>\n  </>\n);`,
        },
      },
      {
        title: {
          en: "Functional Components",
          ru: "Функциональные компоненты",
        },
        content: {
          en: "A React functional component is a JavaScript function that returns JSX. Component names must start with a capital letter so React can distinguish them from regular HTML elements. Components let you split the UI into independent, reusable pieces.",
          ru: "Функциональный компонент React — это JavaScript-функция, возвращающая JSX. Имена компонентов должны начинаться с заглавной буквы, чтобы React мог отличить их от обычных HTML-элементов. Компоненты позволяют разделить интерфейс на независимые переиспользуемые части.",
        },
        code: {
          language: "tsx",
          code: `function Welcome() {\n  return <h1>Hello, React!</h1>;\n}\n\n// Arrow function style\nconst Card = () => {\n  return (\n    <div className="card">\n      <h2>Title</h2>\n      <p>Description</p>\n    </div>\n  );\n};`,
        },
      },
      {
        title: {
          en: "Component Composition",
          ru: "Композиция компонентов",
        },
        content: {
          en: "Component composition means building complex UIs by combining simpler components. You nest components inside one another just like HTML elements. This is the core pattern of React — small, focused components assembled together to form entire pages.",
          ru: "Композиция компонентов — это построение сложных интерфейсов путём комбинирования простых компонентов. Вы вкладываете компоненты друг в друга так же, как HTML-элементы. Это главный паттерн React — маленькие, сфокусированные компоненты, собранные вместе для формирования целых страниц.",
        },
        code: {
          language: "tsx",
          code: `function Header() {\n  return <header><h1>My App</h1></header>;\n}\n\nfunction Footer() {\n  return <footer><p>&copy; 2025</p></footer>;\n}\n\nfunction App() {\n  return (\n    <>\n      <Header />\n      <main><p>Content here</p></main>\n      <Footer />\n    </>\n  );\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does JSX get compiled into?",
          ru: "Во что компилируется JSX?",
        },
        options: [
          { en: "HTML strings", ru: "HTML-строки" },
          { en: "React.createElement() calls", ru: "Вызовы React.createElement()" },
          { en: "DOM nodes directly", ru: "Напрямую в DOM-узлы" },
          { en: "Web Components", ru: "Web Components" },
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
          en: "A React component name can start with a lowercase letter.",
          ru: "Имя компонента React может начинаться со строчной буквы.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each JSX concept to its description.",
          ru: "Сопоставьте каждое понятие JSX с его описанием.",
        },
        pairs: [
          {
            term: { en: "JSX", ru: "JSX" },
            definition: {
              en: "Syntax extension that mixes HTML-like markup with JavaScript",
              ru: "Расширение синтаксиса, смешивающее HTML-подобную разметку с JavaScript",
            },
          },
          {
            term: { en: "Fragment (<>)", ru: "Fragment (<>)" },
            definition: {
              en: "Invisible wrapper that groups elements without extra DOM node",
              ru: "Невидимая обёртка, группирующая элементы без лишнего DOM-узла",
            },
          },
          {
            term: { en: "className", ru: "className" },
            definition: {
              en: "JSX attribute used instead of HTML class",
              ru: "JSX-атрибут, используемый вместо HTML-атрибута class",
            },
          },
          {
            term: { en: "Component", ru: "Компонент" },
            definition: {
              en: "Reusable function that returns JSX describing part of the UI",
              ru: "Переиспользуемая функция, возвращающая JSX-описание части интерфейса",
            },
          },
          {
            term: { en: "Composition", ru: "Композиция" },
            definition: {
              en: "Combining smaller components to build complex interfaces",
              ru: "Объединение маленьких компонентов для построения сложных интерфейсов",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about JSX and components.",
          ru: "Заполните пропуски о JSX и компонентах.",
        },
        blanks: [
          {
            text: {
              en: "In JSX, you use ___ instead of the HTML class attribute.",
              ru: "В JSX вместо HTML-атрибута class используется ___.",
            },
            options: [
              { en: "className", ru: "className" },
              { en: "cssClass", ru: "cssClass" },
              { en: "htmlClass", ru: "htmlClass" },
              { en: "style", ru: "style" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To group multiple elements without an extra DOM node, use a ___.",
              ru: "Чтобы сгруппировать несколько элементов без лишнего DOM-узла, используйте ___.",
            },
            options: [
              { en: "Fragment", ru: "Fragment" },
              { en: "Container", ru: "Container" },
              { en: "Wrapper", ru: "Wrapper" },
              { en: "Section", ru: "Section" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Component names must start with a ___ letter.",
              ru: "Имена компонентов должны начинаться с ___ буквы.",
            },
            options: [
              { en: "capital", ru: "заглавной" },
              { en: "lowercase", ru: "строчной" },
              { en: "any", ru: "любой" },
              { en: "vowel", ru: "гласной" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps to create and render a React component.",
          ru: "Расположите шаги создания и рендеринга React-компонента в правильном порядке.",
        },
        items: [
          { en: "Import React (if needed)", ru: "Импортировать React (если нужно)" },
          { en: "Define a function with a capital name", ru: "Определить функцию с заглавным именем" },
          { en: "Return JSX from the function", ru: "Вернуть JSX из функции" },
          { en: "Export the component", ru: "Экспортировать компонент" },
          { en: "Use <Component /> in parent JSX", ru: "Использовать <Component /> в родительском JSX" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a valid React functional component.",
          ru: "Расположите строки, чтобы создать валидный функциональный React-компонент.",
        },
        items: [
          { en: "function Greeting() {", ru: "function Greeting() {" },
          { en: "  return (", ru: "  return (" },
          { en: "    <>", ru: "    <>" },
          { en: "      <h1>Hello</h1>", ru: "      <h1>Привет</h1>" },
          { en: "      <p>Welcome!</p>", ru: "      <p>Добро пожаловать!</p>" },
          { en: "    </>", ru: "    </>" },
          { en: "  );", ru: "  );" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What short syntax (<>...</>) is used to wrap multiple JSX elements without adding an extra DOM node? (one word)",
          ru: "Какой краткий синтаксис (<>...</>) используется для обёртки нескольких JSX-элементов без добавления лишнего DOM-узла? (одно слово)",
        },
        correctText: { en: "Fragment", ru: "Fragment" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key JSX and component terms.",
          ru: "Повторите ключевые термины JSX и компонентов.",
        },
        pairs: [
          {
            term: { en: "JSX", ru: "JSX" },
            definition: {
              en: "A syntax extension that lets you write HTML-like code in JavaScript",
              ru: "Расширение синтаксиса, позволяющее писать HTML-подобный код в JavaScript",
            },
          },
          {
            term: { en: "Functional Component", ru: "Функциональный компонент" },
            definition: {
              en: "A JavaScript function that returns JSX to describe a piece of UI",
              ru: "JavaScript-функция, возвращающая JSX для описания части интерфейса",
            },
          },
          {
            term: { en: "Fragment", ru: "Фрагмент" },
            definition: {
              en: "An invisible wrapper (<>...</>) that groups elements without extra DOM nodes",
              ru: "Невидимая обёртка (<>...</>), группирующая элементы без лишних DOM-узлов",
            },
          },
          {
            term: { en: "Composition", ru: "Композиция" },
            definition: {
              en: "The pattern of nesting smaller components to build complex UIs",
              ru: "Паттерн вложения маленьких компонентов для построения сложных интерфейсов",
            },
          },
          {
            term: { en: "className", ru: "className" },
            definition: {
              en: "JSX attribute equivalent to HTML's class attribute",
              ru: "JSX-атрибут, эквивалентный HTML-атрибуту class",
            },
          },
        ],
      },
    ],
  },

  "fe-16-2": {
    id: "fe-16-2",
    title: {
      en: "Props & Rendering",
      ru: "Props и рендеринг",
    },
    slides: [
      {
        title: {
          en: "Passing Props",
          ru: "Передача Props",
        },
        content: {
          en: "Props (short for properties) are the way data flows from parent to child components in React. You pass props like HTML attributes, and the child receives them as a single object parameter. Props are read-only — a component must never modify its own props. You can also pass default values using default parameters or defaultProps.",
          ru: "Props (сокращение от properties, свойства) — это способ передачи данных от родительского компонента к дочернему в React. Props передаются как HTML-атрибуты, а дочерний компонент получает их как единый объект-параметр. Props доступны только для чтения — компонент никогда не должен изменять свои props. Можно задать значения по умолчанию через параметры по умолчанию или defaultProps.",
        },
        code: {
          language: "tsx",
          code: `function UserCard({ name, age = 18 }: { name: string; age?: number }) {\n  return (\n    <div>\n      <h2>{name}</h2>\n      <p>Age: {age}</p>\n    </div>\n  );\n}\n\n// Usage\n<UserCard name="Alice" age={25} />\n<UserCard name="Bob" /> // age defaults to 18`,
        },
      },
      {
        title: {
          en: "Children Prop & Conditional Rendering",
          ru: "Prop children и условный рендеринг",
        },
        content: {
          en: "The special children prop represents whatever you put between the opening and closing tags of a component. Conditional rendering lets you show different UI based on conditions — use ternary operators, && short-circuit, or early returns. This makes components dynamic and responsive to data.",
          ru: "Специальный prop children представляет всё, что помещено между открывающим и закрывающим тегами компонента. Условный рендеринг позволяет показывать разный интерфейс в зависимости от условий — используйте тернарный оператор, оператор && или ранний return. Это делает компоненты динамичными и отзывчивыми к данным.",
        },
        code: {
          language: "tsx",
          code: `function Panel({ children, title }: { children: React.ReactNode; title: string }) {\n  return (\n    <div className="panel">\n      <h3>{title}</h3>\n      {children}\n    </div>\n  );\n}\n\nfunction App({ isLoggedIn }: { isLoggedIn: boolean }) {\n  return (\n    <Panel title="Status">\n      {isLoggedIn ? <p>Welcome back!</p> : <p>Please log in</p>}\n    </Panel>\n  );\n}`,
        },
      },
      {
        title: {
          en: "Rendering Lists with Keys",
          ru: "Рендеринг списков с ключами",
        },
        content: {
          en: "To render a list in React, use the .map() method on an array and return JSX for each item. Each item must have a unique key prop so React can efficiently track which items changed, were added, or removed. Never use array indexes as keys if the list can be reordered.",
          ru: "Для рендеринга списка в React используйте метод .map() на массиве и верните JSX для каждого элемента. У каждого элемента должен быть уникальный prop key, чтобы React мог эффективно отслеживать, какие элементы изменились, были добавлены или удалены. Никогда не используйте индексы массива в качестве ключей, если список может быть переупорядочен.",
        },
        code: {
          language: "tsx",
          code: `const fruits = [\n  { id: 1, name: "Apple" },\n  { id: 2, name: "Banana" },\n  { id: 3, name: "Cherry" },\n];\n\nfunction FruitList() {\n  return (\n    <ul>\n      {fruits.map((fruit) => (\n        <li key={fruit.id}>{fruit.name}</li>\n      ))}\n    </ul>\n  );\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What is the purpose of the key prop when rendering lists?",
          ru: "Какова цель prop key при рендеринге списков?",
        },
        options: [
          { en: "It styles the list items", ru: "Он стилизует элементы списка" },
          { en: "It helps React track which items changed", ru: "Он помогает React отслеживать, какие элементы изменились" },
          { en: "It sorts the list automatically", ru: "Он автоматически сортирует список" },
          { en: "It sets the item's CSS id", ru: "Он задаёт CSS id элемента" },
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
          en: "A child component is allowed to modify the props it receives from its parent.",
          ru: "Дочерний компонент может изменять props, полученные от родительского компонента.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each concept to its description.",
          ru: "Сопоставьте каждое понятие с его описанием.",
        },
        pairs: [
          {
            term: { en: "props", ru: "props" },
            definition: {
              en: "Read-only data passed from parent to child component",
              ru: "Данные только для чтения, передаваемые от родителя к дочернему компоненту",
            },
          },
          {
            term: { en: "children", ru: "children" },
            definition: {
              en: "Special prop that holds content between component tags",
              ru: "Специальный prop, содержащий контент между тегами компонента",
            },
          },
          {
            term: { en: "key", ru: "key" },
            definition: {
              en: "Unique identifier for list items to optimize re-rendering",
              ru: "Уникальный идентификатор элементов списка для оптимизации перерисовки",
            },
          },
          {
            term: { en: "Conditional rendering", ru: "Условный рендеринг" },
            definition: {
              en: "Showing different UI elements based on a condition",
              ru: "Отображение различных элементов интерфейса в зависимости от условия",
            },
          },
          {
            term: { en: "Default props", ru: "Props по умолчанию" },
            definition: {
              en: "Fallback values used when a prop is not provided",
              ru: "Значения, используемые когда prop не передан",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about props and rendering.",
          ru: "Заполните пропуски о props и рендеринге.",
        },
        blanks: [
          {
            text: {
              en: "To render a list of items, you use the ___ array method.",
              ru: "Для рендеринга списка элементов используется метод массива ___.",
            },
            options: [
              { en: ".map()", ru: ".map()" },
              { en: ".forEach()", ru: ".forEach()" },
              { en: ".filter()", ru: ".filter()" },
              { en: ".reduce()", ru: ".reduce()" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The special ___ prop represents content placed between component tags.",
              ru: "Специальный prop ___ представляет контент, размещённый между тегами компонента.",
            },
            options: [
              { en: "children", ru: "children" },
              { en: "content", ru: "content" },
              { en: "inner", ru: "inner" },
              { en: "body", ru: "body" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Props in React are ___ — a component cannot modify them.",
              ru: "Props в React являются ___ — компонент не может их изменять.",
            },
            options: [
              { en: "read-only", ru: "только для чтения" },
              { en: "mutable", ru: "изменяемыми" },
              { en: "optional", ru: "необязательными" },
              { en: "global", ru: "глобальными" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps of data flow from parent to child via props.",
          ru: "Расположите шаги передачи данных от родителя к дочернему компоненту через props.",
        },
        items: [
          { en: "Parent component defines data", ru: "Родительский компонент определяет данные" },
          { en: "Parent passes data as props in JSX", ru: "Родитель передаёт данные как props в JSX" },
          { en: "Child receives props as function parameter", ru: "Дочерний компонент получает props как параметр функции" },
          { en: "Child destructures needed values", ru: "Дочерний компонент деструктурирует нужные значения" },
          { en: "Child renders UI using prop values", ru: "Дочерний компонент рендерит интерфейс, используя значения props" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to render a list of users.",
          ru: "Расположите строки, чтобы отрендерить список пользователей.",
        },
        items: [
          { en: "function UserList({ users }) {", ru: "function UserList({ users }) {" },
          { en: "  return (", ru: "  return (" },
          { en: "    <ul>", ru: "    <ul>" },
          { en: "      {users.map((user) => (", ru: "      {users.map((user) => (" },
          { en: "        <li key={user.id}>{user.name}</li>", ru: "        <li key={user.id}>{user.name}</li>" },
          { en: "      ))}", ru: "      ))}" },
          { en: "    </ul>", ru: "    </ul>" },
          { en: "  );", ru: "  );" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What special prop name represents the content placed between a component's opening and closing tags? (one word)",
          ru: "Какой специальный prop представляет контент, размещённый между открывающим и закрывающим тегами компонента? (одно слово)",
        },
        correctText: { en: "children", ru: "children" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms about props and rendering.",
          ru: "Повторите ключевые термины о props и рендеринге.",
        },
        pairs: [
          {
            term: { en: "Props", ru: "Props (свойства)" },
            definition: {
              en: "Read-only data passed from a parent to a child component",
              ru: "Данные только для чтения, передаваемые от родителя к дочернему компоненту",
            },
          },
          {
            term: { en: "children", ru: "children" },
            definition: {
              en: "A special prop that holds everything placed between component tags",
              ru: "Специальный prop, содержащий всё, что размещено между тегами компонента",
            },
          },
          {
            term: { en: "key", ru: "key (ключ)" },
            definition: {
              en: "A unique identifier that React uses to track list items during updates",
              ru: "Уникальный идентификатор, используемый React для отслеживания элементов списка при обновлениях",
            },
          },
          {
            term: { en: "Ternary operator", ru: "Тернарный оператор" },
            definition: {
              en: "condition ? trueJSX : falseJSX — used for inline conditional rendering",
              ru: "condition ? trueJSX : falseJSX — используется для инлайн условного рендеринга",
            },
          },
          {
            term: { en: "Default props", ru: "Значения по умолчанию" },
            definition: {
              en: "Fallback values for props when they are not passed by the parent",
              ru: "Значения props по умолчанию, когда родитель их не передаёт",
            },
          },
        ],
      },
    ],
  },

  "fe-17-1": {
    id: "fe-17-1",
    title: {
      en: "useState & Events",
      ru: "useState и события",
    },
    slides: [
      {
        title: {
          en: "The useState Hook",
          ru: "Хук useState",
        },
        content: {
          en: "useState is a React hook that lets functional components hold and update state. It returns an array with two elements: the current state value and a setter function. When the setter is called, React re-renders the component with the new value. Always call hooks at the top level of your component — never inside conditions or loops.",
          ru: "useState — это хук React, позволяющий функциональным компонентам хранить и обновлять состояние. Он возвращает массив из двух элементов: текущее значение состояния и функцию-сеттер. При вызове сеттера React перерисовывает компонент с новым значением. Всегда вызывайте хуки на верхнем уровне компонента — никогда внутри условий или циклов.",
        },
        code: {
          language: "tsx",
          code: `import { useState } from "react";\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n\n  return (\n    <div>\n      <p>Count: {count}</p>\n      <button onClick={() => setCount(count + 1)}>+1</button>\n    </div>\n  );\n}`,
        },
      },
      {
        title: {
          en: "Handling Events",
          ru: "Обработка событий",
        },
        content: {
          en: "React events use camelCase naming (onClick, onChange, onSubmit) instead of lowercase HTML events. Event handlers receive a synthetic event object. For buttons use onClick, for inputs use onChange, and for forms use onSubmit. Always pass a function reference — not a function call — to event handlers.",
          ru: "События React используют camelCase (onClick, onChange, onSubmit) вместо строчных HTML-событий. Обработчики получают синтетический объект события. Для кнопок используйте onClick, для полей ввода — onChange, для форм — onSubmit. Всегда передавайте ссылку на функцию, а не вызов функции, в обработчик событий.",
        },
        code: {
          language: "tsx",
          code: `function LoginForm() {\n  const [email, setEmail] = useState("");\n\n  const handleSubmit = (e: React.FormEvent) => {\n    e.preventDefault();\n    console.log("Submitted:", email);\n  };\n\n  return (\n    <form onSubmit={handleSubmit}>\n      <input\n        type="email"\n        value={email}\n        onChange={(e) => setEmail(e.target.value)}\n      />\n      <button type="submit">Log In</button>\n    </form>\n  );\n}`,
        },
      },
      {
        title: {
          en: "Controlled Inputs & Previous State",
          ru: "Управляемые поля ввода и предыдущее состояние",
        },
        content: {
          en: "A controlled input is one whose value is driven by React state, with onChange updating that state. When the new state depends on the old one, use the functional updater form: setState(prev => prev + 1). This guarantees correctness even when multiple updates are batched together.",
          ru: "Управляемое поле ввода — это поле, значение которого определяется состоянием React, а onChange обновляет это состояние. Когда новое состояние зависит от предыдущего, используйте функциональную форму обновления: setState(prev => prev + 1). Это гарантирует корректность даже при пакетной обработке нескольких обновлений.",
        },
        code: {
          language: "tsx",
          code: `function TodoApp() {\n  const [todos, setTodos] = useState<string[]>([]);\n  const [input, setInput] = useState("");\n\n  const addTodo = () => {\n    setTodos((prev) => [...prev, input]);\n    setInput("");\n  };\n\n  return (\n    <div>\n      <input value={input} onChange={(e) => setInput(e.target.value)} />\n      <button onClick={addTodo}>Add</button>\n      <ul>\n        {todos.map((t, i) => <li key={i}>{t}</li>)}\n      </ul>\n    </div>\n  );\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does useState return?",
          ru: "Что возвращает useState?",
        },
        options: [
          { en: "An object with state and dispatch", ru: "Объект со state и dispatch" },
          { en: "An array with [value, setter]", ru: "Массив с [значение, сеттер]" },
          { en: "Just the current state value", ru: "Только текущее значение состояния" },
          { en: "A ref to the state variable", ru: "Ссылку на переменную состояния" },
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
          en: "You can call useState inside an if statement to conditionally add state.",
          ru: "Можно вызывать useState внутри оператора if для условного добавления состояния.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each concept to its description.",
          ru: "Сопоставьте каждое понятие с его описанием.",
        },
        pairs: [
          {
            term: { en: "useState", ru: "useState" },
            definition: {
              en: "Hook that creates a state variable in a functional component",
              ru: "Хук, создающий переменную состояния в функциональном компоненте",
            },
          },
          {
            term: { en: "onClick", ru: "onClick" },
            definition: {
              en: "Event handler that fires when the user clicks an element",
              ru: "Обработчик события, срабатывающий при клике пользователя на элемент",
            },
          },
          {
            term: { en: "onChange", ru: "onChange" },
            definition: {
              en: "Event handler that fires when an input value changes",
              ru: "Обработчик события, срабатывающий при изменении значения поля ввода",
            },
          },
          {
            term: { en: "Controlled input", ru: "Управляемое поле" },
            definition: {
              en: "An input whose value is driven by React state",
              ru: "Поле ввода, значение которого определяется состоянием React",
            },
          },
          {
            term: { en: "Functional updater", ru: "Функциональное обновление" },
            definition: {
              en: "setState(prev => newValue) pattern for safe state updates",
              ru: "Паттерн setState(prev => newValue) для безопасного обновления состояния",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about useState and events.",
          ru: "Заполните пропуски о useState и событиях.",
        },
        blanks: [
          {
            text: {
              en: "const [count, ___] = useState(0);",
              ru: "const [count, ___] = useState(0);",
            },
            options: [
              { en: "setCount", ru: "setCount" },
              { en: "updateCount", ru: "updateCount" },
              { en: "changeCount", ru: "changeCount" },
              { en: "count++", ru: "count++" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "React events are named in ___ convention.",
              ru: "События React именуются в соглашении ___.",
            },
            options: [
              { en: "camelCase", ru: "camelCase" },
              { en: "snake_case", ru: "snake_case" },
              { en: "kebab-case", ru: "kebab-case" },
              { en: "UPPER_CASE", ru: "UPPER_CASE" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To prevent default form submission, call ___.",
              ru: "Чтобы предотвратить стандартную отправку формы, вызовите ___.",
            },
            options: [
              { en: "e.preventDefault()", ru: "e.preventDefault()" },
              { en: "e.stopDefault()", ru: "e.stopDefault()" },
              { en: "return false", ru: "return false" },
              { en: "e.cancel()", ru: "e.cancel()" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps of a controlled input update cycle.",
          ru: "Расположите шаги цикла обновления управляемого поля ввода.",
        },
        items: [
          { en: "User types into the input", ru: "Пользователь вводит текст в поле" },
          { en: "onChange event fires", ru: "Срабатывает событие onChange" },
          { en: "Handler calls setState with new value", ru: "Обработчик вызывает setState с новым значением" },
          { en: "React re-renders the component", ru: "React перерисовывает компонент" },
          { en: "Input displays the updated state value", ru: "Поле отображает обновлённое значение состояния" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a counter component with useState.",
          ru: "Расположите строки, чтобы создать компонент-счётчик с useState.",
        },
        items: [
          { en: "import { useState } from \"react\";", ru: "import { useState } from \"react\";" },
          { en: "function Counter() {", ru: "function Counter() {" },
          { en: "  const [count, setCount] = useState(0);", ru: "  const [count, setCount] = useState(0);" },
          { en: "  return (", ru: "  return (" },
          { en: "    <button onClick={() => setCount(prev => prev + 1)}>", ru: "    <button onClick={() => setCount(prev => prev + 1)}>" },
          { en: "      Count: {count}", ru: "      Счёт: {count}" },
          { en: "    </button>", ru: "    </button>" },
          { en: "  );", ru: "  );" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What React hook is used to add state to a functional component? (write the hook name, e.g. useState)",
          ru: "Какой хук React используется для добавления состояния в функциональный компонент? (напишите название хука, например useState)",
        },
        correctText: { en: "useState", ru: "useState" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms about state and events.",
          ru: "Повторите ключевые термины о состоянии и событиях.",
        },
        pairs: [
          {
            term: { en: "useState", ru: "useState" },
            definition: {
              en: "A hook that returns [value, setter] to manage component state",
              ru: "Хук, возвращающий [значение, сеттер] для управления состоянием компонента",
            },
          },
          {
            term: { en: "Synthetic Event", ru: "Синтетическое событие" },
            definition: {
              en: "React's cross-browser wrapper around native DOM events",
              ru: "Кросс-браузерная обёртка React вокруг нативных DOM-событий",
            },
          },
          {
            term: { en: "Controlled Input", ru: "Управляемое поле" },
            definition: {
              en: "An input element whose value is bound to state and updated via onChange",
              ru: "Элемент ввода, значение которого привязано к состоянию и обновляется через onChange",
            },
          },
          {
            term: { en: "Batching", ru: "Батчинг" },
            definition: {
              en: "React groups multiple state updates into a single re-render for performance",
              ru: "React группирует несколько обновлений состояния в одну перерисовку для производительности",
            },
          },
          {
            term: { en: "Functional updater", ru: "Функциональный апдейтер" },
            definition: {
              en: "setState(prev => ...) pattern that ensures correct state based on previous value",
              ru: "Паттерн setState(prev => ...), гарантирующий корректное состояние на основе предыдущего значения",
            },
          },
        ],
      },
    ],
  },

  "fe-18-1": {
    id: "fe-18-1",
    title: {
      en: "useEffect",
      ru: "useEffect",
    },
    slides: [
      {
        title: {
          en: "What is useEffect?",
          ru: "Что такое useEffect?",
        },
        content: {
          en: "useEffect is a hook that lets you perform side effects in functional components. Side effects include fetching data, setting up subscriptions, or manually updating the DOM. It runs after the component renders. Think of useEffect as a combination of componentDidMount, componentDidUpdate, and componentWillUnmount from class components.",
          ru: "useEffect — это хук, позволяющий выполнять побочные эффекты в функциональных компонентах. К побочным эффектам относятся запросы данных, подписки или ручное обновление DOM. Он запускается после рендеринга компонента. Думайте о useEffect как о комбинации componentDidMount, componentDidUpdate и componentWillUnmount из классовых компонентов.",
        },
        code: {
          language: "tsx",
          code: `import { useEffect, useState } from "react";\n\nfunction Timer() {\n  const [seconds, setSeconds] = useState(0);\n\n  useEffect(() => {\n    const id = setInterval(() => {\n      setSeconds((s) => s + 1);\n    }, 1000);\n\n    return () => clearInterval(id); // cleanup\n  }, []); // empty array = run once on mount\n\n  return <p>Elapsed: {seconds}s</p>;\n}`,
        },
      },
      {
        title: {
          en: "Dependency Array",
          ru: "Массив зависимостей",
        },
        content: {
          en: "The second argument to useEffect is the dependency array. It controls when the effect re-runs. An empty array [] means the effect runs only once after mount. Listing specific values [a, b] makes it re-run when those values change. Omitting the array entirely makes the effect run after every render — usually not what you want.",
          ru: "Второй аргумент useEffect — массив зависимостей. Он контролирует, когда эффект запускается повторно. Пустой массив [] означает, что эффект запустится только один раз после монтирования. Указание конкретных значений [a, b] вызовет повторный запуск при их изменении. Если массив не указан вовсе, эффект запускается после каждого рендера — обычно это не то, что нужно.",
        },
        code: {
          language: "tsx",
          code: `// Runs ONCE after mount\nuseEffect(() => {\n  console.log("Mounted");\n}, []);\n\n// Runs when userId changes\nuseEffect(() => {\n  fetchUser(userId);\n}, [userId]);\n\n// Runs after EVERY render (avoid if possible)\nuseEffect(() => {\n  console.log("Rendered");\n});`,
        },
      },
      {
        title: {
          en: "Fetching Data with useEffect",
          ru: "Загрузка данных с useEffect",
        },
        content: {
          en: "A common pattern is fetching data inside useEffect. Since the effect callback cannot be async directly, define an async function inside and call it immediately. Use a cleanup function or an AbortController to cancel in-flight requests when the component unmounts or dependencies change.",
          ru: "Частый паттерн — загрузка данных внутри useEffect. Поскольку колбэк эффекта не может быть напрямую async, определите async-функцию внутри и вызовите её сразу. Используйте функцию очистки или AbortController для отмены незавершённых запросов при размонтировании компонента или изменении зависимостей.",
        },
        code: {
          language: "tsx",
          code: `function UserProfile({ userId }: { userId: string }) {\n  const [user, setUser] = useState(null);\n  const [loading, setLoading] = useState(true);\n\n  useEffect(() => {\n    const controller = new AbortController();\n\n    async function fetchData() {\n      setLoading(true);\n      const res = await fetch(\`/api/users/\${userId}\`, {\n        signal: controller.signal,\n      });\n      const data = await res.json();\n      setUser(data);\n      setLoading(false);\n    }\n\n    fetchData();\n    return () => controller.abort();\n  }, [userId]);\n\n  if (loading) return <p>Loading...</p>;\n  return <p>{user?.name}</p>;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "When does a useEffect with an empty dependency array run?",
          ru: "Когда запускается useEffect с пустым массивом зависимостей?",
        },
        options: [
          { en: "Before every render", ru: "Перед каждым рендером" },
          { en: "Only once, after the first render", ru: "Только один раз, после первого рендера" },
          { en: "After every state change", ru: "После каждого изменения состояния" },
          { en: "Only when props change", ru: "Только при изменении props" },
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
          en: "The callback function passed to useEffect can be directly declared as async.",
          ru: "Колбэк-функция, переданная в useEffect, может быть объявлена напрямую как async.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each useEffect pattern to its behavior.",
          ru: "Сопоставьте каждый паттерн useEffect с его поведением.",
        },
        pairs: [
          {
            term: { en: "useEffect(fn, [])", ru: "useEffect(fn, [])" },
            definition: {
              en: "Runs once after mount, like componentDidMount",
              ru: "Запускается один раз после монтирования, аналог componentDidMount",
            },
          },
          {
            term: { en: "useEffect(fn, [dep])", ru: "useEffect(fn, [dep])" },
            definition: {
              en: "Runs when the dep value changes",
              ru: "Запускается при изменении значения dep",
            },
          },
          {
            term: { en: "useEffect(fn)", ru: "useEffect(fn)" },
            definition: {
              en: "Runs after every render",
              ru: "Запускается после каждого рендера",
            },
          },
          {
            term: { en: "return () => {...}", ru: "return () => {...}" },
            definition: {
              en: "Cleanup function that runs before the effect re-runs or on unmount",
              ru: "Функция очистки, запускаемая перед повторным запуском эффекта или при размонтировании",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about useEffect.",
          ru: "Заполните пропуски о useEffect.",
        },
        blanks: [
          {
            text: {
              en: "useEffect runs ___ the component renders.",
              ru: "useEffect запускается ___ рендеринга компонента.",
            },
            options: [
              { en: "after", ru: "после" },
              { en: "before", ru: "перед" },
              { en: "during", ru: "во время" },
              { en: "instead of", ru: "вместо" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "An empty dependency array [] means the effect runs ___.",
              ru: "Пустой массив зависимостей [] означает, что эффект запустится ___.",
            },
            options: [
              { en: "once on mount", ru: "один раз при монтировании" },
              { en: "on every render", ru: "при каждом рендере" },
              { en: "never", ru: "никогда" },
              { en: "only on unmount", ru: "только при размонтировании" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ function returned from useEffect is called on unmount or before re-running the effect.",
              ru: "Функция ___, возвращаемая из useEffect, вызывается при размонтировании или перед повторным запуском эффекта.",
            },
            options: [
              { en: "cleanup", ru: "очистки (cleanup)" },
              { en: "destroy", ru: "destroy" },
              { en: "dispose", ru: "dispose" },
              { en: "reset", ru: "reset" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the lifecycle of a useEffect with cleanup.",
          ru: "Расположите этапы жизненного цикла useEffect с очисткой.",
        },
        items: [
          { en: "Component mounts and renders", ru: "Компонент монтируется и рендерится" },
          { en: "useEffect callback runs", ru: "Запускается колбэк useEffect" },
          { en: "Dependency value changes, component re-renders", ru: "Значение зависимости меняется, компонент перерисовывается" },
          { en: "Cleanup function from previous effect runs", ru: "Запускается функция очистки предыдущего эффекта" },
          { en: "useEffect callback runs again with new values", ru: "Колбэк useEffect запускается снова с новыми значениями" },
          { en: "Component unmounts, final cleanup runs", ru: "Компонент размонтируется, запускается финальная очистка" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to fetch data with useEffect.",
          ru: "Расположите строки, чтобы загрузить данные с useEffect.",
        },
        items: [
          { en: "const [data, setData] = useState(null);", ru: "const [data, setData] = useState(null);" },
          { en: "useEffect(() => {", ru: "useEffect(() => {" },
          { en: "  async function fetchData() {", ru: "  async function fetchData() {" },
          { en: "    const res = await fetch(\"/api/items\");", ru: "    const res = await fetch(\"/api/items\");" },
          { en: "    const json = await res.json();", ru: "    const json = await res.json();" },
          { en: "    setData(json);", ru: "    setData(json);" },
          { en: "  }", ru: "  }" },
          { en: "  fetchData();", ru: "  fetchData();" },
          { en: "}, []);", ru: "}, []);" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What do you return from a useEffect callback to perform cleanup? (answer: a function)",
          ru: "Что нужно вернуть из колбэка useEffect для очистки? (ответ: функцию)",
        },
        correctText: { en: "a function", ru: "функцию" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms about useEffect.",
          ru: "Повторите ключевые термины о useEffect.",
        },
        pairs: [
          {
            term: { en: "Side effect", ru: "Побочный эффект" },
            definition: {
              en: "Any operation that affects something outside the component (API calls, timers, DOM)",
              ru: "Любая операция, влияющая на что-то за пределами компонента (API-запросы, таймеры, DOM)",
            },
          },
          {
            term: { en: "Dependency array", ru: "Массив зависимостей" },
            definition: {
              en: "The second argument to useEffect that controls when the effect re-runs",
              ru: "Второй аргумент useEffect, контролирующий повторный запуск эффекта",
            },
          },
          {
            term: { en: "Cleanup function", ru: "Функция очистки" },
            definition: {
              en: "A function returned from useEffect that runs on unmount or before re-run",
              ru: "Функция, возвращаемая из useEffect, запускаемая при размонтировании или перед перезапуском",
            },
          },
          {
            term: { en: "AbortController", ru: "AbortController" },
            definition: {
              en: "Browser API used to cancel fetch requests in useEffect cleanup",
              ru: "Браузерный API для отмены fetch-запросов в функции очистки useEffect",
            },
          },
          {
            term: { en: "Mount", ru: "Монтирование" },
            definition: {
              en: "The moment a component is inserted into the DOM for the first time",
              ru: "Момент первого добавления компонента в DOM",
            },
          },
        ],
      },
    ],
  },

  "fe-18-2": {
    id: "fe-18-2",
    title: {
      en: "Custom Hooks",
      ru: "Пользовательские хуки",
    },
    slides: [
      {
        title: {
          en: "Why Custom Hooks?",
          ru: "Зачем нужны пользовательские хуки?",
        },
        content: {
          en: "Custom hooks let you extract reusable logic from components. A custom hook is just a function whose name starts with \"use\" and that can call other hooks inside. This lets you share stateful logic between components without duplicating code. The rules of hooks still apply: only call hooks at the top level, only in React functions.",
          ru: "Пользовательские хуки позволяют извлекать переиспользуемую логику из компонентов. Пользовательский хук — это просто функция, имя которой начинается с \"use\" и которая может вызывать другие хуки внутри себя. Это позволяет делиться логикой с состоянием между компонентами без дублирования кода. Правила хуков по-прежнему действуют: вызывайте хуки только на верхнем уровне, только в React-функциях.",
        },
        code: {
          language: "tsx",
          code: `// Custom hook: useToggle\nfunction useToggle(initial = false) {\n  const [value, setValue] = useState(initial);\n  const toggle = () => setValue((v) => !v);\n  return [value, toggle] as const;\n}\n\n// Usage\nfunction Menu() {\n  const [isOpen, toggleMenu] = useToggle();\n  return (\n    <div>\n      <button onClick={toggleMenu}>{isOpen ? "Close" : "Open"}</button>\n      {isOpen && <nav>Menu items...</nav>}\n    </div>\n  );\n}`,
        },
      },
      {
        title: {
          en: "useLocalStorage Hook",
          ru: "Хук useLocalStorage",
        },
        content: {
          en: "A useLocalStorage hook synchronizes React state with the browser's localStorage. On init it reads the stored value (or uses a default). On every state change it writes back to localStorage. This is a perfect example of combining useState and useEffect in a reusable hook.",
          ru: "Хук useLocalStorage синхронизирует состояние React с localStorage браузера. При инициализации он читает сохранённое значение (или использует значение по умолчанию). При каждом изменении состояния записывает обратно в localStorage. Это отличный пример комбинирования useState и useEffect в переиспользуемом хуке.",
        },
        code: {
          language: "tsx",
          code: `function useLocalStorage<T>(key: string, defaultValue: T) {\n  const [value, setValue] = useState<T>(() => {\n    const stored = localStorage.getItem(key);\n    return stored ? JSON.parse(stored) : defaultValue;\n  });\n\n  useEffect(() => {\n    localStorage.setItem(key, JSON.stringify(value));\n  }, [key, value]);\n\n  return [value, setValue] as const;\n}\n\n// Usage\nconst [theme, setTheme] = useLocalStorage("theme", "light");`,
        },
      },
      {
        title: {
          en: "useFetch Hook",
          ru: "Хук useFetch",
        },
        content: {
          en: "A useFetch hook encapsulates the data-fetching pattern with loading and error states. It takes a URL, fetches data in a useEffect, and returns { data, loading, error }. You can compose hooks together — useFetch might use useState and useEffect internally, and other hooks can use useFetch.",
          ru: "Хук useFetch инкапсулирует паттерн загрузки данных с состояниями загрузки и ошибки. Он принимает URL, загружает данные в useEffect и возвращает { data, loading, error }. Хуки можно компоновать — useFetch внутри использует useState и useEffect, а другие хуки могут использовать useFetch.",
        },
        code: {
          language: "tsx",
          code: `function useFetch<T>(url: string) {\n  const [data, setData] = useState<T | null>(null);\n  const [loading, setLoading] = useState(true);\n  const [error, setError] = useState<string | null>(null);\n\n  useEffect(() => {\n    setLoading(true);\n    fetch(url)\n      .then((res) => res.json())\n      .then((json) => { setData(json); setLoading(false); })\n      .catch((err) => { setError(err.message); setLoading(false); });\n  }, [url]);\n\n  return { data, loading, error };\n}\n\n// Usage\nconst { data: users, loading } = useFetch<User[]>("/api/users");`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What naming rule must a custom hook follow?",
          ru: "Какому правилу именования должен следовать пользовательский хук?",
        },
        options: [
          { en: "Start with \"hook\"", ru: "Начинаться с \"hook\"" },
          { en: "Start with \"use\"", ru: "Начинаться с \"use\"" },
          { en: "Start with an underscore", ru: "Начинаться с подчёркивания" },
          { en: "End with \"Hook\"", ru: "Заканчиваться на \"Hook\"" },
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
          en: "Custom hooks can call other hooks, including useState and useEffect.",
          ru: "Пользовательские хуки могут вызывать другие хуки, включая useState и useEffect.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each custom hook to what it does.",
          ru: "Сопоставьте каждый пользовательский хук с его назначением.",
        },
        pairs: [
          {
            term: { en: "useToggle", ru: "useToggle" },
            definition: {
              en: "Manages a boolean state with a toggle function",
              ru: "Управляет булевым состоянием с функцией переключения",
            },
          },
          {
            term: { en: "useLocalStorage", ru: "useLocalStorage" },
            definition: {
              en: "Syncs React state with browser localStorage",
              ru: "Синхронизирует состояние React с localStorage браузера",
            },
          },
          {
            term: { en: "useFetch", ru: "useFetch" },
            definition: {
              en: "Fetches data from a URL and returns data, loading, and error",
              ru: "Загружает данные по URL и возвращает data, loading и error",
            },
          },
          {
            term: { en: "Rules of Hooks", ru: "Правила хуков" },
            definition: {
              en: "Call hooks at the top level only, only inside React functions",
              ru: "Вызывать хуки только на верхнем уровне, только внутри React-функций",
            },
          },
          {
            term: { en: "Hook composition", ru: "Композиция хуков" },
            definition: {
              en: "Using one custom hook inside another to combine behavior",
              ru: "Использование одного хука внутри другого для комбинирования поведения",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about custom hooks.",
          ru: "Заполните пропуски о пользовательских хуках.",
        },
        blanks: [
          {
            text: {
              en: "A custom hook name must start with ___.",
              ru: "Имя пользовательского хука должно начинаться с ___.",
            },
            options: [
              { en: "use", ru: "use" },
              { en: "hook", ru: "hook" },
              { en: "custom", ru: "custom" },
              { en: "on", ru: "on" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "useLocalStorage typically combines ___ and useEffect internally.",
              ru: "useLocalStorage обычно комбинирует ___ и useEffect внутри себя.",
            },
            options: [
              { en: "useState", ru: "useState" },
              { en: "useRef", ru: "useRef" },
              { en: "useMemo", ru: "useMemo" },
              { en: "useContext", ru: "useContext" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Hooks must be called at the ___ level of a component or hook.",
              ru: "Хуки должны вызываться на ___ уровне компонента или хука.",
            },
            options: [
              { en: "top", ru: "верхнем" },
              { en: "bottom", ru: "нижнем" },
              { en: "any", ru: "любом" },
              { en: "nested", ru: "вложенном" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps to create and use a custom hook.",
          ru: "Расположите шаги создания и использования пользовательского хука.",
        },
        items: [
          { en: "Identify reusable logic in a component", ru: "Определить переиспользуемую логику в компоненте" },
          { en: "Create a function starting with \"use\"", ru: "Создать функцию, начинающуюся с \"use\"" },
          { en: "Move state and effects into the hook", ru: "Перенести состояние и эффекты в хук" },
          { en: "Return needed values and functions", ru: "Вернуть нужные значения и функции" },
          { en: "Call the custom hook in any component", ru: "Вызвать пользовательский хук в любом компоненте" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a useToggle custom hook.",
          ru: "Расположите строки, чтобы создать пользовательский хук useToggle.",
        },
        items: [
          { en: "import { useState } from \"react\";", ru: "import { useState } from \"react\";" },
          { en: "function useToggle(initial = false) {", ru: "function useToggle(initial = false) {" },
          { en: "  const [value, setValue] = useState(initial);", ru: "  const [value, setValue] = useState(initial);" },
          { en: "  const toggle = () => setValue((v) => !v);", ru: "  const toggle = () => setValue((v) => !v);" },
          { en: "  return [value, toggle] as const;", ru: "  return [value, toggle] as const;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What prefix must every custom hook name start with? (write the prefix)",
          ru: "С какого префикса должно начинаться имя каждого пользовательского хука? (напишите префикс)",
        },
        correctText: { en: "use", ru: "use" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms about custom hooks.",
          ru: "Повторите ключевые термины о пользовательских хуках.",
        },
        pairs: [
          {
            term: { en: "Custom Hook", ru: "Пользовательский хук" },
            definition: {
              en: "A reusable function starting with \"use\" that encapsulates stateful logic",
              ru: "Переиспользуемая функция, начинающаяся с \"use\", инкапсулирующая логику с состоянием",
            },
          },
          {
            term: { en: "useLocalStorage", ru: "useLocalStorage" },
            definition: {
              en: "Hook that persists state to localStorage and reads it on mount",
              ru: "Хук, сохраняющий состояние в localStorage и считывающий его при монтировании",
            },
          },
          {
            term: { en: "useFetch", ru: "useFetch" },
            definition: {
              en: "Hook that fetches data and exposes data, loading, and error states",
              ru: "Хук, загружающий данные и предоставляющий состояния data, loading и error",
            },
          },
          {
            term: { en: "Rules of Hooks", ru: "Правила хуков" },
            definition: {
              en: "Hooks must be called at the top level and only in React functions",
              ru: "Хуки должны вызываться на верхнем уровне и только в React-функциях",
            },
          },
          {
            term: { en: "Hook Composition", ru: "Композиция хуков" },
            definition: {
              en: "Building complex hooks by calling simpler hooks inside them",
              ru: "Построение сложных хуков путём вызова более простых хуков внутри них",
            },
          },
        ],
      },
    ],
  },

  "fe-19-1": {
    id: "fe-19-1",
    title: {
      en: "Routing with React Router",
      ru: "Маршрутизация с React Router",
    },
    slides: [
      {
        title: {
          en: "Setting Up React Router",
          ru: "Настройка React Router",
        },
        content: {
          en: "react-router-dom is the standard library for client-side routing in React. Wrap your app in <BrowserRouter> to enable routing. Then define routes using <Routes> and <Route> components. Each Route maps a URL path to a component. The <Link> component navigates between pages without a full page reload.",
          ru: "react-router-dom — стандартная библиотека для клиентской маршрутизации в React. Оберните приложение в <BrowserRouter> для включения маршрутизации. Затем определите маршруты с помощью компонентов <Routes> и <Route>. Каждый Route сопоставляет URL-путь с компонентом. Компонент <Link> обеспечивает навигацию между страницами без полной перезагрузки.",
        },
        code: {
          language: "tsx",
          code: `import { BrowserRouter, Routes, Route, Link } from "react-router-dom";\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <nav>\n        <Link to="/">Home</Link>\n        <Link to="/about">About</Link>\n      </nav>\n      <Routes>\n        <Route path="/" element={<Home />} />\n        <Route path="/about" element={<About />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}`,
        },
      },
      {
        title: {
          en: "Dynamic Routes & useParams",
          ru: "Динамические маршруты и useParams",
        },
        content: {
          en: "Dynamic segments in routes are defined with a colon, like /users/:id. Inside the component, use the useParams() hook to access these dynamic values. The useNavigate() hook lets you navigate programmatically — for example, redirecting after a form submission or a button click.",
          ru: "Динамические сегменты в маршрутах определяются через двоеточие, например /users/:id. Внутри компонента используйте хук useParams() для доступа к этим динамическим значениям. Хук useNavigate() позволяет навигировать программно — например, выполнять редирект после отправки формы или нажатия кнопки.",
        },
        code: {
          language: "tsx",
          code: `import { useParams, useNavigate } from "react-router-dom";\n\nfunction UserProfile() {\n  const { id } = useParams<{ id: string }>();\n  const navigate = useNavigate();\n\n  return (\n    <div>\n      <h1>User #{id}</h1>\n      <button onClick={() => navigate("/")}>Go Home</button>\n    </div>\n  );\n}\n\n// Route definition\n<Route path="/users/:id" element={<UserProfile />} />`,
        },
      },
      {
        title: {
          en: "Nested Routes & Outlet",
          ru: "Вложенные маршруты и Outlet",
        },
        content: {
          en: "Nested routes let you define child routes inside a parent route. The parent component renders an <Outlet /> where child routes appear. This is perfect for layouts — the parent provides shared UI (navbar, sidebar) and the Outlet swaps content based on the URL.",
          ru: "Вложенные маршруты позволяют определять дочерние маршруты внутри родительского. Родительский компонент рендерит <Outlet />, где отображаются дочерние маршруты. Это идеально подходит для лейаутов — родитель предоставляет общий интерфейс (навбар, сайдбар), а Outlet меняет контент в зависимости от URL.",
        },
        code: {
          language: "tsx",
          code: `import { Outlet } from "react-router-dom";\n\nfunction DashboardLayout() {\n  return (\n    <div>\n      <Sidebar />\n      <main>\n        <Outlet /> {/* Child route renders here */}\n      </main>\n    </div>\n  );\n}\n\n// Nested routes\n<Route path="/dashboard" element={<DashboardLayout />}>\n  <Route index element={<Overview />} />\n  <Route path="settings" element={<Settings />} />\n  <Route path="profile" element={<Profile />} />\n</Route>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which component must wrap your app to enable React Router?",
          ru: "Какой компонент должен оборачивать приложение для включения React Router?",
        },
        options: [
          { en: "<RouterProvider>", ru: "<RouterProvider>" },
          { en: "<BrowserRouter>", ru: "<BrowserRouter>" },
          { en: "<RouteWrapper>", ru: "<RouteWrapper>" },
          { en: "<NavigationRoot>", ru: "<NavigationRoot>" },
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
          en: "The <Link> component causes a full page reload when clicked.",
          ru: "Компонент <Link> вызывает полную перезагрузку страницы при клике.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each routing concept to its description.",
          ru: "Сопоставьте каждое понятие маршрутизации с его описанием.",
        },
        pairs: [
          {
            term: { en: "<Route>", ru: "<Route>" },
            definition: {
              en: "Maps a URL path to a React component",
              ru: "Сопоставляет URL-путь с React-компонентом",
            },
          },
          {
            term: { en: "<Link>", ru: "<Link>" },
            definition: {
              en: "Navigates to a route without full page reload",
              ru: "Навигирует к маршруту без полной перезагрузки страницы",
            },
          },
          {
            term: { en: "useParams", ru: "useParams" },
            definition: {
              en: "Hook that reads dynamic URL parameters",
              ru: "Хук, считывающий динамические параметры URL",
            },
          },
          {
            term: { en: "useNavigate", ru: "useNavigate" },
            definition: {
              en: "Hook for programmatic navigation",
              ru: "Хук для программной навигации",
            },
          },
          {
            term: { en: "<Outlet>", ru: "<Outlet>" },
            definition: {
              en: "Placeholder where nested child routes render",
              ru: "Плейсхолдер, где рендерятся вложенные дочерние маршруты",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about React Router.",
          ru: "Заполните пропуски о React Router.",
        },
        blanks: [
          {
            text: {
              en: "Dynamic route parameters are defined with a ___ prefix, like /users/:id.",
              ru: "Динамические параметры маршрута определяются с помощью префикса ___, например /users/:id.",
            },
            options: [
              { en: "colon (:)", ru: "двоеточие (:)" },
              { en: "hash (#)", ru: "решётка (#)" },
              { en: "dollar ($)", ru: "доллар ($)" },
              { en: "asterisk (*)", ru: "звёздочка (*)" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ hook lets you navigate programmatically in code.",
              ru: "Хук ___ позволяет навигировать программно в коде.",
            },
            options: [
              { en: "useNavigate", ru: "useNavigate" },
              { en: "useHistory", ru: "useHistory" },
              { en: "useRouter", ru: "useRouter" },
              { en: "useRedirect", ru: "useRedirect" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "In nested routes, the parent component uses ___ to render child routes.",
              ru: "Во вложенных маршрутах родительский компонент использует ___ для рендеринга дочерних маршрутов.",
            },
            options: [
              { en: "<Outlet />", ru: "<Outlet />" },
              { en: "<Children />", ru: "<Children />" },
              { en: "<Slot />", ru: "<Slot />" },
              { en: "<View />", ru: "<View />" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the elements to set up routing in a React app.",
          ru: "Расположите элементы для настройки маршрутизации в React-приложении.",
        },
        items: [
          { en: "Import BrowserRouter, Routes, Route", ru: "Импортировать BrowserRouter, Routes, Route" },
          { en: "Wrap the app in <BrowserRouter>", ru: "Обернуть приложение в <BrowserRouter>" },
          { en: "Add <Routes> container", ru: "Добавить контейнер <Routes>" },
          { en: "Define <Route path element> for each page", ru: "Определить <Route path element> для каждой страницы" },
          { en: "Use <Link to> for navigation", ru: "Использовать <Link to> для навигации" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to set up basic routing.",
          ru: "Расположите строки для настройки базовой маршрутизации.",
        },
        items: [
          { en: "import { BrowserRouter, Routes, Route } from \"react-router-dom\";", ru: "import { BrowserRouter, Routes, Route } from \"react-router-dom\";" },
          { en: "function App() {", ru: "function App() {" },
          { en: "  return (", ru: "  return (" },
          { en: "    <BrowserRouter>", ru: "    <BrowserRouter>" },
          { en: "      <Routes>", ru: "      <Routes>" },
          { en: "        <Route path=\"/\" element={<Home />} />", ru: "        <Route path=\"/\" element={<Home />} />" },
          { en: "      </Routes>", ru: "      </Routes>" },
          { en: "    </BrowserRouter>", ru: "    </BrowserRouter>" },
          { en: "  );", ru: "  );" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What hook do you use to read dynamic URL parameters like :id? (write the hook name)",
          ru: "Какой хук используется для чтения динамических параметров URL, таких как :id? (напишите имя хука)",
        },
        correctText: { en: "useParams", ru: "useParams" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key React Router terms.",
          ru: "Повторите ключевые термины React Router.",
        },
        pairs: [
          {
            term: { en: "BrowserRouter", ru: "BrowserRouter" },
            definition: {
              en: "Wrapper component that enables HTML5 history-based routing",
              ru: "Компонент-обёртка, включающий маршрутизацию на основе HTML5 History API",
            },
          },
          {
            term: { en: "Route", ru: "Route" },
            definition: {
              en: "Declares which component to render for a given URL path",
              ru: "Объявляет, какой компонент рендерить для данного URL-пути",
            },
          },
          {
            term: { en: "Link", ru: "Link" },
            definition: {
              en: "A component that navigates between routes without page reloads",
              ru: "Компонент, навигирующий между маршрутами без перезагрузки страницы",
            },
          },
          {
            term: { en: "Outlet", ru: "Outlet" },
            definition: {
              en: "Renders the matching child route inside a parent layout",
              ru: "Рендерит совпадающий дочерний маршрут внутри родительского лейаута",
            },
          },
          {
            term: { en: "Nested Routes", ru: "Вложенные маршруты" },
            definition: {
              en: "Routes defined inside a parent Route, sharing the parent's layout",
              ru: "Маршруты, определённые внутри родительского Route, разделяющие лейаут родителя",
            },
          },
        ],
      },
    ],
  },

  "fe-20-1": {
    id: "fe-20-1",
    title: {
      en: "State Management",
      ru: "Управление состоянием",
    },
    slides: [
      {
        title: {
          en: "React Context & useContext",
          ru: "React Context и useContext",
        },
        content: {
          en: "React Context lets you pass data through the component tree without manually passing props at every level (prop drilling). You create a context with createContext(), wrap a subtree with a Provider, and consume the value in any descendant with useContext(). Context is ideal for global data like theme, locale, or auth status.",
          ru: "React Context позволяет передавать данные через дерево компонентов, не передавая props вручную на каждом уровне (prop drilling). Создайте контекст с помощью createContext(), оберните поддерево в Provider и используйте значение в любом потомке через useContext(). Context идеально подходит для глобальных данных: тема, локаль, статус авторизации.",
        },
        code: {
          language: "tsx",
          code: `import { createContext, useContext, useState } from "react";\n\nconst ThemeContext = createContext<"light" | "dark">("light");\n\nfunction ThemeProvider({ children }: { children: React.ReactNode }) {\n  const [theme, setTheme] = useState<"light" | "dark">("light");\n  return (\n    <ThemeContext.Provider value={theme}>\n      {children}\n    </ThemeContext.Provider>\n  );\n}\n\nfunction Header() {\n  const theme = useContext(ThemeContext);\n  return <header className={theme}>My App</header>;\n}`,
        },
      },
      {
        title: {
          en: "Zustand Basics",
          ru: "Основы Zustand",
        },
        content: {
          en: "Zustand is a lightweight state management library. You create a store with create(), define state and actions in one place, and use the store hook in any component. Unlike Context, Zustand only re-renders components that use the specific piece of state that changed. No providers or wrappers needed.",
          ru: "Zustand — легковесная библиотека для управления состоянием. Вы создаёте хранилище с помощью create(), определяете состояние и действия в одном месте и используете хук хранилища в любом компоненте. В отличие от Context, Zustand перерисовывает только компоненты, использующие конкретную часть состояния, которая изменилась. Никаких провайдеров или обёрток не нужно.",
        },
        code: {
          language: "tsx",
          code: `import { create } from "zustand";\n\ninterface CounterStore {\n  count: number;\n  increment: () => void;\n  decrement: () => void;\n}\n\nconst useCounterStore = create<CounterStore>((set) => ({\n  count: 0,\n  increment: () => set((s) => ({ count: s.count + 1 })),\n  decrement: () => set((s) => ({ count: s.count - 1 })),\n}));\n\nfunction Counter() {\n  const { count, increment } = useCounterStore();\n  return <button onClick={increment}>Count: {count}</button>;\n}`,
        },
      },
      {
        title: {
          en: "When to Use What",
          ru: "Когда что использовать",
        },
        content: {
          en: "Use local state (useState) for data that belongs to one component. Use Context for low-frequency global data like theme or auth. Use Zustand (or similar) for frequently changing shared state or complex state logic. The key principle: keep state as local as possible, and lift it up only when needed.",
          ru: "Используйте локальное состояние (useState) для данных, принадлежащих одному компоненту. Используйте Context для редко меняющихся глобальных данных, таких как тема или авторизация. Используйте Zustand (или аналог) для часто меняющегося общего состояния или сложной логики состояния. Ключевой принцип: держите состояние максимально локальным и поднимайте вверх только при необходимости.",
        },
        code: {
          language: "tsx",
          code: `// Local state — for one component\nconst [isOpen, setIsOpen] = useState(false);\n\n// Context — for global, low-frequency data\nconst theme = useContext(ThemeContext);\n\n// Zustand — for shared, frequently updated state\nconst items = useCartStore((s) => s.items);\n\n// Rule of thumb:\n// 1 component → useState\n// Whole app, rarely changes → Context\n// Multiple components, frequent updates → Zustand`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What problem does React Context solve?",
          ru: "Какую проблему решает React Context?",
        },
        options: [
          { en: "Slow rendering performance", ru: "Медленную производительность рендеринга" },
          { en: "Prop drilling through many component levels", ru: "Прокидывание props через множество уровней компонентов" },
          { en: "Memory leaks in useEffect", ru: "Утечки памяти в useEffect" },
          { en: "CSS styling conflicts", ru: "Конфликты CSS-стилей" },
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
          en: "Zustand requires wrapping your app in a Provider component.",
          ru: "Zustand требует оборачивания приложения в компонент Provider.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each state solution to its best use case.",
          ru: "Сопоставьте каждое решение для состояния с его лучшим применением.",
        },
        pairs: [
          {
            term: { en: "useState", ru: "useState" },
            definition: {
              en: "State that belongs to a single component",
              ru: "Состояние, принадлежащее одному компоненту",
            },
          },
          {
            term: { en: "React Context", ru: "React Context" },
            definition: {
              en: "Global data that changes infrequently (theme, locale)",
              ru: "Глобальные данные, которые редко меняются (тема, локаль)",
            },
          },
          {
            term: { en: "Zustand", ru: "Zustand" },
            definition: {
              en: "Shared state with frequent updates and selective re-renders",
              ru: "Общее состояние с частыми обновлениями и выборочной перерисовкой",
            },
          },
          {
            term: { en: "Prop drilling", ru: "Prop drilling" },
            definition: {
              en: "Passing data through many intermediate components (anti-pattern)",
              ru: "Передача данных через множество промежуточных компонентов (антипаттерн)",
            },
          },
          {
            term: { en: "Lifting state up", ru: "Подъём состояния" },
            definition: {
              en: "Moving state to the nearest common ancestor of components that need it",
              ru: "Перемещение состояния к ближайшему общему предку компонентов, которым оно нужно",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about state management.",
          ru: "Заполните пропуски об управлении состоянием.",
        },
        blanks: [
          {
            text: {
              en: "You create a context using ___().",
              ru: "Контекст создаётся с помощью ___().",
            },
            options: [
              { en: "createContext", ru: "createContext" },
              { en: "useContext", ru: "useContext" },
              { en: "newContext", ru: "newContext" },
              { en: "makeContext", ru: "makeContext" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "In Zustand, you define a store using the ___ function.",
              ru: "В Zustand хранилище создаётся с помощью функции ___.",
            },
            options: [
              { en: "create", ru: "create" },
              { en: "createStore", ru: "createStore" },
              { en: "defineStore", ru: "defineStore" },
              { en: "useStore", ru: "useStore" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The best practice is to keep state as ___ as possible.",
              ru: "Лучшая практика — держать состояние максимально ___.",
            },
            options: [
              { en: "local", ru: "локальным" },
              { en: "global", ru: "глобальным" },
              { en: "immutable", ru: "неизменяемым" },
              { en: "complex", ru: "сложным" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps to set up and use React Context.",
          ru: "Расположите шаги настройки и использования React Context.",
        },
        items: [
          { en: "Call createContext() with a default value", ru: "Вызвать createContext() со значением по умолчанию" },
          { en: "Create a Provider component with state", ru: "Создать компонент Provider с состоянием" },
          { en: "Wrap the component tree with the Provider", ru: "Обернуть дерево компонентов в Provider" },
          { en: "Call useContext() in a descendant component", ru: "Вызвать useContext() в компоненте-потомке" },
          { en: "Use the context value in the component", ru: "Использовать значение контекста в компоненте" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to create a Zustand store.",
          ru: "Расположите строки, чтобы создать Zustand-хранилище.",
        },
        items: [
          { en: "import { create } from \"zustand\";", ru: "import { create } from \"zustand\";" },
          { en: "const useStore = create((set) => ({", ru: "const useStore = create((set) => ({" },
          { en: "  count: 0,", ru: "  count: 0," },
          { en: "  increment: () => set((s) => ({ count: s.count + 1 })),", ru: "  increment: () => set((s) => ({ count: s.count + 1 }))," },
          { en: "}));", ru: "}));" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What hook reads the value from a React Context? (write the hook name)",
          ru: "Какой хук считывает значение из React Context? (напишите имя хука)",
        },
        correctText: { en: "useContext", ru: "useContext" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key state management terms.",
          ru: "Повторите ключевые термины управления состоянием.",
        },
        pairs: [
          {
            term: { en: "React Context", ru: "React Context" },
            definition: {
              en: "Built-in API for passing data through the component tree without prop drilling",
              ru: "Встроенный API для передачи данных через дерево компонентов без prop drilling",
            },
          },
          {
            term: { en: "Provider", ru: "Provider" },
            definition: {
              en: "A component that supplies the context value to its descendants",
              ru: "Компонент, предоставляющий значение контекста своим потомкам",
            },
          },
          {
            term: { en: "Zustand", ru: "Zustand" },
            definition: {
              en: "A minimal state management library with no providers required",
              ru: "Минималистичная библиотека управления состоянием, не требующая провайдеров",
            },
          },
          {
            term: { en: "Prop drilling", ru: "Prop drilling" },
            definition: {
              en: "The anti-pattern of passing props through many layers of components",
              ru: "Антипаттерн передачи props через множество слоёв компонентов",
            },
          },
          {
            term: { en: "Selective re-render", ru: "Выборочная перерисовка" },
            definition: {
              en: "Only re-rendering components that use the specific changed state slice",
              ru: "Перерисовка только тех компонентов, которые используют конкретную изменившуюся часть состояния",
            },
          },
        ],
      },
    ],
  },
};
