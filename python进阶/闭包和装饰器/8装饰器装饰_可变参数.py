"""
@File : 8装饰器装饰_可变参数.py
@Author : 王子墨
@Description : 
@Date :2026/4/26
"""
"""
案例：装饰器装饰_可变参数
细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致，
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的。
    原函数有参有返回的，则 装饰器的内部函数也必须是 有参有返回的。
"""

#需求:定义1个可以计算多个数据和字典value值和的函数,并给友好提示
#1.定义装饰器
def my_decorator(fu_name):
    def fn_inner(*args, **kwargs):
        print("正在努力计算中...")
        return fu_name(*args, **dict(kwargs))
    return fn_inner

#2.定义原函数
@my_decorator
def get_sum(*args,**kwargs):
    """
    该函数用于计算 数字元组 和 字典value值 之和
    :param args: 数字元组 *args -> 接受所有的位置参数,封装到 元组
    :param kwargs: 字典,键是字符串,值是数字 **kwargs -> 接受所有的关键字参数,封装到 字典
    :return: 结果之和
    """
    #2.1定义求和变量
    sum = 0
    #2.2遍历元组,求和
    for i in args:
        sum += i
    #2.3遍历字典,求和
    for v in kwargs.values():
        sum += v
    #2.4返回结果
    return sum

    #return sum(args) + sum(kwargs.values())

#3.测试
sum = get_sum(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)
print(sum)

# sum2 = sum((1,2,3,5))
# print(sum2)
#
# my_dict = {"a":1,"b":2,"c":3,"d":4}
# sum3 = sum(my_dict.values())
# print(sum3)