# try: #有可能出现异常的代码
#     x = 6 / 2
#     print ( x )
# except  ZeroDivisionError as e: #异常类型as 实例,捕获特定异常
#     print ( '不能除零' , e )
# except:#后面不指定异常类型,指所有异常
#     print ( '其他错误' )
# else:
#     print ( '没有异常' )


# class Person:
#     def __init__(self,name):
#         self.name = name
#
# p = Person('KAT')
#
# try:
#     print(p.age)
# except AttributeError as e:
#     print('没有属性异常',e)


# f = open('date.txt')
# try:
#     f.read()
# except:
#     print('文件操作遇到错误')
# finally: #不管有没有异常,都要执行
#     f.close()

def method():
    raise NotImplementedError('该方法代码没有实现')# 手动抛出异常

method()