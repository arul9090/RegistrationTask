from email.message import EmailMessage
import smtplib
from config import Config


def smtp_is_configured() -> bool:
    return all([
        Config.SMTP_HOST,
        Config.SMTP_PORT,
        Config.SMTP_USERNAME,
        Config.SMTP_PASSWORD,
        Config.SMTP_FROM_EMAIL,
    ])


def send_welcome_email(user) -> bool:
    if not smtp_is_configured():
        return False

    message = EmailMessage()
    message["Subject"] = "Welcome to SkillRank"
    message["From"] = Config.SMTP_FROM_EMAIL
    message["To"] = user["email"]
    message.set_content(
        f"Hi {user.get('name', 'there')},\n\n"
        "Your SkillRank account was created successfully.\n\n"
        "Thanks,\nSkillRank Team"
    )

    with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT, timeout=15) as smtp:
        if Config.SMTP_USE_TLS:
            smtp.starttls()
        smtp.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
        smtp.send_message(message)

    return True
