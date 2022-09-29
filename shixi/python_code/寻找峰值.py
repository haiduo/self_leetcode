from typing import List

def findPeakElement(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 # 定义target在左闭右闭的区间里，[left, right]
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(findPeakElement(nums))