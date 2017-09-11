#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhengchao.deng'


class File(object):
    def __init__(self, file, method):
        self._file = open(file, method)

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


if __name__ == '__main__':
    with File("demo.file.txt", 'r') as demo_file:
        print demo_file.readxxx()
