from typing import List
from functools import reduce

# 只有一个数出现一次，每个不同的数总和*2作差(前提是重复的元素最多出现两次)
def singleNumber1(nums: List[int]) -> int: 
    return 2*sum(set(nums))-sum(nums)

def singleNumber2(nums: List[int]) -> int: # 采用异或算法 a ^ a = 0 且 a ^ 0 = a
    return reduce(lambda x,y: x^y,nums)  # reduce()函数会对参数序列中元素进行累积。
    # res = 0
    # for num in nums: res ^= num 
    # return res

if __name__ == "__main__":
    nums1 = [2,2,1]
    nums2 = [4,1,2,1,2]
    print(singleNumber1(nums1))
    print(singleNumber2(nums1))
    print(singleNumber1(nums2))
    print(singleNumber2(nums2))

