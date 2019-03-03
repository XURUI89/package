#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 包含一个学生类，一个sayhello，一个打印语句
class Student():
    def __init__(self,name="noname",age=18):
        self.name=name
        self.age=age

    def say(self):
        print("My name is {0}".format(self.name))
    if __name__ == '__main__':
        print("我是模块呀")
#记得空一行
def sayhello():
    print("Hi,hello!")
'''
if __name__ == '__main__'的意思是：
当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行

'''

