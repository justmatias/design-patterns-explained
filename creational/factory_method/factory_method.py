from abc import ABC, abstractmethod
from dataclasses import dataclass


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str: ...


@dataclass
class EmailNotification(Notification):
    email: str

    def send(self, message: str) -> str:
        return f"[Email → {self.email}] {message}"


@dataclass
class SMSNotification(Notification):
    phone: str

    def send(self, message: str) -> str:
        return f"[SMS → {self.phone}] {message}"


@dataclass
class PushNotification(Notification):
    device_token: str

    def send(self, message: str) -> str:
        return f"[Push → {self.device_token}] {message}"


class NotificationService(ABC):
    @abstractmethod
    def create_notification(self) -> Notification: ...

    def notify(self, message: str) -> str:
        return self.create_notification().send(message)


class EmailService(NotificationService):
    def __init__(self, email: str) -> None:
        self.email = email

    def create_notification(self) -> Notification:
        return EmailNotification(self.email)


class SMSService(NotificationService):
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def create_notification(self) -> Notification:
        return SMSNotification(self.phone)


class PushService(NotificationService):
    def __init__(self, device_token: str) -> None:
        self.device_token = device_token

    def create_notification(self) -> Notification:
        return PushNotification(self.device_token)


if __name__ == "__main__":
    services: list[NotificationService] = [
        EmailService("user@example.com"),
        SMSService("+1-555-0100"),
        PushService("device-token-abc123"),
    ]
    for service in services:
        print(service.notify("Your order has been shipped!"))
