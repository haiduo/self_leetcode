"https://leetcode.cn/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/"
# Definition for singly-linked list.
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
            cur.next = node
            self.length +=1

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

#双指针迭代法
def reverseList_i(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

#递归法
def reverseList_r(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    p = reverseList_r(head.next)
    head.next.next = head
    head.next = None

    return p

if __name__ == "__main__":
    list_link = [1,2]
    list_link = [1,2,3,4]
    single_list = SingleLinkedList()
    createSinglyLink(single_list, list_link)
    print(single_list.traversal())
    head = single_list.head
    head = reverseList_i(head)
    print(traversal_node(head))
    head = reverseList_r(head)
    print(traversal_node(head))