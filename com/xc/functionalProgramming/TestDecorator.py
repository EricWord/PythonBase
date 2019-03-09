#装饰器就是一个返回函数的高阶函数
#一个可以打印日志的decorator
#注意一个*是可变参数，两个*是关键字参数
def log(func):
    def wrapper(*args,**kw):
        #注意__name__是两个下划线
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper



@log
def now():
    print('2019-03-09')
now()
#自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('执行')
def now():
    print('现在时间')

now()
print(now.__name__)

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('执行')
def now():
    print('现在时间')

now()
print(now.__name__)




