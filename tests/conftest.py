import pytest
import sqlite3


@pytest.fixture(scope='session')
def db_connection():
    """
    :return: sqlite3 connection class
    """
    db_settings = {
        'database': 'test_db.sqlite3',
    }

    # DB setting for non-test env
    dbc = sqlite3.connect(**db_settings)

    return dbc


@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_connection):
    """
    This will alter application database connection settings, for all the tests
    in unit tests module.
    :param mocker: pytest-mock plugin fixture
    :param db_connection: connection class
    :return: True upon successful monkey-patching
    """
    mocker.patch('db.database.get_db_connection', db_connection)
    return True
