# Python Coding (Pyodide)

Интерактивные Python-упражнения, выполняемые прямо в браузере через Pyodide (WebAssembly).

## Архитектура

```
┌──────────────────────────────────────────┐
│            PythonCodingStep              │
│  ┌────────────────────────────────────┐  │
│  │  Задание (prompt)                  │  │
│  ├────────────────────────────────────┤  │
│  │  CodeMirror (Python syntax)        │  │
│  │  > print("Hello!")                 │  │
│  ├────────────────────────────────────┤  │
│  │  [▶ Запустить]  [↺ Сбросить]      │  │
│  ├────────────────────────────────────┤  │
│  │  Консоль: Hello!                  │  │
│  │  ✅ Верно! +XP                     │  │
│  └────────────────────────────────────┘  │
└──────────────┬───────────────────────────┘
               │
       ┌───────┴───────┐
       │  usePyodide   │ ← React hook
       │  (singleton)  │
       └───────┬───────┘
               │
       ┌───────┴───────────┐
       │  Web Worker        │
       │  pyodideWorker.ts  │
       │  (Pyodide WASM)   │
       └───────────────────┘
       Python 3.12 в браузере
```

## Компоненты и файлы

| Файл | Назначение |
|---|---|
| `src/lib/pyodideWorker.ts` | Web Worker — загрузка Pyodide, выполнение кода, захват stdout/stderr |
| `src/hooks/usePyodide.ts` | React hook — инициализация worker, `runCode()`, таймаут 5 сек |
| `src/components/courses/steps/PythonCodingStep.tsx` | UI — редактор + консоль + валидация |
| `src/services/courseApi.ts` | Тип `StepPythonCoding` в union `LessonStep` |
| `src/components/courses/CourseStepPlayer.tsx` | `case "python-coding"` в switch рендеринга |

## Степ формат (JSON)

```json
{
  "type": "python-coding",
  "prompt": "Напишите программу которая выводит сумму 2 + 3",
  "starterCode": "# Ваш код здесь\n",
  "expectedOutput": "5",
  "hint": "Используйте print() и оператор +"
}
```

| Поле | Тип | Описание |
|---|---|---|
| `type` | `"python-coding"` | Фиксированный тип степа |
| `prompt` | `string` | Текст задания |
| `starterCode` | `string` | Начальный код в редакторе |
| `expectedOutput` | `string` | Ожидаемый stdout. Пустая строка `""` — любой вывод принят |
| `hint` | `string?` | Подсказка (опционально) |

## Как работает

1. Студент открывает урок с `python-coding` степом
2. Pyodide (~10 МБ) загружается в Web Worker (кэшируется браузером после первого раза)
3. Студент пишет код в CodeMirror с Python-подсветкой
4. Нажимает "Запустить" → код отправляется в Worker
5. Pyodide выполняет Python, перехватывает `stdout`
6. Вывод сравнивается с `expectedOutput` (после trim)
7. Совпало → зелёная галочка, XP начисляется
8. Не совпало → красная ошибка "Ожидалось: X, Получено: Y"

## Защита

- **Таймаут 5 сек** — защита от бесконечных циклов (while True)
- **Web Worker sandbox** — нет доступа к DOM, cookies, localStorage
- **Нет сети** — Worker не может делать HTTP-запросы
- **Нет файловой системы** — только stdout

## Pyodide

- **Версия:** 0.27.0
- **CDN:** `https://cdn.jsdelivr.net/pyodide/v0.27.0/full/`
- **Размер:** ~10 МБ (первая загрузка), кэшируется Service Worker (PWA)
- **Поддерживаемые модули:** `math`, `random`, `json`, `datetime`, `collections`, `itertools`, `re`, `string`
- **Не поддерживается:** `input()`, `open()`, `pip install`, сетевые запросы

## Python курс

Курс "Python — с нуля до Junior" использует `python-coding` степы:

| Секция | Темы | Уроков |
|---|---|---|
| 1. Основы | print(), комментарии, вычисления | 3 |
| 2. Переменные | int, float, str, преобразование типов | 4 |
| 3. Строки | методы, срезы, f-strings | 3 |
| 4. Условия | if/elif/else, and/or/not | 3 |
| 5. Циклы | for, while, range(), break/continue | 4 |
| 6. Списки | [], методы, list comprehension | 3 |
| 7. Функции | def, return, параметры, lambda | 4 |
| 8. Словари | {}, вложенные структуры, финальный проект | 3 |

**Итого:** 8 секций, 27 уроков, ~110 степов (~50% coding, ~25% info, ~25% quiz)

## Как добавить coding-степ в другой курс

В seed-скрипте добавьте степ в массив `steps` урока:

```python
{"type": "python-coding",
 "prompt": "Создайте список из 5 чисел и выведите его сумму",
 "starterCode": "numbers = [1, 2, 3, 4, 5]\n# Выведите сумму\n",
 "expectedOutput": "15",
 "hint": "Используйте функцию sum()"}
```

---

См. также: [[Компоненты]], [[Сторы]], [[Добавление курса]]
