"""
@File : 2生成器_推导式写法.py
@Author : 王子墨
@Description : 
@Date :2026/8/29
案例：演示生成器之 推导式写法。

生成器介绍：
    概述：
        所谓的生成器就是基于 数据规则，用一部分在生成一部分，而不是一下子生成完所有。
    目的：
        可以节省大量的内存。
    实现方式：
        1．推导式写法。
        2．yield关键字
"""
import sys

my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print("*"*23)

my_generator2 = (i for i in range(1,11) if i%2==0)
print(my_generator2)
print(type(my_generator2))

#从生成器中获取对象
#1.next()
print(next(my_generator2))
print(next(my_generator2))
print(next(my_generator2))
print("*"*23)
for i in my_generator2:
    print(i)

my_list = [i for i in range(10000000)]
my_gt = (i for i in range(10000000))
print(type(my_list))
print(type(my_gt))

print(f'my_list的内存占用:{sys.getsizeof(my_list)}')
print(f'my_gt的内存占用:{sys.getsizeof(my_gt)}')
