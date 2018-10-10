# print('hello,world')
# print('aaa','bbb','ccc')
# print(1+2)
# print('1 + 2 =',1+2)
# name=input()
# print(name)
# print("1024 * 768 =",1024*768)
# print('I\'m \"OK\"!')
# print("I'm OK!")
# print('I\'m learning\nPyrhon.')
# print('\\\n\\')
# print('\\\t\\')
# print(r'\\\t\\')
# print('''line
# line2
# line3''')
# print(r'''hello,\n
# world''')
#
# print(3>2)
# print(3>2 and 3<2)

# a='ABC'
# b=a
# a='XYZ'
# print(b)

#
# n=123
# f=456.789
# s1='hello,world'
# s2='hello,\'Adam\''
# S3=r'hello,"bart"'
# s4=r'''hello,lisa!'''
# print(2*'1')
# print(n,f,s1,s2,s3,s4)

# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(20013))
# print('\u42ed\u6587')
# print(ord('文'))
# print("0123456".find('1'))


# name='Lizz'
# print(name[0:2])
# print(np.array([1,-1])*np.array([1,1]))

# x = b'abc'
# print(x)
# print('中文'.encode('utf-8'))
# print('abc'.encode('ascii'))
# print(b'abc'.decode('ascii'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

# print(len('abc'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')))


# s1=72
# s2=85
#
# r=(s2-s1)/s1*100
# print('小明的成绩提升了%.1f%%'%r)
# print('小明的成绩提升了{0:.1f}%'.format(r))

# classmates=['michiael','bob','tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])

# classmates.append('adam')
# classmates.insert(1,'jack')
# classmates.pop()
# print(classmates)
# classmates[1]='vivian'
# print(classmates)
# L=['apple',123,True]
# s=['python','java',['asp','php'],'scheme']
# print(len(s))

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])
#
# age=20
# if age>=18:
#     print("your age is",age)
#
#
# age=3
# if age>=18:
#     print('your age is',age)
#     print('adutl')
# else:
#     print('your age is',age)
#     print('teenager')

# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')
#
# x=61
# if x:
#     print('True')


# s=input('birth:')
# birth=int(s)
# if birth<2000:
#     print('00前')
# else:
#     print('00后')

# height=1.75
# weight=80.5
# bmi=weight/(height**2)
# if bmi<18.5:
#     print('过轻')
# elif bmi<25:
#     print('正常')
# elif bmi<28:
#     print('过重')
# elif bmi<32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
#
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)
#
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)
#
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print("hello,%sL！"%name,)

# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue
#     print(n)

# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# index=0
# for a in names:
#     if a=='Bob':
#         print(scores[index])
#         break
#     else:
#         index+=1
#
#
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# d['Adam'] = 67
# print(d['Adam'])
# d['Jack'] = 90
# print(d['Jack'])
# d['Jack'] = 88
# print(d['Jack'])
#
# print('Jack' in d)
# print(d.get('Thomas',0))
# d.pop('Bob')
# print(d)
#
# s=set([1,2,3])
# print(s)
# s.add(4)
# print(s)
# s.remove(4)
# print(s)
# s1=set([2,3,4])
# print(s&s1)
#
# print(abs(100))
# print(max(1.111,1.112))
# print(int(12.2))
# a=abs
# print(a(-1))

# n1 = 255
# n2 = '1024'
# n3='45'
# print(int(n3,6))
# print(bin(int(n2,10)))
# print(str(hex(n1)))
# print(str(hex(n2)))


# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))
#
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs('a'))

# import math
#
# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
#
# x,y=move(100,100,60,math.pi/6)
# print(x,y)

