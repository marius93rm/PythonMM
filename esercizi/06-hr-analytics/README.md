# Esercizio: Gestione Dipendenti e Stipendi (Pandas + OOP)

Obiettivo: costruire un mini-sistema HR che carica dati CSV con **pandas**, modella la logica con **classi** (incluse **classi astratte** ed **ereditarietà**), esegue **analisi statistiche** e genera **report**. Include **gestione errori** e **test** eseguibili premendo Invio.

## 1) Creare e attivare un virtual env

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Se non vuoi usare `requirements.txt`, puoi installare direttamente: `pip install pandas`.

## 2) Struttura cartelle
```
06-hr-analytics/
├─ data/
│  ├─ employees.csv
│  ├─ departments.csv
├─ reports/              # qui verranno salvati i report
├─ hr_domain.py          # classi e dominio OOP
├─ hr_analysis.py        # funzioni pandas per analisi e report
├─ tests_hr.py           # test
├─ esercizio_09_hr_app.py  # entrypoint: premi Invio per lanciare i test
├─ requirements.txt
└─ README.md
```

## 3) Eseguire i test
Nell'ambiente virtuale attivo:
```bash
python esercizio_09_hr_app.py
```
Quando richiesto, **premi Invio** per eseguire i test. Al termine, trovi i report in `./reports`.
