from typing import List

#回溯法
def generateParenthesis( n: int) -> List[str]:
        result = []
        backtracking(n, result, 0, 0, "")
        return result
    
def backtracking(n, result, left, right, s):
    if right > left:
        return
    if (left == n and right == n):
        result.append(s)
        return
    if left < n:
        backtracking(n, result, left+1, right, s+"(")
    if right < left:
        backtracking(n, result, left, right+1, s+")")

if __name__ == '__main__':
    n = 3
    print(generateParenthesis(n))
    n = 0
    print(generateParenthesis(n))