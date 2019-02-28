#复习迭代
d={'小明':88,'王者':89,'二狗子':90,'狗三儿':67,'铁蛋儿':56}
# for key in d:
#     print(key)

# for value in d.values():
#     print(value)
#同时迭代key value
# for k,v in d.items():
#     print(k,v)
#字符串也是可迭代对象
# for s in 'ABC':
#    print(s)
#判断是否可迭代

# from  collections.abc import Iterable
# print(isinstance('absc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))

for i,v in enumerate(['A','B','C']):
    print(i,v)
