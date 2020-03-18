import sqlite3
import os


def get_db_connection():
    db_settings = {
        'database': 'db.sqlite3',
    }

    # DB setting for non-test env
    if not os.environ.get('TEST'):
        dbc = sqlite3.connect(**db_settings)
        dbc.autocommit = True
    else:
        # if we are in test return dummy object we will override by mock
        dbc = None
    return dbc
