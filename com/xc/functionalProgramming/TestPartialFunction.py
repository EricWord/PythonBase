#偏函数
print(int('12345',base=8))
#创建一个偏函数
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))