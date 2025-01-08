from typing import Literal

import click


@click.group()
def anabolicarius():
    """
    Entry point for the cli.
    :return:
    """
    pass


@anabolicarius.command()
@click.option('--db', default='oracle', help = 'For which db type you want to initialize you example db (postgres or oracle).')
def init(db: Literal['postgres', 'oracle']):
    """
    Initialize a new db container.
    :param db:
    :return:
    """
    click.echo('Initializing database...')


if __name__ == "__main__":
    anabolicarius()