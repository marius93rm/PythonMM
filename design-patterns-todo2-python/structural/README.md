# Pattern Structural

I pattern **strutturali** spiegano come combinare oggetti e classi per ottenere architetture flessibili, estendibili e con responsabilità ben definite. In questa sezione troverai esempi concreti che mostrano come gestire adattamento, composizione e semplificazione delle dipendenze.

## Adapter
**Che problema risolve**
Capita spesso di voler riutilizzare una libreria esistente che espone un'interfaccia incompatibile con il nostro codice. Il pattern **Adapter** introduce un oggetto ponte che traduce richieste da un'interfaccia all'altra. In questo modo, manteniamo **riuso** del software legacy senza modificarlo e offriamo al nostro sistema un contratto uniforme.

**Esempio pratico in Python (spiegato)**
```python
class LegacyTemperatureSensor:
    def read_celsius(self) -> float:
        return 21.5

class FahrenheitDisplay:
    def show(self, temperature_f: float) -> None:
        print(f"Temperatura: {temperature_f:.1f}°F")

class CelsiusToFahrenheitAdapter:
    def __init__(self, sensor: LegacyTemperatureSensor) -> None:
        self._sensor = sensor

    def read_fahrenheit(self) -> float:
        celsius = self._sensor.read_celsius()
        return celsius * 9 / 5 + 32

sensor = LegacyTemperatureSensor()
adapter = CelsiusToFahrenheitAdapter(sensor)
display = FahrenheitDisplay()
display.show(adapter.read_fahrenheit())
```
L'adapter converte il valore in Fahrenheit senza modificare le classi originali, fungendo da traduttore tra interfacce diverse.

**Cosa devi fare tu nel file `adapter_pattern.py`**
Troverai `AudioPlayer` e `LegacyAudioSystem`. Dovrai implementare l'interfaccia moderna e l'adapter che converte le chiamate da `play_sound()` a `playFile()` mantenendo i TODO come guida.

## Bridge
**Che problema risolve**
Quando un'astrazione può avere più varianti e anche l'implementazione sottostante può cambiare, legarle rigidamente crea una matrice di classi ingestibile. Il pattern **Bridge** separa le due gerarchie: l'astrazione delega a un oggetto implementatore. Così otteniamo **scalabilità** e riduciamo la proliferazione di classi.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None: ...

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API1 disegna cerchio ({x},{y}) r={radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API2 disegna cerchio ({x},{y}) r={radius}")

class Shape(ABC):
    def __init__(self, api: DrawingAPI) -> None:
        self.api = api

    @abstractmethod
    def draw(self) -> None: ...

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, api: DrawingAPI) -> None:
        super().__init__(api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        self.api.draw_circle(self.x, self.y, self.radius)

Circle(0, 0, 10, DrawingAPI1()).draw()
Circle(10, 5, 8, DrawingAPI2()).draw()
```
La classe `Circle` (astrazione) dipende da un `DrawingAPI` (implementazione) che può variare liberamente.

**Cosa devi fare tu nel file `bridge_pattern.py`**
Implementerai `Device` come interfaccia astratta con operazioni come `power_on`, `power_off` e `set_volume`. La classe `RemoteControl` avrà un riferimento a `Device` e dovrai creare remote concrete che invocano i metodi dell'implementazione senza conoscere i dettagli specifici.

## Composite
**Che problema risolve**
Quando gestiamo strutture gerarchiche come filesystem o UI annidate, vogliamo trattare nodi foglia e nodi composti nello stesso modo. Il pattern **Composite** unifica l'interfaccia, così il client interagisce con i nodi senza distinguere se sono singoli o aggregati. Il risultato è una struttura **ricorsiva** facile da percorrere e manipolare.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None: ...

class Dot(Graphic):
    def draw(self) -> None:
        print("Disegno un punto")

class CompoundGraphic(Graphic):
    def __init__(self) -> None:
        self.children: list[Graphic] = []

    def add(self, child: Graphic) -> None:
        self.children.append(child)

    def draw(self) -> None:
        print("Inizio compound")
        for child in self.children:
            child.draw()
        print("Fine compound")

scene = CompoundGraphic()
scene.add(Dot())
scene.add(Dot())
scene.draw()
```
Il client chiama `draw()` sia su singoli punti che sull'oggetto composto, senza dover conoscere la struttura interna.

**Cosa devi fare tu nel file `composite_pattern.py`**
Dovrai definire l'interfaccia `FileSystemNode`, completare `FileNode` e `DirectoryNode` con i TODO richiesti. Il composite deve sommare le dimensioni dei figli e permettere di aggiungerli in modo coerente.

## Decorator
**Che problema risolve**
Talvolta è necessario estendere il comportamento di un oggetto in maniera dinamica, senza ricorrere all'ereditarietà e senza modificare la classe originale. Il pattern **Decorator** avvolge l'oggetto con un wrapper che espone la stessa interfaccia, aggiungendo responsabilità prima o dopo la delega. In questo modo otteniamo **composizione** flessibile.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SlackDecorator(Notifier):
    def __init__(self, wrapped: Notifier) -> None:
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)
        print(f"Slack: {message}")

