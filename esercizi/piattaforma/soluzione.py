# notifications_platform_exercise_solution.py
# ==============================================
# ESERCIZIO 2 — Piattaforma di Notifiche (Observer Pattern)
# Soluzione completa M1..M8
# ==============================================

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
        # stesso canale, destinatario e messaggio => notifica uguale
        return (self.channel, self.to, self.message) == (other.channel, other.to, other.message)

    def __repr__(self) -> str:
        flag = "✓" if self.seen else "•"
        return f"<{flag} {self.channel}:{self.to} '{self.message[:30]}...'>"


class Inbox:
    """Composizione: raccoglie Notification."""
    def __init__(self) -> None:
        self._items: List[Notification] = []

    # M4: dunder
    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item: Notification) -> bool:
        # equality definita in Notification.__eq__
        return any(n == item for n in self._items)

    # API base
    def add(self, notif: Notification) -> None:
        self._items.append(notif)

    # M5: filtri/ricerche/stat
    def by_user(self, username: str) -> List[Notification]:
        return [n for n in self._items if n.to == username]

    def by_channel(self, channel: str) -> List[Notification]:
        ch = channel.lower()
        return [n for n in self._items if n.channel.lower() == ch]

    def unseen_count(self) -> int:
        return sum(1 for n in self._items if not n.seen)

    # M6: persistenza JSON/CSV (con dedupe su (channel,to,message))
    def export_json(self, path: str) -> None:
        payload = []
        for n in self._items:
            d = asdict(n)
            d["created_at"] = n.created_at.isoformat()
            payload.append(d)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def import_json(self, path: str) -> int:
        if not os.path.exists(path):
            return 0
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        sigs = {(n.channel, n.to, n.message) for n in self._items}
        added = 0
        for d in data:
            ch = d.get("channel", "")
            to = d.get("to", "")
            msg = d.get("message", "")
            sig = (ch, to, msg)
            if sig in sigs:
                continue
            ts = d.get("created_at")
            try:
                created = datetime.fromisoformat(ts) if ts else datetime.utcnow()
            except Exception:
                created = datetime.utcnow()
            seen = bool(d.get("seen", False))
            self._items.append(Notification(ch, to, msg, created, seen))
            sigs.add(sig)
            added += 1
        return added

    def export_csv(self, path: str) -> None:
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["channel", "to", "message", "created_at", "seen"])
            for n in self._items:
                w.writerow([n.channel, n.to, n.message, n.created_at.isoformat(), int(n.seen)])

    def import_csv(self, path: str) -> int:
        if not os.path.exists(path):
            return 0
        with open(path, "r", encoding="utf-8") as f:
            r = csv.DictReader(f)
            sigs = {(n.channel, n.to, n.message) for n in self._items}
            added = 0
            for row in r:
                ch = row.get("channel", "")
                to = row.get("to", "")
                msg = row.get("message", "")
                sig = (ch, to, msg)
                if sig in sigs:
                    continue
                ts = row.get("created_at") or ""
                try:
                    created = datetime.fromisoformat(ts)
                except Exception:
                    created = datetime.utcnow()
                seen = str(row.get("seen", "0")).strip() in ("1", "true", "True", "yes", "y")
                self._items.append(Notification(ch, to, msg, created, seen))
                sigs.add(sig)
                added += 1
        return added


# =============================================================
# OBSERVER & STRATEGY
# =============================================================

class Observable:
    """Soggetto osservabile: gestisce la lista di osservatori (follower)."""
    def __init__(self) -> None:
        self._observers: set[str] = set()

    # M2: attach/detach/observers
    def attach(self, username: str) -> None:
        self._observers.add(username)

    def detach(self, username: str) -> None:
        self._observers.discard(username)

    def observers(self) -> List[str]:
        return sorted(self._observers)

    # M2: notify su nuovo Post. Ritorna elenco username notificati.
    def notify(self, post: Post) -> List[str]:
        # M2 si limita a restituire la lista degli osservatori (consegna canali verrà in M3)
        return self.observers()


@runtime_checkable
class Notifier(Protocol):
    """Strategy: canale di notifica pluggable."""
    channel: str
    def send(self, to: str, message: str) -> Notification: ...


class EmailNotifier:
    channel = "email"
    # M3: implementa send()
    def send(self, to: str, message: str) -> Notification:
        # qui simuleremmo l'invio email; ritorniamo l'oggetto Notification
        return Notification(self.channel, to, message)


class SMSNotifier:
    channel = "sms"
    def send(self, to: str, message: str) -> Notification:
        return Notification(self.channel, to, message)


class PushNotifier:
    channel = "push"
    def send(self, to: str, message: str) -> Notification:
        return Notification(self.channel, to, message)


class LoggableMixin:
    """Mixin per tracciare eventi in memoria (M7)."""
    def __init__(self) -> None:
        self._log: List[str] = []

    # M7: metodo log()
    def log(self, event: str) -> None:
        self._log.append(f"{datetime.utcnow().isoformat()} {event}")

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

    # M1: follow/unfollow altri utenti
    def follow(self, other: "User") -> None:
        other.attach(self.username)
        self.log(f"follow {other.username}")

    def unfollow(self, other: "User") -> None:
        other.detach(self.username)
        self.log(f"unfollow {other.username}")

    # M1: post() crea Post (niente notify qui; M2 lo chiama esplicitamente)
    def post(self, content: str) -> Post:
        self.log("post")
        return Post(author=self.username, content=content)

    # M3: ricevi una notifica tramite il canale preferito
    def receive(self, message: str) -> Notification:
        notif = self.preferred.send(self.username, message)
        self.inbox.add(notif)
        self.log(f"receive via {notif.channel}")
        return notif


# =============================================================
# TEST HARNESS
# =============================================================

def _safe_test(name: str, fn):
    try:
        fn()
        print(f"✅ {name}")
        return True
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
    lg = " ".join(u.get_log())
    assert "login" in lg and "follow bob" in lg


def test_m8():
    a = Notification("email", "alice", "m1")
    b = Notification("email", "alice", "m1")
    c = Notification("email", "alice", "m2")
    assert a == b and a != c
    inbox = Inbox()
    inbox.add(c); inbox.add(a); inbox.add(b)
    # ordinamento per data (facoltativo)
    sorted_by_time = sorted(inbox._items, key=lambda n: n.created_at)
    assert len(sorted_by_time) == 3


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
        print("Suggerimento: rivedi i TODO non superati.")


if __name__ == "__main__":
    run_all_tests()
