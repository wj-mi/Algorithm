# -*- coding:utf-8 -*-

"""
插入排序之直接插入：
    每次从待排序列中取出一个，于已排好序列比较，找到待排数的正确位置，插入。

"""


import random


def right_insert(unorder):
    """unorder: 待排列表"""
    if not isinstance(unorder, list):
        print("Type error,need LIST !")
    length = len(unorder)
    if length <= 1:
        return unorder
    # insert_num = unorder[0]

    for index in range(1, length):
        insert_num = unorder[index]
        # flag = 0
        for j in range(index-1, -1, -1):
            if insert_num < unorder[j]:
                unorder[j + 1], unorder[j] = unorder[j], insert_num
        #     else:
        #         unorder[j+1] = insert_num
        #         flag = 1
        #         break
        # if not flag:
        #     unorder[j] = insert_num
    return unorder


def insert_sort(unorded):
    """unorder: 待排列表"""
    if not isinstance(unorded, list):
        print("Type error,need LIST !")
    length = len(unorded)
    if length <= 1:
        return
    for index in range(1, length):
        insert_num = unorded[index]
        for j in range(index, -1, -1):
            if insert_num < unorded[j - 1]:
                unorded[j] = unorded[j-1]
        unorded[j] = insert_num
    return unorded

"""
分析：
    1、生成了新的列表，占用空间
    2、用flag表示是否以插入，占用空间，不必要的变量
    3、流程冗余
    思路不清晰，分支没考虑好
"""

def main():
    for item in range(0, 5):
        print("----------"*4)
        unorder = [random.randrange(0, 99) for _ in range(0, 5)]
        print("before sort: {}".format(unorder))
        result = right_insert(unorder)
        print("After sort: {}".format(result))
        assert result == insert_sort(unorder)


if __name__ == '__main__':
    main()
