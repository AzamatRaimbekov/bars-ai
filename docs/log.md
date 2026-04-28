---
description: Chronological log of wiki changes. Append-only.
---

# Wiki Log

## [2026-04-27] init | Wiki restructured to LLM Wiki pattern
- Converted existing docs to LLM Wiki pattern with index.md and log.md
- Added feature pages: Геймификация, Спринты, Курсы и шаги, Онбординг, AI Менторство, Admin Panel, Landing i18n, Production
- Updated CLAUDE.md with wiki schema (ingest, query, lint workflows)
- Existing pages preserved and cross-referenced

## [2026-04-27] ingest | Multi-language landing
- Added Landing i18n page documenting 4-language support (RU/EN/KY/UZ)
- Updated Компоненты page with language switcher in LandingNav

## [2026-04-27] ingest | Hero video background
- Updated HeroSection with mascot video as full-screen background
- Fixed .railwayignore to allow PNG/JPG images on production

## [2026-04-27] ingest | Web Speech API for pronunciation
- Replaced OpenAI Whisper with browser Web Speech API
- No API key needed, works in Chrome/Edge/Safari

## [2026-04-27] ingest | AI course generator with file upload
- Added prompt field and file upload (PDF/Word/Excel) to admin AI generator
- Backend extracts text from uploaded files for Claude context

## [2026-04-27] ingest | Currency change KZT to USD
- Replaced all тенге references with dollars across frontend and seeds

## [2026-04-27] fix | Database migrations
- Added missing columns: onboarding_complete, assessment_context, tags
- Backfilled tags for all courses based on category mapping
- Fixed course list 500 error (tags schema allowing None)
