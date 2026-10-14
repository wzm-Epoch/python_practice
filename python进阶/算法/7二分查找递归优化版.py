"""
@File : 7二分查找优化版.py
@Author : 王子墨
@Description : 
@Date :2026/9/22
"""
def binary_search_recursion(nums, target, left=0, right=None):
    """返回元素从 1 开始的位置；找不到时返回 False。"""
    if right is None:
        right = len(nums) - 1

    if left > right:
        return False

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid + 1
    elif target < nums[mid]:
        return binary_search_recursion(nums, target, left, mid - 1)
    else:
        return binary_search_recursion(nums, target, mid + 1, right)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    t1, t2, t3 = 4, 2, 7

    l1 = binary_search_recursion(nums, t1)
    l2 = binary_search_recursion(nums, t2)
    l3 = binary_search_recursion(nums, t3)

    print(f"{t1}在第{l1}个位置，"
          f"{t2}在第{l2}个位置，"
          f"{t3}在第{l3}个位置")