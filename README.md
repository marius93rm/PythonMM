# 📚 Corso Python — Materiale & Esercizi

![Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python\&logoColor=white)
![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)

Repository ufficiale del corso Python curato da **Marius Minia**. Troverai un percorso completo che parte dalle basi del linguaggio 🐍 e arriva a concetti avanzati come **OOP**, principi **SOLID**, design pattern e **analisi dati con Pandas**. Ogni modulo include slide, esercizi guidati, soluzioni commentate e materiale di supporto.

---

## 🗂 Struttura della repo

```
PYTHONMM/
│
├── 📂 esercizi/                # Percorso graduato di esercizi e mini–progetti
│   ├── 01-fondamenti-funzioni/
│   │   ├── esercizio_01_fondamenti_python.py
│   │   ├── esercizio_02_generatori_slicing.py
│   │   ├── esercizio_03_list_comprehension.py
│   │   ├── esercizio_04_compito_funzioni.py
│   │   ├── soluzione_01_fondamenti_python.py
│   │   └── soluzione_02_generatori_slicing.py
│   ├── 02-data-framework/
│   │   ├── brief_05_data_framework.pdf
│   │   ├── esercizio_05_data_framework.py
│   │   └── soluzione_05_data_framework.py
│   ├── 03-hr-report/
│   │   ├── data/
│   │   ├── notebook/
│   │   ├── esercizio_06_hr_report.py
│   │   ├── soluzione_06_hr_report.py
│   │   ├── supporto_06_hr_report_compendio.pdf
│   │   └── supporto_06_hr_report_funzioni.pdf
│   ├── 04-piattaforma-notifiche/
│   │   ├── esercizio_07_piattaforma_notifiche.py
│   │   ├── soluzione_07_piattaforma_notifiche.py
│   │   ├── milestone_07_piattaforma_notifiche.pdf
│   │   └── supporto_07_piattaforma_notifiche.pdf
│   ├── 05-sistema-hr/
│   │   ├── esercizio_08_sistema_hr.py
│   │   └── soluzione_08_sistema_hr.py
│   ├── 06-hr-analytics/
│   │   ├── data/
│   │   ├── reports/
│   │   ├── esercizio_09_hr_app.py
│   │   ├── hr_analysis.py
│   │   ├── hr_domain.py
│   │   ├── tests_hr.py
│   │   ├── requirements.txt
│   │   ├── README.md
│   │   └── STUDENT_GUIDE.md
│   ├── 07-randomuser/
│   │   ├── brief_10_randomuser.pdf
│   │   ├── esercizio_10_randomuser_scheletro.py
│   │   └── soluzione_10_randomuser.py
│   ├── 08-todo/
│   │   ├── esercizio_11_todo_milestone.py
│   │   └── soluzione_11_todo_milestone.py
│   ├── 09-logger-universale/
│   │   └── esercizio_12_logger_universale.py
│   └── 10-PomodoroPythonExercise/
│       ├── README.md
│       ├── compendio.pdf
│       ├── pyproject.toml
│       ├── src/
│       └── tests/
│
├── 📂 slide/                  # Slide numerate del corso (01 ➝ 12)
│   ├── 01-introduzione-python.pdf
│   ├── 02-recap-base.pdf
│   ├── 03-recap-avanzato.pdf
│   ├── 04-programmazione-oggetti.pdf
│   ├── 05-python-avanzato-argomenti-chiave.pdf
│   ├── 06-automazione-testing.pdf
│   ├── 07-sviluppo-web-python.pdf
│   ├── 08-sviluppo-api.pdf
│   ├── 09-visualizzazione-matplotlib.pdf
│   ├── 10-analisi-dati-pandas.pdf
│   ├── 11-lezione-pandas.pdf
│   └── 12-cheatsheet-sqlite.pdf
│
├── 📂 notebook/               # Notebook interattivi e dati di supporto
│   ├── HR_Analysis_OOP_walkthrough.ipynb
│   ├── explore_hr_data.ipynb
│   ├── report.ipynb
│   ├── data/
│   └── pyvenv.cfg
│
├── 📂 extra/                  # Approfondimenti, cheat sheet e script extra
│   ├── Pandas con esempi.pdf
│   ├── SOLID.pdf
│   ├── SOLID.png
│   ├── oop2altro.pdf
│   └── pjwt.py
│
└── 📖 README.md
```

