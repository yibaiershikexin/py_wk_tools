import xlrd
import xlwt
import xlutils
from pprint import pprint

excel_file = '../datas/from intranet.xls'


def base_read():
    book = xlrd.open_workbook(excel_file)
    # iter sheet
    for sheet in book.sheets():
        pprint(sheet.name)
        pprint(sheet.nrows)
        # iter sheet data row
        for row in range(sheet.nrows):
            row_data = sheet.row_values(row)
            print(row_data)
            for cell in row_data:
                pprint(cell)

    # pprint(book.sheet_by_name('bauck_1'))


def dir_sheet():
    book = xlrd.open_workbook(excel_file)
    sheet = book.sheet_by_name('bauck_1')
    pprint(dir(sheet))


def xlrd_get_xls_property():
    import xlrd
    from xlrd.sheet import ctype_text

    # {0: 'empty', 1: 'text', 2: 'number', 3: 'xldate', 4: 'bool', 5: 'error', 6: 'blank'}
    print(ctype_text)

    workbook = xlrd.open_workbook('data.xls')
    sheet_0 = workbook.sheets()[0]
    title = sheet_0.row_values(0, start_colx=0, end_colx=None)
    row = sheet_0.row_values(6, start_colx=0, end_colx=None)
    print(row)
    print(sheet_0.row(6))
    print(sheet_0.row(6)[0].ctype)
    print(sheet_0.row(6)[0].value)


base_read()
