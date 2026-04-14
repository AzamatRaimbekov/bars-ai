#!/bin/bash

echo "🚀 Запуск PathMind..."
echo ""

# Backend
echo "⚡ Backend (FastAPI) → http://localhost:3847"
cd backend && source venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 3847 --reload &
BACK_PID=$!
cd ..

# Frontend
echo "⚡ Frontend (Vite)   → http://localhost:3846"
npx vite --port 3846 &
FRONT_PID=$!

echo ""
echo "✅ Оба сервера запущены. Ctrl+C для остановки."
echo ""

# Остановить оба при Ctrl+C
trap "kill $BACK_PID $FRONT_PID 2>/dev/null; echo ''; echo '⏹ Остановлено.'; exit 0" INT TERM

wait
