class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

#层次构造
def createtree(list_):
        if list_[0]:
            root=TreeNode(list_[0])
            q_nodes=[root]
            id=1
            while q_nodes and id<len(list_):
                node=q_nodes[0]#依次为每个节点分配子节点
                node.left=TreeNode(list_[id]) if list_[id] else TreeNode(None)
                q_nodes.append(node.left)
                node.right=TreeNode(list_[id+1]) if id+1<len(list_) and list_[id+1] else TreeNode(None)
                q_nodes.append(node.right)
                id+=2#每次取出两个节点
                q_nodes.pop(0) #删除列表的第一个元素
            return root
        else:
            return None

#方法：递归
def longestUnivaluePath(root):
    ans = 0
    def arrow_length(node):
        nonlocal ans
        if not node: 
            return 0
        left_length = arrow_length(node.left)
        right_length = arrow_length(node.right)
        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1
        ans = max(ans, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    arrow_length(root)
    return ans


if __name__ == "__main__":
    list2 = [5,4,5,1,1,None,5]
    root = createtree(list2)
    print(longestUnivaluePath(root))
