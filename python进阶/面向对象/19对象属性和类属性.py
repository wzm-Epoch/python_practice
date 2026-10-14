"""
@File : 19对象属性和类属性.py
@Author : 王子墨
@Description : 
@Date :2026/4/23
"""
"""
对象属性 属于每个对象的,每个对象的属性值可能都不同,修改A对象的属性,不影响对象B
类属性   属于类的,能被该类下所有的对象共享,A对象修改类属性,B对象访问的时修改后的

对象属性
    定义到 init 魔法方法中的属性,每个对象都有自己的内容
    只能通过 对象名. 的方式调用
    
类属性
    定义到类中,函数外的属性(变量),能被该类下所有的对象所共享
    既能通过 类名. 还能通过 对象名. 的方式来调用,推荐使用 类名. 的方式    
"""

class Student:

    #类属性
    teacher_name = "陈旭昌"

    def __init__(self,name,age):
        #对象属性
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名:{self.name} ,年龄:{self.age}'

if __name__ == '__main__':

    c1 = Student("小明",18)
    c2 = Student("小美",18)

    print(c1)
    print("-"*23)
    print(c2)
    print("*"*23)

    print(c1.teacher_name)
    print("-"*23)
    print(c2.teacher_name)
    print("-"*23)
    print(Student.teacher_name)
    print("*"*23)

    c1.teacher_name = "袁飞龙"
    print(c1.teacher_name)
    print("-" * 23)
    print(c2.teacher_name)
    print("-" * 23)
    print(Student.teacher_name)
    print("*" * 23)

    Student.teacher_name = "袁飞龙"
    print(c1.teacher_name)
    print("-" * 23)
    print(c2.teacher_name)
    print("-" * 23)
    print(Student.teacher_name)
    print("*" * 23)




