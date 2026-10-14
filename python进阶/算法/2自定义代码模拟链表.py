"""
@File : 2自定义代码模拟链表.py
@Author : 王子墨
@Description : 
@Date :2026/9/9
案例：自定义代码模拟链表

链表介绍：
概述：
    它属于数据结构之 线性结构的一种，每个节点都只能有 1个前驱 和 1个后继节点。
作用：
    用于优化顺序表的弊端(如果没有足够的连续的内存空间，会导致扩容失败)
    链表扩容时，有地儿就行，连不连续无所谓。
组成：
    由 节点 组成，其中节点由 元素域(数值域) 和 链接域(地址域)组成。
分类：
    根据 节点类型不同，链表主要分为：
    单向链表：节点由1个数值域 和 1个地址域组成，前边节点的地址域存储的是后续节点的地址，最后1个节点的地址域为 None
    单向循环链表：
    双向链表：
    双向循环链表：
    详见今日随堂图片。

自定义代码模拟链表，思路分析：
1. 自定义SingleNode类，表示 节点类。
    属性：
        item    数值域(元素域)
        next    地址域(链接域)

2. 自定义SingleLinkedList类，表示：链表
    属性：
        head  表示头结点，指向第1个节点。
    行为：
        is_empty(self) 链表是否为空
        length(self) 链表长度
        travel(self) 遍历整个链表
        add(self, item) 链表头部添加元素
        append(self, item) 链表尾部添加元素
        insert(self, pos, item) 指定位置添加元素
        remove(self, item) 删除节点
        search(self, item) 查找节点是否存在

3. 测试。
"""
#1. 自定义SingleNode类，表示 节点类。
class SingleNode:

    def __init__(self,item):

        self.item = item
        self.next = None

# 2. 自定义SingleLinkedList类，表示：链表
class SingleLinkedList:

    def __init__(self,node=None):
        self.head = node

    # 链表是否为空
    def is_empty(self):

        # if self.head == None:
        #     return True
        # else:
        #     return False

        # return True if self.head is None else False

        return  self.head is None

    # 链表长度
    def length(self):

        #创建游标(表示当前节点),默认从头节点开始
        cur = self.head
        #定义计数器
        count = 0
        #开始遍历，只要当前节点不为空，就一直循环
        while cur is not None:
            count += 1
            #cur指向下一个节点
            cur = cur.next

        return count

    # 遍历整个链表
    def travel(self):

        #创建游标(表示当前节点),默认从头节点开始
        cur = self.head
        #开始遍历，只要当前节点不为空，就一直循环
        while cur is not None:
            print(f"数值域:{cur.item}")
            cur = cur.next

    # 链表头部添加元素
    def add(self, item):

        #创建新节点
        new_node = SingleNode(item)
        #设置新节点的地址域 指向 头节点
        new_node.next = self.head
        #设置头节点 指向 新节点
        self.head = new_node

    # 链表尾部添加元素
    def append(self, item):

        #创建新节点
        new_node = SingleNode(item)
        #判断链表如果为空，直接设置当前节点为头节点
        if self.is_empty():
            self.head = new_node
        else:
            #链表不为空，需要找到尾节点
            # 创建游标(表示当前节点),默认从头节点开始
            cur = self.head
            # 开始遍历，只要当前节点不为空，就一直循环
            while cur.next is not None:
                #游标后移
                cur = cur.next
            #cur是最后一个节点，设置它的地址域指向新节点
            cur.next = new_node


    # 指定位置添加元素
    def insert(self, pos, item):

        # pos <= 0 往前加
        if pos <= 0:
            self.add(item)

        # pos > 0 往后加
        elif pos>=self.length():
            self.append(item)

        # 往中间加
        else:
            # 创建游标(表示当前节点),默认从头节点开始
            cur = self.head
            #记录当前节点的位置
            count = 0
            node = SingleNode(item)
            #找到要插入的前一个位置的前一个位置
            while count < pos -1 :
                cur = cur.next
                count += 1
            #设置 新节点的地址域 指向 插入位置前那个节点的 地址域
            node.next = cur.next
            #设置 插入位置前的那个节点的地址域 指向 新节点
            cur.next = node

    # 删除节点
    def remove(self, item):

        # 创建游标(表示当前节点),默认从头节点开始
        cur = self.head
        #要删除的节点的前驱节点
        pre = None
        #遍历 只要当前节点不为空，就一直循环
        while cur is not None:
            if cur.item == item:
                #判断要删除的节点是否是头节点
                if cur == self.head:
                    self.head = cur.next
                else:
                    #设置 前驱节点的地址域 指向 当前节点的地址域
                    pre.next = cur.next
                return
            else:
                #当前节点不是要删除的节点，游标后移
                pre = cur
                cur = cur.next

    # 查找节点是否存在
    def search(self, item):

        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":

    # node1 = SingleNode(10)
    # print(f"元素域: {node1.item}")
    # print(f"地址域:{node1.next}")
    # print(f"node1对象:{node1}")   #地址值
    # print(f"node1的类型:{type(node1)}")
    # print('-'*23)
    #
    # my_linkedlist = SingleLinkedList(node1)
    # print(f"头节点为:{my_linkedlist.head}")
    # print(f"头节点的元素域：{my_linkedlist.head.item}")
    # print(f"头节点的地址域：{my_linkedlist.head.next}")

    node2 = SingleNode("王子墨")
    my_linkedlist2 = SingleLinkedList(node2)
    # my_linkedlist2 = SingleLinkedList()
    # print(f"头节点为:{my_linkedlist2.head}")
    # print(f"头节点的元素域:{my_linkedlist2.head.item}")
    # print(f"头节点的地址域:{my_linkedlist2.head.next}")
    print('-'*23)

    print(f"链表是否为空:{my_linkedlist2.is_empty()}")
    print('-'*23)

    #头部添加
    my_linkedlist2.add("wzm")

    #尾部添加
    my_linkedlist2.append(19)

    #指定添加
    my_linkedlist2.insert(2,25)

    #删除
    my_linkedlist2.remove('wzm')


    print(f"链表长度:{my_linkedlist2.length()}")
    print('-'*23)

    #遍历
    my_linkedlist2.travel()
    print('-'*23)

    #查找
    print(f"查找结果:{my_linkedlist2.search("王子墨")}")
    print(f"查找结果:{my_linkedlist2.search("wzm")}")
    print("-"*23)


