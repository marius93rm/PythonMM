#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Progetto (SOLUZIONI): Analisi utenti da randomuser.me
Milestones:
  1) Pulizia dati e validazione
  2) Statistiche demografiche
  3) Analisi dei nomi
  4) Sistema di matching / suggerimenti
  5) Export CSV (first,last,email,phone)

Esecuzione (esempio):
  python progetto_randomuser_soluzione.py --results 100 --nat "us,it,dk" --gender "male,female" --seed "corso123"

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
    p = argparse.ArgumentParser(description="Analisi utenti randomuser.me (soluzioni)")
    p.add_argument("--results", type=int, default=50, help="Numero di utenti da scaricare")
    p.add_argument("--nat", type=str, default=None, help='Nazionalità (es: "us,it,dk")')
    p.add_argument("--gender", type=str, default=None, help='Genere (es: "male,female")')
    p.add_argument("--seed", type=str, default=None, help="Seed per risultati ripetibili")
    p.add_argument("--outdir", type=str, default="out", help="Cartella di output")
    return p.parse_args()


# ==============================
# MILESTONE 0 — FETCH & MAPPING (SOLUZIONI)
# ==============================

def fetch_users(results: int = 50,
                nat: str | None = None,
                gender: str | None = None,
                seed: str | None = None,
                timeout: int = 10) -> List[dict]:
    """
    Scarica utenti dall'API randomuser.me e restituisce la lista di dict (raw).
    """
    url = "https://randomuser.me/api/"
    params: dict = {"results": results}
    if nat:
        params["nat"] = nat
    if gender:
        params["gender"] = gender
    if seed:
        params["seed"] = seed

    r = requests.get(url, params=params, timeout=timeout)
    r.raise_for_status()
    payload = r.json()
    return payload.get("results", [])


def _to_float(x) -> float:
    # randomuser fornisce stringhe tipo "-46.8052"
    try:
        return float(str(x).strip())
    except Exception:
        return 0.0

def _to_int(x) -> int:
    try:
        return int(x)
    except Exception:
        return 0

def map_to_user(raw: dict) -> User:
    """
    Converte un dict grezzo in User (normalizzando campi base).
    """
    return User(
        uuid=str(raw["login"]["uuid"]).strip(),
        first=str(raw["name"]["first"]).strip().title(),
        last=str(raw["name"]["last"]).strip().title(),
        email=str(raw["email"]).strip().lower(),
        gender=str(raw.get("gender", "")).strip().lower(),
        country=str(raw["location"]["country"]).strip(),
        age=_to_int(raw["dob"]["age"]),
        nat=str(raw.get("nat", "")).strip().lower(),
        phone=str(raw.get("phone") or raw.get("cell") or "").strip(),
        lat=_to_float(raw["location"]["coordinates"]["latitude"]),
        lon=_to_float(raw["location"]["coordinates"]["longitude"]),
    )


# ==============================
# MILESTONE 1 — PULIZIA & VALIDAZIONE (SOLUZIONI)
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

        email_ok = EMAIL_RE.match(u.email) is not None
        age_ok = (age_min <= u.age <= age_max)
        nat_ok = True if allowed_nat is None else (u.nat in allowed_nat)
        dup_ok = (u.email not in seen_emails)

        if email_ok and age_ok and nat_ok and dup_ok:
            valid.append(u)
            seen_emails.add(u.email)
        else:
            reasons = []
            if not email_ok: reasons.append("email")
            if not age_ok: reasons.append("age")
            if not nat_ok: reasons.append("nat")
            if not dup_ok: reasons.append("duplicate_email")
            discarded.append(f"Invalid({','.join(reasons)}): {u.email}")

    return valid, discarded


# ==============================
# MILESTONE 2 — STATISTICHE DEMOGRAFICHE (SOLUZIONI)
# ==============================

