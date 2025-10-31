"""Monitor Ambientale guidato dai test.

Questo modulo contiene la classe `MonitorAmbientale`, cuore del percorso TDD.
Partiremo definendo lo storico delle letture, poi introdurremo le soglie di
allarme e infine collegheremo un notificatore esterno rispettando il principio
DIP (Dependency Inversion Principle).
"""

from __future__ import annotations

from typing import Iterable, List, Optional

from lettura_sensore import LetturaSensore


class MonitorAmbientale:
    """Gestisce lo storico delle letture e la logica di allarme.

    I test guideranno l'implementazione passo dopo passo: prima verificheremo
    la corretta memorizzazione (milestone 2), poi il calcolo dell'allarme
    (milestone 3) e infine l'integrazione con un notificatore esterno (milestone 4).
    """

    # TODO 2.1: inizializza la struttura dati interna (es. lista) e il riferimento al notificatore.
    def __init__(self, notificatore: Optional[object] = None) -> None:
        """Crea un monitor opzionalmente collegato a un notificatore.

        Secondo il DIP, il monitor deve dipendere da un'interfaccia astratta
        (qualunque oggetto con `manda_alert`). I test useranno un mock.
        """
        # Suggerimento: memorizza le letture in una lista privata e conserva il notificatore.
        # self._letture: List[LetturaSensore] = ...
        # self._notificatore = notificatore
        # TODO 4.1 e 4.3 verranno completati qui.
        raise NotImplementedError("Completa i TODO 2.1, 4.1 e 4.3 nel costruttore")

    # TODO 2.2: aggiungi una docstring e implementa l'aggiunta allo storico.
    def aggiungi_lettura(self, lettura: LetturaSensore) -> None:
        """Aggiunge una lettura allo storico e valuta eventuali allarmi."""
        # Ricorda di seguire il ciclo TDD: fai fallire il test prima di implementare.
        # self._letture.append(lettura)
        # TODO 4.2: dopo aver aggiornato lo storico, verifica se serve notificare.
        raise NotImplementedError

    # TODO 2.2: restituisci lo storico delle letture in ordine di inserimento.
    def tutte_le_letture(self) -> Iterable[LetturaSensore]:
        """Ritorna lo storico delle letture raccolte finora."""
        # Potresti restituire una copia per evitare modifiche esterne.
        raise NotImplementedError

    # TODO 3.1: definisci le soglie di allarme e documenta il perché.
    def _verifica_soglie(self, lettura: LetturaSensore) -> bool:
        """Controlla se la lettura supera le soglie di sicurezza."""
        # Esempio: temperatura > 50 oppure umidità < 20 -> True.
        # Lascia che siano i test a guidare l'esatta implementazione.
        raise NotImplementedError

    # TODO 3.2: esponi un metodo pubblico che riutilizzi la logica di soglia.
    def is_allarme(self, lettura: LetturaSensore) -> bool:
        """Restituisce True se la lettura richiede un allarme."""
        # Probabilmente vorrai richiamare `_verifica_soglie` qui.
        raise NotImplementedError

    # TODO 4.2: metodo di supporto per notificare quando serve.
    def _notifica_se_necessario(self, lettura: LetturaSensore) -> None:
        """Invoca il notificatore se la lettura è fuori soglia.

        Durante i test useremo un mock che espone `manda_alert`. Il monitor non
        deve conoscere l'implementazione concreta, solo l'interfaccia.
        """
        # Suggerimento: controlla se `_notificatore` esiste e se `is_allarme` è True.
        raise NotImplementedError
