from datetime import datetime, timedelta
from typing import Optional
import secrets
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib, ssl
import yagmail


def send_reset_token_email(email: str, reset_token: str) -> bool:
    smtp_username = 'sau.bol.app@hotmail.com'
    smtp_password = 'Sau.Bol951123@'
    subject = 'Password Reset Token'
    body = f'Your password reset token is: {reset_token}'

    try:
        yag = yagmail.SMTP(smtp_username, smtp_password, "smtp.office365.com", 587,)
        yag.send(
            to=email,
            subject=subject,
            contents=body
        )
        print("done")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

send_reset_token_email("aldiyar09.02@mail.ru", "shdfkjsjlgjslkf")