"""Soluzione commentata del pattern Mediator."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class Mediator(ABC):
    """Interfaccia per i mediatori di chat."""

    @abstractmethod
    def register(self, user: "User") -> None:
        """Registra un nuovo partecipante alla chat."""

    @abstractmethod
    def send(self, sender: "User", message: str) -> None:
        """Invia un messaggio a tutti i partecipanti (escluso il mittente)."""


class ChatRoomMediator(Mediator):
    """Implementazione concreta che gestisce utenti e messaggi."""

    def __init__(self) -> None:
        self._users: Dict[str, "User"] = {}

    def register(self, user: "User") -> None:
        self._users[user.name] = user

    def send(self, sender: "User", message: str) -> None:
        for user in self._users.values():
            if user is not sender:
                user.receive(sender, message)


class User:
    """Partecipante alla chat che comunica tramite il mediatore."""

    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator
        self.inbox: List[str] = []
        self.mediator.register(self)

    def send(self, message: str) -> None:
        self.mediator.send(self, message)

    def receive(self, sender: "User", message: str) -> None:
        formatted = f"{sender.name}: {message}"
        self.inbox.append(formatted)
        print(f"[{self.name} receives] {formatted}")


def start_demo_chat(names: List[str]) -> ChatRoomMediator:
    """Utility per creare utenti e restituire il mediatore."""
    mediator = ChatRoomMediator()
    for name in names:
        User(name, mediator)
    return mediator
