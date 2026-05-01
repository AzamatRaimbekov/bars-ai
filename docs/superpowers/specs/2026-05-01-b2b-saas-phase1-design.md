# Фаза 1: B2B SaaS Фундамент — Дизайн

**Дата:** 2026-05-01
**Статус:** Утверждён
**Scope:** Multi-tenancy, организации, отделы, кастомные роли (RBAC), инвайты, адаптация онбординга

---

## Контекст

Bars AI трансформируется из B2C платформы в multi-tenant B2B SaaS. Компании-клиенты разворачивают платформу для обучения своих сотрудников с кастомными ролями, отделами и назначением курсов.

Фаза 1 закладывает фундамент: изоляция данных, организационная структура, RBAC, инвайт-система. Последующие фазы добавляют назначение курсов (Фаза 2), аналитику (Фаза 3) и enterprise-фичи (Фаза 4).

### Целевые клиенты

- SMB (10-100 сотрудников) → Mid-market (100-1000) → Enterprise (1000+)
- Архитектура должна работать на всех уровнях

---

## 1. Multi-Tenancy

### Подход

Shared database + `organization_id` (tenant_id) во всех таблицах. Одна PostgreSQL база, разделение на уровне приложения.

### Модель: Organization

```sql
CREATE TABLE organization (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,  -- для URL: bars-ai.app/acme
    logo_url VARCHAR(500),
    primary_color VARCHAR(7),  -- hex, заготовка под Фазу 3
    owner_id UUID NOT NULL REFERENCES "user"(id),
    plan VARCHAR(50) DEFAULT 'free',  -- free/starter/business/enterprise
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
```

### Изменения в существующих таблицах

```sql
-- User
ALTER TABLE "user" ADD COLUMN organization_id UUID REFERENCES organization(id);
ALTER TABLE "user" ADD COLUMN is_superadmin BOOLEAN DEFAULT false;

-- Course
ALTER TABLE course ADD COLUMN organization_id UUID REFERENCES organization(id);
-- NULL = платформенный курс (доступен всем организациям)
-- NOT NULL = приватный курс компании
```

### Изоляция данных

- FastAPI middleware извлекает `organization_id` из JWT токена
- Все эндпоинты автоматически фильтруют данные по `organization_id`
- Суперадмин (`is_superadmin=true`) обходит фильтрацию

```python
class TenantMiddleware:
    """Извлекает org_id из JWT, добавляет в request.state."""
    async def __call__(self, request, call_next):
        token = extract_token(request)
        if token:
            request.state.org_id = token.get("org_id")
            request.state.is_superadmin = token.get("is_superadmin", False)
        return await call_next(request)
```

### Регистрация организации

1. Пользователь регистрируется (существующий flow)
2. Создаёт организацию: POST /api/organizations (name, slug)
3. Автоматически становится owner с полными правами
4. Получает 4 системные роли (owner, admin, manager, employee)
5. Приглашает сотрудников

---

## 2. Отделы

### Модель: Department

```sql
CREATE TABLE department (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organization(id),
    name VARCHAR(255) NOT NULL,
    parent_id UUID REFERENCES department(id),  -- вложенность
    head_id UUID REFERENCES "user"(id),  -- руководитель
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(organization_id, name, parent_id)
);
```

### Модель: UserDepartment (M2M)

```sql
CREATE TABLE user_department (
    user_id UUID NOT NULL REFERENCES "user"(id),
    department_id UUID NOT NULL REFERENCES department(id),
    joined_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (user_id, department_id)
);
```

### Правила

- Many-to-many: сотрудник может быть в нескольких отделах
- Максимум 3 уровня вложенности (проверка на уровне приложения)
- Курсы назначенные на родительский отдел наследуются дочерними (Фаза 2)
- Руководитель (`head_id`) видит прогресс всех сотрудников отдела

### Пример иерархии

```
Acme Corp
├── Маркетинг
│   ├── SMM
│   └── Контент
├── Разработка
│   ├── Frontend
│   └── Backend
└── HR
```

---

## 3. Кастомные роли и RBAC

### Модель: Role

```sql
CREATE TABLE role (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organization(id),
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL,
    is_system BOOLEAN DEFAULT false,  -- системные нельзя удалить
    description TEXT,
    color VARCHAR(7),  -- hex для UI
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(organization_id, slug)
);
```

### Модель: RolePermission

```sql
CREATE TABLE role_permission (
    role_id UUID NOT NULL REFERENCES role(id) ON DELETE CASCADE,
    permission VARCHAR(100) NOT NULL,
    PRIMARY KEY (role_id, permission)
);
```

### Модель: UserRole (M2M)

