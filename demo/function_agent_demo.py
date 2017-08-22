def hello_chinese(name):
    print('你好' , name)


def hello_eglish(name):
    print('hello' , name)


def hello_canadel(name):
    print('xxxx' , name)


# 委托,比较绕,将函数作为参数传递给方法
def hello(action , name):
    action(name)


hello(hello_chinese , '来了')
hello(hello_eglish , '来了')
hello(hello_canadel , '来了')
hello(lambda name: print('韩文' , name) , '来了')
