import pytest
import sqlite3
from HERNY.main_herny.create_table_db import create_user, create_role, create_status


@pytest.fixture(scope='session')  # Scope='session' - база данных создаётся один раз для всей сессии
def test_db_connection(tmpdir_factory):
    db_path = tmpdir_factory.mktemp("data").join("test.db")
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    create_user()

    # ... ваши действия с базой данных, например, инициализируйте данные ...
    cursor.execute("select * from User")
    connection.commit()

    yield connection
    cursor.close()
    connection.close()  # Закрываем соединение после окончания тестов