```sql
CREATE TABLE user_role (
    user_id UUID NOT NULL REFERENCES "user"(id),
    role_id UUID NOT NULL REFERENCES role(id) ON DELETE CASCADE,
    assigned_at TIMESTAMP DEFAULT now(),
    assigned_by UUID REFERENCES "user"(id),
    PRIMARY KEY (user_id, role_id)
);
```

### Системные роли (создаются при создании организации)

| Slug | Название | Описание | Permissions |
|------|----------|----------|-------------|
| `owner` | Владелец | Все права. Нельзя удалить/изменить | * (implicit) |
| `admin` | Админ | Полный доступ кроме удаления организации | all except org.delete |
| `manager` | Менеджер | Управление своим отделом | departments.manage_members, progress.view_department, courses.assign, users.view_all |
| `employee` | Сотрудник | Базовый доступ | progress.view_own |

### Полный список permissions

```python
PERMISSIONS = [
    # Организация
    "org.settings.edit",
    "org.branding.edit",
    "org.billing.manage",

    # Пользователи
    "users.invite",
    "users.remove",
    "users.view_all",
    "users.edit_roles",

    # Отделы
    "departments.create",
    "departments.edit",
    "departments.delete",
    "departments.manage_members",

    # Курсы
    "courses.create",
    "courses.edit",
    "courses.delete",
    "courses.publish",
    "courses.assign",

    # Learning Paths (заготовка для Фазы 2)
    "paths.create",
    "paths.edit",
    "paths.assign",

    # Прогресс
    "progress.view_own",
    "progress.view_department",
    "progress.view_all",
    "progress.export",

    # Аналитика (заготовка для Фазы 3)
    "analytics.view_department",
    "analytics.view_all",
]
```

### Проверка прав

```python
async def require_permission(permission: str, current_user: User, db: AsyncSession):
    """FastAPI dependency для проверки прав."""
    # Суперадмин обходит проверку
    if current_user.is_superadmin:
        return

    # Owner имеет все права неявно
    user_roles = await get_user_roles(db, current_user.id)
    if any(r.slug == "owner" for r in user_roles):
        return

    # Собираем все permissions из всех ролей (union)
    user_permissions = set()
    for role in user_roles:
        perms = await get_role_permissions(db, role.id)
        user_permissions.update(perms)

    if permission not in user_permissions:
        raise HTTPException(403, "Недостаточно прав")
```

- Права складываются из всех ролей пользователя (union)
- Нет "deny" — только "allow"
- Owner имеет все права неявно (hardcoded)
- Суперадмин (`is_superadmin`) обходит RBAC полностью

---

## 4. Два уровня админки

### Platform Admin (суперадмин — владелец SaaS)

**Маршрут:** `/platform-admin`
**Доступ:** `User.is_superadmin == true`

**Функционал:**
- Список всех организаций (создание, блокировка, удаление)
- Список всех пользователей платформы
- Управление тарифами организаций
- Метрики платформы (общее кол-во организаций, пользователей, курсов)
- Управление платформенными курсами (библиотека)
- Текущая Admin Panel `/admin` перенаправляется сюда для суперадмина

### Org Admin (админ компании-клиента)

**Маршрут:** `/admin` (текущая Admin Panel, трансформированная)
**Доступ:** RBAC — роль с нужными permissions

**Функционал:**
- Управление сотрудниками (приглашение, роли, отделы)
- Управление отделами (CRUD, иерархия, назначение руководителей)
- Управление ролями (создание кастомных, назначение permissions)
- Управление курсами (приватные + добавление из библиотеки платформы)
- Управление инвайт-ссылками
- Просмотр прогресса сотрудников (в рамках прав)

### Библиотека курсов

- **Платформенные** (`organization_id = NULL`): созданы суперадмином, доступны всем организациям
- **Приватные** (`organization_id = X`): созданы админом компании, видны только внутри организации
- Админ компании может добавлять платформенные курсы в свою организацию и назначать сотрудникам

---

## 5. Инвайт-система

### Модель: InviteLink

```sql
CREATE TABLE invite_link (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organization(id),
    code VARCHAR(50) UNIQUE NOT NULL,
    department_id UUID REFERENCES department(id),  -- авто-привязка
    role_id UUID REFERENCES role(id),  -- авто-назначение роли
    max_uses INTEGER,  -- NULL = безлимит
    used_count INTEGER DEFAULT 0,
    expires_at TIMESTAMP,  -- NULL = бессрочная
    created_by UUID NOT NULL REFERENCES "user"(id),
    created_at TIMESTAMP DEFAULT now()
);
```

### Три способа приглашения

