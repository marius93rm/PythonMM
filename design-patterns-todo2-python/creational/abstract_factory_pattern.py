"""Pattern Abstract Factory
===========================
Cos'è il pattern:
    L'Abstract Factory crea famiglie di oggetti correlati mantenendo coerenza tra gli elementi prodotti.
Obiettivo didattico:
    Comprendere come separare la creazione da componenti specifici per offrire temi intercambiabili.
Scenario proposto:
    Un sistema UI deve creare bottoni e checkbox coordinati con tema chiaro o scuro.
Cosa deve fare lo studente:
    Implementare le interfacce dei componenti e le factory concrete che producono elementi coerenti.
Passi TODO:
    1. Definire le interfacce `Button` e `Checkbox` utilizzando `abc.ABC` e `@abstractmethod`.
    2. Implementare le versioni concrete Light e Dark.
    3. Completare `UIComponentFactory` e il metodo `demo_render` che usa la factory senza conoscere la variante.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):
    """Interfaccia per i bottoni dei diversi temi."""

    # TODO: dichiarare un metodo astratto render() -> str


class Checkbox(ABC):
    """Interfaccia per le checkbox dei diversi temi."""

    # TODO: dichiarare un metodo astratto render() -> str


class LightButton(Button):
    """Bottone in stile chiaro."""

    # TODO: implementare render
    ...


class DarkButton(Button):
    """Bottone in stile scuro."""

    # TODO: implementare render
    ...


class LightCheckbox(Checkbox):
    """Checkbox in stile chiaro."""

    # TODO: implementare render
    ...


class DarkCheckbox(Checkbox):
    """Checkbox in stile scuro."""

    # TODO: implementare render
    ...


class UIComponentFactory(ABC):
    """Factory astratta per produrre componenti coerenti."""

    # TODO: dichiarare i metodi astratti create_button() e create_checkbox()


class LightUIFactory(UIComponentFactory):
    """Crea componenti per il tema chiaro."""

    # TODO: restituire LightButton e LightCheckbox nei metodi richiesti
    ...


class DarkUIFactory(UIComponentFactory):
    """Crea componenti per il tema scuro."""

    # TODO: restituire DarkButton e DarkCheckbox nei metodi richiesti
    ...


def demo_render(factory: UIComponentFactory) -> list[str]:
    """Crea componenti con la factory e restituisce le stringhe renderizzate.

    Il client non conosce l'implementazione concreta: deve funzionare con qualsiasi
    factory che rispetti l'interfaccia. Usa questa funzione durante i test manuali per
    verificare che le stringhe restituite siano coerenti con il tema scelto.
    """

    # TODO: creare button e checkbox tramite la factory e chiamare render
    raise NotImplementedError("Completare la demo di renderizzazione")
