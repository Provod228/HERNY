import sqlite3
import datetime
from dateutil import parser


def update_user_status(cursor_db):
    deactivate_list = []
    cursor_db.execute("select time_status_change_user, id_user, status_user from User")
    for item in cursor_db.fetchall():
        if datetime.datetime.today() - parser.parse(item[0]) > datetime.timedelta(days=14) and item[2] == 4:
            deactivate_list.append(str(item[1]))
    print(deactivate_list)
    cursor_db.execute(
        f"DELETE FROM User where id_user in ({', '.join(deactivate_list)})"
    )


if __name__ == "__main__":
    connection = sqlite3.connect('application.db')
    cursor = connection.cursor()
    update_user_status(cursor)

    connection.commit()
    connection.close()
