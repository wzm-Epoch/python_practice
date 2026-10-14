
"""
@File : 5property_装饰器用法.py
@Author : 王子墨
@Description :
@Date :2026/8/29
案例：演示property属性的用法。

property属性介绍：
概述/目的/作用：
    把 函数 当做 变量来使用。
实现方式：
    方式1：装饰器。
    方式2：类属性。

property的装饰器用法：
@property                修饰 获取值的函数
@获取值的函数名.setter   修饰 设置值的函数

之后，就可以直接 .上述的函数名 来当做变量直接使用。
"""
#需求：定义学生类，私有属性 age，通过property实现简化调用。

class Student:

    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

if __name__ == '__main__':

    s = Student()
    #设置值
    s.age = 19
    #获取值
    print(s.age)