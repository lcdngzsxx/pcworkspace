import datetime


class Book:
    def __init__(self , title , price='30' , author='cate' , publisher='xxxxx' , pubdate=datetime.date.today()):
        self.title = title
        self.price = price
        self.author = author
        self.publisher = publisher
        self.pubdate = pubdate

    def __repr__(self):
        return '<图书{} at 0x{}>'.format(self.title , id(self))

    def print_info(self):
        print('当前这本书的信息如下:')
        print('标题:{}'.format(self.title))
        print('价格:{}'.format(self.price))
        print('作者:{}'.format(self.author))
        print('出版社:{}'.format(self.publisher))
        print('出版日期:{}'.format(self.pubdate))

    def cls_method(cls):
        print('类函数')

    def staic_method():
        print('静态函数,逻辑上与实例无关')


book1 = Book('php' , '5' , 'cat' , 'cccc' , datetime.date(2017 , 8 , 20))
# print(book1.title)
# book1.print_info ()
#
# book2 = Book ( 'JAVA' )
# book2.print_info ()
# print ( book2.__repr__ () )

Book.cls_method(book1)
Book.staic_method()
