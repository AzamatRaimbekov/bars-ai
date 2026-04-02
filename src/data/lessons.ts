export interface LessonContent {
  id: string;
  title: string;
  content: string;
  codeExamples?: Array<{ language: string; code: string }>;
  quiz?: Array<{ question: string; options: string[]; correct: number }>;
}

export const LESSONS: Record<string, LessonContent> = {
  "fe-1-1": {
    id: "fe-1-1",
    title: "Document Structure",
    content: `# HTML Document Structure\n\nEvery HTML page starts with a basic structure that tells the browser how to render the content.\n\n## The DOCTYPE\n\nThe <!DOCTYPE html> declaration tells the browser this is an HTML5 document.\n\n## The HTML Element\n\nThe <html> element is the root of the page. Inside it, you have:\n\n- <head> — metadata, title, links to stylesheets\n- <body> — visible content\n\n## Basic Template\n\nEvery HTML file follows this pattern. The head contains information about the page, while the body contains the page itself.`,
    codeExamples: [
      {
        language: "html",
        code: '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <title>My First Page</title>\n</head>\n<body>\n  <h1>Hello World!</h1>\n  <p>This is my first web page.</p>\n</body>\n</html>',
      },
    ],
    quiz: [
      {
        question: "What does the <head> element contain?",
        options: ["Visible content", "Metadata and page info", "Images", "Links"],
        correct: 1,
      },
      {
        question: "Which declaration specifies HTML5?",
        options: ["<html5>", "<!DOCTYPE html>", "<version>5</version>", "<meta html5>"],
        correct: 1,
      },
    ],
  },
};
