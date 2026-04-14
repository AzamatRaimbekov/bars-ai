import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_V2_JUNIOR_HTML: Record<string, LessonContentV2> = {
  "fe-2-1": {
    id: "fe-2-1",
    title: { en: "Form Elements", ru: "Элементы форм" },
    slides: [
      {
        title: { en: "Building HTML Forms", ru: "Создание HTML-форм" },
        content: {
          en: "Forms are the primary way users send data to a server. The <form> element wraps all form controls and defines where data is submitted via the `action` attribute and how it is sent via the `method` attribute (GET or POST). Every form control should be paired with a <label> element — this improves accessibility and allows users to click the label to focus the input. You can link a label to an input using the `for` attribute that matches the input's `id`.",
          ru: "Формы — основной способ отправки данных пользователем на сервер. Элемент <form> оборачивает все элементы управления и определяет, куда отправляются данные (атрибут `action`) и каким методом (атрибут `method` — GET или POST). Каждый элемент формы должен быть связан с элементом <label> — это улучшает доступность и позволяет кликнуть по подписи для фокусировки на поле ввода. Связь задаётся через атрибут `for`, совпадающий с `id` поля.",
        },
        code: {
          language: "html",
          code: `<form action="/submit" method="POST">
  <label for="name">Full Name</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>

  <button type="submit">Send</button>
</form>`,
        },
      },
      {
        title: { en: "Input Types and Select", ru: "Типы полей ввода и выпадающие списки" },
        content: {
          en: "HTML5 introduced many specialized input types: `text`, `email`, `password`, `number`, `date`, `checkbox`, `radio`, `file`, and more. Each type provides built-in validation and a tailored interface (e.g., a date picker for `date`, a numeric keypad for `number` on mobile). The <select> element creates a dropdown list. It contains <option> elements, each with a `value` attribute sent to the server. You can group options using <optgroup> and allow multiple selections with the `multiple` attribute.",
          ru: "HTML5 ввёл множество специализированных типов полей: `text`, `email`, `password`, `number`, `date`, `checkbox`, `radio`, `file` и другие. Каждый тип обеспечивает встроенную валидацию и адаптированный интерфейс (например, выбор даты для `date`, цифровая клавиатура для `number` на мобильных). Элемент <select> создаёт выпадающий список. Он содержит элементы <option>, каждый с атрибутом `value`, который отправляется на сервер. Опции можно группировать через <optgroup>, а множественный выбор включается атрибутом `multiple`.",
        },
        code: {
          language: "html",
          code: `<label for="role">Role</label>
<select id="role" name="role">
  <option value="">-- Choose --</option>
  <option value="dev">Developer</option>
  <option value="design">Designer</option>
  <option value="pm">Project Manager</option>
</select>

<label>
  <input type="checkbox" name="agree" value="yes">
  I agree to the terms
</label>`,
        },
      },
      {
        title: { en: "Textarea, Fieldset, and Buttons", ru: "Textarea, Fieldset и кнопки" },
        content: {
          en: "The <textarea> element is used for multi-line text input, such as comments or messages. Unlike <input>, its size is controlled with `rows` and `cols` attributes. The <fieldset> element groups related form controls together, and <legend> provides a caption for the group — this is especially important for accessibility. Buttons have three types: `submit` sends the form, `reset` clears all fields, and `button` does nothing by default (used with JavaScript). Always specify the `type` attribute on buttons inside forms to avoid accidental submission.",
          ru: "Элемент <textarea> используется для многострочного текстового ввода — комментариев, сообщений. В отличие от <input>, его размер задаётся атрибутами `rows` и `cols`. Элемент <fieldset> группирует связанные элементы формы, а <legend> задаёт заголовок группы — это особенно важно для доступности. У кнопок три типа: `submit` отправляет форму, `reset` очищает все поля, а `button` по умолчанию ничего не делает (используется с JavaScript). Всегда указывайте атрибут `type` у кнопок внутри форм, чтобы избежать случайной отправки.",
        },
        code: {
          language: "html",
          code: `<fieldset>
  <legend>Contact Information</legend>

  <label for="msg">Message</label>
  <textarea id="msg" name="message" rows="5" cols="40"
            placeholder="Type your message..."></textarea>

  <button type="submit">Submit</button>
  <button type="reset">Clear</button>
</fieldset>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which attribute on a <label> element links it to a specific form control?",
          ru: "Какой атрибут элемента <label> связывает его с определённым полем формы?",
        },
        options: [
          { en: "name", ru: "name" },
          { en: "for", ru: "for" },
          { en: "link", ru: "link" },
          { en: "target", ru: "target" },
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
          en: "A <button> element inside a <form> without a type attribute will behave as a submit button by default.",
          ru: "Элемент <button> внутри <form> без атрибута type по умолчанию действует как кнопка отправки формы.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each form element with its purpose.",
          ru: "Сопоставьте каждый элемент формы с его назначением.",
        },
        pairs: [
          {
            term: { en: "<input type=\"email\">", ru: "<input type=\"email\">" },
            definition: { en: "Email field with built-in validation", ru: "Поле для email со встроенной валидацией" },
          },
          {
            term: { en: "<textarea>", ru: "<textarea>" },
            definition: { en: "Multi-line text input", ru: "Многострочное текстовое поле" },
          },
          {
            term: { en: "<select>", ru: "<select>" },
            definition: { en: "Dropdown selection list", ru: "Выпадающий список" },
          },
          {
            term: { en: "<fieldset>", ru: "<fieldset>" },
            definition: { en: "Groups related form controls", ru: "Группирует связанные элементы формы" },
          },
          {
            term: { en: "<legend>", ru: "<legend>" },
            definition: { en: "Caption for a fieldset", ru: "Заголовок группы fieldset" },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Complete the form element attributes.",
          ru: "Заполните атрибуты элементов формы.",
        },
        blanks: [
          {
            text: {
              en: "The <form> element sends data using the ___ attribute to specify the HTTP method.",
              ru: "Элемент <form> отправляет данные, используя атрибут ___ для указания HTTP-метода.",
            },
            options: [
              { en: "method", ru: "method" },
              { en: "action", ru: "action" },
              { en: "type", ru: "type" },
              { en: "enctype", ru: "enctype" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To make a form field mandatory, add the ___ attribute.",
              ru: "Чтобы сделать поле формы обязательным, добавьте атрибут ___.",
            },
            options: [
              { en: "required", ru: "required" },
              { en: "mandatory", ru: "mandatory" },
              { en: "validate", ru: "validate" },
              { en: "must", ru: "must" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The <textarea> element uses the ___ attribute to set the number of visible text lines.",
              ru: "Элемент <textarea> использует атрибут ___ для задания количества видимых строк.",
            },
            options: [
              { en: "rows", ru: "rows" },
              { en: "lines", ru: "lines" },
              { en: "height", ru: "height" },
              { en: "size", ru: "size" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange these steps to create a complete form in the correct order.",
          ru: "Расположите шаги создания полной формы в правильном порядке.",
        },
        items: [
          { en: "Create the <form> element with action and method", ru: "Создать элемент <form> с action и method" },
          { en: "Add <fieldset> and <legend> for grouping", ru: "Добавить <fieldset> и <legend> для группировки" },
          { en: "Add <label> and <input> pairs for each field", ru: "Добавить пары <label> и <input> для каждого поля" },
          { en: "Add validation attributes (required, pattern)", ru: "Добавить атрибуты валидации (required, pattern)" },
          { en: "Add a <button type=\"submit\"> to send the form", ru: "Добавить <button type=\"submit\"> для отправки формы" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange these lines to build a login form.",
          ru: "Расположите строки кода для создания формы входа.",
        },
        items: [
          { en: "<form action=\"/login\" method=\"POST\">", ru: "<form action=\"/login\" method=\"POST\">" },
          { en: "  <label for=\"user\">Username</label>", ru: "  <label for=\"user\">Имя пользователя</label>" },
          { en: "  <input type=\"text\" id=\"user\" name=\"username\" required>", ru: "  <input type=\"text\" id=\"user\" name=\"username\" required>" },
          { en: "  <label for=\"pass\">Password</label>", ru: "  <label for=\"pass\">Пароль</label>" },
          { en: "  <input type=\"password\" id=\"pass\" name=\"password\" required>", ru: "  <input type=\"password\" id=\"pass\" name=\"password\" required>" },
          { en: "  <button type=\"submit\">Log In</button>", ru: "  <button type=\"submit\">Войти</button>" },
          { en: "</form>", ru: "</form>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What HTML attribute on <input> specifies the key name sent to the server when the form is submitted?",
          ru: "Какой атрибут <input> задаёт имя ключа, отправляемого на сервер при отправке формы?",
        },
        correctText: { en: "name", ru: "name" },
      },
      {
        type: "flash_cards",
        question: { en: "Review key terms.", ru: "Повторите ключевые термины." },
        pairs: [
          {
            term: { en: "<form>", ru: "<form>" },
            definition: { en: "Container element that wraps form controls and defines submission target", ru: "Контейнер, оборачивающий элементы формы и определяющий цель отправки" },
          },
          {
            term: { en: "<label>", ru: "<label>" },
            definition: { en: "Text caption linked to a form control for accessibility", ru: "Текстовая подпись, связанная с элементом формы для доступности" },
          },
          {
            term: { en: "<fieldset>", ru: "<fieldset>" },
            definition: { en: "Groups related form controls with an optional legend", ru: "Группирует связанные элементы формы с необязательным заголовком" },
          },
          {
            term: { en: "required", ru: "required" },
            definition: { en: "Boolean attribute that prevents form submission until the field is filled", ru: "Булев атрибут, запрещающий отправку формы, пока поле не заполнено" },
          },
          {
            term: { en: "placeholder", ru: "placeholder" },
            definition: { en: "Hint text shown inside an input when it is empty", ru: "Подсказка, отображаемая внутри поля ввода, пока оно пустое" },
          },
        ],
      },
    ],
  },

  "fe-2-2": {
    id: "fe-2-2",
    title: { en: "Tables", ru: "Таблицы" },
    slides: [
      {
        title: { en: "HTML Table Structure", ru: "Структура HTML-таблиц" },
        content: {
          en: "HTML tables display data in rows and columns. The <table> element is the container. Inside it, <thead> defines the header section, <tbody> holds the main data rows, and an optional <tfoot> contains footer rows (like totals). Each row is created with <tr>. Inside the header, use <th> (table header) cells which are bold and centered by default. Inside the body, use <td> (table data) cells. Always use <thead> and <tbody> to give your table semantic structure — this helps screen readers navigate the data and allows independent scrolling of the body.",
          ru: "HTML-таблицы отображают данные в строках и столбцах. Элемент <table> — контейнер. Внутри него <thead> определяет заголовочную часть, <tbody> содержит основные строки данных, а необязательный <tfoot> — строки итогов. Каждая строка создаётся элементом <tr>. В заголовке используются ячейки <th> (выделяются жирным и центрируются по умолчанию), а в теле — ячейки <td>. Всегда используйте <thead> и <tbody> для семантической структуры — это помогает скринридерам навигировать по данным и позволяет независимую прокрутку тела таблицы.",
        },
        code: {
          language: "html",
          code: `<table>
  <thead>
    <tr>
      <th>Product</th>
      <th>Price</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop</td>
      <td>$999</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Mouse</td>
      <td>$25</td>
      <td>50</td>
    </tr>
  </tbody>
</table>`,
        },
      },
      {
        title: { en: "Colspan and Rowspan", ru: "Colspan и Rowspan" },
        content: {
          en: "Sometimes a cell needs to span across multiple columns or rows. The `colspan` attribute on <td> or <th> makes a cell stretch horizontally across the specified number of columns. The `rowspan` attribute makes a cell stretch vertically across multiple rows. When using rowspan, remember that the spanned rows must not include cells in the position already occupied by the spanning cell. These attributes are commonly used for grouped headers, subtotals, or merged category labels.",
          ru: "Иногда ячейке нужно занимать несколько столбцов или строк. Атрибут `colspan` у <td> или <th> растягивает ячейку горизонтально на указанное число столбцов. Атрибут `rowspan` растягивает ячейку вертикально на несколько строк. При использовании rowspan помните, что объединённые строки не должны содержать ячейки в позиции, уже занятой растянутой ячейкой. Эти атрибуты часто используются для группировки заголовков, промежуточных итогов или объединённых меток категорий.",
        },
        code: {
          language: "html",
          code: `<table>
  <thead>
    <tr>
      <th colspan="2">Student Info</th>
      <th>Grade</th>
    </tr>
    <tr>
      <th>First Name</th>
      <th>Last Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>Smith</td>
      <td rowspan="2">A</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>Smith</td>
    </tr>
  </tbody>
</table>`,
        },
      },
      {
        title: { en: "Table Accessibility and Best Practices", ru: "Доступность таблиц и лучшие практики" },
        content: {
          en: "For accessible tables, use the <caption> element as the first child of <table> to provide a descriptive title. Add the `scope` attribute to <th> elements: `scope=\"col\"` for column headers and `scope=\"row\"` for row headers — this tells assistive technology how to associate headers with data cells. For complex tables, use `id` on headers and `headers` attribute on data cells. Never use tables for page layout — they should only contain tabular data. Use CSS for styling: borders, spacing, striped rows, and hover effects.",
          ru: "Для доступных таблиц используйте элемент <caption> как первый дочерний элемент <table> для описательного заголовка. Добавляйте атрибут `scope` к элементам <th>: `scope=\"col\"` для заголовков столбцов и `scope=\"row\"` для заголовков строк — это сообщает вспомогательным технологиям, как связать заголовки с ячейками данных. Для сложных таблиц используйте `id` у заголовков и атрибут `headers` у ячеек данных. Никогда не используйте таблицы для разметки страницы — только для табличных данных. Стилизуйте с помощью CSS: границы, отступы, чередование цветов строк, эффекты при наведении.",
        },
        code: {
          language: "html",
          code: `<table>
  <caption>Quarterly Sales Report</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Q1</th>
      <th scope="col">Q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>$12,000</td>
      <td>$15,000</td>
    </tr>
    <tr>
      <th scope="row">South</th>
      <td>$9,500</td>
      <td>$11,200</td>
    </tr>
  </tbody>
</table>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which element should be used for header cells in a table?",
          ru: "Какой элемент следует использовать для ячеек заголовка в таблице?",
        },
        options: [
          { en: "<td>", ru: "<td>" },
          { en: "<header>", ru: "<header>" },
          { en: "<th>", ru: "<th>" },
          { en: "<head>", ru: "<head>" },
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
          en: "The colspan attribute makes a table cell span across multiple rows vertically.",
          ru: "Атрибут colspan растягивает ячейку таблицы вертикально на несколько строк.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each table element with its role.",
          ru: "Сопоставьте каждый элемент таблицы с его ролью.",
        },
        pairs: [
          {
            term: { en: "<thead>", ru: "<thead>" },
            definition: { en: "Contains header rows", ru: "Содержит строки заголовков" },
          },
          {
            term: { en: "<tbody>", ru: "<tbody>" },
            definition: { en: "Contains main data rows", ru: "Содержит основные строки данных" },
          },
          {
            term: { en: "<caption>", ru: "<caption>" },
            definition: { en: "Descriptive title for the table", ru: "Описательный заголовок таблицы" },
          },
          {
            term: { en: "scope", ru: "scope" },
            definition: { en: "Defines header-cell association direction", ru: "Определяет направление связи заголовка с ячейками" },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Complete the table-related statements.",
          ru: "Заполните пропуски в утверждениях о таблицах.",
        },
        blanks: [
          {
            text: {
              en: "To merge a cell across 3 columns, use the attribute ___=\"3\" on the cell.",
              ru: "Чтобы объединить ячейку на 3 столбца, используйте атрибут ___=\"3\".",
            },
            options: [
              { en: "colspan", ru: "colspan" },
              { en: "rowspan", ru: "rowspan" },
              { en: "span", ru: "span" },
              { en: "merge", ru: "merge" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Each row in a table is defined with the ___ element.",
              ru: "Каждая строка таблицы определяется элементом ___.",
            },
            options: [
              { en: "<tr>", ru: "<tr>" },
              { en: "<row>", ru: "<row>" },
              { en: "<td>", ru: "<td>" },
              { en: "<line>", ru: "<line>" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ element should be the first child of <table> to provide a visible title.",
              ru: "Элемент ___ должен быть первым дочерним элементом <table> для видимого заголовка.",
            },
            options: [
              { en: "<caption>", ru: "<caption>" },
              { en: "<title>", ru: "<title>" },
              { en: "<header>", ru: "<header>" },
              { en: "<label>", ru: "<label>" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the table elements from outermost to innermost.",
          ru: "Расположите элементы таблицы от внешнего к внутреннему.",
        },
        items: [
          { en: "<table>", ru: "<table>" },
          { en: "<thead> / <tbody>", ru: "<thead> / <tbody>" },
          { en: "<tr>", ru: "<tr>" },
          { en: "<th> / <td>", ru: "<th> / <td>" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange these lines to create a table with a caption and header.",
          ru: "Расположите строки кода для создания таблицы с заголовком.",
        },
        items: [
          { en: "<table>", ru: "<table>" },
          { en: "  <caption>Employee List</caption>", ru: "  <caption>Список сотрудников</caption>" },
          { en: "  <thead>", ru: "  <thead>" },
          { en: "    <tr><th>Name</th><th>Role</th></tr>", ru: "    <tr><th>Имя</th><th>Роль</th></tr>" },
          { en: "  </thead>", ru: "  </thead>" },
          { en: "  <tbody>", ru: "  <tbody>" },
          { en: "    <tr><td>Anna</td><td>Developer</td></tr>", ru: "    <tr><td>Анна</td><td>Разработчик</td></tr>" },
          { en: "  </tbody>", ru: "  </tbody>" },
          { en: "</table>", ru: "</table>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What attribute on <th> specifies whether it is a column header or a row header?",
          ru: "Какой атрибут у <th> указывает, является ли он заголовком столбца или строки?",
        },
        correctText: { en: "scope", ru: "scope" },
      },
      {
        type: "flash_cards",
        question: { en: "Review key terms.", ru: "Повторите ключевые термины." },
        pairs: [
          {
            term: { en: "<table>", ru: "<table>" },
            definition: { en: "Root container element for tabular data", ru: "Корневой контейнер для табличных данных" },
          },
          {
            term: { en: "<tr>", ru: "<tr>" },
            definition: { en: "Defines a single row in a table", ru: "Определяет одну строку в таблице" },
          },
          {
            term: { en: "colspan", ru: "colspan" },
            definition: { en: "Attribute that merges a cell across multiple columns", ru: "Атрибут, объединяющий ячейку по нескольким столбцам" },
          },
          {
            term: { en: "rowspan", ru: "rowspan" },
            definition: { en: "Attribute that merges a cell across multiple rows", ru: "Атрибут, объединяющий ячейку по нескольким строкам" },
          },
          {
            term: { en: "<caption>", ru: "<caption>" },
            definition: { en: "Provides an accessible title for the entire table", ru: "Предоставляет доступный заголовок для всей таблицы" },
          },
        ],
      },
    ],
  },

  "fe-3-1": {
    id: "fe-3-1",
    title: { en: "Semantic Elements", ru: "Семантические элементы" },
    slides: [
      {
        title: { en: "Why Semantic HTML Matters", ru: "Зачем нужен семантический HTML" },
        content: {
          en: "Semantic HTML uses elements that describe the meaning of content rather than just its appearance. Instead of using <div> for everything, HTML5 introduced elements like <header>, <nav>, <main>, <section>, <article>, <aside>, and <footer>. These elements carry meaning: a <nav> tells browsers and screen readers \"this is navigation,\" while a <div> says nothing. Benefits include better accessibility (screen readers can jump between landmarks), improved SEO (search engines understand page structure), and cleaner, more maintainable code.",
          ru: "Семантический HTML использует элементы, описывающие смысл содержимого, а не просто его внешний вид. Вместо <div> для всего HTML5 ввёл элементы <header>, <nav>, <main>, <section>, <article>, <aside> и <footer>. Они несут смысловую нагрузку: <nav> сообщает браузерам и скринридерам «это навигация», тогда как <div> ничего не говорит. Преимущества: улучшенная доступность (скринридеры могут переключаться между ориентирами), лучшее SEO (поисковики понимают структуру страницы) и более чистый, поддерживаемый код.",
        },
        code: {
          language: "html",
          code: `<!-- Non-semantic (avoid) -->
<div class="header">...</div>
<div class="nav">...</div>
<div class="content">...</div>

<!-- Semantic (preferred) -->
<header>...</header>
<nav>...</nav>
<main>...</main>`,
        },
      },
      {
        title: { en: "Page Layout with Semantic Elements", ru: "Разметка страницы семантическими элементами" },
        content: {
          en: "A typical page layout uses these elements together. <header> contains the site logo, title, and top-level navigation. <nav> holds the main navigation links — a page can have multiple <nav> elements (e.g., main nav and footer nav). <main> wraps the primary content unique to that page — there must be only one <main> per page. Inside <main>, use <section> for thematic groupings of content (each should have a heading) and <article> for self-contained content that makes sense on its own (blog posts, news articles, product cards). <aside> is for supplementary content like sidebars, related links, or ads.",
          ru: "Типичная разметка страницы использует эти элементы вместе. <header> содержит логотип сайта, заголовок и основную навигацию. <nav> содержит навигационные ссылки — на странице может быть несколько <nav> (например, основная навигация и навигация в подвале). <main> оборачивает основной контент, уникальный для данной страницы — на странице должен быть только один <main>. Внутри <main> используйте <section> для тематических группировок (каждая должна иметь заголовок) и <article> для самостоятельного контента, понятного вне контекста (статьи блога, новости, карточки товаров). <aside> — для дополнительного контента: боковые панели, связанные ссылки, реклама.",
        },
        code: {
          language: "html",
          code: `<body>
  <header>
    <h1>My Blog</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
    </nav>
  </header>
  <main>
    <section>
      <h2>Recent Posts</h2>
      <article>
        <h3>Learning Semantic HTML</h3>
        <p>Semantic elements improve...</p>
      </article>
    </section>
    <aside>
      <h2>Related Links</h2>
      <ul><li><a href="#">CSS Guide</a></li></ul>
    </aside>
  </main>
  <footer>&copy; 2026 My Blog</footer>
</body>`,
        },
      },
      {
        title: { en: "Figure, Figcaption, and Other Semantic Elements", ru: "Figure, Figcaption и другие семантические элементы" },
        content: {
          en: "The <figure> element represents self-contained content, often an image, diagram, or code snippet, that is referenced from the main flow. <figcaption> provides a caption for the figure — it must be the first or last child of <figure>. Other useful semantic elements include <time> for dates and times (with a machine-readable `datetime` attribute), <address> for contact information, <details> and <summary> for collapsible sections, and <mark> for highlighted text. Using these elements correctly makes your HTML a meaningful document rather than a collection of styled divs.",
          ru: "Элемент <figure> представляет самостоятельный контент — часто изображение, диаграмму или фрагмент кода, — на который ссылаются из основного потока. <figcaption> задаёт подпись к figure — он должен быть первым или последним дочерним элементом <figure>. Другие полезные семантические элементы: <time> для дат и времени (с машинночитаемым атрибутом `datetime`), <address> для контактной информации, <details> и <summary> для сворачиваемых секций, <mark> для выделенного текста. Правильное использование этих элементов превращает HTML в осмысленный документ, а не набор стилизованных div.",
        },
        code: {
          language: "html",
          code: `<figure>
  <img src="chart.png" alt="Sales growth chart for 2026">
  <figcaption>Figure 1: Sales grew 25% in Q1 2026.</figcaption>
</figure>

<details>
  <summary>Show more details</summary>
  <p>Here is the extended description...</p>
</details>

<p>Published on
  <time datetime="2026-04-08">April 8, 2026</time>
</p>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "How many <main> elements are allowed per HTML page?",
          ru: "Сколько элементов <main> допускается на одной HTML-странице?",
        },
        options: [
          { en: "As many as needed", ru: "Сколько угодно" },
          { en: "Exactly one", ru: "Ровно один" },
          { en: "Up to three", ru: "До трёх" },
          { en: "None — it is not a real element", ru: "Ни одного — такого элемента нет" },
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
          en: "The <article> element should only be used for blog posts and news articles.",
          ru: "Элемент <article> следует использовать только для статей блогов и новостей.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each semantic element with its typical content.",
          ru: "Сопоставьте каждый семантический элемент с его типичным содержимым.",
        },
        pairs: [
          {
            term: { en: "<header>", ru: "<header>" },
            definition: { en: "Site logo, title, and top navigation", ru: "Логотип сайта, заголовок и верхняя навигация" },
          },
          {
            term: { en: "<aside>", ru: "<aside>" },
            definition: { en: "Sidebar or supplementary content", ru: "Боковая панель или дополнительный контент" },
          },
          {
            term: { en: "<footer>", ru: "<footer>" },
            definition: { en: "Copyright, links, and contact info at the bottom", ru: "Копирайт, ссылки и контакты внизу страницы" },
          },
          {
            term: { en: "<figure>", ru: "<figure>" },
            definition: { en: "Self-contained image or diagram with a caption", ru: "Самостоятельное изображение или диаграмма с подписью" },
          },
          {
            term: { en: "<nav>", ru: "<nav>" },
            definition: { en: "Block of navigation links", ru: "Блок навигационных ссылок" },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Complete the sentences about semantic HTML.",
          ru: "Заполните предложения о семантическом HTML.",
        },
        blanks: [
          {
            text: {
              en: "The ___ element is used for self-contained content like blog posts or product cards.",
              ru: "Элемент ___ используется для самостоятельного контента, такого как статьи или карточки товаров.",
            },
            options: [
              { en: "<article>", ru: "<article>" },
              { en: "<section>", ru: "<section>" },
              { en: "<div>", ru: "<div>" },
              { en: "<main>", ru: "<main>" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "A ___ element groups thematic content and should generally include a heading.",
              ru: "Элемент ___ группирует тематический контент и обычно должен содержать заголовок.",
            },
            options: [
              { en: "<section>", ru: "<section>" },
              { en: "<article>", ru: "<article>" },
              { en: "<aside>", ru: "<aside>" },
              { en: "<span>", ru: "<span>" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ element provides a caption for a <figure>.",
              ru: "Элемент ___ задаёт подпись для <figure>.",
            },
            options: [
              { en: "<figcaption>", ru: "<figcaption>" },
              { en: "<caption>", ru: "<caption>" },
              { en: "<label>", ru: "<label>" },
              { en: "<summary>", ru: "<summary>" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the typical page layout elements from top to bottom.",
          ru: "Расположите типичные элементы разметки страницы сверху вниз.",
        },
        items: [
          { en: "<header>", ru: "<header>" },
          { en: "<nav>", ru: "<nav>" },
          { en: "<main>", ru: "<main>" },
          { en: "<aside> (inside or next to main)", ru: "<aside> (внутри или рядом с main)" },
          { en: "<footer>", ru: "<footer>" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange these lines to build a semantic page structure.",
          ru: "Расположите строки для создания семантической структуры страницы.",
        },
        items: [
          { en: "<header>", ru: "<header>" },
          { en: "  <nav><a href=\"/\">Home</a></nav>", ru: "  <nav><a href=\"/\">Главная</a></nav>" },
          { en: "</header>", ru: "</header>" },
          { en: "<main>", ru: "<main>" },
          { en: "  <article><h2>Post Title</h2><p>Content...</p></article>", ru: "  <article><h2>Заголовок статьи</h2><p>Содержание...</p></article>" },
          { en: "</main>", ru: "</main>" },
          { en: "<footer><p>&copy; 2026</p></footer>", ru: "<footer><p>&copy; 2026</p></footer>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What attribute on the <time> element provides a machine-readable date format?",
          ru: "Какой атрибут элемента <time> предоставляет машинночитаемый формат даты?",
        },
        correctText: { en: "datetime", ru: "datetime" },
      },
      {
        type: "flash_cards",
        question: { en: "Review key terms.", ru: "Повторите ключевые термины." },
        pairs: [
          {
            term: { en: "<header>", ru: "<header>" },
            definition: { en: "Introductory content or navigational aids for a page or section", ru: "Вводный контент или навигационные элементы страницы или секции" },
          },
          {
            term: { en: "<main>", ru: "<main>" },
            definition: { en: "The dominant content unique to the page, only one allowed", ru: "Основное содержимое, уникальное для страницы, допускается только один" },
          },
          {
            term: { en: "<article>", ru: "<article>" },
            definition: { en: "Self-contained content that can stand alone", ru: "Самостоятельный контент, имеющий смысл вне контекста" },
          },
          {
            term: { en: "<section>", ru: "<section>" },
            definition: { en: "Thematic grouping of content, typically with a heading", ru: "Тематическая группировка контента, обычно с заголовком" },
          },
          {
            term: { en: "<figure>", ru: "<figure>" },
            definition: { en: "Self-contained content like images or diagrams with an optional caption", ru: "Самостоятельный контент (изображения, диаграммы) с необязательной подписью" },
          },
        ],
      },
    ],
  },

  "fe-4-1": {
    id: "fe-4-1",
    title: { en: "ARIA & Accessibility", ru: "ARIA и доступность" },
    slides: [
      {
        title: { en: "Web Accessibility Fundamentals", ru: "Основы веб-доступности" },
        content: {
          en: "Web accessibility (often abbreviated as a11y) means designing websites that everyone can use, including people with visual, motor, auditory, or cognitive disabilities. The Web Content Accessibility Guidelines (WCAG) define four principles: Perceivable (content must be presentable to users), Operable (UI must be navigable via keyboard), Understandable (content must be readable and predictable), and Robust (content must work with assistive technologies). Key practices include: always adding `alt` text to images, ensuring sufficient color contrast (at least 4.5:1 for normal text), using semantic HTML, and making all functionality available via keyboard.",
          ru: "Веб-доступность (часто сокращается как a11y) означает создание сайтов, которыми может пользоваться каждый, включая людей с нарушениями зрения, моторики, слуха или когнитивных функций. Руководство по доступности веб-контента (WCAG) определяет четыре принципа: Воспринимаемость (контент должен быть представлен пользователям), Управляемость (интерфейс должен быть доступен с клавиатуры), Понятность (контент должен быть читаемым и предсказуемым) и Надёжность (контент должен работать с вспомогательными технологиями). Ключевые практики: всегда добавляйте `alt` к изображениям, обеспечивайте достаточную контрастность цветов (минимум 4.5:1 для обычного текста), используйте семантический HTML и делайте весь функционал доступным с клавиатуры.",
        },
        code: {
          language: "html",
          code: `<!-- Good: descriptive alt text -->
<img src="logo.png" alt="PathMind company logo">

<!-- Good: decorative image with empty alt -->
<img src="divider.png" alt="">

<!-- Good: keyboard-accessible button -->
<button onclick="save()">Save Changes</button>

<!-- Bad: div as button (not keyboard accessible) -->
<div onclick="save()">Save Changes</div>`,
        },
      },
      {
        title: { en: "ARIA Roles and Attributes", ru: "ARIA-роли и атрибуты" },
        content: {
          en: "ARIA (Accessible Rich Internet Applications) is a set of attributes that enhance accessibility when native HTML semantics are not enough. ARIA has three main categories: Roles define what an element is (e.g., `role=\"button\"`, `role=\"dialog\"`, `role=\"alert\"`). States describe the current condition (e.g., `aria-expanded=\"true\"`, `aria-checked=\"false\"`). Properties provide extra information (e.g., `aria-label`, `aria-describedby`, `aria-required`). The first rule of ARIA: do not use ARIA if a native HTML element already provides the semantics you need. For example, use <button> instead of <div role=\"button\">. ARIA does not change behavior — it only changes what assistive technologies announce.",
          ru: "ARIA (Accessible Rich Internet Applications) — набор атрибутов, улучшающих доступность, когда встроенной семантики HTML недостаточно. ARIA имеет три категории: Роли определяют, чем является элемент (например, `role=\"button\"`, `role=\"dialog\"`, `role=\"alert\"`). Состояния описывают текущее положение (например, `aria-expanded=\"true\"`, `aria-checked=\"false\"`). Свойства предоставляют дополнительную информацию (например, `aria-label`, `aria-describedby`, `aria-required`). Первое правило ARIA: не используйте ARIA, если нативный HTML-элемент уже предоставляет нужную семантику. Например, используйте <button> вместо <div role=\"button\">. ARIA не меняет поведение — она лишь меняет то, что озвучивают вспомогательные технологии.",
        },
        code: {
          language: "html",
          code: `<!-- ARIA label for icon-only button -->
<button aria-label="Close menu">
  <svg><!-- X icon --></svg>
</button>

<!-- Expandable section -->
<button aria-expanded="false" aria-controls="details">
  Show Details
</button>
<div id="details" hidden>
  <p>Extra information here.</p>
</div>

<!-- Live region for dynamic updates -->
<div role="alert" aria-live="polite">
  Form submitted successfully!
</div>`,
        },
      },
      {
        title: { en: "Keyboard Navigation and Screen Readers", ru: "Клавиатурная навигация и скринридеры" },
        content: {
          en: "Many users navigate entirely with a keyboard using Tab to move between interactive elements, Enter or Space to activate them, and Escape to close dialogs. Ensure all interactive elements are focusable: native <button>, <a>, and <input> elements are focusable by default. Use `tabindex=\"0\"` to make custom elements focusable, and `tabindex=\"-1\"` for elements that should only be focused programmatically. Never use positive tabindex values as they create confusing tab order. For screen readers, use `aria-label` to provide accessible names for elements without visible text, `aria-describedby` to link to a longer description, and `aria-hidden=\"true\"` to hide decorative elements from assistive technology. Always test your site with a screen reader — VoiceOver on macOS or NVDA on Windows.",
          ru: "Многие пользователи навигируют только с клавиатуры: Tab для перемещения между интерактивными элементами, Enter или Space для активации, Escape для закрытия диалогов. Убедитесь, что все интерактивные элементы фокусируемы: нативные <button>, <a> и <input> фокусируемы по умолчанию. Используйте `tabindex=\"0\"` для фокусировки пользовательских элементов и `tabindex=\"-1\"` для элементов, фокусируемых только программно. Никогда не используйте положительные значения tabindex — они создают запутанный порядок перехода. Для скринридеров используйте `aria-label` для доступных имён элементов без видимого текста, `aria-describedby` для ссылки на подробное описание и `aria-hidden=\"true\"` для скрытия декоративных элементов от вспомогательных технологий. Всегда тестируйте сайт со скринридером — VoiceOver на macOS или NVDA на Windows.",
        },
        code: {
          language: "html",
          code: `<!-- Custom focusable element -->
<div role="button" tabindex="0"
     onkeydown="if(event.key==='Enter') toggle()">
  Toggle Panel
</div>

<!-- Skip navigation link -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<!-- Hiding decorative content -->
<span aria-hidden="true">★★★</span>
<span class="sr-only">3 out of 5 stars</span>

<!-- Describing an input -->
<input type="password" aria-describedby="pw-hint">
<p id="pw-hint">Must be at least 8 characters.</p>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What is the first rule of ARIA?",
          ru: "Каково первое правило ARIA?",
        },
        options: [
          { en: "Always add role attributes to every element", ru: "Всегда добавлять атрибуты role к каждому элементу" },
          { en: "Do not use ARIA if a native HTML element provides the needed semantics", ru: "Не использовать ARIA, если нативный HTML-элемент уже предоставляет нужную семантику" },
          { en: "ARIA attributes must come before other attributes", ru: "Атрибуты ARIA должны стоять перед другими атрибутами" },
          { en: "Every page must have at least 5 ARIA attributes", ru: "На каждой странице должно быть минимум 5 ARIA-атрибутов" },
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
          en: "Adding role=\"button\" to a <div> automatically makes it keyboard-focusable and clickable with Enter.",
          ru: "Добавление role=\"button\" к <div> автоматически делает его фокусируемым с клавиатуры и активируемым по Enter.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each ARIA attribute with its purpose.",
          ru: "Сопоставьте каждый ARIA-атрибут с его назначением.",
        },
        pairs: [
          {
            term: { en: "aria-label", ru: "aria-label" },
            definition: { en: "Provides an accessible name for an element", ru: "Задаёт доступное имя для элемента" },
          },
          {
            term: { en: "aria-hidden", ru: "aria-hidden" },
            definition: { en: "Hides an element from assistive technology", ru: "Скрывает элемент от вспомогательных технологий" },
          },
          {
            term: { en: "aria-expanded", ru: "aria-expanded" },
            definition: { en: "Indicates whether a collapsible section is open or closed", ru: "Указывает, раскрыта или свёрнута сворачиваемая секция" },
          },
          {
            term: { en: "aria-describedby", ru: "aria-describedby" },
            definition: { en: "Links to an element that provides a longer description", ru: "Ссылается на элемент с подробным описанием" },
          },
          {
            term: { en: "aria-live", ru: "aria-live" },
            definition: { en: "Announces dynamic content changes to screen readers", ru: "Озвучивает изменения динамического контента для скринридеров" },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Complete the accessibility statements.",
          ru: "Заполните утверждения о доступности.",
        },
        blanks: [
          {
            text: {
              en: "To make a custom element focusable via Tab, add ___=\"0\".",
              ru: "Чтобы сделать пользовательский элемент фокусируемым через Tab, добавьте ___=\"0\".",
            },
            options: [
              { en: "tabindex", ru: "tabindex" },
              { en: "focusable", ru: "focusable" },
              { en: "role", ru: "role" },
              { en: "aria-focus", ru: "aria-focus" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The minimum color contrast ratio for normal text under WCAG AA is ___.",
              ru: "Минимальный коэффициент контрастности для обычного текста по WCAG AA составляет ___.",
            },
            options: [
              { en: "4.5:1", ru: "4.5:1" },
              { en: "3:1", ru: "3:1" },
              { en: "2:1", ru: "2:1" },
              { en: "7:1", ru: "7:1" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "Images that are purely decorative should have an ___ attribute set to an empty string.",
              ru: "У чисто декоративных изображений атрибут ___ должен быть пустой строкой.",
            },
            options: [
              { en: "alt", ru: "alt" },
              { en: "title", ru: "title" },
              { en: "aria-label", ru: "aria-label" },
              { en: "role", ru: "role" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the steps to make an interactive widget accessible, from first to last.",
          ru: "Расположите шаги по обеспечению доступности интерактивного виджета от первого к последнему.",
        },
        items: [
          { en: "Use a native HTML element if possible (e.g., <button>)", ru: "Используйте нативный HTML-элемент, если возможно (например, <button>)" },
          { en: "Add an appropriate ARIA role if a native element is not suitable", ru: "Добавьте подходящую ARIA-роль, если нативный элемент не подходит" },
          { en: "Make the element focusable with tabindex=\"0\"", ru: "Сделайте элемент фокусируемым через tabindex=\"0\"" },
          { en: "Add keyboard event handlers (Enter, Space, Escape)", ru: "Добавьте обработчики клавиатурных событий (Enter, Space, Escape)" },
          { en: "Add ARIA states (aria-expanded, aria-pressed) and update them dynamically", ru: "Добавьте ARIA-состояния (aria-expanded, aria-pressed) и обновляйте их динамически" },
          { en: "Test with a screen reader and keyboard-only navigation", ru: "Протестируйте со скринридером и навигацией только с клавиатуры" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange these lines to create an accessible modal dialog.",
          ru: "Расположите строки для создания доступного модального диалога.",
        },
        items: [
          { en: "<div role=\"dialog\" aria-labelledby=\"dialog-title\" aria-modal=\"true\">", ru: "<div role=\"dialog\" aria-labelledby=\"dialog-title\" aria-modal=\"true\">" },
          { en: "  <h2 id=\"dialog-title\">Confirm Action</h2>", ru: "  <h2 id=\"dialog-title\">Подтверждение действия</h2>" },
          { en: "  <p>Are you sure you want to proceed?</p>", ru: "  <p>Вы уверены, что хотите продолжить?</p>" },
          { en: "  <button autofocus>Yes, continue</button>", ru: "  <button autofocus>Да, продолжить</button>" },
          { en: "  <button aria-label=\"Close dialog\">Cancel</button>", ru: "  <button aria-label=\"Закрыть диалог\">Отмена</button>" },
          { en: "</div>", ru: "</div>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What ARIA attribute would you use to provide an accessible name for an icon-only button?",
          ru: "Какой ARIA-атрибут вы используете для задания доступного имени кнопке, содержащей только иконку?",
        },
        correctText: { en: "aria-label", ru: "aria-label" },
      },
      {
        type: "flash_cards",
        question: { en: "Review key terms.", ru: "Повторите ключевые термины." },
        pairs: [
          {
            term: { en: "ARIA", ru: "ARIA" },
            definition: { en: "Accessible Rich Internet Applications — attributes that enhance accessibility for assistive technologies", ru: "Accessible Rich Internet Applications — атрибуты, улучшающие доступность для вспомогательных технологий" },
          },
          {
            term: { en: "tabindex", ru: "tabindex" },
            definition: { en: "Controls whether and in what order an element receives keyboard focus", ru: "Управляет тем, получает ли элемент фокус с клавиатуры и в каком порядке" },
          },
          {
            term: { en: "alt text", ru: "alt-текст" },
            definition: { en: "Alternative text description for images, read by screen readers", ru: "Альтернативный текстовый описатель изображения, озвучиваемый скринридерами" },
          },
          {
            term: { en: "WCAG", ru: "WCAG" },
            definition: { en: "Web Content Accessibility Guidelines — the international standard for web accessibility", ru: "Web Content Accessibility Guidelines — международный стандарт веб-доступности" },
          },
          {
            term: { en: "Screen reader", ru: "Скринридер" },
            definition: { en: "Software that reads page content aloud for visually impaired users", ru: "Программа, озвучивающая содержимое страницы для пользователей с нарушениями зрения" },
          },
        ],
      },
    ],
  },
};
