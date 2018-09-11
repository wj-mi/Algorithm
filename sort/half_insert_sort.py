# -*- coding:utf-8 -*-

"""二分折半插入排序：
    每次选出一个数，插入有序队列中。

"""
import random


def half_sort(origin):
    """origin : 原始未排序序列"""
    length = len(origin)
    if length <= 1:
        return origin
    for index in range(1, length):
        num = origin[index]
        origin[:index+1] = inner_insert(origin[:index], num)
    return origin


def inner_insert(origin, num):
    """origin  为有序序列，将num插入"""
    # index 为折半序列
    length = len(origin)
    index = length / 2
    if num < origin[index]:
        if index > 0:
            # origin[: index+1] = inner_insert(origin[: index], num)
            left = inner_insert(origin[: index], num)
            origin = left + origin[index:]
        else:
            origin.insert(index, num)
    elif num > origin[index]:
        if index == length - 1:   # index 为最大值，即没有序列了
            origin.insert(index+1, num)
        else:
            origin = origin[:index+1] + inner_insert(origin[index+1:], num)
    else:  # eq
        origin.insert(index, num)
    return origin




def main():
    for item in range(0, 5):
        print("----------"*4)
        # unorder = [76, 31, 88, 94, 53]
        unorder = [random.randrange(0, 99) for _ in range(0, 5)]
        print("before sort: {}".format(unorder))
        result = half_sort(unorder)
        print("After sort: {}".format(result))
        # assert result == insert_sort(unorder)


if __name__ == '__main__':
    main()

