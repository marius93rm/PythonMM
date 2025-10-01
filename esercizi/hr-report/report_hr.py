"""
Esercizio 2 — Report HR: stipendi e performance dipendenti (Pandas)
===================================================================
Obiettivo:
- Caricare CSV (employees, salaries, performance)
- Unire e pulire i dati
- Calcolare aggregazioni per department/role
- Identificare outlier retributivi (IQR)
- Costruire ranking dei top performer (normalizzazione per reparto)
- Esportare un report multi-sheet (Excel) + CSV outlier

Come lavorare:
1) Completa i TODO dentro le funzioni (non cambiare firme e nomi).
2) Lancia i test: `python report_hr.py --test` (devono diventare verdi).
3) Esegui la pipeline completa: `python report_hr.py` (usa cartella data/).

Struttura attesa del progetto:
hr-report/
  data/
    employees.csv
    salaries.csv
    performance.csv
  output/
  report_hr.py
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple, Optional

import numpy as np
import pandas as pd

# =========================
# Configurazione cartelle
# =========================
DATA_DIR = Path("data")
OUT_DIR = Path("output")
OUT_XLSX = OUT_DIR / "hr_summary.xlsx"
OUT_OUTLIERS = OUT_DIR / "hr_outliers.csv"


# =========================
# Funzioni di caricamento
# =========================
def load_data(
    employees_csv: Path,
    salaries_csv: Path,
    performance_csv: Path,
    performance_year: Optional[int] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carica i 3 CSV in DataFrame pandas.

    Atteso:
    - employees.csv -> columns: employee_id, first_name, last_name, department, role, hire_date
      - parse_dates su hire_date
    - salaries.csv  -> columns: employee_id, base_salary, bonus
    - performance.csv -> columns: employee_id, year, rating, goals_met
    - se performance_year è fornito, filtra df_perf su quell'anno

    Ritorna: (df_emp, df_sal, df_perf)
    """
    df_emp = pd.read_csv(employees_csv, parse_dates=["hire_date"])
    df_sal = pd.read_csv(salaries_csv)
    df_perf = pd.read_csv(performance_csv)
    if performance_year is not None:
        df_perf = df_perf[df_perf["year"] == performance_year].copy()
    return df_emp, df_sal, df_perf


