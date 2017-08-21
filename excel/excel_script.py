import xlrd

def xl_read():
    '''excel read '''
    book = xlrd.open_workbook('tmp001.xls')
    for sheet in book.sheets():
        print(sheet.name)

def xl_read_data():
    '''数据读取 '''
    book = xlrd.open_workbook('tmp001.xls')
    sheet = book.sheet_by_name('areas')
    print('sheet name :{}'.format(sheet.name))
    print('sheet rows :{}'.format(sheet.nrows))
    print('area date')
    print('='*50)
    for i in range((sheet.nrows)):
        print(sheet.row_values(i)) # get index data


if __name__ == '__main__':
    xl_read_data()