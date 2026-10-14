"""
@File : 5插入排序.py
@Author : 王子墨
@Description : 
@Date :2026/9/14

 5.插入排序
插入排序（Insertion Sort）：将未排序区中的一个元素，插入到已排序区中适当的位置，从而得到一个新的、个数加一的有序数据。适用于少量数据的排序。

它将数组分成两部分：
- 有序区：默认第一个元素为有序区
- 无序区：除第一个元素外，其余元素为无序区

基本思想：每一轮从无序区取出一个元素，插入到有序区的合适的位置，直到无序区为空。

## 代码实现
以5个元素为例，每轮的比较次数如下：

|第几轮（索引i）   |该轮比较的总次数   |比较对象|
|第1轮（1）             |1次       |索引1与0|
|第2轮（2）             |2次|     索引2与1、0|
|第3轮（3）             |3次|    索引3与2、1、0|
|第4轮（4）             |4次|    索引4与3、2、1、0|

要点：
1. 比较的总轮数 = 列表长度 -1（range(1, n)）
2. 每轮比较的总次数 = range(i, 0, -1)（从 i 向前比较到索引1）
3. 谁和谁比较：索引 j 和 j‑1 位置的元素


# def insert_sort(list):
#
#     n = len(list)
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if list[j] < list[j-1]:
#                 list[j], list[j-1] = list[j-1], list[j]
#             else:
#                 break
#
# if __name__ == '__main__':
#
#     list = [5,3,4,7,2]
#     insert_sort(list)
#     print(list)
"""
def insert_sort(my_list: list):
    # 获取列表长度
    length = len(my_list)

    # 外循环：控制比较的轮数
    for i in range(1, length):
        # 内循环：控制每次比较的总次数
        for j in range(i, 0, -1):
            # 如果 j < j - 1 的元素，就交换
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            else:
                break

    return my_list


if __name__ == '__main__':
    my_list = [5, 3, 4, 7, 2]
    print(insert_sort(my_list))