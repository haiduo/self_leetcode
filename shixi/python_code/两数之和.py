from typing import List

# 暴力求解
def twoSum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        x = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == target - x:
                return [i, j]
    return []


#哈希表法
def twoSum2(nums: List[int], target: int) -> List[int]:
    hashtable = dict() # hashtable = {}
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum1(nums, target))
    print(twoSum2(nums, target))