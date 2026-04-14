# MediaPipe Dance Engine — Design Spec

**Date:** 2026-04-14

---

## Overview

Движок для обучения танцам с проверкой движений через камеру. Использует MediaPipe Pose для отслеживания 33 точек тела и сравнения с эталонными позами по углам суставов. 6 новых типов шагов для CourseStepPlayer.

## Архитектура

```
Камера (WebRTC) → MediaPipe Pose (WASM) → 33 landmarks → PoseAnalyzer
                                                              ↓
                                                    Углы суставов студента
                                                              ↓
                                                    Сравнение с эталоном
                                                              ↓
                                                    Score 0-100% + подсветка
```

**Библиотека:** `@mediapipe/tasks-vision` (WebAssembly, работает в браузере)

**Принцип сравнения:** Углы суставов, НЕ абсолютные координаты. Работает с любым ростом, расстоянием от камеры, положением в кадре.

**Ключевые суставы для сравнения (8 пар):**
- leftElbow / rightElbow — угол в локте
- leftShoulder / rightShoulder — угол в плече
- leftKnee / rightKnee — угол в колене
- leftHip / rightHip — угол в бедре

**Tolerance:** 15° по умолчанию. Score = max(0, 100 - (diff / tolerance) * 100).

---

## 6 новых типов шагов

### 1. video-demo — Видео демонстрация

Встроенный видеоплеер с замедлением и ракурсами.

```typescript
interface StepVideoDemo {
  type: "video-demo"
  title: string
  videos: { url: string; angle: "front" | "side" | "back" }[]
  description?: string
}
```

**UI:**
- Видеоплеер с контролами скорости (0.25x, 0.5x, 1x)
- Табы для ракурсов (если несколько видео)
- Описание движения под видео
- Кнопка "Далее" для перехода

---

### 2. pose-check — Покадровая проверка позы

Студент повторяет статичную позу, камера сравнивает с эталоном.

```typescript
interface StepPoseCheck {
  type: "pose-check"
  title: string
  description: string
  referencePose: { landmarks: number[][] }  // 33 landmarks [x,y,z]
  referenceImage?: string  // URL картинки эталонной позы
  threshold: number  // минимальный % для прохождения (70)
}
```

**UI:**
- Слева: эталонная поза (картинка или скелет)
- Справа: камера студента с наложенным скелетом
- Цвет суставов: зелёный (совпадает) / красный (не совпадает)
- Круговой индикатор % совпадения
- Кнопка "Захватить позу" — фиксирует текущий кадр и оценивает
- ≥threshold → pass, иначе "Попробуй ещё раз"

---

### 3. mirror-practice — Реалтайм зеркало

Студент повторяет движение в реальном времени рядом с эталонным видео.

```typescript
interface StepMirrorPractice {
  type: "mirror-practice"
  title: string
  referenceVideo: string  // URL эталонного видео
  duration: number  // секунды (30-60)
  threshold: number  // минимальный средний % (60)
}
```

**UI:**
- Split screen: слева эталонное видео, справа камера со скелетом
- Реалтайм score обновляется каждые 500ms
- Таймер обратного отсчёта
- Средний score за всё время → pass/fail
- Цветовая полоса прогресса (красный → жёлтый → зелёный)

---

### 4. combo-challenge — Связка движений

Последовательность поз под музыку с оценкой каждого элемента.

```typescript
interface StepComboChallenge {
  type: "combo-challenge"
  title: string
  music: string  // URL аудиофайла
  bpm: number
  moves: {
    name: string
    pose: { landmarks: number[][] }
    beatStart: number  // на каком бите начинается
    beatEnd: number
  }[]
  threshold: number  // 60
}
```

**UI:**
- Камера на весь экран со скелетом
- Музыка играет
- Индикатор текущего движения: "Pop → Wave → Robot → ..."
- Подсветка текущего move (какой сейчас нужно делать)
- Score за каждый move отдельно
- Финальная оценка = среднее всех moves

---

### 5. battle-sim — Баттл-симуляция

Фристайл под музыку с AI-оценкой.

