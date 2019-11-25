#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:18:09 2019

@author: abdala
"""


class Encapsulation(object):
    def __init__(self, a, b, c):
        self.Apublic = a
        self._Bprotected = b
        self.__Cprivate = c

    def getprivate(self):
        return self.__Cprivate


x = Encapsulation(11, 13, 17)
print(x.Apublic)
print(x._Bprotected)
# print(x.__Cprivate)  # ->>>> Error
print(x.getprivate())


class A(object):
    def __init__(self):
        print('world')


class B(A):
    def __init__(self):
        print('hello')
        super().__init__()
        A.__init__(self)


b1 = B()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
