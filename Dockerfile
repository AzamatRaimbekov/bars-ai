# Stage 1: Build frontend
FROM node:20-slim AS frontend
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --legacy-peer-deps
COPY . .
RUN npm run build

# Stage 2: Python backend + serve frontend
FROM python:3.12-slim
WORKDIR /app

# Install backend deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy built frontend
COPY --from=frontend /app/dist /app/static

ENV PYTHONPATH=/app
EXPOSE 3847
CMD ["sh", "-c", "python create_tables.py && python seed_production.py && python -m seed_claude_code_advanced; python -m seed_claude_code_full; python -m seed_kyrgyz_language; python -m seed_kazakh_language; python -m seed_french_language; python -m seed_chinese_language; python -m seed_popping_course; uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-3847}"]
