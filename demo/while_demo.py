# x = 10
# while x:
#     x -= 1
#     if x%2 != 0:# %取余
#         continue
#     print(x,end=' ')


# while True:
#     name = input('请输入你的姓名:')
#     if name == 'stop':
#         break
#     age = input('请输入你的年龄:')
#     age = int(age)
#     if age<0 or age>100:
#         age = input('滚犊子,请输入你的正确年龄:')
#     print('你好:{},你的年龄是:{}'.format(name,age))

# for x in range(1,5):
#     if x == 6:
#         print('没有这个数字',x)
#         break
# else:
#     print('未找到')


# emp = {
#     'name':'Cat',
#     'department':'technoloty',
#     'job':'development',
#     'salart':1000.00
# }
#
# for key in emp:
#     print('{}=>{}'.format(key,emp.get(key)))
#
# for value in emp.values():
#     print(value)
#
# print(type(emp))
# print(emp)
# print(type(emp.values()))

def hello_chinese(name):
    print('你好',name)

def hello_eglish(name):
    print('hello',name)

def hello_canadel(name):
    print('xxxx',name)

#委托,比较绕,将函数作为参数传递给方法
def hello(action,name):
    action(name)

hello(hello_chinese,'来了')
hello(hello_eglish,'来了')
hello(hello_canadel,'来了')
hello(lambda name:print('韩文',name),'来了')