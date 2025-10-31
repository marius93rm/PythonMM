# Pattern Creational

I pattern **creazionali** affrontano il tema della nascita degli oggetti: quando instanziarli, come controllare le dipendenze e come mantenere coerente la configurazione dell'applicazione. In questa sezione trovi esempi guidati per tutti i pattern GoF di questa famiglia.

## Singleton
**Che problema risolve**
Quando abbiamo bisogno di un'unica istanza condivisa – ad esempio una configurazione globale o un registro di log – vogliamo evitare che parti diverse del codice creino copie indipendenti. Il pattern **Singleton** impone un punto di accesso centralizzato, controllando il ciclo di vita dell'oggetto. In questo modo manteniamo **consistenza** e **sincronizzazione** dei dati condivisi. Inoltre, la creazione ritardata dell'istanza evita lavoro inutile se la risorsa non viene mai richiesta.

**Esempio pratico in Python (spiegato)**
```python
class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._messages = []
        return cls._instance

    def log(self, message: str) -> None:
        self._messages.append(message)

    def dump(self) -> list[str]:
        return list(self._messages)

logger_a = LoggerSingleton()
logger_b = LoggerSingleton()
logger_a.log("Partenza")
logger_b.log("In esecuzione")
print(logger_a.dump())
print("Stesso oggetto?", logger_a is logger_b)
```
Questo esempio mostra un singleton che accumula messaggi. Le due variabili `logger_a` e `logger_b` puntano alla stessa istanza, e la lista interna viene condivisa tra tutti gli utilizzatori.

**Cosa devi fare tu nel file `singleton_pattern.py`**
Troverai lo scheletro di una classe `AppConfig` che deve rispettare il pattern Singleton. Dovrai gestire l'attributo `_instance`, assicurarti che l'inizializzazione avvenga una sola volta e completare le proprietà di configurazione richieste dai TODO.

## Factory Method
**Che problema risolve**
Il pattern **Factory Method** permette di delegare alle sottoclassi la creazione di oggetti concreti. In scenari con tipi multipli – ad esempio notifiche email o SMS – vogliamo invocare un'unica interfaccia senza conoscere le classi specifiche. Così manteniamo **disaccoppiamento** e rendiamo semplice l'aggiunta di nuovi formati.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str: ...

class PdfDocument(Document):
    def render(self) -> str:
        return "Documento PDF pronto"

class HtmlDocument(Document):
    def render(self) -> str:
        return "<html><body>Documento HTML</body></html>"

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document: ...

class PdfFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PdfDocument()

class HtmlFactory(DocumentFactory):
    def create_document(self) -> Document:
        return HtmlDocument()

def generate(factory: DocumentFactory) -> None:
    document = factory.create_document()
    print(document.render())

generate(PdfFactory())
generate(HtmlFactory())
```
Qui ogni factory specializzata crea il documento appropriato. Il codice client chiama `generate` senza sapere nulla delle classi concrete.

**Cosa devi fare tu nel file `factory_method_pattern.py`**
Dovrai definire l'interfaccia `Notification`, implementare le classi concrete per email e SMS, quindi completare una factory che decida il tipo basandosi su una stringa. Ricordati di sollevare `ValueError` quando il tipo richiesto non è riconosciuto.

## Abstract Factory
**Che problema risolve**
Quando dobbiamo creare famiglie di oggetti correlati – come componenti di un tema grafico – serve garantire **coerenza** tra gli elementi generati. L'**Abstract Factory** ci consente di produrre interi insiemi compatibili (es. bottoni e checkbox) senza esporre le classi concrete al client, che invoca solo l'interfaccia di alto livello.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def draw(self) -> str: ...

class Toolbar(ABC):
    @abstractmethod
    def draw(self) -> str: ...

class ClassicWindow(Window):
    def draw(self) -> str:
        return "Finestra classica"

class ClassicToolbar(Toolbar):
    def draw(self) -> str:
        return "Toolbar classica"

class MinimalWindow(Window):
    def draw(self) -> str:
        return "Finestra minimal"

class MinimalToolbar(Toolbar):
    def draw(self) -> str:
        return "Toolbar minimal"

class UIFactory(ABC):
    @abstractmethod
    def create_window(self) -> Window: ...

    @abstractmethod
    def create_toolbar(self) -> Toolbar: ...

class ClassicFactory(UIFactory):
    def create_window(self) -> Window:
        return ClassicWindow()

    def create_toolbar(self) -> Toolbar:
        return ClassicToolbar()

class MinimalFactory(UIFactory):
    def create_window(self) -> Window:
        return MinimalWindow()

    def create_toolbar(self) -> Toolbar:
        return MinimalToolbar()

def render_ui(factory: UIFactory) -> None:
    window = factory.create_window()
    toolbar = factory.create_toolbar()
    print(window.draw())
    print(toolbar.draw())

render_ui(ClassicFactory())
render_ui(MinimalFactory())
```
L'esempio crea componenti coerenti per due temi differenti. Il client `render_ui` non sa quale tema sta utilizzando: interagisce solo con l'interfaccia `UIFactory`.

