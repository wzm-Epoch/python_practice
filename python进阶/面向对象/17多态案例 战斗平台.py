"""
@File : 17多态案例 战斗平台.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
class HeroFighter:
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 90

class EnemyFighter:
    def power(self):
        return 70

def object_play(hero,enemy):
    if hero.power() >= enemy.power():
        print("英雄机 战胜 敌机")
    else:
        print("英雄机 惜败 敌机")

if __name__ == "__main__":
    # 思路一 不使用多态
    h1 = HeroFighter()
    e1 = EnemyFighter()
    if h1.power() >= e1.power():
        print("英雄机1代 战胜 敌机1代")
    else :
        print("英雄机1代 惜败 敌机1代")

    print("-"*23)

    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    if h2.power() >= e1.power():
        print("英雄机2代 战胜 敌机1代")
    else :
        print("英雄机2代 惜败 敌机1代")

    print("*"*23)

    #思路二 使用多态


    object_play(h1,e1)
    print("-"*23)
    object_play(h2,e1)

