import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_LESSONS_V2: Record<string, LessonContentV2> = {
  "fe-1-1": {
    id: "fe-1-1",
    title: {
      en: "HTML Document Structure",
      ru: "Структура HTML-документа",
    },
    slides: [
      {
        title: {
          en: "What is an HTML Document?",
          ru: "Что такое HTML-документ?",
        },
        content: {
          en: "HTML (HyperText Markup Language) is the standard language for creating web pages. Every HTML page starts with a DOCTYPE declaration that tells the browser which version of HTML is being used. Modern pages use <!DOCTYPE html> which declares HTML5.",
          ru: "HTML (язык гипертекстовой разметки) — стандартный язык для создания веб-страниц. Каждая HTML-страница начинается с объявления DOCTYPE, которое сообщает браузеру версию используемого HTML. Современные страницы используют <!DOCTYPE html>, что означает HTML5.",
        },
        code: {
          language: "html",
          code: `<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8">\n    <title>My Page</title>\n  </head>\n  <body>\n    <p>Hello, World!</p>\n  </body>\n</html>`,
        },
      },
      {
        title: {
          en: "The <head> Element",
          ru: "Элемент <head>",
        },
        content: {
          en: "The <head> element contains metadata about the document — information that is not displayed on the page itself. This includes the page title (shown in the browser tab), character encoding, viewport settings for mobile, and links to stylesheets or scripts.",
          ru: "Элемент <head> содержит метаданные о документе — информацию, которая не отображается на странице. Сюда входят заголовок страницы (отображается во вкладке браузера), кодировка символов, настройки области просмотра для мобильных устройств, а также ссылки на стили и скрипты.",
        },
        code: {
          language: "html",
          code: `<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="A beginner HTML page">\n  <title>My First Page</title>\n</head>`,
        },
      },
      {
        title: {
          en: "The <body> Element",
          ru: "Элемент <body>",
        },
        content: {
          en: "The <body> element holds all visible content of the web page — text, images, links, buttons, and everything users see and interact with. There is only one <body> per page. All the HTML tags that create visible content go inside <body>.",
          ru: "Элемент <body> содержит весь видимый контент веб-страницы — текст, изображения, ссылки, кнопки и всё, что пользователи видят и с чем взаимодействуют. На странице только один <body>. Все HTML-теги, создающие видимый контент, размещаются внутри <body>.",
        },
        code: {
          language: "html",
          code: `<body>\n  <h1>Welcome to My Site</h1>\n  <p>This text is visible to visitors.</p>\n</body>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which declaration must appear at the very beginning of an HTML5 document?",
          ru: "Какое объявление должно стоять в самом начале HTML5-документа?",
        },
        options: [
          { en: "<!DOCTYPE html>", ru: "<!DOCTYPE html>" },
          { en: "<html>", ru: "<html>" },
          { en: "<head>", ru: "<head>" },
          { en: "<!-- HTML5 -->", ru: "<!-- HTML5 -->" },
        ],
        correct: 0,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "The <head> element contains content that is directly visible to users on the page.",
          ru: "Элемент <head> содержит контент, который напрямую виден пользователям на странице.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each HTML element or attribute to its purpose.",
          ru: "Сопоставьте каждый HTML-элемент или атрибут с его назначением.",
        },
        pairs: [
          {
            term: { en: "<!DOCTYPE html>", ru: "<!DOCTYPE html>" },
            definition: {
              en: "Declares the document type as HTML5",
              ru: "Объявляет тип документа HTML5",
            },
          },
          {
            term: { en: "<html>", ru: "<html>" },
            definition: {
              en: "The root element that wraps the entire page",
              ru: "Корневой элемент, охватывающий всю страницу",
            },
          },
          {
            term: { en: "<head>", ru: "<head>" },
            definition: {
              en: "Contains metadata not shown on the page",
              ru: "Содержит метаданные, не отображаемые на странице",
            },
          },
          {
            term: { en: "<body>", ru: "<body>" },
            definition: {
              en: "Holds all visible content of the page",
              ru: "Содержит весь видимый контент страницы",
            },
          },
          {
            term: { en: "<title>", ru: "<title>" },
            definition: {
              en: "Sets the text shown in the browser tab",
              ru: "Устанавливает текст, отображаемый во вкладке браузера",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks to complete the HTML document skeleton.",
          ru: "Заполните пропуски, чтобы завершить скелет HTML-документа.",
        },
        blanks: [
          {
            text: {
              en: "The first line of an HTML5 file should be ___.",
              ru: "Первой строкой HTML5-файла должна быть ___.",
            },
            options: [
              { en: "<!DOCTYPE html>", ru: "<!DOCTYPE html>" },
              { en: "<html5>", ru: "<html5>" },
              { en: "<start>", ru: "<start>" },
              { en: "<!-- begin -->", ru: "<!-- begin -->" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ element contains the page title and meta tags.",
              ru: "Элемент ___ содержит заголовок страницы и мета-теги.",
            },
            options: [
              { en: "<body>", ru: "<body>" },
              { en: "<header>", ru: "<header>" },
              { en: "<head>", ru: "<head>" },
              { en: "<meta>", ru: "<meta>" },
            ],
            correctIndex: 2,
          },
          {
            text: {
              en: "Visible page content belongs inside the ___ element.",
              ru: "Видимый контент страницы размещается внутри элемента ___.",
            },
            options: [
              { en: "<body>", ru: "<body>" },
              { en: "<main>", ru: "<main>" },
              { en: "<content>", ru: "<content>" },
              { en: "<visible>", ru: "<visible>" },
            ],
            correctIndex: 0,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange the parts of an HTML document in the correct top-to-bottom order.",
          ru: "Расположите части HTML-документа в правильном порядке сверху вниз.",
        },
        items: [
          { en: "<!DOCTYPE html>", ru: "<!DOCTYPE html>" },
          { en: "<html lang=\"en\">", ru: "<html lang=\"en\">" },
          { en: "<head> ... </head>", ru: "<head> ... </head>" },
          { en: "<body> ... </body>", ru: "<body> ... </body>" },
          { en: "</html>", ru: "</html>" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Put these lines in order to form a valid minimal HTML5 page.",
          ru: "Упорядочьте строки, чтобы получить корректную минимальную HTML5-страницу.",
        },
        items: [
          { en: "<!DOCTYPE html>", ru: "<!DOCTYPE html>" },
          { en: "<html>", ru: "<html>" },
          { en: "<head><title>Page</title></head>", ru: "<head><title>Page</title></head>" },
          { en: "<body>", ru: "<body>" },
          { en: "<p>Hello</p>", ru: "<p>Привет</p>" },
          { en: "</body>", ru: "</body>" },
          { en: "</html>", ru: "</html>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What tag is used to set the character encoding of an HTML document? (write the tag name only, e.g. meta)",
          ru: "Какой тег используется для установки кодировки символов HTML-документа? (напишите только имя тега, например meta)",
        },
        correctText: { en: "meta", ru: "meta" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review these key HTML document terms.",
          ru: "Повторите ключевые термины структуры HTML-документа.",
        },
        pairs: [
          {
            term: { en: "DOCTYPE", ru: "DOCTYPE" },
            definition: {
              en: "A declaration that defines the HTML version being used",
              ru: "Объявление, определяющее используемую версию HTML",
            },
          },
          {
            term: { en: "Metadata", ru: "Метаданные" },
            definition: {
              en: "Data about the page (charset, viewport, description) stored in <head>",
              ru: "Данные о странице (кодировка, область просмотра, описание), хранящиеся в <head>",
            },
          },
          {
            term: { en: "charset", ru: "charset" },
            definition: {
              en: "Attribute of <meta> that specifies character encoding (usually UTF-8)",
              ru: "Атрибут тега <meta>, задающий кодировку символов (обычно UTF-8)",
            },
          },
          {
            term: { en: "viewport", ru: "область просмотра" },
            definition: {
              en: "The visible area of a web page on a device screen",
              ru: "Видимая область веб-страницы на экране устройства",
            },
          },
          {
            term: { en: "lang attribute", ru: "атрибут lang" },
            definition: {
              en: "Specifies the language of the page content, e.g. lang=\"en\"",
              ru: "Указывает язык содержимого страницы, например lang=\"ru\"",
            },
          },
        ],
      },
      {
        type: "quiz",
        question: {
          en: "Which meta tag is used to make a page display correctly on mobile devices?",
          ru: "Какой мета-тег используется для корректного отображения страницы на мобильных устройствах?",
        },
        options: [
          {
            en: "<meta name=\"mobile\" content=\"true\">",
            ru: "<meta name=\"mobile\" content=\"true\">",
          },
          {
            en: "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
            ru: "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
          },
          {
            en: "<meta name=\"screen\" content=\"responsive\">",
            ru: "<meta name=\"screen\" content=\"responsive\">",
          },
          {
            en: "<meta name=\"device\" content=\"width=device-width\">",
            ru: "<meta name=\"device\" content=\"width=device-width\">",
          },
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
          en: "A valid HTML document can have more than one <body> element.",
          ru: "Валидный HTML-документ может содержать более одного элемента <body>.",
        },
        answer: false,
      },
    ],
  },

  "fe-1-2": {
    id: "fe-1-2",
    title: {
      en: "Common HTML Tags",
      ru: "Часто используемые HTML-теги",
    },
    slides: [
      {
        title: {
          en: "Headings and Paragraphs",
          ru: "Заголовки и абзацы",
        },
        content: {
          en: "HTML provides six levels of headings: <h1> through <h6>. <h1> is the most important (largest) and <h6> the least important (smallest). There should normally be only one <h1> per page. The <p> tag defines a paragraph of text and automatically adds spacing around it.",
          ru: "HTML предоставляет шесть уровней заголовков: от <h1> до <h6>. <h1> — самый важный (наибольший), <h6> — наименее важный (наименьший). Обычно на странице должен быть только один <h1>. Тег <p> определяет абзац текста и автоматически добавляет отступы вокруг него.",
        },
        code: {
          language: "html",
          code: `<h1>Main Page Title</h1>\n<h2>Section Title</h2>\n<h3>Subsection Title</h3>\n<p>This is a paragraph of text.</p>\n<p>This is another paragraph.</p>`,
        },
      },
      {
        title: {
          en: "Links and Images",
          ru: "Ссылки и изображения",
        },
        content: {
          en: "The <a> (anchor) tag creates hyperlinks. The href attribute specifies the URL destination. Adding target=\"_blank\" opens the link in a new tab. The <img> tag embeds images. It requires a src attribute (image URL) and an alt attribute (text description for accessibility).",
          ru: "Тег <a> (якорь) создаёт гиперссылки. Атрибут href задаёт URL-адрес назначения. Добавление target=\"_blank\" открывает ссылку в новой вкладке. Тег <img> вставляет изображения. Он требует атрибута src (URL изображения) и alt (текстовое описание для доступности).",
        },
        code: {
          language: "html",
          code: `<a href="https://example.com">Visit Example</a>\n<a href="about.html" target="_blank">Open About</a>\n\n<img src="photo.jpg" alt="A scenic photo">\n<img src="logo.png" alt="Company logo" width="200">`,
        },
      },
      {
        title: {
          en: "Lists",
          ru: "Списки",
        },
        content: {
          en: "HTML has two main list types. <ul> (unordered list) creates a bulleted list, while <ol> (ordered list) creates a numbered list. Both use <li> (list item) tags for each entry. Lists can be nested inside each other to create multi-level structures.",
          ru: "В HTML есть два основных типа списков. <ul> (неупорядоченный список) создаёт маркированный список, а <ol> (упорядоченный список) — нумерованный. Оба используют теги <li> (элемент списка) для каждого пункта. Списки можно вкладывать друг в друга для создания многоуровневых структур.",
        },
        code: {
          language: "html",
          code: `<ul>\n  <li>Apples</li>\n  <li>Bananas</li>\n  <li>Cherries</li>\n</ul>\n\n<ol>\n  <li>Boil water</li>\n  <li>Add pasta</li>\n  <li>Cook 10 minutes</li>\n</ol>`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which tag creates the most important (largest) heading on a page?",
          ru: "Какой тег создаёт самый важный (наибольший) заголовок на странице?",
        },
        options: [
          { en: "<heading>", ru: "<heading>" },
          { en: "<h6>", ru: "<h6>" },
          { en: "<h1>", ru: "<h1>" },
          { en: "<title>", ru: "<title>" },
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
          en: "The <img> tag requires both a src attribute and an alt attribute for proper use.",
          ru: "Тег <img> для корректного использования требует наличия атрибутов src и alt.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each HTML tag to what it creates.",
          ru: "Сопоставьте каждый HTML-тег с тем, что он создаёт.",
        },
        pairs: [
          {
            term: { en: "<p>", ru: "<p>" },
            definition: {
              en: "A paragraph of text",
              ru: "Абзац текста",
            },
          },
          {
            term: { en: "<a>", ru: "<a>" },
            definition: {
              en: "A clickable hyperlink",
              ru: "Кликабельная гиперссылка",
            },
          },
          {
            term: { en: "<img>", ru: "<img>" },
            definition: {
              en: "An embedded image",
              ru: "Встроенное изображение",
            },
          },
          {
            term: { en: "<ul>", ru: "<ul>" },
            definition: {
              en: "An unordered (bulleted) list",
              ru: "Неупорядоченный (маркированный) список",
            },
          },
          {
            term: { en: "<ol>", ru: "<ol>" },
            definition: {
              en: "An ordered (numbered) list",
              ru: "Упорядоченный (нумерованный) список",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks to complete the HTML snippets.",
          ru: "Заполните пропуски в HTML-фрагментах.",
        },
        blanks: [
          {
            text: {
              en: "To create a link you use the ___ tag.",
              ru: "Для создания ссылки используется тег ___.",
            },
            options: [
              { en: "<link>", ru: "<link>" },
              { en: "<a>", ru: "<a>" },
              { en: "<href>", ru: "<href>" },
              { en: "<url>", ru: "<url>" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "The ___ attribute of <img> provides a text description for screen readers.",
              ru: "Атрибут ___ тега <img> предоставляет текстовое описание для программ чтения с экрана.",
            },
            options: [
              { en: "title", ru: "title" },
              { en: "src", ru: "src" },
              { en: "alt", ru: "alt" },
              { en: "desc", ru: "desc" },
            ],
            correctIndex: 2,
          },
          {
            text: {
              en: "List items inside both <ul> and <ol> are wrapped in ___ tags.",
              ru: "Элементы списка внутри <ul> и <ol> оборачиваются в теги ___.",
            },
            options: [
              { en: "<item>", ru: "<item>" },
              { en: "<list>", ru: "<list>" },
              { en: "<dt>", ru: "<dt>" },
              { en: "<li>", ru: "<li>" },
            ],
            correctIndex: 3,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Arrange these heading tags from most important to least important.",
          ru: "Расположите теги заголовков от самого важного к наименее важному.",
        },
        items: [
          { en: "<h1>", ru: "<h1>" },
          { en: "<h2>", ru: "<h2>" },
          { en: "<h3>", ru: "<h3>" },
          { en: "<h4>", ru: "<h4>" },
          { en: "<h5>", ru: "<h5>" },
          { en: "<h6>", ru: "<h6>" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Put these lines in order to create a valid unordered list with three items.",
          ru: "Упорядочьте строки, чтобы создать корректный неупорядоченный список из трёх элементов.",
        },
        items: [
          { en: "<ul>", ru: "<ul>" },
          { en: "  <li>HTML</li>", ru: "  <li>HTML</li>" },
          { en: "  <li>CSS</li>", ru: "  <li>CSS</li>" },
          { en: "  <li>JavaScript</li>", ru: "  <li>JavaScript</li>" },
          { en: "</ul>", ru: "</ul>" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What attribute of the <a> tag specifies the URL that the link goes to? (write the attribute name only)",
          ru: "Какой атрибут тега <a> указывает URL-адрес, на который ведёт ссылка? (напишите только название атрибута)",
        },
        correctText: { en: "href", ru: "href" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review these common HTML tag terms.",
          ru: "Повторите термины часто используемых HTML-тегов.",
        },
        pairs: [
          {
            term: { en: "Anchor tag <a>", ru: "Тег якоря <a>" },
            definition: {
              en: "Creates hyperlinks; uses href to set the destination URL",
              ru: "Создаёт гиперссылки; использует href для задания URL-адреса назначения",
            },
          },
          {
            term: { en: "src attribute", ru: "Атрибут src" },
            definition: {
              en: "Specifies the file path or URL of an image in <img>",
              ru: "Указывает путь к файлу или URL изображения в теге <img>",
            },
          },
          {
            term: { en: "target=\"_blank\"", ru: "target=\"_blank\"" },
            definition: {
              en: "Opens a link in a new browser tab or window",
              ru: "Открывает ссылку в новой вкладке или окне браузера",
            },
          },
          {
            term: { en: "<li>", ru: "<li>" },
            definition: {
              en: "List item tag used inside <ul> or <ol>",
              ru: "Тег элемента списка, используемый внутри <ul> или <ol>",
            },
          },
          {
            term: { en: "Nesting", ru: "Вложение" },
            definition: {
              en: "Placing HTML elements inside other elements to create structure",
              ru: "Размещение HTML-элементов внутри других элементов для создания структуры",
            },
          },
        ],
      },
      {
        type: "quiz",
        question: {
          en: "Which tag would you use to create a numbered step-by-step list?",
          ru: "Какой тег использовать для создания нумерованного пошагового списка?",
        },
        options: [
          { en: "<ul>", ru: "<ul>" },
          { en: "<nl>", ru: "<nl>" },
          { en: "<list type=\"number\">", ru: "<list type=\"number\">" },
          { en: "<ol>", ru: "<ol>" },
        ],
        correct: 3,
      },
      {
        type: "true_false",
        question: {
          en: "Is the following statement true or false?",
          ru: "Верно ли следующее утверждение?",
        },
        statement: {
          en: "It is best practice to have multiple <h1> tags on a single web page.",
          ru: "Рекомендуется использовать несколько тегов <h1> на одной веб-странице.",
        },
        answer: false,
      },
    ],
  },
};