# import math
#
# def quadratic(L):
#     for i in L:
#         int(L)
#          if not isinstance(i, (int, float)):
#             raise TypeError('bad operand type')
#     a=L[0]
#     b=L[1]
#     c=L[2]
#     d=b**2-4*a*c
#     if d>=0:
#         x1=(-b+math.sqrt(d))/(2*a)
#         x2=(-b-math.sqrt(d))/(2*a)
#         return x1,x2
#     else:
#         print("无解！！！")
#         return
# L=[]
# print('请输入一元二次方程的A,B,C:')
# for i in range(3):
#     L.append(input())
# try:
#     x1,x2=quadratic(L)
#     print(x1,x2)
# except:
#     print('请输入整数或小数')

# def power(x):
#     return x*x
# print(power(5))

# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(power(6))
# print(power(6,3))

# def enroll(name,gender,age=6,city='Beijing'):
#     print('name:',name)
#     print('gender:',gender)
#     print('age:',age)
#     print('city:',city)
# print(enroll('Shirely','F'))
#
# print(enroll('Bob','M',7))
# print(enroll('Adam','M',city='Tianjin'))
#
# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end([1,2,3]))
# print(add_end(['x','y','z']))
#
# print(add_end())
# print(add_end())
# print(add_end())

# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())
# print(add_end())

# def calc(numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# a=calc([1,2,3])
# print(a)
#
#
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(calc(1,2,3))
# print(calc(1,3,5,7))
# nums=[1,2,3]
# print(calc(*nums))
#
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# print(person('Michael',30))
# print(person('Shirley',21,city='Xi\'an'))
# extra={'city':'Beijing','job':'Engineer'}
# print(person('Jack',24,**extra))

# def person(name,age,**kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:',name,'age:',age,'other:',kw)
# print(person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456))
# def person(name,age,*args,city,job):
#     print(name,age,args,city,job)
# print(person('Jack',24,city='Beijing',job='Engineer'))

# def person(name,age,*,city='Beijing',job):
#     print(name,age,city,job)
# print(person('Jack',24,job='Engineer'))
#
# def person(name,age,city,job):
#     pass
#
# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# def f2(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# print(f1(1,2))
# print(f1(1,2,c=3))
# print(f1(1,2,3,'a','b'))
# print(f1(1,2,3,'a','b',x=99))
# print(f2(1,2,d=99,ext=None))
#
# args=(1,2,3,4)
# kw={'d':99,'x':'#'}
# print(f1(*args,**kw))
# args=(1,2,3)
# kw={'d':88,'x':"#"}
# print(f2(*args,**kw))

# def product(*nums):
#     for n in nums:
#         if not isinstance(n, (int, float)):
#             raise TypeError("参数类型错误！")
#     if len(nums)==0:
#         raise TypeError("参数数量不能为0")
#     else:
#         result=1
#         for n in nums:
#             result=result*n
#         return result
# print('请输入要计算乘积的数字:\'#\'结束')
# nums = []
# while(True):
#     a=input()
#     if a!='#':
#         nums.append(float(a))
#     else:
#         break
# print(product(*nums))

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# n=float(input())
#
# print(fact(n))

# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
#
# def move(n,a,b,c):
#     if n==1:
#         print(a,'-->',c)
#         return
#     elif n==2:
#         print(a,'-->',b)
#         print(a,'-->',c)
#         print(b,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(4,'a','b','c')

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print([L[0],L[1],L[2]])
# print(L[0:3])
# print(L[1:4])
# print(L[-2:-1])
#
# L=list(range(100))
# print(L[:20])
# print(L[-20:])
# print(L[:10:3])

# def trim(s):
#     while s[:1]==' ':
#         s=s[1:]
#     while s[-1:]==' ':
#         s=s[:-1]
#     return s
# s=input()
# print(trim(s))

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for key,value in d.items():
#     print(key,value)
# for ch in 'ABC':
#     print(ch)
# from collections import Iterable
# print(isinstance('abc',Iterable))
#
# for i,value in enumerate(['a','b','c']):
#     print(i,value)
# for x,y in [(1,1),(2,4),(3,9)]:
#     print(x,y)

