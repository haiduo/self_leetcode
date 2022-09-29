####构建平衡二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def helper(left, right):
        if left > right:
            return None
        # 总是选择中间位置左边的数字作为根节点
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)
        return root
    return helper(0, len(nums)-1)


#中序输出二叉树
def inorderTraversal(root):
    def inorder(root, ret):
        if not root: return
        inorder(root.left, ret)
        ret.append(root.val)
        inorder(root.right, ret)
        return None #可以省略不写

    ret = []
    inorder(root, ret)
    return ret


#求树的最大深度
def calDepth(root):
    if root is None:
        return 0
    else:
        left_depth = calDepth(root.left)
        right_depth = calDepth(root.right)
        return max(left_depth, right_depth)+1

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    # 构建二叉树
    tree = sortedArrayToBST(nums)
    # 中序遍历
    ret = inorderTraversal(tree)
    print(ret)
    # 二叉树深度
    depth = calDepth(tree)
    print(depth)






