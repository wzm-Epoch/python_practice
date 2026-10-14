"""
@File : 3生成器_yield方式.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
"""

def my_func():

    # my_list = []
    # for i in range(1,11):
    #     my_list.append(i)
    # return my_list
    #yield在这里做了三件事：1.创建生成器对象 2.把值存储到生成器中 3.返回生成器
    for i in range(1,11):
        yield i

my_g = my_func()
print(type(my_g))

print(next(my_g))
print(next(my_g))
print("*"*3)
for i in my_g:
    print(i)