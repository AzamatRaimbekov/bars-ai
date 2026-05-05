# B2B SaaS (Phase 1)

Трансформация из B2C в мульти-тенантный B2B SaaS.

## Архитектура

- **Multi-tenancy**: shared database с `organization_id` изоляцией
- **RBAC**: Role + RolePermission с union-based permission checking
- **Два уровня админов**: Platform Admin (superadmin) и Org Admin

## Модели

| Модель | Описание |
|---|---|
| Organization | Тенант: name, slug, logo, plan (free/pro/enterprise) |
| Department | Отдел с иерархией (parent_id), head_id |
| UserDepartment | M2M связь пользователь-отдел |
| Role | Роль в организации, системные роли (org_admin, member) |
| RolePermission | Разрешения привязанные к роли |
| UserRole | M2M связь пользователь-роль |
| InviteLink | Инвайт-ссылка с авто-назначением отдела/роли, TTL, max_uses |

## JWT расширение

JWT payload теперь включает:
- `org_id` — UUID организации (nullable для B2C пользователей)
- `is_superadmin` — флаг суперадмина платформы

## CurrentUser & Permissions

- `get_current_user` dependency — возвращает полный User объект
- `require_permission()` — RBAC dependency с union checking:
  1. superadmin — полный доступ
  2. org_admin (системная роль) — доступ ко всему в своей организации
  3. role permissions — гранулярные разрешения через RolePermission

## Спека

`docs/superpowers/specs/2026-05-01-b2b-saas-phase1-design.md`

---

См. также: [[Модели]], [[База данных]], [[Аутентификация]]
