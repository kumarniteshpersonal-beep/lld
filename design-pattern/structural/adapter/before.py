from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class SMSNotificationService(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")

class EmailNotificationService(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"Sending Email notification: {message}")

class SendBirdEmailService:
    def __init__(self, api_key: str):
        self.client = "client_" + api_key
    def send(self, message: str) -> None:
        print(f"Sending Email via SendBird: {message} with client {self.client}")

# client code
sms_service = SMSNotificationService()
email_service = EmailNotificationService()
sms_service.send_notification("Hello via SMS!")
email_service.send_notification("Hello via Email!")

SendBirdEmailService("abc123").send("Hello via SendBird Email!")

# problems
# 1. Client have to deal with different interfaces.
# 2. If we want to use SendBirdEmailService, we have to change client code.
# 3. Hence adapter pattern help making different interfaces compatible which intend to perform same function without changing client code.