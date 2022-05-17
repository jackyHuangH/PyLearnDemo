# python基础练习
from collections.abc import Iterable
import sys
import math
import functools
import time

# from...import... 导入特定成员
from sys import argv, path

# r字符串，屏蔽转义
print("this is a \n long string")
print(r"this is a \n long string")
print(f'''我是字符串看看
... djk kjk
... kdjkHjkdhfj 
好好好''')

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
string = "谁说站在光里的才算英雄"
# 不换行输出，末尾加上end=""
print(string, end="")
print(string*2)
# 输出第一个到倒数第一个字符
print(string[0:-1])
print(string[0:2:1])
# 变量赋值
a, b, c = 3, "3", 98
print(type(a), type(b), type(c))
# true,false是int子类
print(1 is True, 1+True)

weight = 70.0
height = 1.75
bmi = weight / (height ** 2)
print('bmi:%.2f' % bmi)
print(f'bmi:{bmi:.4f}')
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")

# age: int = int(input("input your age:"))
# if age >= 18:
#     print("你成年了")
# elif age > 24:
#     print("工作了")
# else:
#     print("还未成年")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
ls = [1, 3, 4, 5, 6]
for n in ls:
    print(f"hello,{n}")
s = 0
lsA = range(101)
for item in lsA:
    s += item
print(s)

# list = [],py的list可以包含不同数据类型元素
fruit = ["apple", "orange", "banana", 555, 4.55]
fruit.append("taylor swift")
print(f"fruit:{fruit}")
# tuple = () ,元组，类似于Java的数组，元素类型可以不同，长度不可变
grade = (1, 3, 4, 5,)
# 单个元素的tuple必须后面跟逗号,
singleTuple = (1,)
print("single tuple:", singleTuple)
grades = (1, 3, 4, 5, ['小乌龟', 999])

# set =set([]),不重复的集合，与Java相同
sss = set([1, 2, 2, 3, 4, 4])
print("set:", sss)
sss.add(7)
sss.add("dddd")
sss.remove(4)
sss.add(grade)  # set中只允许不可变的对象
print(sss)

# dict={key:value} ,键-值对，类比Java Map
d = {"name": "jacky", "wealth": 9999999999999999999999999999}
print(d["name"], d["wealth"], d.get("age"))
if "age" in d:
    d.pop("age")
else:
    d.pop("name")
d["sex"] = 'man'
d['list'] = grades
print(d)


# 函数
# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：，可用于TODO，后续方便更改
# def nop():
#     pass 返回None
# def my_fun(num):
#     return abs(num)
# print(my_fun(-333))
# print(do_nothing())

# 练习：请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
# x=(-b±根号b^2-4ac)/2a
# 提示：计算平方根可以调用math.sqrt()函数：


