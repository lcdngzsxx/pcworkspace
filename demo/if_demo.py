score = 75

if score > 90:
    print('优')
elif score >= 80:
    print('良')
else:
    print('差')

if score >= 60:
    result = '及格'
else:
    result = '不及格'

# 类似JAVA中的 ? ....:.....
# Int A,B,C;
# A=2;
# B=3;
# C=A>B ? 100 :200;
resultl = '及格' if score >= 60 else '不及格'
print(result)
print(resultl)
