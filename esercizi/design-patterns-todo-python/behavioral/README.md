# Pattern Behavioral

I pattern **comportamentali** descrivono come gli oggetti collaborano fra loro, come condividono responsabilità e come reagiscono ai cambi di stato. Questa sezione offre una guida dettagliata per ogni pattern della famiglia, con esempi concreti e indicazioni operative.

## Chain of Responsibility
**Che problema risolve**
Quando una richiesta può essere gestita da attori diversi, vogliamo incanalarla attraverso una catena fino a trovare chi se ne occupa. Il pattern **Chain of Responsibility** permette di collegare handler in sequenza, evitando `if` annidati e rendendo **estendibile** l'aggiunta di nuovi passaggi nella catena.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class SupportTicket:
    def __init__(self, severity: str) -> None:
        self.severity = severity

class Handler(ABC):
    def __init__(self) -> None:
        self.next_handler: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self.next_handler = handler
        return handler

    def handle(self, ticket: SupportTicket) -> None:
        if self.next_handler:
            self.next_handler.handle(ticket)

class Tier1Handler(Handler):
    def handle(self, ticket: SupportTicket) -> None:
        if ticket.severity == "low":
            print("Tier1 gestisce il ticket")
        else:
            super().handle(ticket)

class Tier2Handler(Handler):
    def handle(self, ticket: SupportTicket) -> None:
        if ticket.severity == "medium":
            print("Tier2 gestisce il ticket")
        else:
            super().handle(ticket)

Tier1Handler().set_next(Tier2Handler()).handle(SupportTicket("medium"))
```
Ogni handler decide se gestire la richiesta o passarla al successivo, mantenendo il codice modulare.

**Cosa devi fare tu nel file `chain_of_responsibility_pattern.py`**
Dovrai modellare una catena di logger per livelli INFO, WARNING ed ERROR. Completa la classe base con il riferimento al successivo e implementa i TODO nei gestori concreti.

## Command
**Che problema risolve**
Quando vogliamo trattare un'azione come un oggetto – ad esempio per annullarla o accodarla – il pattern **Command** incapsula l'operazione e il suo ricevitore. Questo consente di implementare **undo**, scripting e macro mantenendo un'interfaccia uniforme.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Light:
    def __init__(self) -> None:
        self.is_on = False

    def switch(self) -> None:
        self.is_on = not self.is_on
        print("Luce accesa" if self.is_on else "Luce spenta")

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

class SwitchCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.switch()

class RemoteInvoker:
    def __init__(self) -> None:
        self.history: list[Command] = []

    def press(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

invoker = RemoteInvoker()
light = Light()
invoker.press(SwitchCommand(light))
invoker.press(SwitchCommand(light))
```
Ogni comando incapsula l'azione `switch`, e il remote mantiene una history delle operazioni eseguite.

**Cosa devi fare tu nel file `command_pattern.py`**
Troverai uno scheletro per un editor di testo con comandi `AppendTextCommand` e `ClearTextCommand`. Dovrai completare l'interfaccia `Command`, definire le classi concrete e gestire la history nell'invoker come indicato dai TODO.

## Interpreter
**Che problema risolve**
Quando una grammatica è relativamente semplice e si desidera un interprete specializzato, il pattern **Interpreter** rappresenta ogni regola con una classe dedicata. In questo modo possiamo costruire espressioni complesse come alberi, mantenendo **leggibilità** e facilitando l'estensione con nuovi simboli.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict[str, int]) -> int: ...

class Number(Expression):
    def __init__(self, value: int) -> None:
        self.value = value

    def interpret(self, context: dict[str, int]) -> int:
        return self.value

class Variable(Expression):
    def __init__(self, name: str) -> None:
        self.name = name

    def interpret(self, context: dict[str, int]) -> int:
        return context[self.name]

class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self.left.interpret(context) + self.right.interpret(context)

expr = Add(Number(5), Variable("x"))
print(expr.interpret({"x": 3}))
```
L'espressione calcola il valore di un albero composto da numeri e variabili, delegando il calcolo alle sottoparti.

**Cosa devi fare tu nel file `interpreter_pattern.py`**
Costruirai un linguaggio booleano con espressioni `VarExpr`, `NotExpr`, `AndExpr` e `OrExpr`. Implementa il metodo `interpret(context)` nei punti indicati, rispettando l'interfaccia `BooleanExpr`.

## Iterator
**Che problema risolve**
Collezioni diverse richiedono modi differenti di attraversamento, ma vogliamo presentare un'interfaccia uniforme. Il pattern **Iterator** incapsula l'algoritmo di percorrenza in un oggetto dedicato, mantenendo **incapsulamento** dei dettagli della collezione.

**Esempio pratico in Python (spiegato)**
```python
class ReverseIterator:
    def __init__(self, data: list[int]) -> None:
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

numbers = [1, 2, 3]
for value in ReverseIterator(numbers):
    print(value)
