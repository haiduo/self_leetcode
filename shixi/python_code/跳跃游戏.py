from typing import List

#贪心，维护可达到的最远坐标
def canJump1(nums: List[int]) -> bool:
    if 0 not in nums: return True  # 如果没有0则一定可以到达
    if len(nums) < 2: return True
    max_distance = nums[0]  # 设定可以达到的最大坐标
    for i in range(1, len(nums) - 1):
        if i <= max_distance:  # 表示当前坐标可以达到
            max_distance = max(max_distance, i + nums[i])  # 更新可以达到的最远坐标
        else:
            return False #当前位置都不可能到达，终点位置更不可能，直接退出
    return max_distance >= len(nums) - 1

#逆推-最早开始的位置是否为起点
def canJump2(nums: List[int]) -> bool:
    if 0 not in nums: return True  # 如果没有0则一定可以到达
    if len(nums) < 2: return True
    n = len(nums)
    last = n - 1
    for i in range(n-2,-1,-1):
        if(i + nums[i] >= last): #表示当前坐标可以达到last的位置
            last = i #更新当前位置为last位置
    return last == 0

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(canJump1(nums))
    print(canJump2(nums))