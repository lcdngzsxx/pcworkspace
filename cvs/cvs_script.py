import csv


def cvs_read():
    '''cvs read'''
    with open('city.csv' , encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        # print(headers)
        for row in reader:
            print('id:{} name:{} countcode:{} district:{} population:{}'.format
                  (row[0] , row[1] , row[2] , row[3] , row[4]))


# def csv_read_by_namedtuple():
#     '''read csv name with tuple'''
#     with open('city.csv',encoding='utf-8') as f:
#         reader = csv.reader(f)
#         header = next(reader)
#         Row = namedtuple('Row',header)

def cvs_read_by_dict():
    '''read into dict'''
    with open('city.csv' , encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


def cvs_read1():
    '''cvs read'''
    with open('areas.csv' , encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        # print(headers)
        for row in reader:
            print('id:{} name:{} countcode:{} district:{} population:{}'.format
                  (row[0] , row[1] , row[2] , row[3] , row[4]))


def cvs_file():
    print(csv.__file__)


if __name__ == '__main__':
    cvs_file()
