from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) ->List[List[int]]:
        if not intervals: return []   #等价if len(intervals) == 0: return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空,或者当前区间与上一区间不重合,直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话,我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

if __name__ == "__main__":
    sol = Solution()
    a = [[1,3],[2,6],[8,10],[15,18]]
    b = []
    print(sol.merge(a))
    print(sol.merge(b))


