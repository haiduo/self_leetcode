from typing import List

#回溯法-DFS遍历-交换思想
def permute1(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    if len(nums) == 0:
        return res
    def backtrack(first):
        # 所有数都填完了
        if first == n-1:  #满足条件，退出
            res.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]
    backtrack(first=0) #first为当前遍历到序列的第几个位置
    return res

#回溯法-DFS遍历-使用path变量栈
def permute2(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    if len(nums) == 0:
        return res
    path = [] #借助系统栈空间，保存所需要的状态变量
    used = [False]*n #初始化的时候都为false,表示这些数还没有被选择
    def dfs(n, depth):
        if depth == n:
            res.append(path.copy())
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs(n, depth + 1)
                used[i] = False
                path.pop()
    dfs(n, 0)
    return res

#回溯法-DFS遍历-使用path变量栈-（n,k）的排列
def permute3(nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    res = []
    if len(nums) == 0:
        return res
    path = [] #借助系统栈空间，保存所需要的状态变量
    used = [False]*n #初始化的时候都为false,表示这些数还没有被选择
    def dfs(n, depth):
        if depth == k:
            res.append(path.copy())
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs(n, depth + 1)
                used[i] = False
                path.pop()
    dfs(n, 0)
    return res



if __name__ == '__main__':
    nums = [1,2,3]
    print(permute1(nums))
    print(permute2(nums))
    print(permute3(nums, 2))