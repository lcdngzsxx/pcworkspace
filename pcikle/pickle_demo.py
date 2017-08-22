import pickle

'''presistent'''
# person = {'name': 'cat' , 'age': 20}
# print ( type ( person ) )
# p = pickle.dumps ( person )
# print ( p )
# print ( type ( p ) )
#
# cat = {'name':'kitty','character':'kawayi'}
#
# pickle.dump(cat,open('cat_db','wb'))

'''unpresistent'''
cat = pickle.load(open('cat_db' , 'rb'))
print(type(cat))
print(cat)
