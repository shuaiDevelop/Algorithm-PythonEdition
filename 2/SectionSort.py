#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: shuai
@license: Apache Licence 
@software: PyCharm
@file: SectionSort.py
@time: 2018-03-01 14:26
"""
import time

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 重载 小于的方法
    def __lt__(self, other):
        return self.score > other.score if self.score != other.score else self.name < other.name

    # # 重载str 方法
    # def __str__(self):
    #     return "Student: " + self.name + " " + str(self.score)

    def __repr__(self):
        return "Student: " + self.name + " " + str(self.score)


def selection_sort(arr):
    """ 选择排序 简单的实现"""
    if not isinstance(arr, list):
        raise Exception("arr must be a list")
    n = len(arr)
    for i in range(n):
        """ 寻找 [i, n)区间里的最小值"""
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    print(selection_sort([3, 4, 6, 1, 2, 6, 8, 9, 0, 5]))
    print(selection_sort(['2', '1', 'a', 'b', 'c', '7']))
    print(selection_sort([Student('A', 100), Student('D', 10), Student('F', 88), Student('B', 88)]))

    # # 通过测试  10000个数的数组 通过选择排序 花费的时间 大概是 2.717s  100000个数花费时间大概是  273.217s
    # #  大致可以得出  选择排序的时间复杂度 是 n^2 级别的  所消耗的时间和数据之间成平方的关系  数据量增大10倍 处理时间增大100倍
    # arr = list(range(10000))
    # start_time = time.clock()
    # selection_sort(arr)
    # end_time = time.clock()
    # print(end_time - start_time)






