# notifications_platform_exercise.py
# ==============================================
# ESERCIZIO 2 — Piattaforma di Notifiche (Observer Pattern)
# ==============================================
#
# Obiettivo
# ---------
# Progettare e implementare una mini piattaforma di notifiche in stile social
# che sfrutta i concetti OOP visti nelle slide:
# - Incapsulamento, ereditarietà, polimorfismo
# - Classi astratte (ABC) e mixin
# - Metodi speciali (__repr__, __len__, __contains__, __eq__)
# - Observer pattern (Subject/Observable + Observer)
# - Strategy pattern leggero per canali di notifica
# - Composizione (Inbox che raccoglie Notifiche)
# - Persistenza JSON/CSV (bonus)
#
# Come lavorare
# -------------
# - Completa le funzioni con i TODO per milestone, in ordine.
# - Esegui questo file: vedrai il report "Milestones superate: X/..".
# - Ogni milestone sblocca la successiva.
# - Mantieni il codice pulito e mantenibile.
#
# Requisiti tecnici
# -----------------
# - Solo standard library (json, csv, datetime, abc, dataclasses, typing, os, tempfile).
# - Python >= 3.10 consigliato.
#
# Milestones
# ----------
# M1) Modello base e follow                       (User, Post, follow/unfollow, post())
# M2) Observer: Observable + notify()            (attach/detach, notify followers su nuovo Post)
# M3) Canali di notifica (polimorfismo/Strategy) (Email/SMS/Push implementano send())
# M4) Inbox + metodi speciali                    (__len__, __contains__, __repr__)
# M5) Filtri/ricerche e statistiche              (by_user, by_channel, unseen_count)
# M6) Persistenza JSON/CSV                        (export/import notifiche)
# M7) Mixin di logging                            (LoggableMixin per tracciare eventi)
# M8) Confronti/ordinamenti                       (__eq__ sulle notifiche, ordinamento per data)
#
# NOTA: I test sono "tolleranti": se un TODO non è implementato, il test fallisce ma l'esecuzione continua.

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional, Iterable, Protocol, runtime_checkable, List, Dict
from abc import ABC, abstractmethod
import json, csv, os, tempfile

# =============================================================
# DOMINIO
# =============================================================

@dataclass
class Post:
    author: str
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Post(author={self.author!r}, content={self.content!r})"


@dataclass
class Notification:
    """Entità 'value object' che rappresenta l'esito di un invio notifica."""
    channel: str
    to: str
    message: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    seen: bool = False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Notification):
            return NotImplemented
        # due notifiche sono uguali se stesso canale, destinatario e messaggio
        return (self.channel, self.to, self.message) == (other.channel, other.to, other.message)

    def __repr__(self) -> str:
        flag = "✓" if self.seen else "•"
        return f"<{flag} {self.channel}:{self.to} '{self.message[:30]}...'>"


class Inbox:
    """Composizione: raccoglie Notification."""
    def __init__(self) -> None:
        self._items: List[Notification] = []

    # TODO(M4): implementa __len__ (numero notifiche)
    def __len__(self) -> int:
        raise NotImplementedError

    # TODO(M4): implementa __contains__ per: notif in inbox
    def __contains__(self, item: Notification) -> bool:
        raise NotImplementedError

    # TODO(M4): aggiungi add() per inserire una notifica
    def add(self, notif: Notification) -> None:
        raise NotImplementedError

    # TODO(M5): filtri base
    def by_user(self, username: str) -> List[Notification]:
        """Ritorna le notifiche indirizzate a 'username'."""
        raise NotImplementedError

    def by_channel(self, channel: str) -> List[Notification]:
        """Ritorna le notifiche per canale."""
        raise NotImplementedError

    def unseen_count(self) -> int:
        """Numero di notifiche non viste."""
        raise NotImplementedError

    # TODO(M6): persistenza JSON/CSV
    def export_json(self, path: str) -> None:
        raise NotImplementedError

    def import_json(self, path: str) -> int:
        """Ritorna quante notifiche nuove ha importato (dedupe su (channel,to,message))."""
        raise NotImplementedError

    def export_csv(self, path: str) -> None:
        raise NotImplementedError

    def import_csv(self, path: str) -> int:
        raise NotImplementedError


# =============================================================
# OBSERVER & STRATEGY
# =============================================================

class Observable:
    """Soggetto osservabile: gestisce la lista di osservatori (follower)."""
    def __init__(self) -> None:
        self._observers: set[str] = set()

    # TODO(M2): implementa attach/detach/observers
    def attach(self, username: str) -> None:
        raise NotImplementedError

    def detach(self, username: str) -> None:
        raise NotImplementedError

    def observers(self) -> List[str]:
        raise NotImplementedError

    # TODO(M2): notify su nuovo Post. Ritorna elenco username notificati.
    def notify(self, post: Post) -> List[str]:
        raise NotImplementedError


@runtime_checkable
class Notifier(Protocol):
    """Strategy: canale di notifica pluggable."""
    channel: str
    def send(self, to: str, message: str) -> Notification: ...


class EmailNotifier:
    channel = "email"
    # TODO(M3): implementa send()
    def send(self, to: str, message: str) -> Notification:
        raise NotImplementedError


class SMSNotifier:
    channel = "sms"
    def send(self, to: str, message: str) -> Notification:
        raise NotImplementedError


