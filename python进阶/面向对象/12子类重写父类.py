"""
@File : 12子类重写父类.py
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

class Prentice(Master):
    def __init__(self):
        self.kongfu = "枪术"

    def action(self):
        print(f"使用{self.kongfu}")
        
if __name__ == "__main__":
    td = Prentice()
    print(td.kongfu)
    td.action()