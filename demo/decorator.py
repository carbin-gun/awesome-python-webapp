#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

__author__ = 'zhengchao.deng'


def new_decorator(func):
    # 如果没有functools里wraps,那么被装饰器返回后的函数的__name__就是wrap_func,要想还是返回外部传进来的(被装饰器修饰的函数名),就可以用 @wraps.
    @wraps(func)
    def wrap_func():
        print("I am doing some boring work before executing a_func()")
        func()
        print("I am doing some boring work after executing a_func()")

    return wrap_func


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
print "================"
wrap_func = new_decorator(a_function_requiring_decoration)
wrap_func()
print "================"


@new_decorator
def my_func():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


my_func()
print "================"
wrap_my_func = new_decorator(new_decorator(my_func)) #my_func上本身就有一个new_decorator 所以这个会有三次before 三次after.
wrap_my_func()

print 'my_func.__name__ =%s' % my_func.__name__
