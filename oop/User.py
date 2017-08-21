import  datetime

class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday

    @property
    def age(self):
        return datetime.date.today().year - self.birthday.year
    @age.setter
    def age(self,value):
        raise AttributeError('禁止赋值年龄!')
    @age.deleter
    def age(self):
        raise AttributeError('不能删除年龄')

# class Programer ( User ):
#     def __init__ (self , name , birthday , work):
#         super().__init__ (name , birthday)
#         self.work = work
#
#     def workinig (self):
#         print ( '用户{}正在做:{}东西'.format ( self.name , self.work ) )
#
# p = Programer ( '小海哥' , datetime.date( 1989 , 8 , 1 ) , '写代码' )
# p.workinig ()

# u = User( '小海哥' , datetime.date( 1989 , 8 , 1 ) )
# print( u.birthday )
# print( u.age )
# e.birthday = datetime.date(1998,8,7)
# print(e.birthday)
# e.age = '20'
# del(u.age)
# print( u.name )
# del(u.name)
# print( u.name )
