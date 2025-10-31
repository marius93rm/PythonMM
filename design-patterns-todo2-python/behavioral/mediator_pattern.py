"""Pattern Mediator
===================
Cos'è il pattern:
    Il Mediator centralizza la comunicazione tra oggetti riducendo dipendenze dirette.
Obiettivo didattico:
    Modellare una chat room dove gli utenti parlano solo tramite un mediatore.
Scenario proposto:
    Gli utenti registrano il proprio nickname presso il mediatore e inviano messaggi broadcast.
Cosa deve fare lo studente:
    Implementare il mediatore e la logica di invio/ricezione dei messaggi.
Passi TODO:
    1. Definire l'interfaccia `Mediator` con il metodo `send`.
    2. Implementare `ChatRoomMediator` per registrare utenti e inoltrare messaggi.
    3. Completare la classe `User` per parlare con il mediatore.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class Mediator(ABC):
    """Interfaccia per i mediatori di chat."""

    # TODO: dichiarare metodo astratto register(user: "User") -> None
    # TODO: dichiarare metodo astratto send(sender: "User", message: str) -> None


class ChatRoomMediator(Mediator):
    """Implementazione concreta che gestisce utenti e messaggi."""

    def __init__(self) -> None:
        self._users: Dict[str, "User"] = {}

    def register(self, user: "User") -> None:
        # TODO: aggiungere l'utente alla chat room
        raise NotImplementedError("Registrazione utente non implementata")

    def send(self, sender: "User", message: str) -> None:
        # TODO: inoltrare il messaggio a tutti gli utenti tranne il mittente
        raise NotImplementedError("Invio dei messaggi non implementato")


class User:
    """Partecipante alla chat che comunica tramite il mediatore."""

    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator
        # TODO: registrarsi immediatamente presso il mediatore

    def send(self, message: str) -> None:
        # TODO: inviare il messaggio tramite il mediatore
        raise NotImplementedError("Invio messaggio dell'utente non implementato")

    def receive(self, sender: "User", message: str) -> None:
        # TODO: gestire la ricezione (es. memorizzare messaggi o stampare)
        raise NotImplementedError("Ricezione messaggio non implementata")


def start_demo_chat(names: List[str]) -> ChatRoomMediator:
    """Utility per creare utenti e restituire il mediatore."""
    mediator = ChatRoomMediator()
    for name in names:
        # TODO: istanziare User per ogni nome
        raise NotImplementedError("Creare utenti demo")
    return mediator
