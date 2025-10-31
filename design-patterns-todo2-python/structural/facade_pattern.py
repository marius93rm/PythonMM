"""Pattern Facade
=================
Cos'è il pattern:
    La Facade semplifica l'accesso a un sottosistema complesso offrendo un'interfaccia più piccola e chiara.
Obiettivo didattico:
    Coordinare più componenti interni senza esporre i dettagli al client.
Scenario proposto:
    Un convertitore video deve orchestrare caricamento, decodifica, codifica e salvataggio.
Cosa deve fare lo studente:
    Creare i sottosistemi e far sì che `VideoConverterFacade` li utilizzi nell'ordine corretto.
Passi TODO:
    1. Implementare classi di supporto (`VideoLoader`, `VideoDecoder`, `VideoEncoder`, `VideoSaver`).
    2. Istanziarle nel costruttore della facade.
    3. Completare il metodo `convert()` restituendo una descrizione finale dell'operazione.
"""

from __future__ import annotations


class VideoLoader:
    """Carica il file di input."""

    def load(self, source: str) -> str:
        # TODO: simulare il caricamento del file e restituire un identificatore
        raise NotImplementedError("Implementare il caricamento del video")


class VideoDecoder:
    """Decodifica il file in un formato intermedio."""

    def decode(self, raw_stream: str) -> str:
        # TODO: simulare la decodifica e restituire un nome di stream
        raise NotImplementedError("Implementare la decodifica del video")


class VideoEncoder:
    """Codifica lo stream nel formato finale."""

    def encode(self, intermediate: str, target_format: str) -> str:
        # TODO: simulare la codifica e restituire il nome del file finale
        raise NotImplementedError("Implementare la codifica del video")


class VideoSaver:
    """Salva il risultato su disco."""

    def save(self, encoded_stream: str, destination: str) -> str:
        # TODO: simulare il salvataggio e restituire un messaggio di conferma
        raise NotImplementedError("Implementare il salvataggio del video")


class VideoConverterFacade:
    """Coordina il processo di conversione video."""

    def __init__(self) -> None:
        # TODO: istanziare i sottosistemi e salvarli come attributi
        raise NotImplementedError("Inizializzazione dei sottosistemi non completata")

    def convert(self, source: str, destination: str, *, format: str) -> str:
        """Esegue tutte le operazioni necessarie per convertire un video."""
        # TODO: orchestrare load -> decode -> encode -> save
        # TODO: restituire una stringa riassuntiva dell'operazione
        raise NotImplementedError("Sequenza di conversione da completare")


def demo_conversion(facade: VideoConverterFacade) -> None:
    """Helper da usare nei test manuali."""
    # TODO: chiamare convert con parametri fittizi e gestire il risultato
    raise NotImplementedError("Scrivere una demo di conversione")
