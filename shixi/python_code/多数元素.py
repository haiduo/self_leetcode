import collections
from typing import List

#分治思想
def getMajority(nums,left,right):
    if left == right:
        return nums[left]

    mid = (left + right) // 2
    leftMajority = getMajority(nums,left,mid)
    rightMajority = getMajority(nums,mid+1,right)

    if leftMajority == rightMajority:
        return leftMajority
    else:
        left_count = 0
        right_count = 0
        for i in nums[left:right+1]: #切片右侧得是right+1 不然当前数组取不到right
            if i == leftMajority:
                left_count += 1
            elif i == rightMajority:
                right_count += 1

        return leftMajority if left_count > right_count else rightMajority

def majorityElement1(nums: List[int]) -> int:
    return getMajority(nums,0,len(nums) - 1)

#Boyer-Moore 摩尔投票算法
def majorityElement2(nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

#哈希表法
def majorityElement3(nums: List[int]) -> int:
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

#排序算法
def majorityElement(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]

if __name__ == "__main__":
    nums = [2,2,3,3,3]
    nums1 = [2,2,1,1,1,2,2]
    print(majorityElement1(nums))
    print(majorityElement2(nums))
    print(majorityElement3(nums))
    print(majorityElement1(nums1))
    print(majorityElement2(nums1))
    print(majorityElement3(nums1))