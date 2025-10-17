# =====================================
# ESERCIZIO: Logger Universale (Singleton)
# =====================================
# Obiettivo:
# Creare un sistema di logging centralizzato che registri tutte le chiamate
# di funzioni e messaggi su file di testo. Tutte le parti dell'applicazione
# devono usare la stessa istanza di Logger.
#
# ISTRUZIONI PER LO STUDENTE:
# - Completa ogni milestone in ordine.
# - Leggi i suggerimenti nei commenti per capire quali metodi e proprietà implementare.
# - Non modificare la sezione dei test automatici: usala per verificare la tua soluzione.

# Milestone 1:
# Crea la classe Logger come Singleton, salvando l'unica istanza in una variabile di classe.
# Il metodo __new__ deve assicurarsi che venga creata una sola istanza.
# Suggerimento: usa un attributo di classe (es. _instance) per memorizzare l'oggetto creato.

# Milestone 2:
# Aggiungi un metodo log(self, message) che scrive su file "log.txt" con timestamp.
# Suggerimento: puoi usare datetime.datetime.now() per ottenere la data/ora corrente.

# Milestone 3:
# Implementa un metodo statico get_instance() che restituisce la stessa istanza di Logger.
# Suggerimento: fai in modo che richiami internamente il costruttore della classe.

# Milestone 4:
# Crea un decoratore @logged che logga automaticamente l'esecuzione
# di qualsiasi funzione decorata, salvando nome della funzione e data/ora.
# Suggerimento: sfrutta functools.wraps per preservare il metadata della funzione originale.

# Milestone 5:
# Testa il logger con alcune funzioni e verifica che il file contenga le righe corrette.
# Suggerimento: usa i test automatici in fondo al file per verificare il comportamento.

# =====================================
# SCRIVI QUI IL TUO CODICE
# =====================================

from __future__ import annotations

from typing import Callable, Any


class Logger:
    """Singleton responsabile della scrittura dei messaggi di log."""

    # TODO: definisci la variabile di classe che conterrà l'unica istanza.

    def __new__(cls, *args: Any, **kwargs: Any) -> "Logger":
        """Crea o restituisce l'unica istanza di Logger."""
        # TODO: implementa il controllo sull'esistenza dell'istanza e creala solo se necessario.
        raise NotImplementedError("Implementa il pattern Singleton in __new__")

    def __init__(self, log_file: str = "log.txt") -> None:
        """Inizializza eventuali risorse (chiamato ad ogni get_instance)."""
        # TODO: opzionalmente memorizza il percorso del file di log.
        # Nota: __init__ viene richiamato a ogni invocazione, quindi fai attenzione a non sovrascrivere dati importanti.
        pass

    def log(self, message: str) -> None:
        """Scrive un messaggio con timestamp nel file di log."""
        # TODO: implementa l'apertura del file in modalità append e scrivi il messaggio con timestamp.
        raise NotImplementedError("Implementa il metodo log")

    @staticmethod
    def get_instance() -> "Logger":
        """Restituisce l'unica istanza del Logger (creandola se necessario)."""
        # TODO: richiamare Logger() e restituire l'istanza condivisa.
        raise NotImplementedError("Implementa il metodo statico get_instance")


def logged(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decoratore che logga automaticamente l'esecuzione della funzione decorata."""
    # TODO: utilizza functools.wraps e assicurati di invocare Logger.get_instance().log(...).
    raise NotImplementedError("Implementa il decoratore logged")


# =====================================
# TEST AUTOMATICI
# =====================================

if __name__ == "__main__":
    import os
    import datetime

    # 1. Verifica Singleton
    l1 = Logger.get_instance()
    l2 = Logger.get_instance()
    assert l1 is l2, "ERRORE: Logger non è Singleton"

    # 2. Verifica logging base
    l1.log("Test messaggio")
    assert os.path.exists("log.txt"), "ERRORE: File log non creato"

    # 3. Verifica decoratore
    @logged
    def hello() -> str:
        return "Ciao mondo"

    hello()
    with open("log.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "hello" in content, "ERRORE: Decoratore non ha loggato la funzione"

    print("✅ Tutti i test superati!")
