from behavioral.command_pattern import (
    AppendTextCommand,
    ClearTextCommand,
    EditorInvoker,
    TextDocument,
    setup_editor,
)


def test_append_and_clear_commands_modify_document() -> None:
    document, invoker = setup_editor()

    append = AppendTextCommand(document, "Hello")
    invoker.run(append)
    invoker.run(AppendTextCommand(document, " World"))

    assert document.content == "Hello World"
    assert invoker.last_commands()[-1].__class__ is AppendTextCommand

    clear = ClearTextCommand(document)
    invoker.run(clear)
    assert document.content == ""
    assert invoker.last_commands()[-1] is clear


def test_editor_history_preserves_execution_order() -> None:
    document = TextDocument()
    invoker = EditorInvoker()

    commands = [
        AppendTextCommand(document, part)
        for part in ("One", " Two", " Three")
    ]

    for command in commands:
        invoker.run(command)

    assert [cmd.text for cmd in invoker.last_commands() if isinstance(cmd, AppendTextCommand)] == [
        "One",
        " Two",
        " Three",
    ]
