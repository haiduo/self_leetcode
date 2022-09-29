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
    
    def len(self):
        """获取链表的长度"""
        return self.length

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

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
            self.length +=1
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            tem_node = self.search_node_is_exist(node.val)
            cur.next = node
            if tem_node:
                node.next = tem_node
                return 
            self.length +=1
    
    def search_node_is_exist(self, val):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return cur
            else:
                cur = cur.next
        return False

    def traversal(self):
        """遍历整个链表"""
        cur = self.head
        link_list = []
        while cur is not None:
            # print(cur.val)
            link_list.append(cur.val)
            cur = cur.next
        return link_list

#创建单链表
def createSinglyLink(single_list: SingleLinkedList, list_link:list)-> ListNode:
    for val in list_link:
        single_list.add_last(val)

def traversal_node(head: ListNode):
        """遍历整个链表"""
        cur = head
        link_list = []
        while cur is not None:
            # print(cur.val)
            link_list.append(cur.val)
            cur = cur.next
        return link_list

#判断是否有环
def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

#判断是否有环，并返回入口节点位置
def detectCycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # 如果相遇
        if slow == fast:
            p = head #从起始位置开始
            q = slow #从相遇位置开始
            while p!=q:
                p = p.next
                q = q.next
            return p.val #也可以return q
    return None


if __name__ == "__main__":
    
    list_link = [1,3,4,5,6,7,3]
    single_list = SingleLinkedList()
    createSinglyLink(single_list, list_link)
    # print(single_list.traversal())
    head = single_list.head
    print(hasCycle(head))
    print(detectCycle(head))

    list_link = [1,3,4,5,6,7]
    single_list = SingleLinkedList()
    createSinglyLink(single_list, list_link)
    # print(single_list.traversal())
    head = single_list.head
    print(hasCycle(head))
    print(detectCycle(head))

