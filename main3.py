import time

# from johnson import*
import sys

sys.setrecursionlimit(20000)

time_start = time.time()
file_path = 'L:\program_contest\初赛/3w节点28w边的测试数据/test_data.txt'
graph = {}
temp = 0
with open(file_path) as file_object:
    for line in file_object:
        a = ''
        b = ''
        k = 1
        for st in line:
            if k < 3:
                if st != ',' and k < 2:
                    a += st
                elif st != ',' and k == 2:
                    b += st
                else:
                    k += 1
            else:
                break
        if a == temp:
            graph[a].append(b)
        else:
            graph[a] = [b]
        temp = a
time_1 = time.time()
time1 = time_1 - time_start

# cycle = list(tuple(simple_cycles(graph)))
# print(len(cycle))
# cycle.sort(key=len)
# for list1 in cycle:
#     print(list1, end='\n')
print('把数据处理成字典时间：', time1, 's')
# print('打印字典时间:', time_c, 's')
