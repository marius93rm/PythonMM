# Test automatici per gli esercizi `design-patterns-todo2`

Questa cartella contiene una suite di test pronta all'uso per verificare le
soluzioni degli esercizi. I test utilizzano [pytest](https://pytest.org), uno
strumento standard dell'ecosistema Python.

## Requisiti

Assicurati di avere installato `pytest` nell'ambiente virtuale in cui stai
sviluppando gli esercizi:

```bash
pip install pytest
```

## Come eseguire i test

Posizionati nella cartella principale del repository (quella che contiene la
sottocartella `design-patterns-todo2-python`) ed esegui:

```bash
pytest design-patterns-todo2-python/tests
```

Il comando eseguirà tutti i test presenti nella cartella. In alternativa puoi
lanciare un singolo file di test, ad esempio:

```bash
pytest design-patterns-todo2-python/tests/behavioral/test_strategy_pattern.py
```

I test sono organizzati in tre sottocartelle (`behavioral`, `creational`,
`structural`) che rispecchiano le famiglie dei pattern affrontati.

## Suggerimenti

* I test riflettono il comportamento atteso dalle consegne: se alcuni TODO non
  sono ancora stati completati è normale che i test falliscano.
* Usa l'opzione `-k` di pytest per filtrare rapidamente un sottoinsieme dei
  test mentre stai lavorando su un pattern specifico.
