import pytest

from behavioral.memento_pattern import (
    EditorMemento,
    HistoryCaretaker,
    TextEditor,
)


def test_editor_creates_and_restores_memento() -> None:
    editor = TextEditor()
    editor.type_text("Hello")
    snapshot = editor.create_memento()
    assert isinstance(snapshot, EditorMemento)

    editor.type_text(" World")
    assert editor.content == "Hello World"

    editor.restore(snapshot)
    assert editor.content == "Hello"


def test_history_caretaker_behaves_like_stack() -> None:
    editor = TextEditor()
    history = HistoryCaretaker()

    editor.type_text("A")
    history.push(editor.create_memento())
    editor.type_text("B")
    history.push(editor.create_memento())

    editor.restore(history.pop())
    assert editor.content == "AB"

    editor.restore(history.pop())
    assert editor.content == "A"

    with pytest.raises(IndexError):
        history.pop()
