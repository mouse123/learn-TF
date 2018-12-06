#coding=utf-8
print('hello python','it is good')
print('100+200=',100+200)
# name = input('please input your name:')
# print(name)
a = 100
if a>=0:
    print(a)
else:
    print(-a)

print('I\'m \"OK\"!')
print('''line1
line2
line3''')
print(True and False)
print(not False)
print(None == 0)
print(10/3)
print(10//3)
print(10%3)
print('Hi,%s,your scope is %d' %( 'Mouse',60 ))
# print('Hi,100%')
print(list(range(5)))

# 字典 dict == json == key:value
# print(my_abs(10))
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x 
print(my_abs(-10))
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))

L = list(range(100))
print(L[:])#复制
print(L[:10])#前十个
print(L[-10:])#后十个
print(L[5:10])#第五到第十
print(L[:10:2])#前十个 => 每两个取一个
print(L[::5])#每五个取一个
print('ABCDEFG'[:3])#字符串也可以
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys()==d)
print(d.values())
print(d.items())
for key in d:#无序输出
    print(key)
for key, value in d.items():
    print(key,':',value)
# for j in 'ABCD':
#     print(j)
# for i, value in enumerate(['A', 'B', 'C']):#enumerate list下标
#     print(i, value)
# list comprehensions
print([x*x for x in range(1,11) if x%2 == 0])# x*x => for in 循环执行的过程代码  判断代码可以写在循环后面
print([x+y for x in 'ABC' for y in 'XYZ' if x+y != 'AX'])

import os #操作文件
print([d for d in os.listdir('.')])
g = ( x*x for x in range(1,11))#generator也是可迭代对象
for n in g:
    print(n)
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'
f=fib(6)#generator对象
# for i in f:
#     print (i)
while True:
    try:
        x = next(f)
        print('x',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print(abs(-10)) #abs 函数名 
f = abs
print(f(-10))
# abs = 10 
# print(abs(-10))

print(list(map(abs,[1,-1,2,-2,3,-3])))
print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['1'])

from functools import reduce
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s],s))

print(str2int('2468'))

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         print(n)
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# p = primes()
# next(p)
# next(p)
# next(p)  

print(sorted(['A','b','C','D','e'],key = str.lower,reverse = True))

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200,200))
im.save('thumb.png','png')

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 81))
# # 发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)

# s.close()

# header.html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# with open('sina.html', 'wb') as f
#     f.write(html)
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()