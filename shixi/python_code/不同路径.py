from math import comb

#动态规划
def uniquePaths1(m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

#组合数学:从 m+n-2次移动中选择 m-1 次向下移动的方案数，即组合数
def uniquePaths2(m: int, n: int) -> int:
    return comb(m + n - 2, n - 1)


if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths1(m, n))
    print(uniquePaths2(m, n))
