"""
@File : 2 nonlocal关键字.py
@Author : 王子墨
@Description : 
@Date :2026/4/25
"""
"""
global:声明全局变量
nonlocal:声明能够让内部函数去修改外部函数的变量
"""

#1.定义外部函数
def fn_outer():
    #2.定义外部函数的(局部)变量
    a = 100

    #3.定义内部函数,访问外部函数的变量
    def fn_inner():
        #4.在内部函数中修改外部函数的变量
        nonlocal a
        a = a + 1
        #5.打印外部函数的变量
        print(f"a:{a}")

    #6.返回 内部函数名(对象)
    return fn_inner

#7.测试
if __name__ == "__main__":
    fn_inner = fn_outer()
    fn_inner()
    fn_inner()
    fn_inner()