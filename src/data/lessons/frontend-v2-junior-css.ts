import type { LessonContentV2 } from "@/types/lesson";

export const FRONTEND_V2_JUNIOR_CSS: Record<string, LessonContentV2> = {
  // ─── LESSON fe-5-1: Selectors & Box Model ──────────────────────────
  "fe-5-1": {
    id: "fe-5-1",
    title: {
      en: "Selectors & Box Model",
      ru: "Селекторы и блочная модель",
    },
    slides: [
      {
        title: {
          en: "CSS Selectors",
          ru: "CSS-селекторы",
        },
        content: {
          en: "CSS selectors let you target HTML elements to apply styles. The most common selectors are: element selectors (p, h1), class selectors (.card), and ID selectors (#header). You can also combine them — for example, div.container targets only <div> elements with the class 'container'. Descendant selectors like .nav a target all <a> tags inside an element with class 'nav'.",
          ru: "CSS-селекторы позволяют выбирать HTML-элементы для применения стилей. Самые распространённые селекторы: по элементу (p, h1), по классу (.card) и по ID (#header). Их можно комбинировать — например, div.container выберет только <div> с классом 'container'. Селектор потомков .nav a выберет все <a> внутри элемента с классом 'nav'.",
        },
        code: {
          language: "css",
          code: `/* Element selector */\np { color: navy; }\n\n/* Class selector */\n.card { border: 1px solid #ccc; }\n\n/* ID selector */\n#header { background: #f5f5f5; }\n\n/* Descendant selector */\n.nav a { text-decoration: none; }`,
        },
      },
      {
        title: {
          en: "Specificity",
          ru: "Специфичность",
        },
        content: {
          en: "When multiple CSS rules target the same element, specificity determines which one wins. The hierarchy is: inline styles (1000) > ID selectors (100) > class/attribute selectors (10) > element selectors (1). If two rules have equal specificity, the last one in the stylesheet wins. The !important flag overrides all specificity, but should be avoided in most cases.",
          ru: "Когда несколько CSS-правил нацелены на один элемент, специфичность определяет, какое из них применится. Иерархия: инлайн-стили (1000) > ID-селекторы (100) > селекторы класса/атрибута (10) > селекторы элемента (1). При равной специфичности побеждает последнее правило в таблице стилей. Флаг !important перекрывает любую специфичность, но его следует избегать.",
        },
        code: {
          language: "css",
          code: `/* Specificity: 0-0-1 (element) */\np { color: black; }\n\n/* Specificity: 0-1-0 (class) */\n.text { color: blue; }\n\n/* Specificity: 1-0-0 (ID) */\n#intro { color: red; }\n\n/* This <p class="text" id="intro"> will be red */`,
        },
      },
      {
        title: {
          en: "The Box Model",
          ru: "Блочная модель",
        },
        content: {
          en: "Every HTML element is a rectangular box. The CSS box model has four layers from inside out: content (the actual text or image), padding (space between content and border), border (the outline around the padding), and margin (space outside the border). By default, width and height apply only to the content area. Using box-sizing: border-box makes width and height include padding and border, which is much easier to work with.",
          ru: "Каждый HTML-элемент — это прямоугольный блок. Блочная модель CSS состоит из четырёх слоёв изнутри наружу: контент (текст или изображение), padding (отступ между контентом и рамкой), border (рамка вокруг padding) и margin (внешний отступ за рамкой). По умолчанию width и height задают только область контента. Свойство box-sizing: border-box включает padding и border в ширину и высоту, что гораздо удобнее.",
        },
        code: {
          language: "css",
          code: `/* Box model example */\n.card {\n  width: 300px;\n  padding: 20px;\n  border: 2px solid #333;\n  margin: 16px;\n  box-sizing: border-box;\n}\n\n/* Universal reset */\n*, *::before, *::after {\n  box-sizing: border-box;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which selector has the HIGHEST specificity?",
          ru: "Какой селектор имеет НАИВЫСШУЮ специфичность?",
        },
        options: [
          { en: "p", ru: "p" },
          { en: ".card", ru: ".card" },
          { en: "#header", ru: "#header" },
          { en: "div p", ru: "div p" },
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
          en: "By default, the CSS width property includes padding and border in its calculation.",
          ru: "По умолчанию свойство CSS width включает padding и border в расчёт.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each box model property to its description.",
          ru: "Сопоставьте каждое свойство блочной модели с его описанием.",
        },
        pairs: [
          {
            term: { en: "margin", ru: "margin" },
            definition: {
              en: "Space outside the border",
              ru: "Пространство за пределами рамки",
            },
          },
          {
            term: { en: "border", ru: "border" },
            definition: {
              en: "The outline around the element",
              ru: "Обводка вокруг элемента",
            },
          },
          {
            term: { en: "padding", ru: "padding" },
            definition: {
              en: "Space between content and border",
              ru: "Пространство между контентом и рамкой",
            },
          },
          {
            term: { en: "content", ru: "content" },
            definition: {
              en: "The actual text or image inside",
              ru: "Непосредственно текст или изображение внутри",
            },
          },
          {
            term: { en: "box-sizing", ru: "box-sizing" },
            definition: {
              en: "Controls how width and height are calculated",
              ru: "Определяет, как рассчитываются ширина и высота",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about CSS selectors and the box model.",
          ru: "Заполните пропуски о CSS-селекторах и блочной модели.",
        },
        blanks: [
          {
            text: {
              en: "A ___ selector starts with a dot and targets elements by their class attribute.",
              ru: "Селектор ___ начинается с точки и выбирает элементы по атрибуту class.",
            },
            options: [
              { en: "class", ru: "класса" },
              { en: "ID", ru: "ID" },
              { en: "element", ru: "элемента" },
              { en: "universal", ru: "универсальный" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The ___ property adds space outside the border of an element.",
              ru: "Свойство ___ добавляет пространство за пределами рамки элемента.",
            },
            options: [
              { en: "padding", ru: "padding" },
              { en: "margin", ru: "margin" },
              { en: "border", ru: "border" },
              { en: "outline", ru: "outline" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "Setting box-sizing to ___ makes width include padding and border.",
              ru: "Установка box-sizing в ___ включает padding и border в ширину.",
            },
            options: [
              { en: "content-box", ru: "content-box" },
              { en: "padding-box", ru: "padding-box" },
              { en: "border-box", ru: "border-box" },
              { en: "margin-box", ru: "margin-box" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the box model layers from innermost to outermost.",
          ru: "Расположите слои блочной модели от внутреннего к внешнему.",
        },
        items: [
          { en: "Content", ru: "Контент" },
          { en: "Padding", ru: "Padding (внутренний отступ)" },
          { en: "Border", ru: "Border (рамка)" },
          { en: "Margin", ru: "Margin (внешний отступ)" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS lines to style a card with padding, border, margin, and border-box sizing.",
          ru: "Расположите строки CSS, чтобы стилизовать карточку с padding, border, margin и border-box.",
        },
        items: [
          { en: ".card {", ru: ".card {" },
          { en: "  box-sizing: border-box;", ru: "  box-sizing: border-box;" },
          { en: "  width: 320px;", ru: "  width: 320px;" },
          { en: "  padding: 24px;", ru: "  padding: 24px;" },
          { en: "  border: 1px solid #ddd;", ru: "  border: 1px solid #ddd;" },
          { en: "  margin: 16px auto;", ru: "  margin: 16px auto;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS property adds space BETWEEN the content and the border?",
          ru: "Какое CSS-свойство добавляет пространство МЕЖДУ контентом и рамкой?",
        },
        correctText: { en: "padding", ru: "padding" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "Specificity", ru: "Специфичность" },
            definition: {
              en: "A scoring system that determines which CSS rule takes priority",
              ru: "Система оценки, определяющая приоритет CSS-правила",
            },
          },
          {
            term: { en: "Class selector", ru: "Селектор класса" },
            definition: {
              en: "Targets elements by class name, written as .className",
              ru: "Выбирает элементы по имени класса, записывается как .className",
            },
          },
          {
            term: { en: "Box model", ru: "Блочная модель" },
            definition: {
              en: "Content + padding + border + margin around every element",
              ru: "Контент + padding + border + margin вокруг каждого элемента",
            },
          },
          {
            term: { en: "border-box", ru: "border-box" },
            definition: {
              en: "A box-sizing value that includes padding and border in the element's width",
              ru: "Значение box-sizing, включающее padding и border в ширину элемента",
            },
          },
          {
            term: { en: "margin: auto", ru: "margin: auto" },
            definition: {
              en: "Centers a block element horizontally within its container",
              ru: "Центрирует блочный элемент по горизонтали внутри контейнера",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-5-2: Colors & Typography ─────────────────────────────
  "fe-5-2": {
    id: "fe-5-2",
    title: {
      en: "Colors & Typography",
      ru: "Цвета и типографика",
    },
    slides: [
      {
        title: {
          en: "Color Values in CSS",
          ru: "Значения цветов в CSS",
        },
        content: {
          en: "CSS supports multiple color formats. Named colors (red, blue, coral) are the simplest. Hex codes (#ff5733) use six hexadecimal digits for red, green, and blue. RGB — rgb(255, 87, 51) — uses decimal values 0-255. RGBA adds an alpha channel for transparency: rgba(255, 87, 51, 0.5). HSL — hsl(14, 100%, 60%) — uses hue, saturation, and lightness, which is often more intuitive for adjusting colors.",
          ru: "CSS поддерживает несколько форматов цветов. Именованные цвета (red, blue, coral) — самые простые. Hex-коды (#ff5733) используют шесть шестнадцатеричных цифр для красного, зелёного и синего. RGB — rgb(255, 87, 51) — использует десятичные значения 0-255. RGBA добавляет альфа-канал для прозрачности: rgba(255, 87, 51, 0.5). HSL — hsl(14, 100%, 60%) — использует оттенок, насыщенность и светлоту, что часто удобнее при подборе цветов.",
        },
        code: {
          language: "css",
          code: `/* Named color */\nh1 { color: coral; }\n\n/* Hex */\n.accent { color: #ff5733; }\n\n/* RGB & RGBA */\n.overlay { background: rgba(0, 0, 0, 0.5); }\n\n/* HSL */\n.btn { background: hsl(220, 90%, 56%); }`,
        },
      },
      {
        title: {
          en: "Fonts & Google Fonts",
          ru: "Шрифты и Google Fonts",
        },
        content: {
          en: "The font-family property sets the typeface. Always provide a fallback stack: font-family: 'Inter', Arial, sans-serif. Google Fonts is a free library of web fonts — you add a <link> tag in your HTML <head> or an @import in CSS. After including the font, you can use it in font-family. Common font families are serif, sans-serif, and monospace.",
          ru: "Свойство font-family задаёт шрифт. Всегда указывайте запасной стек: font-family: 'Inter', Arial, sans-serif. Google Fonts — бесплатная библиотека веб-шрифтов: подключается через тег <link> в HTML или @import в CSS. После подключения шрифт можно использовать в font-family. Основные семейства шрифтов: serif, sans-serif и monospace.",
        },
        code: {
          language: "css",
          code: `/* Google Fonts import */\n@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');\n\nbody {\n  font-family: 'Inter', Arial, sans-serif;\n  font-size: 16px;\n  line-height: 1.6;\n}`,
        },
      },
      {
        title: {
          en: "Text Properties",
          ru: "Свойства текста",
        },
        content: {
          en: "CSS offers many text properties. font-size sets the size (px, rem, em). font-weight controls boldness (400 = normal, 700 = bold). line-height sets the spacing between lines — a value of 1.5 to 1.6 is comfortable for body text. text-align positions text (left, center, right, justify). text-transform changes capitalization (uppercase, lowercase, capitalize). letter-spacing and word-spacing fine-tune readability.",
          ru: "CSS предлагает множество свойств текста. font-size задаёт размер (px, rem, em). font-weight управляет жирностью (400 = обычный, 700 = жирный). line-height задаёт межстрочный интервал — значение 1.5–1.6 комфортно для основного текста. text-align выравнивает текст (left, center, right, justify). text-transform меняет регистр (uppercase, lowercase, capitalize). letter-spacing и word-spacing настраивают читаемость.",
        },
        code: {
          language: "css",
          code: `.title {\n  font-size: 2rem;\n  font-weight: 700;\n  text-align: center;\n  text-transform: uppercase;\n  letter-spacing: 0.05em;\n}\n\n.body-text {\n  font-size: 1rem;\n  line-height: 1.6;\n  color: #333;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which color format includes an alpha channel for transparency?",
          ru: "Какой формат цвета включает альфа-канал для прозрачности?",
        },
        options: [
          { en: "HEX", ru: "HEX" },
          { en: "RGB", ru: "RGB" },
          { en: "RGBA", ru: "RGBA" },
          { en: "Named colors", ru: "Именованные цвета" },
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
          en: "A font-weight value of 400 represents bold text.",
          ru: "Значение font-weight 400 означает жирный текст.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each CSS text property to what it controls.",
          ru: "Сопоставьте каждое CSS-свойство текста с тем, что оно контролирует.",
        },
        pairs: [
          {
            term: { en: "font-size", ru: "font-size" },
            definition: {
              en: "Sets the size of the text",
              ru: "Устанавливает размер текста",
            },
          },
          {
            term: { en: "line-height", ru: "line-height" },
            definition: {
              en: "Controls spacing between text lines",
              ru: "Управляет межстрочным интервалом",
            },
          },
          {
            term: { en: "text-transform", ru: "text-transform" },
            definition: {
              en: "Changes text capitalization",
              ru: "Меняет регистр текста",
            },
          },
          {
            term: { en: "letter-spacing", ru: "letter-spacing" },
            definition: {
              en: "Adjusts space between characters",
              ru: "Регулирует расстояние между символами",
            },
          },
          {
            term: { en: "text-align", ru: "text-align" },
            definition: {
              en: "Sets horizontal alignment of text",
              ru: "Задаёт горизонтальное выравнивание текста",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about colors and typography.",
          ru: "Заполните пропуски о цветах и типографике.",
        },
        blanks: [
          {
            text: {
              en: "The color format hsl() stands for hue, saturation, and ___.",
              ru: "Формат цвета hsl() означает оттенок, насыщенность и ___.",
            },
            options: [
              { en: "lightness", ru: "светлота" },
              { en: "luminance", ru: "яркость" },
              { en: "level", ru: "уровень" },
              { en: "length", ru: "длина" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The property ___ specifies which typeface to use for text.",
              ru: "Свойство ___ указывает, какой шрифт использовать для текста.",
            },
            options: [
              { en: "font-style", ru: "font-style" },
              { en: "font-family", ru: "font-family" },
              { en: "font-weight", ru: "font-weight" },
              { en: "font-size", ru: "font-size" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "A hex color code starts with the ___ symbol.",
              ru: "Hex-код цвета начинается с символа ___.",
            },
            options: [
              { en: "@", ru: "@" },
              { en: ".", ru: "." },
              { en: "#", ru: "#" },
              { en: "$", ru: "$" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order these font-weight values from lightest to heaviest.",
          ru: "Расположите значения font-weight от самого тонкого к самому жирному.",
        },
        items: [
          { en: "100 (Thin)", ru: "100 (Тонкий)" },
          { en: "300 (Light)", ru: "300 (Лёгкий)" },
          { en: "400 (Normal)", ru: "400 (Обычный)" },
          { en: "600 (Semi-bold)", ru: "600 (Полужирный)" },
          { en: "700 (Bold)", ru: "700 (Жирный)" },
          { en: "900 (Black)", ru: "900 (Сверхжирный)" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the lines to import and apply a Google Font.",
          ru: "Расположите строки, чтобы импортировать и применить Google Font.",
        },
        items: [
          {
            en: "@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');",
            ru: "@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');",
          },
          { en: "", ru: "" },
          { en: "body {", ru: "body {" },
          { en: "  font-family: 'Roboto', sans-serif;", ru: "  font-family: 'Roboto', sans-serif;" },
          { en: "  font-size: 16px;", ru: "  font-size: 16px;" },
          { en: "  color: #333;", ru: "  color: #333;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS property controls the boldness of text? (one word, with a hyphen)",
          ru: "Какое CSS-свойство управляет жирностью текста? (одно слово, через дефис)",
        },
        correctText: { en: "font-weight", ru: "font-weight" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "HEX color", ru: "HEX-цвет" },
            definition: {
              en: "A six-digit code like #ff5733 representing red, green, blue",
              ru: "Шестизначный код вида #ff5733, представляющий красный, зелёный, синий",
            },
          },
          {
            term: { en: "RGBA", ru: "RGBA" },
            definition: {
              en: "RGB color with an alpha channel for transparency (0-1)",
              ru: "RGB-цвет с альфа-каналом для прозрачности (0-1)",
            },
          },
          {
            term: { en: "font-family", ru: "font-family" },
            definition: {
              en: "Specifies the typeface with a fallback stack",
              ru: "Задаёт шрифт с запасным стеком",
            },
          },
          {
            term: { en: "line-height", ru: "line-height" },
            definition: {
              en: "Sets the vertical space between lines of text",
              ru: "Задаёт вертикальное расстояние между строками текста",
            },
          },
          {
            term: { en: "Google Fonts", ru: "Google Fonts" },
            definition: {
              en: "A free library of web fonts loaded via <link> or @import",
              ru: "Бесплатная библиотека веб-шрифтов, подключаемая через <link> или @import",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-6-1: Flexbox Layout ──────────────────────────────────
  "fe-6-1": {
    id: "fe-6-1",
    title: {
      en: "Flexbox Layout",
      ru: "Вёрстка с Flexbox",
    },
    slides: [
      {
        title: {
          en: "Introduction to Flexbox",
          ru: "Введение во Flexbox",
        },
        content: {
          en: "Flexbox is a one-dimensional layout system for arranging items in a row or a column. To activate it, set display: flex on a container element. All direct children become flex items. By default, items line up in a row (flex-direction: row) and stretch to fill the container height. Flexbox eliminated the need for float-based layouts and makes centering trivial.",
          ru: "Flexbox — это одномерная система компоновки для расположения элементов в строку или столбец. Чтобы активировать её, задайте display: flex контейнеру. Все прямые потомки становятся flex-элементами. По умолчанию элементы выстраиваются в строку (flex-direction: row) и растягиваются на всю высоту контейнера. Flexbox избавил от необходимости использовать float и упростил центрирование.",
        },
        code: {
          language: "css",
          code: `.container {\n  display: flex;\n  flex-direction: row; /* default */\n}\n\n/* Column layout */\n.sidebar {\n  display: flex;\n  flex-direction: column;\n}`,
        },
      },
      {
        title: {
          en: "Alignment: justify-content & align-items",
          ru: "Выравнивание: justify-content и align-items",
        },
        content: {
          en: "justify-content controls alignment along the main axis (horizontal in a row). Values include flex-start, flex-end, center, space-between (equal space between items), and space-around. align-items controls alignment along the cross axis (vertical in a row). Common values: stretch (default), flex-start, flex-end, center, and baseline. Combining justify-content: center with align-items: center perfectly centers content.",
          ru: "justify-content управляет выравниванием по главной оси (горизонтально в строке). Значения: flex-start, flex-end, center, space-between (равные промежутки между элементами) и space-around. align-items управляет выравниванием по поперечной оси (вертикально в строке). Основные значения: stretch (по умолчанию), flex-start, flex-end, center и baseline. Комбинация justify-content: center и align-items: center идеально центрирует контент.",
        },
        code: {
          language: "css",
          code: `/* Center everything */\n.hero {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  min-height: 100vh;\n}\n\n/* Space items evenly */\n.navbar {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}`,
        },
      },
      {
        title: {
          en: "Flex Wrap & Gap",
          ru: "Flex Wrap и Gap",
        },
        content: {
          en: "By default, flex items try to fit on one line. flex-wrap: wrap allows items to wrap to the next line when they run out of space — essential for responsive card grids. The gap property adds consistent spacing between flex items without extra margins. You can set row-gap and column-gap separately, or use the shorthand gap: 16px. This is cleaner than using margin on individual items.",
          ru: "По умолчанию flex-элементы стараются уместиться в одну строку. flex-wrap: wrap позволяет элементам переноситься на следующую строку, когда места не хватает — это необходимо для адаптивных сеток карточек. Свойство gap добавляет одинаковые промежутки между flex-элементами без лишних margin. Можно задать row-gap и column-gap отдельно или использовать сокращение gap: 16px. Это чище, чем использование margin для каждого элемента.",
        },
        code: {
          language: "css",
          code: `.card-grid {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 24px;\n}\n\n.card-grid .card {\n  flex: 1 1 300px; /* grow, shrink, basis */\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does justify-content: space-between do?",
          ru: "Что делает justify-content: space-between?",
        },
        options: [
          { en: "Centers all items", ru: "Центрирует все элементы" },
          {
            en: "Distributes equal space between items, none at edges",
            ru: "Распределяет равные промежутки между элементами, без отступов по краям",
          },
          {
            en: "Adds equal space around every item",
            ru: "Добавляет равные отступы вокруг каждого элемента",
          },
          { en: "Stacks items vertically", ru: "Располагает элементы вертикально" },
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
          en: "Flexbox is a two-dimensional layout system that controls both rows and columns simultaneously.",
          ru: "Flexbox — двумерная система компоновки, управляющая строками и столбцами одновременно.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each Flexbox property to its role.",
          ru: "Сопоставьте каждое свойство Flexbox с его ролью.",
        },
        pairs: [
          {
            term: { en: "display: flex", ru: "display: flex" },
            definition: {
              en: "Activates Flexbox on a container",
              ru: "Активирует Flexbox на контейнере",
            },
          },
          {
            term: { en: "flex-direction", ru: "flex-direction" },
            definition: {
              en: "Sets the main axis direction (row or column)",
              ru: "Задаёт направление главной оси (строка или столбец)",
            },
          },
          {
            term: { en: "justify-content", ru: "justify-content" },
            definition: {
              en: "Aligns items along the main axis",
              ru: "Выравнивает элементы по главной оси",
            },
          },
          {
            term: { en: "align-items", ru: "align-items" },
            definition: {
              en: "Aligns items along the cross axis",
              ru: "Выравнивает элементы по поперечной оси",
            },
          },
          {
            term: { en: "gap", ru: "gap" },
            definition: {
              en: "Adds spacing between flex items",
              ru: "Добавляет промежутки между flex-элементами",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about Flexbox layout.",
          ru: "Заполните пропуски о компоновке Flexbox.",
        },
        blanks: [
          {
            text: {
              en: "To allow flex items to wrap onto multiple lines, use flex-wrap: ___.",
              ru: "Чтобы flex-элементы переносились на несколько строк, используйте flex-wrap: ___.",
            },
            options: [
              { en: "wrap", ru: "wrap" },
              { en: "nowrap", ru: "nowrap" },
              { en: "break", ru: "break" },
              { en: "auto", ru: "auto" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The default flex-direction value is ___.",
              ru: "Значение flex-direction по умолчанию — ___.",
            },
            options: [
              { en: "column", ru: "column" },
              { en: "row", ru: "row" },
              { en: "row-reverse", ru: "row-reverse" },
              { en: "inherit", ru: "inherit" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "To perfectly center a child, set both justify-content and align-items to ___.",
              ru: "Чтобы идеально центрировать дочерний элемент, задайте justify-content и align-items значение ___.",
            },
            options: [
              { en: "flex-start", ru: "flex-start" },
              { en: "stretch", ru: "stretch" },
              { en: "center", ru: "center" },
              { en: "space-around", ru: "space-around" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order these steps to create a centered flex layout.",
          ru: "Расположите шаги по порядку для создания центрированной flex-компоновки.",
        },
        items: [
          { en: "Create a container element in HTML", ru: "Создать элемент-контейнер в HTML" },
          { en: "Set display: flex on the container", ru: "Задать display: flex контейнеру" },
          { en: "Set justify-content: center", ru: "Задать justify-content: center" },
          { en: "Set align-items: center", ru: "Задать align-items: center" },
          { en: "Add child elements inside the container", ru: "Добавить дочерние элементы внутри контейнера" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS to create a responsive card grid with flexbox.",
          ru: "Расположите CSS-код для создания адаптивной сетки карточек на flexbox.",
        },
        items: [
          { en: ".grid {", ru: ".grid {" },
          { en: "  display: flex;", ru: "  display: flex;" },
          { en: "  flex-wrap: wrap;", ru: "  flex-wrap: wrap;" },
          { en: "  gap: 20px;", ru: "  gap: 20px;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "Which CSS property adds equal spacing between flex items without using margins?",
          ru: "Какое CSS-свойство добавляет равные промежутки между flex-элементами без использования margin?",
        },
        correctText: { en: "gap", ru: "gap" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "Flex container", ru: "Flex-контейнер" },
            definition: {
              en: "An element with display: flex that arranges its children",
              ru: "Элемент с display: flex, который компонует дочерние элементы",
            },
          },
          {
            term: { en: "Main axis", ru: "Главная ось" },
            definition: {
              en: "The primary direction of flex layout (row = horizontal)",
              ru: "Основное направление flex-компоновки (row = горизонтальное)",
            },
          },
          {
            term: { en: "Cross axis", ru: "Поперечная ось" },
            definition: {
              en: "The perpendicular axis to the main axis",
              ru: "Ось, перпендикулярная главной оси",
            },
          },
          {
            term: { en: "flex-wrap", ru: "flex-wrap" },
            definition: {
              en: "Allows flex items to wrap to the next line",
              ru: "Позволяет flex-элементам переноситься на следующую строку",
            },
          },
          {
            term: { en: "space-between", ru: "space-between" },
            definition: {
              en: "Distributes items with equal space between them, no space at edges",
              ru: "Распределяет элементы с равными промежутками между ними без отступов по краям",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-7-1: Grid Layout ─────────────────────────────────────
  "fe-7-1": {
    id: "fe-7-1",
    title: {
      en: "Grid Layout",
      ru: "Вёрстка с Grid",
    },
    slides: [
      {
        title: {
          en: "Introduction to CSS Grid",
          ru: "Введение в CSS Grid",
        },
        content: {
          en: "CSS Grid is a two-dimensional layout system that handles both rows and columns at once. Set display: grid on a container, then define columns with grid-template-columns and rows with grid-template-rows. The fr unit represents a fraction of the available space — 1fr 2fr means the second column is twice as wide as the first. Grid is ideal for page layouts, dashboards, and complex arrangements.",
          ru: "CSS Grid — двумерная система компоновки, управляющая строками и столбцами одновременно. Задайте display: grid контейнеру, затем определите столбцы через grid-template-columns и строки через grid-template-rows. Единица fr представляет долю доступного пространства — 1fr 2fr означает, что второй столбец вдвое шире первого. Grid идеально подходит для макетов страниц, дашбордов и сложных компоновок.",
        },
        code: {
          language: "css",
          code: `.layout {\n  display: grid;\n  grid-template-columns: 1fr 2fr 1fr;\n  grid-template-rows: auto 1fr auto;\n  gap: 16px;\n}`,
        },
      },
      {
        title: {
          en: "Grid Areas & Placement",
          ru: "Области Grid и размещение",
        },
        content: {
          en: "grid-template-areas lets you name regions of your grid and place items visually. Each string represents a row, and each word is a cell name. Items are then placed using grid-area: name. You can also place items using grid-column and grid-row with line numbers — for example, grid-column: 1 / 3 spans from line 1 to line 3 (two columns). The span keyword is a shorthand: grid-column: span 2.",
          ru: "grid-template-areas позволяет именовать области сетки и размещать элементы наглядно. Каждая строка представляет ряд, а каждое слово — имя ячейки. Элементы размещаются через grid-area: имя. Можно также размещать элементы через grid-column и grid-row с номерами линий — например, grid-column: 1 / 3 охватывает от линии 1 до линии 3 (два столбца). Ключевое слово span — сокращение: grid-column: span 2.",
        },
        code: {
          language: "css",
          code: `.page {\n  display: grid;\n  grid-template-areas:\n    "header header"\n    "sidebar main"\n    "footer footer";\n  grid-template-columns: 250px 1fr;\n}\n\n.header  { grid-area: header; }\n.sidebar { grid-area: sidebar; }\n.main    { grid-area: main; }\n.footer  { grid-area: footer; }`,
        },
      },
      {
        title: {
          en: "Auto-fit, Auto-fill & Responsive Grids",
          ru: "Auto-fit, auto-fill и адаптивные сетки",
        },
        content: {
          en: "The repeat() function avoids repetition: repeat(3, 1fr) creates three equal columns. For responsive grids without media queries, use auto-fit or auto-fill with minmax(). auto-fit: repeat(auto-fit, minmax(280px, 1fr)) creates as many columns as fit, each at least 280px wide. auto-fill creates the same grid but keeps empty tracks if there is extra space. auto-fit collapses empty tracks, so items stretch to fill the row.",
          ru: "Функция repeat() избавляет от повторений: repeat(3, 1fr) создаёт три равных столбца. Для адаптивных сеток без медиа-запросов используйте auto-fit или auto-fill с minmax(). auto-fit: repeat(auto-fit, minmax(280px, 1fr)) создаёт столько столбцов, сколько помещается, шириной не менее 280px. auto-fill создаёт аналогичную сетку, но сохраняет пустые дорожки при лишнем пространстве. auto-fit схлопывает пустые дорожки, и элементы растягиваются на всю строку.",
        },
        code: {
          language: "css",
          code: `/* Responsive grid — no media queries needed */\n.cards {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: 24px;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "What does the fr unit represent in CSS Grid?",
          ru: "Что представляет единица fr в CSS Grid?",
        },
        options: [
          { en: "A fixed pixel size", ru: "Фиксированный размер в пикселях" },
          {
            en: "A fraction of the available space",
            ru: "Долю доступного пространства",
          },
          { en: "A percentage of the viewport", ru: "Процент от области просмотра" },
          { en: "A font-relative unit", ru: "Единицу, относительную к шрифту" },
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
          en: "auto-fill and auto-fit behave identically — there is no difference between them.",
          ru: "auto-fill и auto-fit ведут себя одинаково — между ними нет разницы.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each Grid property to its purpose.",
          ru: "Сопоставьте каждое свойство Grid с его назначением.",
        },
        pairs: [
          {
            term: { en: "grid-template-columns", ru: "grid-template-columns" },
            definition: {
              en: "Defines the number and size of columns",
              ru: "Определяет количество и размер столбцов",
            },
          },
          {
            term: { en: "grid-template-areas", ru: "grid-template-areas" },
            definition: {
              en: "Names grid regions for visual placement",
              ru: "Именует области сетки для наглядного размещения",
            },
          },
          {
            term: { en: "grid-area", ru: "grid-area" },
            definition: {
              en: "Places an item into a named area",
              ru: "Размещает элемент в именованной области",
            },
          },
          {
            term: { en: "gap", ru: "gap" },
            definition: {
              en: "Sets spacing between grid cells",
              ru: "Задаёт расстояние между ячейками сетки",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about CSS Grid.",
          ru: "Заполните пропуски о CSS Grid.",
        },
        blanks: [
          {
            text: {
              en: "To create three equal columns, use grid-template-columns: repeat(3, ___).",
              ru: "Чтобы создать три равных столбца, используйте grid-template-columns: repeat(3, ___).",
            },
            options: [
              { en: "1fr", ru: "1fr" },
              { en: "100px", ru: "100px" },
              { en: "auto", ru: "auto" },
              { en: "33%", ru: "33%" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The function ___ creates as many columns as will fit with a minimum width.",
              ru: "Функция ___ создаёт столько столбцов, сколько поместится с минимальной шириной.",
            },
            options: [
              { en: "auto-fill", ru: "auto-fill" },
              { en: "auto-fit", ru: "auto-fit" },
              { en: "flex-wrap", ru: "flex-wrap" },
              { en: "auto-flow", ru: "auto-flow" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "CSS Grid is a ___-dimensional layout system.",
              ru: "CSS Grid — это ___-мерная система компоновки.",
            },
            options: [
              { en: "one", ru: "одно" },
              { en: "two", ru: "двух" },
              { en: "three", ru: "трёх" },
              { en: "multi", ru: "много" },
            ],
            correctIndex: 1,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to create a named-area grid layout.",
          ru: "Расположите шаги по порядку для создания макета с именованными областями.",
        },
        items: [
          { en: "Set display: grid on the container", ru: "Задать display: grid контейнеру" },
          { en: "Define grid-template-columns", ru: "Определить grid-template-columns" },
          { en: "Define grid-template-areas with named regions", ru: "Определить grid-template-areas с именованными областями" },
          { en: "Assign grid-area to each child element", ru: "Назначить grid-area каждому дочернему элементу" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS to create a responsive auto-fit grid.",
          ru: "Расположите CSS-код для создания адаптивной сетки с auto-fit.",
        },
        items: [
          { en: ".grid {", ru: ".grid {" },
          { en: "  display: grid;", ru: "  display: grid;" },
          {
            en: "  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));",
            ru: "  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));",
          },
          { en: "  gap: 20px;", ru: "  gap: 20px;" },
          { en: "  padding: 16px;", ru: "  padding: 16px;" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS function avoids writing the same column size repeatedly? (one word)",
          ru: "Какая CSS-функция избавляет от многократного написания одного размера столбца? (одно слово)",
        },
        correctText: { en: "repeat", ru: "repeat" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "fr unit", ru: "Единица fr" },
            definition: {
              en: "A fractional unit representing a share of available space",
              ru: "Дробная единица, представляющая долю доступного пространства",
            },
          },
          {
            term: { en: "grid-template-areas", ru: "grid-template-areas" },
            definition: {
              en: "Defines named regions of a grid for intuitive placement",
              ru: "Определяет именованные области сетки для интуитивного размещения",
            },
          },
          {
            term: { en: "minmax()", ru: "minmax()" },
            definition: {
              en: "Sets a minimum and maximum size for a grid track",
              ru: "Задаёт минимальный и максимальный размер дорожки сетки",
            },
          },
          {
            term: { en: "auto-fit", ru: "auto-fit" },
            definition: {
              en: "Creates as many columns as fit and collapses empty tracks",
              ru: "Создаёт столько столбцов, сколько поместится, и схлопывает пустые дорожки",
            },
          },
          {
            term: { en: "span", ru: "span" },
            definition: {
              en: "A keyword to stretch a grid item across multiple tracks",
              ru: "Ключевое слово для растягивания элемента на несколько дорожек",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-8-1: Media Queries ───────────────────────────────────
  "fe-8-1": {
    id: "fe-8-1",
    title: {
      en: "Media Queries",
      ru: "Медиа-запросы",
    },
    slides: [
      {
        title: {
          en: "What Are Media Queries?",
          ru: "Что такое медиа-запросы?",
        },
        content: {
          en: "Media queries let you apply CSS rules only when certain conditions are met — most commonly based on the viewport width. The @media rule wraps styles that only activate at specific screen sizes. This is the foundation of responsive web design. Common breakpoints: 480px (mobile), 768px (tablet), 1024px (laptop), 1280px (desktop). You can use min-width (styles apply above that width) or max-width (styles apply below).",
          ru: "Медиа-запросы позволяют применять CSS-правила только при выполнении определённых условий — чаще всего по ширине области просмотра. Правило @media оборачивает стили, которые активируются при определённых размерах экрана. Это основа адаптивного веб-дизайна. Распространённые точки перелома: 480px (мобильные), 768px (планшеты), 1024px (ноутбуки), 1280px (десктопы). Используют min-width (стили применяются выше указанной ширины) или max-width (ниже).",
        },
        code: {
          language: "css",
          code: `/* Tablet and above */\n@media (min-width: 768px) {\n  .container {\n    max-width: 720px;\n    margin: 0 auto;\n  }\n}\n\n/* Mobile only */\n@media (max-width: 479px) {\n  .sidebar {\n    display: none;\n  }\n}`,
        },
      },
      {
        title: {
          en: "Combining Conditions",
          ru: "Комбинирование условий",
        },
        content: {
          en: "You can combine media conditions with 'and' to target a specific range. For example, @media (min-width: 768px) and (max-width: 1023px) targets only tablet-sized screens. You can also use comma separation (acting as OR) to apply styles for multiple conditions. The 'orientation' feature lets you target landscape or portrait modes — useful for mobile apps and fullscreen experiences.",
          ru: "Условия медиа-запросов можно комбинировать через 'and' для нацеливания на конкретный диапазон. Например, @media (min-width: 768px) and (max-width: 1023px) нацелен только на планшетные экраны. Через запятую (как ИЛИ) можно применять стили для нескольких условий. Свойство 'orientation' позволяет нацелиться на альбомный или портретный режим — полезно для мобильных приложений.",
        },
        code: {
          language: "css",
          code: `/* Tablet only */\n@media (min-width: 768px) and (max-width: 1023px) {\n  .grid { grid-template-columns: 1fr 1fr; }\n}\n\n/* Landscape orientation */\n@media (orientation: landscape) {\n  .hero { min-height: 60vh; }\n}`,
        },
      },
      {
        title: {
          en: "Responsive Patterns",
          ru: "Адаптивные паттерны",
        },
        content: {
          en: "Common responsive patterns include: stacking columns on mobile (switching from multi-column to single column), hiding or showing elements at certain sizes, changing font sizes, and adjusting spacing. A typical pattern is a navbar that shows full links on desktop but collapses into a hamburger menu on mobile. Another pattern is switching a sidebar layout to a stacked layout on smaller screens.",
          ru: "Типичные адаптивные паттерны: укладка столбцов на мобильных (переход от нескольких столбцов к одному), скрытие или показ элементов при определённых размерах, изменение размера шрифтов и настройка отступов. Распространённый паттерн — навбар, показывающий все ссылки на десктопе и сворачивающийся в гамбургер-меню на мобильных. Другой паттерн — переход от боковой панели к вертикальной укладке на малых экранах.",
        },
        code: {
          language: "css",
          code: `/* Mobile: single column */\n.layout {\n  display: grid;\n  grid-template-columns: 1fr;\n}\n\n/* Desktop: sidebar + main */\n@media (min-width: 1024px) {\n  .layout {\n    grid-template-columns: 280px 1fr;\n  }\n  .mobile-menu-btn {\n    display: none;\n  }\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which media query targets screens 768px wide and above?",
          ru: "Какой медиа-запрос нацелен на экраны шириной 768px и больше?",
        },
        options: [
          { en: "@media (max-width: 768px)", ru: "@media (max-width: 768px)" },
          { en: "@media (min-width: 768px)", ru: "@media (min-width: 768px)" },
          { en: "@media (width: 768px)", ru: "@media (width: 768px)" },
          { en: "@media (screen: 768px)", ru: "@media (screen: 768px)" },
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
          en: "You can combine multiple media conditions using the 'and' keyword.",
          ru: "Можно комбинировать несколько условий медиа-запроса с помощью ключевого слова 'and'.",
        },
        answer: true,
      },
      {
        type: "match",
        question: {
          en: "Match each breakpoint to its typical device.",
          ru: "Сопоставьте каждую точку перелома с типичным устройством.",
        },
        pairs: [
          {
            term: { en: "480px", ru: "480px" },
            definition: { en: "Small mobile phones", ru: "Маленькие мобильные телефоны" },
          },
          {
            term: { en: "768px", ru: "768px" },
            definition: { en: "Tablets", ru: "Планшеты" },
          },
          {
            term: { en: "1024px", ru: "1024px" },
            definition: { en: "Laptops", ru: "Ноутбуки" },
          },
          {
            term: { en: "1280px", ru: "1280px" },
            definition: { en: "Desktops", ru: "Десктопы" },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about media queries.",
          ru: "Заполните пропуски о медиа-запросах.",
        },
        blanks: [
          {
            text: {
              en: "The @media rule applies styles only when a ___ is met.",
              ru: "Правило @media применяет стили только при выполнении ___.",
            },
            options: [
              { en: "condition", ru: "условия" },
              { en: "selector", ru: "селектора" },
              { en: "variable", ru: "переменной" },
              { en: "function", ru: "функции" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To target screens smaller than 768px, use @media (___: 767px).",
              ru: "Для экранов уже 768px используйте @media (___: 767px).",
            },
            options: [
              { en: "min-width", ru: "min-width" },
              { en: "max-width", ru: "max-width" },
              { en: "min-height", ru: "min-height" },
              { en: "screen-width", ru: "screen-width" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "The ___ media feature detects whether the device is in landscape or portrait mode.",
              ru: "Медиа-функция ___ определяет, находится ли устройство в альбомном или портретном режиме.",
            },
            options: [
              { en: "resolution", ru: "resolution" },
              { en: "aspect-ratio", ru: "aspect-ratio" },
              { en: "orientation", ru: "orientation" },
              { en: "display-mode", ru: "display-mode" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order these screen widths from smallest to largest.",
          ru: "Расположите эти ширины экрана от наименьшей к наибольшей.",
        },
        items: [
          { en: "320px (small phone)", ru: "320px (маленький телефон)" },
          { en: "480px (phone)", ru: "480px (телефон)" },
          { en: "768px (tablet)", ru: "768px (планшет)" },
          { en: "1024px (laptop)", ru: "1024px (ноутбук)" },
          { en: "1440px (desktop)", ru: "1440px (десктоп)" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS to create a responsive layout that switches from 1 to 3 columns.",
          ru: "Расположите CSS-код для адаптивного макета, переключающегося с 1 на 3 столбца.",
        },
        items: [
          { en: ".grid {", ru: ".grid {" },
          { en: "  display: grid;", ru: "  display: grid;" },
          { en: "  grid-template-columns: 1fr;", ru: "  grid-template-columns: 1fr;" },
          { en: "}", ru: "}" },
          { en: "@media (min-width: 768px) {", ru: "@media (min-width: 768px) {" },
          { en: "  .grid { grid-template-columns: repeat(3, 1fr); }", ru: "  .grid { grid-template-columns: repeat(3, 1fr); }" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS at-rule is used to apply styles conditionally based on viewport size?",
          ru: "Какое CSS-правило используется для условного применения стилей в зависимости от размера области просмотра?",
        },
        correctText: { en: "@media", ru: "@media" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "Breakpoint", ru: "Точка перелома" },
            definition: {
              en: "A screen width at which the layout changes",
              ru: "Ширина экрана, при которой макет меняется",
            },
          },
          {
            term: { en: "min-width", ru: "min-width" },
            definition: {
              en: "Condition that applies styles when the viewport is at or above the given width",
              ru: "Условие, применяющее стили, когда область просмотра равна или шире указанной ширины",
            },
          },
          {
            term: { en: "max-width", ru: "max-width" },
            definition: {
              en: "Condition that applies styles when the viewport is at or below the given width",
              ru: "Условие, применяющее стили, когда область просмотра равна или уже указанной ширины",
            },
          },
          {
            term: { en: "Responsive design", ru: "Адаптивный дизайн" },
            definition: {
              en: "An approach where layouts adapt to different screen sizes",
              ru: "Подход, при котором макеты адаптируются к различным размерам экрана",
            },
          },
          {
            term: { en: "orientation", ru: "Ориентация" },
            definition: {
              en: "A media feature detecting landscape or portrait device mode",
              ru: "Медиа-функция, определяющая альбомный или портретный режим устройства",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-8-2: Mobile-First Approach ───────────────────────────
  "fe-8-2": {
    id: "fe-8-2",
    title: {
      en: "Mobile-First Approach",
      ru: "Подход Mobile-First",
    },
    slides: [
      {
        title: {
          en: "What Is Mobile-First?",
          ru: "Что такое Mobile-First?",
        },
        content: {
          en: "Mobile-first means writing your base CSS for the smallest screen and then adding media queries with min-width to enhance the layout for larger screens. This is the opposite of writing desktop styles first and overriding them for mobile. Mobile-first is preferred because it leads to simpler base styles, faster mobile load times, and forces you to prioritize content. Most CSS frameworks (Tailwind, Bootstrap) follow this approach.",
          ru: "Mobile-first означает написание базового CSS для самого маленького экрана с последующим добавлением медиа-запросов с min-width для улучшения макета на больших экранах. Это противоположно написанию десктопных стилей с последующим переопределением для мобильных. Mobile-first предпочтителен, потому что приводит к более простым базовым стилям, быстрой загрузке на мобильных и заставляет приоритизировать контент. Большинство CSS-фреймворков (Tailwind, Bootstrap) используют этот подход.",
        },
        code: {
          language: "css",
          code: `/* Base styles — mobile */\n.container {\n  padding: 16px;\n}\n\n.nav-links {\n  display: none;\n}\n\n/* Tablet and up */\n@media (min-width: 768px) {\n  .container { padding: 24px; }\n  .nav-links { display: flex; }\n}\n\n/* Desktop */\n@media (min-width: 1024px) {\n  .container { max-width: 1200px; margin: 0 auto; }\n}`,
        },
      },
      {
        title: {
          en: "Relative & Viewport Units",
          ru: "Относительные и viewport-единицы",
        },
        content: {
          en: "Fixed pixel values break on different screens. Relative units adapt: rem is relative to the root font size (usually 16px), em is relative to the parent's font size, and % is relative to the parent element's dimension. Viewport units are powerful: vw = 1% of viewport width, vh = 1% of viewport height. dvh (dynamic viewport height) accounts for mobile browser bars. Use clamp() for fluid typography: clamp(1rem, 2.5vw, 2rem) sets a min, preferred, and max size.",
          ru: "Фиксированные пиксели ломаются на разных экранах. Относительные единицы адаптируются: rem относится к корневому размеру шрифта (обычно 16px), em — к размеру шрифта родителя, % — к размерам родительского элемента. Viewport-единицы мощны: vw = 1% ширины области просмотра, vh = 1% высоты. dvh (динамическая высота) учитывает панели мобильных браузеров. Используйте clamp() для плавной типографики: clamp(1rem, 2.5vw, 2rem) задаёт минимум, предпочтительный и максимальный размер.",
        },
        code: {
          language: "css",
          code: `/* Fluid typography with clamp */\nh1 {\n  font-size: clamp(1.5rem, 4vw, 3rem);\n}\n\n/* Full-height hero section */\n.hero {\n  min-height: 100dvh;\n  padding: 5vw;\n}\n\n/* Responsive spacing with rem */\n.section {\n  padding: 2rem 1rem;\n}`,
        },
      },
      {
        title: {
          en: "Responsive Images",
          ru: "Адаптивные изображения",
        },
        content: {
          en: "Images must scale with the layout. The simplest rule is max-width: 100% with height: auto — this ensures images never overflow their container. For art direction (different images for different screens), use the <picture> element with <source> tags and media attributes. The object-fit property controls how images fill their container: cover (fills, may crop), contain (fits, may leave gaps). Always include width and height attributes on <img> to prevent layout shift.",
          ru: "Изображения должны масштабироваться вместе с макетом. Простейшее правило — max-width: 100% с height: auto — гарантирует, что изображения не выходят за контейнер. Для арт-дирекции (разные изображения для разных экранов) используйте элемент <picture> с тегами <source> и атрибутом media. Свойство object-fit контролирует заполнение контейнера: cover (заполняет, может обрезать), contain (вмещает, могут быть поля). Всегда указывайте width и height на <img> для предотвращения сдвигов макета.",
        },
        code: {
          language: "css",
          code: `/* Responsive image */\nimg {\n  max-width: 100%;\n  height: auto;\n  display: block;\n}\n\n/* Cover image for cards */\n.card-img {\n  width: 100%;\n  height: 200px;\n  object-fit: cover;\n  border-radius: 8px;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "In a mobile-first approach, which type of media query do you add for larger screens?",
          ru: "При подходе mobile-first какой тип медиа-запроса добавляется для больших экранов?",
        },
        options: [
          { en: "max-width", ru: "max-width" },
          { en: "min-width", ru: "min-width" },
          { en: "exact-width", ru: "exact-width" },
          { en: "device-width", ru: "device-width" },
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
          en: "1rem always equals 16 pixels regardless of any settings.",
          ru: "1rem всегда равен 16 пикселям вне зависимости от настроек.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each unit to its reference point.",
          ru: "Сопоставьте каждую единицу с её точкой отсчёта.",
        },
        pairs: [
          {
            term: { en: "rem", ru: "rem" },
            definition: {
              en: "Relative to the root element font size",
              ru: "Относительно размера шрифта корневого элемента",
            },
          },
          {
            term: { en: "em", ru: "em" },
            definition: {
              en: "Relative to the parent element font size",
              ru: "Относительно размера шрифта родительского элемента",
            },
          },
          {
            term: { en: "vw", ru: "vw" },
            definition: {
              en: "1% of the viewport width",
              ru: "1% ширины области просмотра",
            },
          },
          {
            term: { en: "vh", ru: "vh" },
            definition: {
              en: "1% of the viewport height",
              ru: "1% высоты области просмотра",
            },
          },
          {
            term: { en: "%", ru: "%" },
            definition: {
              en: "Relative to the parent element's dimension",
              ru: "Относительно размеров родительского элемента",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about responsive techniques.",
          ru: "Заполните пропуски о методах адаптивности.",
        },
        blanks: [
          {
            text: {
              en: "To prevent images from overflowing, set ___: 100% on the img element.",
              ru: "Чтобы изображения не выходили за контейнер, задайте ___: 100% элементу img.",
            },
            options: [
              { en: "max-width", ru: "max-width" },
              { en: "width", ru: "width" },
              { en: "min-width", ru: "min-width" },
              { en: "flex-basis", ru: "flex-basis" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "The CSS function ___ lets you set a minimum, preferred, and maximum value.",
              ru: "CSS-функция ___ позволяет задать минимальное, предпочтительное и максимальное значение.",
            },
            options: [
              { en: "calc()", ru: "calc()" },
              { en: "clamp()", ru: "clamp()" },
              { en: "min()", ru: "min()" },
              { en: "var()", ru: "var()" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "The object-fit value ___ fills the container and may crop the image.",
              ru: "Значение object-fit ___ заполняет контейнер и может обрезать изображение.",
            },
            options: [
              { en: "contain", ru: "contain" },
              { en: "fill", ru: "fill" },
              { en: "cover", ru: "cover" },
              { en: "none", ru: "none" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the mobile-first media queries from smallest to largest breakpoint.",
          ru: "Расположите медиа-запросы mobile-first от наименьшей к наибольшей точке перелома.",
        },
        items: [
          { en: "Base styles (no media query)", ru: "Базовые стили (без медиа-запроса)" },
          { en: "@media (min-width: 480px)", ru: "@media (min-width: 480px)" },
          { en: "@media (min-width: 768px)", ru: "@media (min-width: 768px)" },
          { en: "@media (min-width: 1024px)", ru: "@media (min-width: 1024px)" },
          { en: "@media (min-width: 1280px)", ru: "@media (min-width: 1280px)" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS for a mobile-first responsive container.",
          ru: "Расположите CSS для адаптивного контейнера в стиле mobile-first.",
        },
        items: [
          { en: ".container {", ru: ".container {" },
          { en: "  width: 100%;", ru: "  width: 100%;" },
          { en: "  padding: 1rem;", ru: "  padding: 1rem;" },
          { en: "}", ru: "}" },
          { en: "@media (min-width: 768px) {", ru: "@media (min-width: 768px) {" },
          { en: "  .container { max-width: 720px; margin: 0 auto; }", ru: "  .container { max-width: 720px; margin: 0 auto; }" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS unit equals 1% of the viewport width?",
          ru: "Какая CSS-единица равна 1% ширины области просмотра?",
        },
        correctText: { en: "vw", ru: "vw" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "Mobile-first", ru: "Mobile-first" },
            definition: {
              en: "Writing base styles for mobile and adding min-width queries for larger screens",
              ru: "Написание базовых стилей для мобильных с добавлением min-width запросов для больших экранов",
            },
          },
          {
            term: { en: "clamp()", ru: "clamp()" },
            definition: {
              en: "A function that sets min, preferred, and max values in one declaration",
              ru: "Функция, задающая минимум, предпочтительное и максимальное значения в одном объявлении",
            },
          },
          {
            term: { en: "object-fit", ru: "object-fit" },
            definition: {
              en: "Controls how an image fills its container (cover, contain, etc.)",
              ru: "Управляет тем, как изображение заполняет контейнер (cover, contain и т.д.)",
            },
          },
          {
            term: { en: "dvh", ru: "dvh" },
            definition: {
              en: "Dynamic viewport height that accounts for mobile browser UI changes",
              ru: "Динамическая высота области просмотра, учитывающая изменения интерфейса мобильного браузера",
            },
          },
          {
            term: { en: "max-width: 100%", ru: "max-width: 100%" },
            definition: {
              en: "Ensures an element never exceeds its container width",
              ru: "Гарантирует, что элемент никогда не превышает ширину контейнера",
            },
          },
        ],
      },
    ],
  },

  // ─── LESSON fe-9-1: Animations & Transitions ───────────────────────
  "fe-9-1": {
    id: "fe-9-1",
    title: {
      en: "Animations & Transitions",
      ru: "Анимации и переходы",
    },
    slides: [
      {
        title: {
          en: "CSS Transitions",
          ru: "CSS-переходы",
        },
        content: {
          en: "Transitions smoothly animate property changes triggered by state changes like :hover or class toggling. The transition shorthand takes: property, duration, timing function, and delay. For example, transition: background-color 0.3s ease means when background-color changes, it animates over 0.3 seconds with an ease curve. Use transition: all 0.3s ease to animate every property, or list specific ones for better performance. Stick to transform and opacity for the smoothest animations — they are GPU-accelerated.",
          ru: "Переходы плавно анимируют изменения свойств, вызванные сменой состояния, например :hover или переключением класса. Сокращение transition принимает: свойство, длительность, функцию плавности и задержку. Например, transition: background-color 0.3s ease означает, что при изменении background-color анимация занимает 0.3 секунды с кривой ease. Используйте transition: all 0.3s ease для анимации всех свойств или перечислите конкретные для лучшей производительности. Используйте transform и opacity для самых плавных анимаций — они ускоряются GPU.",
        },
        code: {
          language: "css",
          code: `.btn {\n  background: #3b82f6;\n  color: white;\n  padding: 12px 24px;\n  border-radius: 8px;\n  transition: background-color 0.3s ease, transform 0.2s ease;\n}\n\n.btn:hover {\n  background: #2563eb;\n  transform: translateY(-2px);\n}`,
        },
      },
      {
        title: {
          en: "Keyframe Animations",
          ru: "Анимации с @keyframes",
        },
        content: {
          en: "@keyframes lets you define multi-step animations independent of state changes. You name the animation and define stages using percentages (0% to 100%) or 'from' and 'to'. Then apply it with the animation shorthand: animation: name duration timing-function iteration-count. Use animation-fill-mode: forwards to keep the final state. infinite makes the animation loop forever. You can combine multiple animations separated by commas.",
          ru: "@keyframes позволяет задавать многоэтапные анимации, не зависящие от смены состояния. Вы именуете анимацию и определяете этапы через проценты (0%–100%) или 'from' и 'to'. Затем применяете через сокращение animation: имя длительность функция-плавности число-повторов. Используйте animation-fill-mode: forwards для сохранения конечного состояния. infinite зацикливает анимацию. Можно комбинировать несколько анимаций через запятую.",
        },
        code: {
          language: "css",
          code: `@keyframes fadeInUp {\n  from {\n    opacity: 0;\n    transform: translateY(20px);\n  }\n  to {\n    opacity: 1;\n    transform: translateY(0);\n  }\n}\n\n.card {\n  animation: fadeInUp 0.5s ease forwards;\n}`,
        },
      },
      {
        title: {
          en: "Transform & Practical Effects",
          ru: "Transform и практические эффекты",
        },
        content: {
          en: "The transform property changes an element's position, size, or shape without affecting layout. Key functions: translate(x, y) moves the element, scale(x) resizes it, rotate(deg) spins it, and skew(deg) tilts it. Transforms can be chained: transform: translateY(-4px) scale(1.02). The opacity property (0 to 1) controls visibility. Combining transform and opacity creates most UI animations: hover effects, loading spinners, page enter/exit transitions, and modal fade-ins.",
          ru: "Свойство transform изменяет положение, размер или форму элемента, не влияя на макет. Основные функции: translate(x, y) перемещает элемент, scale(x) масштабирует, rotate(deg) вращает и skew(deg) наклоняет. Трансформации можно цеплять: transform: translateY(-4px) scale(1.02). Свойство opacity (0–1) управляет видимостью. Комбинация transform и opacity создаёт большинство UI-анимаций: эффекты наведения, спиннеры загрузки, переходы между страницами и появление модальных окон.",
        },
        code: {
          language: "css",
          code: `/* Hover scale effect */\n.card {\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n}\n.card:hover {\n  transform: translateY(-4px) scale(1.02);\n  box-shadow: 0 12px 24px rgba(0,0,0,0.15);\n}\n\n/* Spinning loader */\n@keyframes spin {\n  to { transform: rotate(360deg); }\n}\n.loader {\n  width: 32px;\n  height: 32px;\n  border: 3px solid #e5e7eb;\n  border-top-color: #3b82f6;\n  border-radius: 50%;\n  animation: spin 0.8s linear infinite;\n}`,
        },
      },
    ],
    questions: [
      {
        type: "quiz",
        question: {
          en: "Which properties are GPU-accelerated and best for smooth animations?",
          ru: "Какие свойства ускоряются GPU и лучше всего подходят для плавных анимаций?",
        },
        options: [
          { en: "width and height", ru: "width и height" },
          { en: "margin and padding", ru: "margin и padding" },
          { en: "transform and opacity", ru: "transform и opacity" },
          { en: "color and background", ru: "color и background" },
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
          en: "CSS transitions require @keyframes to work.",
          ru: "CSS-переходы требуют @keyframes для работы.",
        },
        answer: false,
      },
      {
        type: "match",
        question: {
          en: "Match each animation concept to its description.",
          ru: "Сопоставьте каждое понятие анимации с его описанием.",
        },
        pairs: [
          {
            term: { en: "transition", ru: "transition" },
            definition: {
              en: "Animates property changes between two states",
              ru: "Анимирует изменения свойств между двумя состояниями",
            },
          },
          {
            term: { en: "@keyframes", ru: "@keyframes" },
            definition: {
              en: "Defines multi-step animation sequences",
              ru: "Определяет многоэтапные последовательности анимации",
            },
          },
          {
            term: { en: "transform", ru: "transform" },
            definition: {
              en: "Moves, scales, rotates, or skews an element",
              ru: "Перемещает, масштабирует, вращает или наклоняет элемент",
            },
          },
          {
            term: { en: "opacity", ru: "opacity" },
            definition: {
              en: "Controls the transparency of an element (0 to 1)",
              ru: "Управляет прозрачностью элемента (от 0 до 1)",
            },
          },
          {
            term: { en: "animation-fill-mode", ru: "animation-fill-mode" },
            definition: {
              en: "Determines whether styles persist after animation ends",
              ru: "Определяет, сохраняются ли стили после окончания анимации",
            },
          },
        ],
      },
      {
        type: "fill_blanks",
        question: {
          en: "Fill in the blanks about CSS animations.",
          ru: "Заполните пропуски о CSS-анимациях.",
        },
        blanks: [
          {
            text: {
              en: "The transition shorthand takes property, duration, timing function, and ___.",
              ru: "Сокращение transition принимает свойство, длительность, функцию плавности и ___.",
            },
            options: [
              { en: "delay", ru: "задержку" },
              { en: "direction", ru: "направление" },
              { en: "count", ru: "количество" },
              { en: "mode", ru: "режим" },
            ],
            correctIndex: 0,
          },
          {
            text: {
              en: "To loop an animation forever, set animation-iteration-count to ___.",
              ru: "Чтобы зациклить анимацию навсегда, задайте animation-iteration-count значение ___.",
            },
            options: [
              { en: "forever", ru: "forever" },
              { en: "infinite", ru: "infinite" },
              { en: "loop", ru: "loop" },
              { en: "repeat", ru: "repeat" },
            ],
            correctIndex: 1,
          },
          {
            text: {
              en: "The transform function ___(x, y) moves an element without affecting layout.",
              ru: "Функция transform ___(x, y) перемещает элемент, не влияя на макет.",
            },
            options: [
              { en: "move", ru: "move" },
              { en: "shift", ru: "shift" },
              { en: "translate", ru: "translate" },
              { en: "position", ru: "position" },
            ],
            correctIndex: 2,
          },
        ],
      },
      {
        type: "drag_order",
        question: {
          en: "Order the steps to create a fade-in animation.",
          ru: "Расположите шаги по порядку для создания анимации появления.",
        },
        items: [
          { en: "Define @keyframes with a name", ru: "Определить @keyframes с именем" },
          { en: "Set from state (opacity: 0)", ru: "Задать начальное состояние (opacity: 0)" },
          { en: "Set to state (opacity: 1)", ru: "Задать конечное состояние (opacity: 1)" },
          { en: "Apply animation property to the element", ru: "Применить свойство animation к элементу" },
          { en: "Set animation-fill-mode: forwards", ru: "Задать animation-fill-mode: forwards" },
        ],
      },
      {
        type: "code_puzzle",
        question: {
          en: "Arrange the CSS to create a hover button effect with transition.",
          ru: "Расположите CSS для создания эффекта кнопки при наведении с transition.",
        },
        items: [
          { en: ".btn {", ru: ".btn {" },
          { en: "  background: #3b82f6;", ru: "  background: #3b82f6;" },
          { en: "  transition: transform 0.2s ease;", ru: "  transition: transform 0.2s ease;" },
          { en: "}", ru: "}" },
          { en: ".btn:hover {", ru: ".btn:hover {" },
          { en: "  transform: scale(1.05);", ru: "  transform: scale(1.05);" },
          { en: "}", ru: "}" },
        ],
      },
      {
        type: "type_answer",
        question: {
          en: "What CSS at-rule defines multi-step animation sequences?",
          ru: "Какое CSS-правило определяет многоэтапные последовательности анимации?",
        },
        correctText: { en: "@keyframes", ru: "@keyframes" },
      },
      {
        type: "flash_cards",
        question: {
          en: "Review key terms.",
          ru: "Повторите ключевые термины.",
        },
        pairs: [
          {
            term: { en: "transition", ru: "transition" },
            definition: {
              en: "Smoothly animates CSS property changes between states",
              ru: "Плавно анимирует изменения CSS-свойств между состояниями",
            },
          },
          {
            term: { en: "ease", ru: "ease" },
            definition: {
              en: "A timing function that starts slow, speeds up, then slows down",
              ru: "Функция плавности: медленное начало, ускорение, затем замедление",
            },
          },
          {
            term: { en: "transform: scale()", ru: "transform: scale()" },
            definition: {
              en: "Resizes an element up or down from its center",
              ru: "Масштабирует элемент от его центра",
            },
          },
          {
            term: { en: "animation: infinite", ru: "animation: infinite" },
            definition: {
              en: "Makes the animation loop forever without stopping",
              ru: "Зацикливает анимацию навсегда без остановки",
            },
          },
          {
            term: { en: "forwards", ru: "forwards" },
            definition: {
              en: "An animation-fill-mode value that keeps the final keyframe styles",
              ru: "Значение animation-fill-mode, сохраняющее стили последнего кадра",
            },
          },
        ],
      },
    ],
  },
};
