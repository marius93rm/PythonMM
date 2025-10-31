"""Soluzione commentata del pattern Bridge."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Device(ABC):
    """Interfaccia per tutti i dispositivi controllabili."""

    @abstractmethod
    def power_on(self) -> None:
        """Accende il dispositivo."""

    @abstractmethod
    def power_off(self) -> None:
        """Spegne il dispositivo."""

    @abstractmethod
    def is_on(self) -> bool:
        """Indica se il dispositivo è attualmente acceso."""

    @abstractmethod
    def set_volume(self, level: int) -> None:
        """Imposta il volume su un valore normalizzato."""

    @abstractmethod
    def get_volume(self) -> int:
        """Restituisce il volume corrente."""


class RemoteControl(ABC):
    """Astrae le operazioni comuni dei telecomandi."""

    def __init__(self, device: Device) -> None:
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_on():
            self._device.power_off()
        else:
            self._device.power_on()

    def volume_up(self) -> None:
        new_level = min(self._device.get_volume() + 5, 100)
        self._device.set_volume(new_level)

    def volume_down(self) -> None:
        new_level = max(self._device.get_volume() - 5, 0)
        self._device.set_volume(new_level)


class BasicRemote(RemoteControl):
    """Telecomando standard senza extra."""
    # Nessuna logica aggiuntiva: eredita i comportamenti base.
    pass


class AdvancedRemote(RemoteControl):
    """Telecomando avanzato con funzionalità extra (es. mute)."""

    def mute(self) -> None:
        self._device.set_volume(0)


class Television(Device):
    """Implementazione concreta di un dispositivo TV."""

    def __init__(self) -> None:
        self._powered = False
        self._volume = 25

    def power_on(self) -> None:
        self._powered = True
        print("TV accesa")

    def power_off(self) -> None:
        self._powered = False
        print("TV spenta")

    def is_on(self) -> bool:
        return self._powered

    def set_volume(self, level: int) -> None:
        self._volume = level
        print(f"TV volume: {self._volume}")

    def get_volume(self) -> int:
        return self._volume


class Radio(Device):
    """Implementazione concreta di un dispositivo radio."""

    def __init__(self) -> None:
        self._powered = False
        self._volume = 50

    def power_on(self) -> None:
        self._powered = True
        print("Radio accesa")

    def power_off(self) -> None:
        self._powered = False
        print("Radio spenta")

    def is_on(self) -> bool:
        return self._powered

    def set_volume(self, level: int) -> None:
        self._volume = level
        print(f"Radio volume: {self._volume}")

    def get_volume(self) -> int:
        return self._volume


def demo_remote(remote: RemoteControl) -> None:
    """Funzione di supporto per provare il bridge."""
    remote.toggle_power()
    remote.volume_up()
    remote.volume_down()
