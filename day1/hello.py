#!/usr/bin/env python3

'a hello module'
__author__ = 'Jacky Huang'

import sys

# 面向对象
import types


class Human(object):
    # 实例属性属于各个实例所有，互不干扰；
    # 类属性属于类所有，所有实例共享一个属性；
    # 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
    # 类属性
    count = 0

    # 类似于构造函数，注意：特殊方法“__init__”前后分别有两个下划线！！！
    # 在Python中，实例的变量名如果以__开头(注意是2个下划线_)，就变成了一个私有变量__xx（private），只有内部可以访问，外部不能访问
    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
    # 所以，不能用__name__、__score__这样的变量名作为私有变量
    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
    # 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
    def __init__(self, name):
        self.__name = name
        Human.count += 1

    def get_name(self):
        return self.__name

    def say_hi(self):
        print('hi,my name is:', self.__name)


class Man(Human):
    # 使用__slots__插槽定义类属性，不在slots定义内的不允许,__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('sex', 'height')


# @property 装饰器就是负责把一个方法变成属性调用
class Screen(object):
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # resolution未设置setter,只读
    @property
    def resolution(self):
        return self.__width * self.__height


def sleep(name):
    print(name, "is sleeping....")


def test():
    args = sys.argv
    print(args, '__name__:', __name__)
    human1 = Human("张三")
    human2 = Human('李四')
    human3 = Human('王五')
    # 给实例新增属性， 新增了类原来没有的属性
    human1.sex = 555
    # print(human1.sex)
    human1.say_hi()
    human2.say_hi()
    # print(isinstance(human1, Human))
    # print(type(human1))
    print(isinstance(test, types.FunctionType))
    # 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    print(dir('ABC'))
    setattr(human1, 'age', 45)
    print(hasattr(human1, 'age'))
    print(getattr(human1, 'age'))
    print('human count:', Human.count)
    man1 = Man("1号")
    man1.sex = 1
    man1.height = 180
    man1.e = 90
    s = Screen()
    s.height = 768
    s.width = 1024
    print('resolution:', s.resolution)


if __name__ == '__main__':
    test()