```
L'iteratore scorre la lista al contrario senza esporre i dettagli di implementazione al codice client.

**Cosa devi fare tu nel file `iterator_pattern.py`**
Dovrai creare una classe `Playlist` con un iteratore personalizzato. Completa i TODO nella logica di `__next__` e gestisci la collezione interna in modo sicuro.

## Mediator
**Che problema risolve**
Sistemi con molti oggetti che comunicano tra loro possono diventare fragili a causa delle dipendenze incrociate. Il pattern **Mediator** introduce un oggetto centrale che coordina i partecipanti, promuovendo **disaccoppiamento** e semplificando le interazioni.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class AirTrafficMediator(ABC):
    @abstractmethod
    def notify(self, sender: "Aircraft", message: str) -> None: ...

class ControlTower(AirTrafficMediator):
    def __init__(self) -> None:
        self.aircrafts: list[Aircraft] = []

    def register(self, aircraft: "Aircraft") -> None:
        self.aircrafts.append(aircraft)

    def notify(self, sender: "Aircraft", message: str) -> None:
        for aircraft in self.aircrafts:
            if aircraft is not sender:
                aircraft.receive(message)

class Aircraft:
    def __init__(self, name: str, mediator: AirTrafficMediator) -> None:
        self.name = name
        self.mediator = mediator
        self.mediator.register(self)

    def send(self, message: str) -> None:
        print(f"{self.name} invia: {message}")
        self.mediator.notify(self, message)

    def receive(self, message: str) -> None:
        print(f"{self.name} riceve: {message}")

mediator = ControlTower()
a1 = Aircraft("A1", mediator)
a2 = Aircraft("A2", mediator)
a1.send("Richiedo atterraggio")
```
La torre di controllo inoltra i messaggi agli altri aeromobili, che non hanno riferimenti diretti fra loro.

**Cosa devi fare tu nel file `mediator_pattern.py`**
Dovrai creare `ChatRoomMediator` e la classe `User` che invia messaggi tramite il mediatore. Completa i TODO su registrazione utenti e smistamento dei messaggi.

## Memento
**Che problema risolve**
Quando serve poter annullare modifiche o ripristinare uno stato precedente, vogliamo memorizzare uno snapshot senza esporre i dettagli interni. Il pattern **Memento** separa l'oggetto originatore dallo stato salvato, consentendo **undo/redo** sicuri.

**Esempio pratico in Python (spiegato)**
```python
class GameMemento:
    def __init__(self, level: int, score: int) -> None:
        self.level = level
        self.score = score

class Game:
    def __init__(self) -> None:
        self.level = 1
        self.score = 0

    def save(self) -> GameMemento:
        return GameMemento(self.level, self.score)

    def restore(self, memento: GameMemento) -> None:
        self.level = memento.level
        self.score = memento.score

class GameHistory:
    def __init__(self) -> None:
        self._states: list[GameMemento] = []

    def push(self, memento: GameMemento) -> None:
        self._states.append(memento)

    def pop(self) -> GameMemento:
        return self._states.pop()

```
Questo esempio mostra come salvare lo stato di un gioco e ripristinarlo in seguito. La storia tiene una pila di memento.

**Cosa devi fare tu nel file `memento_pattern.py`**
Nel file dedicato creerai `EditorMemento`, `TextEditor` e `HistoryCaretaker`. Dovrai gestire i TODO per salvare e ripristinare il contenuto testuale, mantenendo l'incapsulamento.

## Observer
**Che problema risolve**
Quando un oggetto deve notificare automaticamente molti ascoltatori dei cambiamenti, il pattern **Observer** decoupla il soggetto dagli osservatori. In questo modo otteniamo aggiornamenti **push** coordinati senza bisogno di polling manuale.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: "Observer") -> None:
        self._observers.append(observer)

    def notify(self, data: str) -> None:
        for observer in self._observers:
            observer.update(data)

class Observer(ABC):
    @abstractmethod
    def update(self, data: str) -> None: ...

class NewsAgency(Subject):
    def publish(self, news: str) -> None:
        self.notify(news)

class EmailSubscriber(Observer):
    def update(self, data: str) -> None:
        print(f"Email ricevuta: {data}")

agency = NewsAgency()
subscriber = EmailSubscriber()
agency.attach(subscriber)
agency.publish("Breaking news")
```
Il soggetto `NewsAgency` notifica tutti gli osservatori registrati senza conoscerne i dettagli concreti.

**Cosa devi fare tu nel file `observer_pattern.py`**
Completerai `WeatherStation` come soggetto e `DisplayObserver` come osservatori. Gestisci registrazione, rimozione e notifica secondo i TODO.

## State
**Che problema risolve**
Oggetti che cambiano comportamento in base a uno stato interno spesso finiscono con `if` o `switch` ingombranti. Il pattern **State** sposta le varianti di comportamento in classi dedicate, permettendo **transizioni** esplicite e più manutenibili.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, light: "TrafficLight") -> None: ...

class GreenState(TrafficLightState):
    def handle(self, light: "TrafficLight") -> None:
        print("Verde -> Giallo")
        light.state = YellowState()

class YellowState(TrafficLightState):
    def handle(self, light: "TrafficLight") -> None:
        print("Giallo -> Rosso")
        light.state = RedState()

class RedState(TrafficLightState):
    def handle(self, light: "TrafficLight") -> None:
        print("Rosso -> Verde")
        light.state = GreenState()

class TrafficLight:
    def __init__(self) -> None:
        self.state: TrafficLightState = GreenState()

    def change(self) -> None:
        self.state.handle(self)

light = TrafficLight()
light.change()
light.change()
light.change()
```
Ogni stato decide la transizione successiva, mantenendo il comportamento distribuito nelle classi corrette.

