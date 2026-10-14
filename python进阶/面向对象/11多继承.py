"""
@File : 11多继承.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
class Master:
    def __init__(self):
        self.kongfu = "剑术"

    def action(self):
        print(f"使用{self.kongfu}")

class Sect:
    def __init__(self):
        self.kongfu = "刀术"

    def action(self):
        print(f"使用{self.kongfu}")

#就近原则
class Prentice(Master, Sect):
    pass

if __name__ == "__main__":
    
    
    td = Prentice()
    td.action()


#可以使用 类名.__mro__属性 或 类名.mro() 方法查看调用的先后顺序
    print(Prentice.mro())
    print(Prentice.__mro__)