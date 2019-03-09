#匿名函数
ls=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(ls)

#匿名函数也是一个函数对象，也可以把一个匿名函数赋值给一个变量，再利用变量来调用该函数
f=lambda x:x*x
print(f(5))
#将匿名函数作为返回值返回
def build(x,y):
    return lambda : x*x+y*y

print(build(1,2))