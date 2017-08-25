class Obj():
    def __init__(self, arg):
        self.x = arg


if __name__ == '__main__':
    obj = Obj(1)
    print(id(obj))

    obj1 = Obj(2)
    print(id(obj1))

    s = "abc"
    print(id(s))
    
    x = 1
    print(id(x))
    x = 2
    print(id(x))