from typing import List

#快慢指针法---推荐 O(n)
def removeElement1(nums: List[int], val: int) -> int:
    fast = 0
    slow = 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow

#双指针法--O(n)
def removeElement2(nums: List[int], val: int):
    if not nums:
        return 0 
    left ,right = 0, len(nums)-1
    while left<right:
        while(left<right and nums[left]!=val):
            left += 1
        while(left<right and nums[right]==val):
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
    return left if nums[left]==val else left+1

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(removeElement1(nums,val))
    nums = [3,2,2,3]
    val = 3
    print(removeElement2(nums,val))