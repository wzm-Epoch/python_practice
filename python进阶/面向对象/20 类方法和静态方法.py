"""
@File : 20 类方法和静态方法.py
@Author : 王子墨
@Description : 
@Date :2026/4/23
"""
"""
案例：演示类方法和静态方法.

类方法：
    属于类的方法，可以通过 类名. 还可以通过 对象名. 的方式来调用.
    定义类方法的时候，必须使用装饰器 @classmethod, 且第1个参数必须表示 类对象.

静态方法：
    属于该类下所有对象所共享的方法，可以通过 类名. 还可以通过 对象名. 的方式来调用.
    定义静态方法的时候，必须使用装饰器 @staticmethod, 且参数传不传都可以.

区别:
    1. 类方法的第1个参数必须是 类对象, 静态方法无参数的特殊要求
    2. 你可以理解为: 如果函数中要用 类对象, 就定义成类方法, 否则定义成 静态方法, 除此外, 并无任何区别.
    
    
"""

class Student(object):

    school = "北京大学"

    @classmethod
    def show1(cls):
        print(f"cls:{cls}")
        print(cls.school)
        print("我是类方法")

    @staticmethod
    def show2():
        print(Student.school)
        print("我是静态方法")

if __name__ == '__main__':

    s1 = Student()
    s1.show1()
    print("-"*23)
    s1.show2()
    print("-"*23)
    print(Student.show1())
    print("-"*23)

"""
我们来系统梳理一下 Python 中类方法和静态方法的概念、区别和用法，结合你截图里的知识点做补充和拓展。
 
一、先搞懂：实例方法、类方法、静态方法
 
Python 中类里的方法有三种，我们先对比一下，方便你建立整体认知：
 
方法类型 装饰器 第一个参数 访问权限 主要用途 
实例方法 无 self（实例对象） 能访问实例属性、类属性 操作/修改实例的状态 
类方法 @classmethod cls（类对象） 能访问类属性，不能直接访问实例属性 操作/修改类的状态、作为工厂方法 
静态方法 @staticmethod 无强制要求 不能直接访问类/实例属性 与类相关但不依赖类/实例状态的工具函数 
 
 
二、类方法（@classmethod）
 
1. 核心定义
 
- 用 @classmethod装饰器标记。
- 第一个参数必须是 cls（约定俗成，代表当前类对象本身）。
- 可以通过 类名直接调用，也可以通过 实例对象调用。
 
2. 基础示例
 
python
  
class Tool:
    count = 0  # 类属性

    def __init__(self):
        Tool.count += 1

    # 类方法：查看创建了多少个实例
    @classmethod
    def show_count(cls):
        print(f"已创建的实例数量：{cls.count}")

# 调用方式1：类名调用
Tool.show_count()  # 输出：已创建的实例数量：0

# 创建实例
t1 = Tool()
t2 = Tool()

# 调用方式2：实例调用（本质还是访问类的信息）
t1.show_count()  # 输出：已创建的实例数量：2
 
3. 典型用途
 
1.操作/修改类属性：比如统计实例数量、修改类的全局配置。
2.工厂方法：定义多种方式创建实例的方法，替代复杂的 __init__。
python
  
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 工厂方法：从字符串解析日期
    @classmethod
    def from_str(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

# 用工厂方法创建实例
d = Date.from_str("2025-10-01")
print(d.year, d.month, d.day)  # 输出：2025 10 1
 
三、静态方法（@staticmethod）
 
1. 核心定义
 
- 用 @staticmethod 装饰器标记。
- 没有强制要求的第一个参数（既没有 self，也没有 cls）。
- 可以通过 类名直接调用，也可以通过 实例对象调用。
- 本质上就是一个和类绑定的普通函数，不依赖类或实例的状态。
 
2. 基础示例
 
python
  
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# 调用方式1：类名调用
print(MathUtil.add(3, 5))       # 输出：8
print(MathUtil.is_even(4))       # 输出：True

# 调用方式2：实例调用
mu = MathUtil()
print(mu.add(10, 20))            # 输出：30
 
3. 典型用途
 
1.工具函数：和类的业务相关，但不需要访问类或实例的任何属性。
2.逻辑分组：把相关的工具函数放在类里，方便管理和调用，而不是散落成独立函数。
 
四、关键区别（结合你截图里的知识点）
 
1.参数要求不同
- 类方法：第一个参数必须是 cls（代表类本身），可以在方法内访问/修改类属性。
- 静态方法：没有强制参数，不能直接访问类或实例的属性，只能通过参数传入。
2.访问权限不同
- 类方法：只能直接访问类属性，不能直接访问实例属性（除非实例作为参数传入）。
- 静态方法：不能直接访问类属性或实例属性，只能通过类名/实例名显式访问。
3.使用场景不同
- 类方法：当你需要和类本身打交道（比如修改类属性、创建实例的工厂方法）时用它。
- 静态方法：当你需要一个和类相关但不依赖类/实例状态的工具函数时用它。
 
五、补充：什么时候用哪个？
 
场景 推荐方法 
需要修改/访问类属性 类方法 
需要创建不同方式的实例（工厂方法） 类方法 
工具函数，逻辑和类相关但不依赖类/实例状态 静态方法 
操作/修改实例自身的状态 实例方法（默认） 

"""