import sqlite3


def create_user(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS User (
        id_user INTEGER PRIMARY KEY,
        name_user varchar (64) NOT NULL,
        login_user  varchar (32) not null unique,
        mail_user varchar (254) not null unique,
        password_user VARCHAR (128) NOT NULL,
        time_add_user DATETIME not null,
        time_status_change_user DATETIME not null,
        status_user INTEGER,
        role_user INTEGER,
        FOREIGN KEY (status_user) REFERENCES Status (id_status),
        FOREIGN KEY (role_user) REFERENCES Role (id_role)
        )
    ''')


def create_role(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS Role (
        id_role INTEGER PRIMARY KEY,
        name_role TEXT NOT NULL unique
    )
    ''')


def create_status(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS Status (
        id_status INTEGER PRIMARY KEY,
        name_status TEXT NOT NULL unique
        )
    ''')


if __name__ == "__main__":
    connection = sqlite3.connect('application.db')

    cursor = connection.cursor()

    create_status(cursor)
    create_role(cursor)
    create_user(cursor)

    connection.commit()

    connection.close()
