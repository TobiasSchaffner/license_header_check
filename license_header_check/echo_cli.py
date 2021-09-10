"""A command line interface that sends all arguments to the stdout.

Copyright (c) 2021 Mixed Mode GmbH
ALL RIGHTS RESERVED - Unauthorized copying of this file, via any medium is strictly prohibited.
"""
from typing import Any, Tuple

import click


def echo(args: Any) -> Any:
    """Return all the values given as arguments.

    Args:
        args (Any): Some values.

    Returns:
        Any: The given values.
    """
    return args


@click.command()
@click.argument("args", nargs=-1)
def echo_command(args: Tuple[Any]) -> None:
    """Print all the values given as arguments.

    Args:
        args (Tuple[Any]): Some values.
    """
    click.echo(echo(args))


if __name__ == "__main__":
    echo_command()
