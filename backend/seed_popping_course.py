"""Seed: Popping — от начинающих до профи — 6 sections, 50 lessons."""
import asyncio, uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90
T = "Popping — от начинающих до профи"
DESC = "Полный курс по Popping: от базовых хитов до фристайла и баттлов. Проверка движений через камеру с MediaPipe. 5 уровней: основы тела, базовые хиты, изоляции, волны и глайды, фристайл и комбинации."

# -- Realistic 33-point landmark helpers (MediaPipe Pose) --
# Index: 0=nose,1-4=eyes,5-6=ears,7-8=mouth,9-10=shoulders,11-12=elbows,
#        13-14=wrists,15-16=pinkies,17-18=index,19-20=thumbs,21-22=hips,
#        23-24=knees,25-26=ankles,27-28=heels,29-30=foot-index,31-32=misc

def _standing():
    """Neutral standing pose, arms at sides."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],  # shoulders
        [0.38,0.38,0],[0.62,0.38,0],  # elbows
        [0.37,0.50,0],[0.63,0.50,0],  # wrists
        [0.36,0.52,0],[0.64,0.52,0],  # pinkies
        [0.37,0.51,0],[0.63,0.51,0],  # index
        [0.38,0.50,0],[0.62,0.50,0],  # thumbs
        [0.45,0.52,0],[0.55,0.52,0],  # hips
        [0.45,0.70,0],[0.55,0.70,0],  # knees
        [0.45,0.88,0],[0.55,0.88,0],  # ankles
        [0.44,0.90,0],[0.56,0.90,0],  # heels
        [0.46,0.91,0],[0.54,0.91,0],  # foot index
        [0.50,0.06,0],[0.50,0.52,0],  # misc
    ]

def _pop_arms():
    """Pop/hit pose — arms bent, fists clenched, slight chest push."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.38,0.24,0],[0.62,0.24,0],  # shoulders slightly wider
        [0.32,0.32,0],[0.68,0.32,0],  # elbows out
        [0.35,0.26,0],[0.65,0.26,0],  # wrists up near chest
        [0.34,0.27,0],[0.66,0.27,0],
        [0.35,0.26,0],[0.65,0.26,0],
        [0.36,0.27,0],[0.64,0.27,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _chest_pop():
    """Chest pop — chest pushed forward, shoulders back."""
    return [
        [0.50,0.11,0],[0.48,0.09,0],[0.47,0.09,0],[0.52,0.09,0],[0.53,0.09,0],
        [0.44,0.11,0],[0.56,0.11,0],[0.49,0.13,0],[0.51,0.13,0],
        [0.42,0.23,0],[0.58,0.23,0],  # shoulders pulled back
        [0.40,0.36,0],[0.60,0.36,0],
        [0.39,0.48,0],[0.61,0.48,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.39,0.49,0],[0.61,0.49,0],
        [0.40,0.48,0],[0.60,0.48,0],
        [0.45,0.53,0],[0.55,0.53,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.05,0],[0.50,0.53,0],
    ]

def _fresno():
    """Fresno step — weight shifted, one arm angled, one leg stepped out."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.39,0.24,0],[0.61,0.24,0],
        [0.33,0.30,0],[0.64,0.36,0],  # left elbow out, right relaxed
        [0.30,0.24,0],[0.62,0.48,0],  # left wrist up, right down
        [0.29,0.25,0],[0.63,0.50,0],
        [0.30,0.24,0],[0.62,0.49,0],
        [0.31,0.25,0],[0.61,0.48,0],
        [0.44,0.52,0],[0.56,0.52,0],
        [0.42,0.70,0],[0.58,0.70,0],  # wider stance
        [0.40,0.88,0],[0.60,0.88,0],
        [0.39,0.90,0],[0.61,0.90,0],
        [0.41,0.91,0],[0.59,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _neck_pop():
    """Neck pop — head shifted to one side."""
    return [
        [0.54,0.12,0],[0.52,0.10,0],[0.51,0.10,0],[0.56,0.10,0],[0.57,0.10,0],
        [0.48,0.12,0],[0.60,0.12,0],[0.53,0.14,0],[0.55,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.38,0.38,0],[0.62,0.38,0],
        [0.37,0.50,0],[0.63,0.50,0],
        [0.36,0.52,0],[0.64,0.52,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.54,0.06,0],[0.50,0.52,0],
    ]

def _leg_pop():
    """Leg pop — one knee slightly bent, weight on back leg."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.38,0.38,0],[0.62,0.38,0],
        [0.37,0.50,0],[0.63,0.50,0],
        [0.36,0.52,0],[0.64,0.52,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.44,0.52,0],[0.56,0.52,0],
        [0.42,0.68,0],[0.56,0.72,0],  # left knee bent more
        [0.40,0.86,0],[0.56,0.88,0],
        [0.39,0.88,0],[0.57,0.90,0],
        [0.41,0.89,0],[0.55,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _dimestop():
    """Dimestop — frozen mid-step, one arm extended."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.30,0.28,0],[0.62,0.38,0],  # left arm extended
        [0.22,0.25,0],[0.63,0.50,0],
        [0.20,0.26,0],[0.64,0.52,0],
        [0.22,0.25,0],[0.63,0.51,0],
        [0.23,0.26,0],[0.62,0.50,0],
        [0.44,0.52,0],[0.56,0.52,0],
        [0.43,0.69,0],[0.57,0.71,0],
        [0.42,0.87,0],[0.57,0.88,0],
        [0.41,0.89,0],[0.58,0.90,0],
        [0.43,0.90,0],[0.56,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _boogaloo_roll():
    """Boogaloo roll — circular body motion, shoulders offset."""
    return [
        [0.50,0.13,0],[0.48,0.11,0],[0.47,0.11,0],[0.52,0.11,0],[0.53,0.11,0],
        [0.44,0.13,0],[0.56,0.13,0],[0.49,0.15,0],[0.51,0.15,0],
        [0.38,0.26,0],[0.62,0.24,0],  # shoulders tilted
        [0.34,0.36,0],[0.66,0.34,0],
        [0.32,0.46,0],[0.68,0.44,0],
        [0.31,0.48,0],[0.69,0.46,0],
        [0.32,0.47,0],[0.68,0.45,0],
        [0.33,0.46,0],[0.67,0.44,0],
        [0.44,0.53,0],[0.56,0.51,0],
        [0.44,0.70,0],[0.56,0.70,0],
        [0.44,0.88,0],[0.56,0.88,0],
        [0.43,0.90,0],[0.57,0.90,0],
        [0.45,0.91,0],[0.55,0.91,0],
        [0.50,0.07,0],[0.50,0.52,0],
    ]

def _iso_head():
    """Head isolation — head shifted left, body still."""
    return [
        [0.46,0.12,0],[0.44,0.10,0],[0.43,0.10,0],[0.48,0.10,0],[0.49,0.10,0],
        [0.40,0.12,0],[0.52,0.12,0],[0.45,0.14,0],[0.47,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.38,0.38,0],[0.62,0.38,0],
        [0.37,0.50,0],[0.63,0.50,0],
        [0.36,0.52,0],[0.64,0.52,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.46,0.06,0],[0.50,0.52,0],
    ]

def _iso_shoulders():
    """Shoulder isolation — one shoulder up, one down."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.22,0],[0.60,0.28,0],  # left shoulder up, right down
        [0.38,0.36,0],[0.62,0.40,0],
        [0.37,0.48,0],[0.63,0.52,0],
        [0.36,0.50,0],[0.64,0.54,0],
        [0.37,0.49,0],[0.63,0.53,0],
        [0.38,0.48,0],[0.62,0.52,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _iso_chest():
    """Chest isolation — chest shifted right, hips still."""
    return [
        [0.52,0.12,0],[0.50,0.10,0],[0.49,0.10,0],[0.54,0.10,0],[0.55,0.10,0],
        [0.46,0.12,0],[0.58,0.12,0],[0.51,0.14,0],[0.53,0.14,0],
        [0.42,0.25,0],[0.62,0.25,0],  # chest shifted right
        [0.40,0.38,0],[0.64,0.38,0],
        [0.39,0.50,0],[0.65,0.50,0],
        [0.38,0.52,0],[0.66,0.52,0],
        [0.39,0.51,0],[0.65,0.51,0],
        [0.40,0.50,0],[0.64,0.50,0],
        [0.45,0.52,0],[0.55,0.52,0],  # hips centered
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.52,0.06,0],[0.50,0.52,0],
    ]

def _iso_hips():
    """Hip isolation — hips shifted left, upper body still."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.38,0.38,0],[0.62,0.38,0],
        [0.37,0.50,0],[0.63,0.50,0],
        [0.36,0.52,0],[0.64,0.52,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.42,0.52,0],[0.52,0.52,0],  # hips shifted left
        [0.43,0.70,0],[0.53,0.70,0],
        [0.44,0.88,0],[0.54,0.88,0],
        [0.43,0.90,0],[0.55,0.90,0],
        [0.45,0.91,0],[0.53,0.91,0],
        [0.50,0.06,0],[0.47,0.52,0],
    ]

def _tutting():
    """Tutting — angular arm shapes, 90-degree bends."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.32,0.25,0],[0.68,0.25,0],  # elbows straight out
        [0.32,0.15,0],[0.68,0.15,0],  # wrists up at 90 degrees
        [0.31,0.14,0],[0.69,0.14,0],
        [0.32,0.15,0],[0.68,0.15,0],
        [0.33,0.16,0],[0.67,0.16,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _robot():
    """Robot style — stiff, angular, mechanical pose."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.40,0.35,0],[0.60,0.25,0],  # one arm up, one angled
        [0.40,0.20,0],[0.60,0.35,0],
        [0.39,0.19,0],[0.61,0.36,0],
        [0.40,0.20,0],[0.60,0.35,0],
        [0.41,0.21,0],[0.59,0.34,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _arm_wave():
    """Arm wave — one arm extended, wave flowing through."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.28,0.22,0],[0.68,0.25,0],  # left arm extended high
        [0.18,0.20,0],[0.63,0.38,0],
        [0.16,0.21,0],[0.64,0.40,0],
        [0.18,0.20,0],[0.63,0.39,0],
        [0.19,0.21,0],[0.62,0.38,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _body_wave():
    """Body wave — S-curve through torso."""
    return [
        [0.50,0.11,0],[0.48,0.09,0],[0.47,0.09,0],[0.52,0.09,0],[0.53,0.09,0],
        [0.44,0.11,0],[0.56,0.11,0],[0.49,0.13,0],[0.51,0.13,0],
        [0.42,0.24,0],[0.58,0.24,0],  # shoulders back
        [0.40,0.37,0],[0.60,0.37,0],
        [0.39,0.49,0],[0.61,0.49,0],
        [0.38,0.51,0],[0.62,0.51,0],
        [0.39,0.50,0],[0.61,0.50,0],
        [0.40,0.49,0],[0.60,0.49,0],
        [0.46,0.54,0],[0.54,0.54,0],  # hips pushed forward
        [0.46,0.71,0],[0.54,0.71,0],
        [0.46,0.88,0],[0.54,0.88,0],
        [0.45,0.90,0],[0.55,0.90,0],
        [0.47,0.91,0],[0.53,0.91,0],
        [0.50,0.05,0],[0.50,0.54,0],
    ]

def _moonwalk():
    """Moonwalk — one foot sliding back, weight forward."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.38,0.38,0],[0.62,0.38,0],
        [0.37,0.50,0],[0.63,0.50,0],
        [0.36,0.52,0],[0.64,0.52,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.44,0.69,0],[0.56,0.72,0],  # asymmetric knees
        [0.43,0.86,0],[0.58,0.90,0],  # one foot forward, one back
        [0.42,0.88,0],[0.59,0.92,0],
        [0.44,0.89,0],[0.57,0.93,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _snake():
    """Snake — sinuous body curve."""
    return [
        [0.52,0.11,0],[0.50,0.09,0],[0.49,0.09,0],[0.54,0.09,0],[0.55,0.09,0],
        [0.46,0.11,0],[0.58,0.11,0],[0.51,0.13,0],[0.53,0.13,0],
        [0.43,0.24,0],[0.57,0.24,0],  # shoulders offset
        [0.40,0.37,0],[0.60,0.37,0],
        [0.38,0.49,0],[0.62,0.49,0],
        [0.37,0.51,0],[0.63,0.51,0],
        [0.38,0.50,0],[0.62,0.50,0],
        [0.39,0.49,0],[0.61,0.49,0],
        [0.47,0.53,0],[0.53,0.53,0],  # hips offset other way
        [0.46,0.70,0],[0.54,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.52,0.05,0],[0.50,0.53,0],
    ]

def _floor_work():
    """Floor work — low crouch, one hand on ground."""
    return [
        [0.50,0.40,0],[0.48,0.38,0],[0.47,0.38,0],[0.52,0.38,0],[0.53,0.38,0],
        [0.44,0.40,0],[0.56,0.40,0],[0.49,0.42,0],[0.51,0.42,0],
        [0.40,0.48,0],[0.60,0.48,0],  # shoulders low
        [0.34,0.55,0],[0.64,0.55,0],
        [0.30,0.70,0],[0.63,0.62,0],  # left hand on floor
        [0.29,0.72,0],[0.64,0.64,0],
        [0.30,0.71,0],[0.63,0.63,0],
        [0.31,0.70,0],[0.62,0.62,0],
        [0.44,0.60,0],[0.56,0.60,0],
        [0.42,0.75,0],[0.58,0.75,0],
        [0.40,0.85,0],[0.58,0.88,0],
        [0.39,0.87,0],[0.59,0.90,0],
        [0.41,0.88,0],[0.57,0.91,0],
        [0.50,0.34,0],[0.50,0.60,0],
    ]

def _glide():
    """Glide — one foot sliding, arms floating."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.34,0.30,0],[0.66,0.30,0],  # arms slightly out
        [0.30,0.35,0],[0.70,0.35,0],
        [0.29,0.36,0],[0.71,0.36,0],
        [0.30,0.35,0],[0.70,0.35,0],
        [0.31,0.36,0],[0.69,0.36,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.44,0.70,0],[0.56,0.70,0],
        [0.42,0.88,0],[0.58,0.88,0],  # wider foot stance for glide
        [0.41,0.90,0],[0.59,0.90,0],
        [0.43,0.91,0],[0.57,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

def _finger_wave():
    """Finger wave — arm extended, fingers spread."""
    return [
        [0.50,0.12,0],[0.48,0.10,0],[0.47,0.10,0],[0.52,0.10,0],[0.53,0.10,0],
        [0.44,0.12,0],[0.56,0.12,0],[0.49,0.14,0],[0.51,0.14,0],
        [0.40,0.25,0],[0.60,0.25,0],
        [0.28,0.23,0],[0.62,0.38,0],  # left arm extended
        [0.18,0.22,0],[0.63,0.50,0],
        [0.15,0.23,0],[0.64,0.52,0],
        [0.17,0.21,0],[0.63,0.51,0],
        [0.19,0.22,0],[0.62,0.50,0],
        [0.45,0.52,0],[0.55,0.52,0],
        [0.45,0.70,0],[0.55,0.70,0],
        [0.45,0.88,0],[0.55,0.88,0],
        [0.44,0.90,0],[0.56,0.90,0],
        [0.46,0.91,0],[0.54,0.91,0],
        [0.50,0.06,0],[0.50,0.52,0],
    ]

# ── URLs ──
# YouTube embed URLs for each lesson topic
YT = {
    # Level 1 - Basics
    "history":          "https://www.youtube.com/embed/ufRbKMHo0w4",
    "warmup":           "https://www.youtube.com/embed/4vTJHUDB5ak",
    "basic-pop":        "https://www.youtube.com/embed/TYqGBCKFYHs",
    "chest-pop":        "https://www.youtube.com/embed/grWaRMjGfME",
    "pop-music":        "https://www.youtube.com/embed/KVhVHvCMrPY",
    # Level 2 - Fresno & Hits
    "fresno":           "https://www.youtube.com/embed/1JilhFam2bU",
    "neck-pop":         "https://www.youtube.com/embed/TYqGBCKFYHs",
    "dimestop":         "https://www.youtube.com/embed/z3VYqMcBVwc",
    "walkout":          "https://www.youtube.com/embed/KVhVHvCMrPY",
    "boogaloo":         "https://www.youtube.com/embed/ufRbKMHo0w4",
    # Level 3 - Isolations
    "iso-head":         "https://www.youtube.com/embed/4vTJHUDB5ak",
    "iso-shoulders":    "https://www.youtube.com/embed/grWaRMjGfME",
    "iso-chest":        "https://www.youtube.com/embed/TYqGBCKFYHs",
    "iso-hips":         "https://www.youtube.com/embed/1JilhFam2bU",
    "tutting":          "https://www.youtube.com/embed/z3VYqMcBVwc",
    "robot":            "https://www.youtube.com/embed/KVhVHvCMrPY",
    # Level 4 - Waves & Glides
    "arm-wave":         "https://www.youtube.com/embed/ufRbKMHo0w4",
    "body-wave":        "https://www.youtube.com/embed/4vTJHUDB5ak",
    "finger-wave":      "https://www.youtube.com/embed/grWaRMjGfME",
    "glide":            "https://www.youtube.com/embed/TYqGBCKFYHs",
    "float":            "https://www.youtube.com/embed/1JilhFam2bU",
    "snake":            "https://www.youtube.com/embed/z3VYqMcBVwc",
    # Level 5 - Freestyle
    "floor-work":       "https://www.youtube.com/embed/KVhVHvCMrPY",
    "levels":           "https://www.youtube.com/embed/ufRbKMHo0w4",
    "transitions":      "https://www.youtube.com/embed/4vTJHUDB5ak",
    "performance":      "https://www.youtube.com/embed/grWaRMjGfME",
}
# Music URL (royalty-free funk beat from Pixabay)
MUSIC = "https://cdn.pixabay.com/audio/2024/11/04/audio_4956b54637.mp3"

S = [
  # ==================== Level 1: Основы тела и ритм ====================
  {"title":"Уровень 1: Основы тела и ритм","pos":0,"lessons":[
    {"t":"Что такое Popping","xp":20,"steps":[
      {"type":"info","title":"История Popping","markdown":"## Что такое Popping?\n\n**Popping** — это стиль уличного танца, основанный на технике быстрого сокращения и расслабления мышц, создающей эффект **«хита»** (pop/hit) в теле танцора.\n\n### Основатели\n- **Boogaloo Sam (Sam Solomon)** — создатель стиля в Fresno, Калифорния, конец 1970-х\n- **Electric Boogaloos** — легендарная группа, популяризировавшая стиль\n\n### Ключевые понятия\n- **Pop / Hit** — резкое сокращение мышц в ритм музыки\n- **Funk** — основной музыкальный жанр для Popping\n- **Groove** — базовое ощущение ритма в теле\n\n### Стили внутри Popping\n- Boogaloo, Animation, Robot, Waving, Tutting, Strutting"},
      {"type":"quiz","question":"Кто считается основателем стиля Popping?","options":[
        {"id":"a","text":"Michael Jackson","correct":False},
        {"id":"b","text":"Boogaloo Sam","correct":True},
        {"id":"c","text":"James Brown","correct":False},
        {"id":"d","text":"Mr. Wiggles","correct":False}
      ]},
      {"type":"flashcards","cards":[
        {"front":"Pop / Hit","back":"Резкое сокращение и расслабление мышц, создающее визуальный эффект рывка"},
        {"front":"Boogaloo Sam","back":"Создатель Popping, основатель группы Electric Boogaloos"},
        {"front":"Funk","back":"Основной музыкальный жанр для танца Popping"},
        {"front":"Groove","back":"Базовое чувство ритма, пульсация тела под музыку"},
        {"front":"Fresno","back":"Город в Калифорнии, родина стиля Popping"},
        {"front":"Electric Boogaloos","back":"Легендарная танцевальная группа, популяризировавшая Popping"}
      ]},
      {"type":"matching","pairs":[
        {"left":"Pop/Hit","right":"Сокращение мышц"},
        {"left":"Boogaloo Sam","right":"Создатель Popping"},
        {"left":"Electric Boogaloos","right":"Танцевальная группа"},
        {"left":"Funk","right":"Музыкальный жанр"},
        {"left":"Fresno","right":"Город-родина стиля"}
      ]},
    ]},
    {"t":"Разминка для танцора","xp":20,"steps":[
      {"type":"video-demo","title":"Разминка Popping-танцора","videos":[{"url":YT["warmup"],"angle":"front"}],"description":"Полная разминка: шея, плечи, руки, грудь, корпус, бёдра, колени, стопы. 5-10 минут перед каждой тренировкой."},
      {"type":"info","title":"Почему разминка важна","markdown":"## Разминка — основа безопасности\n\n### Зачем разминаться?\n- Popping нагружает суставы и мышцы резкими сокращениями\n- Без разминки высок риск травм шеи, плеч, коленей\n- Разогретые мышцы дают более чёткие хиты\n\n### Порядок разминки\n1. **Шея** — наклоны, круговые (2 мин)\n2. **Плечи** — вращения, подъёмы (2 мин)\n3. **Руки** — кисти, локти, запястья (1 мин)\n4. **Грудь и корпус** — скручивания (2 мин)\n5. **Ноги** — колени, голеностоп, приседания (2 мин)"},
      {"type":"quiz","question":"Какую часть тела нужно разминать первой?","options":[
        {"id":"a","text":"Ноги","correct":False},
        {"id":"b","text":"Шею","correct":True},
        {"id":"c","text":"Руки","correct":False},
        {"id":"d","text":"Корпус","correct":False}
      ]},
    ]},
    {"t":"Музыкальность — слушаем бит","xp":20,"steps":[
      {"type":"info","title":"Считаем биты","markdown":"## Музыкальность в Popping\n\n### Структура музыки\n- Popping танцуют под **Funk**, реже под Electro-Funk, Hip-Hop\n- Считаем **8 битов**: 1-2-3-4-5-6-7-8\n- Pop обычно делается на **каждый бит** или на **1 и 3** (половинный ритм)\n\n### Как тренировать\n1. Включите Funk-трек (100-110 BPM)\n2. Хлопайте на каждый бит\n3. Попробуйте хлопать только на 1 и 5\n4. Добавьте хиты телом вместо хлопков\n\n### Важные понятия\n- **On beat** — точно в бит\n- **Off beat** — между битами\n- **Double time** — удвоенная скорость\n- **Half time** — половинная скорость"},
      {"type":"quiz","question":"Сколько битов в стандартном музыкальном такте для Popping?","options":[
        {"id":"a","text":"4","correct":False},
        {"id":"b","text":"8","correct":True},
        {"id":"c","text":"12","correct":False},
        {"id":"d","text":"16","correct":False}
      ]},
      {"type":"type-answer","question":"Как называется приём, когда pop делается точно в момент удара бита?","acceptedAnswers":["on beat","on-beat","онбит","в бит"]},
    ]},
    {"t":"Базовая стойка","xp":25,"steps":[
      {"type":"video-demo","title":"Базовая стойка Popper'a","videos":[{"url":YT["basic-pop"],"angle":"front"}],"description":"Ноги на ширине плеч, колени слегка согнуты, вес на подушечках стоп, руки расслаблены по бокам, корпус слегка наклонён вперёд."},
      {"type":"pose-check","title":"Проверка стойки","description":"Встаньте в базовую стойку Popper'a: ноги на ширине плеч, колени чуть согнуты, руки расслаблены.","referencePose":{"landmarks":_standing()},"referenceImage":None,"threshold":70},
      {"type":"info","title":"Детали стойки","markdown":"## Базовая стойка\n\n### Ключевые точки:\n- **Ноги** на ширине плеч\n- **Колени** слегка согнуты (не заблокированы)\n- **Вес** на подушечках стоп\n- **Корпус** слегка вперёд\n- **Руки** свободно по бокам\n- **Плечи** опущены, расслаблены\n\nЭта стойка — ваша «нулевая позиция». Из неё начинаются все движения."},
    ]},
    {"t":"Первый Pop (хит)","xp":35,"steps":[
      {"type":"info","title":"Анатомия хита","markdown":"## Как работает Pop\n\n**Pop (хит)** — это быстрое **напряжение → расслабление** мышц.\n\n### Механика:\n1. Расслабьте руку полностью\n2. Резко напрягите все мышцы руки на долю секунды\n3. Мгновенно расслабьте\n\n### Ключевые мышцы для хита:\n- **Бицепс и трицепс** — основной хит руки\n- **Предплечье** — усиливает эффект\n- **Грудные** — для chest pop\n- **Шея** — для neck pop\n\nЦель: создать визуальный **рывок**, видимый со стороны."},
      {"type":"video-demo","title":"Первый Pop — демонстрация","videos":[{"url":YT["basic-pop"],"angle":"front"},{"url":YT["basic-pop"],"angle":"side"}],"description":"Демонстрация базового хита в руках: расслабление → резкое напряжение → расслабление. Обратите внимание на визуальный рывок."},
      {"type":"slow-motion","title":"Pop в замедленном повторе","video":YT["basic-pop"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная позиция — руки расслаблены"},
        {"time":1.0,"pose":{"landmarks":_pop_arms()},"description":"Момент хита — все мышцы рук напряжены"},
        {"time":1.5,"pose":{"landmarks":_standing()},"description":"Расслабление — мгновенный возврат"}
      ]},
      {"type":"pose-check","title":"Покажи свой Pop!","description":"Сделайте хит руками: напрягите бицепсы и предплечья, затем расслабьте.","referencePose":{"landmarks":_pop_arms()},"referenceImage":None,"threshold":65},
    ]},
    {"t":"Pop в руках","xp":30,"steps":[
      {"type":"video-demo","title":"Pop в руках — детальный разбор","videos":[{"url":YT["basic-pop"],"angle":"front"}],"description":"Хит в руках: бицепс, трицепс, предплечье. Тренируйте каждую руку отдельно, затем обе вместе."},
      {"type":"mirror-practice","title":"Тренировка попов в руках","referenceVideo":YT["basic-pop"],"duration":30,"threshold":55},
      {"type":"quiz","question":"Какие мышцы участвуют в хите рук?","options":[
        {"id":"a","text":"Только бицепс","correct":False},
        {"id":"b","text":"Бицепс, трицепс и предплечье","correct":True},
        {"id":"c","text":"Только плечи","correct":False},
        {"id":"d","text":"Только кисти","correct":False}
      ]},
    ]},
    {"t":"Pop в груди (chest pop)","xp":35,"steps":[
      {"type":"info","title":"Chest Pop — теория","markdown":"## Chest Pop\n\nChest pop — один из самых зрелищных элементов.\n\n### Как выполнять:\n1. Расслабьте грудь и плечи\n2. Резко вытолкните грудную клетку вперёд\n3. Одновременно отведите плечи назад\n4. Мгновенно верните в исходное\n\n### Частые ошибки:\n- Двигаете всё тело вместо изолированной груди\n- Слишком медленное движение (нет «рывка»)\n- Задерживаете дыхание"},
      {"type":"video-demo","title":"Chest Pop — демо","videos":[{"url":YT["chest-pop"],"angle":"front"},{"url":YT["chest-pop"],"angle":"side"}],"description":"Chest pop с фронтального и бокового ракурса. Обратите внимание: двигается ТОЛЬКО грудь."},
      {"type":"slow-motion","title":"Chest Pop — slow motion","video":YT["chest-pop"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная позиция"},
        {"time":1.2,"pose":{"landmarks":_chest_pop()},"description":"Грудь вперёд, плечи назад — момент хита"},
        {"time":1.8,"pose":{"landmarks":_standing()},"description":"Возврат в нейтраль"}
      ]},
      {"type":"pose-check","title":"Покажи Chest Pop","description":"Вытолкните грудь вперёд, плечи назад. Камера проверит положение.","referencePose":{"landmarks":_chest_pop()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Ритм + Pop","xp":40,"steps":[
      {"type":"info","title":"Связка: ритм + хиты","markdown":"## Собираем всё вместе\n\nТеперь совместим хиты с ритмом.\n\n### Связка из 4 хитов:\n1. **Бит 1** — Pop в правой руке\n2. **Бит 3** — Pop в левой руке\n3. **Бит 5** — Chest pop\n4. **Бит 7** — Pop обеими руками\n\nПовторяйте под музыку 100 BPM."},
      {"type":"video-demo","title":"Связка Ритм + Pop","videos":[{"url":YT["pop-music"],"angle":"front"}],"description":"4 хита в ритм: правая рука → левая рука → грудь → обе руки. Повторяем 4 такта."},
      {"type":"combo-challenge","title":"Первая связка!","music":MUSIC,"bpm":100,"moves":[
        {"name":"Pop правой рукой","pose":{"landmarks":_pop_arms()},"beatStart":1,"beatEnd":2},
        {"name":"Pop левой рукой","pose":{"landmarks":_pop_arms()},"beatStart":3,"beatEnd":4},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":5,"beatEnd":6},
        {"name":"Pop обеими руками","pose":{"landmarks":_pop_arms()},"beatStart":7,"beatEnd":8}
      ],"threshold":55},
    ]},
  ]},

  # ==================== Level 2: Базовые хиты и Fresno ====================
  {"title":"Уровень 2: Базовые хиты и Fresno","pos":1,"lessons":[
    {"t":"Fresno — основной шаг","xp":35,"steps":[
      {"type":"video-demo","title":"Fresno — разбор шага","videos":[{"url":YT["fresno"],"angle":"front"},{"url":YT["fresno"],"angle":"side"}],"description":"Fresno — фирменный шаг Popping. Шаг в сторону с хитом, возврат. Поочерёдно влево-вправо."},
      {"type":"slow-motion","title":"Fresno — slow motion","video":YT["fresno"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная — ноги вместе"},
        {"time":1.5,"pose":{"landmarks":_fresno()},"description":"Шаг влево + хит"},
        {"time":2.5,"pose":{"landmarks":_standing()},"description":"Возврат в центр"},
        {"time":3.5,"pose":{"landmarks":_fresno()},"description":"Шаг вправо + хит"}
      ]},
      {"type":"pose-check","title":"Покажи Fresno","description":"Выполните шаг Fresno влево с хитом.","referencePose":{"landmarks":_fresno()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Fresno в ритм","xp":30,"steps":[
      {"type":"mirror-practice","title":"Fresno под музыку","referenceVideo":YT["fresno"],"duration":30,"threshold":55},
      {"type":"quiz","question":"На какой бит обычно делается хит в Fresno?","options":[
        {"id":"a","text":"На каждый бит","correct":False},
        {"id":"b","text":"На 1 и 5","correct":True},
        {"id":"c","text":"Только на 8","correct":False},
        {"id":"d","text":"Между битами","correct":False}
      ]},
    ]},
    {"t":"Neck Pop","xp":35,"steps":[
      {"type":"video-demo","title":"Neck Pop — демо","videos":[{"url":YT["neck-pop"],"angle":"front"}],"description":"Neck Pop: резкое смещение головы в сторону. Шея расслаблена → резкий сдвиг → возврат."},
      {"type":"pose-check","title":"Проверка Neck Pop","description":"Сделайте Neck Pop — резко сместите голову в сторону.","referencePose":{"landmarks":_neck_pop()},"referenceImage":None,"threshold":60},
      {"type":"quiz","question":"Что НЕЛЬЗЯ делать при Neck Pop?","options":[
        {"id":"a","text":"Расслаблять шею перед хитом","correct":False},
        {"id":"b","text":"Делать круговые резкие движения","correct":True},
        {"id":"c","text":"Смещать голову в сторону","correct":False},
        {"id":"d","text":"Возвращать голову в центр","correct":False}
      ]},
    ]},
    {"t":"Leg Pop","xp":35,"steps":[
      {"type":"video-demo","title":"Leg Pop — демо","videos":[{"url":YT["neck-pop"],"angle":"front"}],"description":"Leg Pop: хит через ноги. Колено слегка сгибается, затем резко выпрямляется с напряжением квадрицепса."},
      {"type":"slow-motion","title":"Leg Pop — slow motion","video":YT["neck-pop"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная — стоим ровно"},
        {"time":1.2,"pose":{"landmarks":_leg_pop()},"description":"Колено согнуто, вес на задней ноге"},
        {"time":1.8,"pose":{"landmarks":_standing()},"description":"Резкое выпрямление — хит!"}
      ]},
      {"type":"pose-check","title":"Покажи Leg Pop","description":"Согните колено и резко выпрямите с хитом.","referencePose":{"landmarks":_leg_pop()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Hit Combo — руки + грудь + ноги","xp":40,"steps":[
      {"type":"info","title":"Комбинируем хиты","markdown":"## Full Body Hit Combo\n\nТеперь собираем все хиты вместе:\n\n1. **Бит 1-2**: Arm Pop (обе руки)\n2. **Бит 3-4**: Chest Pop\n3. **Бит 5-6**: Leg Pop\n4. **Бит 7-8**: Full Body Pop (всё вместе)\n\nКаждый хит должен быть чётким и резким."},
      {"type":"combo-challenge","title":"Hit Combo Challenge","music":MUSIC,"bpm":100,"moves":[
        {"name":"Arm Pop","pose":{"landmarks":_pop_arms()},"beatStart":1,"beatEnd":2},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":3,"beatEnd":4},
        {"name":"Leg Pop","pose":{"landmarks":_leg_pop()},"beatStart":5,"beatEnd":6},
        {"name":"Full Body Pop","pose":{"landmarks":_pop_arms()},"beatStart":7,"beatEnd":8}
      ],"threshold":55},
    ]},
    {"t":"Dimestop","xp":35,"steps":[
      {"type":"video-demo","title":"Dimestop — мгновенная остановка","videos":[{"url":YT["dimestop"],"angle":"front"}],"description":"Dimestop: двигаетесь и мгновенно замираете, как статуя. Полная остановка всего тела."},
      {"type":"slow-motion","title":"Dimestop — slow motion","video":YT["dimestop"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Движение — тело в динамике"},
        {"time":1.5,"pose":{"landmarks":_dimestop()},"description":"СТОП — полная заморозка"},
        {"time":3.0,"pose":{"landmarks":_dimestop()},"description":"Удержание позы 1-2 секунды"}
      ]},
      {"type":"pose-check","title":"Покажи Dimestop","description":"Замрите в позе — полная остановка, рука вытянута.","referencePose":{"landmarks":_dimestop()},"referenceImage":None,"threshold":65},
    ]},
    {"t":"Walkout","xp":30,"steps":[
      {"type":"video-demo","title":"Walkout — выход на танцпол","videos":[{"url":YT["walkout"],"angle":"front"}],"description":"Walkout: стильный выход с попами. Шагаем, добавляя хиты на каждый шаг."},
      {"type":"mirror-practice","title":"Практика Walkout","referenceVideo":YT["walkout"],"duration":30,"threshold":55},
      {"type":"quiz","question":"Что такое Walkout в Popping?","options":[
        {"id":"a","text":"Обычная ходьба","correct":False},
        {"id":"b","text":"Стильный выход с хитами на каждый шаг","correct":True},
        {"id":"c","text":"Прыжки","correct":False},
        {"id":"d","text":"Бег на месте","correct":False}
      ]},
    ]},
    {"t":"Boogaloo Roll","xp":35,"steps":[
      {"type":"video-demo","title":"Boogaloo Roll","videos":[{"url":YT["boogaloo"],"angle":"front"}],"description":"Boogaloo Roll: круговое движение корпуса, перетекающее от плеч к бёдрам. Мягкое, волнообразное."},
      {"type":"slow-motion","title":"Boogaloo Roll — slow motion","video":YT["boogaloo"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная позиция"},
        {"time":1.5,"pose":{"landmarks":_boogaloo_roll()},"description":"Корпус уходит в круговое движение"},
        {"time":3.0,"pose":{"landmarks":_standing()},"description":"Завершение круга, возврат"}
      ]},
      {"type":"pose-check","title":"Покажи Boogaloo Roll","description":"Выполните круговое движение корпуса.","referencePose":{"landmarks":_boogaloo_roll()},"referenceImage":None,"threshold":55},
    ]},
    {"t":"Связка Level 2","xp":40,"steps":[
      {"type":"info","title":"Связка из 6 движений","markdown":"## Связка Level 2\n\n1. **Fresno влево** (бит 1-2)\n2. **Fresno вправо** (бит 3-4)\n3. **Neck Pop** (бит 5)\n4. **Chest Pop** (бит 6)\n5. **Walkout 2 шага** (бит 7-8)\n6. **Dimestop** (бит 1 следующего такта)"},
      {"type":"combo-challenge","title":"Связка Level 2","music":MUSIC,"bpm":105,"moves":[
        {"name":"Fresno влево","pose":{"landmarks":_fresno()},"beatStart":1,"beatEnd":2},
        {"name":"Fresno вправо","pose":{"landmarks":_fresno()},"beatStart":3,"beatEnd":4},
        {"name":"Neck Pop","pose":{"landmarks":_neck_pop()},"beatStart":5,"beatEnd":5},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":6,"beatEnd":6},
        {"name":"Walkout","pose":{"landmarks":_standing()},"beatStart":7,"beatEnd":8},
        {"name":"Dimestop","pose":{"landmarks":_dimestop()},"beatStart":9,"beatEnd":10}
      ],"threshold":55},
    ]},
    {"t":"Мини-баттл Level 2","xp":50,"steps":[
      {"type":"info","title":"Твой первый баттл!","markdown":"## Мини-баттл\n\nИспользуй все движения Level 1 и 2.\n\n**Правила:**\n- 30 секунд под музыку\n- Используй минимум 3 разных движения\n- Попадай в бит!\n- Закончи Dimestop'ом"},
      {"type":"battle-sim","title":"Мини-баттл 30 сек","music":MUSIC,"duration":30,"bpm":105},
    ]},
  ]},

  # ==================== Level 3: Изоляции ====================
  {"title":"Уровень 3: Изоляции","pos":2,"lessons":[
    {"t":"Что такое изоляции","xp":20,"steps":[
      {"type":"info","title":"Принцип изоляции","markdown":"## Изоляции в Popping\n\n**Изоляция** — способность двигать одну часть тела, пока остальные остаются неподвижными.\n\n### Почему это важно?\n- Делает танец чистым и чётким\n- Основа для стилей Robot, Animation, Tutting\n- Улучшает контроль тела\n- Усиливает визуальный эффект хитов\n\n### Части тела для изоляций:\n1. Голова\n2. Плечи\n3. Грудь\n4. Бёдра\n5. Руки / пальцы\n\nПравило: двигается ТОЛЬКО целевая часть тела!"},
      {"type":"quiz","question":"Что такое изоляция в танце?","options":[
        {"id":"a","text":"Танец в одиночку","correct":False},
        {"id":"b","text":"Движение одной части тела при неподвижности остальных","correct":True},
        {"id":"c","text":"Быстрое вращение","correct":False},
        {"id":"d","text":"Прыжки на месте","correct":False}
      ]},
      {"type":"true-false","statement":"Изоляции используются только в стиле Robot.","correct":False},
    ]},
    {"t":"Изоляция головы","xp":35,"steps":[
      {"type":"video-demo","title":"Изоляция головы","videos":[{"url":YT["iso-head"],"angle":"front"}],"description":"Изоляция головы: вперёд-назад, влево-вправо, по кругу. Плечи НЕ двигаются!"},
      {"type":"slow-motion","title":"Изоляция головы — slow motion","video":YT["iso-head"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Нейтраль — голова по центру"},
        {"time":1.5,"pose":{"landmarks":_iso_head()},"description":"Голова сдвинута влево, плечи неподвижны"},
        {"time":2.5,"pose":{"landmarks":_standing()},"description":"Возврат в центр"}
      ]},
      {"type":"pose-check","title":"Проверка изоляции головы","description":"Сдвиньте голову влево, не двигая плечами.","referencePose":{"landmarks":_iso_head()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Изоляция плеч","xp":35,"steps":[
      {"type":"video-demo","title":"Изоляция плеч","videos":[{"url":YT["iso-shoulders"],"angle":"front"}],"description":"Одно плечо вверх, другое вниз. Поочерёдно. Голова и бёдра неподвижны."},
      {"type":"pose-check","title":"Проверка изоляции плеч","description":"Поднимите левое плечо вверх, правое вниз.","referencePose":{"landmarks":_iso_shoulders()},"referenceImage":None,"threshold":60},
      {"type":"mirror-practice","title":"Практика изоляции плеч","referenceVideo":YT["iso-shoulders"],"duration":30,"threshold":55},
    ]},
    {"t":"Изоляция груди","xp":35,"steps":[
      {"type":"video-demo","title":"Изоляция груди","videos":[{"url":YT["iso-chest"],"angle":"front"}],"description":"Грудь двигается влево-вправо, вперёд-назад. Бёдра и голова остаются на месте."},
      {"type":"slow-motion","title":"Изоляция груди — slow motion","video":YT["iso-chest"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Центр — нейтральная позиция"},
        {"time":1.5,"pose":{"landmarks":_iso_chest()},"description":"Грудь сдвинута вправо"},
        {"time":2.5,"pose":{"landmarks":_standing()},"description":"Возврат"},
        {"time":3.5,"pose":{"landmarks":_chest_pop()},"description":"Грудь вперёд"}
      ]},
      {"type":"pose-check","title":"Проверка изоляции груди","description":"Сдвиньте грудь вправо, бёдра неподвижны.","referencePose":{"landmarks":_iso_chest()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Изоляция бёдер","xp":30,"steps":[
      {"type":"video-demo","title":"Изоляция бёдер","videos":[{"url":YT["iso-hips"],"angle":"front"}],"description":"Бёдра двигаются влево-вправо, по кругу. Верхняя часть тела остаётся неподвижной."},
      {"type":"pose-check","title":"Проверка изоляции бёдер","description":"Сдвиньте бёдра влево, плечи на месте.","referencePose":{"landmarks":_iso_hips()},"referenceImage":None,"threshold":60},
      {"type":"quiz","question":"Какая часть тела должна оставаться неподвижной при изоляции бёдер?","options":[
        {"id":"a","text":"Колени","correct":False},
        {"id":"b","text":"Плечи и голова","correct":True},
        {"id":"c","text":"Стопы","correct":False},
        {"id":"d","text":"Ничего, всё двигается","correct":False}
      ]},
    ]},
    {"t":"Изоляция рук (Tutting basics)","xp":35,"steps":[
      {"type":"video-demo","title":"Tutting — базовые фигуры","videos":[{"url":YT["tutting"],"angle":"front"}],"description":"Tutting: создание геометрических фигур руками. Углы строго 90°. Каждый сегмент руки двигается отдельно."},
      {"type":"slow-motion","title":"Tutting — slow motion","video":YT["tutting"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Руки расслаблены"},
        {"time":1.5,"pose":{"landmarks":_tutting()},"description":"Руки вытянуты в стороны, предплечья вверх под 90°"},
        {"time":3.0,"pose":{"landmarks":_tutting()},"description":"Фиксация угловой позиции"}
      ]},
      {"type":"pose-check","title":"Покажи Tutting","description":"Руки в стороны, предплечья вверх под углом 90 градусов.","referencePose":{"landmarks":_tutting()},"referenceImage":None,"threshold":60},
    ]},
    {"t":"Комбо изоляций","xp":40,"steps":[
      {"type":"info","title":"Комбо изоляций","markdown":"## Связка изоляций\n\n1. **Бит 1-2**: Изоляция головы (влево-вправо)\n2. **Бит 3-4**: Изоляция плеч (вверх-вниз)\n3. **Бит 5-6**: Изоляция груди (влево-вправо)\n4. **Бит 7-8**: Изоляция бёдер (влево-вправо)\n\nПлавно перетекайте от одной изоляции к другой."},
      {"type":"combo-challenge","title":"Isolation Combo","music":MUSIC,"bpm":100,"moves":[
        {"name":"Изоляция головы","pose":{"landmarks":_iso_head()},"beatStart":1,"beatEnd":2},
        {"name":"Изоляция плеч","pose":{"landmarks":_iso_shoulders()},"beatStart":3,"beatEnd":4},
        {"name":"Изоляция груди","pose":{"landmarks":_iso_chest()},"beatStart":5,"beatEnd":6},
        {"name":"Изоляция бёдер","pose":{"landmarks":_iso_hips()},"beatStart":7,"beatEnd":8}
      ],"threshold":55},
    ]},
    {"t":"Робот (Robot style)","xp":35,"steps":[
      {"type":"video-demo","title":"Robot — механический стиль","videos":[{"url":YT["robot"],"angle":"front"}],"description":"Robot: двигайтесь как робот. Каждое движение отдельное, с паузой-фиксацией. Используйте dimestop между движениями."},
      {"type":"mirror-practice","title":"Практика Robot","referenceVideo":YT["robot"],"duration":45,"threshold":55},
      {"type":"quiz","question":"Какой принцип лежит в основе стиля Robot?","options":[
        {"id":"a","text":"Плавность и текучесть","correct":False},
        {"id":"b","text":"Изолированные механические движения с паузами","correct":True},
        {"id":"c","text":"Максимальная скорость","correct":False},
        {"id":"d","text":"Случайные движения","correct":False}
      ]},
    ]},
    {"t":"Связка Level 3","xp":40,"steps":[
      {"type":"combo-challenge","title":"Связка Level 3 — 8 движений","music":MUSIC,"bpm":105,"moves":[
        {"name":"Robot walk","pose":{"landmarks":_robot()},"beatStart":1,"beatEnd":2},
        {"name":"Изоляция головы","pose":{"landmarks":_iso_head()},"beatStart":3,"beatEnd":4},
        {"name":"Изоляция плеч","pose":{"landmarks":_iso_shoulders()},"beatStart":5,"beatEnd":6},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":7,"beatEnd":8},
        {"name":"Tutting","pose":{"landmarks":_tutting()},"beatStart":9,"beatEnd":10},
        {"name":"Изоляция бёдер","pose":{"landmarks":_iso_hips()},"beatStart":11,"beatEnd":12},
        {"name":"Fresno","pose":{"landmarks":_fresno()},"beatStart":13,"beatEnd":14},
        {"name":"Dimestop","pose":{"landmarks":_dimestop()},"beatStart":15,"beatEnd":16}
      ],"threshold":55},
    ]},
    {"t":"Баттл Level 3","xp":50,"steps":[
      {"type":"info","title":"Баттл Level 3","markdown":"## Баттл — изоляции\n\n**45 секунд** под музыку. Покажи все изоляции + хиты.\n\n**Задание:**\n- Начни с Robot walk\n- Покажи минимум 4 разные изоляции\n- Добавь хиты\n- Финиш — Dimestop"},
      {"type":"battle-sim","title":"Баттл Level 3 — 45 сек","music":MUSIC,"duration":45,"bpm":105},
    ]},
  ]},

  # ==================== Level 4: Волны и глайды ====================
  {"title":"Уровень 4: Волны и глайды","pos":3,"lessons":[
    {"t":"Arm Wave (волна рукой)","xp":35,"steps":[
      {"type":"video-demo","title":"Arm Wave","videos":[{"url":YT["arm-wave"],"angle":"front"}],"description":"Волна рукой: движение перетекает от кончиков пальцев одной руки через плечи к другой. Каждый сустав включается последовательно."},
      {"type":"slow-motion","title":"Arm Wave — slow motion","video":YT["arm-wave"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_arm_wave()},"description":"Начало волны — пальцы левой руки"},
        {"time":1.5,"pose":{"landmarks":_standing()},"description":"Волна проходит через плечи"},
        {"time":2.5,"pose":{"landmarks":_arm_wave()},"description":"Волна дошла до правой руки"}
      ]},
      {"type":"mirror-practice","title":"Практика Arm Wave","referenceVideo":YT["arm-wave"],"duration":30,"threshold":50},
    ]},
    {"t":"Body Wave (волна телом)","xp":35,"steps":[
      {"type":"video-demo","title":"Body Wave","videos":[{"url":YT["body-wave"],"angle":"side"}],"description":"Волна проходит через всё тело: голова → грудь → живот → бёдра → колени. Плавное, непрерывное движение."},
      {"type":"slow-motion","title":"Body Wave — slow motion","video":YT["body-wave"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Начало — нейтральная позиция"},
        {"time":1.2,"pose":{"landmarks":_body_wave()},"description":"Волна проходит через грудь"},
        {"time":2.0,"pose":{"landmarks":_iso_hips()},"description":"Волна на уровне бёдер"},
        {"time":2.8,"pose":{"landmarks":_standing()},"description":"Завершение волны"}
      ]},
      {"type":"pose-check","title":"Проверка Body Wave","description":"Выполните волну телом — грудь вперёд, бёдра назад.","referencePose":{"landmarks":_body_wave()},"referenceImage":None,"threshold":55},
    ]},
    {"t":"Finger Wave","xp":30,"steps":[
      {"type":"video-demo","title":"Finger Wave","videos":[{"url":YT["finger-wave"],"angle":"front"}],"description":"Волна пальцами: каждый палец поднимается и опускается последовательно. Мизинец → безымянный → средний → указательный → большой."},
      {"type":"pose-check","title":"Проверка Finger Wave","description":"Вытяните руку и покажите волну пальцами.","referencePose":{"landmarks":_finger_wave()},"referenceImage":None,"threshold":55},
      {"type":"quiz","question":"В каком порядке двигаются пальцы при Finger Wave?","options":[
        {"id":"a","text":"Все одновременно","correct":False},
        {"id":"b","text":"От мизинца к большому","correct":True},
        {"id":"c","text":"От большого к мизинцу","correct":False},
        {"id":"d","text":"Случайно","correct":False}
      ]},
    ]},
    {"t":"Glide (скольжение)","xp":30,"steps":[
      {"type":"video-demo","title":"Glide — базовый","videos":[{"url":YT["glide"],"angle":"front"},{"url":YT["glide"],"angle":"side"}],"description":"Glide: иллюзия скольжения по полу. Одна нога скользит назад, пока другая поднимается на носок."},
      {"type":"slow-motion","title":"Glide — slow motion","video":YT["glide"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Исходная позиция"},
        {"time":1.5,"pose":{"landmarks":_glide()},"description":"Правая нога скользит назад, левая на носке"},
        {"time":2.5,"pose":{"landmarks":_standing()},"description":"Смена ног"},
        {"time":3.5,"pose":{"landmarks":_glide()},"description":"Левая скользит, правая на носке"}
      ]},
    ]},
    {"t":"Moonwalk","xp":35,"steps":[
      {"type":"video-demo","title":"Moonwalk","videos":[{"url":YT["glide"],"angle":"side"}],"description":"Moonwalk: классическое скольжение назад. Одна нога плоская, другая на носке. Плоская скользит назад, затем меняемся."},
      {"type":"slow-motion","title":"Moonwalk — slow motion","video":YT["glide"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_standing()},"description":"Начало — вес на правой ноге"},
        {"time":1.5,"pose":{"landmarks":_moonwalk()},"description":"Левая скользит назад, правая на носке"},
        {"time":2.5,"pose":{"landmarks":_moonwalk()},"description":"Смена — правая скользит, левая на носке"}
      ]},
      {"type":"mirror-practice","title":"Практика Moonwalk","referenceVideo":YT["glide"],"duration":30,"threshold":50},
    ]},
    {"t":"Float / Air Walk","xp":30,"steps":[
      {"type":"video-demo","title":"Float","videos":[{"url":YT["float"],"angle":"front"}],"description":"Float / Air Walk: иллюзия ходьбы по воздуху. Комбинация подъёма на носки и скольжения."},
      {"type":"pose-check","title":"Проверка Float","description":"Выполните Float — поднимитесь на носки одной ноги, скользите другой.","referencePose":{"landmarks":_glide()},"referenceImage":None,"threshold":55},
      {"type":"quiz","question":"Что общего между Glide, Moonwalk и Float?","options":[
        {"id":"a","text":"Все используют прыжки","correct":False},
        {"id":"b","text":"Все создают иллюзию скольжения","correct":True},
        {"id":"c","text":"Все требуют специальной обуви","correct":False},
        {"id":"d","text":"Все выполняются только на месте","correct":False}
      ]},
    ]},
    {"t":"Snake (змейка)","xp":30,"steps":[
      {"type":"video-demo","title":"Snake","videos":[{"url":YT["snake"],"angle":"side"}],"description":"Snake: волнообразное движение всего тела, как змея. Голова ведёт, тело следует волной."},
      {"type":"mirror-practice","title":"Практика Snake","referenceVideo":YT["snake"],"duration":30,"threshold":50},
      {"type":"info","title":"Советы по Snake","markdown":"## Snake — ключевые моменты\n\n- Голова **ведёт** движение\n- Тело **следует** с задержкой\n- Чем медленнее — тем лучше выглядит\n- Совмещайте с Body Wave для эффекта"},
    ]},
    {"t":"Волна + Pop комбинация","xp":40,"steps":[
      {"type":"info","title":"Волны + хиты","markdown":"## Комбинация волн и хитов\n\n1. **Arm Wave** → **Pop** в конце волны\n2. **Body Wave** → **Chest Pop**\n3. **Snake** → **Dimestop**\n\nВолна создаёт плавность, Pop — акцент!"},
      {"type":"combo-challenge","title":"Wave + Pop Combo","music":MUSIC,"bpm":100,"moves":[
        {"name":"Arm Wave","pose":{"landmarks":_arm_wave()},"beatStart":1,"beatEnd":4},
        {"name":"Arm Pop","pose":{"landmarks":_pop_arms()},"beatStart":5,"beatEnd":5},
        {"name":"Body Wave","pose":{"landmarks":_body_wave()},"beatStart":6,"beatEnd":9},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":10,"beatEnd":10},
        {"name":"Snake","pose":{"landmarks":_snake()},"beatStart":11,"beatEnd":14},
        {"name":"Dimestop","pose":{"landmarks":_dimestop()},"beatStart":15,"beatEnd":16}
      ],"threshold":55},
    ]},
    {"t":"Связка Level 4","xp":40,"steps":[
      {"type":"combo-challenge","title":"Связка Level 4 — 10 движений","music":MUSIC,"bpm":108,"moves":[
        {"name":"Arm Wave L→R","pose":{"landmarks":_arm_wave()},"beatStart":1,"beatEnd":3},
        {"name":"Pop","pose":{"landmarks":_pop_arms()},"beatStart":4,"beatEnd":4},
        {"name":"Body Wave","pose":{"landmarks":_body_wave()},"beatStart":5,"beatEnd":7},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":8,"beatEnd":8},
        {"name":"Moonwalk","pose":{"landmarks":_moonwalk()},"beatStart":9,"beatEnd":12},
        {"name":"Snake","pose":{"landmarks":_snake()},"beatStart":13,"beatEnd":15},
        {"name":"Dimestop","pose":{"landmarks":_dimestop()},"beatStart":16,"beatEnd":16},
        {"name":"Fresno","pose":{"landmarks":_fresno()},"beatStart":17,"beatEnd":18},
        {"name":"Tutting","pose":{"landmarks":_tutting()},"beatStart":19,"beatEnd":20},
        {"name":"Final Pop","pose":{"landmarks":_pop_arms()},"beatStart":21,"beatEnd":22}
      ],"threshold":55},
    ]},
    {"t":"Баттл Level 4","xp":50,"steps":[
      {"type":"info","title":"Баттл Level 4","markdown":"## Баттл — волны и глайды\n\n**60 секунд!** Покажи всё: хиты, изоляции, волны, глайды.\n\n**Подсказки:**\n- Начни плавно (волна)\n- Усиль (хиты)\n- Удиви (глайд/moonwalk)\n- Финиш — мощный Dimestop"},
      {"type":"battle-sim","title":"Баттл Level 4 — 60 сек","music":MUSIC,"duration":60,"bpm":108},
    ]},
  ]},

  # ==================== Level 5: Фристайл и комбинации ====================
  {"title":"Уровень 5: Фристайл и комбинации","pos":4,"lessons":[
    {"t":"Принципы фристайла","xp":20,"steps":[
      {"type":"info","title":"Фристайл в Popping","markdown":"## Принципы фристайла\n\n### Музыкальность\n- Слушай музыку, танцуй ПОД неё, а не поверх\n- Реагируй на акценты, брейки, изменения\n- Используй паузы!\n\n### Storytelling\n- Каждый раунд — мини-история\n- Начало (вход) → Развитие → Кульминация → Финал\n\n### Levels (уровни пространства)\n- **Верхний**: стоя, руки вверх\n- **Средний**: полуприсед, наклоны\n- **Нижний**: floor work, колени\n\n### Разнообразие\n- Миксуй стили: waves + pops + isolations\n- Чередуй скорости\n- Удивляй зрителя"},
      {"type":"quiz","question":"Что НЕ является принципом фристайла?","options":[
        {"id":"a","text":"Музыкальность","correct":False},
        {"id":"b","text":"Storytelling","correct":False},
        {"id":"c","text":"Повторение одного движения","correct":True},
        {"id":"d","text":"Использование levels","correct":False}
      ]},
      {"type":"multi-select","question":"Какие уровни пространства используются во фристайле?","options":[
        {"id":"a","text":"Верхний (стоя, руки вверх)","correct":True},
        {"id":"b","text":"Подземный (лёжа на спине)","correct":False},
        {"id":"c","text":"Средний (полуприсед)","correct":True},
        {"id":"d","text":"Нижний (floor work)","correct":True}
      ]},
    ]},
    {"t":"Характер и стиль","xp":20,"steps":[
      {"type":"info","title":"Стили внутри Popping","markdown":"## Суб-стили Popping\n\n### Boogaloo\n- Плавные, круговые движения тела\n- Роллы, вращения\n- Мягкая подача\n\n### Animation\n- Иллюзия покадровой анимации\n- Движения рывками, как стоп-моушн\n- Dimestop между каждым «кадром»\n\n### Robot\n- Механические, изолированные движения\n- Чёткие углы\n- Гидравлические паузы\n\n### Waving\n- Волнообразные движения\n- Arm waves, body waves\n- Плавность и текучесть\n\n### Strutting\n- Шаги с хитами\n- Включает Fresno, walkout\n- Основа перемещений"},
      {"type":"quiz","question":"Какой стиль основан на иллюзии покадровой анимации?","options":[
        {"id":"a","text":"Boogaloo","correct":False},
        {"id":"b","text":"Animation","correct":True},
        {"id":"c","text":"Waving","correct":False},
        {"id":"d","text":"Strutting","correct":False}
      ]},
      {"type":"matching","pairs":[
        {"left":"Boogaloo","right":"Плавные круговые движения"},
        {"left":"Animation","right":"Покадровая иллюзия"},
        {"left":"Robot","right":"Механические движения"},
        {"left":"Waving","right":"Волнообразные движения"},
        {"left":"Strutting","right":"Шаги с хитами"}
      ]},
    ]},
    {"t":"Floor work","xp":35,"steps":[
      {"type":"video-demo","title":"Floor work — работа на полу","videos":[{"url":YT["floor-work"],"angle":"front"}],"description":"Floor work: переходы на нижний уровень. Колени, присед, спин. Плавный вход и мощный выход."},
      {"type":"pose-check","title":"Проверка Floor work","description":"Опуститесь на нижний уровень — присед или на колено.","referencePose":{"landmarks":_floor_work()},"referenceImage":None,"threshold":55},
      {"type":"quiz","question":"Когда лучше всего использовать Floor work в баттле?","options":[
        {"id":"a","text":"В самом начале","correct":False},
        {"id":"b","text":"Как сюрприз для разнообразия","correct":True},
        {"id":"c","text":"Весь раунд на полу","correct":False},
        {"id":"d","text":"Никогда","correct":False}
      ]},
    ]},
    {"t":"Levels (уровни)","xp":30,"steps":[
      {"type":"video-demo","title":"Три уровня пространства","videos":[{"url":YT["levels"],"angle":"front"}],"description":"Демонстрация трёх уровней: верхний (стоя, руки вверх), средний (полуприсед, обычная стойка), нижний (floor work). Переходы между уровнями."},
      {"type":"info","title":"Как использовать Levels","markdown":"## Levels — уровни пространства\n\n### Верхний\n- Руки вверх, на носках\n- Tutting на высоте\n- Энергичные хиты\n\n### Средний\n- Стандартная стойка\n- Основная зона работы\n- Большинство движений\n\n### Нижний\n- Приседы, колени\n- Floor work\n- Драматичные моменты\n\n### Правило: меняй level каждые 4-8 битов!"},
      {"type":"true-false","statement":"В баттле нужно использовать только один уровень пространства.","correct":False},
    ]},
    {"t":"Transition moves","xp":30,"steps":[
      {"type":"video-demo","title":"Переходы между движениями","videos":[{"url":YT["transitions"],"angle":"front"}],"description":"Transitions: как плавно переходить от одного движения к другому. Волна → хит, робот → boogaloo, стоя → floor."},
      {"type":"slow-motion","title":"Transitions — slow motion","video":YT["transitions"],"keyframes":[
        {"time":0.5,"pose":{"landmarks":_robot()},"description":"Robot pose — механическая"},
        {"time":2.0,"pose":{"landmarks":_body_wave()},"description":"Переход: размягчение в body wave"},
        {"time":3.5,"pose":{"landmarks":_pop_arms()},"description":"Финиш: резкий pop для контраста"}
      ]},
      {"type":"quiz","question":"Зачем нужны transitions?","options":[
        {"id":"a","text":"Чтобы отдохнуть между движениями","correct":False},
        {"id":"b","text":"Для плавного и красивого перехода между стилями","correct":True},
        {"id":"c","text":"Они не нужны","correct":False},
        {"id":"d","text":"Чтобы запутать судей","correct":False}
      ]},
    ]},
    {"t":"Создание комбинаций","xp":35,"steps":[
      {"type":"info","title":"Как создавать свои комбо","markdown":"## Создание комбинаций\n\n### Формула:\n1. **Вход** (2 бита) — Walkout или Fresno\n2. **Основная часть** (8 битов) — миксуй 3-4 разных техники\n3. **Кульминация** (2 бита) — самое сложное/эффектное\n4. **Финиш** (2 бита) — Dimestop или мощный хит\n\n### Правила:\n- Не повторяй одно движение подряд\n- Чередуй мягкое и резкое\n- Используй разные levels\n- Всегда заканчивай чётко\n\n### Задание:\nСоздай свою комбинацию из 6+ движений!"},
      {"type":"combo-challenge","title":"Твоя комбинация","music":MUSIC,"bpm":108,"moves":[
        {"name":"Fresno вход","pose":{"landmarks":_fresno()},"beatStart":1,"beatEnd":2},
        {"name":"Arm Wave","pose":{"landmarks":_arm_wave()},"beatStart":3,"beatEnd":5},
        {"name":"Pop","pose":{"landmarks":_pop_arms()},"beatStart":6,"beatEnd":6},
        {"name":"Robot walk","pose":{"landmarks":_robot()},"beatStart":7,"beatEnd":9},
        {"name":"Body Wave","pose":{"landmarks":_body_wave()},"beatStart":10,"beatEnd":12},
        {"name":"Chest Pop","pose":{"landmarks":_chest_pop()},"beatStart":13,"beatEnd":13},
        {"name":"Moonwalk","pose":{"landmarks":_moonwalk()},"beatStart":14,"beatEnd":16},
        {"name":"Dimestop финиш","pose":{"landmarks":_dimestop()},"beatStart":17,"beatEnd":18}
      ],"threshold":50},
    ]},
    {"t":"Performance и подача","xp":20,"steps":[
      {"type":"info","title":"Подача и харизма","markdown":"## Performance\n\n### Как подать танец:\n- **Лицо**: не каменное! Эмоции, характер\n- **Глаза**: смотри на зрителя/камеру\n- **Уверенность**: даже если ошибся — продолжай\n- **Энергия**: начинай на 70%, к финалу — на 100%\n\n### В баттле:\n- Слушай музыку оппонента\n- Не повторяй его движения\n- Покажи свой стиль\n- Заканчивай МОЩНО\n\n### Совет:\nЗаписывай себя на видео и анализируй!"},
      {"type":"video-demo","title":"Performance tips","videos":[{"url":YT["performance"],"angle":"front"}],"description":"Примеры хорошей и плохой подачи. Разница между техникой и шоу."},
      {"type":"true-false","statement":"Если ты ошибся в баттле, нужно остановиться и начать заново.","correct":False},
    ]},
    {"t":"Полная комбинация","xp":40,"steps":[
      {"type":"info","title":"Финальная комбинация","markdown":"## Полная комбинация — 12+ движений\n\nВсё, что вы изучили, в одной связке.\n\n### План:\n1. Walkout вход\n2. Fresno × 2\n3. Arm Wave → Pop\n4. Изоляция плеч → груди\n5. Body Wave\n6. Robot transition\n7. Moonwalk\n8. Snake\n9. Floor work moment\n10. Встаём → Tutting\n11. Combo pops\n12. DIMESTOP финиш!"},
      {"type":"combo-challenge","title":"Полная комбинация","music":MUSIC,"bpm":110,"moves":[
        {"name":"Walkout","pose":{"landmarks":_standing()},"beatStart":1,"beatEnd":2},
        {"name":"Fresno L","pose":{"landmarks":_fresno()},"beatStart":3,"beatEnd":4},
        {"name":"Fresno R","pose":{"landmarks":_fresno()},"beatStart":5,"beatEnd":6},
        {"name":"Arm Wave","pose":{"landmarks":_arm_wave()},"beatStart":7,"beatEnd":9},
        {"name":"Pop","pose":{"landmarks":_pop_arms()},"beatStart":10,"beatEnd":10},
        {"name":"Iso плечи","pose":{"landmarks":_iso_shoulders()},"beatStart":11,"beatEnd":12},
        {"name":"Iso грудь","pose":{"landmarks":_iso_chest()},"beatStart":13,"beatEnd":14},
        {"name":"Body Wave","pose":{"landmarks":_body_wave()},"beatStart":15,"beatEnd":17},
        {"name":"Robot","pose":{"landmarks":_robot()},"beatStart":18,"beatEnd":20},
        {"name":"Moonwalk","pose":{"landmarks":_moonwalk()},"beatStart":21,"beatEnd":24},
        {"name":"Snake","pose":{"landmarks":_snake()},"beatStart":25,"beatEnd":27},
        {"name":"Tutting","pose":{"landmarks":_tutting()},"beatStart":28,"beatEnd":30},
        {"name":"Combo Pops","pose":{"landmarks":_pop_arms()},"beatStart":31,"beatEnd":33},
        {"name":"DIMESTOP","pose":{"landmarks":_dimestop()},"beatStart":34,"beatEnd":36}
      ],"threshold":50},
    ]},
    {"t":"Тренировочный баттл","xp":50,"steps":[
      {"type":"info","title":"Тренировочный баттл","markdown":"## 60 секунд фристайла!\n\n### Чек-лист:\n- [ ] Чистый вход\n- [ ] Минимум 5 разных техник\n- [ ] Смена levels\n- [ ] Музыкальность\n- [ ] Мощный финиш\n\nПокажи всё, что умеешь!"},
      {"type":"battle-sim","title":"Тренировочный баттл — 60 сек","music":MUSIC,"duration":60,"bpm":110},
    ]},
    {"t":"Финальный баттл","xp":50,"steps":[
      {"type":"info","title":"Финальный экзамен","markdown":"## Финальный баттл — 90 секунд!\n\nЭто ваш выпускной экзамен.\n\n### Критерии оценки:\n- **Техника** — чистота хитов, изоляций, волн\n- **Музыкальность** — попадание в бит\n- **Разнообразие** — использование всех техник\n- **Performance** — подача, энергия, характер\n- **Оригинальность** — свой стиль, неожиданные моменты\n\n### 90 секунд. Всё или ничего. Удачи!"},
      {"type":"battle-sim","title":"ФИНАЛЬНЫЙ БАТТЛ — 90 сек","music":MUSIC,"duration":90,"bpm":112},
    ]},
  ]},

  # ==================== Bonus: Баттл-арена ====================
  {"title":"Бонус: Баттл-арена","pos":5,"lessons":[
    {"t":"1 раунд баттл","xp":50,"steps":[
      {"type":"info","title":"Баттл-арена: 1 раунд","markdown":"## Баттл-арена\n\nДобро пожаловать в баттл-арену! Здесь нет обучения — только практика.\n\n**1 раунд — 60 секунд.**\n\nПравила:\n- Любые техники\n- Максимум стиля\n- Попадай в бит\n- Покажи характер"},
      {"type":"battle-sim","title":"Баттл-арена: 1 раунд","music":MUSIC,"duration":60,"bpm":110},
    ]},
    {"t":"3 раунда подряд","xp":50,"steps":[
      {"type":"info","title":"3 раунда подряд!","markdown":"## Ультра-баттл: 3 раунда\n\n**90 секунд непрерывного танца!**\n\nЭто самое сложное испытание курса.\n\n### Стратегия:\n- **0-30 сек**: Разогрев, groove, базовые хиты\n- **30-60 сек**: Основная часть, все техники\n- **60-90 сек**: Финал, максимум энергии, шоу\n\nПоехали!"},
      {"type":"battle-sim","title":"УЛЬТРА-БАТТЛ — 90 сек","music":MUSIC,"duration":90,"bpm":115},
    ]},
  ]},
]

async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping."); return

        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author: print("No users."); return

        course = Course(title=T, slug="popping-beginner-to-pro-"+uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id, category="Dance", difficulty="Beginner",
            price=0, currency="USD", status="published")
        db.add(course); await db.flush()

        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(course_id=course.id, title=sd["title"], position=sd["pos"])
            db.add(sec); await db.flush()
            for li, ld in enumerate(sd["lessons"]):
                les = CourseLesson(section_id=sec.id, title=ld["t"], position=li,
                    content_type="interactive", content_markdown="",
                    xp_reward=ld["xp"], steps=ld["steps"])
                db.add(les); await db.flush()
                r, c = lc // 5, lc % 5
                x, y = SNAKE_X[c]*CANVAS_W, V_PAD+r*ROW_H
                nodes.append({"id":str(les.id),"x":x,"y":y})
                if lc > 0: edges.append({"id":f"e-{lc}","source":nodes[-2]["id"],"target":nodes[-1]["id"]})
                lc += 1; tl += 1
        course.roadmap_nodes = nodes; course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")

if __name__ == "__main__":
    asyncio.run(main())
