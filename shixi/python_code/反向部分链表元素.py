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

# 方法1 穿针引线 t=O(N) s=O(1)  缺点：最多需要遍历两次
def reverseBetween1(head: ListNode, left: int, right: int) -> ListNode:
    def reverse_linked_list(head: ListNode):
        # 也可以使用递归反转一个链表
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

    # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
    # 建议写在 for 循环里，语义清晰
    for _ in range(left - 1):
        pre = pre.next

    # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
    right_node = pre
    for _ in range(right - left + 1):
        right_node = right_node.next
    # 第 3 步：切断出一个子链表（截取链表）
    left_node = pre.next
    curr = right_node.next

    # 注意：切断链接
    pre.next = None
    right_node.next = None

    # 第 4 步：同第 206 题，反转链表的子区间
    reverse_linked_list(left_node)
    # 第 5 步：接回到原来的链表中
    pre.next = right_node
    left_node.next = curr
    return dummy_node.next

# 方法2 一次遍历「穿针引线」反转链表（头插法）
def reverseBetween2(head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next


if __name__ == "__main__":
    list_link = [1,2]
    list_link = [1,2,3,4,5,6,7]
    single_list = SingleLinkedList()
    createSinglyLink(single_list, list_link)
    print(single_list.traversal())
    head = single_list.head
    #翻转部分链表
    head = reverseBetween1(head, 2, 6)
    print(traversal_node(head))
    head = reverseBetween2(head, 2, 6)
    print(traversal_node(head))