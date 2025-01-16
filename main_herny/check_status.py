import sqlite3
import os
import json
import datetime
from dateutil import parser


def delete_data_user_json(file_path):
    new_users_list = []
    with open(file_path, 'r') as file:
        existing_data = json.load(file)
        for user_object_dict in existing_data:
            for id_user, attribute_user in user_object_dict.items():
                if datetime.datetime.today() - parser.parse(attribute_user['time_status_change_user']) < datetime.timedelta(days=14):
                    print(id_user, attribute_user)
                    new_users_list.append({id_user: attribute_user})
    with open(file_path, 'w') as file:
        json.dump(new_users_list, file, indent=4)


def update_data_user_json(file_path, new_users_dict):
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except Exception as e:
        print(e)
        existing_data = []

    new_users_list = []
    for user in new_users_dict:
        user_data = {user: new_users_dict[user]}
        new_users_list.append(user_data)

    existing_data.extend(new_users_list)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)


def update_user_status(cursor_db):
    user_dict = {}
    user_dict_deactivate = {}
    deactivate_list = []
    cursor_db.execute("select * from User")
    for item in cursor_db.fetchall():
        user_object = {
            "name_user": item[1], "login_user": item[2], "mail_user": item[3],
            "password_user": item[4],
            "time_add_user": item[5], "time_status_change_user": item[6],
            "status_user": item[7], "role_user": item[8],
        }
        user_dict[item[0]] = user_object
        if item[7] == 1:
            user_dict_deactivate[item[0]] = user_object
            deactivate_list.append(str(item[0]))
    update_data_user_json("data_user.json", user_dict_deactivate)
    cursor_db.execute(
        f"DELETE FROM User where id_user in ({', '.join(deactivate_list)})"
    )


if __name__ == "__main__":
    data_base_file = 'application.db'
    if os.path.exists(data_base_file):
        connection = sqlite3.connect(data_base_file)
        cursor = connection.cursor()
        delete_data_user_json("data_user.json")
        # update_user_status(cursor)

        connection.commit()
        connection.close()
    else:
        print(f"База данных '{data_base_file}' не существует.")
