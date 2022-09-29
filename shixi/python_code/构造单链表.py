class ListNode:
    """创建单个结点类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class SingleLinkedList:
    """创建一个单链表"""
 
    def __init__(self):
        self.head = None 
        self.length = 0
 
    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None
    
    def len(self):
        """获取链表的长度"""
        return self.length

    def clear(self):
        """清空链表"""
        self.head = None
        self.length = 0

    def add_fist(self, val):
        """在链表的头部添加元素"""
        node = None
        if isinstance(val, ListNode):
            node = val
        else:
            node = ListNode(val)
        node.next = self.head
        self.head = node
        self.length +=1
 
    def add_last(self, val):
        """在链表的尾部添加元素"""
        node = None
        if isinstance(val, ListNode):
            node = val
        else:
            node = ListNode(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            self.length +=1
 
    def insert_node(self, index, val):
        """在指定位置添加元素"""
        node = None
        if isinstance(val, ListNode):
            node = val
        else:
            node = ListNode(val)
        if index < 0 or index > self.length:
            print("error:out of index.")
            return None
        elif index == 0:
            self.add_fist(node)
        elif index == self.length:
            self.add_last(node)
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
            self.length +=1
 
    def remove_node(self, index):
        """删除指定结点"""
        if self.is_empty():
            print("this link list is empty.")
            return None
        if index<0 or index >= self.length:
            print("error:out of index.")
            return None
        if index == 0:
            cur = self.head
            self.head = self.head.next
            self.length -= 1
            del cur
            return None

        cur = self.head
        pre = self.head
        while cur.next and index:
            pre = cur
            cur = cur.next
            index -= 1

        if not index:
            pre.next = cur.next
            del cur
            self.length -= 1

    def update_node(self, index, value):
        """更新指定结点"""
        if self.is_empty():
            print("this link list is empty.")
            return None
        if index<0 or index >= self.length:
            print("error:out of index.")
            return None

        node = self.head
        while node.next and index:
            node = node.next
            index -= 1

        if not index:
            node.val = value

    def search_node_is_exist(self, val):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    def get_node(self, index):
        """获取指定结点的值"""
        if self.is_empty():
            print("this link list is empty.")
            return None
        if index<0 or index >= self.length:
            print("error:out of index.")
            return None

        node = self.head
        while node.next and index:
            node = node.next
            index -= 1

        if not index:
            return node.val

    def get_index(self, value):
        """获取指定结点的首次出现的索引"""
        if self.is_empty():
            print("this link list is empty.")
            return
        node = self.head
        j = 0
        while node:
            if node.val == value:
                return j
            else:
                node = node.next
                j += 1

        if j == self.length:
            print("%s not found" % str(value))
            return

    def traversal(self):
        """遍历整个链表"""
        cur = self.head
        link_list = []
        while cur is not None:
            # print(cur.val)
            link_list.append(cur.val)
            cur = cur.next
        return link_list
 
 
if __name__ == '__main__':
    lists = SingleLinkedList()
    lists.add_fist(2)
    print(lists.traversal())
    lists.add_fist(1)
    print(lists.traversal())
    lists.add_last(4)
    print(lists.traversal())
    lists.insert_node(2, 3)
    print(lists.traversal())
    print(lists.get_index(2))
    print(lists.get_node(2))
    print(lists.is_empty())
    print(lists.len())
    lists.remove_node(4)
    lists.remove_node(3)
    print(lists.traversal())
    print(lists.search_node_is_exist(3))
    print(lists.traversal())
    lists.update_node(0,6)
    print(lists.traversal())
    lists.clear()
    print(lists.traversal())