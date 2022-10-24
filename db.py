import sqlite3



DATABASE_NAME = 'user_inews.db'


def create_table_users():
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS USERSiNEWS ('
                   'id INTEGER AUTO INCREMENT, '
                   'id_telegram INTEGER NOT NULL, '
                   'username TEXT NOT NULL, '
                   'name TEXT, '
                   'phone TEXT, '
                   'email TEXT)'
                   )
    connect.commit()
    connect.close()


def add_user(user: dict):
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    get = f'INSERT INTO USERSiNEWS (' \
          f'id_telegram,' \
          f'username, ' \
          f'name,' \
          f'phone,' \
          f'email' \
          f') VALUES (' \
          f'"{user["id_telegram"]}", ' \
          f'"{user["username"]}", ' \
          f'"{user.get("name")}", ' \
          f'"{user.get("phone")}", ' \
          f'"{str(user.get("email"))}"' \
          f');'
    cursor.execute(get)
    connect.commit()
    connect.close()


def get_user(id_telegram: int):
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    get = f'SELECT * FROM USERSiNEWS WHERE id_telegram="{id_telegram}"'
    result = cursor.execute(get)
    data = result.fetchall()
    return data


def get_users():
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    get = f'SELECT * FROM USERSiNEWS'
    result = cursor.execute(get)
    data = result.fetchall()
    return data


if __name__ == '__main__':
    create_table_users()
    # add_user({
    #     'id_telegram': 1234567,
    #     'username': 'test_full',
    #     'name': 'test',
    #     'phone': '05051909123',
    #     'email': 'aaa@xxx.com',
    # })
    # add_user({
    #     'id_telegram': 123456,
    #     'username': 'test_name',
    #     'name': 'test',
    # })
    # add_user({
    #     'id_telegram': 123456,
    #     'username': 'test_email',
    #     'email': 'aaa@xxx.com'
    # })
    # print(get_user(1234567))
