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


def test_write_csv():
    from csv import writer

    title = ['No', 'name', 'size']
    recoders = ['1', 'b', 2]
    f_path = './tmp.csv'
    with open(f_path, 'w') as obj_f:
        csv_writer = csv.writer(obj_f)
        csv_writer.writerow(title)
        csv_writer.writerow(recoders)
        csv_writer.writerow(recoders)


def main():
    # test_dictreader()
    test_write_csv()


main()
