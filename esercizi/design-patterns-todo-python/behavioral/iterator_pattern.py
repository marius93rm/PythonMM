"""Pattern Iterator
===================
Cos'è il pattern:
    L'Iterator fornisce un modo uniforme per attraversare una collezione senza esporne l'implementazione interna.
Obiettivo didattico:
    Creare un iteratore personalizzato per una playlist musicale.
Scenario proposto:
    Una classe `Playlist` gestisce un elenco di tracce e deve fornire un iteratore che rispetta l'ordine di inserimento.
Cosa deve fare lo studente:
    Completare le classi della playlist e dell'iteratore, curando lo stato interno.
Passi TODO:
    1. Implementare l'aggiunta di tracce in `Playlist`.
    2. Creare un iteratore con `__iter__` e `__next__` che avanza correttamente.
    3. Gestire il termine dell'iterazione sollevando `StopIteration`.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import List


class Playlist:
    """Collezione di tracce audio."""

    def __init__(self) -> None:
        self._tracks: List[str] = []

    def add_track(self, track: str) -> None:
        # TODO: aggiungere la traccia alla lista interna
        raise NotImplementedError("Implementare add_track")

    def __iter__(self) -> "PlaylistIterator":
        return PlaylistIterator(self)

    def _get_tracks(self) -> List[str]:
        """Restituisce una copia delle tracce per evitare modifiche esterne."""
        return list(self._tracks)


class PlaylistIterator(Iterator[str]):
    """Iteratore personalizzato per Playlist."""

    def __init__(self, playlist: Playlist) -> None:
        self._tracks = playlist._get_tracks()
        self._index = 0

    def __iter__(self) -> "PlaylistIterator":
        return self

    def __next__(self) -> str:
        # TODO: restituire la traccia corrente e avanzare l'indice
        # TODO: sollevare StopIteration quando i brani sono terminati
        raise NotImplementedError("Implementare la logica di avanzamento dell'iteratore")


def build_playlist(*tracks: str) -> Playlist:
    """Utility per popolare rapidamente una playlist."""
    playlist = Playlist()
    for track in tracks:
        # TODO: usare add_track per inserire ciascun brano
        raise NotImplementedError("Completare build_playlist")
    return playlist
