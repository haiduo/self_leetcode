import itertools
from typing import List

#库函数
def subsets1(nums: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(nums)+1):
        for tmp in itertools.combinations(nums, i):
            res.append(tmp)
    return res

#迭代
def subsets2(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res

#DFS递归--回溯法
def subsets3(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    
    def helper(i, tmp):
        res.append(tmp)
        # if i == n: #当当前索引已经不在nums的范围内，就是提前终止
        #     return
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])
    helper(0, [])
    return res  

if __name__ == "__main__":
    nums = [1,2,3]
    print(subsets1(nums))
    print(subsets2(nums))
    print(subsets3(nums))

    nums = []
    print(subsets1(nums))
    print(subsets2(nums))
    print(subsets3(nums))

