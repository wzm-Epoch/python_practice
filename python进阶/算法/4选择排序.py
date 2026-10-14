"""
@File : 4选择排序.py
@Author : 王子墨
@Description : 
@Date :2026/9/14
案例：演示选择排序。

选择排序介绍：
原理：
每轮都假设该轮最前边的那个元素为最小值，然后去剩下的元素列表中找真正的最小值，最终交换即可，本轮就找到了 本轮的最小值，重复即可。

流程：假设共 5 个元素
第几轮(索引)	每轮比较的总次数	    公式
第1轮(0)：	    4次	        5 - 1 - 0 = 4
第2轮(1)：	    3次	        5 - 1 - 1 = 3
第3轮(2)：	    2次	        5 - 1 - 2 = 2
第4轮(3)：	    1次	        5 - 1 - 3 = 1

要点：

1.比较的总轮数.	列表长度 - 1
2.每轮比较的总次数.	列表长度 - 1 - 轮数的索引(从0开始)
3.谁和谁比较.	索引 j 和 j + 1位置的元素比较

时间复杂度：
最优：O(n)
最坏：O(n²)

扩展：
选择排序 = 稳定 排序算法

扩展：
外层循环的 -1 是什么意思：减少比较的轮数，提高效率。
内循环的 -1 是什么意思：为了防止索引 越界。
内循环的 -i 是什么意思：减少每轮比较的次数，提高效率。

待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位
"""

list = [7,3,5,2,6]

def select_sort(list):

    n = len(list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if list[min_index] > list[j]:
                min_index,j = j,min_index
        if min_index != i:
            list[i],list[min_index] = list[min_index],list[i]

if __name__ == '__main__':
    select_sort(list)
    print(list)
