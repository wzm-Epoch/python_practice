"""
@File : 18抽象类(接口)案例 空调.py
@Author : 王子墨
@Description : 
@Date :2026/4/23
"""
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷技术")

    def hot_wind(self):
        print("美的空调核心制热技术")

    def swing_l_r(self):
        print("美的空调无风感左右摆风")


class XiaoMi_AC(AC):
    def cool_wind(self):
        print("小米空调核心制冷技术")

    def hot_wind(self):
        print("小米空调核心制热技术")

    def swing_l_r(self):
        print("小米空调无风感左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

if __name__ == '__main__':

    ac1 = Midea_AC()
    ac2 = XiaoMi_AC()

    make_cool(ac1)
    print("-"*23)
    make_cool(ac2)