📌 Ogni risorsa porta un **prefisso numerico** che indica l'ordine consigliato di studio: le slide guidano la teoria mentre le cartelle in `esercizi/` raccolgono attività pratiche, supporti PDF e soluzioni complete.

---

## 🧭 Percorso di studio consigliato

| Modulo | Focus principale | Materiali correlati |
| --- | --- | --- |
| 01 — Fondamenti | Sintassi base, funzioni, generatori e list comprehension | `esercizi/01-fondamenti-funzioni`, slide 01-03 |
| 02 — Data Framework | Gestione dati strutturati, pulizia e trasformazioni | `esercizi/02-data-framework`, slide 05 |
| 03 — HR Report | Analisi dati HR e reportistica in Python | `esercizi/03-hr-report`, notebook `explore_hr_data.ipynb`, slide 09-11 |
| 04 — Piattaforma notifiche | Automazione e gestione eventi | `esercizi/04-piattaforma-notifiche`, slide 06-08 |
| 05 — Sistema HR | Applicazioni a oggetti con focus su dominio HR | `esercizi/05-sistema-hr`, slide 04-06 |
| 06 — HR Analytics | Applicazione completa con dominio, test e report | `esercizi/06-hr-analytics`, notebook `HR_Analysis_OOP_walkthrough.ipynb` |
| 07 — RandomUser | Integrazione API e parsing di risposte JSON | `esercizi/07-randomuser`, slide 08 |
| 08 — To-Do | Gestione attività e milestone applicative | `esercizi/08-todo`, slide 07 |
| 09 — Logger universale | Pattern Singleton e logging condiviso | `esercizi/09-logger-universale`, slide 05-06 |
| 10 — Pomodoro | Applicazione Pomodoro con timer e interfaccia testuale | `esercizi/10-PomodoroPythonExercise`, materiali extra |

---

## 🛠️ Come utilizzare il materiale

1. **Consulta le slide** per una panoramica teorica dell'argomento.
2. **Leggi il brief PDF** (quando presente) nella cartella dell'esercizio per capire obiettivi e requisiti.
3. **Lavora sugli esercizi** partendo dai file `esercizio_*.py` o dagli scaffold forniti.
4. **Confronta la tua soluzione** con i file `soluzione_*.py` o con i notebook di walkthrough.
5. **Approfondisci** con i documenti in `extra/` e sperimenta con gli script di esempio (`pjwt.py`, ecc.).

Suggerimento: mantieni un ambiente virtuale dedicato per il corso e salva gli esercizi svolti in una cartella separata per seguire i progressi nel tempo.

---

## 📓 Notebook & dataset

I notebook nella cartella `notebook/` riprendono gli esercizi più articolati (soprattutto il modulo HR) e contengono walkthrough completi, analisi esplorative e report automatici. Tutti i dataset necessari sono disponibili nelle relative sottocartelle `data/`, sia qui che dentro `esercizi/03-hr-report` e `esercizi/06-hr-analytics`.

Puoi aprire i notebook con Jupyter o VS Code:

```bash
python -m venv .venv
source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install jupyter pandas matplotlib
jupyter notebook
```

---

## ⚙️ Requisiti e setup

- **Python 3.12** (consigliato) – in linea con le slide e con i badge della repo.
- Alcuni esercizi forniscono un proprio `requirements.txt`, ad esempio `esercizi/06-hr-analytics/requirements.txt`, da installare nel tuo ambiente virtuale.
- Per eseguire i test del modulo HR Analytics:
  ```bash
  cd esercizi/06-hr-analytics
  pip install -r requirements.txt
  pytest
  ```
- I progetti non richiedono database esterni: i dataset sono inclusi o generati via script.

---

## 💡 Suggerimenti didattici

- Le soluzioni sono pensate per il confronto: prova sempre prima a completare gli esercizi in autonomia.
- Usa i materiali `extra/` per recuperare o consolidare concetti teorici (OOP, SOLID, Pandas).
- Ogni cartella contiene PDF di supporto con milestone, compendi e schede riepilogative: sfruttali come checklist di revisione.

Buono studio e buon divertimento! 🐍
