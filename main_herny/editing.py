import hashlib
import sqlite3
import datetime
from abc import ABCMeta, abstractmethod


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def add(self, cursor_db):
        pass

    @abstractmethod
    def delete(self, cursor_db, condition_list):
        pass

    @abstractmethod
    def change(self, cursor_db, condition_list, change_list):
        pass

    @abstractmethod
    def delete_all(self, cursor_db):
        pass


class User(Entity):
    def __new__(
            cls, name_user=None, login_user=None, mail_user=None, password_user=None,
            time_add_user=None, time_status_change_user=None, status_user=1, role_user=1,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.name_user = name_user
        cls.instance.login_user = login_user
        cls.instance.mail_user = mail_user
        cls.instance.password_user = hash_password(password_user)
        cls.instance.time_add_user = time_add_user
        cls.instance.time_status_change_user = time_status_change_user
        cls.instance.role_user = role_user
        cls.instance.status_user = status_user
        return cls.instance

    @classmethod
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
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
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM User where {condition_list}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        for change_list_index in range(len(change_list)):
            if "password_user" in change_list[change_list_index]:
                list_change = change_list[change_list_index].split('"')
                password = hash_password(list_change[1])
                new_password = list_change[0] + '"' + password + '"'
                change_list.pop(change_list_index)
                change_list.append(new_password)
            elif "status_user" in change_list[change_list_index]:
                print(' and '.join(condition_list))
                cursor_db.execute(
                    f"select status_user "
                    f"from User"
                    f"Where {' and '.join(condition_list)}"
                )
                # if change_list[change_list_index].split('"')[1]:
                date_time = datetime.datetime.today()
                print(change_list[change_list_index].split('"')[1])
                new_date_time = "time_status_change_user=" + '"' + str(date_time) + '"'
                change_list.append(new_date_time)
            print(change_list)
        try:
            cursor_db.execute(
                f"UPDATE User "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
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
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
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
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM Role where {condition_list}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        try:
            cursor_db.execute(
                f"UPDATE Role "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
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
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
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
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM Status where {condition_list}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        try:
            cursor_db.execute(
                f"UPDATE Status "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
                f"DELETE FROM Status"
            )
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    connection = sqlite3.connect('application.db')
    cursor = connection.cursor()
    # User.delete_all(cursor)
    # Role(name_role="Пользователь").add(cursor)
    # Role(name_role="Менеджер").add(cursor)
    # Role(name_role="Администратор").add(cursor)
    # Role.delete_all(cursor)
    # Role.change(cursor, ['name_role="Пользователь"'], ['name_role="user"'])
    # Status(name_status="Активный").add(cursor)
    # Status(name_status="Уточнение").add(cursor)
    # Status(name_status="Не активный").add(cursor)
    # Status(name_status="Удалён").add(cursor)
    # Status.delete_all(cursor)
    # Status.change(cursor, ['name_status="активен"'], ['name_status="activ"'])
    # Status.delete_all()
    # User(
    #     name_user="Ignat", login_user="aaa", mail_user="ggg@mail.ru", password_user="123",
    #     time_add_user=datetime.datetime.today(), time_status_change_user=datetime.datetime(2025, 1, 1),
    #     status_user=1, role_user=1,
    # ).add(cursor)
    # User.delete('name_user="Ignat"')
    User.change(cursor, ['login_user="aaa"'], ['status_user="4"'])

    connection.commit()

    connection.close()

    # ss = {
    #     'id_user': "",
    #     'name_user': "",
    #     'login_user': "",
    #     'mail_user': "",
    #     'password_user': "",
    #     'time_add_user': "",
    #     'time_status_change_user': "",
    #     'role_user': "",
    #     'status_user': "",
    # }


