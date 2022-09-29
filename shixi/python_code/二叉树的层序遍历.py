from typing import List
from collections import deque
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

class Solution(object):
    def levelOrder_bfs(self, root): #BFS遍历
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            size = len(queue)
            tmp = []
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for _ in range(size):
                r = queue.pop(0)
                if r.val is not None: tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            # 将临时list加入最终返回结果中
            res.append(tmp)
        return res

    def levelOrder_dfs(self, root):#DFS遍历
        if not root:
            return []
        res = []
        def dfs(level,r):
            # 假设res是[ [1],[2,3] ]， level是3，就再插入一个空list放到res中
            if len(res)<level:
                res.append([])
            #  将当前节点的值加入到res中，level代表当前层，假设level是3，节点值是99
            # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
            if r.val is not None:res[level-1].append(r.val)
            # 递归的处理左子树，右子树，同时将层数level+1
            if r.left:
                dfs(level+1,r.left)
            if r.right:
                dfs(level+1,r.right)
        dfs(1,root)
        return res

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:#返回自底向上的层序遍历
        result = []
        if root is None:
            return result
        
        q = deque([])
        q.append(root)
        temp = deque([])
        while len(q) > 0:
            size = len(q)
            ls = []
            while size > 0:
                cur = q.popleft()
                if cur.val is not None:ls.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                size = size - 1
            temp.appendleft(ls[:]) #添加到最左边，一般用链表实现
        result = list(temp)
        
        return result

if __name__ == "__main__":
    sol =Solution()
    list_ = [3,9,20,None,None,15,7]
    low = 7
    high = 15
    tree = createtree(list_)
    print('BFS：', sol.levelOrder_bfs(tree))
    print('DFS：', sol.levelOrder_dfs(tree))
    print('BFS_reverse：', sol.levelOrder_bfs(tree)[::-1])
    print('DFS_reverse：', sol.levelOrder_dfs(tree)[::-1])
    print('BFS_reverse：', sol.levelOrderBottom(tree))