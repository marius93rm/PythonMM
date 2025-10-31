"""Soluzione commentata del pattern Factory Method per il sistema di notifiche."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Notification(ABC):
    """Interfaccia comune per ogni canale di notifica."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Invia il messaggio attraverso il canale specifico."""


class EmailNotification(Notification):
    """Invia una notifica via email."""

    def send(self, message: str) -> None:
        print(f"[EMAIL] {message}")


class SmsNotification(Notification):
    """Invia una notifica via SMS."""

    def send(self, message: str) -> None:
        print(f"[SMS] {message}")


class NotificationFactory:
    """Factory che restituisce un oggetto Notification a partire da una stringa."""

    def create_notification(self, channel: str) -> Notification:
        """Restituisce la notifica appropriata in base al canale richiesto."""
        normalized = channel.strip().lower()
        if normalized == "email":
            return EmailNotification()
        if normalized == "sms":
            return SmsNotification()
        raise ValueError(f"Unsupported notification channel: {channel!r}")


def demo(factory: NotificationFactory) -> None:
    """Esempio di utilizzo della factory."""

    # Creiamo una notifica d'esempio per mostrare l'uso del factory method.
    notification = factory.create_notification("email")
    notification.send("Messaggio di test dal pattern Factory Method")
