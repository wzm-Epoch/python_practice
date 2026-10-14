"""
@File : 1闭包入门.py
@Author : 王子墨
@Description : 
@Date :2026/4/25
"""
"""
闭包解释
概述:
    内部函数 使用了外部函数的变量, 这种写法就称之为闭包.
格式:
def 外部函数名(形参列表):
    外部函数的(局部)变量

    def 内部函数名(形参列表):
        使用外部函数的变量

    return 内部函数名
前提条件:
    1. 有嵌套.      外部函数嵌套内部函数
    2. 有引用.      内部函数使用外部函数的变量
    3. 有返回.      外部函数中, 返回 内部函数名(对象)

细节:
    1. 函数名 和 函数名() 是两个概念, 前者表示 函数对象, 后者表示 调用函数, 获取返回值.
"""
# 案例1: 函数名 → 是对象

def get_sum(a, b):
    return a + b

print(get_sum)
print(get_sum(1,2))

my_sum = get_sum
print(my_sum)
print(my_sum(10,20))
print("-"*23)

#案例2:演示闭包写法
def fn_outer(num1):
    def fn_inner(num2):
        sum = num1 + num2
        print(f"求和结果:{sum}")
    return fn_inner

fn_inner = fn_outer(10)
fn_inner(20)
print("-"*23)

fn_outer(10)(20)