import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings


async def send_reset_email(to_email: str, reset_token: str) -> None:
    """Send password reset email with a link containing the token."""
    reset_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Bars AI — Сброс пароля"
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email

    text = f"""Вы запросили сброс пароля на Bars AI.

Перейдите по ссылке для установки нового пароля:
{reset_url}

Ссылка действительна 1 час.

Если вы не запрашивали сброс пароля, проигнорируйте это письмо.
"""

    html = f"""
<div style="font-family: -apple-system, sans-serif; max-width: 480px; margin: 0 auto; padding: 32px;">
  <h2 style="color: #F97316; margin-bottom: 16px;">Bars AI</h2>
  <p style="color: #333; font-size: 14px; line-height: 1.6;">Вы запросили сброс пароля.</p>
  <a href="{reset_url}" style="display: inline-block; background: linear-gradient(135deg, #F97316, #FB923C); color: white; padding: 12px 32px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 14px; margin: 16px 0;">Сбросить пароль</a>
  <p style="color: #999; font-size: 12px; margin-top: 24px;">Ссылка действительна 1 час. Если вы не запрашивали сброс — проигнорируйте это письмо.</p>
</div>
"""

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_FROM, to_email, msg.as_string())
