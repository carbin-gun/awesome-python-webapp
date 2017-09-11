#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhengchao.deng'


def uncertain(**kwargs):
    print type(kwargs)
    cols, vals = zip(*kwargs.iteritems())
    print cols
    print vals


def greet_me(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.iteritems():
            print "%s == %s" % (k, v)


def greet_me2(**kwargs):
    if kwargs is not None:
        cols, vals = zip(*kwargs.iteritems())
        print cols
        print vals


def star_zip(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.iteritems():
            print "%s,%s" % (k, v)
        print "---------"
        names, values = zip(*kwargs.iteritems())
        print names
        print values


if __name__ == '__main__':
    a = (1, 2, 3)
    b = (4, 5, 6)
    zipped = zip(a, b)
    print zipped
    print "================="

    my_dict = {"name": "zhengchao.deng", "email": "cilendeng@gmail.com", "age": 28}
    uncertain(**my_dict)
    print "-------------"
    greet_me(name="zhengchao.deng", age=28)
    print "-------------"
    greet_me(**{"name": "zhengchao.dneg", "age": 28, "gender": "male"})
    print "-------------"
    greet_me2(**{"name": "zhengchao.dneg", "age": 28, "gender": "male"})
    print "============="
    star_zip(**{"name": "zhengchao.dneg", "age": 28, "gender": "male"})
