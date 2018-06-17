# encoding=utf-8
import agate
import datetime
import random
from pprint import pprint


def create_by_list():
    column_names = ['letter', 'number']
    column_types = [agate.Text(), agate.Number()]

    rows = [
        ('a', 1),
        ('b', 2),
        ('c', None)
    ]
    table = agate.Table(rows, column_names, column_types)
    return table


def create_by_dict():
    rows = [
        dict(letter='a', number=1),
        dict(letter='b', number=2),
        dict(letter='c', number=None)
    ]

    table = agate.Table.from_object(rows)
    return table


def create_by_csv():
    table = agate.Table.from_csv('data.csv')
    return table


def create_by_csv_define_type():
    text_type = agate.Text()
    number_type = agate.Number()

    csv_title = ['Country', 'Year', 'Infants exclusively breastfed for the first six months of life (%)']
    csv_type = [text_type, text_type, text_type]

    table = agate.Table.from_csv('data.csv', column_names=csv_title,
                                 column_types=csv_type, encoding='utf-8', delimiter=',', header=False)
    # # you can use this method to load data from a file that does not have a header row:
    # table = agate.Table.from_csv('data.csv', column_names=csv_title, column_types=csv_type, header=False)
    # # 标记解析式用的数据分隔符
    # table = agate.Table.from_csv('data.csv', column_names=csv_title, column_types=csv_type, delimiter=',')
    return table


def override_data_type():
    # In some cases agate’s TypeTester may guess incorrectly.
    # To override the type for some columns and use TypeTester for the rest,
    # pass a dictionary to the column_types argument.
    specified_types = {
        'column_name_one': agate.Text(),
        'column_name_two': agate.Number()
    }
    table = agate.Table.from_csv('data.csv', column_types=specified_types)
    return table


def limit_large_data():
    tester = agate.TypeTester(limit=100)
    table = agate.Table.from_csv('data.csv', column_types=tester)


def write_to_json(table):
    table.to_json('data.json', newline=True)


def write_to_csv(table):
    table.to_csv('data.csv')


def write_to_db(table):
    import agatesql
    table.to_sql('postgresql:///database', 'output_table')


def table_define(table):
    #
    include_columns = ['column_name_one', 'column_name_two']
    inclue_table = table.select(include_columns)
    exclude_columns = ['column_name_one', 'column_name_two']
    exclude_table = table.exclude(exclude_columns)


def control_table_data(table):
    import re
    new_table = table.where(lambda row: re.match('^C', row['state']))
    new_table = table.where(lambda row: not re.match('\d{3}-\d{3}-\d{4}', row['phone']))

    # windows 类似的匹配模式
    from fnmatch import fnmatch
    new_table = table.where(lambda row: fnmatch('C*', row['state']))

    new_table = table.where(lambda row: 100000 < row['income'] < 200000)
    new_table = table.where(lambda row: datetime.datetime(2015, 6, 1) <= row['date'] <= datetime.datetime(2015, 8, 31))
    new_table = table.where(lambda row: 6 <= row['date'].month <= 8)

    # Top N percent
    percentiles = table.aggregate(agate.Percentiles('salary'))
    top_ten_percent = table.where(lambda r: r['salary'] >= percentiles[90])

    # Ordered sample
    sampled = table.limit(step=10)

    # Random sample
    randomized = table.order_by(lambda row: random.random())
    sampled = table.limit(10)

    # Distinct values
    columns = ('value',)
    rows = ([1], [2], [2], [5])
    new_table = agate.Table(rows, columns)
    # >>     (Decimal('1'), Decimal('2'), Decimal('5'))
    new_table.columns['value'].values_distinct()
    # or
    new_table.distinct('value').columns['value'].values()


def main():
    # #
    # table = create_by_list()
    # # <agate.table.Table object at 0x000001CD7A53AE80>
    # # letter, number
    # # a, 1
    # # b, 2
    # # c,
    # # None
    # pprint(table)
    # print(table.print_csv())
    # #
    # table_dict = create_by_dict()
    # #
    # table_csv = create_by_csv()
    # pprint(table_csv.print_csv())

    table_csv_specify_type = create_by_csv_define_type()
    pprint(table_csv_specify_type)


main()
