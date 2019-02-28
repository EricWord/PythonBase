def f(x):
    return  x*x


# r=map(f,[1,2,3,4,5,6,7,8,9])
#
# print(list(r))

#使用for循环实现与上面相同的效果
# L=[]
# for n in [1,2,3,4,5,6,7,8,9]:
#     L.append(f(n))
#
# print(L)

from functools import  reduce
# def add(x,y):
#     return  x+y
# print(reduce(add,[1,3,5,7,9]))

#将数字转为字符串
# L=list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(L)
#将序列转为整数
def fn(x,y):
    return  x*10+y

r=reduce(fn,[1,3,5,7,9])
print(r)
#将字符串转为int
def char2num(s):
    #字符与数字对应的字典
    digits={'0': 0 , '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    return digits[s]
r1=reduce(fn,map(char2num,'13579'))
print(r1)






