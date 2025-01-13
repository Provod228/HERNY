import sqlite3


def add_db(entity: str = None, entity_dictionary: dict = None) -> None:
    if entity is None or entity_dictionary is None:
        raise AttributeError(f"{entity}, {entity_dictionary}, all attributes must not contain: None")
    try:
        attributes = list(entity_dictionary.keys())
        attributes_value = list(entity_dictionary.values())
        placeholders = ", ".join("?" * len(entity_dictionary))
        sql = f"INSERT INTO {entity} ({', '.join(attributes)}) VALUES ({placeholders})"
        cursor.execute(sql, attributes_value)
    except Exception as error:
        print(f"Error: {error}")


def delete_db(entity: str = None, condition_dictionary: str = None) -> None:
    if entity is None or condition_dictionary is None:
        raise AttributeError(f"{entity}, {condition_dictionary}, all attributes must not contain: None")
    try:
        sql = f"DELETE FROM {entity} where {condition_dictionary}"
        cursor.execute(sql)
    except Exception as error:
        print(f"Error: {error}")


def change_db(entity: str = None, condition_dictionary: str = None, entity_dictionary: dict = None) -> None:
    if entity is None or entity_dictionary is None or condition_dictionary is None:
        raise AttributeError(
            f"{entity}, {entity_dictionary}, {condition_dictionary}, all attributes must not contain: None"
        )
    try:
        attributes = list(entity_dictionary.keys())
        attributes_value = list(entity_dictionary.values())
        placeholders = [f'{attributes[index]} = "{attributes_value[index]}"' for index in range(len(entity_dictionary))]
        sql = f" UPDATE {entity} SET {', '.join(placeholders)} Where {condition_dictionary}"
        print(sql)
        cursor.execute(sql)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    connection = sqlite3.connect('application.db')

    cursor = connection.cursor()

    # add_db(
    #     "Role",
    #     {"name_role": "Админ"}
    # )
    #
    # add_db(
    #     "Role",
    #     {"name_role": "Модератор"}
    # )

    # delete_db(
    #     "Role",
    #     'name_role = "Админ"'
    # )

    # change_db(
    #     "Role",
    #     'name_role = "Модератор"',
    #     {"name_role": "moder"}
    # )

    connection.commit()

    connection.close()


