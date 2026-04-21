# API Обзор

Бэкенд доступен на порту `3847`. Все эндпоинты начинаются с `/api/`.

## Health Check

```
GET /api/health → { "status": "ok" }
```

## Аутентификация (`/api/auth`)
| Метод | Путь | Описание |
|---|---|---|
| POST | `/api/auth/register` | Регистрация |
| POST | `/api/auth/login` | Логин → access + refresh |
| POST | `/api/auth/refresh` | Обновление access token |

## Пользователи (`/api/users`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/users/me` | Текущий пользователь |
| PATCH | `/api/users/me` | Обновление профиля |

## Курсы (`/api/courses`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/courses` | Список курсов (пагинация) |
| GET | `/api/courses/:id` | Детали курса |
| POST | `/api/courses` | Создание курса |
| PATCH | `/api/courses/:id` | Редактирование |

## Прогресс (`/api/progress`)
| Метод | Путь | Описание |
|---|---|---|
| POST | `/api/progress/complete` | Отметить урок завершённым |
| GET | `/api/progress/course/:id` | Прогресс по курсу |

## AI (`/api/ai`)
| Метод | Путь | Описание |
|---|---|---|
| POST | `/api/ai/generate` | Генерация контента |

## Ментор (`/api/mentor`)
| Метод | Путь | Описание |
|---|---|---|
| POST | `/api/mentor/chat` | Чат с AI-ментором |
| GET | `/api/mentor/history` | История чата |

## Квесты (`/api/quests`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/quests` | Список квестов |
| POST | `/api/quests/complete` | Завершение квеста |

## Лидерборд (`/api/leaderboard`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/leaderboard` | Топ пользователей (Redis) |

## Лиги (`/api/leagues`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/leagues` | Список лиг |

## Спринты (`/api/sprint`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/sprint/current` | Текущий спринт |
| POST | `/api/sprint/trophy` | Получение трофея |

## Оплата (`/api/payments`)
| Метод | Путь | Описание |
|---|---|---|
| POST | `/api/payments/request` | Создать запрос на оплату (скриншот) |
| GET | `/api/payments/my` | Мои запросы на оплату |

## Админ (`/api/admin`)
| Метод | Путь | Описание |
|---|---|---|
| GET | `/api/admin/stats` | Статистика платформы |
| GET | `/api/admin/payments` | Список запросов на оплату |
| POST | `/api/admin/payments/:id/review` | Подтвердить/отклонить оплату |

---

> Автодокументация FastAPI: `http://localhost:3847/docs` (Swagger UI)

См. также: [[Аутентификация]], [[AI Сервисы]]
