import sqlite3
from pprint import pprint

TABLE_NAME = 'user'
SQL_CMD = 'select id, name, card_number from user'

# create connect of db file
db_conn = sqlite3.connect('./db/win_sample.db')


# print(db_conn)

def get_data_by_cursor(sql_cmd=SQL_CMD):
    cursor = db_conn.cursor()
    datas = cursor.execute(sql_cmd)
    for _datas in datas:
        _id, _name, _card_number = _datas
        pprint('id: %s, _name: %s' % (_id, _name))


def get_data_by_cursor_with_map(sql_cmd=SQL_CMD):
    # [(1, 'test_user', 1), (2, 'test_user', 1), ...]
    cursor = db_conn.cursor()
    db_conn.row_factory = sqlite3.Row
    cursor.execute(sql_cmd)
    rows = cursor.fetchall()

    print(rows)


def test():
    get_data_by_cursor()
    get_data_by_cursor_with_map()


test()
