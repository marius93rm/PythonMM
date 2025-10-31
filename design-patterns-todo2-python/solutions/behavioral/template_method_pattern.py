"""Soluzione commentata del pattern Template Method."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Sequence


class ReportGenerator(ABC):
    """Classe base con il template per generare report."""

    def run(self) -> str:
        """Esegue il flusso completo: load -> process -> render."""
        data = self.load_data()
        processed = self.process_data(data)
        return self.render_output(processed)

    @abstractmethod
    def load_data(self) -> Sequence[Any]:
        """Carica i dati grezzi da elaborare."""

    @abstractmethod
    def process_data(self, data: Sequence[Any]) -> Any:
        """Applica l'elaborazione sui dati."""

    @abstractmethod
    def render_output(self, result: Any) -> str:
        """Trasforma il risultato in un output presentabile."""


class SalesReport(ReportGenerator):
    """Esempio di report concreto basato su vendite settimanali."""

    def load_data(self) -> Sequence[int]:
        # Dati di esempio: vendite per giorno.
        return [120, 135, 98, 143, 155, 90, 110]

    def process_data(self, data: Sequence[int]) -> dict[str, float]:
        total = sum(data)
        average = total / len(data)
        return {"total": total, "average": average}

    def render_output(self, result: dict[str, float]) -> str:
        return f"Weekly sales - Total: {result['total']}, Average: {result['average']:.2f}"


class InventoryReport(ReportGenerator):
    """Secondo esempio di report con dati di inventario."""

    def load_data(self) -> Sequence[tuple[str, int]]:
        return [("Laptop", 12), ("Mouse", 58), ("Keyboard", 34)]

    def process_data(self, data: Sequence[tuple[str, int]]) -> list[str]:
        return [f"{name}: {qty} pezzi" for name, qty in data]

    def render_output(self, result: list[str]) -> str:
        lines = "\n".join(result)
        return f"Inventory report:\n{lines}"


def run_report(report: ReportGenerator) -> str:
    """Helper per avviare un report e restituire il risultato."""
    return report.run()
