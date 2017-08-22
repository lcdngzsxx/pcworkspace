# f = open('demo.text','a',encoding='utf-8')
# f.write('我家住在黄土高坡\n'
#         '那大风嗖嗖\n'
#         '剩下的词是啥'
#         '母鸡')
# f.close()


f = open('demo.text' , 'r' , encoding='utf-8')
for line in f:
    print(line , end=' ')
    # print(f.__next__())
    # print(next(f))