def demographic_stats(users: List[User]) -> Dict[str, object]:
    if not users:
        return {"age": {"avg": 0.0, "min": 0, "max": 0},
                "gender": Counter(),
                "countries_top5": []}

    ages = [u.age for u in users]
    avg_age = round(sum(ages) / len(ages), 2)
    min_age = min(ages)
    max_age = max(ages)

    gender_counter = Counter(u.gender or "unknown" for u in users)
    country_counter = Counter(u.country for u in users)
    top5_countries = country_counter.most_common(5)

    return {
        "age": {"avg": avg_age, "min": min_age, "max": max_age},
        "gender": gender_counter,
        "countries_top5": top5_countries,
    }


# ==============================
# MILESTONE 3 — ANALISI DEI NOMI (SOLUZIONI)
# ==============================

def name_analysis(users: List[User]) -> Dict[str, object]:
    if not users:
        return {"initials": {"first": Counter(), "last": Counter()},
                "length_avg": {"first": 0.0, "last": 0.0},
                "top_first_names": []}

    initials_first = Counter(u.first[0].upper() for u in users if u.first)
    initials_last = Counter(u.last[0].upper() for u in users if u.last)

    avg_first_len = round(sum(len(u.first) for u in users) / len(users), 2)
    avg_last_len  = round(sum(len(u.last) for u in users) / len(users), 2)

    top_first = Counter(u.first for u in users).most_common(10)

    return {
        "initials": {"first": initials_first, "last": initials_last},
        "length_avg": {"first": avg_first_len, "last": avg_last_len},
        "top_first_names": top_first,
    }


# ==============================
# MILESTONE 4 — MATCHING / SUGGERIMENTI (SOLUZIONI)
# ==============================

def suggestions(users: List[User],
                max_suggestions: int = 5,
                age_delta: int = 2) -> Dict[str, List[str]]:
    by_uuid: Dict[str, List[str]] = defaultdict(list)

    # Algoritmo O(n^2) semplice e leggibile
    for i, a in enumerate(users):
        candidates: List[tuple[int, str]] = []  # (score, uuid)
        for j, b in enumerate(users):
            if i == j:
                continue
            score = 0
            if a.nat and a.nat == b.nat:
                score += 2
            if abs(a.age - b.age) <= age_delta:
                score += 1
            if score > 0:
                candidates.append((score, b.uuid))
        candidates.sort(key=lambda t: t[0], reverse=True)
        by_uuid[a.uuid] = [uid for _, uid in candidates[:max_suggestions]]

    return dict(by_uuid)


# ==============================
# MILESTONE 5 — EXPORT CSV (SOLUZIONI)
# ==============================

def export_basic_csv(users: List[User], outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    out_csv = outdir / "users_basic.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["first", "last", "email", "phone"])
        for u in users:
            w.writerow([u.first, u.last, u.email, u.phone])
    return out_csv


# ==============================
# MAIN — orchestrazione
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
    if discarded:
        print("Esempi scarti:", discarded[:5])

    print("\n=== Milestone 2: Demographic Stats ===")
    stats = demographic_stats(valid)
    print("Età   ->", stats["age"])
    print("Genere->", dict(stats["gender"]))
    print("Top-5 Paesi:", stats["countries_top5"])

    print("\n=== Milestone 3: Name Analysis ===")
    na = name_analysis(valid)
    print("Iniziali first (top5):", na["initials"]["first"].most_common(5))
    print("Iniziali last  (top5):", na["initials"]["last"].most_common(5))
    print("Lunghezze medie:", na["length_avg"])
    print("Top-10 nomi:", na["top_first_names"])

    print("\n=== Milestone 4: Suggestions ===")
    sug = suggestions(valid, max_suggestions=5, age_delta=2)
    for k, v in list(sug.items())[:3]:
        print(f"{k} -> {v}")

    print("\n=== Milestone 5: Export CSV ===")
    csv_path = export_basic_csv(valid, outdir)
    print("CSV:", csv_path)

    print("\nFATTO ✔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
