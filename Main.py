# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/310:47
# 文件名称：Main.py
# 开发工具：PyCharm
import csv
import time
# from johnson import *
# from collections import defaultdict
import sys

sys.setrecursionlimit(20000)


def getdict():
    time_start = time.time()
    file_path = 'L:\program_contest\初赛/3w节点28w边的测试数据/test_data.txt'
    dict = {}
    with open(file_path) as file_object:
        reader = csv.reader(file_object, delimiter=',')
        for li in reader:
            if int(li[0]) in dict:
                dict[int(li[0])].append(int(li[1]))
            else:
                dict[int(li[0])] = [int(li[1])]
    # return dict
    time_mid = time.time()
    print(dict)
    time_end = time.time()
    print("处理成字典时长：", time_mid - time_start, "s")
    print("打印字典时长：", time_end - time_mid, "s")


# cycle = list(tuple(simple_cycles(dict)))
# print(len(cycle))
# cycle.sort(key=len)
# for list1 in cycle:
#     print(list1,end='\n')
getdict()
#
