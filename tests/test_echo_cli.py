import pytest

from license_header_check.echo_cli import echo, echo_command


def test_echo():
    assert echo(5) == 5


def test_echo_command():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        echo_command("test")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 0
