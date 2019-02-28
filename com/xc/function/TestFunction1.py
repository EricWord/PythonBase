# 函数的复习
# 取绝对值函数
# print(abs(-100))
# 取最大值
# print(max(99,1010,-292920,2929))
# 定义函数
# def my_bas(x):
#     if x > 0:
#         return x
#     else:
#         return -x
#
# print(my_bas(-3929))

# def power(x,n=2):
#     s=1
#     while (n>0):
#         s*=x
#         n=n-1
#
#     return s
#
# print(power(5))

# 定义参数可变的函数
# def sum(*nums):
#     s=0
#     for n in nums:
#         s+=n
#     return  s
#
# print(sum(100,200))

# 关键字参数
def disp(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


disp('二狗子', 30, city='北京')
