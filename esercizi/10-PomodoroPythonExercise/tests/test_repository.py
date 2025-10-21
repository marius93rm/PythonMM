import csv
import pytest
from datetime import datetime
from pomodoro.persistence import CsvSessionRepository, SessionLog

def test_csv_repository_writes_header_and_row(tmp_path):
    path = tmp_path / "sessions.csv"
    repo = CsvSessionRepository(str(path))

    log = SessionLog(started_at=datetime(2020,1,1,12,0,0), kind="focus", seconds=1500)

    with pytest.raises(NotImplementedError):
        repo.save(log)

    # Quando implementi M5, rimuovi la riga sopra e verifica:
    # repo.save(log)
    # assert path.exists()
    # rows = list(csv.reader(open(path, newline="", encoding="utf-8")))
    # assert rows[0] == ["started_at_iso", "kind", "seconds"]
    # assert rows[1] == ["2020-01-01T12:00:00", "focus", "1500"]
