# SensoriMonitor.TDD

Benvenuta/o in un percorso guidato di Test-Driven Development (TDD) in Python. In questo esercizio costruirai passo dopo passo un piccolo sistema di monitoraggio per sensori IoT: partiremo da un modello semplice e arriveremo a gestire allarmi e notifiche. Ogni milestone introduce un concetto chiave (TDD di base, gestione dello stato, refactor, principio di inversione delle dipendenze e mocking). Ricorda: procedi sempre nel ciclo Red ➜ Green ➜ Refactor.

## 📂 Struttura del progetto
- `src/`: contiene il codice di produzione, organizzato in moduli semplici da testare.
- `tests/`: raccoglie i test `pytest` che guideranno ogni passo del percorso TDD.

## Milestone

1. **Milestone 1 – Lettura sensore (SRP)**  
   **Obiettivo:** modellare una singola lettura di sensore (temperatura + umidità + timestamp) come oggetto semplice e testabile.  
   1. Scrivi il test in `tests/test_lettura_sensore.py` (TODO `1.T1`) che verifica la creazione corretta di una `LetturaSensore` con valori immutabili.  
   2. Implementa la classe in `src/lettura_sensore.py` (TODO `1.1`) rendendo le proprietà in sola lettura e rispettando il Single Responsibility Principle.

2. **Milestone 2 – Storico letture (Red-Green)**  
   **Obiettivo:** creare una classe `MonitorAmbientale` che memorizza le letture ricevute.  
   1. Completa il test in `tests/test_monitor_ambientale.py` (TODO `2.T1`) per verificare che le letture vengano accumulate nell'ordine di arrivo.  
   2. Lavora su `src/monitor_ambientale.py`: inizializza la struttura interna (TODO `2.1`) e implementa i metodi `aggiungi_lettura` e `tutte_le_letture` (TODO `2.2`).

3. **Milestone 3 – Soglie e allarmi**  
   **Obiettivo:** aggiungere la logica di verifica soglia (temperatura troppo alta > 50, oppure umidità troppo bassa < 20).  
   1. Scrivi il test in `tests/test_monitor_ambientale.py` (TODO `3.T1`) che usa letture di esempio per verificare l'attivazione dell'allarme.  
   2. Implementa la logica in `src/monitor_ambientale.py`: definisci le costanti/controlli di soglia (TODO `3.1`) e il metodo pubblico per verificare l'allarme (TODO `3.2`).

4. **Milestone 4 – Notificatore esterno (DIP)**  
   **Obiettivo:** introdurre un "notificatore di allarme" esterno che espone `manda_alert(msg)`.  
   1. Integra il mock nel test `tests/test_monitor_ambientale.py` (TODO `4.T1`) per accertarti che il notificatore venga chiamato quando serve.  
   2. In `src/monitor_ambientale.py` passa il notificatore tramite il costruttore (TODO `4.1`), invocalo quando l'allarme scatta (TODO `4.2`) e assicurati di dipendere da un'interfaccia/protocollo, non da un'implementazione concreta (TODO `4.3`).  
   3. Personalizza `src/notificatore.py` (TODO `4.1`) se vuoi simulare comportamenti specifici mantenendo l'interfaccia semplice.

5. **Milestone 5 – Refactor e pulizia**  
   **Obiettivo:** rinomina metodi, estrai funzioni di supporto e rimuovi duplicazioni mantenendo tutti i test verdi. Non ci sono nuovi TODO, ma osserva il codice e valuta: c'è logica che merita un nome più espressivo? Puoi migliorare la leggibilità della verifica soglie? I messaggi di notifica possono essere uniformati? Ricorda che ogni refactor va protetto dai test esistenti.

## Suggerimenti finali
- Scrivi sempre prima il test (lascia che fallisca), poi implementa il codice minimo per farlo passare, quindi rifattorizza se necessario.
- Esegui `pytest` dopo ogni TODO completato per avere feedback immediato.
- Commenta il tuo ragionamento: il TDD è un processo di progettazione guidato dagli esempi.
- Se ti blocchi, torna ai test: descrivi il comportamento desiderato con casi semplici e lascia che guidino l'implementazione.
