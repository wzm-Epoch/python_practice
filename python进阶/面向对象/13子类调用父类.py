"""
@File : 13子类调用父类.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
"""
1 父类名.父类函数名(self) 精准访问
2 super().父类函数名()   就近原则
"""
#第一种
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

class Prentice(Master,Sect):
    def __init__(self):
        self.kongfu = "枪术"

    def action(self):
        print(f"使用{self.kongfu}")

    def master_action(self):
        Master.__init__(self)
        Master.action(self)

    def sect_action(self):
        Sect.__init__(self)
        Sect.action(self)

if __name__ == "__main__":
    td = Prentice()
    td.action()
    print("-"*23)
    td.master_action()
    print("-" * 23)
    td.sect_action()
    print("*"*23)

#第二种
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

class Prentice(Sect,Master):
    def __init__(self):
        self.kongfu = "枪术"

    def action(self):
        print(f"使用{self.kongfu}")

    def master_action(self):
        super().__init__()
        super().action()

if __name__ == "__main__":
    td = Prentice()
    td.action()
    print("-"*23)
    td.master_action()
