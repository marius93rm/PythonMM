"""Configurazione condivisa per i test.

Rende importabili i moduli degli esercizi aggiungendo la cartella principale
`esercizi/design-patterns-todo-python` al `sys.path` di Python durante
l'esecuzione di pytest.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
