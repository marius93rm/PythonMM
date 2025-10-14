#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Progetto (scheletro): Analisi utenti da randomuser.me
Milestones:
  1) Pulizia dati e validazione
  2) Statistiche demografiche
  3) Analisi dei nomi
  4) Sistema di matching / suggerimenti
  5) Export CSV (first,last,email,phone)

Esecuzione (esempio):
  python progetto_randomuser_scheletro.py --results 100 --nat "us,it,dk" --gender "male,female" --seed "corso123"

Dipendenze:
  pip install requests
"""

from __future__ import annotations
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import requests

# ==============================
# DATA MODEL
# ==============================

@dataclass
class User:
    uuid: str
    first: str
    last: str
    email: str
    gender: str
    country: str
    age: int
    nat: str
    phone: str
    lat: float
    lon: float

    @property
    def full_name(self) -> str:
        return f"{self.first} {self.last}"


# ==============================
# COSTANTI / UTILITIES
# ==============================

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Analisi utenti randomuser.me (scheletro)")
    p.add_argument("--results", type=int, default=50, help="Numero di utenti da scaricare")
    p.add_argument("--nat", type=str, default=None, help='Nazionalità (es: "us,it,dk")')
    p.add_argument("--gender", type=str, default=None, help='Genere (es: "male,female")')
    p.add_argument("--seed", type=str, default=None, help="Seed per risultati ripetibili")
    p.add_argument("--outdir", type=str, default="out", help="Cartella di output")
    return p.parse_args()


# ==============================
# MILESTONE 0 — FETCH & MAPPING
#   Obiettivo: scaricare utenti dall’API e mapparli nel dataclass User.
#   TODO: completare fetch_users e map_to_user.
# ==============================

def fetch_users(results: int = 50,
                nat: str | None = None,
                gender: str | None = None,
                seed: str | None = None,
                timeout: int = 10) -> List[dict]:
    """
    Scarica utenti dall'API randomuser.me e restituisce la lista di dict (raw).
    TODO: implementare la chiamata HTTP con requests.get + params + timeout.
          r.raise_for_status()
          return r.json()["results"]
    """
    url = "https://randomuser.me/api/"
    params = {}  # TODO: aggiungere results, e opzionalmente nat, gender, seed
    # TODO: richiesta HTTP
    # TODO: gestione errori di base (raise_for_status)
    # TODO: restituire la lista raw degli utenti
    raise NotImplementedError("fetch_users: TODO")

def map_to_user(raw: dict) -> User:
    """
    Converte un dict grezzo in User (normalizzando campi base).
    Suggerimenti: .strip(), .lower(), .title(), cast int/float.
    -------------- Campi richiesti --------------
      uuid: raw["login"]["uuid"]
      first: raw["name"]["first"]
      last: raw["name"]["last"]
      email: raw["email"]
      gender: raw.get("gender", "")
      country: raw["location"]["country"]
      age: raw["dob"]["age"]
      nat: raw.get("nat","")
      phone: raw.get("phone") or raw.get("cell") or ""
      lat: raw["location"]["coordinates"]["latitude"]
      lon: raw["location"]["coordinates"]["longitude"]
    """
    # TODO: estrarre i campi dal raw e costruire User(...)
    raise NotImplementedError("map_to_user: TODO")


# ==============================
# MILESTONE 1 — PULIZIA & VALIDAZIONE
#   Regole minime:
#     - email valida (match EMAIL_RE)
#     - 18 <= età <= 100
#     - nazionalità ammessa (se provided)
#     - nessun duplicato per email
#   Output: (validi: List[User], scartati: List[str])
# ==============================

def clean_and_validate(users_raw: Iterable[dict],
                       age_min: int = 18,
                       age_max: int = 100,
                       allowed_nat: set[str] | None = None) -> Tuple[List[User], List[str]]:
    valid: List[User] = []
    discarded: List[str] = []
    seen_emails: set[str] = set()

    for raw in users_raw:
        try:
            u = map_to_user(raw)
        except Exception as e:
            discarded.append(f"MappingError: {e}")
            continue

        # TODO: implementare i controlli e decidere se tenere/scartare
        # email_ok = ...
        # age_ok = ...
        # nat_ok = ...
        # dup_ok = ...
        # if tutti OK -> append a valid e aggiungi u.email a seen_emails
        # else -> aggiungi una descrizione breve a discarded (es: "Invalid(email,age): <email>")
        raise NotImplementedError("clean_and_validate: TODO (validazioni)")

    return valid, discarded


# ==============================
# MILESTONE 2 — STATISTICHE DEMOGRAFICHE
#   Calcolare:
#     - età media, min, max
#     - distribuzione generi (Counter)
#     - top-5 paesi (lista di tuple)
# ==============================

def demographic_stats(users: List[User]) -> Dict[str, object]:
    if not users:
        return {"age": {"avg": 0.0, "min": 0, "max": 0},
                "gender": Counter(),
                "countries_top5": []}

    # TODO: ricavare ages, calcolare avg/min/max
    # TODO: Counter per gender
    # TODO: Counter per country e most_common(5)
    raise NotImplementedError("demographic_stats: TODO")


# ==============================
# MILESTONE 3 — ANALISI DEI NOMI
#   Calcolare:
#     - iniziali più comuni (first letter di first e last)
#     - lunghezza media di first/last
#     - top-10 nomi propri (first)
# ==============================

def name_analysis(users: List[User]) -> Dict[str, object]:
    if not users:
        return {"initials": {"first": Counter(), "last": Counter()},
                "length_avg": {"first": 0.0, "last": 0.0},
                "top_first_names": []}

    # TODO:
    # initials_first = Counter(...)
    # initials_last = Counter(...)
    # avg_first_len = ...
    # avg_last_len = ...
    # top_first = Counter(...).most_common(10)
    raise NotImplementedError("name_analysis: TODO")


# ==============================
# MILESTONE 4 — MATCHING / SUGGERIMENTI
#   Regole (semplici):
#     - affinità se stessa nat OR differenza età <= 2
#     - max 5 suggerimenti/utente
#   Output: dict {uuid: [uuid_suggeriti, ...]}
# ==============================

def suggestions(users: List[User],
                max_suggestions: int = 5,
                age_delta: int = 2) -> Dict[str, List[str]]:
    by_uuid: Dict[str, List[str]] = defaultdict(list)

    # TODO: doppio loop O(n^2) semplice:
    # per ogni utente a, valuta ogni utente b:
    #   calcola score (es. +2 se nat uguale, +1 se |age diff| <= age_delta)
    #   se score > 0 aggiungi candidato
    # ordina candidati per score desc e conserva max_suggestions
    raise NotImplementedError("suggestions: TODO")

    # return dict(by_uuid)


# ==============================
# MILESTONE 5 — EXPORT CSV (first,last,email,phone)
# ==============================

def export_basic_csv(users: List[User], outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    out_csv = outdir / "users_basic.csv"

    # TODO: aprire file CSV e scrivere intestazione + righe richieste
    # intestazione: ["first", "last", "email", "phone"]
    raise NotImplementedError("export_basic_csv: TODO")

    # return out_csv


# ==============================
# MAIN — orchestrazione (già pronto)
# ==============================

def main() -> int:
    args = parse_args()
    outdir = Path(args.outdir)

    print("=== Milestone 0: Fetch raw ===")
    raw = fetch_users(results=args.results, nat=args.nat, gender=args.gender, seed=args.seed)
    print(f"Scaricati: {len(raw)} utenti raw")

    allowed_nat = set(x.strip().lower() for x in (args.nat or "").split(",") if x.strip()) or None

    print("\n=== Milestone 1: Clean & Validate ===")
    valid, discarded = clean_and_validate(raw, age_min=18, age_max=100, allowed_nat=allowed_nat)
    print(f"Validi: {len(valid)} | Scartati: {len(discarded)}")

    print("\n=== Milestone 2: Demographic Stats ===")
    stats = demographic_stats(valid)
    print(stats)

    print("\n=== Milestone 3: Name Analysis ===")
    na = name_analysis(valid)
    print(na)

    print("\n=== Milestone 4: Suggestions ===")
    sug = suggestions(valid, max_suggestions=5, age_delta=2)
    # Mostra solo i primi 3
    for k in list(sug.keys())[:3]:
        print(k, "->", sug[k])

    print("\n=== Milestone 5: Export CSV ===")
    csv_path = export_basic_csv(valid, outdir)
    print("CSV:", csv_path)

    print("\nFATTO (scheletro). Completare i TODO per farlo funzionare ✔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
