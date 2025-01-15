import pytest
import sqlite3
from faker import Faker
from random import randint
from HERNY.main_herny.editing import User, Role, Status
from HERNY.main_herny.create_table_db import create_user, create_role, create_status


@pytest.fixture(scope='function')
def test_user_db_connection(tmpdir_factory):
    fake = Faker()
    db_path = tmpdir_factory.mktemp("data").join("test.db")
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    create_user(cursor)
    create_role(cursor)
    create_status(cursor)

    for index in range(3, randint(4, 10)):
        User(
            name_user=fake.name(), login_user=str(index), mail_user=f"gg{index}@mail.ru",
            password_user=fake.password(length=randint(10, 20)),
            time_add_user=fake.date(), time_status_change_user=fake.date(),
            status_user=1, role_user=1,
        ).add(cursor)
        Status(name_status=f"test_status{index}").add(cursor)
        Role(name_role=f"test_role{index}").add(cursor)

    cursor.execute("select * from User")
    connection.commit()

    yield cursor.fetchall()
    cursor.close()
    connection.close()


@pytest.fixture(scope='function')
def test_status_db_connection(tmpdir_factory):
    db_path = tmpdir_factory.mktemp("data").join("test.db")
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    create_status(cursor)

    for index in range(3, randint(4, 10)):
        Status(name_status=f"test_status{index}").add(cursor)

    cursor.execute("select * from Status")
    connection.commit()

    yield cursor.fetchall()
    cursor.close()
    connection.close()


@pytest.fixture(scope='function')
def test_role_db_connection(tmpdir_factory):
    db_path = tmpdir_factory.mktemp("data").join("test.db")
    connection = sqlite3.connect(str(db_path))
    cursor = connection.cursor()

    create_role(cursor)

    for index in range(3, randint(4, 10)):
        Role(name_role=f"test_role{index}").add(cursor)

    cursor.execute("select * from Role")
    connection.commit()

    yield cursor.fetchall()
    cursor.close()
    connection.close()

