# notifications.py
import firebase_admin
from firebase_admin import messaging, credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

async def send_push_notification(device_token: str, title: str, body: str, data: dict = None):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        token=device_token,
        data=data or {}
    )
    response = messaging.send(message)
    return response
