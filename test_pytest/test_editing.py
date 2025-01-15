import datetime
import pytest
from HERNY.main_herny.editing import User


def test_user(test_db_connection):
    user_dict = {}
    index = 0
    for item in test_db_connection:
        user_dict[index] = {
            "id_user": item[0], "name_user": item[1], "login_user": item[2],
            "mail_user": item[3], "password_user": item[4], "time_add_user": item[5],
            "time_status_change_user": item[6], "status_user": item[7], "role_user": item[8],
        }
        index += 1
    for k, v in user_dict.items():
        print(v)
        assert isinstance(v["id_user"], int)
        assert isinstance(v["name_user"], str)
        assert isinstance(v["login_user"], str)
        assert isinstance(v["mail_user"], str)
        assert isinstance(v["password_user"], str)
        assert isinstance(v["time_add_user"], str)
        assert isinstance(v["time_status_change_user"], str)
        assert isinstance(v["status_user"], int)
        assert isinstance(v["role_user"], int)
