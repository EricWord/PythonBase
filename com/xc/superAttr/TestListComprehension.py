#列表生成式
# print(list(range(1,11)))
#生成[1x1, 2x2, 3x3, ..., 10x10]
# L=[]
# for x in range(1,11):
#     L.append(x*x)
#
# print(L)

# L=[x*x for x in range(1,11)]
# print(L)
#生成全排列
# L=[m+n for m in 'ABC' for n in 'XYZ' ]
# print(L)

# import  os
# L=[d for d in os.listdir('.')]
# print(L)

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# L=[k+'='+v for k,v in d.items()]
# print(L)
#将所有字符串变为小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# li=[s.lower() for s in L]
# print(li)

#生成器
# g=(x*x  for x in range(10))
# for n in g:
#     print(n)


def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'

fib(6)