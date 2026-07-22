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

# this adapter converts SendBirdEmailService's interface to NotificationService's interface
class SendBirdEmailAdapter(NotificationService):
    def __init__(self, send_bird_service: SendBirdEmailService):
        self.send_bird_service = send_bird_service

    def send_notification(self, message: str) -> None:
        self.send_bird_service.send(message)

# client code
for service in [SMSNotificationService(), EmailNotificationService(), SendBirdEmailAdapter(SendBirdEmailService("abc123"))]:
    service.send_notification("Hello via Notification Service!")