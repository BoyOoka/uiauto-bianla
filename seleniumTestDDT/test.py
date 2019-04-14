import csv
import xlrd
def get_data_excel(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    print(sheet.nrows)
    print(sheet.ncols)
    print(sheet.row_values(1, 0, 2))
    # for row_idx in range(1, sheet.nrows):
    #     rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    #     print(sheet.row_values(1,0))
    #     print(row_idx, sheet.ncols)
    # print(rows)
    return rows

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    # 跳过第一行
    next(reader, None)
    for row in reader:
        rows.append(row)
    print(rows)
    return rows

#get_data('testdata.csv')

get_data_excel('testdata.xlsx')
