#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 包含一个学生类，一个sayhello，一个打印语句
class Student():
    def __init__(self,name="noname",age=18):
        self.name=name
        self.age=age
    def say(self):
        print("My name is {0}".format(self.name))
#记得空一行
def sayhello():
    print("Hi,hello!")

print("我是模块呀")
'''
三个平级的函数
这个文件里面的都是在一个模块里面


'''