# def findMinAndMax(L):
#     if not L:
#         print('没有输入数字，请重新输入!')
#         return None
#     min_value=L[0]
#     max_value=L[0]
#     for i in L:
#         if i<min_value:
#             min_value=i
#         elif i>max_value:
#             max_value=i
#     print((min_value,max_value))
# L=[]
# while(True):
#     a=input()
#     if a!='#':
#         L.append(float(a))
#     else:
#         break
# findMinAndMax(L)

# print(list(range(1,11)))
# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)
# print([x*x for x in range(1,11)if x%2==0])
# print([m+n for m in 'ABC' for n in 'XYZ'])
#
# import os
# print(d for d in os.listdir('.'))
#
# d={'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#     print(k,'=',v)
#
# d={'x':'A','y':'B','z':'C'}
# print([k + '=' + v for k,v in d.items()])

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower()for s in L])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2=[]
# for i in L1:
#     if(isinstance(i,str))==True:
#         L2.append(i)
# print(L2)
# print([i.lower() for i in L1 if(isinstance(i,str) == True)])

# L=[x * x for x in range(10)]
# print(L)
# g=(x * x for x in range(10))
# print(g)
# print(next(g))
# for n in g:
#     print(n)

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a + b
#         n = n + 1
#     return 'done'
# print(fib(7))

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a + b
#         n = n + 1
#     return 'done'
# for n in fib(7):
#     print(n)

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
# o = odd()
# next(o)

# g = fib(6)
# while(True):
#     try:
#         x = next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

# 生成器
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
# n = 0
# result = []
# for t in triangles():
#     print(t)
#     result.append(t)
#     n = n + 1
#     if n == 10:
#         break

# it = iter([1,2,3,4,5])
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break

# print(abs(-10))
# f=abs
# print(f(-10))

# def add(x,y,f):
#     return f(x) + f(y)
# print(add(-5,6,abs)

# def add(x, y, f):
#     return f(x) + f(y)
# list1 = [1,6,2,5,3]
# list2 = [34,67,13,678,67]
# print(add(list1,list2,max))

# def f(x):
#     return x * x
# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))
#
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#
# from functools import reduce
# def add(x,y):
#     return x + y
# print(reduce(add,[1,3,5,7,9]))

# from functools import reduce
# def fn(x,y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# print(reduce(fn,map(char2num,'13579')))

# from functools import reduce
# DIGHTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x,y):
#         return x * 10 + y
#     def char2nums(s):
#         return DIGHTS[s]
#     return reduce(fn,map(char2nums,s))
# print(str2int('12345678'))

# from functools import reduce
# DIGHTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2nums(s):
#     return DIGHTS[s]
# def str2int(s):
#     return reduce(lambda x,y: x *10 + y,map(char2nums,s))
# print(str2int('1234567'))


# def normalize(i):
#     return i.title()
# L1=['adam', 'LISA', 'barT']
# print(list(map(normalize,L1)))

# from functools import reduce
# def prod(L):
#     return reduce(lambda x,y:x*y,L)
# L=[]
# while(True):
#     a=input()
#     if a!='#':
#         L.append(float(a))
#     else:
#         break
# print(prod(L))

# from functools import reduce
# def str2float(s):
#     d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}
#     index = s.index('.')
#     s=s[:index]+s[index + 1 :]
#     result = reduce(lambda x,y : x * 10 + y,map(lambda x: d[x],s))
#     return result / pow(10,index)
# print('str2float(\'123.456\') = ',str2float('123.456'))

# def is_odd(n):
#     return n % 2 == 1
# print(list(filter(is_odd,[1,2,3,4,5,6,7])))
#
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,['a','',None,'c',' '])))

# def _odd_iter():#生成器生成从3开始的无限奇数序列
#     n=1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x : x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n),it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
#
# def is_palindrome(n):
#     strlist = list(str(n))
#     restrlist = strlist[::-1]
#     return strlist == restrlist
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:',list(output))

