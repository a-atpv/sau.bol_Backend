from datetime import datetime, timedelta
from typing import Optional
``

from bson.objectid import ObjectId
from pymongo.database import Database
from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user: dict):
        payload = {
            "email": user["email"],
            "password": hash_password(user["password"]),
            "created_at": datetime.utcnow(),
        }

        self.database["users"].insert_one(payload)

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def add_user_info(self, user_id: str, data: dict):
        self.database["users"].update_one(
            filter={"_id": ObjectId(user_id)},
            update={
                "$push": {
                    "name": data["name"],
                    "age": data["age"],
                    "height": data["height"],
                    "weight": data["weight"],
                    "BMI": data["BMI"]
                }
            }
        )

    def get_user_by_email(self, email: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user

    def delete_user(self, user_id: str) -> Optional[dict]:
        user = self.get_user_by_id(user_id)
        if user:
            self.database["users"].delete_one({"_id": ObjectId(user_id)})
        return user

    def reset_password(self, email: str) -> Optional[str]:
        user = self.get_user_by_email(email)
        if not user:
            return None

        reset_token = secrets.token_urlsafe(32)
        expiry_time = datetime.utcnow() + timedelta(hours=1)

        self.database["users"].update_one(
            filter={"_id": user["_id"]},
            update={
                "$set": {
                    "reset_token": reset_token,
                    "reset_token_expiry": expiry_time
                }
            }
        )

        return reset_token

    def reset_password_with_token(self, email: str, reset_token: str, new_password: str) -> bool:
        user = self.get_user_by_email(email)
        if not user:
            return False

        if "reset_token" not in user or user["reset_token"] != reset_token:
            return False

        if "reset_token_expiry" not in user or user["reset_token_expiry"] < datetime.utcnow():
            return False

        hashed_password = hash_password(new_password)
        self.database["users"].update_one(
            filter={"_id": user["_id"]},
            update={
                "$set": {
                    "password": hashed_password,
                    "reset_token": None,
                    "reset_token_expiry": None
                }
            }
        )

        return True

    def send_reset_token_email(self, email: str, reset_token: str) -> bool:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        smtp_username = 'sau.bol.app@hotmail.com'
        smtp_password = 'sau.Bol951123@'
        sender_email = 'sau.bol.app@hotmail.com'

        subject = 'Password Reset Token'
        message = f'Your password reset token is: {reset_token}'

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, email, msg.as_string())
            server.quit()

            return True

        except Exception as e:
            print(f"Error sending email: {e}")
            return False
