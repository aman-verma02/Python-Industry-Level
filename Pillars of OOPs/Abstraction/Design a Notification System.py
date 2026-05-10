"""❓ Problem

Support:
Email
SMS
Push notifications

System should:
send_notification(user, message)

🧠 Thinking (IMPORTANT)
👉 What varies?
delivery mechanism
👉 What stays same?
sending notification


"""


# Abstraction Design

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, user, message):
        pass


# Implementations

class EmailNotification(Notification):
    def send(self, user, message):
        return f"Email sent to {user}"
    
class SMSNotification(Notification):
    def send(self, user, message):
        return f"SMS sent to {user}"
    
class PushNotification(Notification):
    def send(self, user, message):
        return f"Push sent to {user}"
    
# System Layer
class NotificationService:
    def __init__(self, notifier: Notification):
        self.notifier = notifier

    def notify(self, user, message):
        return self.notifier.send(user, message)


# Usage
service = NotificationService(EmailNotification())
print(service.notify("Trek", "Hello"))  # Output: Email sent to Trek