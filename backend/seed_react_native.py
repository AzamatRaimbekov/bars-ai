"""Seed: React Native — Мобильная разработка — 7 sections, ~38 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "React Native — Мобильная разработка"
DESC = (
    "Полный курс по React Native — от установки среды до публикации в App Store и Google Play. "
    "Научитесь создавать кроссплатформенные мобильные приложения на JavaScript/TypeScript "
    "с использованием Expo и React Navigation."
)

S = [
    # ===== SECTION 1: Введение в React Native =====
    {
        "title": "Введение в React Native",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое React Native",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "React Native — кроссплатформенная разработка",
                        "markdown": (
                            "## Что такое React Native?\n\n"
                            "**React Native** — это фреймворк от Meta (Facebook) для создания "
                            "**нативных** мобильных приложений на JavaScript и TypeScript.\n\n"
                            "### Ключевые особенности:\n"
                            "- Один код → iOS + Android\n"
                            "- Нативные компоненты (не WebView!)\n"
                            "- Горячая перезагрузка (Hot Reload)\n"
                            "- Огромная экосистема npm-пакетов\n\n"
                            "### Кто использует:\n"
                            "- **Instagram** — лента, сторис\n"
                            "- **Discord** — мобильный клиент\n"
                            "- **Shopify** — мобильное приложение\n"
                            "- **Bloomberg** — новости и финансы\n\n"
                            "### Как работает:\n"
                            "```\n"
                            "JavaScript код\n"
                            "      ↓\n"
                            "React Native Bridge / New Architecture (JSI)\n"
                            "      ↓\n"
                            "Нативные компоненты (UIKit / Android Views)\n"
                            "```\n\n"
                            "React Native компилирует не в WebView, а взаимодействует с **нативными API** "
                            "платформы через мост (bridge) или новую архитектуру JSI."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что такое React Native?",
                        "options": [
                            {"id": "a", "text": "Фреймворк для создания нативных мобильных приложений на JavaScript", "correct": True},
                            {"id": "b", "text": "Библиотека для создания веб-сайтов", "correct": False},
                            {"id": "c", "text": "Язык программирования от Apple", "correct": False},
                            {"id": "d", "text": "Система управления базами данных", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "React Native рендерит компоненты через WebView, как Cordova.",
                        "correct": False,
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "React Native", "right": "Кроссплатформенный мобильный фреймворк"},
                            {"left": "Hot Reload", "right": "Мгновенное обновление UI при изменении кода"},
                            {"left": "Bridge", "right": "Мост между JS и нативным кодом"},
                            {"left": "JSI", "right": "Новая архитектура прямого вызова нативных модулей"},
                        ],
                    },
                ],
            },
            {
                "t": "Expo vs React Native CLI",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Два подхода к разработке",
                        "markdown": (
                            "## Expo vs React Native CLI\n\n"
                            "### Expo (рекомендуется для начинающих)\n"
                            "```bash\n"
                            "npx create-expo-app MyApp\n"
                            "cd MyApp\n"
                            "npx expo start\n"
                            "```\n\n"
                            "**Плюсы:**\n"
                            "- Быстрый старт без Xcode/Android Studio\n"
                            "- Expo Go — сканируй QR и смотри на телефоне\n"
                            "- OTA-обновления (EAS Update)\n"
                            "- Встроенные API: камера, уведомления, геолокация\n\n"
                            "**Минусы:**\n"
                            "- Ограниченный доступ к нативным модулям (решается через dev client)\n\n"
                            "### React Native CLI (bare workflow)\n"
                            "```bash\n"
                            "npx react-native init MyApp\n"
                            "cd MyApp\n"
                            "npx react-native run-ios\n"
                            "```\n\n"
                            "**Плюсы:**\n"
                            "- Полный контроль над нативным кодом\n"
                            "- Любые нативные модули\n\n"
                            "**Минусы:**\n"
                            "- Нужен Xcode (macOS) и Android Studio\n"
                            "- Сложнее настройка\n\n"
                            "### Вывод:\n"
                            "Начинайте с **Expo** — при необходимости всегда можно перейти на bare workflow."
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какая команда создаёт Expo-проект?",
                        "options": [
                            {"id": "a", "text": "npx create-expo-app MyApp", "correct": True},
                            {"id": "b", "text": "npx react-native init MyApp", "correct": False},
                            {"id": "c", "text": "npm install expo", "correct": False},
                            {"id": "d", "text": "expo create MyApp", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Expo требует обязательной установки Xcode и Android Studio для разработки.",
                        "correct": False,
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "Expo Go", "back": "Приложение для просмотра Expo-проекта на реальном устройстве через QR-код"},
                            {"front": "Bare Workflow", "back": "Режим React Native с полным доступом к нативному коду iOS и Android"},
                            {"front": "EAS Build", "back": "Облачная сборка приложений от Expo для iOS и Android"},
                            {"front": "Dev Client", "back": "Кастомная сборка Expo Go с поддержкой нативных модулей"},
                        ],
                    },
                ],
            },
            {
                "t": "Установка среды разработки",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Настройка окружения",
                        "markdown": (
                            "## Установка среды разработки\n\n"
                            "### 1. Node.js\n"
                            "```bash\n"
                            "# Проверка версии\n"
                            "node --version  # >= 18\n"
                            "npm --version\n"
                            "```\n\n"
                            "### 2. Создание проекта\n"
                            "```bash\n"
                            "npx create-expo-app@latest RNApp --template blank-typescript\n"
                            "cd RNApp\n"
                            "```\n\n"
                            "### 3. Запуск\n"
                            "```bash\n"
                            "npx expo start\n"
                            "```\n\n"
                            "После запуска:\n"
                            "- **i** — открыть iOS-симулятор\n"
                            "- **a** — открыть Android-эмулятор\n"
                            "- **QR-код** — открыть на реальном устройстве через Expo Go\n\n"
                            "### 4. Структура файлов:\n"
                            "```\n"
                            "RNApp/\n"
                            "├── App.tsx          # Точка входа\n"
                            "├── app.json         # Конфигурация Expo\n"
                            "├── package.json     # Зависимости\n"
                            "├── tsconfig.json    # TypeScript\n"
                            "├── assets/          # Изображения, шрифты\n"
                            "└── node_modules/    # Пакеты\n"
                            "```"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Установить Node.js версии 18+",
                            "Выполнить npx create-expo-app MyApp",
                            "Перейти в папку проекта: cd MyApp",
                            "Запустить npx expo start",
                            "Отсканировать QR-код в Expo Go",
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Какой командой запускается Expo-проект для разработки?",
                        "acceptedAnswers": ["npx expo start", "expo start"],
                    },
                ],
            },
            {
                "t": "Первое приложение: Hello World",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Пишем Hello World",
                        "markdown": (
                            "## Первое приложение\n\n"
                            "Откройте `App.tsx` и замените содержимое:\n\n"
                            "```tsx\n"
                            "import { Text, View, StyleSheet } from 'react-native';\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <View style={styles.container}>\n"
                            "      <Text style={styles.title}>Привет, React Native!</Text>\n"
                            "      <Text style={styles.subtitle}>Моё первое приложение</Text>\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n\n"
                            "const styles = StyleSheet.create({\n"
                            "  container: {\n"
                            "    flex: 1,\n"
                            "    justifyContent: 'center',\n"
                            "    alignItems: 'center',\n"
                            "    backgroundColor: '#f0f0f0',\n"
                            "  },\n"
                            "  title: {\n"
                            "    fontSize: 28,\n"
                            "    fontWeight: 'bold',\n"
                            "    color: '#333',\n"
                            "  },\n"
                            "  subtitle: {\n"
                            "    fontSize: 18,\n"
                            "    color: '#666',\n"
                            "    marginTop: 8,\n"
                            "  },\n"
                            "});\n"
                            "```\n\n"
                            "### Что тут происходит:\n"
                            "- **View** — аналог `<div>` в вебе\n"
                            "- **Text** — аналог `<p>` или `<span>`\n"
                            "- **StyleSheet.create** — создаёт оптимизированные стили\n"
                            "- **flex: 1** — занимает всё доступное пространство"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите код Hello World компонента в правильном порядке:",
                        "correctOrder": [
                            "import { Text, View } from 'react-native';",
                            "export default function App() {",
                            "  return (",
                            "    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>",
                            "      <Text>Привет, React Native!</Text>",
                            "    </View>",
                            "  );",
                            "}",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой компонент React Native является аналогом <div> в вебе?",
                        "options": [
                            {"id": "a", "text": "View", "correct": True},
                            {"id": "b", "text": "Text", "correct": False},
                            {"id": "c", "text": "Container", "correct": False},
                            {"id": "d", "text": "Div", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Для вывода текста в React Native используется компонент ___.",
                        "answer": "Text",
                    },
                ],
            },
            {
                "t": "Структура проекта",
                "xp": 20,
                "steps": [
                    {
                        "type": "info",
                        "title": "Организация файлов в React Native проекте",
                        "markdown": (
                            "## Рекомендуемая структура проекта\n\n"
                            "```\n"
                            "src/\n"
                            "├── components/       # Переиспользуемые компоненты\n"
                            "│   ├── Button.tsx\n"
                            "│   └── Card.tsx\n"
                            "├── screens/          # Экраны приложения\n"
                            "│   ├── HomeScreen.tsx\n"
                            "│   └── ProfileScreen.tsx\n"
                            "├── navigation/       # Навигация\n"
                            "│   └── AppNavigator.tsx\n"
                            "├── hooks/            # Кастомные хуки\n"
                            "│   └── useAuth.ts\n"
                            "├── services/         # API, запросы\n"
                            "│   └── api.ts\n"
                            "├── utils/            # Утилиты\n"
                            "│   └── helpers.ts\n"
                            "├── constants/        # Константы, цвета, размеры\n"
                            "│   └── colors.ts\n"
                            "└── types/            # TypeScript типы\n"
                            "    └── index.ts\n"
                            "```\n\n"
                            "### Важные файлы:\n"
                            "- **app.json** — конфигурация Expo (имя, иконка, splash)\n"
                            "- **App.tsx** — точка входа приложения\n"
                            "- **babel.config.js** — настройка Babel\n"
                            "- **tsconfig.json** — настройка TypeScript"
                        ),
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "components/", "right": "Переиспользуемые UI-компоненты"},
                            {"left": "screens/", "right": "Экраны (страницы) приложения"},
                            {"left": "navigation/", "right": "Конфигурация навигации"},
                            {"left": "services/", "right": "API-запросы и бизнес-логика"},
                            {"left": "app.json", "right": "Конфигурация Expo-приложения"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "В какой папке хранятся экраны приложения?",
                        "options": [
                            {"id": "a", "text": "screens/", "correct": True},
                            {"id": "b", "text": "components/", "correct": False},
                            {"id": "c", "text": "views/", "correct": False},
                            {"id": "d", "text": "pages/", "correct": False},
                        ],
                    },
                ],
            },
        ],
    },
    # ===== SECTION 2: Компоненты и стили =====
    {
        "title": "Компоненты и стили",
        "pos": 1,
        "lessons": [
            {
                "t": "View, Text и Image",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Базовые компоненты React Native",
                        "markdown": (
                            "## Основные компоненты\n\n"
                            "### View — контейнер\n"
                            "```tsx\n"
                            "<View style={{ padding: 16, backgroundColor: '#fff' }}>\n"
                            "  <Text>Содержимое</Text>\n"
                            "</View>\n"
                            "```\n\n"
                            "### Text — текст\n"
                            "```tsx\n"
                            "<Text style={{ fontSize: 20, fontWeight: 'bold' }}>\n"
                            "  Заголовок\n"
                            "</Text>\n"
                            "<Text numberOfLines={2} ellipsizeMode=\"tail\">\n"
                            "  Длинный текст будет обрезан после двух строк...\n"
                            "</Text>\n"
                            "```\n\n"
                            "### Image — изображение\n"
                            "```tsx\n"
                            "// Локальное изображение\n"
                            "<Image source={require('./assets/logo.png')} style={{ width: 100, height: 100 }} />\n\n"
                            "// URL изображение\n"
                            "<Image\n"
                            "  source={{ uri: 'https://example.com/photo.jpg' }}\n"
                            "  style={{ width: 200, height: 200, borderRadius: 100 }}\n"
                            "/>\n"
                            "```\n\n"
                            "### Важно:\n"
                            "- В RN нет `<div>`, `<p>`, `<img>` — используйте нативные компоненты\n"
                            "- Текст **обязательно** оборачивается в `<Text>`\n"
                            "- У `<Image>` обязательно указывайте `width` и `height`"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой компонент используется для отображения изображений?",
                        "options": [
                            {"id": "a", "text": "Image", "correct": True},
                            {"id": "b", "text": "Img", "correct": False},
                            {"id": "c", "text": "Picture", "correct": False},
                            {"id": "d", "text": "Photo", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "В React Native можно писать текст прямо внутри <View> без обёртки в <Text>.",
                        "correct": False,
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Для отображения изображения по URL в React Native используется компонент ___ с пропом source={{ uri: '...' }}.",
                        "answer": "Image",
                    },
                ],
            },
            {
                "t": "StyleSheet и стилизация",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Стили в React Native",
                        "markdown": (
                            "## StyleSheet\n\n"
                            "В React Native нет CSS-файлов. Стили задаются через JavaScript-объекты.\n\n"
                            "### Создание стилей:\n"
                            "```tsx\n"
                            "import { StyleSheet, View, Text } from 'react-native';\n\n"
                            "export default function Card() {\n"
                            "  return (\n"
                            "    <View style={styles.card}>\n"
                            "      <Text style={styles.title}>Заголовок</Text>\n"
                            "      <Text style={styles.body}>Текст карточки</Text>\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n\n"
                            "const styles = StyleSheet.create({\n"
                            "  card: {\n"
                            "    backgroundColor: '#fff',\n"
                            "    borderRadius: 12,\n"
                            "    padding: 16,\n"
                            "    shadowColor: '#000',\n"
                            "    shadowOffset: { width: 0, height: 2 },\n"
                            "    shadowOpacity: 0.1,\n"
                            "    shadowRadius: 4,\n"
                            "    elevation: 3, // тень для Android\n"
                            "  },\n"
                            "  title: {\n"
                            "    fontSize: 18,\n"
                            "    fontWeight: '600',\n"
                            "    marginBottom: 8,\n"
                            "  },\n"
                            "  body: {\n"
                            "    fontSize: 14,\n"
                            "    color: '#666',\n"
                            "  },\n"
                            "});\n"
                            "```\n\n"
                            "### Комбинирование стилей:\n"
                            "```tsx\n"
                            "<Text style={[styles.text, styles.bold, { color: 'red' }]}>Красный жирный</Text>\n"
                            "```\n\n"
                            "### Отличия от CSS:\n"
                            "- camelCase вместо kebab-case (`fontSize` вместо `font-size`)\n"
                            "- Размеры без единиц (`padding: 16` вместо `padding: 16px`)\n"
                            "- `elevation` — тень на Android"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите StyleSheet.create для карточки с тенью:",
                        "correctOrder": [
                            "const styles = StyleSheet.create({",
                            "  card: {",
                            "    backgroundColor: '#fff',",
                            "    borderRadius: 12,",
                            "    padding: 16,",
                            "    elevation: 3,",
                            "  },",
                            "});",
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "fontSize", "right": "font-size в CSS"},
                            {"left": "backgroundColor", "right": "background-color в CSS"},
                            {"left": "borderRadius", "right": "border-radius в CSS"},
                            {"left": "elevation", "right": "Тень для Android"},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "В React Native размеры указываются в пикселях с суффиксом px.",
                        "correct": False,
                    },
                ],
            },
            {
                "t": "Flexbox-раскладка",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Flexbox в React Native",
                        "markdown": (
                            "## Flexbox\n\n"
                            "React Native использует **Flexbox** для раскладки, но с отличиями от веба:\n"
                            "- `flexDirection` по умолчанию `'column'` (не `'row'`)\n\n"
                            "### Основные свойства:\n"
                            "```tsx\n"
                            "<View style={{\n"
                            "  flex: 1,\n"
                            "  flexDirection: 'row',       // горизонтальная раскладка\n"
                            "  justifyContent: 'center',   // выравнивание по главной оси\n"
                            "  alignItems: 'center',       // выравнивание по перпендикулярной оси\n"
                            "  gap: 10,                    // отступ между элементами\n"
                            "}}>\n"
                            "  <View style={{ width: 50, height: 50, backgroundColor: 'red' }} />\n"
                            "  <View style={{ width: 50, height: 50, backgroundColor: 'blue' }} />\n"
                            "  <View style={{ width: 50, height: 50, backgroundColor: 'green' }} />\n"
                            "</View>\n"
                            "```\n\n"
                            "### Пример: экран с шапкой, контентом и футером:\n"
                            "```tsx\n"
                            "<View style={{ flex: 1 }}>\n"
                            "  <View style={{ height: 60, backgroundColor: '#007AFF' }}>\n"
                            "    <Text>Шапка</Text>\n"
                            "  </View>\n"
                            "  <View style={{ flex: 1 }}>\n"
                            "    <Text>Контент (занимает всё пространство)</Text>\n"
                            "  </View>\n"
                            "  <View style={{ height: 50, backgroundColor: '#eee' }}>\n"
                            "    <Text>Футер</Text>\n"
                            "  </View>\n"
                            "</View>\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какое значение flexDirection по умолчанию в React Native?",
                        "options": [
                            {"id": "a", "text": "column", "correct": True},
                            {"id": "b", "text": "row", "correct": False},
                            {"id": "c", "text": "column-reverse", "correct": False},
                            {"id": "d", "text": "row-reverse", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "justifyContent", "right": "Выравнивание по главной оси"},
                            {"left": "alignItems", "right": "Выравнивание по перпендикулярной оси"},
                            {"left": "flex: 1", "right": "Занять всё доступное пространство"},
                            {"left": "flexDirection: 'row'", "right": "Горизонтальная раскладка"},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Свойство ___ отвечает за распределение элементов вдоль главной оси.",
                        "answer": "justifyContent",
                    },
                ],
            },
            {
                "t": "ScrollView — прокрутка",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Прокручиваемый контент",
                        "markdown": (
                            "## ScrollView\n\n"
                            "View не прокручивается. Для длинного контента используйте **ScrollView**.\n\n"
                            "```tsx\n"
                            "import { ScrollView, View, Text, StyleSheet } from 'react-native';\n\n"
                            "export default function SettingsScreen() {\n"
                            "  return (\n"
                            "    <ScrollView style={styles.container}\n"
                            "      contentContainerStyle={styles.content}\n"
                            "      showsVerticalScrollIndicator={false}\n"
                            "    >\n"
                            "      {Array.from({ length: 20 }).map((_, i) => (\n"
                            "        <View key={i} style={styles.card}>\n"
                            "          <Text>Элемент {i + 1}</Text>\n"
                            "        </View>\n"
                            "      ))}\n"
                            "    </ScrollView>\n"
                            "  );\n"
                            "}\n\n"
                            "const styles = StyleSheet.create({\n"
                            "  container: { flex: 1 },\n"
                            "  content: { padding: 16, gap: 12 },\n"
                            "  card: {\n"
                            "    backgroundColor: '#fff',\n"
                            "    padding: 16,\n"
                            "    borderRadius: 8,\n"
                            "  },\n"
                            "});\n"
                            "```\n\n"
                            "### Горизонтальная прокрутка:\n"
                            "```tsx\n"
                            "<ScrollView horizontal showsHorizontalScrollIndicator={false}>\n"
                            "  <View style={{ width: 200, height: 150, backgroundColor: 'red', marginRight: 10 }} />\n"
                            "  <View style={{ width: 200, height: 150, backgroundColor: 'blue', marginRight: 10 }} />\n"
                            "</ScrollView>\n"
                            "```\n\n"
                            "### Важно:\n"
                            "- ScrollView рендерит **все** дочерние элементы сразу\n"
                            "- Для длинных списков (100+ элементов) используйте **FlatList**"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Почему для длинных списков лучше использовать FlatList вместо ScrollView?",
                        "options": [
                            {"id": "a", "text": "FlatList рендерит только видимые элементы, экономя память", "correct": True},
                            {"id": "b", "text": "ScrollView не поддерживает прокрутку", "correct": False},
                            {"id": "c", "text": "FlatList красивее выглядит", "correct": False},
                            {"id": "d", "text": "ScrollView не работает на Android", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "ScrollView рендерит все дочерние элементы сразу, даже если они не видны на экране.",
                        "correct": True,
                    },
                ],
            },
            {
                "t": "FlatList — производительные списки",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "FlatList для больших списков",
                        "markdown": (
                            "## FlatList\n\n"
                            "**FlatList** — виртуализированный список, рендерит только видимые элементы.\n\n"
                            "```tsx\n"
                            "import { FlatList, View, Text, StyleSheet } from 'react-native';\n\n"
                            "type Item = { id: string; title: string; subtitle: string };\n\n"
                            "const DATA: Item[] = [\n"
                            "  { id: '1', title: 'React Native', subtitle: 'Мобильная разработка' },\n"
                            "  { id: '2', title: 'TypeScript', subtitle: 'Типизация' },\n"
                            "  { id: '3', title: 'Expo', subtitle: 'Инструменты' },\n"
                            "];\n\n"
                            "export default function ListScreen() {\n"
                            "  const renderItem = ({ item }: { item: Item }) => (\n"
                            "    <View style={styles.item}>\n"
                            "      <Text style={styles.title}>{item.title}</Text>\n"
                            "      <Text style={styles.subtitle}>{item.subtitle}</Text>\n"
                            "    </View>\n"
                            "  );\n\n"
                            "  return (\n"
                            "    <FlatList\n"
                            "      data={DATA}\n"
                            "      renderItem={renderItem}\n"
                            "      keyExtractor={(item) => item.id}\n"
                            "      ItemSeparatorComponent={() => <View style={styles.separator} />}\n"
                            "      ListEmptyComponent={<Text>Список пуст</Text>}\n"
                            "    />\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Ключевые пропы:\n"
                            "- `data` — массив данных\n"
                            "- `renderItem` — функция рендеринга элемента\n"
                            "- `keyExtractor` — уникальный ключ\n"
                            "- `ListHeaderComponent` — шапка списка\n"
                            "- `ListFooterComponent` — футер списка\n"
                            "- `onEndReached` — подгрузка при прокрутке до конца\n"
                            "- `refreshing` + `onRefresh` — pull-to-refresh"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите FlatList с данными:",
                        "correctOrder": [
                            "<FlatList",
                            "  data={items}",
                            "  renderItem={({ item }) => (",
                            "    <Text>{item.title}</Text>",
                            "  )}",
                            "  keyExtractor={(item) => item.id}",
                            "/>",
                        ],
                    },
                    {
                        "type": "multi-select",
                        "question": "Какие пропы являются обязательными для FlatList?",
                        "options": [
                            {"id": "a", "text": "data", "correct": True},
                            {"id": "b", "text": "renderItem", "correct": True},
                            {"id": "c", "text": "ListHeaderComponent", "correct": False},
                            {"id": "d", "text": "onEndReached", "correct": False},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Проп ___ в FlatList определяет функцию, возвращающую уникальный ключ для каждого элемента.",
                        "answer": "keyExtractor",
                    },
                ],
            },
            {
                "t": "TouchableOpacity и Pressable",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Кнопки и нажатия",
                        "markdown": (
                            "## Обработка нажатий\n\n"
                            "### TouchableOpacity — кнопка с затуханием\n"
                            "```tsx\n"
                            "import { TouchableOpacity, Text, Alert, StyleSheet } from 'react-native';\n\n"
                            "export default function MyButton() {\n"
                            "  return (\n"
                            "    <TouchableOpacity\n"
                            "      style={styles.button}\n"
                            "      activeOpacity={0.7}\n"
                            "      onPress={() => Alert.alert('Нажата кнопка!')}\n"
                            "    >\n"
                            "      <Text style={styles.text}>Нажми меня</Text>\n"
                            "    </TouchableOpacity>\n"
                            "  );\n"
                            "}\n\n"
                            "const styles = StyleSheet.create({\n"
                            "  button: {\n"
                            "    backgroundColor: '#007AFF',\n"
                            "    paddingVertical: 12,\n"
                            "    paddingHorizontal: 24,\n"
                            "    borderRadius: 8,\n"
                            "    alignItems: 'center',\n"
                            "  },\n"
                            "  text: { color: '#fff', fontSize: 16, fontWeight: '600' },\n"
                            "});\n"
                            "```\n\n"
                            "### Pressable — более гибкий вариант\n"
                            "```tsx\n"
                            "<Pressable\n"
                            "  onPress={() => console.log('Press')}\n"
                            "  onLongPress={() => console.log('Long press')}\n"
                            "  style={({ pressed }) => ({\n"
                            "    backgroundColor: pressed ? '#005BB5' : '#007AFF',\n"
                            "    padding: 12,\n"
                            "    borderRadius: 8,\n"
                            "  })}\n"
                            ">\n"
                            "  <Text style={{ color: '#fff' }}>Pressable кнопка</Text>\n"
                            "</Pressable>\n"
                            "```\n\n"
                            "### Когда что использовать:\n"
                            "- **TouchableOpacity** — простые кнопки\n"
                            "- **Pressable** — сложная обработка состояний (hover, pressed, focused)"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой проп отвечает за действие при нажатии?",
                        "options": [
                            {"id": "a", "text": "onPress", "correct": True},
                            {"id": "b", "text": "onClick", "correct": False},
                            {"id": "c", "text": "onTap", "correct": False},
                            {"id": "d", "text": "onTouch", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "TouchableOpacity", "right": "Кнопка с эффектом затухания при нажатии"},
                            {"left": "Pressable", "right": "Гибкий компонент с доступом к состоянию нажатия"},
                            {"left": "onPress", "right": "Обычное нажатие"},
                            {"left": "onLongPress", "right": "Долгое нажатие"},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Pressable позволяет менять стили в зависимости от состояния нажатия через функцию в style.",
                        "correct": True,
                    },
                ],
            },
        ],
    },
    # ===== SECTION 3: Навигация =====
    {
        "title": "Навигация",
        "pos": 2,
        "lessons": [
            {
                "t": "React Navigation: установка",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Настройка React Navigation",
                        "markdown": (
                            "## React Navigation\n\n"
                            "Главная библиотека для навигации в React Native.\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install @react-navigation/native \\\n"
                            "  react-native-screens react-native-safe-area-context\n"
                            "```\n\n"
                            "### Настройка App.tsx:\n"
                            "```tsx\n"
                            "import { NavigationContainer } from '@react-navigation/native';\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <NavigationContainer>\n"
                            "      {/* Навигаторы будут здесь */}\n"
                            "    </NavigationContainer>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Типы навигаторов:\n"
                            "- **Stack** — стек экранов (как страницы в браузере)\n"
                            "- **Tab** — нижние вкладки\n"
                            "- **Drawer** — боковое меню\n\n"
                            "### NavigationContainer:\n"
                            "- Оборачивает всё приложение\n"
                            "- Управляет состоянием навигации\n"
                            "- Обрабатывает deep linking\n"
                            "- Должен быть **один** на приложение"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Установить @react-navigation/native",
                            "Установить react-native-screens и safe-area-context",
                            "Импортировать NavigationContainer",
                            "Обернуть App в NavigationContainer",
                            "Добавить навигатор (Stack, Tab или Drawer)",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой компонент является обязательной обёрткой для навигации?",
                        "options": [
                            {"id": "a", "text": "NavigationContainer", "correct": True},
                            {"id": "b", "text": "NavigationProvider", "correct": False},
                            {"id": "c", "text": "RouterProvider", "correct": False},
                            {"id": "d", "text": "AppContainer", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Stack Navigator",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Стек-навигация",
                        "markdown": (
                            "## Stack Navigator\n\n"
                            "Экраны складываются в стек — как стопка карточек.\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install @react-navigation/native-stack\n"
                            "```\n\n"
                            "### Пример:\n"
                            "```tsx\n"
                            "import { createNativeStackNavigator } from '@react-navigation/native-stack';\n"
                            "import { NavigationContainer } from '@react-navigation/native';\n"
                            "import { View, Text, Button } from 'react-native';\n\n"
                            "type RootStackParams = {\n"
                            "  Home: undefined;\n"
                            "  Details: { itemId: number; title: string };\n"
                            "};\n\n"
                            "const Stack = createNativeStackNavigator<RootStackParams>();\n\n"
                            "function HomeScreen({ navigation }: any) {\n"
                            "  return (\n"
                            "    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>\n"
                            "      <Text>Главная</Text>\n"
                            "      <Button\n"
                            "        title=\"Открыть детали\"\n"
                            "        onPress={() => navigation.navigate('Details', {\n"
                            "          itemId: 42, title: 'Товар'\n"
                            "        })}\n"
                            "      />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n\n"
                            "function DetailsScreen({ route, navigation }: any) {\n"
                            "  const { itemId, title } = route.params;\n"
                            "  return (\n"
                            "    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>\n"
                            "      <Text>{title} (ID: {itemId})</Text>\n"
                            "      <Button title=\"Назад\" onPress={() => navigation.goBack()} />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <NavigationContainer>\n"
                            "      <Stack.Navigator initialRouteName=\"Home\">\n"
                            "        <Stack.Screen name=\"Home\" component={HomeScreen}\n"
                            "          options={{ title: 'Главная' }} />\n"
                            "        <Stack.Screen name=\"Details\" component={DetailsScreen}\n"
                            "          options={{ title: 'Детали' }} />\n"
                            "      </Stack.Navigator>\n"
                            "    </NavigationContainer>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Как передать параметры на другой экран в Stack Navigator?",
                        "options": [
                            {"id": "a", "text": "navigation.navigate('Screen', { param: value })", "correct": True},
                            {"id": "b", "text": "navigation.push({ screen: 'Screen', params: {} })", "correct": False},
                            {"id": "c", "text": "navigation.goTo('Screen', params)", "correct": False},
                            {"id": "d", "text": "navigation.redirect('Screen')", "correct": False},
                        ],
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите Stack Navigator:",
                        "correctOrder": [
                            "const Stack = createNativeStackNavigator();",
                            "<NavigationContainer>",
                            "  <Stack.Navigator>",
                            "    <Stack.Screen name=\"Home\" component={HomeScreen} />",
                            "    <Stack.Screen name=\"Details\" component={DetailsScreen} />",
                            "  </Stack.Navigator>",
                            "</NavigationContainer>",
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Для получения параметров навигации на экране используется объект route.___.",
                        "answer": "params",
                    },
                ],
            },
            {
                "t": "Tab Navigator",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Навигация с вкладками",
                        "markdown": (
                            "## Bottom Tab Navigator\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install @react-navigation/bottom-tabs\n"
                            "```\n\n"
                            "### Пример:\n"
                            "```tsx\n"
                            "import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';\n"
                            "import { Ionicons } from '@expo/vector-icons';\n\n"
                            "const Tab = createBottomTabNavigator();\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <NavigationContainer>\n"
                            "      <Tab.Navigator screenOptions={({ route }) => ({\n"
                            "        tabBarIcon: ({ color, size }) => {\n"
                            "          let iconName: keyof typeof Ionicons.glyphMap = 'home';\n"
                            "          if (route.name === 'Home') iconName = 'home';\n"
                            "          else if (route.name === 'Search') iconName = 'search';\n"
                            "          else if (route.name === 'Profile') iconName = 'person';\n"
                            "          return <Ionicons name={iconName} size={size} color={color} />;\n"
                            "        },\n"
                            "        tabBarActiveTintColor: '#007AFF',\n"
                            "      })}>\n"
                            "        <Tab.Screen name=\"Home\" component={HomeScreen} />\n"
                            "        <Tab.Screen name=\"Search\" component={SearchScreen} />\n"
                            "        <Tab.Screen name=\"Profile\" component={ProfileScreen} />\n"
                            "      </Tab.Navigator>\n"
                            "    </NavigationContainer>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Кастомизация:\n"
                            "- `tabBarActiveTintColor` — цвет активной вкладки\n"
                            "- `tabBarBadge` — бейдж с числом\n"
                            "- `tabBarStyle` — стили панели вкладок"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой пакет нужен для нижних вкладок?",
                        "options": [
                            {"id": "a", "text": "@react-navigation/bottom-tabs", "correct": True},
                            {"id": "b", "text": "@react-navigation/tabs", "correct": False},
                            {"id": "c", "text": "@react-navigation/tab-navigator", "correct": False},
                            {"id": "d", "text": "react-native-tab-view", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Tab Navigator может содержать внутри себя Stack Navigator для каждой вкладки.",
                        "correct": True,
                    },
                ],
            },
            {
                "t": "Drawer Navigator",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Боковое меню",
                        "markdown": (
                            "## Drawer Navigator\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install @react-navigation/drawer react-native-gesture-handler react-native-reanimated\n"
                            "```\n\n"
                            "### Пример:\n"
                            "```tsx\n"
                            "import { createDrawerNavigator } from '@react-navigation/drawer';\n\n"
                            "const Drawer = createDrawerNavigator();\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <NavigationContainer>\n"
                            "      <Drawer.Navigator initialRouteName=\"Home\"\n"
                            "        screenOptions={{\n"
                            "          drawerStyle: { backgroundColor: '#f5f5f5', width: 250 },\n"
                            "          drawerActiveTintColor: '#007AFF',\n"
                            "        }}\n"
                            "      >\n"
                            "        <Drawer.Screen name=\"Home\" component={HomeScreen}\n"
                            "          options={{ title: 'Главная' }} />\n"
                            "        <Drawer.Screen name=\"Settings\" component={SettingsScreen}\n"
                            "          options={{ title: 'Настройки' }} />\n"
                            "        <Drawer.Screen name=\"About\" component={AboutScreen}\n"
                            "          options={{ title: 'О приложении' }} />\n"
                            "      </Drawer.Navigator>\n"
                            "    </NavigationContainer>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Открытие drawer программно:\n"
                            "```tsx\n"
                            "navigation.openDrawer();\n"
                            "navigation.closeDrawer();\n"
                            "navigation.toggleDrawer();\n"
                            "```"
                        ),
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "Stack Navigator", "right": "Экраны стопкой, переход вперёд-назад"},
                            {"left": "Tab Navigator", "right": "Нижние вкладки для переключения разделов"},
                            {"left": "Drawer Navigator", "right": "Боковое выдвижное меню"},
                            {"left": "navigation.openDrawer()", "right": "Программное открытие бокового меню"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какие дополнительные пакеты нужны для Drawer Navigator?",
                        "options": [
                            {"id": "a", "text": "react-native-gesture-handler и react-native-reanimated", "correct": True},
                            {"id": "b", "text": "react-native-drawer и react-native-menu", "correct": False},
                            {"id": "c", "text": "Никаких дополнительных пакетов не нужно", "correct": False},
                            {"id": "d", "text": "react-native-sidebar", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Deep Linking и параметры навигации",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Deep Linking",
                        "markdown": (
                            "## Deep Linking\n\n"
                            "Позволяет открывать конкретный экран приложения по URL.\n\n"
                            "### Настройка:\n"
                            "```tsx\n"
                            "const linking = {\n"
                            "  prefixes: ['myapp://', 'https://myapp.com'],\n"
                            "  config: {\n"
                            "    screens: {\n"
                            "      Home: '',\n"
                            "      Details: 'details/:id',\n"
                            "      Profile: 'profile',\n"
                            "    },\n"
                            "  },\n"
                            "};\n\n"
                            "<NavigationContainer linking={linking}>\n"
                            "  {/* навигаторы */}\n"
                            "</NavigationContainer>\n"
                            "```\n\n"
                            "### Пример URL:\n"
                            "- `myapp://details/42` → откроет экран Details с id=42\n"
                            "- `https://myapp.com/profile` → откроет экран Profile\n\n"
                            "### Типизация параметров:\n"
                            "```tsx\n"
                            "type RootStackParams = {\n"
                            "  Home: undefined;\n"
                            "  Details: { id: number; title: string };\n"
                            "  Profile: { userId: string } | undefined;\n"
                            "};\n\n"
                            "// В экране:\n"
                            "const { id, title } = route.params as RootStackParams['Details'];\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что такое deep linking в мобильном приложении?",
                        "options": [
                            {"id": "a", "text": "Открытие конкретного экрана приложения по URL-ссылке", "correct": True},
                            {"id": "b", "text": "Глубокое копирование объектов", "correct": False},
                            {"id": "c", "text": "Связывание двух приложений между собой", "correct": False},
                            {"id": "d", "text": "Встраивание веб-страниц в приложение", "correct": False},
                        ],
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "prefixes", "back": "Массив URL-схем для deep linking (например, myapp://)"},
                            {"front": "config.screens", "back": "Маппинг имён экранов на URL-пути"},
                            {"front": "route.params", "back": "Объект с параметрами, переданными при навигации"},
                            {"front": "navigation.navigate()", "back": "Метод для перехода на другой экран"},
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Какой проп NavigationContainer принимает конфигурацию deep linking?",
                        "acceptedAnswers": ["linking"],
                    },
                ],
            },
        ],
    },
    # ===== SECTION 4: Состояние и данные =====
    {
        "title": "Состояние и данные",
        "pos": 3,
        "lessons": [
            {
                "t": "useState и управление состоянием",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Хук useState",
                        "markdown": (
                            "## useState\n\n"
                            "Хук для хранения и обновления локального состояния компонента.\n\n"
                            "### Пример: счётчик\n"
                            "```tsx\n"
                            "import { useState } from 'react';\n"
                            "import { View, Text, Button, StyleSheet } from 'react-native';\n\n"
                            "export default function Counter() {\n"
                            "  const [count, setCount] = useState(0);\n\n"
                            "  return (\n"
                            "    <View style={styles.container}>\n"
                            "      <Text style={styles.count}>{count}</Text>\n"
                            "      <Button title=\"+1\" onPress={() => setCount(count + 1)} />\n"
                            "      <Button title=\"-1\" onPress={() => setCount(count - 1)} />\n"
                            "      <Button title=\"Сброс\" onPress={() => setCount(0)} />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Пример: список задач\n"
                            "```tsx\n"
                            "const [todos, setTodos] = useState<string[]>([]);\n"
                            "const [text, setText] = useState('');\n\n"
                            "const addTodo = () => {\n"
                            "  if (text.trim()) {\n"
                            "    setTodos([...todos, text]);\n"
                            "    setText('');\n"
                            "  }\n"
                            "};\n"
                            "```\n\n"
                            "### Правила:\n"
                            "- Вызывайте хуки только на верхнем уровне компонента\n"
                            "- Не мутируйте состояние напрямую: `setItems([...items, newItem])`"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите useState для счётчика:",
                        "correctOrder": [
                            "const [count, setCount] = useState(0);",
                            "const increment = () => {",
                            "  setCount(count + 1);",
                            "};",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Как правильно добавить элемент в массив в состоянии?",
                        "options": [
                            {"id": "a", "text": "setItems([...items, newItem])", "correct": True},
                            {"id": "b", "text": "items.push(newItem)", "correct": False},
                            {"id": "c", "text": "setItems(items.push(newItem))", "correct": False},
                            {"id": "d", "text": "items = [...items, newItem]", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "useState можно вызывать внутри условий и циклов.",
                        "correct": False,
                    },
                ],
            },
            {
                "t": "useEffect и жизненный цикл",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Хук useEffect",
                        "markdown": (
                            "## useEffect\n\n"
                            "Выполняет побочные эффекты: загрузка данных, подписки, таймеры.\n\n"
                            "### Загрузка данных при монтировании:\n"
                            "```tsx\n"
                            "import { useState, useEffect } from 'react';\n"
                            "import { View, Text, ActivityIndicator } from 'react-native';\n\n"
                            "type Post = { id: number; title: string };\n\n"
                            "export default function PostsScreen() {\n"
                            "  const [posts, setPosts] = useState<Post[]>([]);\n"
                            "  const [loading, setLoading] = useState(true);\n\n"
                            "  useEffect(() => {\n"
                            "    fetch('https://jsonplaceholder.typicode.com/posts')\n"
                            "      .then(res => res.json())\n"
                            "      .then(data => {\n"
                            "        setPosts(data.slice(0, 10));\n"
                            "        setLoading(false);\n"
                            "      });\n"
                            "  }, []); // пустой массив = один раз при монтировании\n\n"
                            "  if (loading) return <ActivityIndicator size=\"large\" />;\n\n"
                            "  return (\n"
                            "    <View>\n"
                            "      {posts.map(p => <Text key={p.id}>{p.title}</Text>)}\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Варианты зависимостей:\n"
                            "- `useEffect(() => {}, [])` — один раз при монтировании\n"
                            "- `useEffect(() => {}, [value])` — при изменении value\n"
                            "- `useEffect(() => { return () => cleanup(); }, [])` — с очисткой"
                        ),
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "useEffect(() => {}, [])", "right": "Выполнится один раз при монтировании"},
                            {"left": "useEffect(() => {}, [count])", "right": "Выполнится при каждом изменении count"},
                            {"left": "useEffect(() => { return () => {} })", "right": "Эффект с функцией очистки"},
                            {"left": "ActivityIndicator", "right": "Индикатор загрузки (спиннер)"},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Чтобы useEffect выполнился только один раз при монтировании, в качестве второго аргумента передаётся пустой ___.",
                        "answer": "массив",
                    },
                ],
            },
            {
                "t": "Context API",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Глобальное состояние через Context",
                        "markdown": (
                            "## Context API\n\n"
                            "Передача данных без пробрасывания через каждый компонент (prop drilling).\n\n"
                            "### Пример: тема приложения\n"
                            "```tsx\n"
                            "import { createContext, useContext, useState, ReactNode } from 'react';\n\n"
                            "type Theme = 'light' | 'dark';\n\n"
                            "const ThemeContext = createContext<{\n"
                            "  theme: Theme;\n"
                            "  toggleTheme: () => void;\n"
                            "}>({ theme: 'light', toggleTheme: () => {} });\n\n"
                            "export function ThemeProvider({ children }: { children: ReactNode }) {\n"
                            "  const [theme, setTheme] = useState<Theme>('light');\n"
                            "  const toggleTheme = () => setTheme(t => t === 'light' ? 'dark' : 'light');\n\n"
                            "  return (\n"
                            "    <ThemeContext.Provider value={{ theme, toggleTheme }}>\n"
                            "      {children}\n"
                            "    </ThemeContext.Provider>\n"
                            "  );\n"
                            "}\n\n"
                            "export const useTheme = () => useContext(ThemeContext);\n"
                            "```\n\n"
                            "### Использование:\n"
                            "```tsx\n"
                            "function SettingsScreen() {\n"
                            "  const { theme, toggleTheme } = useTheme();\n"
                            "  return (\n"
                            "    <View style={{ backgroundColor: theme === 'dark' ? '#000' : '#fff' }}>\n"
                            "      <Button title={`Тема: ${theme}`} onPress={toggleTheme} />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Создать контекст через createContext",
                            "Создать Provider-компонент с состоянием",
                            "Обернуть приложение в Provider",
                            "Вызвать useContext в дочернем компоненте",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какую проблему решает Context API?",
                        "options": [
                            {"id": "a", "text": "Prop drilling — передачу пропов через много уровней", "correct": True},
                            {"id": "b", "text": "Работу с базой данных", "correct": False},
                            {"id": "c", "text": "Стилизацию компонентов", "correct": False},
                            {"id": "d", "text": "Навигацию между экранами", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "AsyncStorage",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Локальное хранилище данных",
                        "markdown": (
                            "## AsyncStorage\n\n"
                            "Аналог localStorage для React Native — хранит данные на устройстве.\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install @react-native-async-storage/async-storage\n"
                            "```\n\n"
                            "### Использование:\n"
                            "```tsx\n"
                            "import AsyncStorage from '@react-native-async-storage/async-storage';\n\n"
                            "// Сохранить строку\n"
                            "await AsyncStorage.setItem('username', 'Azamat');\n\n"
                            "// Прочитать\n"
                            "const username = await AsyncStorage.getItem('username');\n\n"
                            "// Сохранить объект\n"
                            "await AsyncStorage.setItem('user', JSON.stringify({ name: 'Azamat', age: 25 }));\n\n"
                            "// Прочитать объект\n"
                            "const raw = await AsyncStorage.getItem('user');\n"
                            "const user = raw ? JSON.parse(raw) : null;\n\n"
                            "// Удалить\n"
                            "await AsyncStorage.removeItem('username');\n\n"
                            "// Очистить всё\n"
                            "await AsyncStorage.clear();\n"
                            "```\n\n"
                            "### Когда использовать:\n"
                            "- Сохранение настроек (тема, язык)\n"
                            "- Токены авторизации\n"
                            "- Кеш данных\n"
                            "- Onboarding (показан ли туториал)"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Как сохранить объект в AsyncStorage?",
                        "options": [
                            {"id": "a", "text": "AsyncStorage.setItem('key', JSON.stringify(obj))", "correct": True},
                            {"id": "b", "text": "AsyncStorage.setItem('key', obj)", "correct": False},
                            {"id": "c", "text": "AsyncStorage.setObject('key', obj)", "correct": False},
                            {"id": "d", "text": "AsyncStorage.save('key', obj)", "correct": False},
                        ],
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "AsyncStorage.setItem(key, value)", "back": "Сохранить строку по ключу"},
                            {"front": "AsyncStorage.getItem(key)", "back": "Прочитать значение по ключу (возвращает string | null)"},
                            {"front": "AsyncStorage.removeItem(key)", "back": "Удалить значение по ключу"},
                            {"front": "AsyncStorage.clear()", "back": "Очистить всё хранилище"},
                        ],
                    },
                ],
            },
            {
                "t": "Работа с API (fetch)",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Загрузка данных с сервера",
                        "markdown": (
                            "## Fetch API\n\n"
                            "React Native поддерживает `fetch` из коробки.\n\n"
                            "### Кастомный хук для загрузки:\n"
                            "```tsx\n"
                            "import { useState, useEffect } from 'react';\n\n"
                            "function useFetch<T>(url: string) {\n"
                            "  const [data, setData] = useState<T | null>(null);\n"
                            "  const [loading, setLoading] = useState(true);\n"
                            "  const [error, setError] = useState<string | null>(null);\n\n"
                            "  useEffect(() => {\n"
                            "    const fetchData = async () => {\n"
                            "      try {\n"
                            "        const res = await fetch(url);\n"
                            "        if (!res.ok) throw new Error(`HTTP ${res.status}`);\n"
                            "        const json = await res.json();\n"
                            "        setData(json);\n"
                            "      } catch (e: any) {\n"
                            "        setError(e.message);\n"
                            "      } finally {\n"
                            "        setLoading(false);\n"
                            "      }\n"
                            "    };\n"
                            "    fetchData();\n"
                            "  }, [url]);\n\n"
                            "  return { data, loading, error };\n"
                            "}\n"
                            "```\n\n"
                            "### POST-запрос:\n"
                            "```tsx\n"
                            "const createPost = async (title: string, body: string) => {\n"
                            "  const res = await fetch('https://api.example.com/posts', {\n"
                            "    method: 'POST',\n"
                            "    headers: { 'Content-Type': 'application/json' },\n"
                            "    body: JSON.stringify({ title, body }),\n"
                            "  });\n"
                            "  return res.json();\n"
                            "};\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите fetch-запрос для загрузки данных:",
                        "correctOrder": [
                            "const res = await fetch(url);",
                            "if (!res.ok) throw new Error('Ошибка');",
                            "const data = await res.json();",
                            "setData(data);",
                        ],
                    },
                    {
                        "type": "multi-select",
                        "question": "Какие состояния обычно нужны для работы с API?",
                        "options": [
                            {"id": "a", "text": "data — загруженные данные", "correct": True},
                            {"id": "b", "text": "loading — индикатор загрузки", "correct": True},
                            {"id": "c", "text": "error — текст ошибки", "correct": True},
                            {"id": "d", "text": "theme — тема приложения", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "React Query (TanStack Query)",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Управление серверным состоянием",
                        "markdown": (
                            "## TanStack Query (React Query)\n\n"
                            "Библиотека для загрузки, кеширования и синхронизации данных с сервером.\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npm install @tanstack/react-query\n"
                            "```\n\n"
                            "### Настройка:\n"
                            "```tsx\n"
                            "import { QueryClient, QueryClientProvider } from '@tanstack/react-query';\n\n"
                            "const queryClient = new QueryClient();\n\n"
                            "export default function App() {\n"
                            "  return (\n"
                            "    <QueryClientProvider client={queryClient}>\n"
                            "      <NavigationContainer>\n"
                            "        {/* ... */}\n"
                            "      </NavigationContainer>\n"
                            "    </QueryClientProvider>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Использование:\n"
                            "```tsx\n"
                            "import { useQuery, useMutation } from '@tanstack/react-query';\n\n"
                            "function PostsScreen() {\n"
                            "  const { data, isLoading, error, refetch } = useQuery({\n"
                            "    queryKey: ['posts'],\n"
                            "    queryFn: () => fetch('/api/posts').then(r => r.json()),\n"
                            "  });\n\n"
                            "  if (isLoading) return <ActivityIndicator />;\n"
                            "  if (error) return <Text>Ошибка: {error.message}</Text>;\n\n"
                            "  return (\n"
                            "    <FlatList data={data} renderItem={...}\n"
                            "      refreshing={isLoading}\n"
                            "      onRefresh={refetch}\n"
                            "    />\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Преимущества:\n"
                            "- Автоматическое кеширование\n"
                            "- Pull-to-refresh одной строкой\n"
                            "- Автоматический refetch при возврате на экран\n"
                            "- Optimistic updates"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что делает queryKey в useQuery?",
                        "options": [
                            {"id": "a", "text": "Уникально идентифицирует запрос для кеширования", "correct": True},
                            {"id": "b", "text": "Задаёт URL для запроса", "correct": False},
                            {"id": "c", "text": "Определяет HTTP-метод", "correct": False},
                            {"id": "d", "text": "Устанавливает заголовки запроса", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "useQuery", "right": "Загрузка данных (GET)"},
                            {"left": "useMutation", "right": "Изменение данных (POST/PUT/DELETE)"},
                            {"left": "queryKey", "right": "Ключ кеширования запроса"},
                            {"left": "queryFn", "right": "Функция, выполняющая запрос"},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "React Query автоматически кеширует результаты запросов и обновляет их при возврате на экран.",
                        "correct": True,
                    },
                ],
            },
        ],
    },
    # ===== SECTION 5: Нативные возможности =====
    {
        "title": "Нативные возможности",
        "pos": 4,
        "lessons": [
            {
                "t": "Камера и галерея",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Работа с камерой",
                        "markdown": (
                            "## Камера и выбор изображений\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install expo-image-picker expo-camera\n"
                            "```\n\n"
                            "### Выбор из галереи:\n"
                            "```tsx\n"
                            "import * as ImagePicker from 'expo-image-picker';\n"
                            "import { useState } from 'react';\n"
                            "import { View, Image, Button } from 'react-native';\n\n"
                            "export default function PhotoScreen() {\n"
                            "  const [image, setImage] = useState<string | null>(null);\n\n"
                            "  const pickImage = async () => {\n"
                            "    const result = await ImagePicker.launchImageLibraryAsync({\n"
                            "      mediaTypes: ImagePicker.MediaTypeOptions.Images,\n"
                            "      allowsEditing: true,\n"
                            "      aspect: [1, 1],\n"
                            "      quality: 0.8,\n"
                            "    });\n\n"
                            "    if (!result.canceled) {\n"
                            "      setImage(result.assets[0].uri);\n"
                            "    }\n"
                            "  };\n\n"
                            "  const takePhoto = async () => {\n"
                            "    const permission = await ImagePicker.requestCameraPermissionsAsync();\n"
                            "    if (!permission.granted) return;\n\n"
                            "    const result = await ImagePicker.launchCameraAsync({\n"
                            "      allowsEditing: true,\n"
                            "      quality: 0.8,\n"
                            "    });\n\n"
                            "    if (!result.canceled) {\n"
                            "      setImage(result.assets[0].uri);\n"
                            "    }\n"
                            "  };\n\n"
                            "  return (\n"
                            "    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>\n"
                            "      {image && <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}\n"
                            "      <Button title=\"Выбрать из галереи\" onPress={pickImage} />\n"
                            "      <Button title=\"Сделать фото\" onPress={takePhoto} />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой пакет используется для выбора изображений в Expo?",
                        "options": [
                            {"id": "a", "text": "expo-image-picker", "correct": True},
                            {"id": "b", "text": "react-native-camera", "correct": False},
                            {"id": "c", "text": "expo-gallery", "correct": False},
                            {"id": "d", "text": "react-native-image-picker", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Для доступа к камере в Expo необходимо запросить разрешение у пользователя.",
                        "correct": True,
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Метод launchImageLibraryAsync() открывает ___ устройства для выбора изображения.",
                        "answer": "галерею",
                    },
                ],
            },
            {
                "t": "Геолокация",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Определение местоположения",
                        "markdown": (
                            "## Геолокация\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install expo-location\n"
                            "```\n\n"
                            "### Получение координат:\n"
                            "```tsx\n"
                            "import * as Location from 'expo-location';\n"
                            "import { useState, useEffect } from 'react';\n"
                            "import { View, Text } from 'react-native';\n\n"
                            "export default function LocationScreen() {\n"
                            "  const [location, setLocation] = useState<Location.LocationObject | null>(null);\n"
                            "  const [error, setError] = useState<string | null>(null);\n\n"
                            "  useEffect(() => {\n"
                            "    (async () => {\n"
                            "      const { status } = await Location.requestForegroundPermissionsAsync();\n"
                            "      if (status !== 'granted') {\n"
                            "        setError('Доступ к геолокации запрещён');\n"
                            "        return;\n"
                            "      }\n\n"
                            "      const loc = await Location.getCurrentPositionAsync({});\n"
                            "      setLocation(loc);\n"
                            "    })();\n"
                            "  }, []);\n\n"
                            "  return (\n"
                            "    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>\n"
                            "      {error ? <Text>{error}</Text> : null}\n"
                            "      {location ? (\n"
                            "        <Text>\n"
                            "          Широта: {location.coords.latitude}{'\\n'}\n"
                            "          Долгота: {location.coords.longitude}\n"
                            "        </Text>\n"
                            "      ) : <Text>Определение местоположения...</Text>}\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Типы разрешений:\n"
                            "- **Foreground** — только когда приложение открыто\n"
                            "- **Background** — даже когда приложение свёрнуто"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой метод используется для запроса разрешения на геолокацию?",
                        "options": [
                            {"id": "a", "text": "Location.requestForegroundPermissionsAsync()", "correct": True},
                            {"id": "b", "text": "Location.getPermission()", "correct": False},
                            {"id": "c", "text": "navigator.geolocation.requestPermission()", "correct": False},
                            {"id": "d", "text": "Permissions.askAsync('location')", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "Foreground Permission", "right": "Геолокация только при открытом приложении"},
                            {"left": "Background Permission", "right": "Геолокация даже при свёрнутом приложении"},
                            {"left": "coords.latitude", "right": "Географическая широта"},
                            {"left": "coords.longitude", "right": "Географическая долгота"},
                        ],
                    },
                ],
            },
            {
                "t": "Push-уведомления",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Настройка push-уведомлений",
                        "markdown": (
                            "## Push-уведомления с Expo\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install expo-notifications expo-device expo-constants\n"
                            "```\n\n"
                            "### Регистрация токена:\n"
                            "```tsx\n"
                            "import * as Notifications from 'expo-notifications';\n"
                            "import * as Device from 'expo-device';\n"
                            "import Constants from 'expo-constants';\n\n"
                            "async function registerForPushNotifications() {\n"
                            "  if (!Device.isDevice) {\n"
                            "    alert('Push-уведомления работают только на реальном устройстве');\n"
                            "    return;\n"
                            "  }\n\n"
                            "  const { status } = await Notifications.requestPermissionsAsync();\n"
                            "  if (status !== 'granted') {\n"
                            "    alert('Разрешение на уведомления не получено');\n"
                            "    return;\n"
                            "  }\n\n"
                            "  const projectId = Constants.expoConfig?.extra?.eas?.projectId;\n"
                            "  const token = (await Notifications.getExpoPushTokenAsync({ projectId })).data;\n"
                            "  console.log('Push token:', token);\n"
                            "  // Отправьте token на ваш сервер\n"
                            "}\n"
                            "```\n\n"
                            "### Обработка входящих уведомлений:\n"
                            "```tsx\n"
                            "Notifications.setNotificationHandler({\n"
                            "  handleNotification: async () => ({\n"
                            "    shouldShowAlert: true,\n"
                            "    shouldPlaySound: true,\n"
                            "    shouldSetBadge: true,\n"
                            "  }),\n"
                            "});\n"
                            "```"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Установить expo-notifications",
                            "Проверить, что это реальное устройство",
                            "Запросить разрешение на уведомления",
                            "Получить push-токен",
                            "Отправить токен на сервер",
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Push-уведомления работают на эмуляторах и симуляторах так же, как на реальных устройствах.",
                        "correct": False,
                    },
                ],
            },
            {
                "t": "Разрешения (Permissions)",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Система разрешений",
                        "markdown": (
                            "## Разрешения в React Native\n\n"
                            "Приложение должно запрашивать разрешения на доступ к функциям устройства.\n\n"
                            "### Паттерн запроса:\n"
                            "```tsx\n"
                            "import * as ImagePicker from 'expo-image-picker';\n"
                            "import * as Location from 'expo-location';\n"
                            "import * as Notifications from 'expo-notifications';\n\n"
                            "// 1. Проверить текущий статус\n"
                            "const { status } = await ImagePicker.getMediaLibraryPermissionsAsync();\n\n"
                            "// 2. Запросить, если не предоставлено\n"
                            "if (status !== 'granted') {\n"
                            "  const result = await ImagePicker.requestMediaLibraryPermissionsAsync();\n"
                            "  if (!result.granted) {\n"
                            "    // Показать объяснение, зачем нужно разрешение\n"
                            "    Alert.alert(\n"
                            "      'Нужен доступ к фото',\n"
                            "      'Разрешите доступ к галерее для выбора аватара',\n"
                            "      [{ text: 'Настройки', onPress: () => Linking.openSettings() }]\n"
                            "    );\n"
                            "  }\n"
                            "}\n"
                            "```\n\n"
                            "### Виды разрешений:\n"
                            "| Разрешение | Пакет |\n"
                            "| --- | --- |\n"
                            "| Камера | expo-camera, expo-image-picker |\n"
                            "| Галерея | expo-image-picker |\n"
                            "| Геолокация | expo-location |\n"
                            "| Уведомления | expo-notifications |\n"
                            "| Контакты | expo-contacts |\n"
                            "| Микрофон | expo-av |"
                        ),
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "granted", "back": "Разрешение предоставлено пользователем"},
                            {"front": "denied", "back": "Разрешение отклонено пользователем"},
                            {"front": "undetermined", "back": "Разрешение ещё не запрашивалось"},
                            {"front": "Linking.openSettings()", "back": "Открывает системные настройки приложения"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Что делать, если пользователь отклонил разрешение?",
                        "options": [
                            {"id": "a", "text": "Объяснить зачем нужно и предложить открыть настройки", "correct": True},
                            {"id": "b", "text": "Запрашивать повторно в бесконечном цикле", "correct": False},
                            {"id": "c", "text": "Получить доступ без разрешения", "correct": False},
                            {"id": "d", "text": "Закрыть приложение", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Анимации (Animated и Reanimated)",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Анимации в React Native",
                        "markdown": (
                            "## Анимации\n\n"
                            "### Animated API (встроенный):\n"
                            "```tsx\n"
                            "import { useRef, useEffect } from 'react';\n"
                            "import { Animated, View, StyleSheet } from 'react-native';\n\n"
                            "export default function FadeIn() {\n"
                            "  const fadeAnim = useRef(new Animated.Value(0)).current;\n\n"
                            "  useEffect(() => {\n"
                            "    Animated.timing(fadeAnim, {\n"
                            "      toValue: 1,\n"
                            "      duration: 1000,\n"
                            "      useNativeDriver: true,\n"
                            "    }).start();\n"
                            "  }, []);\n\n"
                            "  return (\n"
                            "    <Animated.View style={[styles.box, { opacity: fadeAnim }]}>\n"
                            "      {/* контент */}\n"
                            "    </Animated.View>\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### React Native Reanimated (продвинутый):\n"
                            "```bash\n"
                            "npx expo install react-native-reanimated\n"
                            "```\n"
                            "```tsx\n"
                            "import Animated, {\n"
                            "  useSharedValue,\n"
                            "  useAnimatedStyle,\n"
                            "  withSpring,\n"
                            "} from 'react-native-reanimated';\n\n"
                            "export default function SpringBox() {\n"
                            "  const scale = useSharedValue(1);\n\n"
                            "  const animatedStyle = useAnimatedStyle(() => ({\n"
                            "    transform: [{ scale: scale.value }],\n"
                            "  }));\n\n"
                            "  const onPress = () => {\n"
                            "    scale.value = withSpring(scale.value === 1 ? 1.5 : 1);\n"
                            "  };\n\n"
                            "  return (\n"
                            "    <Animated.View style={[styles.box, animatedStyle]}\n"
                            "      onTouchEnd={onPress} />\n"
                            "  );\n"
                            "}\n"
                            "```\n\n"
                            "### Когда что использовать:\n"
                            "- **Animated** — простые анимации (fade, slide)\n"
                            "- **Reanimated** — сложные жесты, spring-анимации, gesture-driven UI"
                        ),
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "Animated.timing", "right": "Линейная анимация с заданной длительностью"},
                            {"left": "Animated.spring", "right": "Пружинная анимация"},
                            {"left": "useNativeDriver: true", "right": "Запуск анимации на нативном потоке"},
                            {"left": "useSharedValue (Reanimated)", "right": "Анимированное значение на UI-потоке"},
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Зачем нужен useNativeDriver: true?",
                        "options": [
                            {"id": "a", "text": "Запускает анимацию на нативном потоке для плавности 60fps", "correct": True},
                            {"id": "b", "text": "Устанавливает нативные модули", "correct": False},
                            {"id": "c", "text": "Подключает драйвер базы данных", "correct": False},
                            {"id": "d", "text": "Включает аппаратное ускорение GPS", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "React Native Reanimated выполняет анимации на UI-потоке, что обеспечивает лучшую производительность.",
                        "correct": True,
                    },
                ],
            },
        ],
    },
    # ===== SECTION 6: Формы и аутентификация =====
    {
        "title": "Формы и аутентификация",
        "pos": 5,
        "lessons": [
            {
                "t": "TextInput и формы",
                "xp": 25,
                "steps": [
                    {
                        "type": "info",
                        "title": "Ввод текста в React Native",
                        "markdown": (
                            "## TextInput\n\n"
                            "```tsx\n"
                            "import { useState } from 'react';\n"
                            "import { View, TextInput, Text, StyleSheet } from 'react-native';\n\n"
                            "export default function FormScreen() {\n"
                            "  const [name, setName] = useState('');\n"
                            "  const [email, setEmail] = useState('');\n"
                            "  const [password, setPassword] = useState('');\n\n"
                            "  return (\n"
                            "    <View style={styles.container}>\n"
                            "      <TextInput\n"
                            "        style={styles.input}\n"
                            "        placeholder=\"Имя\"\n"
                            "        value={name}\n"
                            "        onChangeText={setName}\n"
                            "        autoCapitalize=\"words\"\n"
                            "      />\n\n"
                            "      <TextInput\n"
                            "        style={styles.input}\n"
                            "        placeholder=\"Email\"\n"
                            "        value={email}\n"
                            "        onChangeText={setEmail}\n"
                            "        keyboardType=\"email-address\"\n"
                            "        autoCapitalize=\"none\"\n"
                            "      />\n\n"
                            "      <TextInput\n"
                            "        style={styles.input}\n"
                            "        placeholder=\"Пароль\"\n"
                            "        value={password}\n"
                            "        onChangeText={setPassword}\n"
                            "        secureTextEntry\n"
                            "      />\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n\n"
                            "const styles = StyleSheet.create({\n"
                            "  container: { padding: 16, gap: 12 },\n"
                            "  input: {\n"
                            "    borderWidth: 1,\n"
                            "    borderColor: '#ddd',\n"
                            "    borderRadius: 8,\n"
                            "    padding: 12,\n"
                            "    fontSize: 16,\n"
                            "  },\n"
                            "});\n"
                            "```\n\n"
                            "### Полезные пропы:\n"
                            "- `secureTextEntry` — скрывает ввод (для паролей)\n"
                            "- `keyboardType` — тип клавиатуры (email-address, numeric, phone-pad)\n"
                            "- `autoCapitalize` — автозаглавные (none, words, sentences)\n"
                            "- `returnKeyType` — кнопка Enter (done, next, search, go)\n"
                            "- `multiline` — многострочный ввод"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой проп скрывает вводимый текст (для паролей)?",
                        "options": [
                            {"id": "a", "text": "secureTextEntry", "correct": True},
                            {"id": "b", "text": "password", "correct": False},
                            {"id": "c", "text": "hideText", "correct": False},
                            {"id": "d", "text": "type=\"password\"", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "keyboardType=\"email-address\"", "right": "Клавиатура с символом @"},
                            {"left": "keyboardType=\"numeric\"", "right": "Только цифровая клавиатура"},
                            {"left": "autoCapitalize=\"none\"", "right": "Без автозаглавных букв"},
                            {"left": "multiline", "right": "Многострочное текстовое поле"},
                        ],
                    },
                    {
                        "type": "fill-blank",
                        "sentence": "Проп ___ в TextInput определяет функцию-обработчик изменения текста.",
                        "answer": "onChangeText",
                    },
                ],
            },
            {
                "t": "Управляемые формы",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Форма регистрации",
                        "markdown": (
                            "## Управляемая форма\n\n"
                            "```tsx\n"
                            "import { useState } from 'react';\n"
                            "import { View, TextInput, TouchableOpacity, Text, Alert, StyleSheet } from 'react-native';\n\n"
                            "type FormData = { name: string; email: string; password: string };\n"
                            "type Errors = Partial<Record<keyof FormData, string>>;\n\n"
                            "export default function RegisterForm() {\n"
                            "  const [form, setForm] = useState<FormData>({ name: '', email: '', password: '' });\n"
                            "  const [errors, setErrors] = useState<Errors>({});\n\n"
                            "  const update = (field: keyof FormData, value: string) => {\n"
                            "    setForm({ ...form, [field]: value });\n"
                            "    setErrors({ ...errors, [field]: undefined });\n"
                            "  };\n\n"
                            "  const validate = (): boolean => {\n"
                            "    const e: Errors = {};\n"
                            "    if (!form.name.trim()) e.name = 'Введите имя';\n"
                            "    if (!form.email.includes('@')) e.email = 'Некорректный email';\n"
                            "    if (form.password.length < 6) e.password = 'Минимум 6 символов';\n"
                            "    setErrors(e);\n"
                            "    return Object.keys(e).length === 0;\n"
                            "  };\n\n"
                            "  const handleSubmit = () => {\n"
                            "    if (validate()) {\n"
                            "      Alert.alert('Успех', `Добро пожаловать, ${form.name}!`);\n"
                            "    }\n"
                            "  };\n\n"
                            "  return (\n"
                            "    <View style={styles.container}>\n"
                            "      <TextInput style={[styles.input, errors.name && styles.error]}\n"
                            "        placeholder=\"Имя\" value={form.name}\n"
                            "        onChangeText={(v) => update('name', v)} />\n"
                            "      {errors.name && <Text style={styles.errorText}>{errors.name}</Text>}\n\n"
                            "      <TextInput style={[styles.input, errors.email && styles.error]}\n"
                            "        placeholder=\"Email\" value={form.email}\n"
                            "        onChangeText={(v) => update('email', v)}\n"
                            "        keyboardType=\"email-address\" autoCapitalize=\"none\" />\n"
                            "      {errors.email && <Text style={styles.errorText}>{errors.email}</Text>}\n\n"
                            "      <TextInput style={[styles.input, errors.password && styles.error]}\n"
                            "        placeholder=\"Пароль\" value={form.password}\n"
                            "        onChangeText={(v) => update('password', v)}\n"
                            "        secureTextEntry />\n"
                            "      {errors.password && <Text style={styles.errorText}>{errors.password}</Text>}\n\n"
                            "      <TouchableOpacity style={styles.button} onPress={handleSubmit}>\n"
                            "        <Text style={styles.buttonText}>Зарегистрироваться</Text>\n"
                            "      </TouchableOpacity>\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "code-puzzle",
                        "instructions": "Соберите функцию валидации email:",
                        "correctOrder": [
                            "const validate = (email: string): boolean => {",
                            "  if (!email.includes('@')) {",
                            "    setError('Некорректный email');",
                            "    return false;",
                            "  }",
                            "  return true;",
                            "};",
                        ],
                    },
                    {
                        "type": "multi-select",
                        "question": "Какие проверки стоит делать при валидации формы регистрации?",
                        "options": [
                            {"id": "a", "text": "Проверка формата email", "correct": True},
                            {"id": "b", "text": "Минимальная длина пароля", "correct": True},
                            {"id": "c", "text": "Непустое имя", "correct": True},
                            {"id": "d", "text": "Проверка скорости интернета", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Валидация форм",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Продвинутая валидация с Zod",
                        "markdown": (
                            "## Валидация с Zod\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npm install zod\n"
                            "```\n\n"
                            "### Схема валидации:\n"
                            "```tsx\n"
                            "import { z } from 'zod';\n\n"
                            "const registerSchema = z.object({\n"
                            "  name: z.string().min(2, 'Имя: минимум 2 символа'),\n"
                            "  email: z.string().email('Некорректный email'),\n"
                            "  password: z.string()\n"
                            "    .min(8, 'Пароль: минимум 8 символов')\n"
                            "    .regex(/[A-Z]/, 'Нужна хотя бы одна заглавная буква')\n"
                            "    .regex(/[0-9]/, 'Нужна хотя бы одна цифра'),\n"
                            "  confirmPassword: z.string(),\n"
                            "}).refine((data) => data.password === data.confirmPassword, {\n"
                            "  message: 'Пароли не совпадают',\n"
                            "  path: ['confirmPassword'],\n"
                            "});\n\n"
                            "type RegisterForm = z.infer<typeof registerSchema>;\n"
                            "```\n\n"
                            "### Использование:\n"
                            "```tsx\n"
                            "const handleSubmit = () => {\n"
                            "  const result = registerSchema.safeParse(form);\n"
                            "  if (!result.success) {\n"
                            "    const fieldErrors: Record<string, string> = {};\n"
                            "    result.error.errors.forEach(e => {\n"
                            "      fieldErrors[e.path[0]] = e.message;\n"
                            "    });\n"
                            "    setErrors(fieldErrors);\n"
                            "  } else {\n"
                            "    // Отправить данные на сервер\n"
                            "    submitForm(result.data);\n"
                            "  }\n"
                            "};\n"
                            "```"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что делает метод safeParse в Zod?",
                        "options": [
                            {"id": "a", "text": "Валидирует данные и возвращает результат без выброса исключения", "correct": True},
                            {"id": "b", "text": "Парсит JSON-строку", "correct": False},
                            {"id": "c", "text": "Сохраняет данные в хранилище", "correct": False},
                            {"id": "d", "text": "Отправляет данные на сервер", "correct": False},
                        ],
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "z.string().email()", "back": "Валидация email-формата"},
                            {"front": "z.string().min(n)", "back": "Минимальная длина строки"},
                            {"front": ".refine()", "back": "Кастомная проверка (например, совпадение паролей)"},
                            {"front": "safeParse()", "back": "Безопасная валидация без исключений"},
                        ],
                    },
                ],
            },
            {
                "t": "JWT-аутентификация",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Авторизация в мобильном приложении",
                        "markdown": (
                            "## JWT-аутентификация\n\n"
                            "### Контекст авторизации:\n"
                            "```tsx\n"
                            "import { createContext, useContext, useState, useEffect, ReactNode } from 'react';\n"
                            "import AsyncStorage from '@react-native-async-storage/async-storage';\n\n"
                            "type AuthContextType = {\n"
                            "  token: string | null;\n"
                            "  login: (email: string, password: string) => Promise<void>;\n"
                            "  logout: () => Promise<void>;\n"
                            "  isLoading: boolean;\n"
                            "};\n\n"
                            "const AuthContext = createContext<AuthContextType | null>(null);\n\n"
                            "export function AuthProvider({ children }: { children: ReactNode }) {\n"
                            "  const [token, setToken] = useState<string | null>(null);\n"
                            "  const [isLoading, setIsLoading] = useState(true);\n\n"
                            "  useEffect(() => {\n"
                            "    AsyncStorage.getItem('token').then(t => {\n"
                            "      setToken(t);\n"
                            "      setIsLoading(false);\n"
                            "    });\n"
                            "  }, []);\n\n"
                            "  const login = async (email: string, password: string) => {\n"
                            "    const res = await fetch('https://api.example.com/login', {\n"
                            "      method: 'POST',\n"
                            "      headers: { 'Content-Type': 'application/json' },\n"
                            "      body: JSON.stringify({ email, password }),\n"
                            "    });\n"
                            "    const { token } = await res.json();\n"
                            "    await AsyncStorage.setItem('token', token);\n"
                            "    setToken(token);\n"
                            "  };\n\n"
                            "  const logout = async () => {\n"
                            "    await AsyncStorage.removeItem('token');\n"
                            "    setToken(null);\n"
                            "  };\n\n"
                            "  return (\n"
                            "    <AuthContext.Provider value={{ token, login, logout, isLoading }}>\n"
                            "      {children}\n"
                            "    </AuthContext.Provider>\n"
                            "  );\n"
                            "}\n\n"
                            "export const useAuth = () => useContext(AuthContext)!;\n"
                            "```\n\n"
                            "### Защищённая навигация:\n"
                            "```tsx\n"
                            "function AppNavigator() {\n"
                            "  const { token, isLoading } = useAuth();\n"
                            "  if (isLoading) return <ActivityIndicator />;\n\n"
                            "  return (\n"
                            "    <Stack.Navigator>\n"
                            "      {token ? (\n"
                            "        <Stack.Screen name=\"Home\" component={HomeScreen} />\n"
                            "      ) : (\n"
                            "        <Stack.Screen name=\"Login\" component={LoginScreen} />\n"
                            "      )}\n"
                            "    </Stack.Navigator>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Пользователь вводит email и пароль",
                            "Приложение отправляет POST-запрос на сервер",
                            "Сервер проверяет данные и возвращает JWT-токен",
                            "Токен сохраняется в AsyncStorage",
                            "Приложение перенаправляет на главный экран",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Где безопаснее всего хранить JWT-токен в React Native?",
                        "options": [
                            {"id": "a", "text": "AsyncStorage (или SecureStore для повышенной безопасности)", "correct": True},
                            {"id": "b", "text": "В глобальной переменной", "correct": False},
                            {"id": "c", "text": "В URL параметрах", "correct": False},
                            {"id": "d", "text": "В cookies", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "При отсутствии токена приложение должно показывать экран авторизации вместо главного экрана.",
                        "correct": True,
                    },
                ],
            },
            {
                "t": "Биометрическая аутентификация",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Face ID и отпечаток пальца",
                        "markdown": (
                            "## Биометрия с expo-local-authentication\n\n"
                            "### Установка:\n"
                            "```bash\n"
                            "npx expo install expo-local-authentication\n"
                            "```\n\n"
                            "### Использование:\n"
                            "```tsx\n"
                            "import * as LocalAuthentication from 'expo-local-authentication';\n"
                            "import { useState } from 'react';\n"
                            "import { View, Text, TouchableOpacity, Alert, StyleSheet } from 'react-native';\n\n"
                            "export default function BiometricLogin() {\n"
                            "  const [isAuthenticated, setIsAuthenticated] = useState(false);\n\n"
                            "  const authenticate = async () => {\n"
                            "    // 1. Проверить доступность биометрии\n"
                            "    const hasHardware = await LocalAuthentication.hasHardwareAsync();\n"
                            "    if (!hasHardware) {\n"
                            "      Alert.alert('Ошибка', 'Биометрия не поддерживается');\n"
                            "      return;\n"
                            "    }\n\n"
                            "    // 2. Проверить наличие сохранённых данных\n"
                            "    const isEnrolled = await LocalAuthentication.isEnrolledAsync();\n"
                            "    if (!isEnrolled) {\n"
                            "      Alert.alert('Ошибка', 'Биометрические данные не настроены');\n"
                            "      return;\n"
                            "    }\n\n"
                            "    // 3. Запустить аутентификацию\n"
                            "    const result = await LocalAuthentication.authenticateAsync({\n"
                            "      promptMessage: 'Войдите с помощью биометрии',\n"
                            "      cancelLabel: 'Отмена',\n"
                            "      fallbackLabel: 'Использовать пароль',\n"
                            "    });\n\n"
                            "    if (result.success) {\n"
                            "      setIsAuthenticated(true);\n"
                            "    }\n"
                            "  };\n\n"
                            "  return (\n"
                            "    <View style={styles.container}>\n"
                            "      <TouchableOpacity style={styles.button} onPress={authenticate}>\n"
                            "        <Text style={styles.text}>Войти по биометрии</Text>\n"
                            "      </TouchableOpacity>\n"
                            "    </View>\n"
                            "  );\n"
                            "}\n"
                            "```"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Проверить наличие биометрического оборудования",
                            "Проверить, настроена ли биометрия на устройстве",
                            "Вызвать authenticateAsync с параметрами",
                            "Обработать результат аутентификации",
                        ],
                    },
                    {
                        "type": "quiz",
                        "question": "Какой пакет используется для биометрической аутентификации в Expo?",
                        "options": [
                            {"id": "a", "text": "expo-local-authentication", "correct": True},
                            {"id": "b", "text": "expo-biometrics", "correct": False},
                            {"id": "c", "text": "react-native-fingerprint", "correct": False},
                            {"id": "d", "text": "expo-face-id", "correct": False},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Перед запуском биометрической аутентификации нужно проверить, поддерживает ли устройство биометрию.",
                        "correct": True,
                    },
                ],
            },
        ],
    },
    # ===== SECTION 7: Публикация =====
    {
        "title": "Публикация",
        "pos": 6,
        "lessons": [
            {
                "t": "Сборка для iOS и Android",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "EAS Build — облачная сборка",
                        "markdown": (
                            "## Сборка приложения\n\n"
                            "### Установка EAS CLI:\n"
                            "```bash\n"
                            "npm install -g eas-cli\n"
                            "eas login\n"
                            "```\n\n"
                            "### Настройка:\n"
                            "```bash\n"
                            "eas build:configure\n"
                            "```\n\n"
                            "Создаёт `eas.json`:\n"
                            "```json\n"
                            "{\n"
                            "  \"build\": {\n"
                            "    \"development\": {\n"
                            "      \"developmentClient\": true,\n"
                            "      \"distribution\": \"internal\"\n"
                            "    },\n"
                            "    \"preview\": {\n"
                            "      \"distribution\": \"internal\"\n"
                            "    },\n"
                            "    \"production\": {}\n"
                            "  }\n"
                            "}\n"
                            "```\n\n"
                            "### Сборка:\n"
                            "```bash\n"
                            "# iOS (нужен Apple Developer Account)\n"
                            "eas build --platform ios\n\n"
                            "# Android\n"
                            "eas build --platform android\n\n"
                            "# Обе платформы\n"
                            "eas build --platform all\n"
                            "```\n\n"
                            "### Профили сборки:\n"
                            "- **development** — dev client для разработки\n"
                            "- **preview** — тестовая сборка (APK / ad hoc IPA)\n"
                            "- **production** — для публикации в магазин"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Какой командой собрать приложение для обеих платформ?",
                        "options": [
                            {"id": "a", "text": "eas build --platform all", "correct": True},
                            {"id": "b", "text": "expo build", "correct": False},
                            {"id": "c", "text": "npx react-native build", "correct": False},
                            {"id": "d", "text": "npm run build:mobile", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "development", "right": "Сборка для разработки с dev client"},
                            {"left": "preview", "right": "Тестовая сборка для внутреннего распространения"},
                            {"left": "production", "right": "Финальная сборка для публикации в магазин"},
                            {"left": "eas.json", "right": "Файл конфигурации профилей сборки"},
                        ],
                    },
                ],
            },
            {
                "t": "Публикация в App Store",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Публикация iOS-приложения",
                        "markdown": (
                            "## App Store\n\n"
                            "### Требования:\n"
                            "- Apple Developer Account ($99/год)\n"
                            "- App Store Connect — портал управления приложениями\n"
                            "- Иконка 1024x1024\n"
                            "- Скриншоты для iPhone и iPad\n\n"
                            "### Шаги публикации:\n\n"
                            "**1. Настройка app.json:**\n"
                            "```json\n"
                            "{\n"
                            "  \"expo\": {\n"
                            "    \"name\": \"Моё приложение\",\n"
                            "    \"slug\": \"my-app\",\n"
                            "    \"version\": \"1.0.0\",\n"
                            "    \"ios\": {\n"
                            "      \"bundleIdentifier\": \"com.mycompany.myapp\",\n"
                            "      \"buildNumber\": \"1\",\n"
                            "      \"supportsTablet\": true\n"
                            "    }\n"
                            "  }\n"
                            "}\n"
                            "```\n\n"
                            "**2. Сборка:**\n"
                            "```bash\n"
                            "eas build --platform ios --profile production\n"
                            "```\n\n"
                            "**3. Отправка в App Store Connect:**\n"
                            "```bash\n"
                            "eas submit --platform ios\n"
                            "```\n\n"
                            "**4. В App Store Connect:**\n"
                            "- Заполните описание, категорию, возрастной рейтинг\n"
                            "- Загрузите скриншоты\n"
                            "- Отправьте на ревью\n\n"
                            "### Ревью Apple:\n"
                            "- Обычно 1-3 дня\n"
                            "- Могут отклонить за нарушения гайдлайнов"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Зарегистрироваться в Apple Developer Program",
                            "Настроить app.json с bundleIdentifier",
                            "Собрать production-сборку через EAS",
                            "Отправить сборку через eas submit",
                            "Заполнить информацию в App Store Connect",
                            "Отправить на ревью Apple",
                        ],
                    },
                    {
                        "type": "type-answer",
                        "question": "Какой командой отправить сборку в App Store Connect?",
                        "acceptedAnswers": ["eas submit --platform ios", "eas submit -p ios"],
                    },
                ],
            },
            {
                "t": "Публикация в Google Play",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Публикация Android-приложения",
                        "markdown": (
                            "## Google Play\n\n"
                            "### Требования:\n"
                            "- Google Play Console ($25 единоразово)\n"
                            "- Подписанный AAB-файл (Android App Bundle)\n"
                            "- Иконка 512x512\n"
                            "- Feature graphic 1024x500\n\n"
                            "### Настройка app.json:\n"
                            "```json\n"
                            "{\n"
                            "  \"expo\": {\n"
                            "    \"android\": {\n"
                            "      \"package\": \"com.mycompany.myapp\",\n"
                            "      \"versionCode\": 1,\n"
                            "      \"adaptiveIcon\": {\n"
                            "        \"foregroundImage\": \"./assets/adaptive-icon.png\",\n"
                            "        \"backgroundColor\": \"#ffffff\"\n"
                            "      }\n"
                            "    }\n"
                            "  }\n"
                            "}\n"
                            "```\n\n"
                            "### Сборка и отправка:\n"
                            "```bash\n"
                            "# Сборка\n"
                            "eas build --platform android --profile production\n\n"
                            "# Отправка в Google Play\n"
                            "eas submit --platform android\n"
                            "```\n\n"
                            "### Трек публикации:\n"
                            "- **Internal testing** — до 100 тестеров\n"
                            "- **Closed testing** — ограниченная группа\n"
                            "- **Open testing** — все могут присоединиться\n"
                            "- **Production** — публичный релиз"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Сколько стоит регистрация в Google Play Console?",
                        "options": [
                            {"id": "a", "text": "$25 единоразово", "correct": True},
                            {"id": "b", "text": "$99 в год", "correct": False},
                            {"id": "c", "text": "Бесплатно", "correct": False},
                            {"id": "d", "text": "$299 в год", "correct": False},
                        ],
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "Internal testing", "right": "До 100 тестеров, быстрая публикация"},
                            {"left": "Closed testing", "right": "Ограниченная группа по приглашению"},
                            {"left": "Open testing", "right": "Любой может стать тестером"},
                            {"left": "Production", "right": "Публичный релиз в Google Play"},
                        ],
                    },
                    {
                        "type": "true-false",
                        "statement": "Google Play использует формат APK для публикации в магазине вместо AAB.",
                        "correct": False,
                    },
                ],
            },
            {
                "t": "OTA-обновления",
                "xp": 30,
                "steps": [
                    {
                        "type": "info",
                        "title": "Обновления без пересборки",
                        "markdown": (
                            "## OTA-обновления (EAS Update)\n\n"
                            "Обновляйте JavaScript-код приложения **без** отправки новой сборки в магазин.\n\n"
                            "### Настройка:\n"
                            "```bash\n"
                            "eas update:configure\n"
                            "```\n\n"
                            "### Публикация обновления:\n"
                            "```bash\n"
                            "# Обновить production-канал\n"
                            "eas update --branch production --message \"Исправлен баг в форме\"\n\n"
                            "# Обновить preview-канал\n"
                            "eas update --branch preview --message \"Новая фича: тёмная тема\"\n"
                            "```\n\n"
                            "### Как работает:\n"
                            "1. Вы запускаете `eas update`\n"
                            "2. JS-бандл загружается на серверы Expo\n"
                            "3. При следующем запуске приложение скачивает обновление\n"
                            "4. Пользователь видит новую версию!\n\n"
                            "### Ограничения:\n"
                            "- Работает только для JS/TS-изменений\n"
                            "- Нативные зависимости требуют новую сборку\n"
                            "- Изменения в app.json требуют новую сборку\n\n"
                            "### Преимущества:\n"
                            "- Мгновенное исправление багов\n"
                            "- Не ждать ревью App Store\n"
                            "- A/B-тестирование через каналы"
                        ),
                    },
                    {
                        "type": "quiz",
                        "question": "Что позволяют OTA-обновления?",
                        "options": [
                            {"id": "a", "text": "Обновить JS-код без новой сборки и ревью магазина", "correct": True},
                            {"id": "b", "text": "Обновить нативные модули без пересборки", "correct": False},
                            {"id": "c", "text": "Изменить bundleIdentifier приложения", "correct": False},
                            {"id": "d", "text": "Автоматически обновить iOS и Android SDK", "correct": False},
                        ],
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "eas update", "back": "Команда для публикации OTA-обновления"},
                            {"front": "--branch", "back": "Канал обновления (production, preview и т.д.)"},
                            {"front": "JS-бандл", "back": "Скомпилированный JavaScript-код приложения"},
                            {"front": "Ограничение OTA", "back": "Нельзя обновить нативный код и зависимости"},
                        ],
                    },
                ],
            },
            {
                "t": "CI/CD для мобильных приложений",
                "xp": 35,
                "steps": [
                    {
                        "type": "info",
                        "title": "Автоматизация сборки и деплоя",
                        "markdown": (
                            "## CI/CD с EAS и GitHub Actions\n\n"
                            "### GitHub Actions для автосборки:\n"
                            "```yaml\n"
                            "# .github/workflows/build.yml\n"
                            "name: EAS Build\n"
                            "on:\n"
                            "  push:\n"
                            "    branches: [main]\n\n"
                            "jobs:\n"
                            "  build:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "        with:\n"
                            "          node-version: 18\n"
                            "      - run: npm ci\n"
                            "      - uses: expo/expo-github-action@v8\n"
                            "        with:\n"
                            "          eas-version: latest\n"
                            "          token: ${{ secrets.EXPO_TOKEN }}\n"
                            "      - run: eas build --platform all --non-interactive\n"
                            "```\n\n"
                            "### Автоматический OTA при пуше:\n"
                            "```yaml\n"
                            "name: EAS Update\n"
                            "on:\n"
                            "  push:\n"
                            "    branches: [main]\n\n"
                            "jobs:\n"
                            "  update:\n"
                            "    runs-on: ubuntu-latest\n"
                            "    steps:\n"
                            "      - uses: actions/checkout@v4\n"
                            "      - uses: actions/setup-node@v4\n"
                            "      - run: npm ci\n"
                            "      - uses: expo/expo-github-action@v8\n"
                            "        with:\n"
                            "          eas-version: latest\n"
                            "          token: ${{ secrets.EXPO_TOKEN }}\n"
                            "      - run: eas update --branch production --auto\n"
                            "```\n\n"
                            "### Полный пайплайн:\n"
                            "1. Разработчик пушит код в main\n"
                            "2. CI запускает тесты\n"
                            "3. Если только JS-изменения → OTA-обновление\n"
                            "4. Если нативные изменения → полная сборка + submit"
                        ),
                    },
                    {
                        "type": "drag-order",
                        "items": [
                            "Разработчик пушит код в main",
                            "GitHub Actions запускает CI-пайплайн",
                            "Устанавливаются зависимости (npm ci)",
                            "Запускается EAS Build или EAS Update",
                            "Сборка автоматически публикуется в магазин",
                        ],
                    },
                    {
                        "type": "multi-select",
                        "question": "Какие шаги обычно включает CI/CD для React Native?",
                        "options": [
                            {"id": "a", "text": "Установка зависимостей", "correct": True},
                            {"id": "b", "text": "Запуск тестов", "correct": True},
                            {"id": "c", "text": "Сборка через EAS Build", "correct": True},
                            {"id": "d", "text": "Ручная загрузка APK на сервер", "correct": False},
                        ],
                    },
                ],
            },
            {
                "t": "Итоговый проект: мобильное приложение",
                "xp": 40,
                "steps": [
                    {
                        "type": "info",
                        "title": "Собираем всё вместе",
                        "markdown": (
                            "## Итоговый проект: TaskMaster\n\n"
                            "Создайте полноценное мобильное приложение для управления задачами.\n\n"
                            "### Технологии:\n"
                            "- Expo + TypeScript\n"
                            "- React Navigation (Stack + Tab)\n"
                            "- React Query для API\n"
                            "- AsyncStorage для кеша\n"
                            "- Zod для валидации\n"
                            "- JWT-аутентификация\n\n"
                            "### Экраны:\n"
                            "1. **LoginScreen** — вход/регистрация\n"
                            "2. **TasksScreen** — список задач (FlatList + pull-to-refresh)\n"
                            "3. **TaskDetailScreen** — детали задачи\n"
                            "4. **CreateTaskScreen** — создание задачи (форма + валидация)\n"
                            "5. **ProfileScreen** — профиль пользователя + аватар\n\n"
                            "### Структура:\n"
                            "```\n"
                            "src/\n"
                            "├── screens/         # 5 экранов\n"
                            "├── components/      # Button, Card, Input\n"
                            "├── navigation/      # Stack + Tab навигаторы\n"
                            "├── hooks/           # useAuth, useTasks\n"
                            "├── services/        # api.ts\n"
                            "├── context/         # AuthContext\n"
                            "└── types/           # TypeScript типы\n"
                            "```\n\n"
                            "### Чеклист:\n"
                            "- [ ] Авторизация (login/register/logout)\n"
                            "- [ ] CRUD задач (создание, чтение, обновление, удаление)\n"
                            "- [ ] Pull-to-refresh и пагинация\n"
                            "- [ ] Валидация форм\n"
                            "- [ ] Тёмная тема\n"
                            "- [ ] Push-уведомления\n"
                            "- [ ] Сборка и публикация"
                        ),
                    },
                    {
                        "type": "matching",
                        "pairs": [
                            {"left": "LoginScreen", "right": "JWT-аутентификация + форма + валидация"},
                            {"left": "TasksScreen", "right": "FlatList + React Query + pull-to-refresh"},
                            {"left": "CreateTaskScreen", "right": "TextInput + Zod + POST-запрос"},
                            {"left": "ProfileScreen", "right": "Аватар + expo-image-picker + настройки"},
                        ],
                    },
                    {
                        "type": "multi-select",
                        "question": "Какие технологии используются в итоговом проекте?",
                        "options": [
                            {"id": "a", "text": "React Navigation", "correct": True},
                            {"id": "b", "text": "React Query", "correct": True},
                            {"id": "c", "text": "JWT-аутентификация", "correct": True},
                            {"id": "d", "text": "Redux Saga", "correct": False},
                        ],
                    },
                    {
                        "type": "flashcards",
                        "cards": [
                            {"front": "Expo + TypeScript", "back": "Основа проекта: быстрый старт + типобезопасность"},
                            {"front": "React Query", "back": "Загрузка данных, кеширование, pull-to-refresh"},
                            {"front": "Zod", "back": "Валидация форм: email, пароль, обязательные поля"},
                            {"front": "EAS Build + Submit", "back": "Сборка и публикация в App Store / Google Play"},
                        ],
                    },
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
            slug="react-native-mobile-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Mobile",
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
                    edges.append(
                        {
                            "id": f"e-{lc}",
                            "source": nodes[-2]["id"],
                            "target": nodes[-1]["id"],
                        }
                    )
                lc += 1
                tl += 1

        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
