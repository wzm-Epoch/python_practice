"""
@File : 12深浅拷贝.py
@Author : 王子墨
@Description : 
@Date :2026/4/26
"""
"""
案例：深浅拷贝．

记忆(总结)：
1．所谓的深浅拷贝分别指的是：
    浅拷贝：copy模块的copy()
    深拷贝：copy模块的deepcopy()函数
2．大白话解释深浅拷贝：
    深拷贝拷贝的多，浅拷贝拷贝的少．
3．深浅拷贝主要是针对可变类型来讲的，深拷贝拷贝所有层(可变)，浅拷贝只拷贝第1层(可变)．
   如果是针对不可变类型,则用法和普通赋值一样
"""
import copy
def dm01_普通赋值():
    #普通赋值_不可变类型
    a = 10
    b = a
    print("id(a)->",id(a))     #0x01
    print("id(b)->",id(b))     #0x01
    print("id(10)->",id(10))   #0x01

    # 普通赋值_可变类型
    a = [1,2,3]
    b = [11,22,33]
    c = [a,b]
    d=c
    print("id(c)->", id(c))   #0x03
    print("id(d)->", id(d))   #0x03

def dm02_浅拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]

    d = copy.copy(c)
    print("id(c)->", id(c))   #0x03
    print("id(d)->", id(d))   #0x04
    print("id(c)和id(d)值不一样,说明浅拷贝第1层(最外面一层的数据)")

    print(id(c[2]))    #0x01
    print(id(a))       #0x01
    print("id(c[2)和id(a)值一样,说明浅拷贝第2层的数据")

    a[2] = 22
    print("c->",c)
    print("d->",d)

def dm03_浅拷贝不可变类型():
    a = (1,2,3)
    b = (11,22,33)
    c = (6,7,a,b)

    d = copy.copy(c)
    print("id(c)->",id(c))   #[6,7,[1,2,22],[11,22,33]]
    print("id(d)->",id(d))   #[6,7,[1,2,22],[11,22,33]]
    print("id(c)和id(d)值一样,说明c和d指向相同的内存空间")

def dm04_深拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6,7,a, b]

    print("id(c)->", id(c))
    print("id(d)->", id(d))
