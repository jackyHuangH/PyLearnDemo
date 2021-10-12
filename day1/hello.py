#!/usr/bin/env python3

'a hello module'
__author__ = 'Jacky Huang'

import sys

# 面向对象
import types


class Human(object):
    # 类似于构造函数，注意：特殊方法“__init__”前后分别有两个下划线！！！
    # 在Python中，实例的变量名如果以__开头(注意是2个下划线_)，就变成了一个私有变量__xx（private），只有内部可以访问，外部不能访问
    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
    # 所以，不能用__name__、__score__这样的变量名作为私有变量
    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
    # 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
    def __init__(self, name):
        self.__name = name

    def say_hi(self):
        print('hi,my name is:', self.__name)


def test():
    args = sys.argv
    print(args, '__name__:', __name__)
    human1 = Human("张三")
    human2 = Human('李四')
    # 新增了类原来没有的属性
    human1.sex = 555
    print(human1.sex)
    human1.say_hi()
    human2.say_hi()
    print(isinstance(human1, Human))
    print(type(human1))
    print(type(test) == types.FunctionType)


if __name__ == '__main__':
    test()
