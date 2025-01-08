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

@anabolicarius.command()
def run():
    """
    Run a database container.
    :return:
    """
    click.echo('Running db container...')

@anabolicarius.command()
def stop():
    """
    Stop a database container.
    :return:
    """
    click.echo('Stopping db container...')

@anabolicarius.command()
def build():
    """
    Build a db container to test the ProSuite.
    :return:
    """
    click.echo('Building db container...')

@anabolicarius.command()
def push():
    """
    Push a local db container to a container registry.
    :return:
    """

@anabolicarius.command()
def registry_init():
    """
    Initialize a db container registry.
    :return:
    """
    click.echo('Initializing db container registry...')

if __name__ == "__main__":
    anabolicarius()