```typescript
interface StepBattleSim {
  type: "battle-sim"
  title: string
  music: string  // URL
  duration: number  // секунды (60-90)
  bpm: number
}
```

**UI:**
- Камера на весь экран, скелет наложен
- Музыка играет
- Таймер обратного отсчёта
- AI анализирует в реальном времени:
  - **Чистота** — насколько чётко выполняются элементы (дисперсия углов)
  - **Музыкальность** — попадание резких движений в биты (через BPM)
  - **Разнообразие** — количество уникальных поз за раунд
- Финальная карточка с 3 оценками + общий score
- Стиль "баттл арена" — тёмный фон, неоновые акценты

---

### 6. slow-motion — Замедленный разбор

Видео на 0.25x с паузами и объяснениями на ключевых кадрах.

```typescript
interface StepSlowMotion {
  type: "slow-motion"
  title: string
  video: string  // URL
  keyframes: {
    time: number  // секунда в видео
    pose: { landmarks: number[][] }
    description: string
  }[]
}
```

**UI:**
- Видео играет на 0.25x скорости
- Автоматическая пауза на каждом keyframe
- На паузе: скелет эталонной позы + текстовое описание
- Кнопка "Далее" для продолжения к следующему keyframe
- Прогресс-бар с маркерами keyframes

---

## Новые файлы

### Сервисы
- `src/services/poseService.ts` — инициализация MediaPipe, получение landmarks из видеопотока камеры
- `src/services/poseAnalyzer.ts` — вычисление углов суставов, сравнение поз, scoring, beat detection

### Компоненты
- `src/components/dance/CameraView.tsx` — камера + скелет overlay (переиспользуемый)
- `src/components/dance/PoseOverlay.tsx` — SVG-рисование скелета поверх видео
- `src/components/dance/ScoreIndicator.tsx` — круговой/линейный индикатор score
- `src/components/dance/VideoDemoStep.tsx` — тип video-demo
- `src/components/dance/PoseCheckStep.tsx` — тип pose-check
- `src/components/dance/MirrorPracticeStep.tsx` — тип mirror-practice
- `src/components/dance/ComboChallengeStep.tsx` — тип combo-challenge
- `src/components/dance/BattleSimStep.tsx` — тип battle-sim
- `src/components/dance/SlowMotionStep.tsx` — тип slow-motion

### Интеграция
- `src/components/courses/CourseStepPlayer.tsx` — добавить 6 новых case в renderStep switch

### Зависимости
- `@mediapipe/tasks-vision` — npm пакет для pose detection

---

## PoseService — детали

```typescript
// poseService.ts
import { PoseLandmarker, FilesetResolver } from "@mediapipe/tasks-vision"

class PoseService {
  private landmarker: PoseLandmarker | null = null

  async init() {
    const vision = await FilesetResolver.forVisionTasks(
      "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm"
    )
    this.landmarker = await PoseLandmarker.createFromOptions(vision, {
      baseOptions: {
        modelAssetPath: "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
        delegate: "GPU"
      },
      runningMode: "VIDEO",
      numPoses: 1,
    })
  }

  detect(videoFrame: HTMLVideoElement, timestamp: number) {
    if (!this.landmarker) return null
    return this.landmarker.detectForVideo(videoFrame, timestamp)
  }

  destroy() {
    this.landmarker?.close()
    this.landmarker = null
  }
}

export const poseService = new PoseService()
```

## PoseAnalyzer — детали

