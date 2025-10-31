"""Soluzione commentata del pattern Abstract Factory."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):
    """Interfaccia per i bottoni dei diversi temi."""

    @abstractmethod
    def render(self) -> str:
        """Restituisce una rappresentazione testuale del bottone."""


class Checkbox(ABC):
    """Interfaccia per le checkbox dei diversi temi."""

    @abstractmethod
    def render(self) -> str:
        """Restituisce una rappresentazione testuale della checkbox."""


class LightButton(Button):
    """Bottone in stile chiaro."""

    def render(self) -> str:
        # Il messaggio differenzia il tema per l'utente finale.
        return "Light theme button"


class DarkButton(Button):
    """Bottone in stile scuro."""

    def render(self) -> str:
        return "Dark theme button"


class LightCheckbox(Checkbox):
    """Checkbox in stile chiaro."""

    def render(self) -> str:
        return "Light theme checkbox"


class DarkCheckbox(Checkbox):
    """Checkbox in stile scuro."""

    def render(self) -> str:
        return "Dark theme checkbox"


class UIComponentFactory(ABC):
    """Factory astratta per produrre componenti coerenti."""

    @abstractmethod
    def create_button(self) -> Button:
        """Restituisce un bottone del tema gestito dalla factory."""

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Restituisce una checkbox del tema gestito dalla factory."""


class LightUIFactory(UIComponentFactory):
    """Crea componenti per il tema chiaro."""

    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkUIFactory(UIComponentFactory):
    """Crea componenti per il tema scuro."""

    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


def demo_render(factory: UIComponentFactory) -> list[str]:
    """Crea componenti con la factory e restituisce le stringhe renderizzate."""

    # Il client conosce solo l'interfaccia factory: crea i componenti e invoca render.
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return [button.render(), checkbox.render()]
