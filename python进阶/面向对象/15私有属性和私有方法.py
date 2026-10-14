"""
@File : 15私有属性和私有方法.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
"""
私有属性  __属性名
私有方法  __方法名():
        ...
只能在类的内部使用,不能在类的外部使用
如果想在类的外部使用公共接口        
"""
class Master:
    def __init__(self):
        self.kongfu = "剑术"
        self.__money = 90000

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def __action(self):
        print(f"使用{self.kongfu}")

    def action(self):
        self.__action()



class Prentice(Master):
    pass


if __name__ == "__main__":
    td = Prentice()
    print(td.get_money())
    td.set_money(-100000)
    print("-"*23)
    print(td.get_money())
    print("-"*23)
    td.action()