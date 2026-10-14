"""
@File : 6property_类属性用法.py
@Author : 王子墨
@Description : 
@Date :2026/8/29

property类属性的用法:
    类属性名 = property(获取值的函数名,设置值的函数名)

     之后，就可以直接 .上述的函数名 来当做变量直接用
"""

class Student:

    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

    age = property(get_age,set_age)

if __name__ == '__main__':

    s = Student()
    s.age = 19
    print(s.age)

