---
description: Master index of all wiki pages. LLM reads this first to find relevant pages.
updated: 2026-04-27
---

# Wiki Index

## Architecture
| Page | Summary | Links |
|------|---------|-------|
| [[Обзор системы]] | Tech stack, architecture diagram, system layers | 3 |
| [[Структура проекта]] | Directory tree, routers, modules | 5 |
| [[База данных]] | SQLAlchemy models, migrations, relationships | 4 |

## API
| Page | Summary | Links |
|------|---------|-------|
| [[API Обзор]] | All backend endpoints (12 route groups) | 6 |
| [[Аутентификация]] | JWT flow, refresh tokens, AuthGuard | 3 |
| [[AI Сервисы]] | Claude API, Barsbek mentor, course generation, transcription | 4 |

## Frontend
| Page | Summary | Links |
|------|---------|-------|
| [[Роутинг]] | React Router v7, 20+ routes, AuthGuard | 4 |
| [[Сторы]] | Zustand stores (auth, chat, roadmap, simulator, user) | 3 |
| [[Компоненты]] | UI components, landing, courses, gamification | 5 |
| [[Python Coding]] | Pyodide Web Worker, browser-based Python execution | 2 |
| [[Landing i18n]] | Multi-language landing (RU/EN/KY/UZ), language switcher | 2 |

## Backend
| Page | Summary | Links |
|------|---------|-------|
| [[Модели]] | 10+ SQLAlchemy models (User, Course, Progress, Badge, Sprint) | 4 |
| [[Сервисы]] | Business logic services (auth, ai, courses, progress, quests) | 5 |
| [[Конфигурация]] | Environment variables, Redis, PostgreSQL, Docker | 3 |

## Features
| Page | Summary | Links |
|------|---------|-------|
| [[Геймификация]] | XP, levels, streaks, badges, leagues, daily quests | 4 |
| [[Спринты]] | Competitive sprints with cash prizes, leaderboard | 3 |
| [[Курсы и шаги]] | 15+ step types, course structure, AI generation | 5 |
| [[Онбординг]] | 4-step flow: name, interests, chat, recommendations | 3 |
| [[AI Менторство]] | Barsbek AI assistant, 8 specializations, voice mode | 3 |
| [[Admin Panel]] | Separate admin app, AI course generator, moderation | 3 |

## Guides
| Page | Summary | Links |
|------|---------|-------|
| [[Быстрый старт]] | Local dev setup, install, run | 2 |
| [[Добавление курса]] | Seed scripts, UI course creation | 3 |
| [[Деплой]] | Railway, Docker, nginx, env vars | 4 |

## Deployment
| Page | Summary | Links |
|------|---------|-------|
| [[Production]] | URLs, services, Railway config, .railwayignore | 2 |
