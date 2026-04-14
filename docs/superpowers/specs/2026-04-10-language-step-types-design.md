# 5 новых типов шагов для изучения языков

**Дата:** 2026-04-10
**Статус:** Утверждён

## Обзор

Добавляем 5 новых step types в CourseStepPlayer, ориентированных на изучение языков (английский и другие). Каждый тип — отдельный файл-компонент в `src/components/courses/steps/`. Подход B — разгрузка CourseStepPlayer при сохранении единого плеера.

## Новые типы

### 1. listening-comprehension — Аудирование с вопросами

Аудиоплеер + серия вопросов по прослушанному.

```typescript
interface StepListeningComprehension {
  type: "listening-comprehension";
  audioUrl: string;
  transcript?: string;
  questions: {
    question: string;
    options: { id: string; text: string; correct: boolean }[];
  }[];
}
```

**UX:** Сверху аудиоплеер (play/pause + прогресс), снизу вопросы по одному. Кнопка "Показать текст" для transcript. Все вопросы нужно ответить правильно для `onAnswer(true)`.

### 2. pronunciation — Произношение с Whisper

Запись голоса пользователя, отправка на Whisper API, сравнение с эталоном.

```typescript
interface StepPronunciation {
  type: "pronunciation";
  word: string;
  audioUrl?: string;
  phonetic?: string;
  acceptedForms: string[];
}
```

**UX:** Слово + транскрипция + кнопка "Прослушать эталон". Большая кнопка микрофона. Аудио → `/api/ai/transcribe` → Whisper. Результат сравнивается с `acceptedForms`. Показываем распознанный текст и результат.

### 3. word-builder — Собери слово из букв

Тап (мобильный) + drag & drop (десктоп) букв в правильном порядке.

```typescript
interface StepWordBuilder {
  type: "word-builder";
  hint: string;
  word: string;
  image?: string;
}
```

**UX:** Подсказка/картинка сверху, пустые ячейки (длина слова) по центру, перемешанные буквы снизу. Тап на мобильном, drag на десктопе. Тап по ячейке убирает букву обратно.

### 4. sentence-translation — Перевод предложения

Гибридная проверка: сначала по списку допустимых ответов, потом Claude AI.

```typescript
interface StepSentenceTranslation {
  type: "sentence-translation";
  sentence: string;
  sourceLanguage: string;
  targetLanguage: string;
  acceptedAnswers: string[];
  aiCheck: boolean;
}
```

**UX:** Исходная фраза крупно, textarea для перевода. При отправке: проверка по `acceptedAnswers` (lowercase, trim). Если не совпало и `aiCheck: true` — запрос на `/api/ai/check-translation`. Показываем фидбек.

### 5. cloze-passage — Текст с множеством пропусков

Текст с inline-пропусками, два режима: dropdown (если есть options) или текстовый input.

```typescript
interface StepClozePassage {
  type: "cloze-passage";
  instruction: string;
  segments: (
    | { type: "text"; value: string }
    | { type: "blank"; answer: string; options?: string[] }
  )[];
}
```

**UX:** Текст течёт как параграф, пропуски — inline dropdown или input. Кнопка "Проверить" внизу, подсветка зелёным/красным.

## Файловая структура

```
src/components/courses/steps/
  ListeningComprehensionStep.tsx
  PronunciationStep.tsx
  WordBuilderStep.tsx
  SentenceTranslationStep.tsx
  ClozePassageStep.tsx
```

Каждый компонент получает единый интерфейс:

```typescript
interface StepProps<T> {
  step: T;
  onAnswer: (correct: boolean) => void;
}
```

В `CourseStepPlayer.tsx` добавляются 5 новых case в `renderStep` + импорты.

## Бэкенд

### POST `/api/ai/transcribe`

- Принимает: multipart/form-data с полем `audio` (webm/mp3)
- Отправляет в OpenAI Whisper API
- Возвращает: `{ "text": "hello", "confidence": 0.95 }`
- Зависимости: пакет `openai`, `OPENAI_API_KEY` в `.env`

### POST `/api/ai/check-translation`

- Принимает: `{ sentence, user_answer, source_language, target_language }`
- Отправляет в Claude API с промптом для оценки перевода
- Возвращает: `{ "correct": true/false, "feedback": "...", "suggested": "..." }`
- Использует уже подключённый Anthropic SDK

## Интеграция в StepEditor

Новые типы добавляются в `StepType` union в `courseApi.ts` и в формы `StepEditor.tsx`:

| Тип | Поля редактора |
|---|---|
| listening-comprehension | URL аудио, transcript, N вопросов (вопрос + варианты + correct) |
| pronunciation | Слово, транскрипция, URL эталона, accepted forms через запятую |
| word-builder | Подсказка, правильное слово, URL картинки |
| sentence-translation | Фраза, source/target язык, accepted answers (по строке), чекбокс AI |
| cloze-passage | Инструкция, textarea с разметкой `{answer}` / `{answer\|opt1,opt2,opt3}` |

### Разметка cloze-passage

Автор пишет текст:
```
The cat {sat} on the {mat|mat,hat,bat}.
```
- `{sat}` → input (нет вариантов)
- `{mat|mat,hat,bat}` → dropdown

Парсится автоматически в массив segments.

## Зависимости

- `openai` в `backend/requirements.txt`
- `OPENAI_API_KEY` в `backend/.env`
- Всё остальное использует существующую инфраструктуру