# =========================
# Pipeline (TODO per studente)
# =========================
def merge_data(
    df_emp: pd.DataFrame, df_sal: pd.DataFrame, df_perf: pd.DataFrame
) -> pd.DataFrame:
    """
    Unisci employees + salaries (left join su employee_id) e poi con performance (left).
    Richieste:
    - Esegui due merge su 'employee_id' (how='left')
    - Riempi i NaN di 'bonus' con 0
    - Crea 'total_comp' = base_salary + bonus
    - Ritorna il DataFrame risultante

    Suggerimenti:
    - usa df_emp.merge(df_sal, on="employee_id", how="left")
    - poi .merge(df_perf, on="employee_id", how="left")
    - df["bonus"] = df["bonus"].fillna(0)
    - df["total_comp"] = df["base_salary"] + df["bonus"]
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pulizia dati minima:
    - Rimuovi duplicati su employee_id (tieni il primo)
    - Assicurati che hire_date sia datetime (se non lo è, converti con to_datetime)
    - Gestione NaN su campi critici:
        * base_salary: se NaN -> drop riga
        * rating: per semplicità -> drop riga
        * bonus è già stato impostato a 0 in merge_data

    Ritorna il DataFrame pulito (copia).
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def aggregate_by_dept_role(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregazioni per ['department','role'] con:
    - emp_count
    - base_salary: mean, median, std
    - total_comp: mean, median, std
    - rating: mean

    Output:
    - DataFrame aggregato (ok avere colonne con nomi espliciti)
    - Ordinato per department, role

    Hint:
    df.groupby(["department","role"]).agg(
        emp_count=("employee_id","count"),
        base_salary_mean=("base_salary","mean"), ...
    )
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def detect_outliers_iqr(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggiunge colonna booleana 'is_comp_outlier' usando regola IQR PER REPARTO su 'total_comp':

    Per ogni department:
      Q1 = quantile(0.25), Q3 = quantile(0.75)
      IQR = Q3 - Q1
      lower = Q1 - 1.5*IQR
      upper = Q3 + 1.5*IQR
      outlier se total_comp < lower o > upper

    Implementazione tipica:
      - usa groupby('department') e transform per ottenere serie allineate (Q1, Q3)
      - costruisci lower/upper e una colonna booleana finale

    Ritorna una COPIA del DataFrame con la nuova colonna.
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def _min_max_norm_by_group(s: pd.Series, g: pd.Series) -> pd.Series:
    """
    Supporto (già implementata): normalizzazione min-max per gruppo (department).
    valore_norm = (val - min_g) / (max_g - min_g), con gestione divisione per zero.
    """
    grp_min = s.groupby(g).transform("min")
    grp_max = s.groupby(g).transform("max")
    denom = (grp_max - grp_min).replace(0, np.nan)
    norm = (s - grp_min) / denom
    return norm.fillna(0.0)


def build_rankings(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Costruisci ranking per reparto e globale.

    Specifica:
    - rating_norm e goals_norm: min-max normalizzati PER department (usa _min_max_norm_by_group)
    - perf_score = 0.7*rating_norm + 0.3*goals_norm
    - top_performers_by_dept: ordina per department ASC e perf_score DESC, prendi top 10 per reparto
    - top_performers_global: prendi le prime 10 righe per perf_score DESC

    Ritorna: (top_performers_by_dept, top_performers_global)
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def export_report(
    df: pd.DataFrame,
    agg_role_dept: pd.DataFrame,
    top_by_dept: pd.DataFrame,
    top_global: pd.DataFrame,
    out_xlsx: Path,
    out_outliers_csv: Path,
) -> None:
    """
    Esporta:
    - Excel con più sheet: KPI, Aggregati, TopByDept, TopGlobal
      * KPI minimi: n_employees (nunique), mean_total_comp, mean_rating
    - CSV con soli outlier (is_comp_outlier=True)

    Hint:
    with pd.ExcelWriter(out_xlsx) as w:
        kpi_df.to_excel(w, sheet_name="KPI", index=False)
        ...
    df[df["is_comp_outlier"]].to_csv(out_outliers_csv, index=False)
    """
    # --- STUDENTE: IMPLEMENTA QUI ---
    pass


def run_pipeline(
    year: int = 2024,
    employees_csv: Path = DATA_DIR / "employees.csv",
    salaries_csv: Path = DATA_DIR / "salaries.csv",
    performance_csv: Path = DATA_DIR / "performance.csv",
) -> None:
    """
    Esegue l'intera pipeline: load -> merge -> clean -> aggregate -> outliers -> ranking -> export
    Scrive in output/:
      - hr_summary.xlsx
      - hr_outliers.csv
    """
    OUT_DIR.mkdir(exist_ok=True, parents=True)
    df_emp, df_sal, df_perf = load_data(
        employees_csv, salaries_csv, performance_csv, performance_year=year
    )
    df = merge_data(df_emp, df_sal, df_perf)
    df = clean_data(df)
    agg = aggregate_by_dept_role(df)
    df = detect_outliers_iqr(df)
    top_by_dept, top_global = build_rankings(df)
    export_report(df, agg, top_by_dept, top_global, OUT_XLSX, OUT_OUTLIERS)
    print(f"[OK] Report salvato in: {OUT_XLSX}")
    print(f"[OK] Outlier CSV:       {OUT_OUTLIERS}")


# =========================
# TEST (unittest)
# =========================
import unittest
import tempfile
import shutil

SAMPLE_EMP = """employee_id,first_name,last_name,department,role,hire_date
101,Alice,Rossi,Sales,Manager,2019-03-12
102,Bob,Bianchi,Engineering,Developer,2021-07-01
103,Chiara,Verdi,HR,Analyst,2020-11-05
104,Diego,Neri,Engineering,Developer,2018-02-20
"""

SAMPLE_SAL = """employee_id,base_salary,bonus
101,52000,5000
102,45000,2500
103,38000,1500
104,70000,12000
"""

SAMPLE_PERF_2024 = """employee_id,year,rating,goals_met
101,2024,4.5,8
102,2024,3.2,5
103,2024,4.0,7
104,2024,4.8,10
"""


class HRReportTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp(prefix="hr_report_"))
        self.data = self.tmpdir / "data"
        self.out = self.tmpdir / "output"
        self.data.mkdir()
        self.out.mkdir()
        (self.data / "employees.csv").write_text(SAMPLE_EMP, encoding="utf-8")
        (self.data / "salaries.csv").write_text(SAMPLE_SAL, encoding="utf-8")
        (self.data / "performance.csv").write_text(SAMPLE_PERF_2024, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_pipeline_core(self):
        df_emp, df_sal, df_perf = load_data(
            self.data / "employees.csv",
            self.data / "salaries.csv",
            self.data / "performance.csv",
            performance_year=2024,
        )

        # --- merge_data ---
        df = merge_data(df_emp, df_sal, df_perf)
        # Atteso: 4 righe (stessi employees) e total_comp corretta per 101 e 104
        self.assertEqual(len(df), 4, "Il merge deve mantenere cardinalità degli employees (4).")

        # Queste assert passeranno solo dopo aver implementato total_comp
        tc_101 = float(df.loc[df["employee_id"] == 101, "total_comp"].iloc[0])
        tc_104 = float(df.loc[df["employee_id"] == 104, "total_comp"].iloc[0])
        self.assertEqual(tc_101, 52000 + 5000)
        self.assertEqual(tc_104, 70000 + 12000)

        # --- clean_data ---
        df = clean_data(df)
        self.assertFalse(df["base_salary"].isna().any(), "base_salary non deve avere NaN")
        self.assertFalse(df["rating"].isna().any(), "rating non deve avere NaN")

        # --- aggregate_by_dept_role ---
        agg = aggregate_by_dept_role(df).reset_index()
        eng_dev = agg[(agg["department"] == "Engineering") & (agg["role"] == "Developer")]
        self.assertEqual(int(eng_dev["emp_count"].iloc[0]), 2)
        mean_expected = (45000 + 2500 + 70000 + 12000) / 2
        self.assertAlmostEqual(float(eng_dev["total_comp_mean"].iloc[0]), mean_expected, places=6)

        # --- detect_outliers_iqr ---
        df = detect_outliers_iqr(df)
        self.assertIn("is_comp_outlier", df.columns, "Deve esserci la colonna is_comp_outlier")

        # --- build_rankings ---
        top_by_dept, top_global = build_rankings(df)
        self.assertEqual(int(top_global.iloc[0]["employee_id"]), 104, "Con i sample, 104 deve essere primo")

    def test_export(self):
        out_xlsx = self.out / "hr_summary.xlsx"
        out_outliers = self.out / "hr_outliers.csv"

        df_emp, df_sal, df_perf = load_data(
            self.data / "employees.csv",
            self.data / "salaries.csv",
            self.data / "performance.csv",
            performance_year=2024,
        )

        # Pipeline minima per arrivare all'export
        df = merge_data(df_emp, df_sal, df_perf)
        df = clean_data(df)
        df = detect_outliers_iqr(df)
        agg = aggregate_by_dept_role(df)
        top_by_dept, top_global = build_rankings(df)

        # Deve scrivere i file senza errori
        export_report(df, agg, top_by_dept, top_global, out_xlsx, out_outliers)
        self.assertTrue(out_xlsx.exists(), "Deve esistere hr_summary.xlsx")
        self.assertTrue(out_outliers.exists(), "Deve esistere hr_outliers.csv")


# =========================
# Entrypoint CLI
# =========================
def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="HR Report (Pandas) — scheletro per studenti")
    p.add_argument("--test", action="store_true", help="Esegui i test unittari")
    p.add_argument("--year", type=int, default=2024, help="Anno performance (default: 2024)")
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    if args.test:
        # Esegui unittest in-line
        import sys
        # Evita che unittest prenda gli argomenti della CLI del file
        sys.argv = ["ignored"]
        import unittest
        unittest.main(verbosity=2, exit=False)
    else:
        # Esegui pipeline su cartelle di progetto (data/ -> output/)
        OUT_DIR.mkdir(exist_ok=True)
        run_pipeline(year=args.year)
