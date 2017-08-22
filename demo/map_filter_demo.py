l = list(range(1 , 11))


#
# print(l)
#
# result = []
#
# for n in l:
#     if n%2 == 0:
#         result.append(n)
#
# print(result)
#
# 匿名函数,委托
# res = list(map(lambda n:n+5,l))
# print(res)

def even_number(x):
    return x % 2 == 0


# res = filter(even_number,l)
res = filter(lambda n: n % 2 == 0 , l)
print(res)

for n in res:
    print(n , end=',')
