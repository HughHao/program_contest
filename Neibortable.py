# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/614:04
# 文件名称：Neibortable.py.py
# 开发工具：PyCharm
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'G', 'H'],
         'E': ['F'],
         'F': ['C']}


# 从图中找出任意一条从起始顶点到终止顶点的路径
def find_path(graph, start, end, path=[]):
    if start == end:
        print("path", path)
        return True
    if not graph.get(start):
        path.pop()
        return False
    for v in graph[start]:
        if v not in path:
            path.append(v)
            if find_path(graph, v, end, path):
                return True
    return False


path = []
if find_path(graph, 'A', 'C', path=path):
    print(path)
else:
    print(1)

# 从图中找出从起始顶点到终止顶点的所有路径
import copy


def find_path_all(curr, end, path):
    '''
    :param curr: 当前顶点
    :param end: 要到达的顶点
    :param path: 当前顶点的一条父路径
    :return:
    '''
    if curr == end:
        path_tmp = copy.deepcopy(path)
        path_all.append(path_tmp)
        return
    if not graph.get(curr):
        return
    for v in graph[curr]:
        # 一个顶点在当前递归路径中只能出现一次，否则会陷入死循环。
        if v in path:
            print("v %s in path %s" % (v, path))
            continue
        # 构造下次递归的父路径
        path.append(v)
        find_path_all(v, end, path)
        path.pop()


path_all = []
find_path_all('A', 'G', path=['A'])
print(path_all)

# 遍历图中所有顶点，按照遍历顺序将顶点添加到列表中
vertex = []


def dfs(v):
    if v not in graph:
        return
    for vv in graph[v]:
        if vv not in vertex:
            vertex.append(vv)
            dfs(vv)


for v in graph:
    if v not in vertex:
        vertex.append(v)
        dfs(v)
print(vertex)
