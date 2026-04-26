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

HEALTHCHECK --interval=30s --timeout=10s --start-period=300s --retries=5 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT:-3847}/api/health')" || exit 1

CMD ["sh", "-c", "python create_tables.py && (python seed_all.py &) && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-3847}"]
