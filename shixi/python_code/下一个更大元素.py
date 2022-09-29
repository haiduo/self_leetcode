from typing import List
class Solution:
    # 单调栈+哈希表 O(n+m) 或 字典
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res_dict = {i:-1 for i in nums2}
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        res = []
        for j in nums1:
            res.append(res_dict[j])
        return res

if __name__ == '__main__':
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(sol.nextGreaterElement(nums1, nums2))