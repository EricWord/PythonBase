#使用sorted函数对list进行排序
l=sorted([12,-37,99,0,22])
# print(l)
#按照绝对值大小排序
l=sorted([12,-37,99,0,22],key=abs)
# print(l)
l=sorted(['Jack','anaoncod','gooD','Python'],key=str.lower,reverse=True)
print(l)