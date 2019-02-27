# -*- coding: utf-8 -*-
name=input('请输入你的姓名：')
print('hello,',name)
print('I\'m ok')
print('''好多行哈
好多行啊
好多行呢''')
#转移字符\
print('\\\t\\')
#r修饰的字符不转义
print(r'\\\t\\')
print(True or True)
print(True and True)
print(not True)
age=input('请输入年龄:')
if(age>18):
    print('成年人')
else:
    print('未成年')
#除法
print(10/3)
#地板除
print(10//3)
#获取字符的整数表示
a=ord('A')
print(a)
#把编码转为对应的字符
b=chr(25991)
print(b)
print('\u4e2d\u6587')
#使用encode将字符转为字节数组
byte='ABX'.encode('ascii')
print(byte)
byte2='中文'.encode('utf-8')
print(byte2)
#使用decode将字节数组转为字符串
res2=b'ABC'.decode('ascii')
print(res2)
#忽略部分错误
res3=b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
print(res3)
#字符串中有多少个字符
print(len('中国'))
#一个中文字符经过UTF-8编码后通常会占用3个字节
#一个英文字符经过UTF-8编码后通常会占用1个字节
print(len('中国'.encode('utf-8')))
#格式化字符串
print('hello,%s'%'小崔')
print('hello,%s,你有$%d银行存款'%('小崔',10000))
#%的转义
print('七日年化利率为%d%%'%8)
print('hello,{0},七日年化利率提升{1:.1f}%'.format('欧阳夏凡',17.192))