1. **По ссылке:** `/join/acme?code=abc123` — массовое приглашение, можно повесить в корпоративный чат
2. **По email:** Админ вводит email → персональное приглашение с одноразовым кодом
3. **По домену:** Заготовка на Фазу 4 (SSO) — все с `@acme.com` автоматически в организацию

### Флоу регистрации через инвайт

```
Сотрудник получает ссылку /join/acme?code=abc123
  → Регистрация (или логин если аккаунт уже есть)
  → Автоматически:
      - organization_id из инвайта
      - department_id из инвайта (если указан)
      - role_id из инвайта (если указан, иначе employee)
  → Онбординг (адаптированный):
      Шаг 0: Приветствие от имени компании (лого, название организации)
      Шаг 1: Интересы (опционально, если админ включил)
      Шаг 2: Мини-чат с Барсбеком
      Шаг 3: Обязательные курсы отдела (вместо рекомендаций)
  → Dashboard с назначенными курсами
```

### Адаптация онбординга

- Шаг 0: показывает лого и название организации вместо дефолтного
- Шаг 3: если у отдела есть обязательные курсы → показать их. Иначе — fallback на текущие рекомендации по интересам
- Флаг `User.onboarding_complete` работает как раньше

---

## 6. Новые API роутеры

### /api/organizations

| Метод | Путь | Permission | Описание |
|-------|------|------------|----------|
| POST | `/` | authenticated | Создать организацию |
| GET | `/current` | authenticated | Текущая организация |
| PATCH | `/current` | org.settings.edit | Обновить настройки |
| GET | `/all` | superadmin | Все организации (Platform Admin) |
| PATCH | `/:id/status` | superadmin | Активировать/блокировать |

### /api/departments

| Метод | Путь | Permission | Описание |
|-------|------|------------|----------|
| POST | `/` | departments.create | Создать отдел |
| GET | `/` | authenticated | Список отделов организации |
| GET | `/:id` | authenticated | Детали отдела |
| PATCH | `/:id` | departments.edit | Обновить отдел |
| DELETE | `/:id` | departments.delete | Удалить отдел |
| POST | `/:id/members` | departments.manage_members | Добавить сотрудника |
| DELETE | `/:id/members/:userId` | departments.manage_members | Убрать сотрудника |

### /api/roles

| Метод | Путь | Permission | Описание |
|-------|------|------------|----------|
| POST | `/` | users.edit_roles | Создать роль |
| GET | `/` | authenticated | Список ролей организации |
| PATCH | `/:id` | users.edit_roles | Обновить роль |
| DELETE | `/:id` | users.edit_roles | Удалить роль (не системную) |
| GET | `/permissions` | users.edit_roles | Список всех permissions |
| POST | `/:id/assign/:userId` | users.edit_roles | Назначить роль пользователю |
| DELETE | `/:id/assign/:userId` | users.edit_roles | Снять роль |

### /api/invites

| Метод | Путь | Permission | Описание |
|-------|------|------------|----------|
| POST | `/` | users.invite | Создать инвайт-ссылку |
| GET | `/` | users.invite | Список активных инвайтов |
| DELETE | `/:id` | users.invite | Деактивировать инвайт |
| POST | `/join/:code` | public | Принять инвайт (регистрация/привязка) |

---

## 7. Миграции БД (Alembic)

Одна миграция создаёт все новые таблицы и колонки:

1. Создать таблицу `organization`
2. Добавить `organization_id` и `is_superadmin` в `user`
3. Добавить `organization_id` в `course`
4. Создать таблицы `department`, `user_department`
5. Создать таблицы `role`, `role_permission`, `user_role`
6. Создать таблицу `invite_link`
7. Создать индексы: `user.organization_id`, `course.organization_id`, `department.organization_id`

Все новые FK nullable — обратная совместимость с существующими B2C пользователями.

---

## 8. JWT Token Changes

Текущий JWT payload расширяется:

```python
{
    "sub": user_id,
    "org_id": organization_id,  # NEW — null для B2C юзеров
    "is_superadmin": false,     # NEW
    "exp": ...,
}
```

---

## Что НЕ входит в Фазу 1

- Назначение курсов на отделы/роли/сотрудников (Фаза 2)
- Learning Paths (Фаза 2)
- Дедлайны и трекинг прохождения (Фаза 2)
- Аналитика и дашборды прогресса (Фаза 3)
- Брендинг кроме лого (Фаза 3)
- SSO (SAML/OIDC) (Фаза 4)
- Аудит логи (Фаза 4)
- Public API для интеграций (Фаза 4)
- White-label (Фаза 4)
- Feature flags / тарифные лимиты (Фаза 4)
