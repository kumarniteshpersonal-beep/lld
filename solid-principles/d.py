# Dependency Inversion Principle - states that high-level modules should not depend on low-level modules, but both should depend on abstractions.

class GmailClient:
    def send_email(self, to, subject, body):
        print(f"Sending email to {to} with subject '{subject}' and body '{body}'")

class NotificationService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_notification(self, to, subject, body):
        self.gmail_client.send_email(to, subject, body)

NotificationService().send_notification("test@example.com", "Test Subject", "Test Body")

# problems:
# 1. The NotificationService class is tightly coupled with the GmailClient class, which violates the Dependency Inversion Principle. 
# 2. If we want to switch to a different email client, we would need to modify the NotificationService class, which is not ideal.

from abc import ABC, abstractmethod
class EmailClient(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass

class GmailClient(EmailClient):
    def send_email(self, to, subject, body):
        print(f"Sending email to {to} with subject '{subject}' and body '{body}'")

class NotificationService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_notification(self, to, subject, body):
        self.email_client.send_email(to, subject, body)

NotificationService(GmailClient()).send_notification("test@example.com", "Test Subject", "Test Body")