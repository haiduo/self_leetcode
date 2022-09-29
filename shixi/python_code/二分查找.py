from typing import List

def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # 定义target在左闭右闭的区间里，[left, right]
        while left <= right: # 当left==right，区间[left, right]依然有效，所以用 <=
            mid = (right - left) // 2 + left # 防止溢出 等同于(left + right)/2
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1 #未找到目标值

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))