import dataset
from pprint import pprint

'''# create new table
table = db['user']
# insert data to table
table.insert(my_data_source)'''

# create connect of db file
db = dataset.connect('sqlite:///db/win_sample.db')

# prepare table data
my_data_source = {
    'name': 'test_user',
    'card_number': 1,
    'interest': 'book',
}


def create_table_insert_datas(table_name, table_datas):
    obj_table = create_table(table_name)
    insert_datas(obj_table, table_datas)


def create_table(table_name):
    table = db[table_name]
    return table


def insert_datas(obj_table, table_datas):
    obj_table.insert(table_datas)


def get_all_datas(table_name):
    return db[table_name].all()


def show_all(table_name):
    datas = get_all_datas(table_name)
    for i in datas:
        pprint(i)


def test():
    # create_table_insert_datas('user', my_data_source)
    show_all('user')


test()
