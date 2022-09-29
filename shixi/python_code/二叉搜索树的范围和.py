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

class Solution:
    # Leetcode 938. Range Sum of BST
    # Time Complexity: O(N)
    # Space Complexity: O(H)
    def rangeSumBST1(self, root: TreeNode, low: int, high: int) -> int: #递归法 任意个二叉树遍历都可以
        if not root or root.val is None: # if not root:
            return 0
        leftSum = self.rangeSumBST1(root.left, low, high)
        rightSum = self.rangeSumBST1(root.right, low, high)
        result = leftSum + rightSum
        if (root.val >= low and root.val <= high): #此处为后序遍历
            result = result + root.val
        return result

    def rangeSumBST_iter(self, root: TreeNode, low: int, high: int) -> int: #迭代法，栈的思想
        cur = 0
        stack = []
        while root or stack:
            if root and root.val is not None: #if root:
                stack.append(root)
                root = root.left
            else:
                t = stack.pop(-1) #默认为 index=-1，删除最后一个列表值
                if low <= t.val <= high:
                    cur += t.val
                root = t.right
        return cur

    #因为题目是二叉搜索树，所以可以根据其性质进行剪枝
    def rangeSumBST2(self, root: TreeNode, low: int, high: int) -> int: 
        res = 0
        if not root or root.val is None: # if not root:
            return res
        if root.val > low: #如果 root.val <= low，那么不用继续搜索左子树；
            res += self.rangeSumBST2(root.left, low, high)
        if low <= root.val <= high:
            res += root.val
        if root.val < high: #如果 root.val >= high，那么不用继续搜索右子树
            res += self.rangeSumBST2(root.right, low, high)
        return res

    # BFS法 广度优先搜索
    def rangeSumBST3(self, root: TreeNode, low: int, high: int) -> int: 
        result = 0
        queue = []
        if root and root.val is not None:
            queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                cur = queue.pop()
                if cur.val >= low and cur.val <= high:
                    result = result + cur.val
                if cur.left is not None and cur.left.val is not None:
                    queue.append(cur.left)
                if cur.right is not None and cur.right.val is not None:
                    queue.append(cur.right)
                size = size - 1
        return result


if __name__ == "__main__":
    sol =Solution()
    list_ = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    tree = createtree(list_)
    print('递归：', sol.rangeSumBST1(tree,low,high))
    print('迭代：', sol.rangeSumBST_iter(tree,low,high))
    print('递归剪枝：', sol.rangeSumBST2(tree,low,high))
    print('BFS:', sol.rangeSumBST3(tree,low,high))