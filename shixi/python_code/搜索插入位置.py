from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right: #定义target在左闭右闭的区间里，[left, right] 
        middle = (right - left) // 2 + left

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
            
    return right + 1

if __name__ == "__main__":
    nums = [0,3,5,9,12]
    target = -1
    print(searchInsert(nums, target))
