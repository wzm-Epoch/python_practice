"""
@File : 9继承人入门.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
class Father:
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("散步")

class Son(Father):
    pass

if __name__ == '__main__':
    son = Son()
    print(son.gender)
    son.walk()