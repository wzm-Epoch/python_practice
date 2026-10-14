"""
@File : 14多层继承.py
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


# 就近原则
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

class Tuson(Prentice):
    def __init__(self):
        self.kongfu = "武术"

    def action(self):
        print(f"使用{self.kongfu}")

    def prentice_action(self):
        Prentice.__init__(self)
        Prentice.action(self)



if __name__ == "__main__":
    ts = Tuson()
    ts.action()
    print("-"*23)
    ts.prentice_action()
    print("-"*23)
    ts.master_action()
    print("-"*23)
    ts.sect_action()
