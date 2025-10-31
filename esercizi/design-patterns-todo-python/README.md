# Esercizio TODO – Design Pattern GoF

## Perché studiamo i pattern
I design pattern della "Gang of Four" rappresentano un linguaggio comune per discutere soluzioni collaudate a problemi ricorrenti nello sviluppo software orientato agli oggetti. Impararli significa acquisire esempi concreti di come strutturare codice flessibile, manutenibile e pronto all'evoluzione dei requisiti. Questa repository ti offre un percorso guidato per allenarti su ogni pattern, passando dalla teoria all'implementazione.

## Le tre famiglie GoF
### Creational – come vengono creati gli oggetti
Questi pattern ti aiutano a controllare la creazione di istanze, mantenendo coerenza e nascondendo la complessità costruttiva.

### Structural – come si compongono gli oggetti
Qui trovi strategie per organizzare gli oggetti in strutture che favoriscono riuso, estensione e separazione delle responsabilità.

### Behavioral – come collaborano gli oggetti
Questi pattern descrivono modi diversi per gestire la comunicazione e il coordinamento tra oggetti con ruoli differenti.

## Elenco dei pattern
### Creational
- Singleton: garantisce che esista una sola istanza condivisa e fornisce un punto di accesso globale.
- Factory Method: delega la creazione di oggetti a sottoclassi specializzate mantenendo un'interfaccia comune.
- Abstract Factory: produce famiglie di oggetti correlati senza legarsi alle classi concrete.
- Builder: costruisce oggetti complessi passo passo offrendo un'API fluente e leggibile.
- Prototype: crea nuove istanze clonando oggetti esistenti anziché istanziarli da zero.

### Structural
- Adapter: consente a interfacce incompatibili di collaborare tramite un traduttore.
- Bridge: separa astrazione e implementazione permettendone l'evoluzione indipendente.
- Composite: unifica il trattamento di oggetti singoli e composti in strutture gerarchiche.
- Decorator: aggiunge responsabilità a un oggetto dinamicamente avvolgendolo in wrapper compatibili.
- Facade: espone un'interfaccia semplificata verso un sottosistema complesso.
- Flyweight: condivide oggetti leggeri per risparmiare memoria in presenza di molti elementi simili.
- Proxy: controlla l'accesso a un oggetto fornendo un sostituto con la stessa interfaccia.

### Behavioral
- Chain of Responsibility: fa attraversare una richiesta lungo una catena di handler finché uno la gestisce.
- Command: incapsula un'operazione in un oggetto che può essere accodato, loggato o annullato.
- Interpreter: rappresenta una grammatica e ne valuta le frasi con oggetti composti.
- Iterator: fornisce un modo standard di scorrere una collezione senza esporne i dettagli interni.
- Mediator: centralizza la comunicazione tra oggetti riducendo le dipendenze reciproche.
- Memento: salva e ripristina lo stato di un oggetto senza violarne l'incapsulamento.
- Observer: notifica automaticamente più ascoltatori quando cambia lo stato di un soggetto osservato.
- State: incapsula comportamenti alternativi in oggetti stato per evitare condizioni ramificate.
- Strategy: seleziona dinamicamente l'algoritmo più adatto incapsulandolo in un oggetto.
- Template Method: definisce la struttura di un algoritmo rimandando alcuni passi alle sottoclassi.
- Visitor: separa gli algoritmi dalla struttura dati permettendo di aggiungere nuove operazioni senza modificare i nodi.

## Come usare questa repository
1. Scegli una famiglia di pattern e leggi il relativo README di cartella per contestualizzare il tema.
2. Studia con attenzione l'esempio funzionante fornito: è un modello diverso dall'esercizio, utile per chiarire idee e naming.
3. Apri il file `*_pattern.py` corrispondente e completa i `# TODO:` seguendo le indicazioni presenti nella docstring iniziale.
4. Testa manualmente il tuo lavoro creando un piccolo `main.py` personale oppure usando l'interprete interattivo per istanziare le classi e verificare il comportamento.
5. Ripeti il processo per tutti i pattern: l'obiettivo è riconoscere gli schemi ricorrenti e saperli riprodurre in autonomia.

## Obiettivo finale
Al termine del percorso dovrai saper riconoscere i design pattern GoF in colloquio tecnico, motivare quando applicarli e mettere mano a uno scheletro di codice per completarli con sicurezza.
