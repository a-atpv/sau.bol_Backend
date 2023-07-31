import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import secrets


def send_reset_token_email(email: str, reset_token: str) -> bool:
    # smtp_server = 'smtp-mail.outlook.com'
    # smtp_port = 587
    smtp_username = 'sau.bol.app@hotmail.com'
    smtp_password = 'sau.Bol951123@'
    sender_email = 'sau.bol.app@hotmail.com'

    # subject = 'Password Reset Token'
    message = f'Your password reset token is: {reset_token}'

    try:
        server = smtplib.SMTP_SSL('smtp-mail.outlook.com:587')
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, email, message)
        server.quit()

        # server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls()
        # server.login(smtp_username, smtp_password)
        # server.sendmail(sender_email, email, msg.as_string())
        # server.quit()

        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False


send_reset_token_email(
    email="aldiyar09.02@mail.ru",
    reset_token="sdf"
)
