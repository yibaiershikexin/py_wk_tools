import csv
from pprint import pprint

csv_file = open('../datas/data.csv', 'r')


def test_base():
    '''title show, '''
    reader = csv.reader(csv_file)

    for row in reader:
        pprint(row)


def test_dictreader():
    '''csv title not show,  recoder format like: OrderedDict([('titlt1', 'data1'), ('titlt2', 'data2'),...')])'''
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row)














test_dictreader()
