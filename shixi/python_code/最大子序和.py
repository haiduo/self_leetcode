from typing import List

#分治法
def maxSubArray1(nums: List[int]) -> int:
    if not nums:
        return 0
    def maxSubArrayDivideWithBorder(nums, start, end):
        if (start == end):
            # 只有一个元素，也就是递归的结束情况
            return nums[start]
        # 计算中间值
        center = (start + end) // 2
        leftMax = maxSubArrayDivideWithBorder(nums, start, center) # 计算左侧子序列最大值
        rightMax = maxSubArrayDivideWithBorder(nums, center + 1, end) # 计算右侧子序列最大值
        '''下面计算横跨两个子序列的最大值'''
        # 计算包含左侧子序列最后一个元素的子序列最大值
        leftCrossMax = nums[center]
        leftCrossSum = 0
        for i in range(center, start-1, -1):
            leftCrossSum += nums[i]
            leftCrossMax = max(leftCrossSum, leftCrossMax)
        # 计算包含右侧子序列第一个元素的子序列最大值
        rightCrossMax = nums[center+1]
        rightCrossSum = 0
        for i in range(center + 1, end+1, 1):
            rightCrossSum += nums[i]
            rightCrossMax = max(rightCrossSum, rightCrossMax)
        # 计算跨中心的子序列的最大值
        crossMax = leftCrossMax + rightCrossMax
        # 比较三者，返回最大值
        return max(crossMax, leftMax, rightMax)
    return maxSubArrayDivideWithBorder(nums, 0, len(nums)-1) 

#动态规划
'''第 i 个子组合的最大值可以通过第i-1个子组合的最大值(至少大于等于0)和第 i 个数字获得，如果第 i-1 
个子组合的最大值没法给第 i 个数字带来正增益，我们就抛弃掉前面的子组合，自己就是最大的了。'''
def maxSubArray2(nums: List[int]) -> int:
    n = len(nums)
    if not n:
        return 0
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1,n):
        if (dp[i-1] > 0):
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    # 最后不要忘记全部看一遍求最大值
    res = dp[0]
    for i in range(1,n): 
        res = max(res, dp[i])
    return res

#动态规划--改进
def maxSubArray3(nums: List[int]) -> int:
    n = len(nums)
    if not n:
        return 0
    max_num = nums[0] #全局最大值
    submax = nums[0] #前一个子组合的最大值,状态压缩
    for i in range(1,n):
        if (submax > 0):
            submax = submax + nums[i] #前一个子组合最大值大于0，正增益
        else:
            submax = nums[i]    #前一个子组合最大值小于0，抛弃前面的结果
        max_num = max(max_num, submax)  #计算全局最大值
    return max_num

#Kadane算法 跟动态方法思想一致
def maxSubArray4(nums: List[int]) -> int:
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in nums:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

#贪心算法--推荐
def maxSubArray5(nums: List[int]) -> int:
    n = len(nums)
    if not n:
        return 0
    max_num = nums[0]
    tmp = 0
    for i in range(n):
        tmp += nums[i]
        max_num = max(tmp, max_num)
        if(tmp < 0): 
            tmp = 0
    return max_num

#延伸——获取最大序列的起始和结束位置
def maxSubArrayPosition(nums: List[int]) -> List:
    n = len(nums)
    if not n:
        return []
    start, end = 0, 0
    sub_start, sub_end = 0, 0
    max_num = nums[0] #全局最大值
    submax = nums[0] #前一个子组合的最大值,状态压缩
    for i in range(1,n):
        if (submax > 0):
            submax = submax + nums[i] #前一个子组合最大值大于0，正增益
            sub_end += 1
        else:
            submax = nums[i]    #前一个子组合最大值小于0，抛弃前面的结果
            sub_start = i
            sub_end = i
        if submax > max_num:  #计算全局最大值
            max_num = submax
            start, end = sub_start, sub_end
    return ["起始和结束位置",[start,end], '最大值：',max_num]


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray1(nums))
    print(maxSubArray2(nums))
    print(maxSubArray3(nums))
    print(maxSubArray4(nums))
    print(maxSubArray5(nums))
    print(maxSubArrayPosition(nums))
    nums = []
    print(maxSubArray1(nums))
    print(maxSubArray2(nums))
    print(maxSubArray3(nums))
    print(maxSubArray4(nums))
    print(maxSubArray5(nums))
    print(maxSubArrayPosition(nums))