# print(sorted([36, 5, -12, 9, -21],key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return -t[1]
# L2=sorted(L,key=by_name)
# print(L2)

# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum()
# f = lazy_sum(1,3,5,7,9)
# f2= lazy_sum(1,3,5,7,9)
# print(f == f2)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count()
# print(f1())

# def createCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a = a + 1
#         return a
#     return counter()
# print(createCounter(),createCounter())

# print(list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9])))
# f= lambda x: x * x
# print(f(5))
# L = list(filter(lambda x : x % 2 == 1,range(1,20)))
# print(L)
#
# def now():
#     print('2015-3-25')
#
# f = now
#
# print(now.__name__)
# print(f.__name__)

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print('2015-3-25')
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('%s %s():' %(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')
# now()
# print(now.__name__)

import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw)
#             print('%s %s()': % (text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# import time,functools
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(args,**kw):
#         start = time.time()
#         fn(args,kw)
#         end = time.time()
#         print('%s executed in %s ms'%(fn.name,end-start))
#         return fn(*args,kw)
#     return wrapper
#
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# def int2(x,base=2):
#     return int(x,base)
# print(int2('1000000'))

# import functools
# int2 = functools.partial(int,base = 2)
# print(int2('1000000'))
# print(int2('1000000',base=10))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ' a test module '
#
# __author__ = 'Michael Liao'
#
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()
#
# class Studetn(object):
#
#     def__init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s:%s' % self.name,self.score)

# class Student(object):
#
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
# bart = Student('Bart Simpson',59)
# # bart.name = 'Bart Simpson'
# # bart.score = 59
# print(bart.name)
#
# def print_score(std):
#     print('%s: %s' % (std.name,std.score))
#
# print_score(bart)

# class Student(object):
#
#     def __init__(self,name,score,gender):
#         self.__name = name
#         self.__score = score
#         self.__gender = gender
#
#     def print_score(std):
#         print('%s: %s' % (std.__name, std.__score))
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >=60:
#             return 'B'
#         else:
#             return 'C'
#
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#
#     def set_score(self,score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         if gender == 'male' or 'female' :
#             self.__gender = gender
#         else:
#             raise ValueError('bad gender')
#
#
# bart = Student('Bart Simpson',59,'male')
# print(bart.get_gender())
# bart.set_gender('female')
# print((bart.get_gender()))

# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
#
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
#
# a = list()
# b = Animal()
# c = Dog()
#
# print(isinstance(a,list))
# print(isinstance(b,Animal))
# print(isinstance(c,Dog))
# print(isinstance(c,Animal))
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Animal())
# run_twice(Dog())
#
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')
#
# run_twice(Tortoise())
#
# class Timer(object):
#     def run(self):
#         print('Start...')
#
# run_twice(Timer())
#
# print(type(123))
# print(type(a))
# print(type(123)==type(456))

# import types
# def fn():
#     pass
#
# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
#
# a = Animal()
# b = Dog()
# h = Husky()
#
# isinstance(h,Husky)

# class Mydog(object):
#     def __len__(self):
#         return 100
# dog = Mydog()
# print(len(dog))
# print('ABC'.lower())
#
# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def power(self):
#         return self.x * self.x
#
# obj = MyObject()
#
# print(hasattr(obj,'x'))
# print(obj.x)
# print(hasattr(obj,'y'))
# setattr(obj,'y',19)
# print(hasattr(obj,'y'))
# print(obj.y)
# print(getattr(obj,'y'))
# print(getattr(obj,'z',404))
#
# print(hasattr(obj,'power'))
# fn = getattr(obj,'power')
# print(fn())
#
# def readImage(fp):
#     if hasattr(fp,'read'):
#         return readData(fp)
#     return None

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# s = Student('Bob')
# s.score = 90

