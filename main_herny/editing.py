import sqlite3
import datetime
from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self, condition_dictionary):
        pass

    @abstractmethod
    def change(self, condition_dictionary, change_dictionary):
        pass

    @abstractmethod
    def delete_all(self):
        pass


class User(Entity):
    def __new__(
            cls, name_user=None, login_user=None, mail_user=None, password_user=None,
            time_add_user=None, time_status_change_user=None, status_user=None, role_user=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.name_user = name_user
        cls.instance.login_user = login_user
        cls.instance.mail_user = mail_user
        cls.instance.password_user = password_user
        cls.instance.time_add_user = time_add_user
        cls.instance.time_status_change_user = time_status_change_user
        cls.instance.role_user = role_user
        cls.instance.status_user = status_user
        return cls.instance

    @classmethod
    def add(cls):
        try:
            cursor.execute(
                "INSERT INTO User "
                "(name_user, login_user, mail_user, password_user, time_add_user,"
                " time_status_change_user, role_user, status_user)"
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    cls.instance.name_user, cls.instance.login_user, cls.instance.mail_user,
                    cls.instance.password_user, str(cls.instance.time_add_user),
                    str(cls.instance.time_status_change_user), cls.instance.role_user, cls.instance.status_user,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, condition_dictionary):
        try:
            cursor.execute(
                f"DELETE FROM User where {condition_dictionary}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, condition_dictionary, change_dictionary):
        try:
            cursor.execute(
                f"UPDATE User "
                f"SET {', '.join(change_dictionary)} "
                f"Where {' and '.join(condition_dictionary)}"
            )
            print(
                f"UPDATE User "
                f"SET {', '.join(change_dictionary)} "
                f"Where {' and '.join(change_dictionary)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls):
        try:
            cursor.execute(
                f"DELETE FROM User"
            )
        except Exception as error:
            print(f"Error: {error}")


class Role(Entity):
    def __new__(
            cls, name_role=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.name_role = name_role
        return cls.instance

    @classmethod
    def add(cls):
        try:
            cursor.execute(
                "INSERT INTO Role "
                "(name_role)"
                "VALUES (?)",
                (
                    cls.instance.name_role,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, condition_dictionary):
        try:
            cursor.execute(
                f"DELETE FROM Role where {condition_dictionary}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, condition_dictionary, change_dictionary):
        try:
            cursor.execute(
                f"UPDATE Role "
                f"SET {', '.join(change_dictionary)} "
                f"Where {' and '.join(condition_dictionary)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls):
        try:
            cursor.execute(
                f"DELETE FROM Role"
            )
        except Exception as error:
            print(f"Error: {error}")


class Status(Entity):
    def __new__(
            cls, name_status=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.name_status = name_status
        return cls.instance

    @classmethod
    def add(cls):
        try:
            cursor.execute(
                "INSERT INTO Status "
                "(name_status)"
                "VALUES (?)",
                (
                    cls.instance.name_status,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, condition_dictionary):
        try:
            cursor.execute(
                f"DELETE FROM Status where {condition_dictionary}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, condition_dictionary, change_dictionary):
        try:
            cursor.execute(
                f"UPDATE Status "
                f"SET {', '.join(change_dictionary)} "
                f"Where {' and '.join(condition_dictionary)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls):
        try:
            cursor.execute(
                f"DELETE FROM Status"
            )
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    connection = sqlite3.connect('application.db')

    cursor = connection.cursor()
    # Role(name_role="Пользователь").add()
    Role.change(['name_role="Пользователь"'], ['name_role="user"'])
    # Status(name_status="активен").add()
    Status.change(['name_status="активен"'], ['name_status="activ"'])
    # Status.delete_all()
    # User(
    #     name_user="Ignat", login_user="ppp", mail_user="gg@mail.ru", password_user="123",
    #     time_add_user=datetime.date.today(), time_status_change_user=datetime.date.today(),
    #     status_user=1, role_user=1,
    # ).add()
    # User.delete('name_user="Ignat"')
    User.change(['name_user="Ignat"'], ['password_user="fsdgew"'])

    connection.commit()

    connection.close()


