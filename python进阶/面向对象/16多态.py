"""
@File : 16多态.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
"""
同样一个函数在不同的场景下有不同的状态
1 有继承
2 函数重写
3 父类引用指向子类对象
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

#父类引用指向子类对象 an:Animal = Dog()
def speak(animal:Animal):
        animal.speak()

if __name__ == "__main__":

    dog = Dog()
    cat = Cat()

    speak(dog)
    print("-"*23)
    speak(cat)