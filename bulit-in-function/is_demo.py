class Obj():
    def __init__(self, arg):
        self.x = arg

if __name__ == '__main__':
    # is与==的区别就是，is是内存中的比较，而==是值的比较
    obj1 = Obj(1)
    obj2 = Obj(1)
    print(obj1 is obj2)  # False
    print(obj1 == obj2)  # True

    lst1 = [1]
    lst2 = [1]
    print(lst1 is lst2)  # False
    print(lst1 == lst2)  # True

    s1 = 'abc'
    s2 = 'abc'
    print(s1 is s2)  # True
    print(s1 == s2)  # True

    a = 2
    b = 1 + 1
    print(a is b)  # True

    a = 19998989890
    b = 19998989889 + 1
    print(a is b)  # False
