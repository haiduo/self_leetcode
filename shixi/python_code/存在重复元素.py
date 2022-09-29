from typing import List
class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool: #集合方法
        return not len(set(nums))==len(nums)
    
    def containsDuplicate2(self, nums: List[int]) -> bool: #哈希表法
        if len(nums) == 0:
            return False
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping [num] = 1
            else:
                return True
                # mapping [num] = mapping.get(num) + 1 #统计出现的次数
        return False

if __name__ == '__main__':
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,1]
    print(sol.containsDuplicate1(nums1))
    print(sol.containsDuplicate1(nums2))
    print(sol.containsDuplicate2(nums1))
    print(sol.containsDuplicate2(nums2))