**Cosa devi fare tu nel file `abstract_factory_pattern.py`**
Completerai le interfacce `Button`, `Checkbox` e `UIComponentFactory`, aggiungendo le versioni Light e Dark. Il metodo `demo_render(factory)` dovrà funzionare con qualsiasi factory concreta senza sapere quale tema è in uso.

## Builder
**Che problema risolve**
Quando un oggetto richiede molti passi di configurazione, costruttori lunghi diventano poco leggibili e fragili. Il pattern **Builder** fornisce una sequenza di metodi fluenti che permettono di costruire gradualmente un prodotto complesso mantenendo **chiarezza** e **riusabilità**. Separare la costruzione dall'oggetto finale rende facile definire configurazioni differenti.

**Esempio pratico in Python (spiegato)**
```python
class Computer:
    def __init__(self) -> None:
        self.cpu = None
        self.ram = None
        self.storage = None

    def __repr__(self) -> str:
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage})"

class ComputerBuilder:
    def __init__(self) -> None:
        self._product = Computer()

    def with_cpu(self, cpu: str) -> "ComputerBuilder":
        self._product.cpu = cpu
        return self

    def with_ram(self, ram: str) -> "ComputerBuilder":
        self._product.ram = ram
        return self

    def with_storage(self, storage: str) -> "ComputerBuilder":
        self._product.storage = storage
        return self

    def build(self) -> Computer:
        return self._product

my_pc = ComputerBuilder().with_cpu("M2").with_ram("16GB").with_storage("512GB SSD").build()
print(my_pc)
```
L'esempio mostra una costruzione passo passo di un oggetto complesso, con metodi fluenti che restituiscono il builder stesso.

**Cosa devi fare tu nel file `builder_pattern.py`**
Implementerai il builder per un oggetto `Meal`, gestendo campi per panino, contorno e bevanda. Dovrai definire il prodotto finale, i metodi fluenti del builder e il metodo `build()` che restituisce la configurazione completa. Nel README troverai anche un approfondimento sulle differenze tra Builder e Factory.

## Prototype
**Che problema risolve**
Quando creare un oggetto richiede molte risorse – ad esempio calcoli o configurazioni complesse – può essere più efficiente clonare un'istanza esistente e modificarla. Il pattern **Prototype** fornisce un contratto `clone()` per duplicare oggetti mantenendo **flessibilità** sugli stati interni. È utile anche per evitare dipendenze dalle classi concrete.

**Esempio pratico in Python (spiegato)**
```python
import copy
from abc import ABC, abstractmethod

class Robot(ABC):
    @abstractmethod
    def clone(self) -> "Robot": ...

class ExplorationRobot(Robot):
    def __init__(self, tools: list[str]) -> None:
        self.tools = tools

    def clone(self) -> "ExplorationRobot":
        return copy.deepcopy(self)

    def add_tool(self, tool: str) -> None:
        self.tools.append(tool)

robot_a = ExplorationRobot(["camera", "sensore" ])
robot_b = robot_a.clone()
robot_b.add_tool("braccio robotico")
print(robot_a.tools)
print(robot_b.tools)
```
Grazie al `clone()` basato su `copy.deepcopy`, `robot_b` possiede una lista indipendente dalla copia originale. L'esempio mette in evidenza la convenienza del cloning rispetto a una nuova costruzione.

**Cosa devi fare tu nel file `prototype_pattern.py`**
Troverai una gerarchia `Shape` con un `Circle` da clonare. Dovrai completare il metodo `clone()` utilizzando il meccanismo suggerito nei TODO e assicurarti che le proprietà principali vengano duplicate correttamente.
