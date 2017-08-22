import shelve


def create_db():
    scores = [99 , 88 , 77]
    student = {'name': 'Mike' , 'age': 20}
    print(shelve.__file__)
    db = shelve.open('shelve_students.db')
    db['s'] = student
    db['c'] = scores
    print(len(db))
    db.close()


def query_db():
    db = shelve.open('shelve_students.db')
    print(db['c'])


def del_db():
    db = shelve.open('shelve_students.db')
    print(db['s'])
    del db['s']
    print(db['s'])


if __name__ == '__main__':
    query_db()
