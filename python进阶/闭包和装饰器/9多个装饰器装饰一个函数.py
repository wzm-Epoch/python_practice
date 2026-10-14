"""
@File : 9多个装饰器装饰一个函数.py
@Author : 王子墨
@Description : 
@Date :2026/4/26
"""
"""
案例：演示多个装饰器装饰1个函数.
记忆：
    多个装饰器装饰1个原函数，是按照 由内向外的顺序来装饰的。
    但如果你是用 装饰器的写法来做，看到的效果是：从上往下执行的。
"""
# 需求：发表评论前，需要先登录，在验证验证码，请用所学，模拟该功能。(装饰器)

def check_login(fn_name):
    def fn_inner():
        print("校验登录!")
        fn_name()
    return fn_inner

def check_code(fn_name):
    def fn_inner():
        print("校验验证码!")
        fn_name()
    return fn_inner

@check_login
@check_code
def comment():
    print("发表评论")

#comment = check_code(comment)
#comment = check_login(comment)
comment()