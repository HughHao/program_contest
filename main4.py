# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/611:09
# 文件名称：main4.py
# 开发工具：PyCharm
import time

time_start = time.time()
file_path = 'L:\program_contest\初赛/3w节点28w边的测试数据/test_data.txt'
graph = {}
keys = []
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        li = line.split(",")
        if li[0] not in keys:
            graph[li[0]] = [li[1]]
            keys.append(li[0])
        else:
            graph[li[0]].append(li[1])
time_1 = time.time()
time1 = time_1 - time_start

for k, v in graph.items():
    print(k, ':', v)

time_end = time.time()
time_c = time_end - time1
print('time_1', time1, 's')
print('time_2', time_c, 's')
