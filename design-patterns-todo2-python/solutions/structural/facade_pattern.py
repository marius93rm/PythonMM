"""Soluzione commentata del pattern Facade."""

from __future__ import annotations


class VideoLoader:
    """Carica il file di input."""

    def load(self, source: str) -> str:
        print(f"Loading video from {source}")
        return f"raw-stream({source})"


class VideoDecoder:
    """Decodifica il file in un formato intermedio."""

    def decode(self, raw_stream: str) -> str:
        print(f"Decoding {raw_stream}")
        return f"decoded[{raw_stream}]"


class VideoEncoder:
    """Codifica lo stream nel formato finale."""

    def encode(self, intermediate: str, target_format: str) -> str:
        print(f"Encoding {intermediate} -> {target_format}")
        return f"{intermediate}.{target_format}"


class VideoSaver:
    """Salva il risultato su disco."""

    def save(self, encoded_stream: str, destination: str) -> str:
        message = f"Saved {encoded_stream} to {destination}"
        print(message)
        return message


class VideoConverterFacade:
    """Coordina il processo di conversione video."""

    def __init__(self) -> None:
        self._loader = VideoLoader()
        self._decoder = VideoDecoder()
        self._encoder = VideoEncoder()
        self._saver = VideoSaver()

    def convert(self, source: str, destination: str, *, format: str) -> str:
        """Esegue tutte le operazioni necessarie per convertire un video."""
        raw = self._loader.load(source)
        decoded = self._decoder.decode(raw)
        encoded = self._encoder.encode(decoded, format)
        confirmation = self._saver.save(encoded, destination)
        return confirmation


def demo_conversion(facade: VideoConverterFacade) -> None:
    """Helper da usare nei test manuali."""
    result = facade.convert("input.mov", "output", format="mp4")
    print(f"[DEMO] {result}")
