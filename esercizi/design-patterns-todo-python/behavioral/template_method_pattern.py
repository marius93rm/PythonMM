"""Pattern Template Method
==========================
Cos'è il pattern:
    Il Template Method definisce lo scheletro di un algoritmo delegando alcuni passi alle sottoclassi.
Obiettivo didattico:
    Stabilire un flusso fisso per la generazione di report con passi personalizzabili.
Scenario proposto:
    Un generatore di report deve caricare dati, elaborarli e produrre un output testuale.
Cosa deve fare lo studente:
    Completare la classe base e creare implementazioni concrete che sostituiscano i passi specifici.
Passi TODO:
    1. Definire i metodi astratti `load_data`, `process_data`, `render_output`.
    2. Creare almeno una classe concreta che implementi i passi.
    3. Fornire una funzione helper per eseguire un report di esempio.
"""

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

    # TODO: definire metodo astratto load_data() -> Sequence[Any]
    # TODO: definire metodo astratto process_data(data: Sequence[Any]) -> Any
    # TODO: definire metodo astratto render_output(result: Any) -> str


class SalesReport(ReportGenerator):
    """Esempio di report concreto basato su vendite settimanali."""

    # TODO: implementare i tre metodi astratti con logica di esempio
    ...


class InventoryReport(ReportGenerator):
    """Secondo esempio di report con dati di inventario."""

    # TODO: implementare i tre metodi astratti con logica di esempio
    ...


def run_report(report: ReportGenerator) -> str:
    """Helper per avviare un report e restituire il risultato."""
    # TODO: chiamare run() e restituire il valore
    raise NotImplementedError("Eseguire il report e restituire l'output")
