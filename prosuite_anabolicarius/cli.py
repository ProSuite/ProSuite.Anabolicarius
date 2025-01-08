from typing import Literal

import click
from prosuite_anabolicarius import anabolicarius


@anabolicarius.command()
@click.option('--db', default='oracle', help = 'For which db type you want to initialize you example db (postgres or oracle).')
def init(db_type: Literal['postgres', 'oracle']):
    click.echo('Initializing database...')
