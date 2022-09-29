def longestCommonSubsequence(text1, text2):
        M, N = len(text1), len(text2)
        # dp = [[0 for _ in range(N+1)] for _ in range(M+1)] # 先对dp数组做初始化操作
        dp = [[0] * (N+1) for _ in range(M+1)]  # 注意二维数组的初始化
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[M][N]

if __name__ == '__main__':
    str1 = 'abcdefg'
    str2 = 'adjbckf'
    print(longestCommonSubsequence(str1, str2))