class PushNotifier:
    channel = "push"
    def send(self, to: str, message: str) -> Notification:
        raise NotImplementedError


class LoggableMixin:
    """Mixin per tracciare eventi in memoria (M7)."""
    def __init__(self) -> None:
        self._log: List[str] = []

    # TODO(M7): metodo log()
    def log(self, event: str) -> None:
        raise NotImplementedError

    def get_log(self) -> List[str]:
        return list(self._log)


class User(LoggableMixin, Observable):
    """Utente con preferenze di notifica e inbox."""
    def __init__(self, username: str, preferred: Optional[Notifier] = None) -> None:
        LoggableMixin.__init__(self)
        Observable.__init__(self)
        self.username = username
        self.preferred: Notifier = preferred or EmailNotifier()  # default
        self.inbox = Inbox()

    # TODO(M1): follow/unfollow altri utenti
    def follow(self, other: "User") -> None:
        """Segui 'other': ti registri come observer dei suoi post."""
        raise NotImplementedError

    def unfollow(self, other: "User") -> None:
        raise NotImplementedError

    # TODO(M1): post() crea Post e scatena notify()
    def post(self, content: str) -> Post:
        raise NotImplementedError

    # TODO(M3): ricevi una notifica tramite il canale preferito
    def receive(self, message: str) -> Notification:
        raise NotImplementedError


# =============================================================
# TEST HARNESS
# =============================================================

def _safe_test(name: str, fn):
    try:
        fn()
        print(f"✅ {name}")
        return True
    except NotImplementedError:
        print(f"❌ {name} — TODO non ancora implementato")
        return False
    except AssertionError as e:
        print(f"❌ {name} — Test fallito: {e}")
        return False
    except Exception as e:
        print(f"❌ {name} — Errore inaspettato: {type(e).__name__}: {e}")
        return False


def _mk_tmpfile(suffix: str) -> str:
    fd, path = tempfile.mkstemp(suffix=suffix, text=True)
    os.close(fd)
    return path


# --------------------------- TESTS PER M1..M8 ---------------------------

def test_m1():
    a = User("alice")
    b = User("bob")
    a.follow(b)
    assert "alice" in b.observers()
    p = b.post("Hello world")
    assert isinstance(p, Post)
    # a non riceve ancora nulla: notify è M2
    assert len(a.inbox) == 0


def test_m2():
    a = User("alice")
    b = User("bob")
    a.follow(b)
    p = b.post("Nuovo post")
    notified = b.notify(p)
    assert "alice" in notified


def test_m3():
    a = User("alice", preferred=SMSNotifier())
    # a riceve via SMS
    notif = a.receive("ciao")
    assert isinstance(notif, Notification)
    assert notif.channel == "sms"
    assert len(a.inbox) == 1


def test_m4():
    inbox = Inbox()
    n1 = Notification(channel="email", to="alice", message="m1")
    inbox.add(n1)
    assert len(inbox) == 1
    assert n1 in inbox
    assert "m1" in repr(n1)


def test_m5():
    inbox = Inbox()
    inbox.add(Notification("email", "alice", "m1"))
    inbox.add(Notification("sms", "bob", "m2", seen=True))
    inbox.add(Notification("email", "alice", "m3"))
    assert inbox.unseen_count() == 2
    assert len(inbox.by_user("alice")) == 2
    assert len(inbox.by_channel("email")) == 2


def test_m6():
    inbox = Inbox()
    inbox.add(Notification("email", "alice", "m1"))
    inbox.add(Notification("sms", "bob", "m2"))
    p_json = _mk_tmpfile(".json")
    p_csv = _mk_tmpfile(".csv")
    inbox.export_json(p_json)
    inbox.export_csv(p_csv)
    inbox2 = Inbox()
    n_json = inbox2.import_json(p_json)
    n_csv = inbox2.import_csv(p_csv)
    assert n_json >= 2 and n_csv >= 2


def test_m7():
    u = User("alice")
    u.log("login")
    u.log("follow bob")
    assert "login" in u.get_log() and "follow bob" in u.get_log()


def test_m8():
    a = Notification("email", "alice", "m1")
    b = Notification("email", "alice", "m1")
    c = Notification("email", "alice", "m2")
    assert a == b and a != c
    inbox = Inbox()
    inbox.add(c); inbox.add(a); inbox.add(b)
    # dedupe logica (se implementata in import) non è richiesta qui; solo verifica comparazioni
    # ordinabilità per data (facoltativo): sorted(inbox._items, key=lambda n: n.created_at)


def run_all_tests():
    tests = [
        ("M1 — Modello base e follow", test_m1),
        ("M2 — Observer notify", test_m2),
        ("M3 — Canali di notifica", test_m3),
        ("M4 — Inbox + dunder", test_m4),
        ("M5 — Filtri/statistiche", test_m5),
        ("M6 — Persistenza JSON/CSV", test_m6),
        ("M7 — LoggableMixin", test_m7),
        ("M8 — Confronti/ordinamento", test_m8),
    ]
    ok = 0
    for name, fn in tests:
        ok += 1 if _safe_test(name, fn) else 0
    print(f"\n▶️  Milestones superate: {ok}/{len(tests)}")
    if ok < len(tests):
        print("Suggerimento: implementa i TODO in ordine di milestone.")


if __name__ == "__main__":
    run_all_tests()
