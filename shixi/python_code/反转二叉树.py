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

#层次遍历
def PrintFromTopToBottom(root):
        ans=[]
        if root==None:
            return ans
        else:
            q=[root]
            while q:
                node=q.pop(0)
                if node.val:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return ans

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: #递归-自低向上
        if not root: #递归函数的终止条件，节点为空时返回
            return root
        # 将当前节点的左右子树交换
        root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
        return root
    
    def invertTree_bfs(self, root):#迭代 BFS
        if not root:
            return None
        # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        queue = [root]
        while queue:
            # 每次都从队列中拿一个节点，并交换这个节点的左右子树
            tmp = queue.pop(0)
            tmp.left,tmp.right = tmp.right,tmp.left
            # 如果当前节点的左子树不为空，则放入队列等待后续处理
            if tmp.left:
                queue.append(tmp.left)
            # 如果当前节点的右子树不为空，则放入队列等待后续处理	
            if tmp.right:
                queue.append(tmp.right)
        # 返回处理完的根节点
        return root

if __name__ == "__main__":
    sol =Solution()
    list_ = [3,9,20,None,None,15,7]
    low = 7
    high = 15
    tree = createtree(list_)
    print('递归：', sol.invertTree(tree))
    print('层次：', PrintFromTopToBottom(tree))
    print('迭代：', sol.invertTree_bfs(tree))
    print('层次：', PrintFromTopToBottom(tree))