# class Student(object):
#     name = 'Student'
#
# s = Student()
# print(s.name)
# print(Student.name)
# s.name='Machael'
# print(s.name)
# print(Student.name)

# class Student(object):
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         Student.count += 1
#
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Student(object):
#     pass
#
# s = Student()
# s.name = 'Micheal'
# print(s.name)
#
# def set_age(self,age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
#
# def set_score(self,score):
#     self.score = score
#
# Student.set_score = set_score
# s2 = Student()
# s.set_score(100)
# print(s.score)
#
# class Student(object):
#     __slots__ = ('name','age')
#
# s = Student()
# s.name = 'Shirley'
# s.age = 21
# s.score = 100

# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         self._score = value
#
# s = Student()
# s.set_score(99)
# print(s.get_score())
# s.set_score(1000)

# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100!')
#         self._score = value
#
# s = Student()
# s.score = 60
# print(s.score)
#
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
#
# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width = value
#
#
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._height * self._width
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Animal(object):
#     pass
#
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running...')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
# class Dog(Mammal,Runnable):
#     pass
#
# class Bat(Mammal,Runnable):
#     pass

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# print(Student('Shirley'))

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__
#
# print(Student('Shirley'))
# s = Student('Shirley')
# s

# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b = self.b,self.a + self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self, n):
#         a,b = 1,1
#         for x in range(n):
#             a,b = b,a + b
#         return a
#
# f = Fib()
# print(f[4])
# print(list(range(100))[5:10])

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int):
#             a,b = 1,1
#             for x in range(n):
#                 a,b = b,a + b
#                 return a
#         if isinstance(n,slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a,b = 1,1
#             L = []
#             for x in range(stop):
#                 if x>= start:
#                     L.append(a)
#                 a,b = b,a + b
#             return L
#
# f = Fib()
# print(f[0:5])
# print(f[5:20:2])

# class Student(object):
#
#     def __init__(self):
#         self.name = 'Shirley'
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#
#         if attr == 'age':
#             return lambda : 25
#
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# print(s.genter)

# class Chain(object):
#
#     def __init__(self,path = ''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path,path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list)
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
# s = Student('Micheal')
# print(s())

# from enum import Enum
#
# Month = Enum('Month',('Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)
#
# from enum import Enum,unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon
# print(day1)
#
# for name,member in Weekday.__members__.items():
#     print(name,'=>',member)
#
# from enum import Enum,unique
#
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Hello(object):
#     def hello(self,name = 'world'):
#         print('Hello,%s.'%name)
#
#
# h = Hello
# print(h.hello)
#
# print(type(Hello))
# print(type(h))
#
# def fn(self,name = 'world'):
#     print('Hello,%s.' %name)
#
# Hello = type('Hello', (object,), dict(hello = fn))
#
# h = Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))
#
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
# class Mylist(list,metaclass=ListMetaclass):
#     pass
#
# L = Mylist()
# L.add(1)
# print(L)

# class User(Model):
#
#      id = IntegerField('id')
#      name = StringField('username')
#      email = StringField('email')
#      password = StringField('password')
#
#
# class Field(object):
#
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#
#     def __init__(self, name):
#         super(StringField, self).__init__(name,'varchar(100)')
#
# class IntegerField(Field):
#
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name,'bigint')
#
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls,name,bases,attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
#         attrs['__table__'] = name  # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)
#
# class Model(dict, metaclass=ModelMetaclass):
#
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
# u = User(id = 12345, name = 'Shirley', email = 'lixyan@cn.ibm.com', password = '0.12310..')
#
# u.save()

# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
#
# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
#
# def foo(s):
#     return 10 /int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' %s)
#     return 10 / n
#
# foo(0)

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invaild value: %s' %s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# from functools import reduce
#
# def str2num(s):
#     isF1o = s.find('.')
#     if isF1o == -1:
#         return int(s)
#     else:
#         return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()