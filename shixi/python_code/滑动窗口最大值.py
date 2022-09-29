from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):#双端队列思想
        # 如果数组为空或 k = 0，直接返回空
        if not nums or not k:
            return []
        # 如果数组只有1个元素，直接返回该元素
        if len(nums) == 1:
            return [nums[0]]
        # 初始化队列和结果，队列存储数组的下标
        queue = deque()
        result = []
        #遍历数组中元素，right表示滑动窗口右边界
        for right in range(len(nums)):
            # 如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列
            if queue and queue[0] == right - k:
                queue.popleft()
            # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            #新元素入队列.存储元素下标
            queue.append(right) 
            # 由于数组下标从0开始，因此当窗口右边界right+1大于等于窗口大小k时，意味着窗口形成。
            # 此时，队首元素就是该窗口内的最大值
            if right + 1 >= k:
                result.append(nums[queue[0]])
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))
    nums = [1]
    k = 1
    print(sol.maxSlidingWindow(nums, k))