**Cosa devi fare tu nel file `state_pattern.py`**
Troverai la classe `Order` e gli stati `NewOrderState`, `ShippedOrderState` e `DeliveredOrderState`. Completa i TODO per gestire `next_step()` e aggiornare lo stato corrente dell'ordine.

## Strategy
**Che problema risolve**
Quando esistono più algoritmi possibili per svolgere un compito, vogliamo poterli intercambiare facilmente senza duplicare codice. Il pattern **Strategy** incapsula ogni algoritmo in una classe separata, consentendo **selezione dinamica** a runtime.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]: ...

class AscendingSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)

class DescendingSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def execute(self, data: list[int]) -> list[int]:
        return self.strategy.sort(data)

sorter = Sorter(AscendingSort())
print(sorter.execute([3, 1, 2]))
sorter.set_strategy(DescendingSort())
print(sorter.execute([3, 1, 2]))
```
Il client può cambiare algoritmo di ordinamento semplicemente sostituendo la strategia.

**Cosa devi fare tu nel file `strategy_pattern.py`**
Definirai `TextFormatStrategy` e le strategie concrete per maiuscole, minuscole e Title Case. Completa anche la classe `TextFormatter` e i TODO che gestiscono il cambio di strategia.

## Template Method
**Che problema risolve**
Quando esiste una sequenza fissa di passi, ma alcune fasi devono essere specializzate, il pattern **Template Method** codifica lo scheletro dell'algoritmo nella superclasse e delega i dettagli alle sottoclassi. In questo modo otteniamo **consistenza** e riuso del flusso generale.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class DataExporter(ABC):
    def export(self) -> None:
        data = self.fetch()
        processed = self.process(data)
        self.write(processed)

    @abstractmethod
    def fetch(self) -> list[str]: ...

    @abstractmethod
    def process(self, data: list[str]) -> str: ...

    @abstractmethod
    def write(self, result: str) -> None: ...

class CsvExporter(DataExporter):
    def fetch(self) -> list[str]:
        return ["nome", "cognome"]

    def process(self, data: list[str]) -> str:
        return ";".join(data)

    def write(self, result: str) -> None:
        print(f"Scrivo CSV: {result}")

CsvExporter().export()
```
Il metodo `export()` fissa la sequenza, mentre le sottoclassi specializzano i passi.

**Cosa devi fare tu nel file `template_method_pattern.py`**
Nel file troverai `ReportGenerator` come classe astratta con `run()` già impostato. Dovrai implementare i metodi astratti per caricamento, elaborazione e render nei TODO e creare esempi di report concreti.

## Visitor
**Che problema risolve**
Quando vogliamo aggiungere nuove operazioni su una gerarchia di classi senza modificarla, il pattern **Visitor** sposta la logica nell'oggetto visitatore. Ogni nodo accetta un visitor e gli delega il comportamento, ottenendo **apertura** a nuove operazioni e stabilità della struttura dati.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class FileElement(ABC):
    @abstractmethod
    def accept(self, visitor: "FileVisitor") -> None: ...

class TextFile(FileElement):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def accept(self, visitor: "FileVisitor") -> None:
        visitor.visit_text(self)

class ImageFile(FileElement):
    def __init__(self, name: str, resolution: str) -> None:
        self.name = name
        self.resolution = resolution

    def accept(self, visitor: "FileVisitor") -> None:
        visitor.visit_image(self)

class FileVisitor(ABC):
    @abstractmethod
    def visit_text(self, element: TextFile) -> None: ...

    @abstractmethod
    def visit_image(self, element: ImageFile) -> None: ...

class ReportVisitor(FileVisitor):
    def visit_text(self, element: TextFile) -> None:
        print(f"Testo {element.name}, {element.size}KB")

    def visit_image(self, element: ImageFile) -> None:
        print(f"Immagine {element.name}, {element.resolution}")

files: list[FileElement] = [TextFile("app.log", 120), ImageFile("logo.png", "1024x768")]
visitor = ReportVisitor()
for element in files:
    element.accept(visitor)
```
Il visitor `ReportVisitor` aggiunge un'operazione senza modificare le classi `TextFile` e `ImageFile`.

**Cosa devi fare tu nel file `visitor_pattern.py`**
Dovrai definire il visitor per un piccolo AST composto da `NumberNode` e `AddNode`, oltre a un visitor che calcola il valore o stampa l'albero. Completa i TODO su `accept()` e sui metodi `visit_*` del visitor.
