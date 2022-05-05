# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/38:48
# 文件名称：graphic.py.py
# 开发工具：PyCharm
import numpy as np

"""
color[i] = 0, 没有被访问过
color[i]  = -1, 后裔节点均被访问过
color[i]  = 1, 之前被访问过，后裔节点中正在被访问
"""


class Graph(object):
    def __init__(self, G):
        self.color = [0] * len(G)
        self.G = np.array(G)
        self.isDAG = True
        self.circlecount = 0

        # 对于graph进行预处理，删除孤立点

    def graph_preprocessing(self):
        index = []
        for i in range(len(self.G)):
            if np.sum(self.G[:, i]) == 0 and np.sum(self.G[i, :]) == 0:
                index.append(i)
        # delete columns
        self.G = np.delete(self.G, index, axis=1)
        # delte rows
        self.G = np.delete(self.G, index, axis=0)
        self.color = [0] * len(self.G)

    def DFS(self, i):
        self.color[i] = 1
        for j in range(len(self.G)):
            if self.G[i][j] != 0:
                # print(str(i) + 'can go to '+ str(j))
                if self.color[j] == 1:
                    self.circlecount = self.circlecount + 1
                    self.isDAG = False
                elif self.color[j] == -1:
                    continue
                else:
                    # print('We are visiting node' + str(j))
                    self.DFS(j)
            self.color[i] = -1

            # print(str(i) + " has been examined")

    def DAG(self):
        for i in range(len(self.G)):
            if self.color[i] == 0:
                print(i)
                self.DFS(i)


##test1 circle = 2
file_path = 'H:\program_contest\初赛\初赛/test_data.txt'
with open (file_path) as file_object:
    lines = file_object.readlines()
start_p=[]
end_p=[]
for line in lines:
    #li=list(line)
    li = line.split(",")
    start_p.append(int(li[0]))
    end_p.append(int(li[1]))
    # print(int(line.rstrip()))
total = start_p+end_p
total = list(set(total))
total.sort()
maxu = max(total)
matrix=[None]*maxu
for i in range(maxu):
    matrix[i]=[0]*maxu
for j in range(len(start_p)):
    matrix[start_p[j]-1][end_p[j]-1]=1
G=matrix
G1 = Graph(G)
G1.DAG()