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


base_read()
