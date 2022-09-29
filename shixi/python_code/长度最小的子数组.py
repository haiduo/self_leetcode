from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    ans = n + 1  # 记录最短长度
    start, end = 0, 0  # 滑动窗口左右边界
    sum = 0  # 记录当前元素和
    while end < n:
        sum += nums[end]
        while sum >= target:
            ans = min(ans, end - start + 1)
            sum -= nums[start]
            start += 1
        end += 1
    return 0 if ans == n + 1 else ans

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    print(minSubArrayLen(target, nums))