# Guida Studente — Gestione Dipendenti e Stipendi (Pandas + OOP)

## Obiettivo
Implementare un mini-sistema HR che unisce **OOP** (classi, ereditarietà, ABC, gestione errori) con **analisi dati** tramite **pandas**.  
I test (`tests_hr.py`) sono già pronti: non modificarli. Eseguili con:

```bash
python hr_app.py
# poi premi Invio
```

## Dove scrivere il codice
- **Dominio OOP:** `hr_domain.py`
  - Lavora sulle classi `Worker` (ABC), `Employee`, `Manager`, `Contractor`.
  - Vedi i commenti `# TODO` nel file per i punti da implementare/estendere.
- **Pandas & Report:** `hr_analysis.py`
  - Caricamento CSV, calcolo `total_compensation`, statistiche per reparto e report.
  - Vedi i commenti `# TODO` nel file per estensioni suggerite.

## Checklist minima
- [ ] Validazioni dati (es. bonus 0–100, workload (0,1], currency ammessa)
- [ ] Calcolo `total_compensation` coerente con le regole del dominio
- [ ] Statistiche per reparto: count, mean, median, min, max
- [ ] Export report CSV + Markdown

## Estensioni consigliate
- [ ] `SeniorManager` con +10% extra
- [ ] `annual_bonus_value` su Employee
- [ ] Nuove metriche (std, var, IQR) e ordinamento reparti
- [ ] Report JSON e grafico a barre per reparto (matplotlib)
- [ ] Verifica `employee_id` univoco e gestione `DuplicateEmployeeError`

## Dati
I CSV sono in `data/`:
- `employees.csv` (anagrafica e retribuzioni)
- `departments.csv` (mappatura reparto → cost center)

Buon lavoro! Le modifiche non devono rompere le API usate dai test. Se i test falliscono, ripristina i metodi coinvolti mantenendo le **estensioni come additive**, non breaking.


## Aree studente nel codice
Cerca i blocchi:
```text
# === INIZIO AREA STUDENTE ===
# (istruzioni)
# === FINE AREA STUDENTE ===
```
Sono presenti in:
- `hr_domain.py`: dentro `validate()`, nelle classi `Employee`, `Manager`, `Contractor` e in fondo per nuove sottoclassi.
- `hr_analysis.py`: dentro `compute_total_compensation`, `department_stats`, `generate_reports`, e in coda per helper extra.
