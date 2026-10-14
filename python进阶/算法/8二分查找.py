"""
@File : 8二分查找.py
@Author : 王子墨
@Description : 
@Date :2026/9/22
"""


def binary_search(list,target):

    start = 0
    end = len(list) - 1

    while start <= end:

        mid = (start+end) // 2

        if target == list[mid]:
            return True
        elif target < list[mid]:
            end = mid - 1
        else :
            start = mid + 1

    return False

if __name__ == '__main__':

    list = [1,2,3,4,5,6,7,8,9]
    print(binary_search(list,6))
    print(binary_search(list,0))