# === TODO STUDENTE =============================================
# In questo file implementi la logica OOP del dominio HR.
# Obiettivi suggeriti (puoi farli in iterazione):
# 1) Aggiungi validazioni extra in Worker.validate() (es. level minimo > 0, bonus tra 0 e 100).
# 2) Implementa una property 'annual_bonus_value' su Employee che ritorna il valore del bonus in €.
# 3) Aggiungi una sottoclasse 'SeniorManager' con extra +10% (sovrascrivi total_compensation).
# 4) Implementa __str__ per una stampa più leggibile.
# 5) Gestisci DuplicateEmployeeError a livello applicativo (vedi hr_analysis.py se vuoi collegarlo).
# Nota: i test esistenti continueranno a passare se non rompi le API pubbliche.
# ================================================================

from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod

class HRDataError(Exception):
    pass

class InvalidSalaryError(HRDataError):
    pass

class DuplicateEmployeeError(HRDataError):
    pass

class SchemaValidationError(HRDataError):
    pass

@dataclass(frozen=True)
class Role:
    name: str
    level: int
    base_multiplier: float = 1.0
    default_bonus_percent: float = 0.0

@dataclass(frozen=True)
class Department:
    name: str
    cost_center: str

@dataclass
class Worker(ABC):
    employee_id: int
    first_name: str
    last_name: str
    role: Role
    department: Department
    base_salary: float
    bonus_percent: float = 0.0
    workload_percent: float = 1.0
    currency: str = "EUR"

    def __post_init__(self) -> None:
        self.validate()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def validate(self) -> None:
        # TODO: aggiungi ulteriori controlli di dominio (range, tipi, ecc.)
        # === INIZIO AREA STUDENTE ===
        # Esempi di controlli (scrivi tu la logica):
        # - Verifica che 'level' nel Role sia >= 1
        # - Vincola 'bonus_percent' tra 0 e 100
        # - Verifica che 'cost_center' non sia vuoto
        # Suggerimenti: usa 'if', 'raise' e le eccezioni del dominio.
        # Non lasciare passaggi silenziosi: fornisci messaggi chiari negli errori.
        # === FINE AREA STUDENTE ===
        if self.base_salary <= 0:
            raise InvalidSalaryError(f"Base salary non valido per {self.full_name}: {self.base_salary}")
        if not (0.0 < self.workload_percent <= 1.0):
            raise HRDataError(f"workload_percent deve essere (0,1]: {self.workload_percent}")
        if self.currency not in {"EUR", "USD", "RON"}:
            raise HRDataError(f"Valuta non supportata: {self.currency}")

    def __lt__(self, other: 'Worker') -> bool:
        return self.total_compensation() < other.total_compensation()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.employee_id} {self.full_name} {self.role.name} {self.department.name}>"

    @abstractmethod
    def total_compensation(self) -> float:
        # TODO: definisci/estendi le regole di calcolo per questa classe
        ...

@dataclass
class Employee(Worker):
    # TODO: valuta di aggiungere property/methods di supporto (es. annual_bonus_value)
    # === INIZIO AREA STUDENTE ===
    # Implementa una property opzionale:
    # @property
    # def annual_bonus_value(self) -> float:
    #     """Ritorna il valore in € del bonus annuale.
    #     Suggerimento: usa self.base_salary, self.workload_percent, self.bonus_percent.
    #     """
    #     ...
    # === FINE AREA STUDENTE ===
    def total_compensation(self) -> float:
        # TODO: definisci/estendi le regole di calcolo per questa classe
        base = self.base_salary * self.workload_percent
        bonus_factor = (self.bonus_percent or 0.0) / 100.0
        return base * (1.0 + bonus_factor)

@dataclass
class Manager(Employee):
    # TODO: sperimenta un diverso extra per i Manager o calibra per 'level'
    # === INIZIO AREA STUDENTE ===
    # Idea: applica un extra variabile in base a self.role.level
    # oppure in base al reparto (self.department.name).
    # === FINE AREA STUDENTE ===
    def total_compensation(self) -> float:
        # TODO: definisci/estendi le regole di calcolo per questa classe
        return super().total_compensation() * 1.05

@dataclass
class Contractor(Worker):
    # TODO: aggiungi eventuali costi accessori/penali se serve alla simulazione
    # === INIZIO AREA STUDENTE ===
    # Esempio: applica una fee fissa di gestione o uno sconto per workload < 0.5.
    # === FINE AREA STUDENTE ===
    def total_compensation(self) -> float:
        # TODO: definisci/estendi le regole di calcolo per questa classe
        return self.base_salary * self.workload_percent


# === INIZIO AREA STUDENTE ===
# Crea una nuova sottoclasse opzionale, es. SeniorManager, che aggiunge +10% extra.
# class SeniorManager(Manager):
#     def total_compensation(self) -> float:
#         """Suggerimento: chiama super().total_compensation() e applica un moltiplicatore."""
#         ...
# === FINE AREA STUDENTE ===
