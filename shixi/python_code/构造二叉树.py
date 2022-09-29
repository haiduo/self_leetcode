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

def PrintFromTopToBottom_1(root):#输出包含空指针
        ans=[]
        if root==None:
            return ans
        else:
            q=[root]
            while q:
                node=q.pop(0)
                if node.val:
                    ans.append(node.val)
                else:
                    ans.append(None)
                    continue
                if node.left:
                    q.append(node.left)
                else:
                    q.append(TreeNode(None))
                if node.right:
                    q.append(node.right)
                else:
                    q.append(TreeNode(None))
            return ans

#先序遍历
def preorderTraversal(root):
    def inorder(root, ret):
        if not root: return
        if root.val:ret.append(root.val)
        inorder(root.left, ret)
        inorder(root.right, ret)
        return None #可以省略不写

    ret = []
    inorder(root, ret)
    return ret

#中序输出二叉树
def inorderTraversal(root):
    def inorder(root, ret):
        if not root: return
        inorder(root.left, ret)
        if root.val:ret.append(root.val)
        inorder(root.right, ret)
        return None #可以省略不写

    ret = []
    inorder(root, ret)
    return ret
    
#后序输出二叉树
def postorderTraversal(root):
    def inorder(root, ret):
        if not root: return
        inorder(root.left, ret)
        inorder(root.right, ret)
        if root.val:ret.append(root.val)
        return None #可以省略不写

    ret = []
    inorder(root, ret)
    return ret

if __name__ == "__main__":
    list_ = [-10,9,20,None,None,15,7]
    tree = createtree(list_)
    print('层次：', PrintFromTopToBottom(tree))
    print('先序：', preorderTraversal(tree))
    print('中序：', inorderTraversal(tree))
    print('后序：', postorderTraversal(tree))