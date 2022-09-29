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

#深度优先搜索
def diameterOfBinaryTree(root: TreeNode) -> int:
    ans = 0
    def depth(node):
        nonlocal ans
        # 访问到空节点了，返回0
        if not node:
            return 0
        # 左儿子为根的子树的深度
        L = depth(node.left)
        # 右儿子为根的子树的深度
        R = depth(node.right)
        # 计算d_node即L+R+1 并更新ans
        ans = max(ans, L + R)
        # 返回该节点为根的子树的深度
        return max(L, R) + 1
    depth(root)
    return ans

if __name__ == "__main__":
    list2 = [1,2,3,4,5]
    root = createtree(list2)
    print(diameterOfBinaryTree(root))