def quadratic(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


# 默认参数, 定义默认参数要牢记一点：默认参数必须指向不变对象(基本数据类型，String)！
def add_end(l=[]):
    l.append('END')
    return l


print(add_end())
print(add_end())


# 可变参数，用*param表示,*num表示传入一个tuple
def sum(*num):
    ss = 0
    for nn in num:
        ss += nn
    return ss


print(sum(1, 3))
print(sum(1, 3, 344, 334))


# 关键字参数 **param，可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def fun(name, age=23, **kv):
    # kv会自动组装成dict
    print("name:", name, "age:", age, "kk:", kv)


fun('jack', city='杭州', sex="男")


# name: jack age: 12 kk: {'city': '杭州', 'sex': '男'}

# 命名关键字参数 (n1,n2,...,*,p1,p2...),*分割符后的参数即为命名关键字参数
def fun1(name, age, *, sex, tel):
    print(name, age, 'other:', sex, tel)


fun1('bob', 11, sex='man', tel=1254444)


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def funMixParam(a, b='ddd', *num, **kv):
    if 'city' in kv:
        print("用户设置了city")
        pass
    print('a=', a, 'b=', b, 'num=', num, 'kv=', kv)


numTuple = (11, 3, 33333, 4)
funMixParam('混合参数', '晚风中闪过', *numTuple, city='北京',
            apple=3, banana=5, orange=None)


def mul(x, *y):
    result = x
    for n in y:
        result = result * n
    return result


print(mul(2, 3, 5))

# 递归函数,尾递归优化（实际没用，仍然会溢出，尽量少用递归，使用循环等代替）
# def fact(n):
#     return recursive(n, 1)
#
#
# def recursive(m, product):
#     if m == 1:
#         return product
#     return recursive(m - 1, m * product)

# print(f'递归函数结果：{fact(100)}')

# range(n) ,包左不包右，
# slice 切片,a[start:stop:step]
list11 = list(range(200))
t = tuple(range(15))
print(f"slice:{list11[0:20:3]}")
print(f"copy:{list11[:]}")
# tuple切片，结果仍为tuple
print(f"tuple slice:{t[:4]}")
# [::-1]step=-1，表示倒序
print(f"tuple slice:{t[::-2]}")

# 练习：实现string的trim(),去除字符串首尾空格

sys.setrecursionlimit(10000)  # 设置递归最大限制深度


def trim(str):
    space = ' '
    if str:
        # 1.for实现
        # for s in str:
        #     # 去除前面空格
        #     if s == space:
        #         str = str[1:]
        #     else:
        #         break
        # for s in str[::-1]:
        #     # 将str逆序，去除后面空格
        #     if s == space:
        #         str = str[:-1]
        #     else:
        #         break
        # 2.while实现
        # while str[:1]==space:
        #     str=str[1:]
        # while str[-1:]==space:
        #     str=str[:-1]
        # 3.递归实现,递归容易翻车
        if str[:1] == ' ':
            str = str[1:]
            return trim(str)
        if str[-1:] == ' ':
            str = str[:-1]
            return trim(str)
    return str


print(trim('s' + ' ' * 1000))

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()

ddd = {"name": "jacky", "wealth": 9999999999999999999999999999,
       "age": 34, "sex": "man"}
for key, value in ddd.items():
    print(key, '---', value)

print(isinstance(112, Iterable))


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    small, large = L[0], L[0]
    for n in L:
        small = min(small, n)
        large = max(large, n)
    return small, large


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式[表达式]:在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
list1 = [x * x for x in range(9) if x % 2 == 0]
print(list1)

L2 = ['Hello', 'World', 18, 'Apple', None]
list2 = [x.lower() for x in L2 if isinstance(x, str)]
print(list2)
# 生成器generator （表达式）
g = (x for x in L2)
print(next(g))


# 斐波拉契数列,"yield"关键字就让函数变成 生成器
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib(max):
    a, b, n = 0, 1, 0
    while (n < max):
        # print('a:', a, '--b:', b)
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'


for n in fib(9):
    print('斐波拉契数列：', n)


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalName(name):
    firstChar = name[0].upper()
    otherChar = name[1:].lower()
    return firstChar + otherChar


def formName(ls):
    result = map(normalName, ls)
    print(list(result))


print(formName(["dakjdfkjgaEJEKJGKJGK", "jkdjkh"]))

# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(tt):
    return tt[0].upper()


def by_score(tt):
    return tt[1]


print("sorted by name:", sorted(L, key=by_name))
print("sorted by score:", sorted(L, key=by_score, reverse=True))

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：


def f(x): return x * x


print(f.__name__, f(3))


# 装饰器，函数内部函数
def log(text):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print('func execute time:', time.localtime())
            return func(*args, **kw)

        return wrapper

    return decor


@log("你好世界")
def now():
    print('2021-10-11 16:15:06')
    print('func name:', now.__name__)


now()


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def currTime(func):
    @functools.wraps(func)
    def wrapper(*args, **kv):
        print("time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return func(*args, **kv)

    return wrapper


@currTime
def nowTime():
    print("我执行了")


nowTime()

# functools.partial(f,param) 帮助创建偏函数:
# def int2(x, base=2):
#     return int(x, base)
int2 = functools.partial(int, base=16)

print(int2('85485245'))
