"""
@File : 21扩展dict属性.py
@Author : 王子墨
@Description : 
@Date :2026/4/23

__dict__属性介绍:
    它是python内置的属性,可以把对象转成字典形式
"""

from 学生信息管理系统.student import Student

#需求1: 把 学生对象 -> 字典形式,属性名做键,属性值做值
s1 = Student("王子墨","男",18,13919541007,"喜欢敲代码")
print(s1)

#{'name': '王子墨', 'gender': '男', 'age': 18, 'phone': 13919541007, 'desc': '喜欢敲代码'}
my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))
print("-"*23)

#需求2: 把 [学生对象,学生对象,学生对象] -> [字典,字典,字典]
s1 = Student("王子墨","男",18,13919541007,"喜欢敲代码")
s2 = Student("张雲斌","男",18,13319541007,"喜欢敲代码")
s3 = Student("肖浩洋","男",18,15619541007,"喜欢敲代码")
stu_list = [s1,s2,s3]

#列表推导式
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)
print("-"*23)

#需求3: 把{'name': '王子墨', 'gender': '男', 'age': 18, 'phone': 13919541007, 'desc': '喜欢敲代码'} -> 学生对象
my_dict = {'name': '王子墨', 'gender': '男', 'age': 18, 'phone': 13919541007, 'desc': '喜欢敲代码'}
s5 = Student(my_dict['name'],my_dict['gender'],my_dict['age'],my_dict['phone'],my_dict['desc'])
print(s5)
print("-"*23)
#效果同上
s6 = Student(**my_dict)
print(s6)