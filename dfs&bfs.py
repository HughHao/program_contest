# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/2715:32
# 文件名称：dfs&bfs.py
# 开发工具：PyCharm
import Main
graph=Main.getdict()
#BFS 广度优先搜索   层序遍历
def BFS(graph,s):#graph图  s指的是开始结点
    #需要一个队列
    queue=[]
    queue.append(s)
    seen=set()#看是否访问过该结点
    seen.add(s)
    while (len(queue)>0):
        vertex=queue.pop(0)#保存第一结点，并弹出，方便把他下面的子节点接入
        nodes=graph[vertex]#子节点的数组
        for w in nodes:
            if w not in seen:#判断是否访问过，使用一个数组
                queue.append(w)
                seen.add(w)
        print(vertex)


# DFS指的是深度优先搜索    回溯法(会回看前面的节点)
# 一直往前走，走不下去往回跳
# 使用stack来进行深度的顺序
# 把栈顶元素去除，在把临接点放入


# 其实并不难，只要把队列改成栈就可以了
def DFS(graph, s):  # 图  s指的是开始结点
    # 需要一个队列
    stack = []
    stack.append(s)
    seen = set()  # 看是否访问过
    seen.add(s)
    lie = []
    a=[]
    b=[]
    k=1
    while (len(stack) > 0):
        # 拿出邻接点
        vertex = stack.pop()  # 这里pop参数没有0了，最后一个元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:  # 如何判断是否访问过，使用一个数组
                stack.append(w)
                seen.add(w)
        lie.append(vertex)
        #print(lie)
        lie.sort()
        if k == 1:
            a=lie
            print(a,end='')
        else:
            b=lie
            if a!=b:
                print(b,end='')
            else:
                continue
        k += 1

for k in graph.keys():
    DFS(graph,k)
    #print('\n')