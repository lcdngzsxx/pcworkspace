import shelve


class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


def write_shelve():
    s = Student('Tom' , 20)
    db = shelve.open('student')
    db['s'] = s
    db.close()


def read_shelve():
    db = shelve.open('student')
    return db['s']


if __name__ == '__main__':
    print(read_shelve())