notifier = SlackDecorator(EmailNotifier())
notifier.send("Build completata")
```
Il decorator aggiunge una notifica su Slack mantenendo la stessa interfaccia `Notifier`.

**Cosa devi fare tu nel file `decorator_pattern.py`**
Implementerai `DataSource` come interfaccia con `read()` e `write()`. `SimpleDataSource` fornirà un comportamento minimale, mentre `LoggingDataSource` dovrà avvolgere un'altra fonte dati per aggiungere log prima di delegare ai metodi reali.

## Facade
**Che problema risolve**
Sistemi complessi spesso espongono molte classi e interazioni complicate. Il pattern **Facade** crea un punto di accesso semplificato che nasconde i dettagli del sottosistema. I client ottengono così un'interfaccia **chiara** e riducono le dipendenze da componenti interni.

**Esempio pratico in Python (spiegato)**
```python
class Light:
    def on(self) -> None:
        print("Luci accese")

    def off(self) -> None:
        print("Luci spente")

class Amplifier:
    def play(self) -> None:
        print("Amplificatore attivo")

    def stop(self) -> None:
        print("Amplificatore spento")

class MovieFacade:
    def __init__(self, light: Light, amp: Amplifier) -> None:
        self.light = light
        self.amp = amp

    def start_movie(self) -> None:
        self.light.off()
        self.amp.play()

    def end_movie(self) -> None:
        self.amp.stop()
        self.light.on()

facade = MovieFacade(Light(), Amplifier())
facade.start_movie()
facade.end_movie()
```
La facade coordina luci e amplificatore con due soli metodi, lasciando nascosti i dettagli del sottosistema.

**Cosa devi fare tu nel file `facade_pattern.py`**
Dovrai creare `VideoConverterFacade` che gestisce `Loader`, `Decoder`, `Encoder` e `Saver`. Il metodo `convert()` deve orchestrare questi componenti nell'ordine suggerito e restituire un messaggio finale riassuntivo.

## Flyweight
**Che problema risolve**
In applicazioni con milioni di oggetti simili, duplicare dati identici è costoso. Il pattern **Flyweight** centralizza lo stato condiviso in un oggetto leggero, riutilizzandolo tramite una factory che gestisce una cache. Il comportamento rimane corretto ma consumiamo molta meno **memoria**.

**Esempio pratico in Python (spiegato)**
```python
class GlyphFlyweight:
    def __init__(self, char: str) -> None:
        self.char = char

    def draw(self, x: int, y: int) -> None:
        print(f"Disegno '{self.char}' in ({x},{y})")

class GlyphFactory:
    def __init__(self) -> None:
        self._pool: dict[str, GlyphFlyweight] = {}

    def get_glyph(self, char: str) -> GlyphFlyweight:
        if char not in self._pool:
            self._pool[char] = GlyphFlyweight(char)
        return self._pool[char]

factory = GlyphFactory()
text = "pattern"
for index, ch in enumerate(text):
    glyph = factory.get_glyph(ch)
    glyph.draw(index, 0)
```
Ogni carattere viene creato una sola volta e riutilizzato per tutte le occorrenze nel testo, evitando duplicazioni inutili.

**Cosa devi fare tu nel file `flyweight_pattern.py`**
Completerai la factory di icone assicurandoti che due richieste identiche ritornino la stessa istanza di `IconFlyweight`. Gestisci la cache e i TODO per evidenziare la differenza tra stato intrinseco e stato estrinseco.

## Proxy
**Che problema risolve**
A volte non vogliamo accedere direttamente a un oggetto perché la creazione è costosa, perché richiede sicurezza, o perché serve controllo addizionale. Il pattern **Proxy** fornisce un sostituto che implementa la stessa interfaccia e gestisce quando e come delegare all'oggetto reale. In questo modo possiamo introdurre **lazy loading** o caching trasparente.

**Esempio pratico in Python (spiegato)**
```python
from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def request(self) -> None: ...

class RealService(Service):
    def request(self) -> None:
        print("Servizio reale: operazione pesante")

class LoggingProxy(Service):
    def __init__(self, real: RealService) -> None:
        self._real = real

    def request(self) -> None:
        print("Proxy: log prima della richiesta")
        self._real.request()

proxy = LoggingProxy(RealService())
proxy.request()
```
Il proxy aggiunge una fase di logging prima di delegare al servizio reale, senza cambiare l'interfaccia del client.

**Cosa devi fare tu nel file `proxy_pattern.py`**
Implementerai l'interfaccia `Image`, la classe `RealImage` che simula un caricamento pesante e `ProxyImage` che ritarda l'istanziazione dell'immagine reale finché `display()` non viene chiamato. Usa i TODO per guidare la logica di lazy loading.
