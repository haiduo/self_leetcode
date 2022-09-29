from math import sqrt
'''
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''
#动态规划
def numSquares1(n: int) -> int:
    dp = [0]*(n+1) #dp[i] 表示i的完全平方和的最少数量
    for i in range(1, n+1):
        dp[i] = i # 最坏的情况就是每次+1 比如: dp[3]=1+1+1
        for j in range(1, int(sqrt(i))+1): # 枚举前一个状态
            dp[i] = min(dp[i], dp[i - j*j]+1)  # 动态转移方程
    return dp[n]

#数学-四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。
def numSquares2(n: int) -> int:
    # 判断是否为完全平方数
    def isPerfectSquare(x):
        y = int(sqrt(x))
        return y*y == x
    # 判断是否能表示为 4^k*(8m+7)
    def checkAnswer4(x):
        while (x % 4 == 0):
            x /= 4
        return x % 8 == 7
    if (isPerfectSquare(n)):
        return 1
    if (checkAnswer4(n)):
        return 4
    for i in range(1, int(sqrt(n))+1):
        j = n - i * i
        if isPerfectSquare(j):
            return 2
    return 3


if __name__ == "__main__":
    n = 13
    print(numSquares1(n))
    print(numSquares2(n))
