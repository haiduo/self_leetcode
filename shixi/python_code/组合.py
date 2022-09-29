from collections import deque
from typing import List

#回溯法
def combine1(n: int, k: int) -> List[List[int]]:
    res = []
    if (k <= 0 or n < k):
        return res
    path = [] #借助系统栈空间，保存所需要的状态变量
    def dfs(n, k, begin):
        # 递归终止条件是：path 的长度等于 k
        if (len(path) == k):
            res.append(path.copy())
            return
        # 遍历可能的搜索起点
        for i in range(begin, n-(k-len(path))+2): #剪枝过程：n+1 改为 n-(k-len(path))+2
            # 向路径变量里添加一个数
            path.append(i)
            # 下一轮搜索，设置的搜索起点要加 1，因为组合数里不允许出现重复的元素
            dfs(n, k, i + 1)
            # 重点理解这里：深度优先遍历有回头的过程，因此递归之前做了什么，递归之后需要做相同操作的逆向操作
            path.pop()
    #从1开始是题目的设定
    path = []
    dfs(n, k, 1)
    return res

#按照每一个数选与不选画出二叉树 二叉树最多 n 层
def combine2(n: int, k: int) -> List[List[int]]:
    res = []
    if (k <= 0 or n < k) :
        return res
    path = [] #借助系统栈空间，保存所需要的状态变量
    def dfs(begin, n, k):
        # 合理的递归终止条件
        if (k == 0):
            res.append(path.copy())
            return
        # 剪枝的递归终止条件：if (begin == n + 1) 
        if (begin > n - k + 1):
            return
        # 不选当前考虑的数 begin，直接递归到下一层
        dfs(begin + 1, n, k)
        # 选当前考虑的数 begin，递归到下一层的时候 k - 1，这里 k 表示还需要选多少个数
        path.append(begin)
        dfs(begin + 1, n, k - 1)
        # 深度优先遍历有回头的过程，因此需要撤销选择
        path.pop()
    dfs(1, n, k)
    return res


if __name__ == '__main__':
    n = 4
    k = 2
    print(combine1(n,k))
    print(combine2(n,k))

