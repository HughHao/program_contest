import time

time_start = time.time()
# from johnson import *
file_path = 'L:\program_contest\初赛/3w节点28w边的测试数据/test_data.txt'
start_p = []
end_p = []
with open(file_path) as file_object:
    for line in file_object:
        # line = lines.readlines()
        li = line.split(",")
        start_p.append(li[0])
        end_p.append(li[1])
time_1 = time.time()
time1 = time_1 - time_start
# print(int(line.rstrip()))
# total = start_p+end_p
# total = list(set(total))
# total.sort()
graph = {}
keys = []
for index in range(len(start_p)):
    key = start_p[index]
    value = end_p[index]
    if key not in keys:
        graph[key] = [value]
        keys.append(key)
    else:
        graph[key].append(value)
# cycle = list(tuple(simple_cycles(graph)))
# print(len(cycle))
# print(cycle)
# for k,v in graph.items():
#     print(k,':',v)

time_end = time.time()
time_c = time_end - time1
print('time_1', time1, 's')
print('time_2', time_c, 's')