```typescript
// poseAnalyzer.ts
type Landmark = { x: number; y: number; z: number }

const JOINT_DEFINITIONS = {
  leftElbow:    [11, 13, 15],  // shoulder, elbow, wrist
  rightElbow:   [12, 14, 16],
  leftShoulder: [23, 11, 13],  // hip, shoulder, elbow
  rightShoulder:[24, 12, 14],
  leftKnee:     [23, 25, 27],  // hip, knee, ankle
  rightKnee:    [24, 26, 28],
  leftHip:      [11, 23, 25],  // shoulder, hip, knee
  rightHip:     [12, 24, 26],
}

function angle(a: Landmark, b: Landmark, c: Landmark): number {
  const radians = Math.atan2(c.y - b.y, c.x - b.x) - Math.atan2(a.y - b.y, a.x - b.x)
  let degrees = Math.abs(radians * 180 / Math.PI)
  if (degrees > 180) degrees = 360 - degrees
  return degrees
}

export function getJointAngles(landmarks: Landmark[]): Record<string, number> {
  const angles: Record<string, number> = {}
  for (const [name, [a, b, c]] of Object.entries(JOINT_DEFINITIONS)) {
    angles[name] = angle(landmarks[a], landmarks[b], landmarks[c])
  }
  return angles
}

export function comparePoses(
  student: Record<string, number>,
  reference: Record<string, number>,
  tolerance = 15
): { score: number; joints: Record<string, { score: number; diff: number }> } {
  let total = 0
  const joints: Record<string, { score: number; diff: number }> = {}
  const keys = Object.keys(reference)

  for (const key of keys) {
    const diff = Math.abs((student[key] || 0) - reference[key])
    const score = Math.max(0, 100 - (diff / tolerance) * 100)
    joints[key] = { score, diff }
    total += score
  }

  return { score: total / keys.length, joints }
}

// Beat detection для battle-sim
export function isOnBeat(timestamp: number, bpm: number, tolerance = 100): boolean {
  const beatInterval = 60000 / bpm  // ms per beat
  const position = timestamp % beatInterval
  return position < tolerance || position > beatInterval - tolerance
}

// Diversity score для battle-sim
export function diversityScore(poseHistory: Record<string, number>[], windowSize = 30): number {
  if (poseHistory.length < 2) return 0
  const recent = poseHistory.slice(-windowSize)
  let totalVariance = 0
  const keys = Object.keys(recent[0])
  for (const key of keys) {
    const values = recent.map(p => p[key])
    const mean = values.reduce((a, b) => a + b, 0) / values.length
    const variance = values.reduce((a, v) => a + (v - mean) ** 2, 0) / values.length
    totalVariance += variance
  }
  return Math.min(100, totalVariance / keys.length / 10)
}
```

## CameraView — переиспользуемый компонент

```typescript
// Общий компонент камеры со скелетом
interface CameraViewProps {
  onFrame?: (landmarks: Landmark[]) => void  // каждый кадр
  skeleton?: boolean  // рисовать скелет
  jointColors?: Record<string, string>  // цвета суставов (green/red)
  mirrored?: boolean  // зеркальное отражение
  className?: string
}
```

- Инициализирует камеру через `navigator.mediaDevices.getUserMedia`
- На каждом кадре вызывает `poseService.detect()`
- Рисует скелет через SVG/Canvas overlay
- Вызывает `onFrame` с landmarks для внешней обработки

---

## Интеграция в CourseStepPlayer

Добавить в `renderStep` switch:

```typescript
case "video-demo":
  return <VideoDemoStep step={step as StepVideoDemo} onNext={goForward} />
case "pose-check":
  return <PoseCheckStep step={step as StepPoseCheck} onAnswer={handleInteractiveAnswer} />
case "mirror-practice":
  return <MirrorPracticeStep step={step as StepMirrorPractice} onAnswer={handleInteractiveAnswer} />
case "combo-challenge":
  return <ComboChallengeStep step={step as StepComboChallenge} onAnswer={handleInteractiveAnswer} />
case "battle-sim":
  return <BattleSimStep step={step as StepBattleSim} onAnswer={handleInteractiveAnswer} />
case "slow-motion":
  return <SlowMotionStep step={step as StepSlowMotion} onNext={goForward} />
```

---

## Требования к камере

- Минимум 640x480 для надёжного распознавания
- Рекомендуемо: хорошее освещение, полный рост в кадре
- Компонент показывает подсказки если тело не полностью видно
- Fallback: если камера недоступна — показывать только видео без проверки

---

## Не входит в скоуп

- Запись видео студента для просмотра позже
- Мультиплеер/батлы между студентами
- Собственная загрузка эталонных видео (пока только из seed)
- Мобильная версия (MediaPipe работает в мобильном Chrome, но UX отличается)
