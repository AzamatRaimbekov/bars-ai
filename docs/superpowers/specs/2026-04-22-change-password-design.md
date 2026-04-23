# Смена пароля в профиле

**Дата:** 2026-04-22

## Флоу

- В Profile.tsx добавить секцию "Безопасность" между Language и Logout
- При клике раскрывается форма: старый пароль → новый пароль → подтверждение
- Кнопка "Сменить пароль"
- Успех → зелёное уведомление, форма сбрасывается
- Ошибка → красный текст ("Неверный текущий пароль")

## Бэкенд

- Новый эндпоинт `POST /api/users/me/password`
- Body: `{ current_password: str, new_password: str }`
- Логика: проверить текущий пароль через `verify_password` → хешировать новый через `hash_password` → сохранить в User.password
- 400 если текущий пароль неверный
- Минимум 8 символов для нового пароля (валидация в Pydantic schema)

## Фронтенд

- Новая секция в Profile.tsx — "Безопасность" с иконкой Lock
- Разворачивающаяся форма (toggle) с 3 полями:
  - Текущий пароль (type=password)
  - Новый пароль (type=password, minLength=8)
  - Подтверждение нового пароля (type=password)
- Клиентская валидация: минимум 8 символов, пароли совпадают
- API вызов: `POST /api/users/me/password` через `apiFetch`
- Стиль: как остальные секции Profile — bg-[#0A0A0A], border-white/6, rounded-2xl

## i18n ключи

- `profile.security` — "Security" / "Безопасность"
- `profile.changePassword` — "Change Password" / "Сменить пароль"
- `profile.currentPassword` — "Current Password" / "Текущий пароль"
- `profile.newPassword` — "New Password" / "Новый пароль"
- `profile.confirmPassword` — "Confirm Password" / "Подтвердите пароль"
- `profile.passwordChanged` — "Password changed!" / "Пароль изменён!"
- `profile.wrongPassword` — "Wrong current password" / "Неверный текущий пароль"
- `profile.passwordMismatch` — "Passwords don't match" / "Пароли не совпадают"

## Что НЕ меняется

- Login / Register
- Auth токены — сессия остаётся активной после смены пароля
- Другие страницы
