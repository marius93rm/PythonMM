"""Pattern Singleton
=====================
Cos'è il pattern:
    Il Singleton assicura che di una classe esista una sola istanza condivisa in tutta l'applicazione.
Obiettivo didattico:
    Gestire la creazione controllata dell'istanza e l'inizializzazione di attributi condivisi.
Scenario proposto:
    Stiamo modellando `AppConfig`, un contenitore di configurazioni globali che deve essere unico.
Cosa deve fare lo studente:
    Implementare la logica di controllo dell'istanza e completare le proprietà richieste.
Passi TODO:
    1. Gestire l'attributo di classe `_instance` nel metodo `__new__`.
    2. Inizializzare gli attributi solo la prima volta (pattern init-once).
    3. Definire e restituire proprietà come `app_name` e `debug`.
"""

from __future__ import annotations

from typing import Any


class AppConfig:
    """Configurazione globale con semantica Singleton."""

    _instance: "AppConfig | None" = None
    _initialized: bool = False

    def __new__(cls, *args: Any, **kwargs: Any) -> "AppConfig":
        # TODO: creare l'istanza se `_instance` è None, altrimenti restituire quella esistente
        raise NotImplementedError("Gestione dell'istanza singleton da completare")

    def __init__(self, app_name: str, debug: bool = False) -> None:
        if self.__class__._initialized:
            return
        # TODO: salvare i parametri di configurazione solo alla prima inizializzazione
        # TODO: impostare `_initialized` a True dopo aver memorizzato gli attributi

    @property
    def app_name(self) -> str:
        """Nome leggibile dell'applicazione."""
        # TODO: restituire il nome dell'applicazione memorizzato
        raise NotImplementedError("Restituire il nome dell'applicazione")

    @property
    def debug(self) -> bool:
        """Indica se il sistema è in modalità debug."""
        # TODO: restituire lo stato di debug memorizzato
        raise NotImplementedError("Restituire il flag di debug")


def get_app_config() -> AppConfig:
    """Helper per accedere all'istanza condivisa.

    Questo metodo viene fornito per incoraggiare l'utilizzo di un punto di accesso
    comune. Puoi usarlo nei test manuali per recuperare la configurazione condivisa.
    """

    # TODO: restituire l'istanza unica, creando AppConfig se necessario
    raise NotImplementedError("Implementare il punto di accesso globale")
