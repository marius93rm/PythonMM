"""Pattern Adapter
==================
Cos'è il pattern:
    L'Adapter permette a interfacce incompatibili di collaborare tramite un traduttore.
Obiettivo didattico:
    Comprendere come incapsulare un oggetto legacy dietro un'interfaccia moderna.
Scenario proposto:
    Un lettore audio moderno deve riprodurre file utilizzando una libreria legacy con metodo `playFile`.
Cosa deve fare lo studente:
    Implementare l'interfaccia `AudioPlayer` e completare l'adapter che dialoga con `LegacyAudioSystem`.
Passi TODO:
    1. Definire il metodo `play_sound` nell'interfaccia `AudioPlayer`.
    2. Implementare `ModernAudioPlayer` che usa l'adapter per parlare con il sistema legacy.
    3. Completare `LegacyAudioAdapter` traducendo le chiamate e gestendo eventuali formati.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class AudioPlayer(ABC):
    """Interfaccia moderna per la riproduzione audio."""

    # TODO: dichiarare metodo astratto play_sound(file_path: str) -> None


class LegacyAudioSystem:
    """Simula una libreria legacy con interfaccia non compatibile."""

    def playFile(self, path: str) -> None:  # noqa: N802 - simuliamo convenzione legacy
        print(f"Legacy playing {path}")


class LegacyAudioAdapter(AudioPlayer):
    """Adapter che traduce la chiamata moderna verso il sistema legacy."""

    def __init__(self, legacy_system: LegacyAudioSystem) -> None:
        self._legacy = legacy_system

    def play_sound(self, file_path: str) -> None:
        # TODO: adattare la chiamata al metodo legacy playFile
        raise NotImplementedError("Traduzione verso la libreria legacy da implementare")


class ModernAudioPlayer(AudioPlayer):
    """Player che utilizza un adapter per parlare con la libreria legacy."""

    def __init__(self, adapter: AudioPlayer) -> None:
        self._adapter = adapter

    def play_sound(self, file_path: str) -> None:
        # TODO: delegare la riproduzione all'adapter, gestendo eventuale pre-processing
        raise NotImplementedError("Implementare la delega al LegacyAudioAdapter")


def demo_playback(player: AudioPlayer, demo_file: str) -> None:
    """Funzione di supporto per test manuali."""
    # TODO: invocare player.play_sound con il file fornito
    raise NotImplementedError("Completare la demo di playback")
