"""
@File : 8案例 烤地瓜.py
@Author : 王子墨
@Description : 
@Date :2026/4/21
"""
class SweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_state = "生的"
        self.condiments = []
    #烘烤动作
    def cook(self,time):
        #根据烘烤时间,修改地瓜的烘烤状态
        if time<0:
            print("无效值")
        else:
            self.cook_time = time
            if 0<=time<3:
                self.cook_state = "生的"
            elif 3<=time<7:
                self.cook_state = "半生不熟"
            elif 7<=time<12:
                self.state = "熟了"
            else:
                self.state = "糊了"
    #添加调料
    def add_condiments(self,condiment):
        self.condiments.append(condiment)
    #重写srt()方法，打印地瓜状态
    def __str__(self):
        return f"烘烤时间:{self.cook_time},地瓜状态:{self.cook_state},调料:{self.condiments}"

#测试
if __name__ == "__main__":
    dg = SweetPotato()
    dg.cook(-3)
    dg.cook(5)
    dg.add_condiments("盐")
    print(dg)