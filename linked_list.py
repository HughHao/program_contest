# _*_ coding:utf-8 _*_
# 开发人员：郝海强
# 开发时间：2020/4/410:28
# 文件名称：linked_list.py.py
# 开发工具：PyCharm
# 链表是由一组被称为结点的数据元素组成的数据结构，每个结点本身包含结点本身的信息和指向下一个节点的地址。
# 信息域+指针域


import time
time_start = time.time()



class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p
class LinkList(object):
    #初始化
    def __init__(self):
        self.head = 0


    #获取元素
    def __getitem__(self,key):
        if self.is_empty():
            print('linklist is empty')
        elif (key<0) or (key > self.getlength()):
            print('the given key is error')
        else:
            return self.getitem(key)

    #设置元素
    def __setitem__(self,key,value):
        if self.is_empty():
            print('linklist is empty.')
        elif (key <0) or (key >self.getlength()):
            print('the given key is error')
        else:
            self.delete(key)
            return self.insert(key)

    #初始化列表
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    #获取链表长度
    def getlength(self):
        p = self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    #判断链表是否为空
    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False


    # 清空链表
    def clear(self):
        self.head = 0

    #尾部追加结点
    def append(self,item):
        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next !=0:
                p = p.next
            p.next = q


    #

    def getitem(self,index):
        if self.is_empty():
            print('linklist is empty')
            return
        j=0
        p = self.head
        while p.next !=0 and j<index:
            p = p.next
            j+=1
        if j==index:
            return p.data
        else:
            print('target is not exist!')

    #插入节点
    def insert(self,index,item):
        if self.is_empty() or index<0 or index>self.getlength():
            print('LinkList is empty.')
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post = self.head
        j=0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p
    # 删除结点
    def delete(self,index):
        if self.is_empty() or index>self.getlength():
            print('LinkList is empty')
            return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p=p.next
            j+=1
        if index ==j:
            post.next = p.next

    # 寻找下标
    def index(self,value):
        if self.is_empty():
            print('LinkList is empty.')
            return
        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1
        if p.data ==value:
            return i
        else:
            return -1



l = LinkList()
l.initlist([1,2,3,4,5])
print(l.getitem(4))
l.append(6)
print(l.getitem(5))


l.insert(4,40)
print(l.getitem(3))
print(l.getitem(4))
print(l.getitem(5))

l.delete(5)
print(l.getitem(5))
l.index(5)


time_end = time.time()
time_c = time_end - time_start
print('time_cost',time_c,'s')