
class Solution:
    def intersection(self, start1, end1, start2, end2)-> bool:
        x1, y1, x2, y2, x3, y3, x4, y4 = *start1, *end1, *start2, *end2
        det = lambda x, y, x0, y0, x1, y1: (y1-y0)*(x-x1) - (x1-x0)*(y-y1)
        if det(x1,y1,x3,y3,x4,y4) * det(x2,y2,x3,y3,x4,y4) > 0:
            return False
        if det(x3,y3,x1,y1,x2,y2) * det(x4,y4,x1,y1,x2,y2) > 0:
            return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    ret = sol.intersection([0.0, 0.0], [10.0, 10.0], [0.0, 0.0], [10.0, -10.0])
    print(ret)
    