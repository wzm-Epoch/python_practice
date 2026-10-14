"""
@File : 1递归入门.py
@Author : 王子墨
@Description : 
@Date :2026/9/7

案例：演示递归入门。

递归介绍：
    概述：
        方法自己调用自己的情况就叫递归。
    经典案例：
        1.求阶乘
        2.不死神兔，斐波那契数列。
        3.文件夹拷贝，删除等...
        4.服务器文件整理。

    核心要点：
        1. 递归必须要有出口，否则容易造成死递归。
        2. 递归调用次数不能过多，否则容易造成死递归。
        3. 递归必须有规律。

    要搞定递归，掌握两点：
        1. 分析出口。
        2. 找规律。

    案例：求阶乘
    公式: n! = n * (n - 1)!
    大白话: 5! = 5 * 4 * 3 * 2 * 1 = 120
    出口: 1! = 1

    分析流程:
        5! = 5 * 4!
            4! = 4 * 3!           --规律--
                3! = 3 * 2!
                    2! = 2 * 1!
                        1! = 1     --出口--

"""

#递归入门
# count = 0
#
# def show():
#     global count
#     if count >= 100:
#         return
#     count = count + 1
#     print(f"我是show函数，第{count}次")
#     show()
#
# if __name__ == '__main__':
#     show()

#求阶乘
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))