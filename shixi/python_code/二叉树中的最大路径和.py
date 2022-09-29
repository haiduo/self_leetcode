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

def maxPathSum(root: TreeNode) -> int:
    maxSum = float("-inf")
    def maxGain(node):
        if not node:
            return 0
        # 递归计算左右子节点的最大贡献值,只有在最大贡献值大于 0 时，才会选取对应子节点
        leftGain = max(maxGain(node.left), 0)
        rightGain = max(maxGain(node.right), 0)
        # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        if node.val: 
            priceNewpath = node.val + leftGain + rightGain
        else : 
            priceNewpath = leftGain + rightGain
        # 更新答案
        nonlocal maxSum   #变量maxSum = float("-inf")在最外层声明则用global
        maxSum = max(maxSum, priceNewpath)
        # 返回节点的最大贡献值
        if node.val: 
            return node.val + max(leftGain, rightGain)
        else:
            return max(leftGain, rightGain)

    maxGain(root)
    return maxSum


if __name__ == "__main__":
    list1 = [1,2,3]
    list2 = [-10,9,20,None,None,15,7]
    list3 = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = createtree(list2)
    print(maxPathSum(root))
