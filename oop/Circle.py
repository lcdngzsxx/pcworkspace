import math


class Circle:
    def __init__(self , radius):
        self.radius = radius

    # 方法,使用的时候为属性
    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(4.0)
print("圆的面积是:{}".format(c.area))
