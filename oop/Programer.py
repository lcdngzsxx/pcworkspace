import datetime
# import oop.User as User
from oop.User import User


class Programer(User):
    def __init__(self , name , birthday , work):
        super().__init__(name , birthday)
        self.work = work

    def workinig(self):
        print('用户{}正在做:{}东西'.format(self.name , self.work))


p = Programer('小海哥' , datetime.date(1989 , 8 , 1) , '写代码')
p.workinig()
