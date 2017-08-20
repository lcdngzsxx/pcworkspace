# #定义函数
# def read_book():
#     print('拿到一本书')
#     print('打开')
#     print('倒一杯茶')
#     print('先烧一下开水')
#     print('数就先不看了')
# #调用函数
# read_book()
#
#
#
#
# def add ( x ):
#     print ( x + 10 )
#
# add(5)
#
# operation = {  # 数据字典
#     'add': add ,
#     'uppdate': lambda x: print ( x * 2 ) ,
#     'delete': lambda x: print ( x - 4 )}
#
#
# def default_method ( x ):
#     print ( '默认/构造方法,什么都不做' )
#
#
# operation.get ( 'delete') ( 10 )

#单星号,接受的是tuple
# def avg(*socres):
#     return sum(socres)/len(socres)
#
# s = (88,89,90)
#
# result = avg(s)
#
# print(result)

#双星号,接受的是dict
def dis_emp(**emp):
    print(emp)

dis_emp(name='Cat',age='18',jon='dev',depart='devp')