"""
@File : 3装饰器入门.py
@Author : 王子墨
@Description : 
@Date :2026/4/25
"""
"""
案例：装饰器入门。

装饰器介绍：
概述/作用：
    它的本质是一个闭包函数，目的是 在不改变原有函数结构的基础上，对其功能做增强。
    大白话：装修队 在不改变房屋结构的情况下，对房屋做装修(功能增强)

前提条件：
    1. 有嵌套。
    2. 有引用。
    3. 有返回。
    4. 有额外功能。

装饰器的用法：
格式1：传统写法。
    装饰后的函数名 = 装饰器名(被装饰的原函数名)
    装饰后的函数名()

格式2：语法糖。
    在要被装饰的原函数上，直接写 @装饰器名，之后直接调用原函数即可。
"""

#需求:在发表评论前,都是需要先登录的

#1.定义外部函数,形参列表接收 要被装饰的函数名(对象)
def check_login(fn_name):
    #1.1定义内部函数
    def fn_inner():
        #1.2额外功能
        print("校验登录... 登录成功!")
        #1.3访问原函数, 即:外部函数的引用
        fn_name()
    #1.4返回内部函数对象
    return fn_inner

#2.定义函数,表示发表评论
@check_login #comment = check_login(comment)
def comment():
    print("发表评论")

@check_login
def payment():
    print("充值中...")

#3.测试
if __name__ == '__main__':
    #3.1传统方式
    # comment = check_login(comment)
    # comment()
    # print("-"*23)
    # payment = check_login(payment)
    # payment()
    # print("-"*23)

    #3.2语法糖
    comment()