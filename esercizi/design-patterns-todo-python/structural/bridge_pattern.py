"""Pattern Bridge
=================
Cos'è il pattern:
    Il Bridge separa astrazione e implementazione così da evolverle indipendentemente.
Obiettivo didattico:
    Gestire due gerarchie parallele (remote e device) senza creare classi esplosive.
Scenario proposto:
    Un telecomando controlla dispositivi diversi come TV e Radio, delegando le azioni a un'interfaccia comune.
Cosa deve fare lo studente:
    Definire i metodi dell'interfaccia `Device`, creare la classe astratta `RemoteControl` e concretizzare vari telecomandi.
Passi TODO:
    1. Implementare l'interfaccia `Device` con metodi per power e volume.
    2. Iniettare un `Device` in `RemoteControl` e delegare le operazioni.
    3. Creare telecomandi concreti che aggiungono eventuale logica specifica.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Device(ABC):
    """Interfaccia per tutti i dispositivi controllabili."""

    # TODO: dichiarare metodi astratti power_on(), power_off(), set_volume(level: int)
    # TODO: aggiungere eventuali metodi ausiliari come is_on() o get_volume() se necessario allo scenario


class RemoteControl(ABC):
    """Astrae le operazioni comuni dei telecomandi."""

    def __init__(self, device: Device) -> None:
        self._device = device

    def toggle_power(self) -> None:
        # TODO: verificare lo stato corrente del device e accenderlo/spegnerlo di conseguenza
        raise NotImplementedError("Gestione toggle_power da completare")

    def volume_up(self) -> None:
        # TODO: aumentare il volume delegando al device
        raise NotImplementedError("Implementare volume_up")

    def volume_down(self) -> None:
        # TODO: diminuire il volume delegando al device
        raise NotImplementedError("Implementare volume_down")


class BasicRemote(RemoteControl):
    """Telecomando standard senza extra."""

    # TODO: implementare eventuali comportamenti aggiuntivi o lasciare l'ereditarietà pura
    ...


class AdvancedRemote(RemoteControl):
    """Telecomando avanzato con funzionalità extra (es. mute)."""

    def mute(self) -> None:
        # TODO: impostare il volume a zero tramite il device
        raise NotImplementedError("Implementare mute sul device")


class Television(Device):
    """Implementazione concreta di un dispositivo TV."""

    # TODO: implementare i metodi dell'interfaccia Device
    ...


class Radio(Device):
    """Implementazione concreta di un dispositivo radio."""

    # TODO: implementare i metodi dell'interfaccia Device
    ...


def demo_remote(remote: RemoteControl) -> None:
    """Funzione di supporto per provare il bridge."""
    # TODO: eseguire qualche operazione sul telecomando passato
    raise NotImplementedError("Completare la demo del telecomando")
