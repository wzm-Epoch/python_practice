"""
@File : 10一个装饰器装饰多个函数.py
@Author : 王子墨
@Description : 
@Date :2026/4/26
"""
"""
案例：演示 带参数的装饰器.
记忆：
    1.个装饰器的参数有且只能有 1 个.
    2.如果装饰器有多个参数，可以在该装饰器的外边再包裹一层，把该装饰器当作其 内部函数 返回即可.
"""

#需求：定义1个既能装饰减法，又能装饰加法的装饰器 → 即：带有参数的装饰器.

def logging(flag):
    def my_decorator(fn_name):
        def fn_inner(a,b):
            if flag == "+":
                print("正在努力计算 加法 中...")
            elif flag == "-":
                print("正在努力计算 减法 中...")
            return fn_name(a,b)
        return fn_inner
    return my_decorator

@logging("+")
def get_sum(a,b):
    return a + b

@logging("-")
def get_sub(a,b):
    return a - b

print(get_sum(78,13))
print("-"*23)
print(get_sub(92,1))