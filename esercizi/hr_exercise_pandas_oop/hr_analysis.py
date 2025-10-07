# === TODO STUDENTE =============================================
# In questo file costruisci la pipeline di analisi con pandas.
# 1) Valida lo schema CSV in load_employees_csv() (già fatto): aggiungi controlli su valori ammessi.
# 2) Estendi compute_total_compensation() con nuove regole (es. seniority da hire_date).
# 3) In department_stats() aggiungi nuove metriche (std, IQR) e ordina per media desc.
# 4) In generate_reports() esporta anche un JSON e opzionalmente un grafico (matplotlib).
# Suggerimento: mantieni compatibile l'output attuale per far passare i test.
# ================================================================

from __future__ import annotations

import os
import pandas as pd
from hr_domain import SchemaValidationError

REQUIRED_EMP_COLS = [
    "employee_id","first_name","last_name","role","level","department","cost_center",
    "contract_type","base_salary","bonus_percent","workload_percent","currency","gender","hire_date"
]

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def load_employees_csv(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File non trovato: {path}")
    df = pd.read_csv(path, parse_dates=["hire_date"])
    missing = [c for c in REQUIRED_EMP_COLS if c not in df.columns]
    if missing:
        raise SchemaValidationError(f"Colonne mancanti in employees.csv: {missing}")
    df["employee_id"] = df["employee_id"].astype(int)
    # TODO: verifica che employee_id sia univoco se vuoi gestire DuplicateEmployeeError
    df["level"] = df["level"].astype(int)
    df["base_salary"] = df["base_salary"].astype(float)
    df["bonus_percent"] = df["bonus_percent"].astype(float)
    df["workload_percent"] = df["workload_percent"].astype(float)
    return df

def compute_total_compensation(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: aggiungi fattori (seniority, performance) o limiti ai bonus
    # === INIZIO AREA STUDENTE ===
    # Esempi di estensioni:
    # - Calcola 'seniority_years' da hire_date e applica un bonus extra (es. +0.5% per anno, max +5%).
    # - Cliff dei bonus: cap tra 0 e 30.
    # - Diversi contratti possono avere regole distinte.
    # Suggerimenti pandas: pd.to_datetime, df.assign, df.apply, np.clip.
    # === FINE AREA STUDENTE ===
    df = df.copy()
    def row_comp(r):
        base = r["base_salary"] * r["workload_percent"]
        if r["contract_type"] == "contractor":
            return base
        bonus = (r["bonus_percent"] or 0.0) / 100.0
        extra_manager = 0.05 if r["role"].lower() == "manager" else 0.0
        return base * (1.0 + bonus + extra_manager)
    df["total_compensation"] = df.apply(row_comp, axis=1)
    return df

def department_stats(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: aggiungi ulteriori aggregazioni (std, var) e ranking
    # === INIZIO AREA STUDENTE ===
    # Aggiungi metriche come deviazione standard, varianza, IQR.
    # Ordina i reparti per 'mean' desc e aggiungi una colonna di ranking.
    # Suggerimenti pandas: .agg({...}), .rank(), .sort_values().
    # === FINE AREA STUDENTE ===
    if "total_compensation" not in df.columns:
        df = compute_total_compensation(df)
    agg = df.groupby("department").agg(
        count=("total_compensation","count"),
        mean=("total_compensation","mean"),
        median=("total_compensation","median"),
        min=("total_compensation","min"),
        max=("total_compensation","max"),
    ).reset_index()
    for col in ["mean","median","min","max"]:
        agg[col] = agg[col].round(2)
    return agg

def generate_reports(employees_csv: str, out_dir: str):
    # TODO: salva anche un report JSON e un grafico a barre per reparto
    # === INIZIO AREA STUDENTE ===
    # Esporta anche un file JSON (usa DataFrame.to_json) con stats di reparto.
    # Genera un grafico a barre (matplotlib) con media retribuzioni per reparto.
    # Salva il grafico in out_dir come 'department_salary_summary.png'.
    # === FINE AREA STUDENTE ===
    ensure_dir(out_dir)
    df = load_employees_csv(employees_csv)
    df = compute_total_compensation(df)
    stats = department_stats(df)
    csv_out = os.path.join(out_dir, "department_salary_summary.csv")
    stats.to_csv(csv_out, index=False)
    md_out = os.path.join(out_dir, "payroll_overview.md")
    total_payroll = df["total_compensation"].sum()
    lines = [
        "# Payroll Overview",
        "",
        f"Totale payroll annuo (stima): **{total_payroll:.2f}**",
        "",
        "## Riepilogo per reparto",
        stats.to_markdown(index=False),
        "",
        "Generato automaticamente."
    ]
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("\\n".join(lines))
    return {"csv": csv_out, "md": md_out}

# === INIZIO AREA STUDENTE ===
# Funzioni helper opzionali per arricchire i report (es. normalizzazione valuta, filtri per data, ecc.)
# Definisci nuove funzioni qui e richiamale in generate_reports.
# === FINE AREA STUDENTE ===
