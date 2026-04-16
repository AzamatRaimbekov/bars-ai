"""Seed: DevOps — Docker, CI/CD, Cloud — 7 sections, ~40 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "DevOps — Docker, CI/CD, Cloud"
DESC = (
    "Полный курс DevOps: Docker, Docker Compose, GitHub Actions, CI/CD пайплайны, "
    "AWS/GCP основы, Kubernetes intro, мониторинг и логирование."
)

S = [
    # ===== SECTION 1: Введение в DevOps =====
    {
        "title": "Введение в DevOps",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое DevOps",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "DevOps — культура и практики", "markdown": "## Что такое DevOps?\n\n**DevOps** — это набор практик, объединяющих разработку (Dev) и операции (Ops) для ускорения доставки ПО.\n\n### Ключевые принципы:\n1. **Автоматизация** — всё, что можно автоматизировать, нужно автоматизировать\n2. **Непрерывная интеграция** — частые слияния кода\n3. **Непрерывная доставка** — автоматический деплой\n4. **Мониторинг** — наблюдение за системой 24/7\n5. **Обратная связь** — быстрое реагирование на проблемы\n\n### До DevOps:\n```\nРазработчик → Код → Ожидание → QA → Ожидание → Ops → Деплой (недели)\n```\n\n### С DevOps:\n```\nКод → CI/CD → Автотесты → Автодеплой (минуты)\n```"},
                    {"type": "quiz", "question": "Что объединяет DevOps?", "options": [{"id": "a", "text": "Разработку и операции", "correct": True}, {"id": "b", "text": "Дизайн и маркетинг", "correct": False}, {"id": "c", "text": "Frontend и Backend", "correct": False}, {"id": "d", "text": "Тестирование и продажи", "correct": False}]},
                    {"type": "true-false", "statement": "DevOps — это конкретная программа, которую нужно установить на сервер.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "DevOps", "back": "Набор практик, объединяющих разработку и операции"}, {"front": "CI", "back": "Continuous Integration — непрерывная интеграция"}, {"front": "CD", "back": "Continuous Delivery/Deployment — непрерывная доставка"}, {"front": "IaC", "back": "Infrastructure as Code — инфраструктура как код"}]},
                ],
            },
            {
                "t": "Культура DevOps",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Культурные принципы DevOps", "markdown": "## Культура DevOps\n\n### CALMS-фреймворк:\n- **C** — Culture (Культура): совместная ответственность\n- **A** — Automation (Автоматизация): устранение ручной работы\n- **L** — Lean (Бережливость): устранение потерь\n- **M** — Measurement (Измерение): метрики всего\n- **S** — Sharing (Обмен): знания для всех\n\n### Антипаттерны:\n- «Это не моя проблема» — разработчик не знает, как деплоится код\n- «Работает на моей машине» — нет единой среды\n- Ручной деплой — человеческий фактор\n\n### DevOps метрики (DORA):\n1. **Lead Time** — время от коммита до продакшна\n2. **Deployment Frequency** — частота деплоев\n3. **MTTR** — среднее время восстановления\n4. **Change Failure Rate** — процент неудачных релизов"},
                    {"type": "matching", "pairs": [{"left": "C — Culture", "right": "Совместная ответственность команды"}, {"left": "A — Automation", "right": "Устранение ручной работы"}, {"left": "L — Lean", "right": "Устранение потерь и лишних шагов"}, {"left": "M — Measurement", "right": "Метрики и измерение всего"}, {"left": "S — Sharing", "right": "Обмен знаниями между командами"}]},
                    {"type": "quiz", "question": "Что означает MTTR в метриках DORA?", "options": [{"id": "a", "text": "Maximum Time To Release", "correct": False}, {"id": "b", "text": "Mean Time To Recovery", "correct": True}, {"id": "c", "text": "Minimum Test To Run", "correct": False}, {"id": "d", "text": "Main Task To Resolve", "correct": False}]},
                ],
            },
            {
                "t": "CI/CD концепция",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Непрерывная интеграция и доставка", "markdown": "## CI/CD — основа DevOps\n\n### Continuous Integration (CI):\n```\nРазработчик → Push → Автосборка → Автотесты → Отчёт\n```\n- Каждый push запускает сборку\n- Автоматические тесты ловят баги\n- Быстрая обратная связь\n\n### Continuous Delivery (CD):\n```\nCI → Staging → Ручное одобрение → Production\n```\n- Код всегда готов к релизу\n- Деплой одной кнопкой\n\n### Continuous Deployment:\n```\nCI → Staging → Автотесты → Production (автоматически)\n```\n- Полная автоматизация\n- Деплой без вмешательства человека\n\n### Популярные CI/CD инструменты:\n- **GitHub Actions** — встроено в GitHub\n- **GitLab CI** — встроено в GitLab\n- **Jenkins** — open-source, самый гибкий\n- **CircleCI** — облачное решение"},
                    {"type": "drag-order", "items": ["Разработчик делает push в репозиторий", "CI-сервер автоматически собирает проект", "Запускаются автоматические тесты", "Код деплоится на staging-среду", "После проверки деплой на production"]},
                    {"type": "multi-select", "question": "Какие из перечисленных являются CI/CD инструментами?", "options": [{"id": "a", "text": "GitHub Actions", "correct": True}, {"id": "b", "text": "Jenkins", "correct": True}, {"id": "c", "text": "Photoshop", "correct": False}, {"id": "d", "text": "GitLab CI", "correct": True}, {"id": "e", "text": "Microsoft Word", "correct": False}]},
                    {"type": "true-false", "statement": "Continuous Deployment означает автоматический деплой на продакшн без ручного одобрения.", "correct": True},
                ],
            },
            {
                "t": "Обзор инструментов DevOps",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Экосистема DevOps инструментов", "markdown": "## Инструменты DevOps\n\n### Контейнеризация:\n- **Docker** — контейнеры для приложений\n- **Podman** — альтернатива Docker без демона\n\n### Оркестрация:\n- **Kubernetes** — управление контейнерами\n- **Docker Swarm** — встроенная оркестрация Docker\n\n### CI/CD:\n- **GitHub Actions** — GitHub-нативные пайплайны\n- **Jenkins** — самый гибкий CI-сервер\n\n### IaC (Infrastructure as Code):\n- **Terraform** — декларативная инфраструктура\n- **Ansible** — автоматизация конфигурации\n\n### Мониторинг:\n- **Prometheus** — сбор метрик\n- **Grafana** — визуализация\n- **ELK Stack** — логирование\n\n### Облака:\n- **AWS** — Amazon Web Services\n- **GCP** — Google Cloud Platform\n- **Azure** — Microsoft Cloud"},
                    {"type": "matching", "pairs": [{"left": "Docker", "right": "Контейнеризация приложений"}, {"left": "Kubernetes", "right": "Оркестрация контейнеров"}, {"left": "Terraform", "right": "Infrastructure as Code"}, {"left": "Prometheus", "right": "Сбор метрик и мониторинг"}, {"left": "Grafana", "right": "Визуализация метрик и дашборды"}]},
                    {"type": "flashcards", "cards": [{"front": "Docker", "back": "Платформа контейнеризации приложений"}, {"front": "Kubernetes", "back": "Система оркестрации контейнеров (K8s)"}, {"front": "Terraform", "back": "Инструмент IaC от HashiCorp"}, {"front": "Ansible", "back": "Инструмент автоматизации конфигурации"}, {"front": "ELK Stack", "back": "Elasticsearch + Logstash + Kibana — стек логирования"}]},
                ],
            },
            {
                "t": "Linux основы для DevOps",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Linux — фундамент DevOps", "markdown": "## Linux для DevOps-инженера\n\n### Почему Linux?\n- 96% серверов работают на Linux\n- Docker работает нативно на Linux\n- Бесплатный и открытый код\n\n### Основные команды:\n```bash\nls -la          # список файлов\ncd /var/log     # перейти в директорию\ncat file.txt    # просмотр файла\ngrep 'error' log.txt  # поиск в файле\nchmod 755 script.sh   # права доступа\n```\n\n### Работа с процессами:\n```bash\nps aux          # все процессы\ntop             # мониторинг ресурсов\nkill -9 PID     # принудительно завершить\nsystemctl status nginx  # статус сервиса\n```\n\n### Сеть:\n```bash\ncurl http://example.com  # HTTP-запрос\nping google.com          # проверка связи\nnetstat -tlnp            # открытые порты\nss -tlnp                 # современная альтернатива\n```"},
                    {"type": "terminal-sim", "task": "Выведите содержимое директории /var/log с подробной информацией", "expectedCommand": "ls -la /var/log", "hint": "Используйте команду ls с флагами -la и путём /var/log"},
                    {"type": "code-puzzle", "instructions": "Составьте команду для поиска слова 'error' в файле /var/log/syslog:", "correctOrder": ["grep", "'error'", "/var/log/syslog"]},
                    {"type": "fill-blank", "sentence": "Команда ___ используется для просмотра запущенных процессов в реальном времени.", "answer": "top"},
                    {"type": "quiz", "question": "Какой процент серверов в мире работает на Linux?", "options": [{"id": "a", "text": "Около 50%", "correct": False}, {"id": "b", "text": "Около 70%", "correct": False}, {"id": "c", "text": "Около 96%", "correct": True}, {"id": "d", "text": "100%", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 2: Docker =====
    {
        "title": "Docker",
        "pos": 1,
        "lessons": [
            {
                "t": "Контейнеры vs Виртуальные машины",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Контейнеры vs VM", "markdown": "## Контейнеры vs Виртуальные машины\n\n### Виртуальная машина (VM):\n```\n┌─────────────────────┐\n│    Приложение        │\n│    Гостевая ОС       │\n│    Гипервизор        │\n│    Хост ОС           │\n│    Железо             │\n└─────────────────────┘\n```\n- Полная ОС внутри\n- Тяжёлые (ГБ)\n- Медленный старт (минуты)\n\n### Контейнер:\n```\n┌─────────────────────┐\n│    Приложение        │\n│    Docker Engine      │\n│    Хост ОС           │\n│    Железо             │\n└─────────────────────┘\n```\n- Разделяет ядро хоста\n- Лёгкие (МБ)\n- Быстрый старт (секунды)\n\n### Когда что использовать:\n- **Контейнеры** — микросервисы, CI/CD, dev-среды\n- **VM** — разные ОС, полная изоляция, legacy"},
                    {"type": "quiz", "question": "Какое преимущество контейнеров перед VM?", "options": [{"id": "a", "text": "Полная ОС внутри каждого контейнера", "correct": False}, {"id": "b", "text": "Быстрый запуск и малый размер", "correct": True}, {"id": "c", "text": "Лучшая изоляция от хостовой системы", "correct": False}, {"id": "d", "text": "Не требуют Docker Engine", "correct": False}]},
                    {"type": "true-false", "statement": "Контейнеры содержат полную гостевую операционную систему, как и виртуальные машины.", "correct": False},
                    {"type": "matching", "pairs": [{"left": "Контейнер", "right": "Лёгкий, старт за секунды, размер в МБ"}, {"left": "VM", "right": "Полная ОС, старт за минуты, размер в ГБ"}, {"left": "Docker Engine", "right": "Среда выполнения контейнеров"}, {"left": "Гипервизор", "right": "Управление виртуальными машинами"}]},
                ],
            },
            {
                "t": "Dockerfile",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Dockerfile — рецепт образа", "markdown": "## Dockerfile\n\nDockerfile — это текстовый файл с инструкциями для создания Docker-образа.\n\n### Основные инструкции:\n```dockerfile\n# Базовый образ\nFROM python:3.11-slim\n\n# Рабочая директория\nWORKDIR /app\n\n# Копировать файлы\nCOPY requirements.txt .\n\n# Выполнить команду\nRUN pip install -r requirements.txt\n\n# Копировать код\nCOPY . .\n\n# Открыть порт\nEXPOSE 8000\n\n# Команда запуска\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\"]\n```\n\n### Инструкции:\n| Инструкция | Описание |\n|-----------|----------|\n| FROM | Базовый образ |\n| WORKDIR | Рабочая директория |\n| COPY | Копировать файлы |\n| RUN | Выполнить при сборке |\n| EXPOSE | Открыть порт |\n| CMD | Команда запуска |\n| ENV | Переменная окружения |"},
                    {"type": "code-puzzle", "instructions": "Составьте правильный Dockerfile для Python-приложения:", "correctOrder": ["FROM python:3.11-slim", "WORKDIR /app", "COPY requirements.txt .", "RUN pip install -r requirements.txt", "COPY . .", "CMD [\"uvicorn\", \"main:app\"]"]},
                    {"type": "fill-blank", "sentence": "Инструкция ___ в Dockerfile указывает базовый образ.", "answer": "FROM"},
                    {"type": "type-answer", "question": "Какая инструкция Dockerfile задаёт команду, выполняемую при запуске контейнера?", "acceptedAnswers": ["CMD", "cmd"]},
                ],
            },
            {
                "t": "Docker образы и контейнеры",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Работа с образами и контейнерами", "markdown": "## Образы и контейнеры\n\n### Образ (Image):\n- Шаблон для создания контейнера\n- Неизменяемый (read-only)\n- Хранится в реестре (Docker Hub)\n\n### Контейнер (Container):\n- Запущенный экземпляр образа\n- Имеет своё состояние\n- Можно остановить, удалить, перезапустить\n\n### Основные команды:\n```bash\n# Работа с образами\ndocker build -t myapp .         # собрать образ\ndocker images                   # список образов\ndocker pull nginx               # скачать образ\ndocker push myrepo/myapp:v1     # загрузить в реестр\n\n# Работа с контейнерами\ndocker run -d -p 8080:80 nginx  # запустить\ndocker ps                       # запущенные контейнеры\ndocker stop <id>                # остановить\ndocker rm <id>                  # удалить\ndocker logs <id>                # логи\ndocker exec -it <id> bash       # зайти внутрь\n```"},
                    {"type": "terminal-sim", "task": "Соберите Docker-образ с тегом myapp из текущей директории", "expectedCommand": "docker build -t myapp .", "hint": "Используйте docker build с флагом -t для тега"},
                    {"type": "drag-order", "items": ["Написать Dockerfile", "Собрать образ (docker build)", "Запустить контейнер (docker run)", "Проверить логи (docker logs)", "Остановить контейнер (docker stop)"]},
                    {"type": "quiz", "question": "Какой командой можно зайти внутрь работающего контейнера?", "options": [{"id": "a", "text": "docker login", "correct": False}, {"id": "b", "text": "docker exec -it <id> bash", "correct": True}, {"id": "c", "text": "docker inspect <id>", "correct": False}, {"id": "d", "text": "docker attach <id>", "correct": False}]},
                ],
            },
            {
                "t": "Docker Volumes",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Тома — хранение данных", "markdown": "## Docker Volumes\n\nПо умолчанию данные контейнера теряются при удалении. Volumes решают эту проблему.\n\n### Типы хранения:\n1. **Volume** — управляется Docker\n2. **Bind mount** — привязка к папке хоста\n3. **tmpfs** — в оперативной памяти\n\n### Команды:\n```bash\n# Создать том\ndocker volume create mydata\n\n# Запустить с томом\ndocker run -v mydata:/app/data nginx\n\n# Bind mount\ndocker run -v $(pwd):/app nginx\n\n# Список томов\ndocker volume ls\n\n# Удалить том\ndocker volume rm mydata\n```\n\n### Когда использовать:\n- **Volume** — БД, данные приложения\n- **Bind mount** — разработка, hot reload\n- **tmpfs** — секреты, кэш"},
                    {"type": "matching", "pairs": [{"left": "Volume", "right": "Управляется Docker, для данных приложения"}, {"left": "Bind mount", "right": "Привязка к папке хоста, для разработки"}, {"left": "tmpfs", "right": "В оперативной памяти, для секретов"}]},
                    {"type": "terminal-sim", "task": "Создайте Docker-том с именем pgdata", "expectedCommand": "docker volume create pgdata", "hint": "Используйте docker volume create с именем тома"},
                    {"type": "true-false", "statement": "По умолчанию данные внутри Docker-контейнера сохраняются после его удаления.", "correct": False},
                ],
            },
            {
                "t": "Docker Networking",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Сеть в Docker", "markdown": "## Docker Networking\n\n### Типы сетей:\n- **bridge** — по умолчанию, изолированная сеть\n- **host** — контейнер использует сеть хоста\n- **none** — без сети\n- **overlay** — для Docker Swarm\n\n### Команды:\n```bash\n# Создать сеть\ndocker network create mynet\n\n# Запустить в сети\ndocker run --network mynet --name web nginx\ndocker run --network mynet --name api myapp\n\n# Из api можно обращаться к web по имени:\n# curl http://web:80\n\n# Проброс портов\ndocker run -p 8080:80 nginx\n# Хост:8080 → Контейнер:80\n\n# Список сетей\ndocker network ls\n```\n\n### DNS в Docker:\nКонтейнеры в одной сети обращаются друг к другу **по имени контейнера** — Docker автоматически резолвит DNS."},
                    {"type": "quiz", "question": "Какой тип сети Docker используется по умолчанию?", "options": [{"id": "a", "text": "host", "correct": False}, {"id": "b", "text": "bridge", "correct": True}, {"id": "c", "text": "overlay", "correct": False}, {"id": "d", "text": "none", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Флаг -p 8080:80 означает проброс с порта 8080 ___ на порт 80 контейнера.", "answer": "хоста"},
                    {"type": "true-false", "statement": "Контейнеры в одной Docker-сети могут обращаться друг к другу по имени контейнера.", "correct": True},
                ],
            },
            {
                "t": "Docker Compose",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Docker Compose — мультиконтейнерные приложения", "markdown": "## Docker Compose\n\nDocker Compose позволяет описывать и запускать несколько контейнеров одной командой.\n\n### docker-compose.yml:\n```yaml\nversion: '3.8'\nservices:\n  web:\n    build: .\n    ports:\n      - '8000:8000'\n    depends_on:\n      - db\n    environment:\n      - DATABASE_URL=postgresql://user:pass@db:5432/mydb\n\n  db:\n    image: postgres:15\n    volumes:\n      - pgdata:/var/lib/postgresql/data\n    environment:\n      - POSTGRES_PASSWORD=pass\n\n  redis:\n    image: redis:7-alpine\n    ports:\n      - '6379:6379'\n\nvolumes:\n  pgdata:\n```\n\n### Команды:\n```bash\ndocker compose up -d        # запустить всё\ndocker compose down          # остановить всё\ndocker compose logs -f       # логи в реальном времени\ndocker compose ps            # статус сервисов\ndocker compose build         # пересобрать образы\n```"},
                    {"type": "code-puzzle", "instructions": "Составьте команды для работы с Docker Compose:", "correctOrder": ["docker compose build", "docker compose up -d", "docker compose ps", "docker compose logs -f", "docker compose down"]},
                    {"type": "terminal-sim", "task": "Запустите все сервисы Docker Compose в фоновом режиме", "expectedCommand": "docker compose up -d", "hint": "Используйте docker compose up с флагом -d для detached mode"},
                    {"type": "quiz", "question": "Для чего нужен ключ depends_on в docker-compose.yml?", "options": [{"id": "a", "text": "Указывает зависимость — сервис запустится после зависимости", "correct": True}, {"id": "b", "text": "Удаляет сервис при остановке", "correct": False}, {"id": "c", "text": "Ограничивает CPU контейнера", "correct": False}, {"id": "d", "text": "Задаёт DNS-имя контейнера", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Файл ___ описывает мультиконтейнерное приложение в Docker Compose.", "answer": "docker-compose.yml"},
                ],
            },
        ],
    },
    # ===== SECTION 3: CI/CD =====
    {
        "title": "CI/CD",
        "pos": 2,
        "lessons": [
            {
                "t": "GitHub Actions основы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "GitHub Actions — CI/CD от GitHub", "markdown": "## GitHub Actions\n\nGitHub Actions — это встроенная система CI/CD в GitHub.\n\n### Ключевые понятия:\n- **Workflow** — автоматизированный процесс\n- **Job** — набор шагов, выполняемых на одном раннере\n- **Step** — отдельное действие\n- **Action** — переиспользуемый блок\n- **Runner** — сервер, который выполняет workflow\n\n### Структура:\n```\n.github/\n  workflows/\n    ci.yml      ← workflow файл\n    deploy.yml  ← ещё один workflow\n```\n\n### Триггеры:\n```yaml\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\n  schedule:\n    - cron: '0 0 * * *'  # каждый день\n```\n\n### Раннеры:\n- `ubuntu-latest` — Linux\n- `macos-latest` — macOS\n- `windows-latest` — Windows"},
                    {"type": "flashcards", "cards": [{"front": "Workflow", "back": "Автоматизированный процесс, описанный в YAML-файле"}, {"front": "Job", "back": "Набор шагов, выполняемых на одном раннере"}, {"front": "Step", "back": "Отдельное действие внутри Job"}, {"front": "Action", "back": "Переиспользуемый блок автоматизации"}, {"front": "Runner", "back": "Сервер, который выполняет workflow"}]},
                    {"type": "quiz", "question": "Где хранятся файлы workflow в GitHub Actions?", "options": [{"id": "a", "text": ".github/workflows/", "correct": True}, {"id": "b", "text": ".ci/pipelines/", "correct": False}, {"id": "c", "text": "ci-config/", "correct": False}, {"id": "d", "text": ".actions/", "correct": False}]},
                    {"type": "fill-blank", "sentence": "GitHub Actions workflow файлы пишутся в формате ___.", "answer": "YAML"},
                ],
            },
            {
                "t": "Workflow файлы",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Пишем workflow", "markdown": "## Workflow YAML-файл\n\n### Минимальный пример:\n```yaml\nname: CI\n\non:\n  push:\n    branches: [main]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - name: Setup Python\n        uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n\n      - name: Install dependencies\n        run: pip install -r requirements.txt\n\n      - name: Run tests\n        run: pytest\n```\n\n### Ключевые элементы:\n- `name:` — имя workflow\n- `on:` — когда запускать\n- `jobs:` — список задач\n- `runs-on:` — на чём запускать\n- `steps:` — шаги задачи\n- `uses:` — использовать action\n- `run:` — выполнить команду"},
                    {"type": "code-puzzle", "instructions": "Составьте структуру GitHub Actions workflow:", "correctOrder": ["name: CI", "on:", "  push:", "    branches: [main]", "jobs:", "  test:", "    runs-on: ubuntu-latest", "    steps:", "      - uses: actions/checkout@v4", "      - run: npm test"]},
                    {"type": "type-answer", "question": "Какой ключ в workflow файле указывает, на каком раннере выполнять job?", "acceptedAnswers": ["runs-on", "runs-on:"]},
                    {"type": "matching", "pairs": [{"left": "uses:", "right": "Использовать готовый action"}, {"left": "run:", "right": "Выполнить bash-команду"}, {"left": "with:", "right": "Передать параметры в action"}, {"left": "on:", "right": "Триггер запуска workflow"}]},
                ],
            },
            {
                "t": "Тесты в CI",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Автоматические тесты в CI", "markdown": "## Тесты в CI-пайплайне\n\n### Зачем тесты в CI?\n- Ловят баги до мёржа в main\n- Гарантируют стабильность кода\n- Автоматическая проверка каждого PR\n\n### Пример с Python (pytest):\n```yaml\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - run: pip install -r requirements.txt\n      - run: pytest --cov=app tests/\n```\n\n### Пример с Node.js:\n```yaml\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-node@v4\n        with:\n          node-version: '20'\n      - run: npm ci\n      - run: npm test\n```\n\n### Матрица тестов:\n```yaml\nstrategy:\n  matrix:\n    python-version: ['3.10', '3.11', '3.12']\n    os: [ubuntu-latest, macos-latest]\n```\nЗапустит тесты на всех комбинациях!"},
                    {"type": "quiz", "question": "Что делает стратегия matrix в GitHub Actions?", "options": [{"id": "a", "text": "Запускает тесты на всех комбинациях параметров", "correct": True}, {"id": "b", "text": "Шифрует переменные окружения", "correct": False}, {"id": "c", "text": "Создаёт Docker-контейнер", "correct": False}, {"id": "d", "text": "Кэширует зависимости", "correct": False}]},
                    {"type": "true-false", "statement": "Матрица стратегий позволяет запускать тесты параллельно на разных версиях языка.", "correct": True},
                    {"type": "drag-order", "items": ["Checkout кода из репозитория", "Установка нужной версии языка", "Установка зависимостей", "Запуск тестов", "Генерация отчёта о покрытии"]},
                ],
            },
            {
                "t": "Деплой через CI/CD",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Автоматический деплой", "markdown": "## Деплой через CI/CD\n\n### Пример деплоя на сервер:\n```yaml\njobs:\n  deploy:\n    runs-on: ubuntu-latest\n    needs: test   # сначала тесты!\n    if: github.ref == 'refs/heads/main'\n    steps:\n      - uses: actions/checkout@v4\n\n      - name: Deploy via SSH\n        uses: appleboy/ssh-action@v1\n        with:\n          host: ${{ secrets.SERVER_HOST }}\n          username: ${{ secrets.SERVER_USER }}\n          key: ${{ secrets.SSH_KEY }}\n          script: |\n            cd /app\n            git pull\n            docker compose up -d --build\n```\n\n### Деплой Docker-образа:\n```yaml\n      - name: Login to Docker Hub\n        uses: docker/login-action@v3\n        with:\n          username: ${{ secrets.DOCKER_USER }}\n          password: ${{ secrets.DOCKER_TOKEN }}\n\n      - name: Build and push\n        uses: docker/build-push-action@v5\n        with:\n          push: true\n          tags: user/app:latest\n```\n\n### Ключевые правила:\n- Деплой **только после** успешных тестов (`needs: test`)\n- Деплой **только из main** (`if: github.ref == 'refs/heads/main'`)"},
                    {"type": "multi-select", "question": "Какие практики важны при настройке деплоя в CI/CD?", "options": [{"id": "a", "text": "Деплой только после успешных тестов", "correct": True}, {"id": "b", "text": "Использование секретов для credentials", "correct": True}, {"id": "c", "text": "Хранение паролей в коде", "correct": False}, {"id": "d", "text": "Деплой только из main ветки", "correct": True}, {"id": "e", "text": "Ручной ввод пароля при каждом деплое", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Ключ needs: test в job означает, что деплой запустится только после успешного выполнения job ___.", "answer": "test"},
                    {"type": "true-false", "statement": "Ключевое слово needs в GitHub Actions указывает зависимость одного job от другого.", "correct": True},
                ],
            },
            {
                "t": "Secrets и переменные",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Секреты в CI/CD", "markdown": "## Secrets и переменные окружения\n\n### Зачем секреты?\n- Пароли, API-ключи, SSH-ключи **нельзя** хранить в коде\n- GitHub Secrets хранит их зашифрованно\n- Доступны через `${{ secrets.NAME }}`\n\n### Добавление секрета:\n```\nSettings → Secrets and variables → Actions → New repository secret\n```\n\n### Использование в workflow:\n```yaml\nenv:\n  DATABASE_URL: ${{ secrets.DATABASE_URL }}\n  API_KEY: ${{ secrets.API_KEY }}\n\nsteps:\n  - name: Deploy\n    run: echo \"Deploying to ${{ secrets.SERVER_HOST }}\"\n```\n\n### Переменные (Variables):\n```yaml\n# Не секретные значения\nenv:\n  APP_ENV: production\n  NODE_ENV: production\n\n# Или через GitHub Variables\n${{ vars.APP_NAME }}\n```\n\n### Правила безопасности:\n- Никогда не выводите секреты в логи\n- Используйте минимальные права\n- Ротируйте секреты регулярно"},
                    {"type": "quiz", "question": "Как обратиться к секрету SERVER_HOST в GitHub Actions?", "options": [{"id": "a", "text": "$SERVER_HOST", "correct": False}, {"id": "b", "text": "${{ secrets.SERVER_HOST }}", "correct": True}, {"id": "c", "text": "process.env.SERVER_HOST", "correct": False}, {"id": "d", "text": "%SERVER_HOST%", "correct": False}]},
                    {"type": "true-false", "statement": "GitHub Secrets можно просматривать после создания через интерфейс GitHub.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "GitHub Secrets", "back": "Зашифрованные переменные для хранения паролей и ключей"}, {"front": "GitHub Variables", "back": "Незашифрованные переменные для несекретных значений"}, {"front": "${{ secrets.NAME }}", "back": "Синтаксис доступа к секрету в workflow"}]},
                ],
            },
            {
                "t": "Артефакты и кэширование",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Артефакты и кэш", "markdown": "## Артефакты и кэширование\n\n### Артефакты (Artifacts):\nФайлы, сохраняемые после выполнения workflow.\n\n```yaml\n- name: Upload test results\n  uses: actions/upload-artifact@v4\n  with:\n    name: test-results\n    path: test-results/\n\n- name: Download artifact\n  uses: actions/download-artifact@v4\n  with:\n    name: test-results\n```\n\n### Кэширование зависимостей:\n```yaml\n- name: Cache pip\n  uses: actions/cache@v4\n  with:\n    path: ~/.cache/pip\n    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}\n    restore-keys: |\n      ${{ runner.os }}-pip-\n```\n\n### Зачем кэш?\n- Ускоряет CI/CD в 2-5 раз\n- Не скачивает зависимости заново\n- Автоматически инвалидируется при изменении lock-файла\n\n### Кэш Node.js:\n```yaml\n- uses: actions/setup-node@v4\n  with:\n    node-version: '20'\n    cache: 'npm'   # встроенный кэш!\n```"},
                    {"type": "matching", "pairs": [{"left": "Artifacts", "right": "Сохранение файлов после workflow"}, {"left": "Cache", "right": "Ускорение сборки через кэш зависимостей"}, {"left": "upload-artifact", "right": "Action для загрузки артефактов"}, {"left": "hashFiles()", "right": "Генерация ключа кэша на основе файла"}]},
                    {"type": "quiz", "question": "Зачем нужно кэширование в CI/CD?", "options": [{"id": "a", "text": "Ускорение сборки — не скачивать зависимости заново", "correct": True}, {"id": "b", "text": "Шифрование секретов", "correct": False}, {"id": "c", "text": "Создание бэкапов кода", "correct": False}, {"id": "d", "text": "Отправка уведомлений", "correct": False}]},
                    {"type": "true-false", "statement": "Кэш в GitHub Actions автоматически инвалидируется при изменении lock-файла зависимостей.", "correct": True},
                ],
            },
        ],
    },
    # ===== SECTION 4: Облачные платформы =====
    {
        "title": "Облачные платформы",
        "pos": 3,
        "lessons": [
            {
                "t": "AWS основы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Amazon Web Services", "markdown": "## AWS — Amazon Web Services\n\n### Что такое AWS?\n- Крупнейший облачный провайдер (33% рынка)\n- 200+ сервисов\n- Регионы по всему миру\n\n### Ключевые сервисы:\n- **EC2** — виртуальные серверы\n- **S3** — хранилище файлов\n- **RDS** — управляемые базы данных\n- **Lambda** — serverless функции\n- **ECS/EKS** — контейнеры\n- **CloudFront** — CDN\n- **Route 53** — DNS\n\n### Модели оплаты:\n- **On-Demand** — платите за использование\n- **Reserved** — скидки за обязательства (1-3 года)\n- **Spot** — до 90% скидки, но могут забрать\n\n### Free Tier:\n- 12 месяцев бесплатного использования\n- EC2 t2.micro — 750 часов/месяц\n- S3 — 5 ГБ\n- RDS — 750 часов/месяц"},
                    {"type": "flashcards", "cards": [{"front": "EC2", "back": "Elastic Compute Cloud — виртуальные серверы"}, {"front": "S3", "back": "Simple Storage Service — объектное хранилище"}, {"front": "RDS", "back": "Relational Database Service — управляемые БД"}, {"front": "Lambda", "back": "Serverless — выполнение функций без серверов"}, {"front": "CloudFront", "back": "CDN — сеть доставки контента"}]},
                    {"type": "quiz", "question": "Какую долю рынка облачных сервисов занимает AWS?", "options": [{"id": "a", "text": "Около 10%", "correct": False}, {"id": "b", "text": "Около 33%", "correct": True}, {"id": "c", "text": "Около 60%", "correct": False}, {"id": "d", "text": "Около 90%", "correct": False}]},
                    {"type": "multi-select", "question": "Какие сервисы входят в AWS?", "options": [{"id": "a", "text": "EC2", "correct": True}, {"id": "b", "text": "S3", "correct": True}, {"id": "c", "text": "BigQuery", "correct": False}, {"id": "d", "text": "Lambda", "correct": True}, {"id": "e", "text": "Azure Functions", "correct": False}]},
                ],
            },
            {
                "t": "EC2 — виртуальные серверы",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "EC2 — сердце AWS", "markdown": "## EC2 — Elastic Compute Cloud\n\n### Что такое EC2?\nВиртуальные серверы в облаке AWS. Вы выбираете конфигурацию и платите по часам.\n\n### Типы инстансов:\n| Тип | Назначение |\n|-----|------------|\n| t2/t3 | Общего назначения, бюджетные |\n| m5/m6 | Сбалансированные |\n| c5/c6 | Вычислительные |\n| r5/r6 | Оптимизированные по памяти |\n| g4/p4 | GPU, ML/AI |\n\n### Запуск через CLI:\n```bash\naws ec2 run-instances \\\n  --image-id ami-0abcdef1234567890 \\\n  --instance-type t3.micro \\\n  --key-name mykey \\\n  --security-group-ids sg-12345\n```\n\n### Security Groups:\n- Встроенный файрвол\n- Правила входящего/исходящего трафика\n- По умолчанию: весь исходящий разрешён, входящий заблокирован\n\n### SSH подключение:\n```bash\nssh -i mykey.pem ec2-user@<public-ip>\n```"},
                    {"type": "matching", "pairs": [{"left": "t2/t3", "right": "Общего назначения, бюджетные"}, {"left": "c5/c6", "right": "Вычислительные (CPU-intensive)"}, {"left": "r5/r6", "right": "Оптимизированные по памяти"}, {"left": "g4/p4", "right": "GPU для ML/AI задач"}]},
                    {"type": "terminal-sim", "task": "Подключитесь к EC2-инстансу по SSH с ключом mykey.pem", "expectedCommand": "ssh -i mykey.pem ec2-user@<public-ip>", "hint": "Используйте ssh с флагом -i для указания ключа"},
                    {"type": "true-false", "statement": "Security Groups в EC2 по умолчанию разрешают весь входящий трафик.", "correct": False},
                ],
            },
            {
                "t": "S3 — хранилище",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "S3 — Simple Storage Service", "markdown": "## S3 — объектное хранилище\n\n### Ключевые концепции:\n- **Bucket** — контейнер для файлов\n- **Object** — файл + метаданные\n- **Key** — путь к объекту\n\n### Классы хранения:\n| Класс | Назначение | Стоимость |\n|-------|-----------|----------|\n| Standard | Частый доступ | $$$ |\n| IA | Редкий доступ | $$ |\n| Glacier | Архив | $ |\n| Deep Archive | Долгий архив | ¢ |\n\n### CLI-команды:\n```bash\n# Создать бакет\naws s3 mb s3://my-bucket\n\n# Загрузить файл\naws s3 cp file.txt s3://my-bucket/\n\n# Скачать файл\naws s3 cp s3://my-bucket/file.txt ./\n\n# Синхронизация папки\naws s3 sync ./dist s3://my-bucket/\n\n# Список файлов\naws s3 ls s3://my-bucket/\n```\n\n### Использование:\n- Хостинг статических сайтов\n- Хранение бэкапов\n- Хранение медиа-файлов\n- Data lake"},
                    {"type": "drag-order", "items": ["Создать S3 bucket (aws s3 mb)", "Загрузить файлы (aws s3 cp)", "Настроить права доступа", "Включить версионирование", "Настроить жизненный цикл объектов"]},
                    {"type": "quiz", "question": "Какой класс хранения S3 самый дешёвый для долгого архива?", "options": [{"id": "a", "text": "Standard", "correct": False}, {"id": "b", "text": "IA (Infrequent Access)", "correct": False}, {"id": "c", "text": "Glacier", "correct": False}, {"id": "d", "text": "Deep Archive", "correct": True}]},
                    {"type": "fill-blank", "sentence": "В S3 файлы хранятся в контейнерах, которые называются ___.", "answer": "bucket"},
                ],
            },
            {
                "t": "RDS — управляемые базы данных",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "RDS — базы данных в облаке", "markdown": "## RDS — Relational Database Service\n\n### Зачем RDS?\n- Автоматические бэкапы\n- Обновления и патчи\n- Multi-AZ для высокой доступности\n- Масштабирование одним кликом\n\n### Поддерживаемые движки:\n- **PostgreSQL** — самый популярный\n- **MySQL** — классика\n- **MariaDB** — форк MySQL\n- **Oracle** — enterprise\n- **SQL Server** — Microsoft\n- **Aurora** — облачный PostgreSQL/MySQL от AWS (5x быстрее)\n\n### Создание через CLI:\n```bash\naws rds create-db-instance \\\n  --db-instance-identifier mydb \\\n  --engine postgres \\\n  --db-instance-class db.t3.micro \\\n  --master-username admin \\\n  --master-user-password secret123 \\\n  --allocated-storage 20\n```\n\n### Multi-AZ:\n- Автоматический failover\n- Реплика в другой зоне доступности\n- Downtime < 60 секунд"},
                    {"type": "quiz", "question": "Что обеспечивает Multi-AZ в RDS?", "options": [{"id": "a", "text": "Высокую доступность через реплику в другой зоне", "correct": True}, {"id": "b", "text": "Бесплатное хранилище", "correct": False}, {"id": "c", "text": "Автоматическое шифрование данных", "correct": False}, {"id": "d", "text": "Ускорение запросов в 10 раз", "correct": False}]},
                    {"type": "multi-select", "question": "Какие движки баз данных поддерживает AWS RDS?", "options": [{"id": "a", "text": "PostgreSQL", "correct": True}, {"id": "b", "text": "MySQL", "correct": True}, {"id": "c", "text": "MongoDB", "correct": False}, {"id": "d", "text": "Aurora", "correct": True}, {"id": "e", "text": "Redis", "correct": False}]},
                    {"type": "true-false", "statement": "Amazon Aurora — это облачная БД, которая до 5 раз быстрее стандартного PostgreSQL.", "correct": True},
                ],
            },
            {
                "t": "GCP обзор",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Google Cloud Platform", "markdown": "## GCP — Google Cloud Platform\n\n### Ключевые сервисы GCP:\n| AWS | GCP | Назначение |\n|-----|-----|------------|\n| EC2 | Compute Engine | Виртуальные серверы |\n| S3 | Cloud Storage | Объектное хранилище |\n| RDS | Cloud SQL | Управляемые БД |\n| Lambda | Cloud Functions | Serverless |\n| EKS | GKE | Kubernetes |\n| CloudFront | Cloud CDN | CDN |\n\n### Преимущества GCP:\n- **BigQuery** — лучший сервис для аналитики\n- **GKE** — лучший managed Kubernetes\n- **Cloud AI/ML** — TensorFlow, Vertex AI\n- Агрессивные цены, автоскидки\n\n### gcloud CLI:\n```bash\n# Инициализация\ngcloud init\n\n# Создать VM\ngcloud compute instances create myvm \\\n  --zone=us-central1-a \\\n  --machine-type=e2-micro\n\n# Список инстансов\ngcloud compute instances list\n```"},
                    {"type": "matching", "pairs": [{"left": "Compute Engine", "right": "Аналог EC2 — виртуальные серверы"}, {"left": "Cloud Storage", "right": "Аналог S3 — объектное хранилище"}, {"left": "GKE", "right": "Managed Kubernetes от Google"}, {"left": "BigQuery", "right": "Сервис аналитики больших данных"}]},
                    {"type": "quiz", "question": "Какой сервис GCP считается лучшим для аналитики больших данных?", "options": [{"id": "a", "text": "Cloud SQL", "correct": False}, {"id": "b", "text": "BigQuery", "correct": True}, {"id": "c", "text": "Compute Engine", "correct": False}, {"id": "d", "text": "Cloud Functions", "correct": False}]},
                ],
            },
            {
                "t": "Infrastructure as Code",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "IaC — инфраструктура как код", "markdown": "## Infrastructure as Code (IaC)\n\n### Зачем IaC?\n- **Воспроизводимость** — одинаковая среда везде\n- **Версионирование** — инфраструктура в Git\n- **Автоматизация** — нет ручных действий\n- **Документация** — код = документация\n\n### Подходы:\n\n**Декларативный** (что нужно получить):\n```hcl\n# Terraform\nresource \"aws_instance\" \"web\" {\n  ami           = \"ami-0abcdef\"\n  instance_type = \"t3.micro\"\n  tags = {\n    Name = \"web-server\"\n  }\n}\n```\n\n**Императивный** (как сделать):\n```yaml\n# Ansible\n- name: Install nginx\n  apt:\n    name: nginx\n    state: present\n- name: Start nginx\n  service:\n    name: nginx\n    state: started\n```\n\n### Инструменты:\n| Инструмент | Тип | Назначение |\n|-----------|-----|------------|\n| Terraform | Декларативный | Создание инфраструктуры |\n| Ansible | Императивный | Конфигурация серверов |\n| Pulumi | Декларативный | IaC на Python/TS/Go |\n| CloudFormation | Декларативный | IaC для AWS |"},
                    {"type": "matching", "pairs": [{"left": "Terraform", "right": "Декларативное создание инфраструктуры"}, {"left": "Ansible", "right": "Императивная конфигурация серверов"}, {"left": "CloudFormation", "right": "IaC нативный для AWS"}, {"left": "Pulumi", "right": "IaC на языках программирования"}]},
                    {"type": "quiz", "question": "Какой подход описывает ЧТО нужно, а не КАК?", "options": [{"id": "a", "text": "Императивный", "correct": False}, {"id": "b", "text": "Декларативный", "correct": True}, {"id": "c", "text": "Процедурный", "correct": False}, {"id": "d", "text": "Функциональный", "correct": False}]},
                    {"type": "true-false", "statement": "Infrastructure as Code позволяет хранить описание инфраструктуры в Git и версионировать его.", "correct": True},
                    {"type": "fill-blank", "sentence": "Terraform использует ___ подход к описанию инфраструктуры.", "answer": "декларативный"},
                ],
            },
        ],
    },
    # ===== SECTION 5: Kubernetes intro =====
    {
        "title": "Kubernetes intro",
        "pos": 4,
        "lessons": [
            {
                "t": "Что такое Kubernetes",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Kubernetes — оркестрация контейнеров", "markdown": "## Kubernetes (K8s)\n\n### Зачем нужен Kubernetes?\nКогда у вас 100+ контейнеров, нужен оркестратор.\n\n### Что умеет K8s:\n- **Автомасштабирование** — больше нагрузки → больше подов\n- **Self-healing** — упал контейнер → автоперезапуск\n- **Load balancing** — распределение трафика\n- **Rolling updates** — обновление без простоя\n- **Service discovery** — контейнеры находят друг друга\n\n### Архитектура:\n```\n┌─── Control Plane ───┐\n│ API Server           │\n│ Scheduler            │\n│ Controller Manager   │\n│ etcd (хранилище)     │\n└─────────────────────┘\n        ↓\n┌─── Worker Node ─────┐\n│ kubelet              │\n│ kube-proxy           │\n│ Container Runtime    │\n│ [Pod] [Pod] [Pod]    │\n└─────────────────────┘\n```\n\n### K8s vs Docker Compose:\n- Docker Compose — один сервер, разработка\n- Kubernetes — кластер серверов, продакшн"},
                    {"type": "flashcards", "cards": [{"front": "Pod", "back": "Минимальная единица деплоя в K8s (один или несколько контейнеров)"}, {"front": "Node", "back": "Рабочий сервер в кластере Kubernetes"}, {"front": "Control Plane", "back": "Управляющие компоненты кластера K8s"}, {"front": "etcd", "back": "Распределённое хранилище состояния кластера"}, {"front": "kubelet", "back": "Агент на каждом Node, управляющий подами"}]},
                    {"type": "quiz", "question": "Что происходит, если контейнер падает в Kubernetes?", "options": [{"id": "a", "text": "Кластер останавливается", "correct": False}, {"id": "b", "text": "K8s автоматически перезапускает контейнер", "correct": True}, {"id": "c", "text": "Нужно вручную перезапустить", "correct": False}, {"id": "d", "text": "Контейнер удаляется навсегда", "correct": False}]},
                    {"type": "true-false", "statement": "Kubernetes подходит только для больших компаний с тысячами серверов.", "correct": False},
                ],
            },
            {
                "t": "Pods и Services",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Pods и Services", "markdown": "## Pods\n\n**Pod** — минимальная единица деплоя в K8s.\n\n```yaml\napiVersion: v1\nkind: Pod\nmetadata:\n  name: myapp\nspec:\n  containers:\n    - name: web\n      image: nginx:latest\n      ports:\n        - containerPort: 80\n```\n\n## Services\n\n**Service** — стабильный способ обращения к Pods.\n\n```yaml\napiVersion: v1\nkind: Service\nmetadata:\n  name: web-service\nspec:\n  selector:\n    app: web\n  ports:\n    - port: 80\n      targetPort: 8080\n  type: ClusterIP\n```\n\n### Типы сервисов:\n- **ClusterIP** — внутренний доступ (по умолчанию)\n- **NodePort** — доступ через порт ноды (30000-32767)\n- **LoadBalancer** — внешний балансировщик\n- **Ingress** — маршрутизация HTTP/HTTPS"},
                    {"type": "matching", "pairs": [{"left": "ClusterIP", "right": "Внутренний доступ внутри кластера"}, {"left": "NodePort", "right": "Доступ через порт на каждом узле"}, {"left": "LoadBalancer", "right": "Внешний облачный балансировщик"}, {"left": "Ingress", "right": "HTTP/HTTPS маршрутизация"}]},
                    {"type": "fill-blank", "sentence": "___ — это минимальная единица деплоя в Kubernetes.", "answer": "Pod"},
                    {"type": "quiz", "question": "Какой тип Service используется в K8s по умолчанию?", "options": [{"id": "a", "text": "NodePort", "correct": False}, {"id": "b", "text": "LoadBalancer", "correct": False}, {"id": "c", "text": "ClusterIP", "correct": True}, {"id": "d", "text": "Ingress", "correct": False}]},
                ],
            },
            {
                "t": "Deployments",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Deployments — управление подами", "markdown": "## Deployments\n\nDeployment управляет репликами подов и обновлениями.\n\n```yaml\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: web-app\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: web\n  template:\n    metadata:\n      labels:\n        app: web\n    spec:\n      containers:\n        - name: web\n          image: myapp:v1\n          ports:\n            - containerPort: 8080\n          resources:\n            limits:\n              memory: '256Mi'\n              cpu: '500m'\n```\n\n### Стратегии обновления:\n- **RollingUpdate** — постепенная замена (по умолчанию)\n- **Recreate** — удалить все, создать новые\n\n### Команды:\n```bash\nkubectl apply -f deployment.yaml    # применить\nkubectl get deployments              # список\nkubectl scale deployment web --replicas=5  # масштаб\nkubectl rollout status deployment/web      # статус\nkubectl rollout undo deployment/web        # откат\n```"},
                    {"type": "code-puzzle", "instructions": "Составьте команды для работы с Deployment:", "correctOrder": ["kubectl apply -f deployment.yaml", "kubectl get deployments", "kubectl get pods", "kubectl scale deployment web --replicas=5", "kubectl rollout status deployment/web"]},
                    {"type": "terminal-sim", "task": "Масштабируйте deployment web до 5 реплик", "expectedCommand": "kubectl scale deployment web --replicas=5", "hint": "Используйте kubectl scale с флагом --replicas"},
                    {"type": "true-false", "statement": "Стратегия RollingUpdate обновляет поды постепенно, без простоя.", "correct": True},
                ],
            },
            {
                "t": "kubectl — управление кластером",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "kubectl — CLI для Kubernetes", "markdown": "## kubectl — командная строка K8s\n\n### Основные команды:\n```bash\n# Информация о кластере\nkubectl cluster-info\nkubectl get nodes\n\n# Работа с ресурсами\nkubectl get pods                # список подов\nkubectl get services            # список сервисов\nkubectl get deployments         # список деплойментов\nkubectl get all                 # всё\n\n# Подробная информация\nkubectl describe pod <name>\nkubectl logs <pod-name>\nkubectl logs -f <pod-name>      # follow\n\n# Создание и удаление\nkubectl apply -f config.yaml    # применить\nkubectl delete -f config.yaml   # удалить\n\n# Зайти в под\nkubectl exec -it <pod> -- bash\n\n# Port forwarding\nkubectl port-forward pod/<name> 8080:80\n```\n\n### Контексты:\n```bash\nkubectl config get-contexts     # список контекстов\nkubectl config use-context prod # переключиться\n```"},
                    {"type": "terminal-sim", "task": "Просмотрите логи пода web-app-xyz в режиме follow", "expectedCommand": "kubectl logs -f web-app-xyz", "hint": "Используйте kubectl logs с флагом -f для follow"},
                    {"type": "drag-order", "items": ["kubectl cluster-info — проверить кластер", "kubectl apply -f deployment.yaml — задеплоить", "kubectl get pods — проверить поды", "kubectl logs <pod> — посмотреть логи", "kubectl exec -it <pod> -- bash — зайти внутрь"]},
                    {"type": "fill-blank", "sentence": "Команда kubectl ___ -f config.yaml применяет конфигурацию к кластеру.", "answer": "apply"},
                ],
            },
            {
                "t": "Helm basics",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Helm — пакетный менеджер K8s", "markdown": "## Helm — пакетный менеджер для Kubernetes\n\n### Зачем Helm?\n- Управление сложными K8s-манифестами\n- Шаблонизация YAML\n- Версионирование релизов\n- Откат к предыдущей версии\n\n### Ключевые понятия:\n- **Chart** — пакет Helm (набор шаблонов)\n- **Release** — установленный chart\n- **Repository** — хранилище charts\n- **Values** — параметры кастомизации\n\n### Команды:\n```bash\n# Установить chart\nhelm install my-release bitnami/nginx\n\n# С кастомными values\nhelm install my-app ./my-chart -f values.yaml\n\n# Список релизов\nhelm list\n\n# Обновить\nhelm upgrade my-release ./my-chart\n\n# Откат\nhelm rollback my-release 1\n\n# Удалить\nhelm uninstall my-release\n```\n\n### Структура Chart:\n```\nmy-chart/\n  Chart.yaml        # метаданные\n  values.yaml       # значения по умолчанию\n  templates/\n    deployment.yaml  # шаблон\n    service.yaml     # шаблон\n```"},
                    {"type": "flashcards", "cards": [{"front": "Helm Chart", "back": "Пакет Helm — набор K8s-шаблонов и значений"}, {"front": "Release", "back": "Конкретная установка Chart в кластере"}, {"front": "values.yaml", "back": "Файл с параметрами кастомизации Chart"}, {"front": "helm rollback", "back": "Откат к предыдущей версии релиза"}]},
                    {"type": "quiz", "question": "Что такое Helm Chart?", "options": [{"id": "a", "text": "Docker-образ", "correct": False}, {"id": "b", "text": "Пакет K8s-шаблонов с параметрами", "correct": True}, {"id": "c", "text": "Плагин для kubectl", "correct": False}, {"id": "d", "text": "CI/CD pipeline", "correct": False}]},
                    {"type": "type-answer", "question": "Какой командой Helm откатить релиз my-release к версии 1?", "acceptedAnswers": ["helm rollback my-release 1"]},
                ],
            },
        ],
    },
    # ===== SECTION 6: Мониторинг и логирование =====
    {
        "title": "Мониторинг и логирование",
        "pos": 5,
        "lessons": [
            {
                "t": "Prometheus",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Prometheus — сбор метрик", "markdown": "## Prometheus\n\nPrometheus — система мониторинга и оповещений с открытым исходным кодом.\n\n### Как работает:\n```\nПриложение → /metrics endpoint → Prometheus (scrape) → Хранилище → PromQL\n```\n\n### Типы метрик:\n- **Counter** — счётчик (только растёт): http_requests_total\n- **Gauge** — значение (может расти и падать): temperature\n- **Histogram** — распределение значений: request_duration\n- **Summary** — статистика (квантили)\n\n### PromQL — язык запросов:\n```promql\n# Количество запросов за 5 минут\nrate(http_requests_total[5m])\n\n# Средняя загрузка CPU\navg(node_cpu_seconds_total)\n\n# 95-й перцентиль задержки\nhistogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))\n```\n\n### Конфигурация:\n```yaml\nscrape_configs:\n  - job_name: 'myapp'\n    static_configs:\n      - targets: ['localhost:8000']\n    scrape_interval: 15s\n```"},
                    {"type": "matching", "pairs": [{"left": "Counter", "right": "Счётчик, который только растёт"}, {"left": "Gauge", "right": "Значение, которое растёт и падает"}, {"left": "Histogram", "right": "Распределение значений в бакетах"}, {"left": "PromQL", "right": "Язык запросов Prometheus"}]},
                    {"type": "quiz", "question": "Каким способом Prometheus собирает метрики?", "options": [{"id": "a", "text": "Приложение отправляет метрики в Prometheus (push)", "correct": False}, {"id": "b", "text": "Prometheus опрашивает /metrics endpoint (pull/scrape)", "correct": True}, {"id": "c", "text": "Через базу данных", "correct": False}, {"id": "d", "text": "Через логи", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Язык запросов Prometheus называется ___.", "answer": "PromQL"},
                ],
            },
            {
                "t": "Grafana",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Grafana — визуализация метрик", "markdown": "## Grafana\n\nGrafana — платформа визуализации и дашбордов.\n\n### Возможности:\n- Красивые интерактивные дашборды\n- Множество источников данных\n- Шаблоны и переменные\n- Алерты и уведомления\n\n### Источники данных:\n- Prometheus (самый популярный)\n- InfluxDB\n- Elasticsearch\n- PostgreSQL / MySQL\n- CloudWatch, Stackdriver\n\n### Создание дашборда:\n1. Добавить Data Source → Prometheus\n2. Создать Dashboard → Add Panel\n3. Написать PromQL запрос\n4. Выбрать тип графика (graph, gauge, table, heatmap)\n5. Настроить thresholds и алерты\n\n### Популярные дашборды:\n- **Node Exporter** — метрики сервера\n- **Docker** — контейнеры\n- **Kubernetes** — кластер\n- **Nginx** — веб-сервер\n\n### Grafana + Docker:\n```yaml\ngrafana:\n  image: grafana/grafana\n  ports:\n    - '3000:3000'\n  volumes:\n    - grafana-data:/var/lib/grafana\n```"},
                    {"type": "drag-order", "items": ["Установить Grafana", "Добавить Data Source (Prometheus)", "Создать новый Dashboard", "Добавить Panel с PromQL запросом", "Настроить алерты и уведомления"]},
                    {"type": "quiz", "question": "Какой самый популярный источник данных для Grafana?", "options": [{"id": "a", "text": "MySQL", "correct": False}, {"id": "b", "text": "Elasticsearch", "correct": False}, {"id": "c", "text": "Prometheus", "correct": True}, {"id": "d", "text": "InfluxDB", "correct": False}]},
                    {"type": "true-false", "statement": "Grafana может работать только с Prometheus в качестве источника данных.", "correct": False},
                ],
            },
            {
                "t": "ELK Stack",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "ELK Stack — логирование", "markdown": "## ELK Stack\n\n### Компоненты:\n- **E**lasticsearch — поисковый движок, хранит логи\n- **L**ogstash — обработка и трансформация логов\n- **K**ibana — визуализация и поиск\n\n### Как работает:\n```\nПриложение → Logstash/Filebeat → Elasticsearch → Kibana\n```\n\n### Filebeat (лёгкий shipper):\n```yaml\nfilebeat.inputs:\n  - type: log\n    paths:\n      - /var/log/app/*.log\n\noutput.elasticsearch:\n  hosts: ['localhost:9200']\n```\n\n### Logstash (обработка):\n```\ninput {\n  beats { port => 5044 }\n}\nfilter {\n  grok {\n    match => { \"message\" => \"%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}\" }\n  }\n}\noutput {\n  elasticsearch { hosts => [\"localhost:9200\"] }\n}\n```\n\n### Kibana:\n- Поиск логов по ключевым словам\n- Фильтрация по времени, уровню, сервису\n- Dashboards и визуализации\n- Discover — интерактивный поиск"},
                    {"type": "matching", "pairs": [{"left": "Elasticsearch", "right": "Поисковый движок, хранение логов"}, {"left": "Logstash", "right": "Обработка и трансформация логов"}, {"left": "Kibana", "right": "Визуализация и поиск логов"}, {"left": "Filebeat", "right": "Лёгкий агент для сбора логов"}]},
                    {"type": "flashcards", "cards": [{"front": "Elasticsearch", "back": "Поисковый и аналитический движок для хранения логов"}, {"front": "Logstash", "back": "Обработка, фильтрация и трансформация логов"}, {"front": "Kibana", "back": "Веб-интерфейс для визуализации и поиска по логам"}, {"front": "Filebeat", "back": "Лёгкий shipper для отправки логов в Elasticsearch"}]},
                    {"type": "quiz", "question": "Какой компонент ELK Stack отвечает за визуализацию?", "options": [{"id": "a", "text": "Elasticsearch", "correct": False}, {"id": "b", "text": "Logstash", "correct": False}, {"id": "c", "text": "Kibana", "correct": True}, {"id": "d", "text": "Filebeat", "correct": False}]},
                ],
            },
            {
                "t": "Алерты и уведомления",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Алерты — реагирование на проблемы", "markdown": "## Алерты и уведомления\n\n### Зачем нужны алерты?\n- Узнавать о проблемах **до** пользователей\n- Автоматическое реагирование\n- Снижение MTTR (время восстановления)\n\n### Prometheus Alertmanager:\n```yaml\n# alert_rules.yml\ngroups:\n  - name: app_alerts\n    rules:\n      - alert: HighErrorRate\n        expr: rate(http_errors_total[5m]) > 0.05\n        for: 5m\n        labels:\n          severity: critical\n        annotations:\n          summary: 'Высокий процент ошибок'\n\n      - alert: HighLatency\n        expr: histogram_quantile(0.95, rate(http_duration_seconds_bucket[5m])) > 2\n        for: 10m\n        labels:\n          severity: warning\n```\n\n### Каналы уведомлений:\n- **Slack** — основной канал команды\n- **PagerDuty** — для дежурных (on-call)\n- **Email** — бэкап-канал\n- **Telegram** — популярен в СНГ\n- **Webhooks** — для кастомных интеграций\n\n### Правила хороших алертов:\n1. Алерт = нужно действие\n2. Не создавайте шум (alert fatigue)\n3. Severity: critical, warning, info"},
                    {"type": "quiz", "question": "Что такое alert fatigue?", "options": [{"id": "a", "text": "Усталость от слишком большого количества алертов", "correct": True}, {"id": "b", "text": "Медленная доставка уведомлений", "correct": False}, {"id": "c", "text": "Ошибка в конфигурации алертов", "correct": False}, {"id": "d", "text": "Отсутствие алертов", "correct": False}]},
                    {"type": "multi-select", "question": "Какие каналы используются для уведомлений об алертах?", "options": [{"id": "a", "text": "Slack", "correct": True}, {"id": "b", "text": "PagerDuty", "correct": True}, {"id": "c", "text": "Instagram", "correct": False}, {"id": "d", "text": "Telegram", "correct": True}, {"id": "e", "text": "TikTok", "correct": False}]},
                    {"type": "true-false", "statement": "Каждый алерт должен требовать действия — если действие не нужно, алерт лишний.", "correct": True},
                ],
            },
            {
                "t": "Метрики приложения",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Ключевые метрики", "markdown": "## Метрики приложения\n\n### RED метрики (для сервисов):\n- **R**ate — количество запросов в секунду\n- **E**rrors — процент ошибок\n- **D**uration — время ответа\n\n### USE метрики (для ресурсов):\n- **U**tilization — загрузка (% CPU, RAM)\n- **S**aturation — насыщение (длина очереди)\n- **E**rrors — ошибки ресурса\n\n### Четыре золотых сигнала Google:\n1. **Latency** — время ответа\n2. **Traffic** — нагрузка (RPS)\n3. **Errors** — процент ошибок\n4. **Saturation** — насыщение\n\n### Пример метрик Python (prometheus_client):\n```python\nfrom prometheus_client import Counter, Histogram\n\nREQUESTS = Counter('http_requests_total', 'Total requests', ['method', 'path'])\nLATENCY = Histogram('http_request_duration_seconds', 'Request latency')\n\n@app.middleware('http')\nasync def metrics_middleware(request, call_next):\n    with LATENCY.time():\n        response = await call_next(request)\n    REQUESTS.labels(method=request.method, path=request.url.path).inc()\n    return response\n```"},
                    {"type": "matching", "pairs": [{"left": "Rate", "right": "Количество запросов в секунду"}, {"left": "Errors", "right": "Процент ошибочных ответов"}, {"left": "Duration", "right": "Время обработки запроса"}, {"left": "Saturation", "right": "Насыщение ресурса (длина очереди)"}]},
                    {"type": "flashcards", "cards": [{"front": "RED метрики", "back": "Rate, Errors, Duration — для мониторинга сервисов"}, {"front": "USE метрики", "back": "Utilization, Saturation, Errors — для мониторинга ресурсов"}, {"front": "Latency", "back": "Время ответа сервиса на запрос"}, {"front": "RPS", "back": "Requests Per Second — запросов в секунду"}]},
                    {"type": "type-answer", "question": "Как расшифровывается аббревиатура RED в мониторинге?", "acceptedAnswers": ["Rate Errors Duration", "Rate, Errors, Duration"]},
                ],
            },
            {
                "t": "SLA, SLO, SLI",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "SLA, SLO, SLI — уровни сервиса", "markdown": "## SLA, SLO, SLI\n\n### SLI — Service Level Indicator\nИзмеряемая метрика сервиса.\n```\nПример: Доступность = uptime / total_time\nПример: Latency p99 = 200ms\n```\n\n### SLO — Service Level Objective\nЦелевое значение SLI.\n```\nПример: Доступность ≥ 99.9% (три девятки)\nПример: p99 latency ≤ 300ms\n```\n\n### SLA — Service Level Agreement\nЮридическое соглашение с клиентом.\n```\nПример: «Гарантируем 99.9% uptime, иначе компенсация»\n```\n\n### Таблица девяток:\n| Uptime | Простой/год | Простой/месяц |\n|--------|-----------|---------------|\n| 99% | 3.65 дня | 7.3 часа |\n| 99.9% | 8.76 часа | 43.8 мин |\n| 99.99% | 52.6 мин | 4.38 мин |\n| 99.999% | 5.26 мин | 26.3 сек |\n\n### Error Budget:\nError Budget = 100% - SLO\nНапример: SLO 99.9% → Error Budget 0.1% (43.8 мин/месяц простоя)"},
                    {"type": "matching", "pairs": [{"left": "SLI", "right": "Измеряемая метрика (indicator)"}, {"left": "SLO", "right": "Целевое значение метрики (objective)"}, {"left": "SLA", "right": "Юридическое соглашение (agreement)"}, {"left": "Error Budget", "right": "Допустимое количество ошибок/простоя"}]},
                    {"type": "quiz", "question": "Сколько минут простоя в месяц допускает SLO в 99.9%?", "options": [{"id": "a", "text": "4.38 минуты", "correct": False}, {"id": "b", "text": "43.8 минуты", "correct": True}, {"id": "c", "text": "7.3 часа", "correct": False}, {"id": "d", "text": "5.26 минуты", "correct": False}]},
                    {"type": "drag-order", "items": ["Определить SLI (что измеряем)", "Установить SLO (целевое значение)", "Рассчитать Error Budget", "Настроить мониторинг и алерты", "Подписать SLA с клиентом"]},
                ],
            },
        ],
    },
    # ===== SECTION 7: Практика DevOps =====
    {
        "title": "Практика DevOps",
        "pos": 6,
        "lessons": [
            {
                "t": "Terraform basics",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Terraform — IaC инструмент", "markdown": "## Terraform\n\nTerraform — декларативный инструмент для создания инфраструктуры.\n\n### Workflow:\n```bash\nterraform init      # инициализация\nterraform plan      # что будет сделано\nterraform apply     # применить изменения\nterraform destroy   # удалить всё\n```\n\n### Пример — EC2 инстанс:\n```hcl\nprovider \"aws\" {\n  region = \"us-east-1\"\n}\n\nresource \"aws_instance\" \"web\" {\n  ami           = \"ami-0abcdef1234567890\"\n  instance_type = \"t3.micro\"\n\n  tags = {\n    Name = \"web-server\"\n  }\n}\n\nresource \"aws_security_group\" \"web_sg\" {\n  ingress {\n    from_port   = 80\n    to_port     = 80\n    protocol    = \"tcp\"\n    cidr_blocks = [\"0.0.0.0/0\"]\n  }\n}\n\noutput \"public_ip\" {\n  value = aws_instance.web.public_ip\n}\n```\n\n### State:\n- Terraform хранит состояние в `terraform.tfstate`\n- Удалённый state: S3 + DynamoDB для блокировки\n- **Никогда** не редактируйте state вручную!"},
                    {"type": "drag-order", "items": ["terraform init — инициализация", "terraform plan — предпросмотр изменений", "terraform apply — применить изменения", "terraform show — проверить состояние", "terraform destroy — удалить ресурсы"]},
                    {"type": "terminal-sim", "task": "Предпросмотрите изменения Terraform перед применением", "expectedCommand": "terraform plan", "hint": "Используйте terraform plan для предпросмотра"},
                    {"type": "quiz", "question": "Где Terraform хранит информацию о созданных ресурсах?", "options": [{"id": "a", "text": "В файле terraform.tfstate", "correct": True}, {"id": "b", "text": "В Docker-контейнере", "correct": False}, {"id": "c", "text": "В переменных окружения", "correct": False}, {"id": "d", "text": "В Kubernetes секретах", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Команда terraform ___ показывает план изменений перед применением.", "answer": "plan"},
                ],
            },
            {
                "t": "Ansible",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Ansible — конфигурация серверов", "markdown": "## Ansible\n\nAnsible — инструмент автоматизации конфигурации серверов.\n\n### Преимущества:\n- **Agentless** — не нужен агент на серверах\n- Работает через SSH\n- Написан на Python, playbooks в YAML\n- Идемпотентный — безопасно запускать повторно\n\n### Inventory (список серверов):\n```ini\n[web]\n192.168.1.10\n192.168.1.11\n\n[db]\n192.168.1.20\n```\n\n### Playbook:\n```yaml\n- hosts: web\n  become: yes\n  tasks:\n    - name: Install nginx\n      apt:\n        name: nginx\n        state: present\n\n    - name: Start nginx\n      service:\n        name: nginx\n        state: started\n        enabled: yes\n\n    - name: Copy config\n      template:\n        src: nginx.conf.j2\n        dest: /etc/nginx/nginx.conf\n      notify: Restart nginx\n\n  handlers:\n    - name: Restart nginx\n      service:\n        name: nginx\n        state: restarted\n```\n\n### Команды:\n```bash\nansible-playbook -i inventory playbook.yml\nansible all -m ping -i inventory\n```"},
                    {"type": "quiz", "question": "Какое ключевое преимущество Ansible перед другими инструментами?", "options": [{"id": "a", "text": "Agentless — не требует установки агента на серверах", "correct": True}, {"id": "b", "text": "Работает только с AWS", "correct": False}, {"id": "c", "text": "Написан на Java", "correct": False}, {"id": "d", "text": "Поддерживает только Linux", "correct": False}]},
                    {"type": "true-false", "statement": "Ansible playbooks написаны в формате YAML и являются идемпотентными.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Playbook", "back": "YAML-файл с задачами для автоматизации"}, {"front": "Inventory", "back": "Файл со списком серверов"}, {"front": "Idempotent", "back": "Повторный запуск даёт тот же результат"}, {"front": "Handler", "back": "Задача, выполняемая только при изменении"}]},
                ],
            },
            {
                "t": "Управление секретами",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Secrets Management", "markdown": "## Управление секретами\n\n### Проблема:\n```\n❌ password = 'super_secret' в коде\n❌ .env файл в Git\n❌ Пароли в Slack\n```\n\n### Решения:\n\n**HashiCorp Vault:**\n```bash\n# Записать секрет\nvault kv put secret/myapp db_password=s3cret\n\n# Прочитать секрет\nvault kv get secret/myapp\n```\n\n**AWS Secrets Manager:**\n```bash\naws secretsmanager create-secret \\\n  --name myapp/db \\\n  --secret-string '{\"password\":\"s3cret\"}'\n```\n\n**Kubernetes Secrets:**\n```yaml\napiVersion: v1\nkind: Secret\nmetadata:\n  name: db-secret\ntype: Opaque\ndata:\n  password: czNjcmV0   # base64\n```\n\n### Лучшие практики:\n1. Никогда не хранить секреты в Git\n2. Ротация секретов каждые 90 дней\n3. Принцип наименьших привилегий\n4. Аудит доступа к секретам\n5. Шифрование at rest и in transit"},
                    {"type": "multi-select", "question": "Какие инструменты используются для управления секретами?", "options": [{"id": "a", "text": "HashiCorp Vault", "correct": True}, {"id": "b", "text": "AWS Secrets Manager", "correct": True}, {"id": "c", "text": "Notepad", "correct": False}, {"id": "d", "text": "Kubernetes Secrets", "correct": True}, {"id": "e", "text": "Google Docs", "correct": False}]},
                    {"type": "true-false", "statement": "Хранение паролей в .env файле, добавленном в Git — безопасная практика.", "correct": False},
                    {"type": "drag-order", "items": ["Выбрать инструмент (Vault, AWS SM)", "Создать и сохранить секреты", "Настроить доступ (RBAC)", "Интегрировать с приложением", "Настроить автоматическую ротацию"]},
                ],
            },
            {
                "t": "Blue-Green и Canary Deploy",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Стратегии деплоя", "markdown": "## Стратегии деплоя\n\n### Blue-Green Deployment:\n```\nBlue (v1) ← трафик      Green (v2) — подготовка\n\nПосле проверки:\nBlue (v1) — standby      Green (v2) ← трафик\n```\n- Мгновенное переключение\n- Быстрый откат (вернуть трафик на Blue)\n- Нужно 2x ресурсов\n\n### Canary Deployment:\n```\nv1: 95% трафика → v1: 80% → v1: 50% → v1: 0%\nv2:  5% трафика → v2: 20% → v2: 50% → v2: 100%\n```\n- Постепенное увеличение трафика\n- Мониторинг ошибок на каждом этапе\n- Откат при проблемах\n\n### Rolling Update:\n```\n[v1] [v1] [v1] [v1]\n[v2] [v1] [v1] [v1]  ← замена по одному\n[v2] [v2] [v1] [v1]\n[v2] [v2] [v2] [v1]\n[v2] [v2] [v2] [v2]  ← все обновлены\n```\n- По умолчанию в Kubernetes\n- Не нужны дополнительные ресурсы\n\n### Feature Flags:\n```python\nif feature_flags.is_enabled('new_ui', user_id):\n    show_new_ui()\nelse:\n    show_old_ui()\n```"},
                    {"type": "matching", "pairs": [{"left": "Blue-Green", "right": "Два идентичных окружения, мгновенное переключение"}, {"left": "Canary", "right": "Постепенное увеличение трафика на новую версию"}, {"left": "Rolling Update", "right": "Поочерёдная замена экземпляров"}, {"left": "Feature Flags", "right": "Включение/отключение функций без деплоя"}]},
                    {"type": "quiz", "question": "Какая стратегия деплоя используется в Kubernetes по умолчанию?", "options": [{"id": "a", "text": "Blue-Green", "correct": False}, {"id": "b", "text": "Canary", "correct": False}, {"id": "c", "text": "Rolling Update", "correct": True}, {"id": "d", "text": "Big Bang", "correct": False}]},
                    {"type": "true-false", "statement": "Blue-Green deployment требует в два раза больше серверных ресурсов.", "correct": True},
                ],
            },
            {
                "t": "GitOps",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "GitOps — Git как источник истины", "markdown": "## GitOps\n\n### Принципы GitOps:\n1. **Git как единый источник истины** — всё описано в Git\n2. **Декларативный подход** — описываем желаемое состояние\n3. **Автоматическая синхронизация** — агент следит за Git\n4. **Pull-модель** — агент в кластере тянет изменения\n\n### Workflow:\n```\nРазработчик → Push в Git → ArgoCD/Flux замечает → Автоматический деплой в K8s\n```\n\n### ArgoCD:\n```yaml\napiVersion: argoproj.io/v1alpha1\nkind: Application\nmetadata:\n  name: myapp\nspec:\n  project: default\n  source:\n    repoURL: https://github.com/user/k8s-configs\n    targetRevision: main\n    path: overlays/production\n  destination:\n    server: https://kubernetes.default.svc\n    namespace: production\n  syncPolicy:\n    automated:\n      prune: true\n      selfHeal: true\n```\n\n### GitOps vs CI/CD Push:\n- **Push (традиционный):** CI pushит в кластер\n- **Pull (GitOps):** Агент в кластере тянет из Git\n\n### Инструменты:\n- **ArgoCD** — самый популярный\n- **Flux** — от Weaveworks\n- **Jenkins X** — Jenkins для K8s"},
                    {"type": "flashcards", "cards": [{"front": "GitOps", "back": "Подход, где Git — единый источник истины для инфраструктуры"}, {"front": "ArgoCD", "back": "Самый популярный GitOps-инструмент для Kubernetes"}, {"front": "Pull-модель", "back": "Агент в кластере сам тянет изменения из Git"}, {"front": "Self-heal", "back": "Автоматическое восстановление при ручных изменениях в кластере"}]},
                    {"type": "quiz", "question": "Чем отличается GitOps (Pull) от традиционного CI/CD (Push)?", "options": [{"id": "a", "text": "В GitOps агент в кластере сам тянет изменения из Git", "correct": True}, {"id": "b", "text": "GitOps не использует Git", "correct": False}, {"id": "c", "text": "GitOps работает только с Docker", "correct": False}, {"id": "d", "text": "В GitOps нет автоматизации", "correct": False}]},
                    {"type": "true-false", "statement": "В GitOps Git является единственным источником истины для инфраструктуры.", "correct": True},
                ],
            },
            {
                "t": "Итоговый проект: CI/CD пайплайн",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Итоговый проект", "markdown": "## Итоговый проект: Полный CI/CD пайплайн\n\n### Что мы создадим:\nПолный DevOps-пайплайн для веб-приложения.\n\n### Архитектура:\n```\nGitHub Repo\n  ↓ push\nGitHub Actions CI\n  ↓ тесты пройдены\nDocker Build & Push\n  ↓ образ загружен\nDeploy to Server\n  ↓ docker compose up\nМониторинг (Prometheus + Grafana)\n```\n\n### Шаги проекта:\n\n**1. Dockerfile:**\n```dockerfile\nFROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nEXPOSE 8000\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\"]\n```\n\n**2. docker-compose.yml:**\n```yaml\nservices:\n  web:\n    build: .\n    ports: ['8000:8000']\n    depends_on: [db]\n  db:\n    image: postgres:15\n    volumes: [pgdata:/var/lib/postgresql/data]\nvolumes:\n  pgdata:\n```\n\n**3. GitHub Actions (.github/workflows/deploy.yml):**\n```yaml\nname: Deploy\non:\n  push:\n    branches: [main]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: pip install -r requirements.txt\n      - run: pytest\n  deploy:\n    needs: test\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Deploy\n        uses: appleboy/ssh-action@v1\n        with:\n          host: ${{ secrets.HOST }}\n          username: ${{ secrets.USER }}\n          key: ${{ secrets.SSH_KEY }}\n          script: |\n            cd /app && git pull\n            docker compose up -d --build\n```\n\n### Чек-лист:\n- [ ] Dockerfile работает\n- [ ] Docker Compose запускает все сервисы\n- [ ] CI запускает тесты\n- [ ] CD деплоит на сервер\n- [ ] Мониторинг настроен"},
                    {"type": "drag-order", "items": ["Написать Dockerfile для приложения", "Создать docker-compose.yml со всеми сервисами", "Настроить GitHub Actions для тестов", "Добавить секреты для деплоя", "Настроить автоматический деплой на сервер", "Добавить мониторинг (Prometheus + Grafana)"]},
                    {"type": "code-puzzle", "instructions": "Составьте порядок этапов CI/CD пайплайна:", "correctOrder": ["git push в main ветку", "GitHub Actions запускает тесты", "Docker build собирает образ", "Docker push загружает в registry", "SSH-деплой на production сервер", "docker compose up -d --build"]},
                    {"type": "multi-select", "question": "Что должно быть в полноценном DevOps-пайплайне?", "options": [{"id": "a", "text": "Автоматические тесты", "correct": True}, {"id": "b", "text": "Docker-контейнеризация", "correct": True}, {"id": "c", "text": "Ручной FTP-upload", "correct": False}, {"id": "d", "text": "Мониторинг и алерты", "correct": True}, {"id": "e", "text": "Secrets management", "correct": True}]},
                    {"type": "true-false", "statement": "В итоговом проекте деплой на production происходит только после успешного прохождения тестов.", "correct": True},
                ],
            },
        ],
    },
]


async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping."); return
        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author:
            print("No users."); return
        course = Course(
            title=T,
            slug="devops-docker-cicd-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="DevOps",
            difficulty="Intermediate",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()
        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(course_id=course.id, title=sd["title"], position=sd["pos"])
            db.add(sec)
            await db.flush()
            for li, ld in enumerate(sd["lessons"]):
                les = CourseLesson(
                    section_id=sec.id,
                    title=ld["t"],
                    position=li,
                    content_type="interactive",
                    content_markdown="",
                    xp_reward=ld["xp"],
                    steps=ld["steps"],
                )
                db.add(les)
                await db.flush()
                r, c = lc // 5, lc % 5
                x, y = SNAKE_X[c] * CANVAS_W, V_PAD + r * ROW_H
                nodes.append({"id": str(les.id), "x": x, "y": y})
                if lc > 0:
                    edges.append({"id": f"e-{lc}", "source": nodes[-2]["id"], "target": nodes[-1]["id"]})
                lc += 1
                tl += 1
        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
