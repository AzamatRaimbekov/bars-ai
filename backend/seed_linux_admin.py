"""Seed: Linux и системное администрирование — 7 sections, 38 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Linux и системное администрирование"
DESC = (
    "Курс по Linux: командная строка, файловая система, управление "
    "пользователями, сети, сервисы, bash-скрипты, серверное администрирование."
)

S = [
    # ===== SECTION 1: Введение в Linux =====
    {
        "title": "Введение в Linux",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое Linux",
                "xp": 15,
                "steps": [
                    {"type": "info", "title": "Linux — свободная ОС", "markdown": "## Что такое Linux?\n\n**Linux** — это семейство свободных и открытых операционных систем на базе ядра Linux, созданного Линусом Торвальдсом в 1991 году.\n\n### Почему Linux?\n- **Бесплатный** — не нужно покупать лицензию\n- **Открытый код** — можно изучать и модифицировать\n- **Безопасный** — меньше вирусов, чем в Windows\n- **Стабильный** — серверы работают годами без перезагрузки\n- **Гибкий** — настраивается под любые задачи\n\n### Где используется Linux?\n- **90%+ серверов** в мире\n- Android-устройства (ядро Linux)\n- Суперкомпьютеры (100% топ-500)\n- IoT-устройства, роутеры\n- Облачные платформы (AWS, GCP, Azure)\n\n### Ядро и ОС:\n```\nПользователь → Приложения → Shell → Ядро (kernel) → Железо\n```"},
                    {"type": "quiz", "question": "Кто создал ядро Linux?", "options": [{"id": "a", "text": "Ричард Столлман", "correct": False}, {"id": "b", "text": "Линус Торвальдс", "correct": True}, {"id": "c", "text": "Деннис Ритчи", "correct": False}, {"id": "d", "text": "Билл Гейтс", "correct": False}]},
                    {"type": "true-false", "statement": "Linux используется на более чем 90% серверов в мире.", "correct": True},
                    {"type": "flashcards", "cards": [{"front": "Kernel (ядро)", "back": "Основная часть ОС, управляющая железом и ресурсами"}, {"front": "Open Source", "back": "Открытый исходный код, который можно изучать и модифицировать"}, {"front": "Shell", "back": "Командная оболочка — интерфейс между пользователем и ядром"}, {"front": "GNU/Linux", "back": "Полное название: ядро Linux + утилиты проекта GNU"}]},
                ],
            },
            {
                "t": "Дистрибутивы Linux",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Популярные дистрибутивы", "markdown": "## Дистрибутивы Linux\n\n**Дистрибутив** — это ядро Linux + набор программ + пакетный менеджер.\n\n### Основные семейства:\n\n#### Debian-based:\n- **Ubuntu** — самый популярный для начинающих\n- **Debian** — стабильный, для серверов\n- **Linux Mint** — удобный десктоп\n- Пакетный менеджер: `apt`\n\n#### Red Hat-based:\n- **CentOS / Rocky Linux** — серверы в Enterprise\n- **Fedora** — новейшие технологии\n- **RHEL** — коммерческая поддержка\n- Пакетный менеджер: `yum` / `dnf`\n\n#### Другие:\n- **Arch Linux** — для продвинутых, rolling release\n- **Alpine** — минимальный, для Docker-контейнеров\n- **openSUSE** — корпоративный\n\n### Как выбрать?\n```\nНовичок → Ubuntu / Linux Mint\nСервер → Debian / Rocky Linux\nDocker → Alpine\nОбучение → Arch Linux\n```"},
                    {"type": "matching", "pairs": [{"left": "Ubuntu", "right": "Самый популярный, для начинающих"}, {"left": "Debian", "right": "Стабильный, для серверов"}, {"left": "CentOS / Rocky", "right": "Enterprise-серверы, Red Hat-based"}, {"left": "Alpine", "right": "Минимальный, для Docker-контейнеров"}]},
                    {"type": "quiz", "question": "Какой пакетный менеджер используется в Ubuntu?", "options": [{"id": "a", "text": "yum", "correct": False}, {"id": "b", "text": "apt", "correct": True}, {"id": "c", "text": "pacman", "correct": False}, {"id": "d", "text": "brew", "correct": False}]},
                    {"type": "category-sort", "categories": [{"name": "Debian-based", "items": ["Ubuntu", "Linux Mint", "Debian"]}, {"name": "Red Hat-based", "items": ["CentOS", "Fedora", "RHEL"]}]},
                ],
            },
            {
                "t": "Установка Linux",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Способы установки Linux", "markdown": "## Установка Linux\n\n### Вариант 1: Виртуальная машина (рекомендуется для обучения)\n```bash\n# Установите VirtualBox или VMware\n# Скачайте ISO-образ Ubuntu\n# Создайте VM: 2 CPU, 4GB RAM, 20GB диск\n```\n\n### Вариант 2: WSL (Windows Subsystem for Linux)\n```powershell\n# В PowerShell (от администратора):\nwsl --install\n# По умолчанию установится Ubuntu\n```\n\n### Вариант 3: Двойная загрузка\n1. Скачать ISO с ubuntu.com\n2. Записать на USB через Rufus / Etcher\n3. Загрузиться с USB\n4. Установить рядом с Windows\n\n### Вариант 4: VPS-сервер\n```bash\n# Арендовать сервер на DigitalOcean / Hetzner\n# Подключиться по SSH:\nssh root@IP_СЕРВЕРА\n```\n\n### После установки:\n```bash\nsudo apt update && sudo apt upgrade -y\n```"},
                    {"type": "drag-order", "items": ["Скачать ISO-образ Ubuntu", "Установить VirtualBox", "Создать виртуальную машину", "Указать ISO-образ как загрузочный", "Следовать мастеру установки Ubuntu"]},
                    {"type": "quiz", "question": "Какой способ установки Linux лучше всего подходит для обучения?", "options": [{"id": "a", "text": "Виртуальная машина", "correct": True}, {"id": "b", "text": "Полная замена Windows", "correct": False}, {"id": "c", "text": "Компиляция ядра из исходников", "correct": False}, {"id": "d", "text": "Установка на телефон", "correct": False}]},
                    {"type": "terminal-sim", "prompt": "Обновите список пакетов и установите обновления в Ubuntu:", "expectedCommand": "sudo apt update && sudo apt upgrade -y", "hint": "Используйте apt update для обновления списка и apt upgrade для установки обновлений"},
                ],
            },
            {
                "t": "Терминал и командная оболочка",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Терминал — главный инструмент", "markdown": "## Терминал Linux\n\nТерминал (эмулятор терминала) — это программа для ввода команд.\n\n### Командные оболочки (shell):\n- **bash** — стандартная в большинстве дистрибутивов\n- **zsh** — расширенная (по умолчанию в macOS)\n- **fish** — удобная с автодополнением\n- **sh** — базовая POSIX-оболочка\n\n### Анатомия команды:\n```bash\nкоманда  -опции  аргументы\nls       -la     /home\n```\n\n### Приглашение (prompt):\n```\nuser@hostname:~$    # обычный пользователь\nroot@hostname:~#    # суперпользователь (root)\n```\n\n### Полезные сочетания:\n| Комбинация | Действие |\n|------------|----------|\n| Tab | Автодополнение |\n| Ctrl+C | Прервать команду |\n| Ctrl+D | Выход / EOF |\n| Ctrl+L | Очистить экран |\n| ↑ / ↓ | История команд |\n| Ctrl+R | Поиск по истории |"},
                    {"type": "quiz", "question": "Какой символ в приглашении означает суперпользователя (root)?", "options": [{"id": "a", "text": "$", "correct": False}, {"id": "b", "text": "#", "correct": True}, {"id": "c", "text": "%", "correct": False}, {"id": "d", "text": "&", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Ctrl+C", "right": "Прервать команду"}, {"left": "Ctrl+L", "right": "Очистить экран"}, {"left": "Ctrl+R", "right": "Поиск по истории команд"}, {"left": "Tab", "right": "Автодополнение"}]},
                    {"type": "fill-blank", "sentence": "Стандартная командная оболочка в большинстве Linux-дистрибутивов — это ___.", "answer": "bash"},
                ],
            },
            {
                "t": "Первые команды",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Базовые команды Linux", "markdown": "## Первые команды в Linux\n\n### Информация о системе:\n```bash\nwhoami          # имя текущего пользователя\nhostname        # имя компьютера\nuname -a        # информация о ядре\ndate            # текущая дата и время\nuptime          # время работы системы\n```\n\n### Справка:\n```bash\nman ls          # полная документация команды ls\nls --help       # краткая справка\nwhich python    # где находится программа\n```\n\n### Работа с историей:\n```bash\nhistory         # показать историю команд\n!100            # выполнить команду #100 из истории\n!!              # повторить последнюю команду\n```\n\n### Вывод текста:\n```bash\necho \"Привет, Linux!\"     # вывести текст\necho $HOME                 # вывести переменную\nclear                      # очистить экран\n```"},
                    {"type": "terminal-sim", "prompt": "Узнайте имя текущего пользователя:", "expectedCommand": "whoami", "hint": "Команда из 6 букв: who am i (слитно)"},
                    {"type": "code-puzzle", "instructions": "Соберите команду для просмотра информации о ядре системы:", "correctOrder": ["uname", "-a"]},
                    {"type": "type-answer", "question": "Какой командой можно открыть документацию по любой команде Linux?", "acceptedAnswers": ["man", "man command"]},
                    {"type": "quiz", "question": "Что выведет команда echo $HOME?", "options": [{"id": "a", "text": "Слово HOME", "correct": False}, {"id": "b", "text": "Путь к домашней директории пользователя", "correct": True}, {"id": "c", "text": "Ошибку", "correct": False}, {"id": "d", "text": "Пустую строку", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 2: Файловая система =====
    {
        "title": "Файловая система",
        "pos": 1,
        "lessons": [
            {
                "t": "Структура директорий",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Дерево каталогов Linux", "markdown": "## Структура файловой системы Linux\n\nВ Linux всё начинается с корня `/` — единое дерево каталогов.\n\n### Основные директории:\n```\n/\n├── bin/      → основные команды (ls, cp, mv)\n├── boot/     → файлы загрузчика\n├── dev/      → файлы устройств\n├── etc/      → конфигурационные файлы\n├── home/     → домашние каталоги пользователей\n├── lib/      → библиотеки\n├── opt/      → дополнительные программы\n├── proc/     → виртуальная ФС процессов\n├── root/     → домашний каталог root\n├── tmp/      → временные файлы\n├── usr/      → пользовательские программы\n├── var/      → переменные данные (логи, почта)\n└── mnt/      → точки монтирования\n```\n\n### Важные правила:\n- Всё является файлом (даже устройства!)\n- Пути разделяются `/` (не `\\` как в Windows)\n- Имена чувствительны к регистру: `File` ≠ `file`"},
                    {"type": "matching", "pairs": [{"left": "/etc", "right": "Конфигурационные файлы"}, {"left": "/home", "right": "Домашние каталоги пользователей"}, {"left": "/var", "right": "Переменные данные, логи"}, {"left": "/tmp", "right": "Временные файлы"}, {"left": "/bin", "right": "Основные команды системы"}]},
                    {"type": "true-false", "statement": "В Linux имена файлов чувствительны к регистру: file.txt и File.txt — это разные файлы.", "correct": True},
                    {"type": "quiz", "question": "Где хранятся конфигурационные файлы системы в Linux?", "options": [{"id": "a", "text": "/home", "correct": False}, {"id": "b", "text": "/etc", "correct": True}, {"id": "c", "text": "/bin", "correct": False}, {"id": "d", "text": "/tmp", "correct": False}]},
                ],
            },
            {
                "t": "Навигация: ls, cd, pwd",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Перемещение по файловой системе", "markdown": "## Навигация в терминале\n\n### pwd — текущая директория:\n```bash\npwd\n# /home/user\n```\n\n### cd — смена директории:\n```bash\ncd /var/log        # перейти в /var/log\ncd ~               # перейти в домашнюю (~)\ncd ..              # на уровень вверх\ncd -               # вернуться в предыдущую\ncd                 # перейти в домашнюю (без аргументов)\n```\n\n### ls — список файлов:\n```bash\nls                 # список файлов\nls -l              # подробный формат\nls -a              # показать скрытые (начинаются с .)\nls -la             # подробно + скрытые\nls -lh             # человекочитаемые размеры\nls -R              # рекурсивно\n```\n\n### Пример ls -la:\n```\ndrwxr-xr-x  5 user group 4096 Mar 10 14:22 Documents\n-rw-r--r--  1 user group  512 Mar  8 09:15 notes.txt\n```\n- `d` — директория, `-` — файл\n- `rwxr-xr-x` — права доступа\n- `user group` — владелец и группа"},
                    {"type": "terminal-sim", "prompt": "Перейдите в директорию /var/log:", "expectedCommand": "cd /var/log", "hint": "Используйте cd и абсолютный путь"},
                    {"type": "terminal-sim", "prompt": "Покажите все файлы (включая скрытые) в подробном формате:", "expectedCommand": "ls -la", "hint": "Флаг -l для подробного вывода, -a для скрытых"},
                    {"type": "type-answer", "question": "Какой командой можно узнать текущую директорию?", "acceptedAnswers": ["pwd"]},
                ],
            },
            {
                "t": "Работа с файлами: cp, mv, rm",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Копирование, перемещение, удаление", "markdown": "## Работа с файлами\n\n### Создание файлов и директорий:\n```bash\ntouch file.txt          # создать пустой файл\nmkdir mydir             # создать директорию\nmkdir -p a/b/c          # создать вложенные директории\n```\n\n### Копирование:\n```bash\ncp file.txt copy.txt           # копировать файл\ncp -r mydir/ backup/           # копировать директорию (-r рекурсивно)\ncp -i file.txt dest/           # спросить перед перезаписью\n```\n\n### Перемещение/переименование:\n```bash\nmv file.txt newname.txt        # переименовать\nmv file.txt /tmp/              # переместить в /tmp\nmv -i old.txt new.txt          # спросить перед перезаписью\n```\n\n### Удаление:\n```bash\nrm file.txt                    # удалить файл\nrm -r mydir/                   # удалить директорию рекурсивно\nrm -rf /tmp/test/              # удалить без подтверждения\nrmdir emptydir                 # удалить пустую директорию\n```\n\n⚠️ **ОСТОРОЖНО:** `rm -rf /` удалит ВСЁ! В Linux нет корзины!"},
                    {"type": "terminal-sim", "prompt": "Создайте вложенную структуру директорий projects/web/css:", "expectedCommand": "mkdir -p projects/web/css", "hint": "Используйте mkdir с флагом -p для создания вложенных директорий"},
                    {"type": "quiz", "question": "Что делает команда mv file.txt newfile.txt?", "options": [{"id": "a", "text": "Копирует файл", "correct": False}, {"id": "b", "text": "Переименовывает файл", "correct": True}, {"id": "c", "text": "Удаляет файл", "correct": False}, {"id": "d", "text": "Создаёт файл", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Соберите команду для рекурсивного копирования директории:", "correctOrder": ["cp", "-r", "source_dir/", "backup_dir/"]},
                    {"type": "true-false", "statement": "Команда rm в Linux перемещает файлы в корзину, откуда их можно восстановить.", "correct": False},
                ],
            },
            {
                "t": "Права доступа: chmod, chown",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Система прав в Linux", "markdown": "## Права доступа\n\n### Три типа прав:\n- **r (read)** = 4 — чтение\n- **w (write)** = 2 — запись\n- **x (execute)** = 1 — выполнение\n\n### Три категории:\n- **u (user)** — владелец\n- **g (group)** — группа\n- **o (others)** — остальные\n\n### Пример: `-rwxr-xr--`\n```\n-  rwx  r-x  r--\n│  │    │    └── others: чтение\n│  │    └── group: чтение + выполнение\n│  └── user: всё\n└── тип файла\n```\nВ числах: 7 (4+2+1) 5 (4+0+1) 4 (4+0+0) = **754**\n\n### chmod — изменение прав:\n```bash\nchmod 755 script.sh        # rwxr-xr-x\nchmod +x script.sh         # добавить выполнение всем\nchmod u+w file.txt         # добавить запись владельцу\nchmod go-w file.txt        # убрать запись у группы и остальных\n```\n\n### chown — смена владельца:\n```bash\nchown user:group file.txt  # сменить владельца и группу\nchown -R user:group dir/   # рекурсивно\n```"},
                    {"type": "quiz", "question": "Что означает числовое право 755?", "options": [{"id": "a", "text": "rwxr-xr-x", "correct": True}, {"id": "b", "text": "rwxrwxrwx", "correct": False}, {"id": "c", "text": "rw-r--r--", "correct": False}, {"id": "d", "text": "rwx------", "correct": False}]},
                    {"type": "terminal-sim", "prompt": "Сделайте файл script.sh исполняемым для всех:", "expectedCommand": "chmod +x script.sh", "hint": "Используйте chmod с +x"},
                    {"type": "fill-blank", "sentence": "Числовое значение права на чтение (r) равно ___.", "answer": "4"},
                    {"type": "matching", "pairs": [{"left": "r (read)", "right": "4 — чтение"}, {"left": "w (write)", "right": "2 — запись"}, {"left": "x (execute)", "right": "1 — выполнение"}, {"left": "chmod 644", "right": "rw-r--r--"}]},
                ],
            },
            {
                "t": "Ссылки: жёсткие и символические",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Ссылки в Linux", "markdown": "## Ссылки (links)\n\n### Символическая ссылка (symlink):\nЯрлык, указывающий на путь к файлу.\n```bash\nln -s /path/to/original link_name\n\n# Пример:\nln -s /etc/nginx/nginx.conf ~/nginx.conf\nls -la ~/nginx.conf\n# lrwxrwxrwx 1 user group 23 ... nginx.conf -> /etc/nginx/nginx.conf\n```\n\n### Жёсткая ссылка (hard link):\nДополнительное имя для того же inode (данных на диске).\n```bash\nln original.txt hardlink.txt\n\n# У обоих одинаковый inode:\nls -li\n# 123456 -rw-r--r-- 2 user group 100 original.txt\n# 123456 -rw-r--r-- 2 user group 100 hardlink.txt\n```\n\n### Различия:\n| Свойство | Символическая | Жёсткая |\n|----------|--------------|----------|\n| Работает между ФС | Да | Нет |\n| Ссылка на директорию | Да | Нет |\n| При удалении оригинала | Битая ссылка | Данные остаются |\n| Свой inode | Да | Нет (общий) |"},
                    {"type": "terminal-sim", "prompt": "Создайте символическую ссылку mylink на файл /etc/hosts:", "expectedCommand": "ln -s /etc/hosts mylink", "hint": "ln -s для символической ссылки"},
                    {"type": "quiz", "question": "Что произойдёт с жёсткой ссылкой при удалении оригинального файла?", "options": [{"id": "a", "text": "Станет битой ссылкой", "correct": False}, {"id": "b", "text": "Данные останутся доступны", "correct": True}, {"id": "c", "text": "Будет удалена автоматически", "correct": False}, {"id": "d", "text": "Вызовет ошибку системы", "correct": False}]},
                    {"type": "true-false", "statement": "Символическая ссылка может указывать на директорию, а жёсткая — нет.", "correct": True},
                ],
            },
            {
                "t": "Поиск: find и grep",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Поиск файлов и текста", "markdown": "## Поиск в Linux\n\n### find — поиск файлов:\n```bash\nfind /home -name \"*.txt\"            # по имени\nfind / -type d -name \"config\"       # директории\nfind . -size +100M                  # файлы > 100MB\nfind . -mtime -7                    # изменённые за 7 дней\nfind . -name \"*.log\" -delete        # найти и удалить\nfind . -type f -exec chmod 644 {} \\; # применить chmod\n```\n\n### grep — поиск текста:\n```bash\ngrep \"error\" /var/log/syslog       # найти строку в файле\ngrep -r \"TODO\" /home/user/project  # рекурсивно\ngrep -i \"error\" file.txt           # без учёта регистра\ngrep -n \"pattern\" file.txt         # показать номера строк\ngrep -c \"error\" log.txt            # подсчитать совпадения\ngrep -v \"debug\" log.txt            # исключить строки\n```\n\n### Комбинирование:\n```bash\n# Найти все .py файлы, содержащие \"import os\"\nfind . -name \"*.py\" -exec grep -l \"import os\" {} \\;\n\n# Или с помощью pipe:\ngrep -rl \"import os\" --include=\"*.py\" .\n```"},
                    {"type": "terminal-sim", "prompt": "Найдите все файлы с расширением .log в директории /var/log:", "expectedCommand": "find /var/log -name \"*.log\"", "hint": "Используйте find с флагом -name и шаблон в кавычках"},
                    {"type": "terminal-sim", "prompt": "Найдите строки со словом error в файле /var/log/syslog (без учёта регистра):", "expectedCommand": "grep -i \"error\" /var/log/syslog", "hint": "Используйте grep с флагом -i"},
                    {"type": "quiz", "question": "Какой флаг grep выполняет рекурсивный поиск?", "options": [{"id": "a", "text": "-i", "correct": False}, {"id": "b", "text": "-r", "correct": True}, {"id": "c", "text": "-n", "correct": False}, {"id": "d", "text": "-v", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "grep -i", "right": "Без учёта регистра"}, {"left": "grep -r", "right": "Рекурсивный поиск"}, {"left": "grep -n", "right": "Показать номера строк"}, {"left": "grep -v", "right": "Исключить совпадения"}]},
                ],
            },
        ],
    },
    # ===== SECTION 3: Пользователи и права =====
    {
        "title": "Пользователи и права",
        "pos": 2,
        "lessons": [
            {
                "t": "Управление пользователями",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "useradd, userdel, usermod", "markdown": "## Управление пользователями\n\n### Создание пользователя:\n```bash\nsudo useradd -m -s /bin/bash newuser   # создать с домашней и shell\nsudo useradd -m -G sudo,docker newuser # создать + добавить в группы\n```\n\n### Удаление пользователя:\n```bash\nsudo userdel newuser           # удалить (без домашней)\nsudo userdel -r newuser        # удалить + домашнюю директорию\n```\n\n### Изменение пользователя:\n```bash\nsudo usermod -aG docker user   # добавить в группу docker\nsudo usermod -l newname old    # переименовать\nsudo usermod -s /bin/zsh user  # сменить shell\n```\n\n### Информация:\n```bash\nid                   # UID, GID, группы текущего пользователя\nid username          # информация о другом пользователе\nwho                  # кто сейчас в системе\nw                    # подробнее: кто и что делает\ncat /etc/passwd      # список всех пользователей\n```\n\n### Файлы:\n- `/etc/passwd` — список пользователей\n- `/etc/shadow` — хеши паролей (только root)\n- `/etc/group` — список групп"},
                    {"type": "terminal-sim", "prompt": "Создайте пользователя developer с домашней директорией и bash-оболочкой:", "expectedCommand": "sudo useradd -m -s /bin/bash developer", "hint": "useradd -m для домашней, -s для shell"},
                    {"type": "quiz", "question": "Где хранятся хеши паролей пользователей Linux?", "options": [{"id": "a", "text": "/etc/passwd", "correct": False}, {"id": "b", "text": "/etc/shadow", "correct": True}, {"id": "c", "text": "/etc/group", "correct": False}, {"id": "d", "text": "/home/passwords", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для добавления пользователя в существующую группу без удаления из других используется команда usermod с флагами ___.", "answer": "-aG"},
                ],
            },
            {
                "t": "Группы пользователей",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Группы в Linux", "markdown": "## Группы пользователей\n\nГруппы позволяют управлять правами доступа для нескольких пользователей.\n\n### Создание и управление группами:\n```bash\nsudo groupadd developers          # создать группу\nsudo groupdel developers          # удалить группу\nsudo gpasswd -a user developers   # добавить пользователя\nsudo gpasswd -d user developers   # удалить из группы\n```\n\n### Просмотр групп:\n```bash\ngroups                  # группы текущего пользователя\ngroups username         # группы другого пользователя\ncat /etc/group          # все группы системы\ngetent group developers # информация о конкретной группе\n```\n\n### Основная и дополнительная группа:\n```bash\n# Основная группа (primary) — создаётся при useradd\n# Дополнительные (supplementary) — добавляются через usermod\n\nsudo usermod -g developers user    # сменить основную группу\nsudo usermod -aG docker,sudo user  # добавить дополнительные\n```\n\n### Совместная работа:\n```bash\n# Создать общую папку для группы\nsudo mkdir /opt/project\nsudo chown :developers /opt/project\nsudo chmod 775 /opt/project\n```"},
                    {"type": "terminal-sim", "prompt": "Создайте группу devops:", "expectedCommand": "sudo groupadd devops", "hint": "groupadd для создания группы"},
                    {"type": "quiz", "question": "Какой командой добавить пользователя в группу без удаления из других?", "options": [{"id": "a", "text": "sudo usermod -aG group user", "correct": True}, {"id": "b", "text": "sudo usermod -G group user", "correct": False}, {"id": "c", "text": "sudo groupadd user group", "correct": False}, {"id": "d", "text": "sudo addgroup user", "correct": False}]},
                    {"type": "true-false", "statement": "Флаг -a в команде usermod -aG означает 'append' — добавить, не удаляя из существующих групп.", "correct": True},
                ],
            },
            {
                "t": "Sudo и привилегии",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Sudo — суперсила пользователя", "markdown": "## Sudo\n\n**sudo** (Super User DO) — выполнение команд от имени root.\n\n### Использование:\n```bash\nsudo apt update               # одна команда от root\nsudo -i                       # открыть root-сессию\nsudo su                       # переключиться на root\nsudo -u www-data whoami       # от имени другого пользователя\n```\n\n### Конфигурация — /etc/sudoers:\n```bash\nsudo visudo                   # безопасное редактирование\n\n# Формат:\n# user HOST=(RUNAS) COMMANDS\nuser ALL=(ALL:ALL) ALL         # полный доступ\n%sudo ALL=(ALL:ALL) ALL        # группа sudo — полный доступ\nuser ALL=(ALL) NOPASSWD: ALL   # без пароля (опасно!)\nuser ALL=(ALL) /usr/bin/apt    # только apt\n```\n\n### Проверка:\n```bash\nsudo -l                 # какие команды доступны текущему пользователю\nsudo -l -U username     # какие команды доступны другому пользователю\n```\n\n### Безопасность:\n- Не работайте постоянно под root!\n- Используйте `sudo` только когда нужно\n- Логи sudo: `/var/log/auth.log`"},
                    {"type": "quiz", "question": "Какой командой безопасно редактировать файл /etc/sudoers?", "options": [{"id": "a", "text": "nano /etc/sudoers", "correct": False}, {"id": "b", "text": "sudo visudo", "correct": True}, {"id": "c", "text": "sudo vim /etc/sudoers", "correct": False}, {"id": "d", "text": "chmod 777 /etc/sudoers", "correct": False}]},
                    {"type": "terminal-sim", "prompt": "Проверьте, какие sudo-команды доступны текущему пользователю:", "expectedCommand": "sudo -l", "hint": "sudo с флагом -l (list)"},
                    {"type": "true-false", "statement": "Работать постоянно под root-пользователем — хорошая практика для удобства.", "correct": False},
                    {"type": "fill-blank", "sentence": "Логи sudo-команд записываются в файл /var/log/___.", "answer": "auth.log"},
                ],
            },
            {
                "t": "Пароли и passwd",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Управление паролями", "markdown": "## Управление паролями\n\n### Установка и смена пароля:\n```bash\npasswd                      # сменить свой пароль\nsudo passwd username         # сменить пароль другому пользователю\nsudo passwd -l username      # заблокировать аккаунт\nsudo passwd -u username      # разблокировать аккаунт\nsudo passwd -e username      # заставить сменить пароль при входе\n```\n\n### Политика паролей:\n```bash\nsudo chage -l username           # информация о паролях\nsudo chage -M 90 username        # макс. возраст: 90 дней\nsudo chage -m 7 username         # мин. возраст: 7 дней\nsudo chage -W 14 username        # предупреждение за 14 дней\n```\n\n### Файл /etc/shadow:\n```\nuser:$6$salt$hash:18000:0:99999:7:::\n│     │              │    │  │    │\n│     │              │    │  │    └── предупреждение\n│     │              │    │  └── максимальный возраст\n│     │              │    └── минимальный возраст\n│     │              └── дата последней смены\n│     └── хеш пароля\n└── имя пользователя\n```"},
                    {"type": "terminal-sim", "prompt": "Принудительно заставьте пользователя admin сменить пароль при следующем входе:", "expectedCommand": "sudo passwd -e admin", "hint": "passwd с флагом -e (expire)"},
                    {"type": "quiz", "question": "Что делает команда sudo passwd -l username?", "options": [{"id": "a", "text": "Показывает список паролей", "correct": False}, {"id": "b", "text": "Блокирует аккаунт пользователя", "correct": True}, {"id": "c", "text": "Меняет пароль", "correct": False}, {"id": "d", "text": "Удаляет пользователя", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "passwd -l", "right": "Заблокировать аккаунт"}, {"left": "passwd -u", "right": "Разблокировать аккаунт"}, {"left": "passwd -e", "right": "Заставить сменить пароль"}, {"left": "chage -M 90", "right": "Максимальный возраст пароля 90 дней"}]},
                ],
            },
            {
                "t": "ACL — расширенные права",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Access Control Lists", "markdown": "## ACL — расширенные права доступа\n\nСтандартные права (ugo) ограничены. ACL позволяет задавать права для конкретных пользователей и групп.\n\n### Установка ACL:\n```bash\nsudo apt install acl\n```\n\n### Назначение прав:\n```bash\n# Дать пользователю alice права на чтение и запись:\nsetfacl -m u:alice:rw file.txt\n\n# Дать группе devs права на чтение:\nsetfacl -m g:devs:r file.txt\n\n# Рекурсивно для директории:\nsetfacl -R -m u:alice:rwx /opt/project/\n\n# ACL по умолчанию (для новых файлов):\nsetfacl -d -m u:alice:rw /opt/project/\n```\n\n### Просмотр ACL:\n```bash\ngetfacl file.txt\n# file: file.txt\n# owner: user\n# group: group\n# user::rw-\n# user:alice:rw-\n# group::r--\n# group:devs:r--\n# mask::rw-\n# other::r--\n```\n\n### Удаление ACL:\n```bash\nsetfacl -x u:alice file.txt      # убрать ACL для alice\nsetfacl -b file.txt              # убрать все ACL\n```"},
                    {"type": "terminal-sim", "prompt": "Дайте пользователю alice права на чтение и запись файла report.txt через ACL:", "expectedCommand": "setfacl -m u:alice:rw report.txt", "hint": "setfacl -m u:пользователь:права файл"},
                    {"type": "quiz", "question": "Какой командой можно просмотреть ACL файла?", "options": [{"id": "a", "text": "ls -l", "correct": False}, {"id": "b", "text": "getfacl", "correct": True}, {"id": "c", "text": "chmod --acl", "correct": False}, {"id": "d", "text": "cat /etc/acl", "correct": False}]},
                    {"type": "true-false", "statement": "ACL позволяет назначить разные права доступа нескольким конкретным пользователям к одному файлу.", "correct": True},
                ],
            },
        ],
    },
    # ===== SECTION 4: Процессы и сервисы =====
    {
        "title": "Процессы и сервисы",
        "pos": 3,
        "lessons": [
            {
                "t": "Процессы: ps, top, htop",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Мониторинг процессов", "markdown": "## Процессы в Linux\n\nКаждая запущенная программа — это процесс с уникальным PID.\n\n### ps — снимок процессов:\n```bash\nps                      # процессы текущего терминала\nps aux                  # все процессы системы\nps aux | grep nginx     # найти процессы nginx\nps -ef --forest         # дерево процессов\n```\n\n### Столбцы ps aux:\n```\nUSER  PID  %CPU  %MEM  VSZ  RSS  TTY  STAT  START  TIME  COMMAND\nroot   1   0.0   0.1  168  11232  ?   Ss    Mar01  0:05  /sbin/init\n```\n\n### top — интерактивный мониторинг:\n```bash\ntop                     # запустить\n# Внутри top:\n# P — сортировка по CPU\n# M — сортировка по памяти\n# k — убить процесс\n# q — выйти\n```\n\n### htop — улучшенный top:\n```bash\nsudo apt install htop\nhtop                    # красивый интерактивный мониторинг\n```\n\n### Другие утилиты:\n```bash\npgrep nginx             # найти PID по имени\npidof nginx             # PID программы\n```"},
                    {"type": "terminal-sim", "prompt": "Покажите все процессы системы в подробном формате:", "expectedCommand": "ps aux", "hint": "ps с флагами a (все), u (подробно), x (без терминала)"},
                    {"type": "quiz", "question": "Какая клавиша в top сортирует процессы по использованию памяти?", "options": [{"id": "a", "text": "P", "correct": False}, {"id": "b", "text": "M", "correct": True}, {"id": "c", "text": "K", "correct": False}, {"id": "d", "text": "Q", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "ps aux", "right": "Снимок всех процессов"}, {"left": "top", "right": "Интерактивный мониторинг"}, {"left": "htop", "right": "Улучшенный мониторинг с цветами"}, {"left": "pgrep", "right": "Поиск PID по имени процесса"}]},
                ],
            },
            {
                "t": "Управление процессами: kill, signals",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Сигналы и kill", "markdown": "## Управление процессами\n\n### Сигналы:\n| Сигнал | Номер | Действие |\n|--------|-------|----------|\n| SIGHUP | 1 | Перезагрузить конфигурацию |\n| SIGINT | 2 | Прервать (Ctrl+C) |\n| SIGKILL | 9 | Принудительно убить |\n| SIGTERM | 15 | Корректно завершить (по умолчанию) |\n| SIGSTOP | 19 | Приостановить |\n\n### Отправка сигналов:\n```bash\nkill PID                  # SIGTERM (мягкое завершение)\nkill -9 PID               # SIGKILL (принудительно)\nkill -HUP PID             # перезагрузить конфигурацию\nkillall nginx             # убить все процессы nginx\npkill -f \"python app.py\"  # убить по шаблону команды\n```\n\n### Фоновые процессы:\n```bash\nlong_command &            # запустить в фоне\njobs                      # список фоновых задач\nfg %1                     # вернуть задачу №1 на передний план\nbg %1                     # продолжить задачу в фоне\nCtrl+Z                    # приостановить текущий процесс\n```\n\n### nohup — процесс продолжит работу после выхода:\n```bash\nnohup ./script.sh &\n```"},
                    {"type": "quiz", "question": "Какой сигнал нельзя перехватить или игнорировать?", "options": [{"id": "a", "text": "SIGTERM (15)", "correct": False}, {"id": "b", "text": "SIGKILL (9)", "correct": True}, {"id": "c", "text": "SIGHUP (1)", "correct": False}, {"id": "d", "text": "SIGINT (2)", "correct": False}]},
                    {"type": "terminal-sim", "prompt": "Принудительно завершите процесс с PID 1234:", "expectedCommand": "kill -9 1234", "hint": "kill с сигналом 9 (SIGKILL)"},
                    {"type": "drag-order", "items": ["Найти PID процесса (ps aux | grep name)", "Попробовать kill PID (SIGTERM)", "Подождать завершения", "Если не завершился — kill -9 PID (SIGKILL)", "Убедиться, что процесс завершён (ps aux | grep PID)"]},
                    {"type": "fill-blank", "sentence": "Сигнал SIGTERM имеет номер ___ и используется для корректного завершения процесса.", "answer": "15"},
                ],
            },
            {
                "t": "Systemd и управление сервисами",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Systemd — менеджер системы", "markdown": "## Systemd\n\n**systemd** — система инициализации и менеджер сервисов в современных Linux.\n\n### systemctl — управление сервисами:\n```bash\nsudo systemctl start nginx       # запустить\nsudo systemctl stop nginx        # остановить\nsudo systemctl restart nginx     # перезапустить\nsudo systemctl reload nginx      # перезагрузить конфигурацию\nsudo systemctl status nginx      # статус\n```\n\n### Автозагрузка:\n```bash\nsudo systemctl enable nginx      # включить автозапуск\nsudo systemctl disable nginx     # отключить автозапуск\nsudo systemctl is-enabled nginx  # проверить\n```\n\n### Просмотр сервисов:\n```bash\nsystemctl list-units --type=service              # активные\nsystemctl list-units --type=service --all         # все\nsystemctl list-unit-files --type=service          # все файлы юнитов\n```\n\n### Unit-файл (пример):\n```ini\n# /etc/systemd/system/myapp.service\n[Unit]\nDescription=My Application\nAfter=network.target\n\n[Service]\nType=simple\nUser=www-data\nExecStart=/usr/bin/python3 /opt/myapp/app.py\nRestart=always\n\n[Install]\nWantedBy=multi-user.target\n```"},
                    {"type": "terminal-sim", "prompt": "Проверьте статус сервиса nginx:", "expectedCommand": "sudo systemctl status nginx", "hint": "systemctl status имя_сервиса"},
                    {"type": "code-puzzle", "instructions": "Соберите команду для включения автозапуска сервиса postgresql:", "correctOrder": ["sudo", "systemctl", "enable", "postgresql"]},
                    {"type": "quiz", "question": "Какая секция unit-файла отвечает за автозагрузку?", "options": [{"id": "a", "text": "[Unit]", "correct": False}, {"id": "b", "text": "[Service]", "correct": False}, {"id": "c", "text": "[Install]", "correct": True}, {"id": "d", "text": "[Boot]", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "systemctl start", "right": "Запустить сервис"}, {"left": "systemctl enable", "right": "Включить автозапуск"}, {"left": "systemctl status", "right": "Проверить состояние"}, {"left": "systemctl reload", "right": "Перезагрузить конфигурацию"}]},
                ],
            },
            {
                "t": "Планировщик задач: cron",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Cron — планировщик задач", "markdown": "## Cron\n\n**cron** — демон для запуска задач по расписанию.\n\n### Формат crontab:\n```\n* * * * * команда\n│ │ │ │ │\n│ │ │ │ └── день недели (0-7, 0 и 7 = воскресенье)\n│ │ │ └── месяц (1-12)\n│ │ └── день месяца (1-31)\n│ └── час (0-23)\n└── минута (0-59)\n```\n\n### Управление crontab:\n```bash\ncrontab -e            # редактировать свои задачи\ncrontab -l            # показать свои задачи\ncrontab -r            # удалить все задачи\nsudo crontab -u user -l  # задачи другого пользователя\n```\n\n### Примеры:\n```bash\n# Каждые 5 минут\n*/5 * * * * /opt/scripts/check.sh\n\n# Каждый день в 3:00\n0 3 * * * /opt/scripts/backup.sh\n\n# Каждый понедельник в 9:00\n0 9 * * 1 /opt/scripts/report.sh\n\n# 1-го числа каждого месяца в полночь\n0 0 1 * * /opt/scripts/monthly.sh\n```\n\n### Логирование:\n```bash\n# Перенаправить вывод в лог:\n0 3 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1\n```"},
                    {"type": "terminal-sim", "prompt": "Откройте crontab для редактирования:", "expectedCommand": "crontab -e", "hint": "crontab с флагом -e (edit)"},
                    {"type": "fill-blank", "sentence": "Запись cron '0 3 * * *' означает запуск задачи каждый день в ___ часа ночи.", "answer": "3"},
                    {"type": "quiz", "question": "Что означает */5 в поле минут crontab?", "options": [{"id": "a", "text": "Каждые 5 минут", "correct": True}, {"id": "b", "text": "5-я минута каждого часа", "correct": False}, {"id": "c", "text": "Каждые 5 часов", "correct": False}, {"id": "d", "text": "5-й день", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "0 3 * * *", "right": "Каждый день в 3:00"}, {"left": "*/5 * * * *", "right": "Каждые 5 минут"}, {"left": "0 9 * * 1", "right": "Каждый понедельник в 9:00"}, {"left": "0 0 1 * *", "right": "1-го числа каждого месяца"}]},
                ],
            },
            {
                "t": "Journalctl и логи systemd",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Журнал systemd", "markdown": "## Journalctl\n\n**journalctl** — утилита для просмотра логов systemd.\n\n### Основные команды:\n```bash\njournalctl                       # все логи\njournalctl -b                    # логи с последней загрузки\njournalctl -b -1                 # логи с предыдущей загрузки\njournalctl -f                    # follow (как tail -f)\njournalctl --since \"1 hour ago\"  # за последний час\njournalctl --since \"2024-01-01\" --until \"2024-01-02\"\n```\n\n### Фильтрация по сервису:\n```bash\njournalctl -u nginx              # логи nginx\njournalctl -u nginx --since today # логи nginx за сегодня\njournalctl -u nginx -f           # follow логов nginx\n```\n\n### Фильтрация по приоритету:\n```bash\njournalctl -p err                # только ошибки и выше\njournalctl -p warning            # предупреждения и выше\n# Уровни: emerg, alert, crit, err, warning, notice, info, debug\n```\n\n### Обслуживание:\n```bash\njournalctl --disk-usage          # сколько места занимают логи\nsudo journalctl --vacuum-size=500M  # ограничить до 500MB\nsudo journalctl --vacuum-time=2weeks # удалить старше 2 недель\n```"},
                    {"type": "terminal-sim", "prompt": "Просмотрите логи сервиса nginx в режиме реального времени:", "expectedCommand": "journalctl -u nginx -f", "hint": "journalctl -u для сервиса, -f для follow"},
                    {"type": "quiz", "question": "Какой флаг journalctl показывает только ошибки?", "options": [{"id": "a", "text": "-u err", "correct": False}, {"id": "b", "text": "-p err", "correct": True}, {"id": "c", "text": "-e", "correct": False}, {"id": "d", "text": "--errors", "correct": False}]},
                    {"type": "drag-order", "items": ["journalctl -u service — логи конкретного сервиса", "journalctl -p err — фильтр по ошибкам", "journalctl --since '1 hour ago' — за последний час", "journalctl --vacuum-size=500M — очистка логов"]},
                ],
            },
            {
                "t": "Демоны и фоновые процессы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Демоны в Linux", "markdown": "## Демоны (daemons)\n\n**Демон** — фоновый процесс, работающий без прямого взаимодействия с пользователем.\n\n### Признаки демонов:\n- Имя заканчивается на **d**: sshd, httpd, crond, systemd\n- Работают в фоне\n- Запускаются при загрузке системы\n- Управляются через systemctl\n\n### Основные системные демоны:\n```bash\nsystemd (PID 1)    # менеджер системы\nsshd               # SSH-сервер\ncrond              # планировщик задач\nrsyslogd           # системные логи\nnetworkd           # управление сетью\n```\n\n### Создание своего демона:\n```ini\n# /etc/systemd/system/mybot.service\n[Unit]\nDescription=My Telegram Bot\nAfter=network.target\n\n[Service]\nType=simple\nUser=botuser\nWorkingDirectory=/opt/mybot\nExecStart=/usr/bin/python3 bot.py\nRestart=on-failure\nRestartSec=5\n\n[Install]\nWantedBy=multi-user.target\n```\n\n### Активация:\n```bash\nsudo systemctl daemon-reload     # перечитать unit-файлы\nsudo systemctl enable --now mybot # включить + запустить\n```"},
                    {"type": "terminal-sim", "prompt": "Перезагрузите конфигурацию systemd после создания нового unit-файла:", "expectedCommand": "sudo systemctl daemon-reload", "hint": "systemctl daemon-reload"},
                    {"type": "true-false", "statement": "Имена демонов в Linux обычно заканчиваются на букву 'd' (sshd, crond, httpd).", "correct": True},
                    {"type": "quiz", "question": "Какой PID всегда имеет процесс systemd?", "options": [{"id": "a", "text": "0", "correct": False}, {"id": "b", "text": "1", "correct": True}, {"id": "c", "text": "100", "correct": False}, {"id": "d", "text": "Случайный", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Для перезагрузки unit-файлов systemd используется команда sudo systemctl ___.", "answer": "daemon-reload"},
                ],
            },
        ],
    },
    # ===== SECTION 5: Сети =====
    {
        "title": "Сети",
        "pos": 4,
        "lessons": [
            {
                "t": "Сетевые интерфейсы: ip и ifconfig",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Настройка сети", "markdown": "## Сетевые интерфейсы\n\n### ip — современная утилита:\n```bash\nip addr show               # все интерфейсы и адреса\nip addr show eth0          # конкретный интерфейс\nip link show               # состояние интерфейсов\nip route show              # таблица маршрутизации\n```\n\n### Настройка (временная):\n```bash\nsudo ip addr add 192.168.1.100/24 dev eth0  # добавить IP\nsudo ip addr del 192.168.1.100/24 dev eth0  # удалить IP\nsudo ip link set eth0 up                     # включить\nsudo ip link set eth0 down                   # выключить\n```\n\n### ifconfig (устаревшая, но часто используется):\n```bash\nifconfig                   # все интерфейсы\nifconfig eth0              # конкретный интерфейс\n```\n\n### Другие полезные команды:\n```bash\nhostname -I                # все IP-адреса хоста\ncurl ifconfig.me           # внешний IP\nping -c 4 google.com       # проверка соединения\ntraceroute google.com      # маршрут до хоста\n```\n\n### Постоянная конфигурация (Netplan — Ubuntu):\n```yaml\n# /etc/netplan/01-config.yaml\nnetwork:\n  ethernets:\n    eth0:\n      addresses: [192.168.1.100/24]\n      gateway4: 192.168.1.1\n      nameservers:\n        addresses: [8.8.8.8, 8.8.4.4]\n```"},
                    {"type": "terminal-sim", "prompt": "Просмотрите все сетевые интерфейсы и их IP-адреса:", "expectedCommand": "ip addr show", "hint": "ip addr show — показать адреса интерфейсов"},
                    {"type": "quiz", "question": "Какая команда пришла на замену ifconfig в современных Linux?", "options": [{"id": "a", "text": "netstat", "correct": False}, {"id": "b", "text": "ip", "correct": True}, {"id": "c", "text": "nmcli", "correct": False}, {"id": "d", "text": "iwconfig", "correct": False}]},
                    {"type": "true-false", "statement": "Команда ifconfig считается устаревшей и заменена утилитой ip.", "correct": True},
                    {"type": "matching", "pairs": [{"left": "ip addr show", "right": "Показать IP-адреса"}, {"left": "ip route show", "right": "Таблица маршрутизации"}, {"left": "ip link show", "right": "Состояние интерфейсов"}, {"left": "ping", "right": "Проверка соединения"}]},
                ],
            },
            {
                "t": "SSH — удалённый доступ",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "SSH — Secure Shell", "markdown": "## SSH — безопасное подключение\n\n### Подключение:\n```bash\nssh user@server_ip               # по паролю\nssh -p 2222 user@server_ip       # нестандартный порт\nssh -i ~/.ssh/mykey user@server  # по ключу\n```\n\n### SSH-ключи (рекомендуется!):\n```bash\n# 1. Генерация ключевой пары:\nssh-keygen -t ed25519 -C \"my@email.com\"\n# Создаст: ~/.ssh/id_ed25519 (приватный) и id_ed25519.pub (публичный)\n\n# 2. Копирование публичного ключа на сервер:\nssh-copy-id user@server_ip\n# Или вручную: добавить содержимое .pub в ~/.ssh/authorized_keys\n```\n\n### Конфигурация ~/.ssh/config:\n```\nHost myserver\n    HostName 192.168.1.100\n    User admin\n    Port 22\n    IdentityFile ~/.ssh/id_ed25519\n```\nПосле этого: `ssh myserver`\n\n### Безопасность (/etc/ssh/sshd_config):\n```bash\nPermitRootLogin no           # запретить вход root\nPasswordAuthentication no     # только ключи\nPort 2222                    # сменить порт\n```\n\n```bash\nsudo systemctl restart sshd  # применить изменения\n```"},
                    {"type": "terminal-sim", "prompt": "Сгенерируйте SSH-ключ типа ed25519:", "expectedCommand": "ssh-keygen -t ed25519", "hint": "ssh-keygen с типом ed25519"},
                    {"type": "drag-order", "items": ["Сгенерировать ключевую пару (ssh-keygen)", "Скопировать публичный ключ на сервер (ssh-copy-id)", "Подключиться по ключу (ssh user@server)", "Отключить вход по паролю (PasswordAuthentication no)", "Перезапустить sshd (systemctl restart sshd)"]},
                    {"type": "quiz", "question": "Какую настройку sshd_config нужно задать для запрета входа root?", "options": [{"id": "a", "text": "PermitRootLogin no", "correct": True}, {"id": "b", "text": "DenyRoot yes", "correct": False}, {"id": "c", "text": "RootLogin false", "correct": False}, {"id": "d", "text": "AllowRoot no", "correct": False}]},
                    {"type": "true-false", "statement": "SSH-ключи безопаснее паролей, потому что приватный ключ никогда не передаётся по сети.", "correct": True},
                ],
            },
            {
                "t": "SCP и передача файлов",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Копирование файлов по сети", "markdown": "## SCP, rsync — передача файлов\n\n### scp — копирование через SSH:\n```bash\n# Скопировать файл на сервер:\nscp file.txt user@server:/home/user/\n\n# Скопировать с сервера:\nscp user@server:/var/log/app.log ./\n\n# Рекурсивно (директория):\nscp -r mydir/ user@server:/opt/\n\n# С нестандартным портом:\nscp -P 2222 file.txt user@server:/tmp/\n```\n\n### rsync — умная синхронизация:\n```bash\n# Синхронизировать директорию:\nrsync -avz ./project/ user@server:/opt/project/\n\n# Флаги:\n# -a  архивный режим (рекурсивно + права + время)\n# -v  подробный вывод\n# -z  сжатие при передаче\n# --delete  удалить лишние файлы на приёмнике\n# --dry-run  показать, что будет сделано (без выполнения)\n\nrsync -avz --delete ./project/ user@server:/opt/project/\n```\n\n### sftp — интерактивная передача:\n```bash\nsftp user@server\nsftp> put localfile.txt\nsftp> get remotefile.txt\nsftp> ls\nsftp> bye\n```"},
                    {"type": "terminal-sim", "prompt": "Скопируйте файл backup.tar.gz на сервер 10.0.0.5 в /tmp/:", "expectedCommand": "scp backup.tar.gz user@10.0.0.5:/tmp/", "hint": "scp файл user@хост:путь"},
                    {"type": "quiz", "question": "Чем rsync лучше scp?", "options": [{"id": "a", "text": "Передаёт только изменённые части файлов", "correct": True}, {"id": "b", "text": "Работает без SSH", "correct": False}, {"id": "c", "text": "Быстрее при первой передаче", "correct": False}, {"id": "d", "text": "Не требует аутентификации", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "scp", "right": "Простое копирование через SSH"}, {"left": "rsync", "right": "Умная синхронизация с diff"}, {"left": "sftp", "right": "Интерактивная передача файлов"}, {"left": "rsync --dry-run", "right": "Показать изменения без выполнения"}]},
                ],
            },
            {
                "t": "Firewall: iptables и ufw",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Межсетевой экран Linux", "markdown": "## Firewall в Linux\n\n### UFW — простой файрвол (Ubuntu):\n```bash\nsudo ufw status               # статус\nsudo ufw enable               # включить\nsudo ufw disable              # выключить\n\n# Правила:\nsudo ufw allow 22             # разрешить SSH\nsudo ufw allow 80/tcp         # разрешить HTTP\nsudo ufw allow 443/tcp        # разрешить HTTPS\nsudo ufw allow from 192.168.1.0/24  # разрешить подсеть\nsudo ufw deny 3306            # запретить MySQL извне\n\nsudo ufw delete allow 80      # удалить правило\nsudo ufw status numbered      # правила с номерами\n```\n\n### iptables — мощный, но сложный:\n```bash\n# Просмотр:\nsudo iptables -L -n -v\n\n# Разрешить SSH:\nsudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT\n\n# Запретить всё входящее:\nsudo iptables -P INPUT DROP\n\n# Разрешить уже установленные соединения:\nsudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n```\n\n### Типичная настройка сервера (UFW):\n```bash\nsudo ufw default deny incoming\nsudo ufw default allow outgoing\nsudo ufw allow 22/tcp\nsudo ufw allow 80/tcp\nsudo ufw allow 443/tcp\nsudo ufw enable\n```"},
                    {"type": "terminal-sim", "prompt": "Разрешите входящие SSH-соединения через UFW:", "expectedCommand": "sudo ufw allow 22", "hint": "ufw allow номер_порта"},
                    {"type": "drag-order", "items": ["sudo ufw default deny incoming", "sudo ufw default allow outgoing", "sudo ufw allow 22/tcp", "sudo ufw allow 80/tcp", "sudo ufw allow 443/tcp", "sudo ufw enable"]},
                    {"type": "quiz", "question": "Что делает команда sudo ufw default deny incoming?", "options": [{"id": "a", "text": "Запрещает все входящие соединения по умолчанию", "correct": True}, {"id": "b", "text": "Разрешает все входящие соединения", "correct": False}, {"id": "c", "text": "Отключает файрвол", "correct": False}, {"id": "d", "text": "Удаляет все правила", "correct": False}]},
                ],
            },
            {
                "t": "DNS и разрешение имён",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "DNS в Linux", "markdown": "## DNS — система доменных имён\n\nDNS преобразует доменные имена (google.com) в IP-адреса (142.250.74.14).\n\n### Проверка DNS:\n```bash\nnslookup google.com          # простой запрос\ndig google.com               # подробный запрос\ndig google.com +short        # только IP\ndig -x 8.8.8.8              # обратный запрос (IP → имя)\nhost google.com              # ещё одна утилита\n```\n\n### Конфигурация:\n```bash\n# DNS-серверы:\ncat /etc/resolv.conf\n# nameserver 8.8.8.8\n# nameserver 8.8.4.4\n\n# Локальные записи:\ncat /etc/hosts\n# 127.0.0.1  localhost\n# 192.168.1.10  myserver.local\n```\n\n### Порядок разрешения:\n```bash\ncat /etc/nsswitch.conf\n# hosts: files dns\n# Сначала /etc/hosts, потом DNS-сервер\n```\n\n### Типы DNS-записей:\n| Тип | Назначение |\n|-----|------------|\n| A | Имя → IPv4 |\n| AAAA | Имя → IPv6 |\n| CNAME | Алиас (псевдоним) |\n| MX | Почтовый сервер |\n| NS | DNS-сервер зоны |\n| TXT | Текстовая запись |"},
                    {"type": "terminal-sim", "prompt": "Узнайте IP-адрес домена example.com:", "expectedCommand": "dig example.com +short", "hint": "dig домен +short для краткого вывода"},
                    {"type": "matching", "pairs": [{"left": "A-запись", "right": "Доменное имя → IPv4-адрес"}, {"left": "AAAA-запись", "right": "Доменное имя → IPv6-адрес"}, {"left": "CNAME", "right": "Алиас (псевдоним домена)"}, {"left": "MX-запись", "right": "Почтовый сервер домена"}]},
                    {"type": "quiz", "question": "В каком файле задаются локальные DNS-записи?", "options": [{"id": "a", "text": "/etc/resolv.conf", "correct": False}, {"id": "b", "text": "/etc/hosts", "correct": True}, {"id": "c", "text": "/etc/dns.conf", "correct": False}, {"id": "d", "text": "/etc/hostname", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Файл ___ содержит адреса DNS-серверов в Linux.", "answer": "/etc/resolv.conf"},
                ],
            },
            {
                "t": "Порты и сокеты",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Сетевые порты и сокеты", "markdown": "## Порты и сокеты\n\n### Что такое порт?\nЛогический адрес приложения в сети. Диапазон: 0–65535.\n\n### Известные порты:\n| Порт | Сервис |\n|------|--------|\n| 22 | SSH |\n| 80 | HTTP |\n| 443 | HTTPS |\n| 3306 | MySQL |\n| 5432 | PostgreSQL |\n| 6379 | Redis |\n| 8080 | HTTP (альтернативный) |\n\n### Просмотр открытых портов:\n```bash\n# ss — современная утилита:\nss -tlnp                     # TCP, listening, numeric, processes\nss -ulnp                     # UDP, listening\n\n# netstat (устаревшая):\nnetstat -tlnp                # аналог ss\n\n# lsof — кто слушает порт:\nsudo lsof -i :80             # кто слушает порт 80\nsudo lsof -i :22             # кто слушает порт 22\n```\n\n### Проверка портов удалённого хоста:\n```bash\nnc -zv server_ip 22          # проверить порт 22\nnc -zv server_ip 80-443      # диапазон портов\nnmap server_ip               # сканирование портов\n```"},
                    {"type": "terminal-sim", "prompt": "Покажите все прослушиваемые TCP-порты и процессы:", "expectedCommand": "ss -tlnp", "hint": "ss -tlnp: TCP, listening, numeric, processes"},
                    {"type": "matching", "pairs": [{"left": "Порт 22", "right": "SSH"}, {"left": "Порт 80", "right": "HTTP"}, {"left": "Порт 443", "right": "HTTPS"}, {"left": "Порт 5432", "right": "PostgreSQL"}, {"left": "Порт 3306", "right": "MySQL"}]},
                    {"type": "quiz", "question": "Какая утилита заменила netstat в современных Linux?", "options": [{"id": "a", "text": "ss", "correct": True}, {"id": "b", "text": "ip", "correct": False}, {"id": "c", "text": "nmap", "correct": False}, {"id": "d", "text": "lsof", "correct": False}]},
                    {"type": "true-false", "statement": "Диапазон сетевых портов — от 0 до 65535.", "correct": True},
                ],
            },
        ],
    },
    # ===== SECTION 6: Bash-скрипты =====
    {
        "title": "Bash-скрипты",
        "pos": 5,
        "lessons": [
            {
                "t": "Переменные и ввод/вывод",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Переменные в Bash", "markdown": "## Переменные в Bash\n\n### Объявление:\n```bash\nname=\"Linux\"            # без пробелов вокруг =\nage=33\npath=\"/home/user\"\n```\n\n### Использование:\n```bash\necho \"Hello, $name!\"     # Hello, Linux!\necho \"Версия: ${name}_v2\" # с фигурными скобками\necho \"Путь: $path\"\n```\n\n### Ввод пользователя:\n```bash\nread -p \"Введите имя: \" username\necho \"Привет, $username!\"\n```\n\n### Переменные среды:\n```bash\necho $HOME          # домашняя директория\necho $USER          # текущий пользователь\necho $PATH          # пути поиска программ\necho $PWD           # текущая директория\necho $SHELL         # текущая оболочка\n\n# Задать переменную среды:\nexport MY_VAR=\"value\"\n```\n\n### Подстановка команд:\n```bash\ncurrent_date=$(date +%Y-%m-%d)\nfile_count=$(ls | wc -l)\necho \"Сегодня: $current_date, файлов: $file_count\"\n```\n\n### Первый скрипт:\n```bash\n#!/bin/bash\necho \"Привет из скрипта!\"\n```\n```bash\nchmod +x script.sh\n./script.sh\n```"},
                    {"type": "terminal-sim", "prompt": "Создайте переменную greeting со значением 'Привет, Linux!' и выведите её:", "expectedCommand": "greeting=\"Привет, Linux!\" && echo $greeting", "hint": "переменная=\"значение\" && echo $переменная"},
                    {"type": "code-puzzle", "instructions": "Соберите bash-скрипт, который спрашивает имя и здоровается:", "correctOrder": ["#!/bin/bash", "read -p \"Как вас зовут? \" name", "echo \"Привет, $name!\""]},
                    {"type": "fill-blank", "sentence": "Первая строка bash-скрипта (shebang) выглядит как ___.", "answer": "#!/bin/bash"},
                    {"type": "quiz", "question": "Как правильно использовать подстановку команд в Bash?", "options": [{"id": "a", "text": "$(команда)", "correct": True}, {"id": "b", "text": "{команда}", "correct": False}, {"id": "c", "text": "[команда]", "correct": False}, {"id": "d", "text": "<команда>", "correct": False}]},
                ],
            },
            {
                "t": "Условия: if/else, test",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Условные конструкции", "markdown": "## Условия в Bash\n\n### Базовый if:\n```bash\nif [ $age -gt 18 ]; then\n    echo \"Совершеннолетний\"\nelse\n    echo \"Несовершеннолетний\"\nfi\n```\n\n### Операторы сравнения:\n| Оператор | Значение |\n|----------|----------|\n| -eq | Равно |\n| -ne | Не равно |\n| -gt | Больше |\n| -lt | Меньше |\n| -ge | Больше или равно |\n| -le | Меньше или равно |\n\n### Проверка строк:\n```bash\nif [ \"$name\" = \"admin\" ]; then\n    echo \"Привет, админ!\"\nfi\n\nif [ -z \"$var\" ]; then    # строка пуста\nif [ -n \"$var\" ]; then    # строка не пуста\n```\n\n### Проверка файлов:\n```bash\nif [ -f /etc/hosts ]; then    # файл существует\nif [ -d /home/user ]; then    # директория существует\nif [ -r file.txt ]; then      # файл доступен для чтения\nif [ -w file.txt ]; then      # файл доступен для записи\nif [ -x script.sh ]; then     # файл исполняемый\n```\n\n### Логические операторы:\n```bash\nif [ $a -gt 0 ] && [ $a -lt 100 ]; then\n    echo \"От 1 до 99\"\nfi\n\nif [ $x -eq 0 ] || [ $y -eq 0 ]; then\n    echo \"Есть ноль\"\nfi\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите скрипт проверки существования файла:", "correctOrder": ["#!/bin/bash", "if [ -f /etc/nginx/nginx.conf ]; then", "    echo \"Nginx установлен\"", "else", "    echo \"Nginx не найден\"", "fi"]},
                    {"type": "matching", "pairs": [{"left": "-eq", "right": "Равно (equal)"}, {"left": "-gt", "right": "Больше (greater than)"}, {"left": "-f", "right": "Файл существует"}, {"left": "-d", "right": "Директория существует"}]},
                    {"type": "quiz", "question": "Какой оператор проверяет, что строка пуста?", "options": [{"id": "a", "text": "-n", "correct": False}, {"id": "b", "text": "-z", "correct": True}, {"id": "c", "text": "-e", "correct": False}, {"id": "d", "text": "-s", "correct": False}]},
                ],
            },
            {
                "t": "Циклы: for, while",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Циклы в Bash", "markdown": "## Циклы\n\n### for:\n```bash\n# Перебор списка:\nfor fruit in apple banana cherry; do\n    echo \"Фрукт: $fruit\"\ndone\n\n# C-style:\nfor ((i=1; i<=5; i++)); do\n    echo \"Число: $i\"\ndone\n\n# Перебор файлов:\nfor file in *.log; do\n    echo \"Обработка: $file\"\n    gzip \"$file\"\ndone\n\n# Перебор строк файла:\nwhile IFS= read -r line; do\n    echo \"Строка: $line\"\ndone < input.txt\n```\n\n### while:\n```bash\ncounter=1\nwhile [ $counter -le 10 ]; do\n    echo \"Count: $counter\"\n    ((counter++))\ndone\n```\n\n### until (пока условие ложно):\n```bash\nuntil ping -c 1 google.com &>/dev/null; do\n    echo \"Ожидание сети...\"\n    sleep 2\ndone\necho \"Сеть доступна!\"\n```\n\n### Управление:\n```bash\nbreak       # выйти из цикла\ncontinue    # перейти к следующей итерации\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите цикл, который сжимает все .log файлы:", "correctOrder": ["#!/bin/bash", "for file in *.log; do", "    gzip \"$file\"", "done"]},
                    {"type": "terminal-sim", "prompt": "Напишите однострочный цикл, выводящий числа от 1 до 5:", "expectedCommand": "for i in 1 2 3 4 5; do echo $i; done", "hint": "for i in 1 2 3 4 5; do echo $i; done"},
                    {"type": "quiz", "question": "Какой цикл выполняется, пока условие ЛОЖНО?", "options": [{"id": "a", "text": "for", "correct": False}, {"id": "b", "text": "while", "correct": False}, {"id": "c", "text": "until", "correct": True}, {"id": "d", "text": "do-while", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Команда ___ прерывает выполнение цикла в Bash.", "answer": "break"},
                ],
            },
            {
                "t": "Функции в Bash",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Функции", "markdown": "## Функции в Bash\n\n### Объявление:\n```bash\n# Способ 1:\nfunction greet {\n    echo \"Привет, $1!\"\n}\n\n# Способ 2 (POSIX):\ngreet() {\n    echo \"Привет, $1!\"\n}\n```\n\n### Аргументы:\n```bash\nbackup() {\n    local src=$1      # первый аргумент\n    local dest=$2     # второй аргумент\n    echo \"Копирование $src → $dest\"\n    cp -r \"$src\" \"$dest\"\n}\n\nbackup /var/www /backup/www_$(date +%Y%m%d)\n```\n\n### Возвращаемое значение:\n```bash\nis_root() {\n    if [ \"$(id -u)\" -eq 0 ]; then\n        return 0    # true (успех)\n    else\n        return 1    # false (ошибка)\n    fi\n}\n\nif is_root; then\n    echo \"Вы root!\"\nfi\n```\n\n### Специальные переменные:\n| Переменная | Значение |\n|-----------|----------|\n| $0 | Имя скрипта |\n| $1, $2... | Аргументы |\n| $# | Количество аргументов |\n| $@ | Все аргументы |\n| $? | Код возврата последней команды |\n| $$ | PID текущего скрипта |"},
                    {"type": "code-puzzle", "instructions": "Соберите функцию, которая проверяет наличие команды:", "correctOrder": ["check_command() {", "    if command -v $1 &>/dev/null; then", "        echo \"$1 установлен\"", "    else", "        echo \"$1 не найден\"", "    fi", "}"]},
                    {"type": "matching", "pairs": [{"left": "$0", "right": "Имя скрипта"}, {"left": "$1", "right": "Первый аргумент"}, {"left": "$#", "right": "Количество аргументов"}, {"left": "$?", "right": "Код возврата последней команды"}]},
                    {"type": "quiz", "question": "Какое ключевое слово делает переменную локальной внутри функции?", "options": [{"id": "a", "text": "var", "correct": False}, {"id": "b", "text": "let", "correct": False}, {"id": "c", "text": "local", "correct": True}, {"id": "d", "text": "private", "correct": False}]},
                    {"type": "fill-blank", "sentence": "Код возврата 0 в Bash означает ___ (успех/ошибку).", "answer": "успех"},
                ],
            },
            {
                "t": "Автоматизация с Bash",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Практические скрипты", "markdown": "## Автоматизация\n\n### Скрипт бэкапа:\n```bash\n#!/bin/bash\nBACKUP_DIR=\"/backup\"\nSOURCE=\"/var/www\"\nDATE=$(date +%Y%m%d_%H%M%S)\nARCHIVE=\"${BACKUP_DIR}/www_${DATE}.tar.gz\"\n\nmkdir -p \"$BACKUP_DIR\"\ntar -czf \"$ARCHIVE\" \"$SOURCE\"\necho \"Бэкап создан: $ARCHIVE\"\n\n# Удалить бэкапы старше 30 дней:\nfind \"$BACKUP_DIR\" -name \"*.tar.gz\" -mtime +30 -delete\n```\n\n### Мониторинг диска:\n```bash\n#!/bin/bash\nTHRESHOLD=80\nUSAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')\n\nif [ $USAGE -gt $THRESHOLD ]; then\n    echo \"ВНИМАНИЕ: Диск заполнен на ${USAGE}%!\" | \\\n    mail -s \"Disk Alert\" admin@example.com\nfi\n```\n\n### Массовое переименование:\n```bash\n#!/bin/bash\nfor file in *.jpg; do\n    new_name=\"photo_$(date +%s)_${file}\"\n    mv \"$file\" \"$new_name\"\n    echo \"$file → $new_name\"\ndone\n```\n\n### Pipe и перенаправление:\n```bash\ncommand > file.txt      # перезаписать\ncommand >> file.txt     # дописать\ncommand 2>&1            # stderr → stdout\ncommand1 | command2     # pipe\ncommand < input.txt     # stdin из файла\n```"},
                    {"type": "code-puzzle", "instructions": "Соберите скрипт автоматического бэкапа:", "correctOrder": ["#!/bin/bash", "DATE=$(date +%Y%m%d)", "tar -czf /backup/site_${DATE}.tar.gz /var/www", "find /backup -name '*.tar.gz' -mtime +30 -delete", "echo \"Бэкап завершён\""]},
                    {"type": "quiz", "question": "Что делает оператор >> в Bash?", "options": [{"id": "a", "text": "Перезаписывает файл", "correct": False}, {"id": "b", "text": "Дописывает в конец файла", "correct": True}, {"id": "c", "text": "Читает из файла", "correct": False}, {"id": "d", "text": "Создаёт pipe", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": ">", "right": "Перезаписать файл"}, {"left": ">>", "right": "Дописать в конец файла"}, {"left": "|", "right": "Pipe — передать вывод следующей команде"}, {"left": "2>&1", "right": "Перенаправить stderr в stdout"}]},
                    {"type": "terminal-sim", "prompt": "Создайте архив site.tar.gz из директории /var/www:", "expectedCommand": "tar -czf site.tar.gz /var/www", "hint": "tar -czf имя_архива источник"},
                ],
            },
        ],
    },
    # ===== SECTION 7: Серверное администрирование =====
    {
        "title": "Серверное администрирование",
        "pos": 6,
        "lessons": [
            {
                "t": "Nginx — веб-сервер",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Nginx — HTTP-сервер и прокси", "markdown": "## Nginx\n\n### Установка:\n```bash\nsudo apt install nginx\nsudo systemctl enable --now nginx\n```\n\n### Основные файлы:\n```\n/etc/nginx/nginx.conf              # главный конфиг\n/etc/nginx/sites-available/        # доступные сайты\n/etc/nginx/sites-enabled/          # включённые сайты\n/var/log/nginx/access.log          # логи доступа\n/var/log/nginx/error.log           # логи ошибок\n/var/www/html/                     # корень сайта по умолчанию\n```\n\n### Конфигурация виртуального хоста:\n```nginx\nserver {\n    listen 80;\n    server_name example.com;\n    root /var/www/example;\n    index index.html;\n\n    location / {\n        try_files $uri $uri/ =404;\n    }\n\n    location /api/ {\n        proxy_pass http://localhost:8000;\n        proxy_set_header Host $host;\n    }\n}\n```\n\n### Управление:\n```bash\nsudo nginx -t                      # проверить конфиг\nsudo systemctl reload nginx        # применить изменения\nsudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/\n```"},
                    {"type": "terminal-sim", "prompt": "Проверьте синтаксис конфигурации Nginx:", "expectedCommand": "sudo nginx -t", "hint": "nginx -t для тестирования конфигурации"},
                    {"type": "quiz", "question": "Где хранятся логи ошибок Nginx по умолчанию?", "options": [{"id": "a", "text": "/var/log/nginx/error.log", "correct": True}, {"id": "b", "text": "/etc/nginx/error.log", "correct": False}, {"id": "c", "text": "/var/www/error.log", "correct": False}, {"id": "d", "text": "/tmp/nginx_error.log", "correct": False}]},
                    {"type": "drag-order", "items": ["Установить Nginx (apt install nginx)", "Создать конфиг в sites-available", "Создать симлинк в sites-enabled", "Проверить конфиг (nginx -t)", "Перезагрузить Nginx (systemctl reload nginx)"]},
                    {"type": "matching", "pairs": [{"left": "listen 80", "right": "Слушать HTTP-порт"}, {"left": "server_name", "right": "Доменное имя сайта"}, {"left": "proxy_pass", "right": "Проксирование запросов на бэкенд"}, {"left": "try_files", "right": "Поиск файлов по порядку"}]},
                ],
            },
            {
                "t": "Логи и их анализ",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Работа с логами", "markdown": "## Логи Linux\n\n### Основные лог-файлы:\n```\n/var/log/syslog        # системные сообщения (Ubuntu)\n/var/log/messages      # системные сообщения (CentOS)\n/var/log/auth.log      # аутентификация, sudo\n/var/log/kern.log      # сообщения ядра\n/var/log/dmesg         # загрузка системы\n/var/log/nginx/        # логи Nginx\n/var/log/apache2/      # логи Apache\n```\n\n### Просмотр логов:\n```bash\ntail -f /var/log/syslog          # в реальном времени\ntail -n 100 /var/log/auth.log    # последние 100 строк\nless /var/log/syslog             # постранично\ngrep \"error\" /var/log/syslog     # поиск ошибок\nawk '{print $1, $2, $3}' /var/log/syslog  # извлечь дату\n```\n\n### Анализ:\n```bash\n# Топ-10 IP по запросам к Nginx:\nawk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10\n\n# Количество ошибок 404:\ngrep \" 404 \" /var/log/nginx/access.log | wc -l\n\n# Последние неудачные входы по SSH:\ngrep \"Failed password\" /var/log/auth.log | tail -20\n```\n\n### Ротация логов (logrotate):\n```bash\ncat /etc/logrotate.d/nginx\n# /var/log/nginx/*.log {\n#     weekly\n#     rotate 52\n#     compress\n#     missingok\n# }\n```"},
                    {"type": "terminal-sim", "prompt": "Просмотрите системный лог в реальном времени:", "expectedCommand": "tail -f /var/log/syslog", "hint": "tail -f для отслеживания файла"},
                    {"type": "quiz", "question": "Какой файл содержит логи аутентификации в Ubuntu?", "options": [{"id": "a", "text": "/var/log/syslog", "correct": False}, {"id": "b", "text": "/var/log/auth.log", "correct": True}, {"id": "c", "text": "/var/log/access.log", "correct": False}, {"id": "d", "text": "/var/log/login.log", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "tail -f", "right": "Просмотр в реальном времени"}, {"left": "grep", "right": "Поиск по шаблону"}, {"left": "wc -l", "right": "Подсчёт строк"}, {"left": "logrotate", "right": "Ротация и сжатие логов"}]},
                ],
            },
            {
                "t": "Бэкапы и восстановление",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Стратегии бэкапов", "markdown": "## Бэкапы\n\n### tar — архивирование:\n```bash\n# Создать архив:\ntar -czf backup.tar.gz /var/www /etc/nginx\n\n# Распаковать:\ntar -xzf backup.tar.gz\n\n# Посмотреть содержимое:\ntar -tzf backup.tar.gz\n```\n\n### rsync — инкрементальный бэкап:\n```bash\nrsync -avz /var/www/ /backup/www/\nrsync -avz --delete /var/www/ user@remote:/backup/www/\n```\n\n### Бэкап базы данных:\n```bash\n# PostgreSQL:\npg_dump mydb > backup_$(date +%Y%m%d).sql\npg_dump mydb | gzip > backup_$(date +%Y%m%d).sql.gz\n\n# MySQL:\nmysqldump -u root -p mydb > backup.sql\n\n# Восстановление:\npsql mydb < backup.sql\nmysql -u root -p mydb < backup.sql\n```\n\n### Автоматизация через cron:\n```bash\n# Ежедневный бэкап в 2:00\n0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1\n```\n\n### Правило 3-2-1:\n- **3** копии данных\n- **2** разных носителя\n- **1** копия вне офиса (облако)"},
                    {"type": "terminal-sim", "prompt": "Создайте сжатый архив директорий /var/www и /etc/nginx:", "expectedCommand": "tar -czf backup.tar.gz /var/www /etc/nginx", "hint": "tar -czf для создания gzip-архива"},
                    {"type": "drag-order", "items": ["Определить что бэкапить (данные, конфиги, БД)", "Написать скрипт бэкапа", "Протестировать восстановление", "Настроить cron-задачу", "Настроить копирование на удалённый сервер"]},
                    {"type": "quiz", "question": "Что означает правило бэкапов 3-2-1?", "options": [{"id": "a", "text": "3 копии, 2 носителя, 1 вне офиса", "correct": True}, {"id": "b", "text": "3 сервера, 2 диска, 1 облако", "correct": False}, {"id": "c", "text": "Бэкап 3 раза в день", "correct": False}, {"id": "d", "text": "3 типа файлов, 2 формата, 1 скрипт", "correct": False}]},
                    {"type": "true-false", "statement": "rsync передаёт только изменившиеся части файлов, что делает его эффективнее обычного cp.", "correct": True},
                ],
            },
            {
                "t": "Мониторинг сервера",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Мониторинг ресурсов", "markdown": "## Мониторинг сервера\n\n### Процессор и память:\n```bash\ntop / htop              # интерактивный мониторинг\nfree -h                 # свободная память\nuptime                  # загрузка системы (load average)\nnproc                   # количество ядер CPU\nlscpu                   # информация о процессоре\n```\n\n### Дисковое пространство:\n```bash\ndf -h                   # свободное место на дисках\ndu -sh /var/log/*       # размер директорий\ndu -h --max-depth=1 /   # размер корневых директорий\nncdu /                  # интерактивный анализатор (TUI)\n```\n\n### Load Average:\n```bash\nuptime\n# 14:30  up 45 days,  load average: 0.15, 0.10, 0.05\n#                       1 мин  5 мин  15 мин\n```\n- Значение = количеству ядер → CPU полностью загружен\n- Значение > количества ядер → перегрузка\n\n### Сетевая активность:\n```bash\niftop                   # трафик по интерфейсам\nnethogs                 # трафик по процессам\nvnstat                  # статистика за период\n```\n\n### Инструменты мониторинга:\n- **Prometheus + Grafana** — графики и алерты\n- **Zabbix** — enterprise-мониторинг\n- **Netdata** — мониторинг в реальном времени\n- **node_exporter** — метрики для Prometheus"},
                    {"type": "terminal-sim", "prompt": "Проверьте свободное место на всех дисках:", "expectedCommand": "df -h", "hint": "df -h для человекочитаемого вывода"},
                    {"type": "quiz", "question": "Что показывает load average 4.00 на сервере с 4 ядрами?", "options": [{"id": "a", "text": "CPU полностью загружен", "correct": True}, {"id": "b", "text": "CPU перегружен", "correct": False}, {"id": "c", "text": "Только 4% загрузки", "correct": False}, {"id": "d", "text": "4 процесса запущено", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "df -h", "right": "Свободное место на дисках"}, {"left": "free -h", "right": "Свободная оперативная память"}, {"left": "uptime", "right": "Время работы и load average"}, {"left": "du -sh", "right": "Размер директории/файла"}]},
                    {"type": "multi-select", "question": "Какие инструменты используются для мониторинга серверов?", "options": [{"id": "a", "text": "Prometheus", "correct": True}, {"id": "b", "text": "Grafana", "correct": True}, {"id": "c", "text": "Photoshop", "correct": False}, {"id": "d", "text": "Zabbix", "correct": True}, {"id": "e", "text": "PowerPoint", "correct": False}]},
                ],
            },
            {
                "t": "Итоговый тест: Linux-администратор",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Итоговый тест", "markdown": "## Итоговый тест по курсу\n\nПоздравляем! Вы прошли весь курс по Linux-администрированию.\n\n### Что вы изучили:\n1. **Основы Linux** — ядро, дистрибутивы, терминал\n2. **Файловая система** — навигация, права, поиск\n3. **Пользователи** — управление, группы, sudo, ACL\n4. **Процессы** — мониторинг, сигналы, systemd, cron\n5. **Сети** — интерфейсы, SSH, firewall, DNS\n6. **Bash-скрипты** — переменные, условия, циклы, функции\n7. **Серверы** — Nginx, логи, бэкапы, мониторинг\n\n### Следующие шаги:\n- Получите сертификат **LPIC-1** или **CompTIA Linux+**\n- Изучите **Docker** и контейнеризацию\n- Освойте **Ansible** для автоматизации\n- Попробуйте **Kubernetes** для оркестрации\n- Настройте свой VPS-сервер\n\nТеперь проверим ваши знания!"},
                    {"type": "quiz", "question": "Какой командой изменить права файла на rwxr-xr-x?", "options": [{"id": "a", "text": "chmod 755 file", "correct": True}, {"id": "b", "text": "chmod 644 file", "correct": False}, {"id": "c", "text": "chmod 777 file", "correct": False}, {"id": "d", "text": "chown 755 file", "correct": False}]},
                    {"type": "multi-select", "question": "Какие из этих команд связаны с управлением сервисами systemd?", "options": [{"id": "a", "text": "systemctl start", "correct": True}, {"id": "b", "text": "systemctl enable", "correct": True}, {"id": "c", "text": "service restart", "correct": False}, {"id": "d", "text": "systemctl status", "correct": True}, {"id": "e", "text": "init.d start", "correct": False}]},
                    {"type": "terminal-sim", "prompt": "Найдите все файлы размером больше 100MB в системе:", "expectedCommand": "find / -size +100M", "hint": "find с флагом -size +100M"},
                    {"type": "drag-order", "items": ["Установить Linux (Ubuntu) на VPS", "Настроить SSH-ключи и отключить пароли", "Установить Nginx и настроить виртуальный хост", "Настроить UFW-файрвол", "Настроить cron-бэкапы и мониторинг"]},
                ],
            },
        ],
    },
]


async def main():
    async with async_session() as db:
        existing = await db.execute(select(Course).where(Course.title == T))
        if existing.scalar_one_or_none():
            print(f"'{T}' already exists — skipping.")
            return
        author = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not author:
            print("No users.")
            return
        course = Course(
            title=T,
            slug="linux-sysadmin-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="SysAdmin",
            difficulty="Beginner",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()
        nodes, edges, lc, tl = [], [], 0, 0
        for sd in S:
            sec = CourseSection(
                course_id=course.id, title=sd["title"], position=sd["pos"]
            )
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
                    edges.append(
                        {
                            "id": f"e-{lc}",
                            "source": nodes[-2]["id"],
                            "target": nodes[-1]["id"],
                        }
                    )
                lc += 1
                tl += 1
        course.roadmap_nodes = nodes
        course.roadmap_edges = edges
        await db.commit()
        print(f"Created '{T}': {len(S)} sections, {tl} lessons.")


if __name__ == "__main__":
    asyncio.run(main())
