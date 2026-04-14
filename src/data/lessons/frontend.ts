import type { LessonContent } from "../lessons";

export const FRONTEND_LESSONS: Record<string, LessonContent> = {
  "fe-1-1": {
    id: "fe-1-1",
    title: "Document Structure",
    content: `# HTML Document Structure

Every HTML page starts with a fundamental structure that tells the browser how to interpret and render the content. Understanding this structure is the very first step in becoming a web developer.

## The DOCTYPE Declaration

The \`<!DOCTYPE html>\` declaration must be the very first line in every HTML file. It tells the browser that this document uses HTML5, the latest standard. Without it, browsers may render your page in "quirks mode," which can cause inconsistent behavior across different browsers.

## The HTML Element

The \`<html>\` element wraps everything on the page. It accepts a \`lang\` attribute (e.g., \`lang="en"\`) that helps screen readers and search engines understand the language of your content. Inside the \`<html>\` tag, there are exactly two direct children: \`<head>\` and \`<body>\`.

## Head vs Body

The \`<head>\` element contains metadata — information about the page that is not directly visible. This includes the page title (shown in the browser tab), character encoding (\`<meta charset="UTF-8">\`), viewport settings for responsive design, links to CSS stylesheets, and other meta tags for SEO.

The \`<body>\` element contains all the visible content: text, images, links, forms, and everything the user interacts with. Think of the head as the backstage and the body as the stage.

## Essential Meta Tags

Two meta tags are considered essential in modern HTML. The charset meta tag ensures your page can display characters from any language. The viewport meta tag is critical for responsive design — without it, mobile browsers will render your page at a desktop width and then zoom out.`,
    videos: [
      { title: "HTML Crash Course For Absolute Beginners", url: "https://www.youtube.com/watch?v=UB1O30fR-EE", duration: "60:00" },
      { title: "HTML Full Course for Beginners", url: "https://www.youtube.com/watch?v=mJgBOIoGihA", duration: "4:10:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="My awesome website">
  <title>My First Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Hello World!</h1>
  <p>This is my first web page.</p>
  <script src="app.js"></script>
</body>
</html>`,
      },
    ],
    quiz: [
      {
        question: "What does the <head> element contain?",
        options: ["Visible content", "Metadata and page info", "Images and videos", "Navigation links"],
        correct: 1,
      },
      {
        question: "Which declaration specifies HTML5?",
        options: ["<html5>", "<!DOCTYPE html>", "<version>5</version>", "<meta html5>"],
        correct: 1,
      },
      {
        question: "What attribute on <html> helps screen readers identify the page language?",
        options: ["class", "lang", "type", "charset"],
        correct: 1,
      },
    ],
    flashCards: [
      { front: "<!DOCTYPE html>", back: "Declares the document as HTML5" },
      { front: "<head>", back: "Contains metadata, title, and links to stylesheets" },
      { front: "<body>", back: "Contains all visible page content" },
      { front: "<meta charset=\"UTF-8\">", back: "Sets character encoding to support all languages" },
      { front: "<title>", back: "Sets the text shown in browser tab" },
      { front: "viewport meta tag", back: "Enables proper rendering on mobile devices" },
    ],
    matchGame: [
      { term: "<!DOCTYPE>", definition: "Document type declaration" },
      { term: "<head>", definition: "Metadata container" },
      { term: "<body>", definition: "Visible content container" },
      { term: "<title>", definition: "Browser tab text" },
      { term: "<meta>", definition: "Page metadata" },
    ],
  },

  "fe-1-2": {
    id: "fe-1-2",
    title: "Common Tags",
    content: `# Common HTML Tags

HTML provides dozens of tags, but a core set of them covers the vast majority of what you'll use in everyday web development. Mastering these common tags gives you the foundation to build any web page.

## Headings

HTML has six levels of headings, from \`<h1>\` (the most important) to \`<h6>\` (the least important). Each page should generally have one \`<h1>\` for the main title, and you should not skip heading levels (e.g., don't jump from \`<h1>\` to \`<h4>\`). Headings are crucial for both SEO and accessibility — screen readers use them to navigate the page structure.

## Paragraphs, Links, and Text Formatting

The \`<p>\` tag defines a paragraph of text. The \`<a>\` (anchor) tag creates hyperlinks — the backbone of the web. It uses the \`href\` attribute for the URL destination. For text emphasis, use \`<strong>\` for bold (important text) and \`<em>\` for italic (stressed text). Avoid \`<b>\` and \`<i>\` unless you specifically need visual styling without semantic meaning.

## Lists

There are two main list types: \`<ul>\` (unordered/bullet list) and \`<ol>\` (ordered/numbered list). Both use \`<li>\` for individual items. Lists are perfect for navigation menus, feature lists, or any grouped content. You can also nest lists inside each other.

## Images and Media

The \`<img>\` tag embeds images. It's a self-closing tag that requires a \`src\` attribute (the image path) and an \`alt\` attribute (alternative text for accessibility). Always provide meaningful alt text — it helps visually impaired users and improves SEO.

## Divs and Spans

The \`<div>\` element is a generic block-level container used for grouping content and applying styles. The \`<span>\` element is its inline equivalent. While semantic tags are preferred, divs and spans remain essential for layout and styling purposes.`,
    videos: [
      { title: "HTML Tags, Attributes, and Elements", url: "https://www.youtube.com/watch?v=salY_Sm6mv4", duration: "14:00" },
      { title: "Learn HTML in 1 Hour", url: "https://www.youtube.com/watch?v=qz0aGYrrlhU", duration: "56:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<!-- Headings -->
<h1>Main Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- Paragraph with link -->
<p>Visit <a href="https://developer.mozilla.org" target="_blank">MDN</a> for documentation.</p>

<!-- Text formatting -->
<p>This is <strong>very important</strong> and this is <em>emphasized</em>.</p>

<!-- Unordered list -->
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<!-- Image with alt text -->
<img src="photo.jpg" alt="A beautiful sunset over the ocean" width="600">

<!-- Generic containers -->
<div class="card">
  <h3>Card Title</h3>
  <p>Card content with a <span class="highlight">highlighted</span> word.</p>
</div>`,
      },
    ],
    quiz: [
      {
        question: "How many heading levels does HTML have?",
        options: ["3", "4", "6", "8"],
        correct: 2,
      },
      {
        question: "Which attribute is required on an <img> tag for accessibility?",
        options: ["title", "alt", "src", "class"],
        correct: 1,
      },
      {
        question: "What is the difference between <div> and <span>?",
        options: [
          "div is for text, span is for images",
          "div is block-level, span is inline",
          "They are identical",
          "span is deprecated",
        ],
        correct: 1,
      },
    ],
  },

  "fe-2-1": {
    id: "fe-2-1",
    title: "Form Elements",
    content: `# HTML Form Elements

Forms are the primary way users interact with and send data to websites. From login pages to search bars, forms are everywhere on the web. Understanding form elements is essential for building interactive applications.

## The Form Tag

The \`<form>\` element wraps all form controls. Key attributes include \`action\` (the URL where data is sent) and \`method\` (usually "GET" or "POST"). In modern single-page applications, you often prevent the default form submission with JavaScript and handle data yourself.

## Input Types

The \`<input>\` tag is the most versatile form element. By changing its \`type\` attribute, you get entirely different controls: \`text\` for single-line text, \`password\` for masked input, \`email\` for email validation, \`number\` for numeric input, \`checkbox\` for boolean choices, \`radio\` for mutually exclusive options, \`date\` for date pickers, and \`file\` for uploading files.

## Labels and Accessibility

Every form control must have an associated \`<label>\`. You connect them either by wrapping the input inside the label, or by using the \`for\` attribute on the label that matches the input's \`id\`. This is essential for accessibility — screen readers read the label when the user focuses the input, and clicking the label focuses the input.

## Select, Textarea, and Buttons

The \`<select>\` element creates a dropdown menu with \`<option>\` children. The \`<textarea>\` element creates a multi-line text input, useful for comments and messages. The \`<button>\` element creates clickable buttons — use \`type="submit"\` inside forms and \`type="button"\` for JavaScript-triggered actions.

## Validation Attributes

HTML5 provides built-in validation through attributes like \`required\`, \`minlength\`, \`maxlength\`, \`min\`, \`max\`, and \`pattern\` (for regex). These give users immediate feedback without needing JavaScript, though you should always validate on the server as well.`,
    videos: [
      { title: "HTML Forms Crash Course", url: "https://www.youtube.com/watch?v=fNcJuPIZ2WE", duration: "38:00" },
      { title: "Learn HTML Forms In 25 Minutes", url: "https://www.youtube.com/watch?v=fNcJuPIZ2WE", duration: "25:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<form action="/register" method="POST">
  <!-- Text input with label -->
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required minlength="3" maxlength="20">

  <!-- Email with validation -->
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required placeholder="you@example.com">

  <!-- Password -->
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" required minlength="8">

  <!-- Radio buttons -->
  <fieldset>
    <legend>Account Type:</legend>
    <label><input type="radio" name="role" value="student" checked> Student</label>
    <label><input type="radio" name="role" value="teacher"> Teacher</label>
  </fieldset>

  <!-- Checkbox -->
  <label>
    <input type="checkbox" name="terms" required>
    I agree to the Terms of Service
  </label>

  <!-- Select dropdown -->
  <label for="country">Country:</label>
  <select id="country" name="country">
    <option value="">Choose...</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="kz">Kazakhstan</option>
  </select>

  <!-- Textarea -->
  <label for="bio">Bio:</label>
  <textarea id="bio" name="bio" rows="4" maxlength="500"></textarea>

  <button type="submit">Create Account</button>
</form>`,
      },
    ],
    quiz: [
      {
        question: "Which input type provides built-in email validation?",
        options: ["text", "email", "validate-email", "mail"],
        correct: 1,
      },
      {
        question: "Why should every input have a <label>?",
        options: [
          "It makes the page load faster",
          "It's required by CSS",
          "It improves accessibility for screen readers",
          "It adds colors to the form",
        ],
        correct: 2,
      },
      {
        question: "What attribute makes a form field mandatory?",
        options: ["mandatory", "needed", "required", "validate"],
        correct: 2,
      },
    ],
  },

  "fe-2-2": {
    id: "fe-2-2",
    title: "Tables",
    content: `# HTML Tables

Tables are used to display structured, tabular data — data that naturally belongs in rows and columns. While tables should not be used for layout (use CSS Grid and Flexbox instead), they are the correct semantic choice for data like schedules, statistics, and spreadsheets.

## Table Structure

An HTML table is defined by the \`<table>\` element. Inside it, you use \`<thead>\` for the header row(s), \`<tbody>\` for the main data, and optionally \`<tfoot>\` for a footer row. Each row is created with \`<tr>\`, header cells use \`<th>\`, and data cells use \`<td>\`.

## Spanning Rows and Columns

Sometimes a cell needs to span multiple columns or rows. The \`colspan\` attribute makes a cell stretch across multiple columns, while \`rowspan\` stretches it across multiple rows. This is useful for merged header cells or summary rows.

## Accessibility in Tables

For accessible tables, use \`<caption>\` to give the table a visible title. Use \`scope="col"\` on column headers and \`scope="row"\` on row headers so screen readers can properly associate data cells with their headers. This helps visually impaired users understand the relationship between data and its labels.

## Styling Tables

Tables come with minimal default styling. Common CSS improvements include: \`border-collapse: collapse\` to remove double borders, alternating row colors with \`:nth-child(even)\`, hover effects on rows, and proper padding on cells. Modern frameworks like Tailwind CSS make table styling straightforward.`,
    videos: [
      { title: "HTML Tables Tutorial", url: "https://www.youtube.com/watch?v=iDA0kF5lrVk", duration: "12:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<table>
  <caption>Q1 2024 Sales Report</caption>
  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">January</th>
      <th scope="col">February</th>
      <th scope="col">March</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Widget A</th>
      <td>$1,200</td>
      <td>$1,500</td>
      <td>$1,800</td>
    </tr>
    <tr>
      <th scope="row">Widget B</th>
      <td>$800</td>
      <td>$950</td>
      <td>$1,100</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td colspan="3">$7,350</td>
    </tr>
  </tfoot>
</table>`,
      },
    ],
    quiz: [
      {
        question: "Should HTML tables be used for page layout?",
        options: [
          "Yes, always",
          "No, use CSS Grid/Flexbox for layout",
          "Only for simple layouts",
          "Tables cannot be styled",
        ],
        correct: 1,
      },
      {
        question: "What does the colspan attribute do?",
        options: [
          "Changes column color",
          "Merges a cell across multiple columns",
          "Adds spacing between columns",
          "Creates a new column",
        ],
        correct: 1,
      },
    ],
  },

  "fe-3-1": {
    id: "fe-3-1",
    title: "Semantic Elements",
    content: `# Semantic HTML Elements

Semantic HTML means using elements that carry meaning about the structure and content of the page, rather than just using \`<div>\` for everything. This is one of the most important practices in modern web development.

## Why Semantics Matter

Semantic elements provide three major benefits. First, they improve accessibility — screen readers use them to help visually impaired users navigate pages efficiently. Second, they boost SEO — search engines understand the structure and content of your page better. Third, they make your code more readable and maintainable for other developers.

## Structural Semantic Elements

HTML5 introduced several structural elements: \`<header>\` for introductory content or navigation, \`<nav>\` for navigation links, \`<main>\` for the primary content (only one per page), \`<article>\` for self-contained compositions (blog posts, news stories), \`<section>\` for thematic groupings of content, \`<aside>\` for tangentially related content (sidebars), and \`<footer>\` for closing content with metadata.

## Text-Level Semantic Elements

Beyond structure, there are elements for inline semantics: \`<time>\` for dates and times (with a machine-readable \`datetime\` attribute), \`<mark>\` for highlighted text, \`<figure>\` with \`<figcaption>\` for images with captions, \`<blockquote>\` and \`<cite>\` for quotations and their sources, \`<code>\` for inline code, and \`<abbr>\` for abbreviations.

## Common Mistakes

A frequent mistake is wrapping everything in divs. If an element has a semantic equivalent, use it. Another mistake is using \`<section>\` without a heading — if content doesn't naturally warrant a heading, a \`<div>\` may be more appropriate. Also, \`<article>\` doesn't just mean "blog article" — it means any self-contained, independently distributable content.

## Practical Page Layout

A typical semantic page has a \`<header>\` with a \`<nav>\` inside, a \`<main>\` containing one or more \`<article>\` or \`<section>\` elements, an optional \`<aside>\` for sidebars, and a \`<footer>\` at the bottom. This structure is both human-readable and machine-parseable.`,
    videos: [
      { title: "Semantic HTML Tutorial", url: "https://www.youtube.com/watch?v=kGW8Al_cga4", duration: "12:00" },
      { title: "Why & When to Use Semantic HTML", url: "https://www.youtube.com/watch?v=bOUhq46fd5g", duration: "10:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/blog">Blog</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <header>
      <h1>Understanding Semantic HTML</h1>
      <time datetime="2024-03-15">March 15, 2024</time>
    </header>

    <section>
      <h2>What Are Semantic Elements?</h2>
      <p>Semantic elements clearly describe their meaning...</p>
    </section>

    <figure>
      <img src="diagram.png" alt="Diagram showing semantic page layout">
      <figcaption>A typical semantic HTML page structure</figcaption>
    </figure>

    <footer>
      <p>Written by <cite>Jane Doe</cite></p>
    </footer>
  </article>

  <aside>
    <h2>Related Articles</h2>
    <ul>
      <li><a href="/a11y">Accessibility Guide</a></li>
    </ul>
  </aside>
</main>

<footer>
  <p>&copy; 2024 My Website</p>
</footer>`,
      },
    ],
    quiz: [
      {
        question: "Which element should wrap the primary content of a page?",
        options: ["<div>", "<section>", "<main>", "<body>"],
        correct: 2,
      },
      {
        question: "What is a benefit of using semantic HTML?",
        options: [
          "Pages load faster",
          "Better SEO and accessibility",
          "CSS is not needed",
          "JavaScript runs more efficiently",
        ],
        correct: 1,
      },
      {
        question: "How many <main> elements should a page have?",
        options: ["As many as needed", "Exactly one", "Two", "None"],
        correct: 1,
      },
    ],
  },

  "fe-4-1": {
    id: "fe-4-1",
    title: "ARIA & A11y",
    content: `# Accessibility (A11y) and ARIA

Web accessibility means ensuring that websites can be used by everyone, including people with visual, auditory, motor, or cognitive disabilities. Approximately 15% of the world's population experiences some form of disability, making accessibility both an ethical responsibility and a legal requirement in many jurisdictions.

## The Four POUR Principles

The Web Content Accessibility Guidelines (WCAG) are built on four principles: Perceivable (information must be presentable in ways users can perceive), Operable (interface components must be operable by all users), Understandable (content must be readable and predictable), and Robust (content must be interpretable by a wide variety of user agents, including assistive technologies).

## ARIA Attributes

ARIA (Accessible Rich Internet Applications) is a set of attributes that supplement HTML when native semantic elements aren't sufficient. Key ARIA attributes include: \`role\` (defines what an element is — e.g., "button", "dialog", "alert"), \`aria-label\` (provides an accessible name), \`aria-labelledby\` (references another element as the label), \`aria-hidden\` (hides elements from assistive technology), \`aria-live\` (announces dynamic content changes), and \`aria-expanded\` / \`aria-pressed\` (for toggle states).

## The First Rule of ARIA

The first rule of ARIA is: don't use ARIA if a native HTML element can do the job. A \`<button>\` is always better than \`<div role="button">\`. Native elements have built-in keyboard handling, focus management, and screen reader support. ARIA should only fill gaps that native HTML cannot.

## Keyboard Navigation

All interactive elements must be accessible via keyboard. Users should be able to Tab through elements, press Enter or Space to activate buttons, use Arrow keys in lists, and press Escape to close dialogs. Use \`tabindex="0"\` to make custom elements focusable, and \`tabindex="-1"\` to make elements programmatically focusable without adding them to the tab order.

## Testing Accessibility

Use browser DevTools accessibility panels, the axe extension, or Lighthouse audits to test accessibility. Screen readers like VoiceOver (macOS), NVDA (Windows), or JAWS can be used for manual testing. Automated tools catch about 30-50% of issues — manual testing is essential for complete coverage.`,
    videos: [
      { title: "Web Accessibility - Complete Course", url: "https://www.youtube.com/watch?v=e2nkq3h1P68", duration: "14:00" },
      { title: "ARIA HTML Tutorial", url: "https://www.youtube.com/watch?v=0hqhAIjE_8I", duration: "6:00" },
    ],
    codeExamples: [
      {
        language: "html",
        code: `<!-- Good: Using native elements -->
<button onclick="toggleMenu()">Menu</button>

<!-- Bad: Div pretending to be a button -->
<div role="button" tabindex="0" onclick="toggleMenu()" onkeydown="if(event.key==='Enter')toggleMenu()">
  Menu
</div>

<!-- ARIA labels for icon buttons -->
<button aria-label="Close dialog">
  <svg><!-- X icon --></svg>
</button>

<!-- Live region for dynamic updates -->
<div aria-live="polite" aria-atomic="true">
  <!-- Screen reader will announce when content changes -->
  <p>3 items in your cart</p>
</div>

<!-- Accessible modal dialog -->
<dialog aria-labelledby="dialog-title" aria-describedby="dialog-desc">
  <h2 id="dialog-title">Confirm Deletion</h2>
  <p id="dialog-desc">This action cannot be undone. Are you sure?</p>
  <button>Cancel</button>
  <button>Delete</button>
</dialog>

<!-- Skip navigation link -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- Accessible form error -->
<label for="email">Email</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<span id="email-error" role="alert">Please enter a valid email address</span>`,
      },
    ],
    quiz: [
      {
        question: "What is the first rule of ARIA?",
        options: [
          "Always use ARIA roles",
          "Don't use ARIA if native HTML can do the job",
          "Every element needs an aria-label",
          "ARIA replaces HTML semantics",
        ],
        correct: 1,
      },
      {
        question: "Which attribute announces dynamic content changes to screen readers?",
        options: ["aria-label", "aria-live", "aria-hidden", "role"],
        correct: 1,
      },
      {
        question: "What does WCAG stand for?",
        options: [
          "Web Content Accessibility Guidelines",
          "Web CSS Accessibility Guide",
          "Website Compliance Assessment Group",
          "World Content Accessibility Goals",
        ],
        correct: 0,
      },
    ],
  },

  "fe-5-1": {
    id: "fe-5-1",
    title: "Selectors & Box Model",
    content: `# CSS Selectors and the Box Model

CSS (Cascading Style Sheets) controls the visual presentation of HTML. The two most fundamental concepts you must master are selectors (how you target elements) and the box model (how every element is sized and spaced).

## CSS Selectors

Selectors determine which elements your styles apply to. The basic selectors are: element selectors (\`p\`, \`h1\`), class selectors (\`.card\`), ID selectors (\`#header\`), and the universal selector (\`*\`). Combinators let you combine selectors: descendant (\`div p\`), child (\`div > p\`), adjacent sibling (\`h2 + p\`), and general sibling (\`h2 ~ p\`).

## Specificity and Cascade

When multiple rules target the same element, specificity determines which wins. Inline styles have the highest specificity, followed by IDs, then classes/attributes/pseudo-classes, then element selectors. If specificity is equal, the last rule in the stylesheet wins. Understanding specificity prevents frustrating "why isn't my CSS working" moments.

## The Box Model

Every HTML element is a rectangular box with four layers: content (the actual text/image), padding (space between content and border), border (the edge of the box), and margin (space outside the border). By default, width and height only apply to the content area, which means padding and border add to the total size.

## Box-Sizing: Border-Box

The default \`box-sizing: content-box\` makes width calculations confusing because padding and border are added on top of the specified width. Setting \`box-sizing: border-box\` changes this so that padding and border are included within the specified width. Most modern CSS resets apply this globally because it makes layout calculations far more intuitive.

## Display Property

The \`display\` property controls how an element behaves in the layout. Block elements (\`div\`, \`p\`, \`h1\`) take up the full width and stack vertically. Inline elements (\`span\`, \`a\`, \`strong\`) flow within text and only take up as much width as needed. \`inline-block\` combines both — flows inline but accepts width/height. \`none\` removes the element from the layout entirely.`,
    videos: [
      { title: "CSS Selectors in 20 Minutes", url: "https://www.youtube.com/watch?v=l1mER1bV0N0", duration: "20:00" },
      { title: "CSS Box Model Tutorial", url: "https://www.youtube.com/watch?v=rIO5326FgPE", duration: "8:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Universal box-sizing reset */
*, *::before, *::after {
  box-sizing: border-box;
}

/* Element selector */
p {
  color: #333;
  line-height: 1.6;
}

/* Class selector */
.card {
  width: 300px;        /* With border-box, this IS the total width */
  padding: 20px;       /* Included in the 300px */
  border: 1px solid #ddd;  /* Included in the 300px */
  margin: 16px;        /* Always outside */
  border-radius: 8px;
}

/* ID selector (avoid for styling — too specific) */
#hero {
  background: linear-gradient(135deg, #667eea, #764ba2);
}

/* Combinators */
.card > h2 {          /* Direct child */
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.card p + p {          /* Adjacent sibling */
  margin-top: 1rem;
}

/* Pseudo-classes */
.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
  transition: all 0.2s ease;
}

/* Attribute selector */
input[type="email"] {
  border: 2px solid #3b82f6;
}`,
      },
    ],
    quiz: [
      {
        question: "Which has the highest specificity?",
        options: ["Element selector (p)", "Class selector (.text)", "ID selector (#title)", "Universal selector (*)"],
        correct: 2,
      },
      {
        question: "What does box-sizing: border-box do?",
        options: [
          "Adds a border to all boxes",
          "Includes padding and border within the specified width",
          "Removes all margins",
          "Sets the box to full width",
        ],
        correct: 1,
      },
      {
        question: "What are the four layers of the CSS box model (inside to outside)?",
        options: [
          "Content, Border, Padding, Margin",
          "Content, Padding, Border, Margin",
          "Margin, Border, Padding, Content",
          "Content, Margin, Padding, Border",
        ],
        correct: 1,
      },
    ],
    matchGame: [
      { term: ".class", definition: "Selects elements by class name" },
      { term: "#id", definition: "Selects element by unique ID" },
      { term: "padding", definition: "Space between content and border" },
      { term: "margin", definition: "Space outside the border" },
      { term: "border-box", definition: "Includes padding/border in width" },
      { term: ":hover", definition: "Pseudo-class for mouse over" },
    ],
  },

  "fe-5-2": {
    id: "fe-5-2",
    title: "Colors & Typography",
    content: `# CSS Colors and Typography

Colors and typography are the two most impactful aspects of visual design. Getting them right makes the difference between a professional-looking website and an amateur one. CSS offers powerful tools for both.

## Color Systems

CSS supports several color formats: named colors (\`red\`, \`blue\`), hexadecimal (\`#ff0000\`, \`#f00\`), RGB (\`rgb(255, 0, 0)\`), RGBA with transparency (\`rgba(255, 0, 0, 0.5)\`), HSL (\`hsl(0, 100%, 50%)\`), and HSLA. HSL is the most intuitive — you specify hue (0-360), saturation (0-100%), and lightness (0-100%). This makes it easy to create color variations by adjusting lightness while keeping the same hue.

## CSS Custom Properties for Colors

Modern CSS uses custom properties (CSS variables) for color systems. Define your palette in the \`:root\` selector and reference them everywhere with \`var()\`. This makes it trivial to implement themes, dark mode, and maintain consistency across your entire site.

## Typography Fundamentals

Typography in CSS involves several properties: \`font-family\` sets the typeface (always include a fallback stack), \`font-size\` sets the text size, \`font-weight\` controls boldness, \`line-height\` controls the vertical spacing between lines (1.5-1.6 is ideal for body text), and \`letter-spacing\` adjusts spacing between characters.

## Responsive Typography

Use relative units like \`rem\` (relative to root font size) and \`em\` (relative to parent font size) instead of pixels. The \`clamp()\` function enables fluid typography that scales smoothly between viewport sizes: \`clamp(1rem, 2.5vw, 2rem)\` sets a minimum, preferred, and maximum font size.

## Web Fonts

Google Fonts and Font Squirrel provide free web fonts. Load them via \`<link>\` tags or \`@import\` in CSS. Use \`font-display: swap\` to show fallback text while fonts load — this avoids invisible text (FOIT). Limit yourself to 2-3 font families maximum to keep load times down and design cohesive.`,
    videos: [
      { title: "CSS Typography - Kevin Powell", url: "https://www.youtube.com/watch?v=88EPZO_PjXE", duration: "23:00" },
      { title: "CSS Colors In Depth", url: "https://www.youtube.com/watch?v=HxztHgRN8I4", duration: "10:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Color system with CSS custom properties */
:root {
  --color-primary: hsl(220, 90%, 56%);
  --color-primary-light: hsl(220, 90%, 70%);
  --color-primary-dark: hsl(220, 90%, 40%);
  --color-text: hsl(220, 15%, 20%);
  --color-text-muted: hsl(220, 10%, 55%);
  --color-bg: hsl(0, 0%, 100%);
  --color-surface: hsl(220, 20%, 97%);
}

/* Dark mode override */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: hsl(220, 15%, 90%);
    --color-text-muted: hsl(220, 10%, 60%);
    --color-bg: hsl(220, 20%, 10%);
    --color-surface: hsl(220, 20%, 15%);
  }
}

/* Typography system */
html {
  font-size: 16px;  /* 1rem = 16px */
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: var(--color-text);
  line-height: 1.6;
}

h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); }
h3 { font-size: clamp(1.25rem, 2vw, 1.75rem); }

.text-muted {
  color: var(--color-text-muted);
  font-size: 0.875rem;
}`,
      },
    ],
    quiz: [
      {
        question: "Which color format is most intuitive for creating color variations?",
        options: ["Hex (#ff0000)", "RGB (rgb(255,0,0))", "HSL (hsl(0,100%,50%))", "Named colors (red)"],
        correct: 2,
      },
      {
        question: "What does the clamp() function do for font sizes?",
        options: [
          "Limits font to one size",
          "Sets min, preferred, and max values for fluid scaling",
          "Clamps text to one line",
          "Prevents font from loading",
        ],
        correct: 1,
      },
    ],
  },

  "fe-6-1": {
    id: "fe-6-1",
    title: "Flexbox Layout",
    content: `# Flexbox Layout

Flexbox (Flexible Box Layout) is a one-dimensional layout method for arranging items in rows or columns. It revolutionized CSS layout by making alignment, spacing, and distribution of space incredibly simple — tasks that were previously painful with floats and positioning.

## Flex Container and Flex Items

To use Flexbox, set \`display: flex\` on a parent element (the flex container). Its direct children automatically become flex items. The container controls the overall layout direction and alignment, while individual items can override their own sizing and ordering.

## Main Axis vs Cross Axis

Flexbox operates on two axes. The main axis runs in the direction set by \`flex-direction\` (default is \`row\`, meaning left to right). The cross axis is perpendicular to it. Understanding which axis is which is key to using \`justify-content\` (main axis alignment), \`align-items\` (cross axis alignment), and \`align-self\` (per-item cross axis alignment).

## Key Container Properties

\`flex-direction\` sets the main axis direction: \`row\`, \`row-reverse\`, \`column\`, \`column-reverse\`. \`flex-wrap\` controls whether items wrap to new lines when they overflow (\`nowrap\` is the default). \`justify-content\` distributes space along the main axis with values like \`flex-start\`, \`center\`, \`space-between\`, and \`space-evenly\`. \`align-items\` aligns items along the cross axis (\`stretch\`, \`center\`, \`flex-start\`, \`flex-end\`). \`gap\` sets the spacing between flex items.

## Key Item Properties

\`flex-grow\` determines how much extra space an item takes (0 means don't grow, 1 means take equal share). \`flex-shrink\` determines how much an item shrinks when space is insufficient. \`flex-basis\` sets the initial size before growing/shrinking. The shorthand \`flex: 1\` is equivalent to \`flex: 1 1 0%\`, making items share space equally. \`order\` changes visual order without changing HTML source order.

## Common Patterns

Flexbox excels at centering (both horizontally and vertically with just three lines), navigation bars, card layouts, footer-at-bottom layouts (using flex-grow on the main content), and equal-height columns. For two-dimensional layouts (rows AND columns), CSS Grid is more appropriate.`,
    videos: [
      { title: "Flexbox CSS In 20 Minutes", url: "https://www.youtube.com/watch?v=JJSoEo8JSnc", duration: "20:00" },
      { title: "Flexbox Tutorial - Kevin Powell", url: "https://www.youtube.com/watch?v=u044iM9xsWU", duration: "46:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Perfect centering */
.center-everything {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* Navigation bar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  gap: 1rem;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  list-style: none;
}

/* Card grid that wraps */
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card {
  flex: 1 1 300px;  /* Grow, shrink, min 300px base */
  padding: 1.5rem;
  border-radius: 8px;
}

/* Sticky footer layout */
.page-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.page-layout main {
  flex: 1;  /* Takes all available space, pushes footer down */
}

/* Equal height columns */
.columns {
  display: flex;
  gap: 2rem;
}

.columns > * {
  flex: 1;  /* Each column gets equal width */
}`,
      },
    ],
    quiz: [
      {
        question: "What does justify-content control in Flexbox?",
        options: [
          "Alignment along the cross axis",
          "Alignment along the main axis",
          "The font justification",
          "The flex direction",
        ],
        correct: 1,
      },
      {
        question: "How do you make all flex items share space equally?",
        options: ["width: equal", "flex: 1", "justify-content: equal", "align-items: stretch"],
        correct: 1,
      },
      {
        question: "What is the default flex-direction?",
        options: ["column", "row", "row-reverse", "inherit"],
        correct: 1,
      },
    ],
  },

  "fe-7-1": {
    id: "fe-7-1",
    title: "Grid Layout",
    content: `# CSS Grid Layout

CSS Grid is a two-dimensional layout system that lets you control both rows and columns simultaneously. While Flexbox is ideal for one-dimensional layouts, Grid is designed for full page layouts and complex component arrangements.

## Defining a Grid

Set \`display: grid\` on a container to create a grid context. Define columns with \`grid-template-columns\` and rows with \`grid-template-rows\`. The \`fr\` unit (fraction) distributes available space proportionally — \`1fr 2fr\` creates two columns where the second is twice as wide as the first.

## The repeat() Function and auto-fill/auto-fit

The \`repeat()\` function avoids repetition: \`repeat(3, 1fr)\` creates three equal columns. For responsive grids without media queries, use \`repeat(auto-fill, minmax(250px, 1fr))\` — this creates as many columns as will fit, each at least 250px wide. \`auto-fill\` creates empty tracks for remaining space, while \`auto-fit\` collapses empty tracks so items stretch to fill.

## Placing Items

By default, grid items fill cells left-to-right, top-to-bottom. You can explicitly place items using \`grid-column\` and \`grid-row\` with line numbers: \`grid-column: 1 / 3\` spans from line 1 to line 3 (two columns). The \`span\` keyword is a shortcut: \`grid-column: span 2\` means "span two columns from wherever I am."

## Named Grid Areas

For full page layouts, \`grid-template-areas\` lets you name regions and place items by name. This creates a visual map of your layout right in the CSS, making it extremely readable. Each string represents a row, and each word in the string represents a column cell.

## Gap, Alignment, and Subgrid

The \`gap\` property (or \`row-gap\` and \`column-gap\`) sets spacing between tracks. Grid supports the same alignment properties as Flexbox (\`justify-items\`, \`align-items\`, \`justify-content\`, \`align-content\`) plus item-level overrides (\`justify-self\`, \`align-self\`). The newer \`subgrid\` value lets nested grids inherit their parent's track sizing, which is powerful for card layouts where you need content alignment across cards.`,
    videos: [
      { title: "CSS Grid Layout Crash Course", url: "https://www.youtube.com/watch?v=jV8B24rSN5o", duration: "28:00" },
      { title: "Learn CSS Grid the Easy Way", url: "https://www.youtube.com/watch?v=rg7Fvvl3taU", duration: "36:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Responsive card grid — no media queries needed! */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 1.5rem;
}

/* Full page layout with named areas */
.page-layout {
  display: grid;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }

/* Item placement */
.featured-card {
  grid-column: span 2;  /* Takes two columns */
  grid-row: span 2;     /* Takes two rows */
}

/* Explicit placement by line number */
.hero {
  grid-column: 1 / -1;  /* Full width (-1 = last line) */
}

/* 12-column layout system */
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}

.col-6 { grid-column: span 6; }
.col-4 { grid-column: span 4; }
.col-3 { grid-column: span 3; }`,
      },
    ],
    quiz: [
      {
        question: "What does the fr unit represent in CSS Grid?",
        options: [
          "Fixed ratio",
          "A fraction of available space",
          "Font ratio",
          "Full row",
        ],
        correct: 1,
      },
      {
        question: "How do you create a responsive grid without media queries?",
        options: [
          "grid-template-columns: auto",
          "grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))",
          "grid-template-columns: responsive",
          "grid-auto-flow: responsive",
        ],
        correct: 1,
      },
      {
        question: "What is the difference between auto-fill and auto-fit?",
        options: [
          "They are identical",
          "auto-fill creates empty tracks; auto-fit collapses them",
          "auto-fit only works with px units",
          "auto-fill is deprecated",
        ],
        correct: 1,
      },
    ],
  },

  "fe-8-1": {
    id: "fe-8-1",
    title: "Media Queries",
    content: `# CSS Media Queries

Media queries are the foundation of responsive web design. They allow you to apply different styles based on the characteristics of the user's device, most commonly the viewport width. This enables your website to look great on everything from phones to widescreen monitors.

## Basic Syntax

A media query uses the \`@media\` rule followed by a media type and conditions. The most common pattern is \`@media (min-width: 768px) { ... }\` which applies styles when the viewport is 768px or wider. You can combine conditions with \`and\`, use \`or\` (comma), and negate with \`not\`.

## Common Breakpoints

While breakpoints should be based on your content rather than specific devices, common starting points are: 640px (small tablets/large phones), 768px (tablets), 1024px (laptops), 1280px (desktops), and 1536px (large screens). Modern frameworks like Tailwind use similar values. The key principle is to add breakpoints where your content needs them, not at specific device widths.

## Media Features Beyond Width

Width is the most used media feature, but there are many others: \`prefers-color-scheme\` detects dark/light mode preference, \`prefers-reduced-motion\` detects motion sensitivity, \`orientation\` checks portrait vs landscape, \`hover\` checks if the device supports hover states, and \`pointer\` checks if the pointer is coarse (touch) or fine (mouse).

## Container Queries

A newer addition to CSS is container queries (\`@container\`). Unlike media queries that check the viewport, container queries check the size of a parent container. This is extremely useful for reusable components that need to adapt to their available space regardless of the overall page layout.

## Using Media Queries Effectively

Avoid duplicating large blocks of CSS in media queries. Instead, write your base styles for the default state and use media queries only for the properties that change. Group related breakpoints together and keep them close to the rules they modify. With modern CSS features like \`clamp()\`, Grid \`auto-fit\`, and Flexbox \`flex-wrap\`, you need fewer media queries than you might think.`,
    videos: [
      { title: "CSS Media Queries Tutorial", url: "https://www.youtube.com/watch?v=yU7jJ3NbPdA", duration: "11:00" },
      { title: "CSS Responsive Design", url: "https://www.youtube.com/watch?v=srvUrASNj0s", duration: "25:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Base styles (mobile) */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  padding: 1rem;
}

/* Tablet and up */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 2rem;
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }
}

/* Dark mode preference */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a2e;
    --text: #e0e0e0;
  }
}

/* Reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* Touch devices — larger tap targets */
@media (pointer: coarse) {
  button, a {
    min-height: 44px;
    min-width: 44px;
  }
}

/* Container queries */
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}`,
      },
    ],
    quiz: [
      {
        question: "Which media feature detects dark mode preference?",
        options: ["prefers-dark-mode", "prefers-color-scheme", "color-mode", "dark-mode"],
        correct: 1,
      },
      {
        question: "What is the difference between media queries and container queries?",
        options: [
          "They are identical",
          "Media queries check viewport; container queries check parent element size",
          "Container queries are not supported",
          "Media queries only work for print",
        ],
        correct: 1,
      },
    ],
  },

  "fe-8-2": {
    id: "fe-8-2",
    title: "Mobile-First",
    content: `# Mobile-First Design

Mobile-first is a design and development strategy where you start by building the mobile version of your site, then progressively enhance it for larger screens. This approach leads to better performance, cleaner code, and a better experience for the majority of web users who browse on mobile devices.

## Why Mobile-First?

Over 60% of global web traffic comes from mobile devices. Starting mobile-first forces you to prioritize content and focus on what truly matters. It results in simpler base CSS that gets enhanced rather than bloated desktop CSS that gets overridden. Mobile-first also leads to better performance because mobile devices load only the base styles plus whatever enhancements apply to their size.

## Mobile-First in Practice

In code, mobile-first means using \`min-width\` media queries exclusively. Your base styles (outside any media query) define the mobile layout. Then you add \`@media (min-width: ...)\` rules to enhance for larger screens. This is the opposite of "desktop-first" which uses \`max-width\` queries to scale down.

## Responsive Images

Images are often the largest assets on a page. Use the \`<picture>\` element or \`srcset\` attribute to serve different image sizes to different devices. The CSS \`max-width: 100%\` on images prevents them from overflowing their container. For decorative images, consider using CSS backgrounds with different images at different breakpoints.

## Viewport Meta Tag

The viewport meta tag \`<meta name="viewport" content="width=device-width, initial-scale=1.0">\` is essential. Without it, mobile browsers render pages at a virtual desktop width (typically 980px) and zoom out, making everything tiny. This single meta tag is the gateway to mobile-responsive design.

## Touch Considerations

Mobile design requires thinking about touch interactions. Tap targets (buttons, links) should be at least 44x44 pixels. Hover states don't exist on touch devices, so don't hide important information behind them. Forms should use appropriate input types (\`type="tel"\`, \`type="email"\`) to trigger the right mobile keyboard.`,
    videos: [
      { title: "Mobile First Responsive Design", url: "https://www.youtube.com/watch?v=0ohtVzCSHqs", duration: "19:00" },
      { title: "Responsive Web Design Tutorial", url: "https://www.youtube.com/watch?v=srvUrASNj0s", duration: "25:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* MOBILE-FIRST approach */

/* Base: Mobile (no media query needed) */
.container {
  padding: 1rem;
  max-width: 100%;
}

.nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.hero-title {
  font-size: 1.75rem;
}

.sidebar {
  display: none;  /* Hidden on mobile */
}

/* Tablet: 768px+ */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    max-width: 720px;
    margin: 0 auto;
  }

  .nav {
    flex-direction: row;
    gap: 2rem;
  }

  .hero-title {
    font-size: 2.5rem;
  }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
  .container {
    max-width: 960px;
  }

  .page-layout {
    display: grid;
    grid-template-columns: 250px 1fr;
  }

  .sidebar {
    display: block;  /* Visible on desktop */
  }

  .hero-title {
    font-size: 3.5rem;
  }
}`,
      },
      {
        language: "html",
        code: `<!-- Responsive images with srcset -->
<img
  src="photo-400.jpg"
  srcset="photo-400.jpg 400w,
          photo-800.jpg 800w,
          photo-1200.jpg 1200w"
  sizes="(min-width: 1024px) 50vw, 100vw"
  alt="A responsive photo"
>

<!-- Picture element for art direction -->
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.jpg">
  <source media="(min-width: 768px)" srcset="hero-tablet.jpg">
  <img src="hero-mobile.jpg" alt="Hero image">
</picture>`,
      },
    ],
    quiz: [
      {
        question: "What does mobile-first mean in CSS?",
        options: [
          "Only support mobile devices",
          "Write base styles for mobile, enhance with min-width queries",
          "Use max-width queries to scale down from desktop",
          "Disable desktop layouts",
        ],
        correct: 1,
      },
      {
        question: "What is the minimum recommended tap target size for mobile?",
        options: ["24x24px", "32x32px", "44x44px", "60x60px"],
        correct: 2,
      },
    ],
  },

  "fe-9-1": {
    id: "fe-9-1",
    title: "Animations & Transitions",
    content: `# CSS Animations and Transitions

Animations and transitions bring interfaces to life, guiding user attention and providing visual feedback. When used thoughtfully, motion makes interfaces feel more responsive and polished. The key is subtlety — animations should enhance the experience, not distract from it.

## CSS Transitions

Transitions are the simplest form of animation. They smoothly interpolate between two states of a property when that property changes (e.g., on hover). You specify which property to transition, the duration, and optionally a timing function and delay. The shorthand \`transition: all 0.3s ease\` transitions all animatable properties, but it's better to be explicit about which properties you're transitioning for performance.

## Timing Functions

Timing functions control the acceleration curve of animations. Built-in options include \`ease\` (default, starts fast then slows), \`linear\` (constant speed), \`ease-in\` (starts slow), \`ease-out\` (ends slow), and \`ease-in-out\` (slow start and end). For custom curves, use \`cubic-bezier(x1, y1, x2, y2)\`. Tools like cubic-bezier.com help you create custom curves visually.

## CSS Keyframe Animations

For more complex, multi-step animations, use \`@keyframes\`. Define named animations with percentage-based steps from \`0%\` (or \`from\`) to \`100%\` (or \`to\`), then apply them with the \`animation\` property. You can control duration, timing, delay, iteration count (including \`infinite\`), direction, and fill mode.

## Performance Considerations

Only animate \`transform\` and \`opacity\` — these properties are handled by the GPU compositor and don't trigger layout recalculations. Animating properties like \`width\`, \`height\`, \`margin\`, or \`top\`/\`left\` forces the browser to recalculate layout every frame, causing jank. Use \`transform: translateX()\` instead of \`left\`, and \`transform: scale()\` instead of changing \`width\`/\`height\`.

## Respecting User Preferences

Always wrap animations in a \`prefers-reduced-motion\` media query check. Some users have vestibular disorders or motion sensitivity that makes animations uncomfortable or even physically harmful. Provide a reduced-motion alternative that removes or minimizes movement while keeping the interface functional.`,
    videos: [
      { title: "CSS Animations Tutorial", url: "https://www.youtube.com/watch?v=YszONjKpgg4", duration: "23:00" },
      { title: "CSS Transitions & Transforms", url: "https://www.youtube.com/watch?v=zHUpx90NerM", duration: "30:00" },
    ],
    codeExamples: [
      {
        language: "css",
        code: `/* Transition on hover */
.button {
  background: #3b82f6;
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  transition: background 0.2s ease, transform 0.2s ease;
}

.button:hover {
  background: #2563eb;
  transform: translateY(-2px);
}

.button:active {
  transform: translateY(0);
}

/* Keyframe animation — fade and slide in */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: fadeInUp 0.5s ease-out forwards;
}

/* Staggered animation with delay */
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 100ms; }
.card:nth-child(3) { animation-delay: 200ms; }

/* Loading spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e5e7eb;
  border-top-color: #3b82f6;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

/* Pulse animation */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.skeleton {
  animation: pulse 2s ease-in-out infinite;
  background: #e5e7eb;
  border-radius: 4px;
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}`,
      },
    ],
    quiz: [
      {
        question: "Which CSS properties are best to animate for performance?",
        options: [
          "width and height",
          "margin and padding",
          "transform and opacity",
          "top and left",
        ],
        correct: 2,
      },
      {
        question: "What does @keyframes define?",
        options: [
          "A transition between two states",
          "A multi-step animation sequence",
          "A media query breakpoint",
          "A CSS variable",
        ],
        correct: 1,
      },
      {
        question: "Why should you check prefers-reduced-motion?",
        options: [
          "To speed up animations on slow devices",
          "Some users have motion sensitivity or vestibular disorders",
          "To enable animations only on mobile",
          "It is required by CSS specification",
        ],
        correct: 1,
      },
    ],
  },

  "fe-10-1": {
    id: "fe-10-1",
    title: "Variables & Types",
    content: `# JavaScript Variables and Data Types

JavaScript is the programming language of the web. Understanding variables and data types is the essential foundation — everything you build in JavaScript works with data stored in variables.

## Declaring Variables

JavaScript has three ways to declare variables: \`var\` (function-scoped, avoid in modern code), \`let\` (block-scoped, for values that change), and \`const\` (block-scoped, for values that don't change). Always prefer \`const\` by default. Only use \`let\` when you know the value will be reassigned. Never use \`var\` in new code — its function-scoping and hoisting behavior cause subtle bugs.

## Primitive Data Types

JavaScript has seven primitive types: \`string\` (text in quotes), \`number\` (integers and floats — JavaScript has no separate integer type), \`boolean\` (\`true\` or \`false\`), \`null\` (intentional absence of value), \`undefined\` (variable declared but not assigned), \`symbol\` (unique identifiers), and \`bigint\` (for integers larger than 2^53). Use \`typeof\` to check a value's type.

## Strings

Strings can be defined with single quotes, double quotes, or backticks. Template literals (backticks) are the most powerful — they support multi-line strings and embedded expressions with \`\${expression}\`. Common string methods include \`.length\`, \`.toUpperCase()\`, \`.toLowerCase()\`, \`.includes()\`, \`.slice()\`, \`.split()\`, and \`.trim()\`.

## Numbers and Math

All numbers in JavaScript are 64-bit floating point. This means \`0.1 + 0.2 !== 0.3\` (a famous gotcha). The \`Math\` object provides utilities: \`Math.round()\`, \`Math.floor()\`, \`Math.ceil()\`, \`Math.random()\`, \`Math.max()\`, \`Math.min()\`. Use \`parseInt()\` and \`parseFloat()\` to convert strings to numbers, or the unary \`+\` operator.

## Type Coercion

JavaScript automatically converts types in certain contexts (type coercion). For example, \`"5" + 3\` gives \`"53"\` (string concatenation), but \`"5" - 3\` gives \`2\` (numeric subtraction). Always use strict equality (\`===\`) instead of loose equality (\`==\`) to avoid coercion surprises. Strict equality checks both value and type.`,
    videos: [
      { title: "JavaScript Variables & Data Types", url: "https://www.youtube.com/watch?v=edlFjlzxkSI", duration: "18:00" },
      { title: "JavaScript Crash Course For Beginners", url: "https://www.youtube.com/watch?v=hdI2bqOjy3c", duration: "1:40:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Variable declarations
const PI = 3.14159;         // Cannot be reassigned
let score = 0;              // Can be reassigned
let playerName = "Alex";    // Can be reassigned

// Primitive types
const name = "Sarah";       // string
const age = 25;             // number
const isStudent = true;     // boolean
const middle = null;        // null (intentional empty)
let address;                // undefined (not yet assigned)

// typeof operator
console.log(typeof name);      // "string"
console.log(typeof age);       // "number"
console.log(typeof isStudent); // "boolean"
console.log(typeof null);      // "object" (known JS quirk!)

// Template literals
const greeting = \`Hello, \${name}! You are \${age} years old.\`;
const multiLine = \`
  This is line 1.
  This is line 2.
\`;

// String methods
console.log(name.length);          // 5
console.log(name.toUpperCase());   // "SARAH"
console.log(name.includes("ar"));  // true
console.log("hello world".split(" ")); // ["hello", "world"]

// Number gotchas
console.log(0.1 + 0.2);           // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);   // false!

// Type coercion — avoid with ===
console.log("5" == 5);   // true (loose — coerces types)
console.log("5" === 5);  // false (strict — checks type too)

// Converting types explicitly
const str = "42";
const num = Number(str);     // 42
const num2 = parseInt(str);  // 42
const back = String(num);    // "42"`,
      },
    ],
    quiz: [
      {
        question: "Which keyword should you prefer for declaring variables?",
        options: ["var", "let", "const", "define"],
        correct: 2,
      },
      {
        question: "What does typeof null return?",
        options: ['"null"', '"undefined"', '"object"', '"boolean"'],
        correct: 2,
      },
      {
        question: "Why should you use === instead of ==?",
        options: [
          "=== is faster",
          "=== checks both value and type, avoiding coercion bugs",
          "== is deprecated",
          "They are identical",
        ],
        correct: 1,
      },
    ],
  },

  "fe-10-2": {
    id: "fe-10-2",
    title: "Control Flow",
    content: `# JavaScript Control Flow

Control flow determines the order in which your code executes. Conditionals let you make decisions, and loops let you repeat actions. Together, they give your programs logic and the ability to handle different scenarios.

## If/Else Statements

The \`if\` statement executes code when a condition is truthy. You can chain conditions with \`else if\` and provide a fallback with \`else\`. JavaScript treats these values as falsy: \`false\`, \`0\`, \`""\` (empty string), \`null\`, \`undefined\`, and \`NaN\`. Everything else is truthy — including empty arrays and objects.

## Ternary Operator

For simple conditional assignments, the ternary operator is more concise: \`const result = condition ? valueIfTrue : valueIfFalse\`. It's perfect for single-line decisions like setting a variable or choosing between two values. Avoid nesting ternaries — they quickly become unreadable.

## Switch Statements

When comparing one value against many possible matches, \`switch\` is cleaner than a chain of \`if/else if\`. Each \`case\` needs a \`break\` statement (or the code "falls through" to the next case). Always include a \`default\` case for unexpected values.

## For Loops

The traditional \`for\` loop gives you full control: \`for (let i = 0; i < array.length; i++)\`. The \`for...of\` loop is simpler for iterating over arrays: \`for (const item of items)\`. The \`for...in\` loop iterates over object keys (use cautiously — it also includes inherited properties). In practice, array methods like \`forEach\`, \`map\`, and \`filter\` are often preferred over loops.

## While and Do-While

The \`while\` loop repeats as long as a condition is true. The \`do...while\` loop executes at least once before checking the condition. Use these when you don't know in advance how many iterations you need. Always ensure the loop condition will eventually become false to avoid infinite loops.

## Short-Circuit Evaluation

JavaScript evaluates logical operators lazily. With \`&&\`, if the left side is falsy, the right side never executes. With \`||\`, if the left side is truthy, the right side is skipped. The nullish coalescing operator \`??\` returns the right side only if the left is \`null\` or \`undefined\` (not just falsy). These are powerful for default values and conditional execution.`,
    videos: [
      { title: "JavaScript If Else & Loops", url: "https://www.youtube.com/watch?v=IsG4Xd6LlsM", duration: "15:00" },
      { title: "JavaScript Loops Explained", url: "https://www.youtube.com/watch?v=Kn06785pkJg", duration: "12:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// If / else if / else
const score = 85;

if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 80) {
  console.log("Grade: B");
} else if (score >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}

// Ternary operator
const status = score >= 60 ? "Pass" : "Fail";

// Switch statement
const day = "monday";
switch (day) {
  case "monday":
  case "tuesday":
  case "wednesday":
  case "thursday":
  case "friday":
    console.log("Weekday");
    break;
  case "saturday":
  case "sunday":
    console.log("Weekend");
    break;
  default:
    console.log("Invalid day");
}

// For loop
for (let i = 0; i < 5; i++) {
  console.log(\`Iteration \${i}\`);
}

// For...of (arrays)
const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
  console.log(fruit);
}

// While loop
let attempts = 0;
while (attempts < 3) {
  console.log(\`Attempt \${attempts + 1}\`);
  attempts++;
}

// Short-circuit evaluation
const user = { name: "Alex" };
const displayName = user.name || "Anonymous";    // "Alex"
const theme = user.theme ?? "light";             // "light" (nullish coalescing)

// Optional chaining with nullish coalescing
const city = user?.address?.city ?? "Unknown";   // "Unknown"`,
      },
    ],
    quiz: [
      {
        question: "Which values are falsy in JavaScript?",
        options: [
          "0, empty string, null, undefined, NaN, false",
          "0, empty string, empty array, null",
          "Only null and undefined",
          "Only false and 0",
        ],
        correct: 0,
      },
      {
        question: "What does the ?? operator do?",
        options: [
          "Checks if value is falsy",
          "Returns right side only if left is null or undefined",
          "Performs type coercion",
          "Throws an error for null values",
        ],
        correct: 1,
      },
      {
        question: "Which loop is best for iterating over array elements?",
        options: ["for...in", "for...of", "while", "do...while"],
        correct: 1,
      },
    ],
  },

  "fe-11-1": {
    id: "fe-11-1",
    title: "Functions & Closures",
    content: `# Functions and Closures

Functions are the fundamental building blocks of JavaScript programs. They let you encapsulate reusable logic, and understanding how they work with scope and closures is essential for writing effective JavaScript.

## Function Declarations vs Expressions

A function declaration uses the \`function\` keyword and is hoisted (available before the line it's defined). A function expression assigns a function to a variable and is not hoisted. Arrow functions (\`=>\`) are a concise syntax for function expressions with one key difference: they don't have their own \`this\` binding, which makes them ideal for callbacks.

## Parameters and Arguments

Functions accept parameters (the names in the definition) and receive arguments (the values passed when called). JavaScript supports default parameters, rest parameters (\`...args\` collects remaining arguments into an array), and destructured parameters. Functions always return \`undefined\` unless you explicitly return a value.

## Scope

Scope determines where variables are accessible. JavaScript has three scope levels: global scope (accessible everywhere), function scope (variables declared with \`var\` inside a function), and block scope (variables declared with \`let\`/\`const\` inside curly braces). Inner scopes can access outer scopes, but not vice versa — this is called the scope chain.

## Closures

A closure is created when a function remembers variables from its outer scope even after the outer function has finished executing. This is one of JavaScript's most powerful features. Closures enable data privacy (variables that can't be accessed from outside), factory functions, and stateful callbacks. Every function in JavaScript forms a closure over its surrounding scope.

## Higher-Order Functions

A higher-order function either takes a function as an argument or returns a function. Array methods like \`map\`, \`filter\`, and \`reduce\` are higher-order functions. Understanding them is critical because they are the idiomatic way to work with data in JavaScript and especially in React.`,
    videos: [
      { title: "JavaScript Functions Crash Course", url: "https://www.youtube.com/watch?v=N8ap4k_1QEQ", duration: "32:00" },
      { title: "Closures Explained", url: "https://www.youtube.com/watch?v=vKJpN5FAeF4", duration: "12:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Function declaration (hoisted)
function greet(name) {
  return \`Hello, \${name}!\`;
}

// Arrow function (not hoisted)
const greetArrow = (name) => \`Hello, \${name}!\`;

// Default parameters
function createUser(name, role = "student", active = true) {
  return { name, role, active };
}

// Rest parameters
function sum(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}
console.log(sum(1, 2, 3, 4)); // 10

// Destructured parameters
function printUser({ name, age, city = "Unknown" }) {
  console.log(\`\${name}, \${age}, from \${city}\`);
}
printUser({ name: "Alex", age: 25 });

// CLOSURE: function remembers its outer scope
function createCounter(initial = 0) {
  let count = initial;  // Private variable!

  return {
    increment: () => ++count,
    decrement: () => --count,
    getCount: () => count,
  };
}

const counter = createCounter(10);
counter.increment();    // 11
counter.increment();    // 12
counter.decrement();    // 11
console.log(counter.getCount()); // 11
// count is NOT accessible directly — true encapsulation!

// Higher-order function
function withLogging(fn) {
  return function (...args) {
    console.log(\`Calling \${fn.name} with\`, args);
    const result = fn(...args);
    console.log(\`Result:\`, result);
    return result;
  };
}

const loggedSum = withLogging(sum);
loggedSum(1, 2, 3); // Logs call info, then returns 6`,
      },
    ],
    quiz: [
      {
        question: "What is a closure?",
        options: [
          "A way to close browser windows",
          "A function that remembers variables from its outer scope",
          "A method to end loops",
          "A type of error handling",
        ],
        correct: 1,
      },
      {
        question: "What is the key difference between arrow functions and regular functions?",
        options: [
          "Arrow functions are faster",
          "Arrow functions don't have their own 'this' binding",
          "Arrow functions can only return numbers",
          "Regular functions can't accept parameters",
        ],
        correct: 1,
      },
      {
        question: "What is a higher-order function?",
        options: [
          "A function defined at the top of the file",
          "A function that takes or returns another function",
          "A function with many parameters",
          "A function inside a class",
        ],
        correct: 1,
      },
    ],
  },

  "fe-12-1": {
    id: "fe-12-1",
    title: "Array Methods",
    content: `# JavaScript Array Methods

Arrays are ordered collections of values and one of the most-used data structures in JavaScript. Modern JavaScript provides a rich set of array methods that enable a functional, declarative programming style — especially important when working with React.

## Creating and Accessing Arrays

Arrays are created with brackets \`[]\` and can hold any mix of types. Access elements by zero-based index: \`arr[0]\`. Use \`.length\` to get the count. Destructuring lets you extract elements: \`const [first, second, ...rest] = arr\`. The spread operator \`[...arr]\` creates a shallow copy.

## Transforming Arrays: map, filter, reduce

\`map()\` creates a new array by transforming each element. \`filter()\` creates a new array with only elements that pass a test. \`reduce()\` accumulates all elements into a single value. These three methods are the foundation of functional data transformation in JavaScript. They never mutate the original array — they return new arrays.

## Searching: find, findIndex, includes, some, every

\`find()\` returns the first element matching a condition (or \`undefined\`). \`findIndex()\` returns its index (or -1). \`includes()\` checks if a value exists. \`some()\` checks if at least one element passes a test. \`every()\` checks if all elements pass a test.

## Modifying: push, pop, unshift, shift, splice, slice

\`push()\`/\`pop()\` add/remove from the end. \`unshift()\`/\`shift()\` add/remove from the beginning. \`splice()\` removes/replaces elements in place (mutating). \`slice()\` extracts a portion without mutating. In React and modern JS, prefer non-mutating approaches: use spread and filter instead of splice.

## Chaining Methods

Array methods return arrays (except reduce, find, etc.), so you can chain them: \`arr.filter(...).map(...).sort(...)\`. This creates readable data pipelines. Each step transforms the data further. Think of it as a production line where each method is a station that does one job.`,
    videos: [
      { title: "8 Must Know JavaScript Array Methods", url: "https://www.youtube.com/watch?v=R8rmfD9Y5-c", duration: "12:00" },
      { title: "JavaScript Array Methods Tutorial", url: "https://www.youtube.com/watch?v=rRgD1yVwIvE", duration: "33:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `const users = [
  { name: "Alice", age: 28, role: "developer" },
  { name: "Bob", age: 35, role: "designer" },
  { name: "Charlie", age: 22, role: "developer" },
  { name: "Diana", age: 31, role: "manager" },
];

// map — transform each element
const names = users.map(user => user.name);
// ["Alice", "Bob", "Charlie", "Diana"]

// filter — keep matching elements
const developers = users.filter(user => user.role === "developer");
// [{name: "Alice"...}, {name: "Charlie"...}]

// find — get first match
const bob = users.find(user => user.name === "Bob");
// {name: "Bob", age: 35, role: "designer"}

// some / every — test conditions
const hasManager = users.some(u => u.role === "manager"); // true
const allAdults = users.every(u => u.age >= 18);          // true

// reduce — accumulate to single value
const totalAge = users.reduce((sum, user) => sum + user.age, 0);
// 116

// Group by role using reduce
const grouped = users.reduce((groups, user) => {
  const key = user.role;
  groups[key] = groups[key] || [];
  groups[key].push(user);
  return groups;
}, {});

// Chaining — readable data pipelines
const seniorDevNames = users
  .filter(u => u.role === "developer")
  .filter(u => u.age >= 25)
  .map(u => u.name)
  .sort();
// ["Alice"]

// sort (mutates! Use spread to avoid)
const sorted = [...users].sort((a, b) => a.age - b.age);

// Flat and flatMap
const nested = [[1, 2], [3, 4], [5]];
const flat = nested.flat(); // [1, 2, 3, 4, 5]

const sentences = ["hello world", "foo bar"];
const words = sentences.flatMap(s => s.split(" "));
// ["hello", "world", "foo", "bar"]`,
      },
    ],
    quiz: [
      {
        question: "What does Array.map() return?",
        options: [
          "The original array, modified",
          "A single value",
          "A new array with transformed elements",
          "undefined",
        ],
        correct: 2,
      },
      {
        question: "Which method accumulates array elements into a single value?",
        options: ["map", "filter", "reduce", "find"],
        correct: 2,
      },
      {
        question: "Does sort() mutate the original array?",
        options: [
          "No, it returns a new array",
          "Yes, it modifies in place",
          "Only for numbers",
          "Only if you use a comparator",
        ],
        correct: 1,
      },
    ],
  },

  "fe-12-2": {
    id: "fe-12-2",
    title: "Object Patterns",
    content: `# JavaScript Object Patterns

Objects are key-value pairs and the most flexible data structure in JavaScript. Almost everything in JavaScript is an object — understanding object creation, manipulation, and common patterns is crucial for writing clean, maintainable code.

## Object Basics

Create objects with literal notation \`{}\`. Access properties with dot notation (\`obj.name\`) or bracket notation (\`obj["name"]\`) — bracket notation is needed for dynamic keys and keys with special characters. Use \`delete obj.prop\` to remove properties, and \`"prop" in obj\` or \`obj.hasOwnProperty("prop")\` to check existence.

## Destructuring and Spread

Object destructuring extracts properties into variables: \`const { name, age } = user\`. You can rename (\`{ name: userName }\`), set defaults (\`{ role = "user" }\`), and nest (\`{ address: { city } }\`). The spread operator \`{ ...obj }\` creates a shallow copy and is perfect for merging objects or adding/overriding properties immutably.

## Computed Properties and Shorthand

ES6 introduced property shorthand: when the variable name matches the key, \`{ name }\` is equivalent to \`{ name: name }\`. Computed property names use brackets: \`{ [dynamicKey]: value }\`. These features make object creation cleaner and more flexible.

## Object Methods

\`Object.keys()\` returns an array of keys. \`Object.values()\` returns values. \`Object.entries()\` returns \`[key, value]\` pairs — perfect for iterating with \`for...of\` or converting to a Map. \`Object.assign()\` merges objects (prefer spread syntax). \`Object.freeze()\` makes an object immutable (shallow).

## Common Patterns

The factory pattern uses functions that return objects. The module pattern uses closures to create private state. The builder pattern uses method chaining. In modern JavaScript and especially React, the most important pattern is immutable updates — never mutating objects directly but creating new ones with the spread operator. This is the foundation of React state management.`,
    videos: [
      { title: "JavaScript Object Fundamentals", url: "https://www.youtube.com/watch?v=BRN_UoUYpHY", duration: "11:00" },
      { title: "Object Destructuring in JavaScript", url: "https://www.youtube.com/watch?v=NIq3qLaHCIs", duration: "14:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Object basics
const user = {
  name: "Alice",
  age: 28,
  address: { city: "NYC", zip: "10001" },
  hobbies: ["coding", "reading"],
};

// Destructuring
const { name, age, address: { city } } = user;
console.log(name, city); // "Alice" "NYC"

// Destructuring with rename and default
const { name: userName, role = "member" } = user;

// Spread — immutable updates (crucial for React!)
const updatedUser = {
  ...user,
  age: 29,                  // Override existing
  email: "alice@example.com", // Add new property
};
// user.age is still 28 — original unchanged

// Nested immutable update
const movedUser = {
  ...user,
  address: { ...user.address, city: "LA" },
};

// Computed property names
const field = "email";
const data = { [field]: "alice@test.com" }; // { email: "alice@test.com" }

// Object methods
console.log(Object.keys(user));    // ["name", "age", "address", "hobbies"]
console.log(Object.values(user));  // ["Alice", 28, {...}, [...]]
console.log(Object.entries(user)); // [["name","Alice"], ["age",28], ...]

// Iterating over object entries
for (const [key, value] of Object.entries(user)) {
  console.log(\`\${key}: \${value}\`);
}

// Factory pattern
function createProduct(name, price) {
  return {
    name,
    price,
    discount(percent) {
      return { ...this, price: this.price * (1 - percent / 100) };
    },
    toString() {
      return \`\${this.name}: $\${this.price.toFixed(2)}\`;
    },
  };
}

const laptop = createProduct("Laptop", 999);
const discounted = laptop.discount(10);
console.log(discounted.toString()); // "Laptop: $899.10"`,
      },
    ],
    quiz: [
      {
        question: "How do you create an immutable update of an object in JavaScript?",
        options: [
          "Directly modify the property",
          "Use Object.freeze()",
          "Use spread operator to create a new object with changes",
          "Use Object.assign() on the same object",
        ],
        correct: 2,
      },
      {
        question: "What does Object.entries() return?",
        options: [
          "An array of keys",
          "An array of values",
          "An array of [key, value] pairs",
          "The number of properties",
        ],
        correct: 2,
      },
    ],
  },

  "fe-13-1": {
    id: "fe-13-1",
    title: "DOM API",
    content: `# DOM Manipulation

The Document Object Model (DOM) is the browser's representation of an HTML page as a tree of objects. JavaScript can read, modify, add, and remove elements from this tree, making web pages dynamic and interactive. Understanding the DOM is essential even when using frameworks like React.

## Selecting Elements

The DOM provides several methods to find elements: \`document.getElementById()\` returns a single element by its ID. \`document.querySelector()\` returns the first element matching a CSS selector. \`document.querySelectorAll()\` returns a NodeList of all matches (use \`Array.from()\` or spread to convert it to an array for array methods). Modern code almost exclusively uses \`querySelector\` and \`querySelectorAll\`.

## Modifying Content and Attributes

\`element.textContent\` gets or sets an element's text. \`element.innerHTML\` gets or sets HTML content (be careful — it can introduce XSS vulnerabilities with user input). \`element.setAttribute()\`, \`element.getAttribute()\`, and \`element.removeAttribute()\` manage attributes. The \`classList\` API provides \`add()\`, \`remove()\`, \`toggle()\`, and \`contains()\` for CSS class management. \`element.style\` provides direct access to inline styles.

## Creating and Removing Elements

\`document.createElement()\` creates a new element in memory. Set its properties and content, then use \`parent.appendChild()\` or \`parent.append()\` to add it to the DOM. \`parent.insertBefore()\` inserts at a specific position. \`element.remove()\` removes an element from the DOM. For bulk changes, use a \`DocumentFragment\` to batch insertions and minimize reflows.

## Event Handling

\`element.addEventListener(type, handler)\` is the standard way to listen for events. Common events include \`click\`, \`input\`, \`submit\`, \`keydown\`, \`mouseover\`, \`focus\`, \`blur\`, and \`scroll\`. The event object passed to handlers contains useful information like \`event.target\` (the element that triggered the event), \`event.preventDefault()\` (stops default behavior like form submission), and \`event.stopPropagation()\` (stops event bubbling).

## Event Delegation

Instead of adding event listeners to many child elements, add one listener to a parent and check \`event.target\`. This is called event delegation — it's more efficient (fewer listeners), handles dynamically added elements automatically, and is the pattern React uses internally for all event handling.`,
    videos: [
      { title: "DOM Manipulation Crash Course", url: "https://www.youtube.com/watch?v=5fb2aPlgoys", duration: "40:00" },
      { title: "Learn DOM Manipulation In 18 Minutes", url: "https://www.youtube.com/watch?v=y17RuWkWdn8", duration: "18:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Selecting elements
const title = document.getElementById("title");
const button = document.querySelector(".submit-btn");
const cards = document.querySelectorAll(".card");
const allCards = [...document.querySelectorAll(".card")]; // Convert to array

// Modifying content
title.textContent = "New Title";
title.innerHTML = "New <em>Title</em>"; // Use carefully

// Managing classes
button.classList.add("active", "primary");
button.classList.remove("disabled");
button.classList.toggle("dark-mode");
const isActive = button.classList.contains("active");

// Modifying styles
button.style.backgroundColor = "#3b82f6";
button.style.padding = "12px 24px";

// Creating elements
const card = document.createElement("div");
card.className = "card";
card.innerHTML = \`
  <h3>New Card</h3>
  <p>Card content here</p>
\`;
document.querySelector(".container").appendChild(card);

// Removing elements
card.remove();

// Event handling
button.addEventListener("click", (event) => {
  event.preventDefault();
  console.log("Button clicked!", event.target);
});

// Form submission
const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const data = Object.fromEntries(formData);
  console.log(data); // { name: "...", email: "..." }
});

// Event delegation
document.querySelector(".card-list").addEventListener("click", (e) => {
  const card = e.target.closest(".card");
  if (!card) return;

  const cardId = card.dataset.id;
  console.log("Clicked card:", cardId);
});

// Keyboard events
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeModal();
  }
  if (e.key === "s" && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    saveDocument();
  }
});`,
      },
    ],
    quiz: [
      {
        question: "What is event delegation?",
        options: [
          "Assigning events to every child element",
          "Adding one listener to a parent to handle events from children",
          "Removing all event listeners",
          "Delegating events to a web worker",
        ],
        correct: 1,
      },
      {
        question: "What does event.preventDefault() do?",
        options: [
          "Prevents the event from firing",
          "Stops the browser's default action (like form submission)",
          "Removes the event listener",
          "Prevents the page from loading",
        ],
        correct: 1,
      },
      {
        question: "Which method returns ALL matching elements?",
        options: ["getElementById", "querySelector", "querySelectorAll", "getElementsByTag"],
        correct: 2,
      },
    ],
  },

  "fe-14-1": {
    id: "fe-14-1",
    title: "Promises & Async/Await",
    content: `# Promises and Async/Await

JavaScript is single-threaded, meaning it can only do one thing at a time. But web applications constantly need to wait for things — network requests, file reads, timers. Asynchronous programming lets JavaScript start these operations and continue executing other code while waiting for results.

## The Problem with Callbacks

Before Promises, asynchronous code used callbacks — functions passed as arguments to be called when an operation completes. This led to "callback hell" where deeply nested callbacks became unreadable and hard to debug. Error handling was particularly messy, requiring error checks at every level.

## Promises

A Promise is an object representing the eventual completion or failure of an asynchronous operation. It has three states: pending (initial), fulfilled (completed successfully), and rejected (failed). You create a Promise with \`new Promise((resolve, reject) => {...})\` and consume it with \`.then()\` for success and \`.catch()\` for errors. Promises chain naturally — each \`.then()\` returns a new Promise.

## Async/Await

\`async/await\` is syntactic sugar over Promises that makes asynchronous code read like synchronous code. Mark a function as \`async\` and use \`await\` before any Promise to pause execution until it resolves. This eliminates \`.then()\` chains and makes code dramatically more readable. Error handling uses familiar \`try/catch\` blocks.

## Promise Utilities

\`Promise.all()\` runs multiple Promises in parallel and waits for all to complete (fails fast if any rejects). \`Promise.allSettled()\` waits for all to complete regardless of success/failure. \`Promise.race()\` returns the result of the first Promise to settle. These are essential for optimizing performance when you have multiple independent async operations.

## Error Handling Patterns

Always handle errors in async code. With \`.catch()\`, chain it at the end of a Promise chain. With \`async/await\`, wrap awaited calls in \`try/catch\`. For unhandled rejections, listen to the global \`unhandledrejection\` event. Never ignore errors — at minimum, log them.`,
    videos: [
      { title: "JavaScript Promises In 10 Minutes", url: "https://www.youtube.com/watch?v=DHvZLI7Db8E", duration: "11:00" },
      { title: "Async Await in JavaScript", url: "https://www.youtube.com/watch?v=V_Kr9OSfDeU", duration: "8:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Creating a Promise
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Using .then() / .catch()
wait(1000)
  .then(() => console.log("1 second passed"))
  .catch(err => console.error(err));

// Async/Await — much cleaner!
async function demo() {
  try {
    await wait(1000);
    console.log("1 second passed");

    const response = await fetch("https://api.example.com/users");
    if (!response.ok) throw new Error(\`HTTP \${response.status}\`);
    const users = await response.json();
    console.log(users);
  } catch (error) {
    console.error("Something failed:", error.message);
  }
}

// Promise.all — run in parallel
async function loadDashboard() {
  const [users, posts, comments] = await Promise.all([
    fetch("/api/users").then(r => r.json()),
    fetch("/api/posts").then(r => r.json()),
    fetch("/api/comments").then(r => r.json()),
  ]);
  // All three requests ran simultaneously!
  return { users, posts, comments };
}

// Promise.allSettled — don't fail fast
async function loadWithFallbacks() {
  const results = await Promise.allSettled([
    fetch("/api/primary"),
    fetch("/api/secondary"),
  ]);

  results.forEach((result, i) => {
    if (result.status === "fulfilled") {
      console.log(\`Request \${i} succeeded\`);
    } else {
      console.log(\`Request \${i} failed: \${result.reason}\`);
    }
  });
}

// Practical pattern: async function with loading state
async function fetchData(url) {
  let loading = true;
  let data = null;
  let error = null;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to fetch");
    data = await response.json();
  } catch (e) {
    error = e.message;
  } finally {
    loading = false;
  }

  return { data, error, loading };
}`,
      },
    ],
    quiz: [
      {
        question: "What are the three states of a Promise?",
        options: [
          "Start, middle, end",
          "Pending, fulfilled, rejected",
          "Loading, success, error",
          "Open, closed, cancelled",
        ],
        correct: 1,
      },
      {
        question: "What does Promise.all() do if one Promise rejects?",
        options: [
          "Waits for all to finish anyway",
          "Ignores the rejection",
          "Rejects immediately with that error",
          "Retries the failed Promise",
        ],
        correct: 2,
      },
      {
        question: "What does the 'await' keyword do?",
        options: [
          "Makes the function synchronous",
          "Pauses execution until the Promise resolves",
          "Creates a new thread",
          "Cancels the Promise",
        ],
        correct: 1,
      },
    ],
  },

  "fe-14-2": {
    id: "fe-14-2",
    title: "Fetch API",
    content: `# The Fetch API

The Fetch API is the modern standard for making HTTP requests in JavaScript. It replaces the older XMLHttpRequest (XHR) with a cleaner, Promise-based interface. Whether you're loading data from an API, submitting forms, or uploading files, Fetch is the tool you'll use.

## Basic GET Requests

\`fetch(url)\` makes a GET request and returns a Promise that resolves to a Response object. The Response has methods to parse the body: \`.json()\` for JSON data, \`.text()\` for plain text, \`.blob()\` for binary data. Important: Fetch only rejects on network failures, not on HTTP errors (404, 500). You must check \`response.ok\` or \`response.status\` manually.

## POST and Other Methods

To make POST, PUT, DELETE, or PATCH requests, pass an options object as the second argument. Specify the \`method\`, \`headers\` (usually \`Content-Type\`), and \`body\` (usually \`JSON.stringify()\` for JSON data). For file uploads, use \`FormData\` as the body and let the browser set the Content-Type automatically.

## Headers and Authentication

The \`Headers\` object or a plain object sets request headers. Common headers include \`Content-Type\`, \`Authorization\` (for Bearer tokens), and \`Accept\`. For APIs requiring authentication, include the token in the Authorization header: \`Authorization: Bearer <token>\`.

## Error Handling and Timeouts

Since Fetch doesn't reject on HTTP errors, create a wrapper function that throws on non-OK responses. Fetch also doesn't have a built-in timeout — use \`AbortController\` to cancel requests after a timeout. Always handle both network errors and HTTP errors gracefully.

## Practical Patterns

In real applications, create a base API service that handles authentication, base URL, error handling, and response parsing. This avoids repeating the same configuration for every request. Libraries like Axios provide these features out of the box, but understanding raw Fetch is essential.`,
    videos: [
      { title: "JavaScript Fetch API Tutorial", url: "https://www.youtube.com/watch?v=cuEtnrL9-H0", duration: "30:00" },
      { title: "Fetch API Explained", url: "https://www.youtube.com/watch?v=-ZI0ea5O2oA", duration: "5:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Basic GET request
async function getUsers() {
  const response = await fetch("https://jsonplaceholder.typicode.com/users");

  if (!response.ok) {
    throw new Error(\`HTTP Error: \${response.status}\`);
  }

  return response.json();
}

// POST request with JSON body
async function createPost(title, body) {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, body, userId: 1 }),
  });

  if (!response.ok) throw new Error("Failed to create post");
  return response.json();
}

// DELETE request
async function deletePost(id) {
  const response = await fetch(\`https://api.example.com/posts/\${id}\`, {
    method: "DELETE",
    headers: {
      Authorization: \`Bearer \${getToken()}\`,
    },
  });
  return response.ok;
}

// File upload with FormData
async function uploadAvatar(file) {
  const formData = new FormData();
  formData.append("avatar", file);

  const response = await fetch("/api/upload", {
    method: "POST",
    body: formData, // Don't set Content-Type — browser handles it
  });

  return response.json();
}

// Timeout with AbortController
async function fetchWithTimeout(url, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, { signal: controller.signal });
    return response.json();
  } catch (error) {
    if (error.name === "AbortError") {
      throw new Error("Request timed out");
    }
    throw error;
  } finally {
    clearTimeout(timeoutId);
  }
}

// Reusable API service
const api = {
  baseURL: "https://api.example.com",

  async request(endpoint, options = {}) {
    const response = await fetch(\`\${this.baseURL}\${endpoint}\`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: \`Bearer \${localStorage.getItem("token")}\`,
        ...options.headers,
      },
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.message || \`HTTP \${response.status}\`);
    }

    return response.json();
  },

  get: (endpoint) => api.request(endpoint),
  post: (endpoint, data) => api.request(endpoint, { method: "POST", body: JSON.stringify(data) }),
  put: (endpoint, data) => api.request(endpoint, { method: "PUT", body: JSON.stringify(data) }),
  delete: (endpoint) => api.request(endpoint, { method: "DELETE" }),
};`,
      },
    ],
    quiz: [
      {
        question: "Does fetch() reject on HTTP 404 or 500 errors?",
        options: [
          "Yes, it always rejects on errors",
          "No, it only rejects on network failures",
          "Only on 500 errors",
          "Only when using POST",
        ],
        correct: 1,
      },
      {
        question: "How do you send JSON data in a POST request?",
        options: [
          "Pass the object directly as body",
          "Use JSON.stringify() on the body and set Content-Type to application/json",
          "Use FormData",
          "Append to the URL as query parameters",
        ],
        correct: 1,
      },
    ],
  },

  "fe-15-1": {
    id: "fe-15-1",
    title: "Modern JS Features",
    content: `# ES6+ Modern JavaScript Features

ES6 (2015) and subsequent versions transformed JavaScript from a quirky scripting language into a modern, expressive programming language. These features are used everywhere in professional JavaScript and React development.

## Destructuring

Destructuring extracts values from arrays and objects into individual variables. Array destructuring uses position: \`const [a, b] = [1, 2]\`. Object destructuring uses keys: \`const { name, age } = user\`. You can set defaults, rename variables, and use rest patterns. Destructuring is especially common in React for props, state, and hook returns.

## Spread and Rest Operators

The spread operator (\`...\`) expands an iterable: \`[...arr1, ...arr2]\` merges arrays, \`{ ...obj1, ...obj2 }\` merges objects. The rest operator (same syntax) collects remaining items: \`const [first, ...rest] = arr\`. These are fundamental for immutable data operations in React.

## Template Literals

Template literals (backticks) support embedded expressions \`\${expr}\`, multi-line strings, and tagged templates. They eliminate awkward string concatenation and make dynamic strings readable. Tagged templates are used by libraries like styled-components.

## Modules (import/export)

ES modules use \`export\` and \`import\` to share code between files. Named exports (\`export function foo()\`) can have many per file. Default exports (\`export default class App\`) have one per file. This module system enables code splitting, tree shaking (removing unused code), and organized codebases.

## Optional Chaining and Nullish Coalescing

Optional chaining (\`?.\`) safely accesses nested properties without throwing if an intermediate value is null/undefined: \`user?.address?.city\`. Nullish coalescing (\`??\`) provides a fallback only for null/undefined (not for falsy values like 0 or ""). Together, they dramatically simplify defensive coding.

## Other Essential Features

\`Map\` and \`Set\` provide better alternatives to objects and arrays for certain use cases. \`for...of\` iterates values directly. \`Symbol\` creates unique identifiers. \`Proxy\` intercepts object operations (used internally by Vue and MobX). \`WeakMap\`/\`WeakSet\` allow garbage-collected keys. \`Array.from()\` converts iterables to arrays. \`Object.fromEntries()\` converts entries back to objects.`,
    videos: [
      { title: "ES6 JavaScript Features", url: "https://www.youtube.com/watch?v=NCwa_xi0Uuc", duration: "12:00" },
      { title: "JavaScript ES6 Modules", url: "https://www.youtube.com/watch?v=cRHQNNcYf6s", duration: "16:00" },
    ],
    codeExamples: [
      {
        language: "javascript",
        code: `// Destructuring
const { name, age, ...rest } = { name: "Alice", age: 28, role: "dev", city: "NYC" };
// name="Alice", age=28, rest={role:"dev", city:"NYC"}

const [first, , third] = [10, 20, 30];
// first=10, third=30 (skip second with empty comma)

// Nested destructuring with defaults
const { settings: { theme = "light", lang = "en" } = {} } = userConfig;

// Spread — immutable operations
const newArr = [...oldArr, newItem];
const withoutItem = arr.filter(item => item.id !== idToRemove);
const updatedObj = { ...oldObj, updatedProp: newValue };

// ES Modules
// math.js
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default class Calculator { /* ... */ }

// app.js
import Calculator, { PI, add } from "./math.js";

// Optional chaining
const street = user?.address?.street; // undefined if any is null
const first = arr?.[0];               // undefined if arr is null
const result = obj?.method?.();        // undefined if method doesn't exist

// Nullish coalescing
const port = config.port ?? 3000;   // 3000 only if port is null/undefined
const count = data.count ?? 0;       // 0 only if count is null/undefined
// Note: 0 ?? 5 = 0  (0 is not null/undefined)
// But:  0 || 5 = 5  (0 is falsy)

// Map and Set
const map = new Map();
map.set("key", "value");
map.set(42, "number key");
console.log(map.get("key")); // "value"
console.log(map.size);       // 2

const set = new Set([1, 2, 3, 2, 1]);
console.log([...set]); // [1, 2, 3] — unique values

// Practical: remove duplicates
const unique = [...new Set(arrayWithDupes)];

// Promise-based dynamic import (code splitting)
const module = await import("./heavyModule.js");
module.doSomething();`,
      },
    ],
    quiz: [
      {
        question: "What is the difference between ?? and ||?",
        options: [
          "They are identical",
          "?? only falls back on null/undefined; || falls back on any falsy value",
          "|| is for strings, ?? is for numbers",
          "?? is deprecated",
        ],
        correct: 1,
      },
      {
        question: "What does optional chaining (?.) do when it encounters null?",
        options: [
          "Throws an error",
          "Returns null",
          "Returns undefined",
          "Skips to the next line",
        ],
        correct: 2,
      },
      {
        question: "How many default exports can a module have?",
        options: ["Unlimited", "One", "Two", "None"],
        correct: 1,
      },
    ],
  },

  "fe-16-1": {
    id: "fe-16-1",
    title: "JSX & Components",
    content: `# JSX and React Components

React is a JavaScript library for building user interfaces. It introduced a component-based architecture that revolutionized frontend development. Components are reusable, self-contained pieces of UI, and JSX is the syntax that makes writing them intuitive.

## What is JSX?

JSX (JavaScript XML) lets you write HTML-like syntax directly in JavaScript. It looks like HTML but gets compiled to \`React.createElement()\` calls. JSX expressions must have a single root element (use a fragment \`<></>\` if you don't want an extra div). JavaScript expressions are embedded with curly braces \`{}\`.

## Key JSX Rules

JSX has a few differences from HTML: use \`className\` instead of \`class\` (because \`class\` is a reserved word in JS), \`htmlFor\` instead of \`for\`, camelCase for event handlers (\`onClick\`, not \`onclick\`), and self-close tags that have no children (\`<img />\`, \`<input />\`). All JSX must be closed — \`<br>\` is invalid, use \`<br />\`.

## Function Components

Modern React uses function components — plain JavaScript functions that return JSX. The function name must start with an uppercase letter. Components receive data through \`props\` (an object of all passed attributes). Components are the building blocks of React apps — everything from a small button to an entire page is a component.

## Component Composition

The real power of components comes from composition — combining simple components to build complex UIs. A Card component might contain a Title component and a Button component. The \`children\` prop passes JSX nested between opening and closing tags, enabling wrapper and layout components.

## Conditional Rendering and Lists

JSX supports conditional rendering with ternary operators (\`condition ? <A /> : <B />\`), logical AND (\`condition && <A />\`), or early returns. For lists, use \`array.map()\` to render arrays of components. Each item in a list must have a unique \`key\` prop — this helps React efficiently update the DOM.`,
    videos: [
      { title: "React Tutorial for Beginners", url: "https://www.youtube.com/watch?v=SqcY0GlETPk", duration: "1:20:00" },
      { title: "React Components Explained", url: "https://www.youtube.com/watch?v=Y2hgEGPzTZY", duration: "12:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `// Basic function component
function Welcome() {
  return <h1>Hello, React!</h1>;
}

// Component with props
interface UserCardProps {
  name: string;
  role: string;
  avatar?: string;
}

function UserCard({ name, role, avatar }: UserCardProps) {
  return (
    <div className="user-card">
      {avatar && <img src={avatar} alt={name} />}
      <h3>{name}</h3>
      <span className="role">{role}</span>
    </div>
  );
}

// Component composition with children
function Card({ children, title }: { children: React.ReactNode; title: string }) {
  return (
    <div className="card">
      <h2 className="card-title">{title}</h2>
      <div className="card-body">{children}</div>
    </div>
  );
}

// Usage: composition
function App() {
  return (
    <Card title="Team Members">
      <UserCard name="Alice" role="Developer" />
      <UserCard name="Bob" role="Designer" />
    </Card>
  );
}

// Conditional rendering
function StatusBadge({ isOnline }: { isOnline: boolean }) {
  return (
    <span className={isOnline ? "badge-green" : "badge-gray"}>
      {isOnline ? "Online" : "Offline"}
    </span>
  );
}

// Rendering lists with keys
interface Todo {
  id: number;
  text: string;
  done: boolean;
}

function TodoList({ todos }: { todos: Todo[] }) {
  if (todos.length === 0) {
    return <p>No todos yet!</p>;
  }

  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id} className={todo.done ? "done" : ""}>
          {todo.text}
        </li>
      ))}
    </ul>
  );
}`,
      },
    ],
    quiz: [
      {
        question: "Why do list items in React need a 'key' prop?",
        options: [
          "For CSS styling",
          "To help React efficiently identify and update changed items",
          "To set the item's index",
          "It's optional",
        ],
        correct: 1,
      },
      {
        question: "Why does JSX use 'className' instead of 'class'?",
        options: [
          "It's a React convention",
          "Because 'class' is a reserved word in JavaScript",
          "className is faster",
          "HTML doesn't support 'class'",
        ],
        correct: 1,
      },
      {
        question: "What must a React component name start with?",
        options: ["Lowercase letter", "Uppercase letter", "An underscore", "The word 'React'"],
        correct: 1,
      },
    ],
  },

  "fe-16-2": {
    id: "fe-16-2",
    title: "Props & Rendering",
    content: `# Props and Rendering in React

Props (short for properties) are React's mechanism for passing data from parent components to child components. Understanding how props flow and how React decides when to re-render is fundamental to building efficient React applications.

## Props Are Read-Only

Props flow in one direction: parent to child. A component must never modify its own props — they are immutable from the receiving component's perspective. If a child needs to communicate back to the parent, the parent passes a callback function as a prop. This unidirectional data flow makes applications predictable and easier to debug.

## Passing Different Data Types

Props can be any JavaScript value: strings, numbers, booleans, arrays, objects, functions, and even other components. String props can use quotes; all other types use curly braces. Boolean props can be passed as just the name (presence = true, absence = false): \`<Button disabled>\` is equivalent to \`<Button disabled={true}>\`.

## Default Props and Destructuring

Use JavaScript default parameters in the function signature to set default prop values: \`function Button({ variant = "primary", size = "md" })\`. This is cleaner than the older \`defaultProps\` static property. Always destructure props in the function signature — it makes it clear what props a component accepts.

## The React Rendering Process

React renders in two phases: the render phase (calls your component functions to produce JSX) and the commit phase (applies changes to the actual DOM). A re-render happens when: state changes, props change, or the parent re-renders. React uses a virtual DOM diffing algorithm to minimize actual DOM updates — only changed elements get updated.

## Performance: Avoiding Unnecessary Re-renders

When a parent re-renders, all its children re-render by default (even if their props haven't changed). \`React.memo()\` wraps a component to skip re-renders when props are shallowly equal. However, premature optimization is an anti-pattern — only use memo when you've measured a performance problem. Profile first, optimize second.`,
    videos: [
      { title: "React Props Explained", url: "https://www.youtube.com/watch?v=PHaECbrKgs0", duration: "11:00" },
      { title: "How React Rendering Works", url: "https://www.youtube.com/watch?v=7YhdqIR2Yzo", duration: "12:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `// Props with TypeScript interface
interface ButtonProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  onClick?: () => void;
}

function Button({
  children,
  variant = "primary",
  size = "md",
  disabled = false,
  onClick,
}: ButtonProps) {
  return (
    <button
      className={\`btn btn-\${variant} btn-\${size}\`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

// Usage with different prop types
function App() {
  return (
    <div>
      <Button onClick={() => alert("Clicked!")}>Click Me</Button>
      <Button variant="danger" size="lg">Delete</Button>
      <Button disabled>Disabled Button</Button>
    </div>
  );
}

// Passing callbacks — child communicates to parent
interface SearchBarProps {
  onSearch: (query: string) => void;
  placeholder?: string;
}

function SearchBar({ onSearch, placeholder = "Search..." }: SearchBarProps) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query);  // Call parent's function
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder={placeholder}
      />
    </form>
  );
}

// Parent using the callback
function SearchPage() {
  const [results, setResults] = useState([]);

  const handleSearch = async (query: string) => {
    const data = await fetchResults(query);
    setResults(data);
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <ResultsList results={results} />
    </div>
  );
}

// React.memo — skip re-renders when props haven't changed
const ExpensiveList = React.memo(function ExpensiveList({ items }: { items: Item[] }) {
  console.log("Rendering ExpensiveList");
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
});`,
      },
    ],
    quiz: [
      {
        question: "In which direction do props flow in React?",
        options: [
          "Child to parent",
          "Parent to child (unidirectional)",
          "Both directions",
          "Between siblings",
        ],
        correct: 1,
      },
      {
        question: "When does a React component re-render?",
        options: [
          "Only when props change",
          "Only when state changes",
          "When state changes, props change, or parent re-renders",
          "Every second automatically",
        ],
        correct: 2,
      },
    ],
  },

  "fe-17-1": {
    id: "fe-17-1",
    title: "useState & Events",
    content: `# useState and Event Handling

State is data that changes over time and drives what the UI displays. The \`useState\` hook is React's primary tool for adding interactive state to function components. Combined with event handling, it enables truly dynamic user interfaces.

## The useState Hook

\`useState\` returns an array with two elements: the current state value and a function to update it. You call it at the top level of your component (never inside conditions or loops). The argument is the initial value. The naming convention uses \`[value, setValue]\` — a pair of the noun and its setter.

## Updating State

State updates are asynchronous — calling \`setValue(newValue)\` doesn't immediately change \`value\`. React batches updates and re-renders after the current event handler finishes. When the new state depends on the previous state, use the functional form: \`setCount(prev => prev + 1)\`. This ensures you always work with the latest value, even in rapid updates.

## State with Objects and Arrays

For objects and arrays, never mutate directly. Always create new references using spread: \`setUser({ ...user, name: "New" })\` or \`setItems([...items, newItem])\`. This is because React uses reference equality to detect changes — mutating an object doesn't create a new reference, so React won't re-render.

## Event Handling in React

React uses synthetic events — a cross-browser wrapper around native DOM events. Event handlers are passed as camelCase props: \`onClick\`, \`onChange\`, \`onSubmit\`, \`onKeyDown\`. The handler receives a SyntheticEvent object. For forms, \`onChange\` fires on every keystroke (unlike native HTML where it fires on blur).

## Controlled Components

In a controlled component, form input values are driven by React state. The input's \`value\` is bound to state, and \`onChange\` updates the state. This gives React full control over the form data, making it easy to validate, transform, or submit. Controlled components are the recommended pattern for forms in React.`,
    videos: [
      { title: "React useState Hook", url: "https://www.youtube.com/watch?v=O6P86uwfdR0", duration: "12:00" },
      { title: "React Events & Forms", url: "https://www.youtube.com/watch?v=dH6i3GurZW8", duration: "20:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `import { useState } from "react";

// Basic counter
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>+1</button>
      <button onClick={() => setCount(prev => prev - 1)}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

// Controlled form inputs
function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (!email || !password) {
      setError("All fields are required");
      return;
    }

    console.log("Logging in:", { email, password });
  };

  return (
    <form onSubmit={handleSubmit}>
      {error && <div className="error">{error}</div>}

      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />

      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />

      <button type="submit">Log In</button>
    </form>
  );
}

// State with objects — immutable updates
interface Profile {
  name: string;
  bio: string;
  social: { twitter: string; github: string };
}

function ProfileEditor() {
  const [profile, setProfile] = useState<Profile>({
    name: "",
    bio: "",
    social: { twitter: "", github: "" },
  });

  const updateField = (field: keyof Profile, value: string) => {
    setProfile(prev => ({ ...prev, [field]: value }));
  };

  const updateSocial = (field: keyof Profile["social"], value: string) => {
    setProfile(prev => ({
      ...prev,
      social: { ...prev.social, [field]: value },
    }));
  };

  return (
    <div>
      <input value={profile.name} onChange={e => updateField("name", e.target.value)} />
      <input value={profile.social.twitter} onChange={e => updateSocial("twitter", e.target.value)} />
    </div>
  );
}

// State with arrays
function TodoApp() {
  const [todos, setTodos] = useState<{ id: number; text: string; done: boolean }[]>([]);
  const [input, setInput] = useState("");

  const addTodo = () => {
    if (!input.trim()) return;
    setTodos(prev => [...prev, { id: Date.now(), text: input, done: false }]);
    setInput("");
  };

  const toggleTodo = (id: number) => {
    setTodos(prev => prev.map(t => t.id === id ? { ...t, done: !t.done } : t));
  };

  const deleteTodo = (id: number) => {
    setTodos(prev => prev.filter(t => t.id !== id));
  };

  return (
    <div>
      <input value={input} onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === "Enter" && addTodo()} />
      <button onClick={addTodo}>Add</button>
      {todos.map(todo => (
        <div key={todo.id}>
          <span onClick={() => toggleTodo(todo.id)}
            style={{ textDecoration: todo.done ? "line-through" : "none" }}>
            {todo.text}
          </span>
          <button onClick={() => deleteTodo(todo.id)}>X</button>
        </div>
      ))}
    </div>
  );
}`,
      },
    ],
    quiz: [
      {
        question: "Why should you use setCount(prev => prev + 1) instead of setCount(count + 1)?",
        options: [
          "It's faster",
          "It ensures you use the latest state value when updates are batched",
          "It's required by TypeScript",
          "There's no difference",
        ],
        correct: 1,
      },
      {
        question: "What happens if you mutate state directly (e.g., state.push(item))?",
        options: [
          "React re-renders immediately",
          "React won't detect the change and won't re-render",
          "It throws an error",
          "It works fine in React",
        ],
        correct: 1,
      },
      {
        question: "What makes a form input a 'controlled component'?",
        options: [
          "It has a name attribute",
          "Its value is driven by React state and updated via onChange",
          "It's wrapped in a form tag",
          "It uses the ref attribute",
        ],
        correct: 1,
      },
    ],
  },

  "fe-18-1": {
    id: "fe-18-1",
    title: "useEffect",
    content: `# The useEffect Hook

\`useEffect\` lets you perform side effects in function components. Side effects are anything that reaches outside the component: fetching data, setting up subscriptions, manually changing the DOM, or setting timers. It replaces the lifecycle methods of class components (\`componentDidMount\`, \`componentDidUpdate\`, \`componentWillUnmount\`).

## Basic useEffect

\`useEffect\` takes two arguments: a function to run (the effect) and an optional dependency array. The effect runs after React commits changes to the DOM. The dependency array tells React when to re-run the effect — only when one of the listed values changes.

## Dependency Array Rules

An empty array \`[]\` means the effect runs once after the initial render (like \`componentDidMount\`). No array means it runs after every render. A filled array \`[dep1, dep2]\` means it runs when any dependency changes. Always include all variables from the component scope that the effect uses — the ESLint plugin \`react-hooks/exhaustive-deps\` enforces this.

## Cleanup Functions

The effect function can return a cleanup function. This cleanup runs before the effect re-runs and when the component unmounts. Use it to clean up subscriptions, timers, event listeners, or abort pending requests. Forgetting cleanup is a common source of memory leaks and bugs.

## Common Patterns

Data fetching is the most common useEffect pattern: fetch data when the component mounts or when a dependency changes, store it in state. Event listeners that need to attach to the window or document should be set up in useEffect with cleanup. Debouncing user input (like search-as-you-type) uses useEffect with a timer and cleanup.

## Pitfalls

Avoid infinite loops by ensuring the dependency array is correct — if your effect updates a state value that's in the dependency array, you'll loop forever. Don't use \`useEffect\` for things that can be calculated during rendering — derive values directly in the component body instead. useEffect is for synchronizing with external systems, not for transforming data.`,
    videos: [
      { title: "React useEffect Hook Explained", url: "https://www.youtube.com/watch?v=0ZJgIjIuY7U", duration: "13:00" },
      { title: "useEffect Complete Guide", url: "https://www.youtube.com/watch?v=QQYeipc_cik", duration: "20:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `import { useState, useEffect } from "react";

// Fetch data on mount
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false; // Prevent setting state after unmount

    async function fetchUser() {
      setLoading(true);
      setError(null);

      try {
        const res = await fetch(\`/api/users/\${userId}\`);
        if (!res.ok) throw new Error("Failed to fetch");
        const data = await res.json();

        if (!cancelled) {
          setUser(data);
        }
      } catch (e) {
        if (!cancelled) {
          setError(e.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    fetchUser();

    return () => { cancelled = true; }; // Cleanup
  }, [userId]); // Re-run when userId changes

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div>{user?.name}</div>;
}

// Window event listener with cleanup
function WindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    const handleResize = () => {
      setSize({ width: window.innerWidth, height: window.innerHeight });
    };

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []); // Empty array — set up once, clean up on unmount

  return <p>{size.width} x {size.height}</p>;
}

// Debounced search
function SearchInput({ onSearch }: { onSearch: (q: string) => void }) {
  const [query, setQuery] = useState("");

  useEffect(() => {
    const timer = setTimeout(() => {
      if (query) onSearch(query);
    }, 300);

    return () => clearTimeout(timer); // Cancel previous timer
  }, [query, onSearch]);

  return (
    <input
      value={query}
      onChange={e => setQuery(e.target.value)}
      placeholder="Search..."
    />
  );
}

// Document title sync
function PageTitle({ title }: { title: string }) {
  useEffect(() => {
    document.title = title;
  }, [title]);

  return null;
}`,
      },
    ],
    quiz: [
      {
        question: "When does a useEffect with an empty dependency array run?",
        options: [
          "On every render",
          "Only once after the initial render",
          "Never",
          "Before the component renders",
        ],
        correct: 1,
      },
      {
        question: "What is the cleanup function in useEffect used for?",
        options: [
          "To delete the component",
          "To clear state",
          "To clean up subscriptions, timers, and event listeners",
          "To reset the DOM",
        ],
        correct: 2,
      },
      {
        question: "What causes an infinite loop in useEffect?",
        options: [
          "Using async functions",
          "Updating a state value that is in the dependency array without guards",
          "Having too many dependencies",
          "Using cleanup functions",
        ],
        correct: 1,
      },
    ],
  },

  "fe-18-2": {
    id: "fe-18-2",
    title: "Custom Hooks",
    content: `# Custom Hooks

Custom hooks let you extract reusable stateful logic from components. They are regular JavaScript functions that call other hooks (useState, useEffect, etc.) and can return anything. Custom hooks are one of the most powerful patterns in React — they enable clean separation of concerns without render props or higher-order components.

## Rules of Custom Hooks

A custom hook is any function whose name starts with "use" — this convention tells React and lint tools to check for hook rules. Custom hooks must follow the same rules as built-in hooks: only call hooks at the top level (not in conditions/loops), and only call them from React components or other custom hooks.

## Why Custom Hooks?

Without custom hooks, you'd duplicate stateful logic across components. For example, if five components need to track window size, each would have its own useState and useEffect. A custom \`useWindowSize\` hook encapsulates this logic in one place. Components call the hook and get the data — they don't care about the implementation.

## Building Custom Hooks

Start by identifying duplicated stateful logic in your components. Extract the state, effects, and return values into a function. Name it \`useSomething\`. The hook returns whatever the consuming components need — a value, an object, an array, or even nothing (if it only performs side effects).

## Common Custom Hook Patterns

Popular custom hooks include: \`useLocalStorage\` (persist state to localStorage), \`useFetch\` (data fetching with loading/error states), \`useDebounce\` (debounce a rapidly changing value), \`useMediaQuery\` (respond to CSS media queries), \`useOnClickOutside\` (detect clicks outside an element), and \`useToggle\` (boolean toggle). Libraries like \`react-use\` and \`usehooks-ts\` provide dozens of battle-tested hooks.

## Composition of Hooks

The real power of custom hooks is composition — hooks can call other hooks. A \`useApi\` hook might use \`useFetch\` internally, which uses \`useState\` and \`useEffect\`. This creates elegant layers of abstraction without any of the complexity of class-based patterns.`,
    videos: [
      { title: "Custom React Hooks Explained", url: "https://www.youtube.com/watch?v=6ThXsUwLWvc", duration: "10:00" },
      { title: "Build 3 Custom React Hooks", url: "https://www.youtube.com/watch?v=Jl4q2cccwf0", duration: "17:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `import { useState, useEffect, useCallback, useRef } from "react";

// useLocalStorage — persist state
function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    try {
      const stored = localStorage.getItem(key);
      return stored ? JSON.parse(stored) : initialValue;
    } catch {
      return initialValue;
    }
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}

// Usage
function Settings() {
  const [theme, setTheme] = useLocalStorage("theme", "light");
  return <button onClick={() => setTheme(t => t === "light" ? "dark" : "light")}>{theme}</button>;
}

// useDebounce — debounce a value
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Usage with search
function Search() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (debouncedQuery) {
      fetch(\`/api/search?q=\${debouncedQuery}\`).then(/* ... */);
    }
  }, [debouncedQuery]);

  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}

// useFetch — reusable data fetching
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchData() {
      setLoading(true);
      setError(null);

      try {
        const res = await fetch(url, { signal: controller.signal });
        if (!res.ok) throw new Error(\`HTTP \${res.status}\`);
        setData(await res.json());
      } catch (e: any) {
        if (e.name !== "AbortError") setError(e.message);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserList() {
  const { data: users, loading, error } = useFetch<User[]>("/api/users");

  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;
  return <ul>{users?.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// useOnClickOutside
function useOnClickOutside(ref: React.RefObject<HTMLElement>, handler: () => void) {
  useEffect(() => {
    const listener = (e: MouseEvent) => {
      if (!ref.current || ref.current.contains(e.target as Node)) return;
      handler();
    };
    document.addEventListener("mousedown", listener);
    return () => document.removeEventListener("mousedown", listener);
  }, [ref, handler]);
}`,
      },
    ],
    quiz: [
      {
        question: "What naming convention must custom hooks follow?",
        options: [
          "Start with 'hook'",
          "Start with 'use'",
          "End with 'Hook'",
          "Start with 'custom'",
        ],
        correct: 1,
      },
      {
        question: "Can custom hooks call other custom hooks?",
        options: [
          "No, only built-in hooks",
          "Yes, hooks can compose with other hooks",
          "Only useState and useEffect",
          "Only in class components",
        ],
        correct: 1,
      },
    ],
  },

  "fe-19-1": {
    id: "fe-19-1",
    title: "Routing",
    content: `# React Router — Client-Side Routing

Single-page applications (SPAs) need routing to display different views based on the URL without full page reloads. React Router is the standard routing library for React, providing declarative, component-based routing.

## How Client-Side Routing Works

In a traditional website, every URL change triggers a full page reload from the server. In an SPA, JavaScript intercepts navigation, updates the URL using the History API, and renders the appropriate components — all without a page reload. This makes navigation feel instant and enables smooth transitions.

## Setting Up React Router

Wrap your app with \`BrowserRouter\` (or \`RouterProvider\` in v6.4+). Define routes that map URL paths to components using \`Routes\` and \`Route\`. The \`path\` prop specifies the URL pattern, and the \`element\` prop specifies the component to render. Use \`Link\` or \`NavLink\` for navigation instead of \`<a>\` tags — they prevent full page reloads.

## Dynamic Routes and URL Parameters

Dynamic segments use a colon prefix: \`/users/:userId\`. Access the parameter value with the \`useParams()\` hook. This enables URLs like \`/users/123\` where \`123\` is the userId. Nested routes define child routes inside parent routes, enabling layouts where part of the page changes while the rest stays the same.

## Navigation and Guards

The \`useNavigate()\` hook provides programmatic navigation: \`navigate("/dashboard")\`. The \`Navigate\` component redirects declaratively: \`<Navigate to="/login" />\`. For protected routes, create a wrapper component that checks authentication and either renders children or redirects to login.

## Search Params and State

The \`useSearchParams()\` hook manages URL query parameters (\`?sort=name&page=2\`). The \`useLocation()\` hook provides the current location object including pathname, search, hash, and state. Location state lets you pass data between routes without putting it in the URL.`,
    videos: [
      { title: "React Router v6 Tutorial", url: "https://www.youtube.com/watch?v=Ul3y1LXxzdU", duration: "34:00" },
      { title: "React Router in 45 Minutes", url: "https://www.youtube.com/watch?v=oTIJunBa6MA", duration: "45:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `import {
  BrowserRouter, Routes, Route, Link, NavLink,
  useParams, useNavigate, useSearchParams, Navigate, Outlet,
} from "react-router-dom";

// App with routes
function App() {
  return (
    <BrowserRouter>
      <nav>
        <NavLink to="/" className={({ isActive }) => isActive ? "active" : ""}>
          Home
        </NavLink>
        <NavLink to="/dashboard">Dashboard</NavLink>
        <NavLink to="/users">Users</NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />

        {/* Protected routes with layout */}
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/users" element={<UserList />} />
          <Route path="/users/:userId" element={<UserDetail />} />
          <Route path="/settings" element={<Settings />} />
        </Route>

        {/* 404 catch-all */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

// Dynamic route parameter
function UserDetail() {
  const { userId } = useParams<{ userId: string }>();
  const navigate = useNavigate();

  return (
    <div>
      <h1>User #{userId}</h1>
      <button onClick={() => navigate("/users")}>Back to list</button>
      <button onClick={() => navigate(\`/users/\${userId}/edit\`)}>Edit</button>
    </div>
  );
}

// Protected route wrapper
function ProtectedRoute() {
  const { user } = useAuth(); // Your auth hook

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />; // Renders child routes
}

// Search params for filters
function UserList() {
  const [searchParams, setSearchParams] = useSearchParams();
  const page = Number(searchParams.get("page") || "1");
  const sort = searchParams.get("sort") || "name";

  const setPage = (p: number) => {
    setSearchParams(prev => {
      prev.set("page", String(p));
      return prev;
    });
  };

  return (
    <div>
      <select value={sort} onChange={e =>
        setSearchParams({ sort: e.target.value, page: "1" })
      }>
        <option value="name">Name</option>
        <option value="date">Date</option>
      </select>

      {/* User list... */}

      <button onClick={() => setPage(page - 1)} disabled={page <= 1}>Prev</button>
      <span>Page {page}</span>
      <button onClick={() => setPage(page + 1)}>Next</button>
    </div>
  );
}`,
      },
    ],
    quiz: [
      {
        question: "Why use <Link> instead of <a> tags in React Router?",
        options: [
          "Link looks better",
          "Link prevents full page reloads and enables SPA navigation",
          "a tags don't work in React",
          "Link is faster to type",
        ],
        correct: 1,
      },
      {
        question: "Which hook accesses URL parameters like /users/:userId?",
        options: ["useNavigate", "useParams", "useLocation", "useSearchParams"],
        correct: 1,
      },
      {
        question: "How do you handle 404 pages in React Router?",
        options: [
          "Use a try/catch block",
          "Add a Route with path='*' as the last route",
          "React Router handles it automatically",
          "Use an error boundary",
        ],
        correct: 1,
      },
    ],
  },

  "fe-20-1": {
    id: "fe-20-1",
    title: "State Management",
    content: `# State Management in React

As applications grow, managing state becomes one of the biggest challenges. React provides built-in tools (Context, useReducer) and the ecosystem offers external libraries (Zustand, Redux, Jotai) for different scales of state management needs.

## When Local State Is Enough

Most state should be local (useState in the component that owns it). Lift state up only when siblings need to share it. The rule of thumb: keep state as close to where it's used as possible. Don't reach for global state management until you've exhausted component composition and prop drilling for 2-3 levels.

## React Context

Context provides a way to share data across the component tree without passing props at every level. Create a context with \`createContext()\`, provide values with a \`<Provider>\`, and consume them with \`useContext()\`. Context is ideal for global, infrequently-changing data: theme, locale, authentication status.

## Context Limitations

Context triggers re-renders for all consumers when any part of the context value changes. If you put a large object in context and update one field, every consumer re-renders — even those that only use other fields. Solutions include splitting context into smaller pieces, memoizing values, or using external state libraries.

## Zustand

Zustand is a lightweight, modern state management library. It creates stores as hooks with a simple API: define state and actions in a single function, then call the hook in any component. Zustand only re-renders components that use the specific state that changed (unlike Context). It requires no Provider wrapper and works with TypeScript out of the box.

## Choosing the Right Tool

For simple apps: useState + prop passing. For shared UI state (theme, sidebar): Context. For complex client state with many consumers: Zustand or Jotai. For server state (API data): TanStack Query (React Query). The best architecture often uses multiple tools together — React Query for server state, Zustand for client state, and Context for theme/auth.`,
    videos: [
      { title: "React State Management Tutorial", url: "https://www.youtube.com/watch?v=zpUMRsAO6-Y", duration: "22:00" },
      { title: "Zustand - React State Management", url: "https://www.youtube.com/watch?v=_ngCLZ5Iz-0", duration: "15:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `// === REACT CONTEXT ===
import { createContext, useContext, useState, ReactNode } from "react";

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  const login = async (email: string, password: string) => {
    const res = await fetch("/api/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    const userData = await res.json();
    setUser(userData);
  };

  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}

// === ZUSTAND ===
import { create } from "zustand";
import { persist } from "zustand/middleware";

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (id: string) => void;
  clearCart: () => void;
  totalPrice: () => number;
}

const useCartStore = create<CartStore>()(
  persist(
    (set, get) => ({
      items: [],

      addItem: (item) =>
        set((state) => {
          const existing = state.items.find((i) => i.id === item.id);
          if (existing) {
            return {
              items: state.items.map((i) =>
                i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
              ),
            };
          }
          return { items: [...state.items, { ...item, quantity: 1 }] };
        }),

      removeItem: (id) =>
        set((state) => ({
          items: state.items.filter((i) => i.id !== id),
        })),

      clearCart: () => set({ items: [] }),

      totalPrice: () =>
        get().items.reduce((sum, item) => sum + item.price * item.quantity, 0),
    }),
    { name: "cart-storage" } // Persists to localStorage
  )
);

// Usage — component only re-renders when items change
function CartBadge() {
  const itemCount = useCartStore((state) => state.items.length);
  return <span className="badge">{itemCount}</span>;
}

function CartTotal() {
  const totalPrice = useCartStore((state) => state.totalPrice());
  return <p>Total: \${totalPrice.toFixed(2)}</p>;
}`,
      },
    ],
    quiz: [
      {
        question: "When should you use Context vs Zustand?",
        options: [
          "Always use Context",
          "Context for infrequent global data (theme/auth); Zustand for frequently changing state with many consumers",
          "Zustand is only for large applications",
          "They are identical in performance",
        ],
        correct: 1,
      },
      {
        question: "What is the main performance issue with React Context?",
        options: [
          "It's slower than props",
          "All consumers re-render when any part of the context value changes",
          "It doesn't work with TypeScript",
          "It can't hold objects",
        ],
        correct: 1,
      },
      {
        question: "Where should most state live in a React application?",
        options: [
          "In a global store",
          "As close to where it's used as possible (local state)",
          "In the URL",
          "In localStorage",
        ],
        correct: 1,
      },
    ],
  },

  "fe-21-1": {
    id: "fe-21-1",
    title: "TypeScript Fundamentals",
    content: `# TypeScript Fundamentals

TypeScript is a superset of JavaScript that adds static type checking. It catches errors at compile time rather than runtime, provides better IDE support (autocomplete, refactoring), and makes code more self-documenting. TypeScript is now the industry standard for professional React development.

## Basic Types

TypeScript provides primitive types: \`string\`, \`number\`, \`boolean\`, \`null\`, \`undefined\`. Arrays use \`string[]\` or \`Array<string>\`. Tuples define fixed-length arrays with specific types: \`[string, number]\`. \`any\` opts out of type checking (avoid it). \`unknown\` is the type-safe alternative to \`any\` — you must narrow it before use.

## Interfaces and Type Aliases

Interfaces define the shape of objects: \`interface User { name: string; age: number; }\`. Type aliases can define unions, intersections, and primitives: \`type Status = "active" | "inactive"\`. Both can be used for objects — interfaces support \`extends\` and declaration merging, while type aliases support unions and intersections. Use whichever your team prefers; be consistent.

## Union Types and Narrowing

Union types represent values that could be one of several types: \`string | number\`. TypeScript requires you to narrow the type before using type-specific methods — use \`typeof\`, \`instanceof\`, \`in\`, or custom type guards. Discriminated unions use a common property to distinguish between types and work beautifully with switch statements.

## Generics

Generics let you write reusable code that works with multiple types while maintaining type safety. A function \`function identity<T>(arg: T): T\` works with any type. Generics are essential for utility types, data structures, and library code. React hooks like \`useState<number>(0)\` use generics.

## TypeScript with React

Type React components with interface for props. Use \`React.ReactNode\` for children, \`React.ChangeEvent<HTMLInputElement>\` for events, and generic hooks like \`useState<User | null>(null)\`. TypeScript transforms React development by catching prop errors, wrong event handler signatures, and missing required props at compile time.`,
    videos: [
      { title: "TypeScript Tutorial for Beginners", url: "https://www.youtube.com/watch?v=d56mG7DezGs", duration: "65:00" },
      { title: "TypeScript with React", url: "https://www.youtube.com/watch?v=TPACABQTHvM", duration: "38:00" },
    ],
    codeExamples: [
      {
        language: "typescript",
        code: `// Basic types
const name: string = "Alice";
const age: number = 28;
const isActive: boolean = true;
const scores: number[] = [95, 87, 92];
const tuple: [string, number] = ["Alice", 28];

// Interface
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user" | "moderator";  // Union literal type
  avatar?: string;                        // Optional
  readonly createdAt: Date;               // Cannot be changed
}

// Type alias with union
type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; message: string }
  | { status: "loading" };

// Narrowing with discriminated union
function handleResponse(response: ApiResponse<User[]>) {
  switch (response.status) {
    case "success":
      console.log(response.data);    // TypeScript knows data exists
      break;
    case "error":
      console.error(response.message); // TypeScript knows message exists
      break;
    case "loading":
      console.log("Loading...");
      break;
  }
}

// Generics
function getFirst<T>(arr: T[]): T | undefined {
  return arr[0];
}

const firstNum = getFirst([1, 2, 3]);      // type: number | undefined
const firstStr = getFirst(["a", "b"]);      // type: string | undefined

// Generic with constraint
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// TypeScript with React
interface CardProps {
  title: string;
  description: string;
  children: React.ReactNode;
  onAction?: (id: string) => void;
  variant?: "default" | "outlined" | "filled";
}

function Card({ title, description, children, onAction, variant = "default" }: CardProps) {
  return (
    <div className={\`card card-\${variant}\`}>
      <h3>{title}</h3>
      <p>{description}</p>
      {children}
      {onAction && <button onClick={() => onAction(title)}>Action</button>}
    </div>
  );
}

// Typed useState
const [user, setUser] = useState<User | null>(null);
const [items, setItems] = useState<Item[]>([]);

// Typed event handlers
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  setQuery(e.target.value);
};

const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();
};

// Utility types
type UserPreview = Pick<User, "id" | "name" | "avatar">;
type EditableUser = Omit<User, "id" | "createdAt">;
type PartialUser = Partial<User>;
type RequiredUser = Required<User>;`,
      },
    ],
    quiz: [
      {
        question: "What is the difference between 'any' and 'unknown'?",
        options: [
          "They are identical",
          "'any' disables type checking; 'unknown' requires narrowing before use",
          "'unknown' is slower",
          "'any' only works with primitives",
        ],
        correct: 1,
      },
      {
        question: "What are generics used for?",
        options: [
          "Making code slower but safer",
          "Creating reusable code that works with multiple types while keeping type safety",
          "Converting JavaScript to TypeScript",
          "Only for React components",
        ],
        correct: 1,
      },
      {
        question: "How do you type an optional prop in TypeScript?",
        options: [
          "Use the 'optional' keyword",
          "Add a question mark after the property name (prop?: type)",
          "Set it to null",
          "Use the Optional<> utility type",
        ],
        correct: 1,
      },
    ],
  },

  "fe-22-1": {
    id: "fe-22-1",
    title: "Testing React Apps",
    content: `# Testing React Applications

Testing ensures your code works correctly and stays correct as you make changes. In React, testing typically involves unit tests (individual functions/components), integration tests (multiple components working together), and end-to-end tests (full user flows). The combination of Jest and React Testing Library (RTL) is the most popular testing stack.

## Jest Fundamentals

Jest is a testing framework that provides test runners, assertions, and mocking. Tests are organized with \`describe\` (group) and \`it\`/\`test\` (individual test). Assertions use \`expect(value).toBe(expected)\` for primitives, \`.toEqual()\` for objects/arrays, \`.toBeTruthy()\`/\`.toBeFalsy()\`, \`.toHaveLength()\`, \`.toThrow()\`, and more.

## React Testing Library Philosophy

RTL promotes testing components the way users interact with them — not testing implementation details. Instead of checking state variables or component instances, you find elements by their accessible roles, labels, and text. This makes tests more resilient to refactoring. The guiding principle: "The more your tests resemble the way your software is used, the more confidence they give you."

## Rendering and Querying

\`render(<Component />)\` renders a component to a virtual DOM. Query elements with \`screen.getByRole()\` (buttons, headings), \`screen.getByText()\`, \`screen.getByLabelText()\` (form inputs), \`screen.getByPlaceholderText()\`. Use \`queryBy*\` when the element might not exist, and \`findBy*\` for elements that appear asynchronously.

## User Interactions

\`@testing-library/user-event\` simulates real user behavior: \`userEvent.click()\`, \`userEvent.type()\`, \`userEvent.clear()\`, \`userEvent.selectOptions()\`. Always use \`userEvent\` over \`fireEvent\` — it more accurately simulates real interactions including focus, keyboard events, and event ordering.

## Mocking

Jest provides \`jest.fn()\` for mock functions, \`jest.mock()\` for mocking modules, and \`jest.spyOn()\` for spying on existing methods. Mock API calls to avoid network requests in tests. Use \`msw\` (Mock Service Worker) for more realistic API mocking that intercepts requests at the network level.`,
    videos: [
      { title: "React Testing Library Tutorial", url: "https://www.youtube.com/watch?v=T2sv8jXoP4s", duration: "40:00" },
      { title: "Jest Crash Course", url: "https://www.youtube.com/watch?v=ajiAl5UNzBU", duration: "32:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `// Counter.test.tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Counter } from "./Counter";

describe("Counter", () => {
  it("renders with initial count of 0", () => {
    render(<Counter />);
    expect(screen.getByText("Count: 0")).toBeInTheDocument();
  });

  it("increments when + button is clicked", async () => {
    const user = userEvent.setup();
    render(<Counter />);

    await user.click(screen.getByRole("button", { name: /increment/i }));

    expect(screen.getByText("Count: 1")).toBeInTheDocument();
  });

  it("decrements when - button is clicked", async () => {
    const user = userEvent.setup();
    render(<Counter initialCount={5} />);

    await user.click(screen.getByRole("button", { name: /decrement/i }));

    expect(screen.getByText("Count: 4")).toBeInTheDocument();
  });
});

// LoginForm.test.tsx
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { LoginForm } from "./LoginForm";

describe("LoginForm", () => {
  const mockOnSubmit = jest.fn();

  beforeEach(() => {
    mockOnSubmit.mockClear();
  });

  it("shows validation error for empty fields", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockOnSubmit} />);

    await user.click(screen.getByRole("button", { name: /log in/i }));

    expect(screen.getByText(/email is required/i)).toBeInTheDocument();
    expect(mockOnSubmit).not.toHaveBeenCalled();
  });

  it("submits with valid data", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={mockOnSubmit} />);

    await user.type(screen.getByLabelText(/email/i), "test@example.com");
    await user.type(screen.getByLabelText(/password/i), "password123");
    await user.click(screen.getByRole("button", { name: /log in/i }));

    expect(mockOnSubmit).toHaveBeenCalledWith({
      email: "test@example.com",
      password: "password123",
    });
  });
});

// Async component with API call
describe("UserProfile", () => {
  it("shows loading state then user data", async () => {
    // Mock fetch
    global.fetch = jest.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve({ name: "Alice", role: "Developer" }),
    });

    render(<UserProfile userId="1" />);

    // Loading state
    expect(screen.getByText(/loading/i)).toBeInTheDocument();

    // Wait for data
    expect(await screen.findByText("Alice")).toBeInTheDocument();
    expect(screen.getByText("Developer")).toBeInTheDocument();
  });
});`,
      },
    ],
    quiz: [
      {
        question: "What is the main philosophy of React Testing Library?",
        options: [
          "Test implementation details",
          "Test components the way users interact with them",
          "Test every function individually",
          "Only test with snapshots",
        ],
        correct: 1,
      },
      {
        question: "Which query should you prefer for finding a button?",
        options: [
          "screen.getByTestId('button')",
          "screen.getByRole('button', { name: /submit/i })",
          "screen.querySelector('button')",
          "screen.getByClassName('btn')",
        ],
        correct: 1,
      },
      {
        question: "When should you use findBy* instead of getBy*?",
        options: [
          "Always",
          "When the element appears asynchronously",
          "When the element might not exist",
          "For form inputs only",
        ],
        correct: 1,
      },
    ],
  },

  "fe-23-1": {
    id: "fe-23-1",
    title: "Git Workflow",
    content: `# Git and GitHub Workflow

Git is the industry-standard version control system. It tracks changes to your code, enables collaboration, and provides a safety net for experimenting. GitHub adds a collaboration layer with pull requests, code reviews, and CI/CD. Every professional developer must be proficient with Git.

## Core Git Concepts

A Git repository tracks the history of your project as a series of snapshots (commits). Each commit has a unique hash, a message, an author, and a pointer to its parent commit(s). The working directory contains your actual files. The staging area (index) holds changes you're preparing to commit. Branches are lightweight pointers to commits.

## Essential Commands

\`git init\` creates a repository. \`git clone\` copies a remote repository. \`git add <file>\` stages changes. \`git commit -m "message"\` creates a commit. \`git status\` shows the current state. \`git log\` shows history. \`git diff\` shows unstaged changes. These six commands cover 80% of daily Git usage.

## Branching Strategy

Create a branch for every feature or bug fix: \`git checkout -b feature/user-auth\`. Work on your branch, commit frequently, then merge back to main via a pull request. The main branch should always be deployable. Common strategies include GitHub Flow (simple: main + feature branches) and Git Flow (main + develop + feature + release branches).

## Pull Requests and Code Review

A pull request (PR) is a request to merge your branch into another branch (usually main). It shows the diff of all changes and provides a space for code review — teammates can comment on specific lines, request changes, and approve. PRs are the primary quality gate in professional teams. Write clear PR descriptions explaining what and why.

## Resolving Conflicts

Conflicts occur when two branches modify the same lines. Git marks conflicts in the file with \`<<<<<<<\`, \`=======\`, and \`>>>>>>>\` markers. Resolve by editing the file to keep the correct code, then stage and commit. Use \`git pull --rebase\` instead of \`git merge\` to keep a cleaner history. Visual tools like VS Code's merge editor make conflict resolution easier.`,
    videos: [
      { title: "Git and GitHub for Beginners", url: "https://www.youtube.com/watch?v=RGOj5yH7evk", duration: "68:00" },
      { title: "Git Branching and Merging", url: "https://www.youtube.com/watch?v=Q1kHG842HoI", duration: "17:00" },
    ],
    codeExamples: [
      {
        language: "bash",
        code: `# Initialize a new repository
git init

# Clone an existing repository
git clone https://github.com/user/repo.git

# Daily workflow
git status                          # Check what's changed
git add src/components/Button.tsx   # Stage specific file
git add .                           # Stage all changes
git commit -m "feat: add Button component with variants"

# Branching
git checkout -b feature/user-auth   # Create and switch to new branch
git branch                          # List branches
git checkout main                   # Switch to main
git branch -d feature/user-auth     # Delete merged branch

# Keeping up to date
git fetch origin                    # Download remote changes
git pull origin main                # Fetch + merge main
git pull --rebase origin main       # Fetch + rebase (cleaner)

# Pushing
git push origin feature/user-auth   # Push branch to remote
git push -u origin feature/user-auth  # Push and set upstream

# Viewing history
git log --oneline --graph           # Compact visual history
git diff                            # Unstaged changes
git diff --staged                   # Staged changes

# Undoing changes
git restore <file>                  # Discard unstaged changes
git restore --staged <file>         # Unstage file
git revert <commit-hash>            # Create a new commit that undoes changes

# Stashing (temporarily save changes)
git stash                           # Save current changes
git stash pop                       # Restore stashed changes
git stash list                      # List stashes

# Conventional commit messages
# feat: add user registration form
# fix: resolve login redirect loop
# refactor: extract validation logic to utils
# docs: update API documentation
# test: add unit tests for Cart component
# chore: update dependencies`,
      },
    ],
    quiz: [
      {
        question: "What is the purpose of the staging area (git add)?",
        options: [
          "To delete files",
          "To select which changes to include in the next commit",
          "To push changes to remote",
          "To create a new branch",
        ],
        correct: 1,
      },
      {
        question: "What should you do before merging a feature branch?",
        options: [
          "Delete the branch",
          "Create a pull request for code review",
          "Push directly to main",
          "Rewrite the branch history",
        ],
        correct: 1,
      },
      {
        question: "What does 'git pull --rebase' do differently from 'git pull'?",
        options: [
          "It's faster",
          "It replays your commits on top of remote changes instead of creating a merge commit",
          "It only downloads changes",
          "It deletes remote changes",
        ],
        correct: 1,
      },
    ],
  },

  "fe-24-1": {
    id: "fe-24-1",
    title: "Performance Optimization",
    content: `# Web Performance Optimization

Performance directly impacts user experience, conversion rates, and SEO. Google uses Core Web Vitals as ranking factors. A one-second delay in page load can reduce conversions by 7%. Understanding and optimizing performance is a crucial professional skill.

## Core Web Vitals

Google's three key metrics are: LCP (Largest Contentful Paint) — how fast the main content appears (should be under 2.5s). FID/INP (First Input Delay / Interaction to Next Paint) — how responsive the page is to user input (should be under 200ms). CLS (Cumulative Layout Shift) — how much the page layout shifts unexpectedly (should be under 0.1). Measure these with Lighthouse, PageSpeed Insights, or the Web Vitals Chrome extension.

## JavaScript Optimization

Reduce bundle size with code splitting (dynamic imports), tree shaking (removing unused exports), and lazy loading (loading components only when needed). React provides \`React.lazy()\` and \`Suspense\` for component-level code splitting. Memoize expensive calculations with \`useMemo\` and stable callbacks with \`useCallback\` — but only when you've measured a real performance problem.

## Image Optimization

Images are typically the heaviest assets. Use modern formats (WebP, AVIF) that are 25-50% smaller than JPEG/PNG. Implement responsive images with \`srcset\` to serve appropriately sized images. Lazy-load below-the-fold images with \`loading="lazy"\`. Use the \`<picture>\` element for art direction. Consider image CDNs like Cloudinary or imgix for automatic optimization.

## Rendering Performance

Avoid unnecessary re-renders in React with \`React.memo\`, proper key usage in lists, and keeping state as local as possible. Use the React DevTools Profiler to identify components that re-render too often. Virtualize long lists (render only visible items) with libraries like \`react-window\` or \`@tanstack/virtual\`.

## Caching and Loading Strategies

Set proper cache headers for static assets (long cache with hashed filenames). Use a service worker for offline support and faster repeat visits. Preload critical resources with \`<link rel="preload">\`. Prefetch likely next pages with \`<link rel="prefetch">\`. Use \`dns-prefetch\` and \`preconnect\` for third-party domains.`,
    videos: [
      { title: "Web Performance - Fireship", url: "https://www.youtube.com/watch?v=0fONene3OIA", duration: "12:00" },
      { title: "React Performance Optimization", url: "https://www.youtube.com/watch?v=uojLJFt9SzY", duration: "18:00" },
    ],
    codeExamples: [
      {
        language: "tsx",
        code: `import { lazy, Suspense, useMemo, useCallback, memo } from "react";

// Code splitting with React.lazy
const AdminDashboard = lazy(() => import("./pages/AdminDashboard"));
const Analytics = lazy(() => import("./pages/Analytics"));

function App() {
  return (
    <Suspense fallback={<div className="spinner">Loading...</div>}>
      <Routes>
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}

// useMemo — memoize expensive calculations
function ExpensiveList({ items, filter }: { items: Item[]; filter: string }) {
  const filteredItems = useMemo(
    () => items.filter(item =>
      item.name.toLowerCase().includes(filter.toLowerCase())
    ).sort((a, b) => a.name.localeCompare(b.name)),
    [items, filter]  // Only recompute when these change
  );

  return <ul>{filteredItems.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
}

// useCallback — stable function reference for child components
function Parent() {
  const [items, setItems] = useState<Item[]>([]);

  const handleDelete = useCallback((id: string) => {
    setItems(prev => prev.filter(item => item.id !== id));
  }, []);  // Stable reference — doesn't change between renders

  return <MemoizedList items={items} onDelete={handleDelete} />;
}

// React.memo — skip re-renders when props unchanged
const MemoizedList = memo(function ItemList({
  items,
  onDelete,
}: {
  items: Item[];
  onDelete: (id: string) => void;
}) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>
          {item.name}
          <button onClick={() => onDelete(item.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
});

// Virtualized list for large datasets
import { useVirtualizer } from "@tanstack/react-virtual";

function VirtualList({ items }: { items: string[] }) {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 40,
  });

  return (
    <div ref={parentRef} style={{ height: "400px", overflow: "auto" }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map(virtualItem => (
          <div key={virtualItem.key}
            style={{ transform: \`translateY(\${virtualItem.start}px)\` }}>
            {items[virtualItem.index]}
          </div>
        ))}
      </div>
    </div>
  );
}`,
      },
      {
        language: "html",
        code: `<!-- Image optimization -->
<img
  src="hero.webp"
  alt="Hero image"
  width="1200"
  height="600"
  loading="lazy"
  decoding="async"
/>

<!-- Preload critical resources -->
<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/critical.css" as="style">

<!-- Prefetch likely next page -->
<link rel="prefetch" href="/dashboard">

<!-- DNS prefetch for third-party -->
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preconnect" href="https://cdn.example.com">`,
      },
    ],
    quiz: [
      {
        question: "What is LCP and what is the target?",
        options: [
          "Last Content Paint — under 1s",
          "Largest Contentful Paint — under 2.5s",
          "Layout Cumulative Performance — under 100ms",
          "Load Complete Point — under 3s",
        ],
        correct: 1,
      },
      {
        question: "When should you use useMemo?",
        options: [
          "For every calculation",
          "Only when you've measured a real performance problem with expensive computations",
          "For all state updates",
          "Only in class components",
        ],
        correct: 1,
      },
    ],
  },

  "fe-25-1": {
    id: "fe-25-1",
    title: "Build & Deploy",
    content: `# Build Tools and Deployment

Taking your React application from development to production involves build tools that optimize your code and deployment platforms that serve it to users worldwide. Understanding this pipeline is essential for shipping real applications.

## Build Tools: Vite

Vite is the modern standard for React development. In development, it uses native ES modules for instant hot module replacement (HMR) — changes appear in the browser in milliseconds. For production, it uses Rollup to bundle, minify, and optimize your code. The \`vite build\` command generates a \`dist\` folder with static files ready for deployment.

## What the Build Does

A production build: transpiles TypeScript and JSX to JavaScript, bundles all modules into optimized chunks, minifies code (removes whitespace, shortens variable names), tree-shakes unused exports, processes and optimizes CSS, hashes filenames for cache busting (\`app.a1b2c3.js\`), and generates an \`index.html\` that loads everything.

## Environment Variables

Use \`.env\` files for configuration: \`.env\` for defaults, \`.env.local\` for local overrides, \`.env.production\` for production values. In Vite, prefix variables with \`VITE_\` to expose them to client code: \`VITE_API_URL=https://api.example.com\`. Access them with \`import.meta.env.VITE_API_URL\`. Never put secrets in frontend env vars — they're visible in the browser.

## Deployment Platforms

Vercel and Netlify are the most popular platforms for frontend deployment. Both offer: automatic deployments from Git (push to main = deploy to production), preview deployments for pull requests, custom domains with free SSL, edge functions for server-side logic, and generous free tiers. Connect your GitHub repository, configure the build command (\`npm run build\`) and output directory (\`dist\`), and you're deployed.

## CI/CD Basics

Continuous Integration (CI) automatically runs tests and checks on every push. Continuous Deployment (CD) automatically deploys when checks pass. GitHub Actions is the most common CI/CD tool for GitHub repositories. A typical pipeline: install dependencies, run linter, run tests, build the project, deploy to staging (on PR) or production (on main merge).`,
    videos: [
      { title: "Vite in 100 Seconds", url: "https://www.youtube.com/watch?v=KCrXgy8qtjM", duration: "3:00" },
      { title: "Deploy React App to Vercel", url: "https://www.youtube.com/watch?v=FvsvHzcwOmQ", duration: "10:00" },
    ],
    codeExamples: [
      {
        language: "typescript",
        code: `// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    outDir: "dist",
    sourcemap: true,
    rollupOptions: {
      output: {
        // Code splitting by vendor
        manualChunks: {
          vendor: ["react", "react-dom"],
          router: ["react-router-dom"],
        },
      },
    },
  },
});`,
      },
      {
        language: "yaml",
        code: `# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - run: npm ci
      - run: npm run lint
      - run: npm run test -- --coverage
      - run: npm run build

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - run: npm ci
      - run: npm run build

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: \${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: \${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: \${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: "--prod"`,
      },
      {
        language: "bash",
        code: `# .env files
# .env (committed — defaults)
VITE_APP_NAME=MyApp

# .env.local (not committed — local dev)
VITE_API_URL=http://localhost:3001

# .env.production (committed — production values)
VITE_API_URL=https://api.myapp.com

# Usage in code:
# const apiUrl = import.meta.env.VITE_API_URL;

# Build commands
npm run dev        # Start development server
npm run build      # Create production build
npm run preview    # Preview production build locally
npx vite build --mode staging  # Build with staging env`,
      },
    ],
    quiz: [
      {
        question: "What does tree shaking do?",
        options: [
          "Organizes files into a tree structure",
          "Removes unused exports from the final bundle",
          "Converts TypeScript to JavaScript",
          "Minifies variable names",
        ],
        correct: 1,
      },
      {
        question: "Why should you never put secrets in VITE_ environment variables?",
        options: [
          "Vite doesn't support secrets",
          "They are visible in the browser's JavaScript bundle",
          "They cause build errors",
          "They are slower to process",
        ],
        correct: 1,
      },
      {
        question: "What does a CI pipeline typically do on every push?",
        options: [
          "Only deploy to production",
          "Run linter, tests, and build to catch issues early",
          "Send email notifications",
          "Create a new branch",
        ],
        correct: 1,
      },
    ],
  },
};
