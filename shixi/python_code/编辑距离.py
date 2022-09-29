#最少编辑距离
def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    # 初始化
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i
    # 状态转移
    # i , j 代表 word1, word2 对应位置的 index
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 如果word1[:i][-1]==word2[:j][-1]
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 否则从三种状态中选一个最小的然后 +1
            else:
                # dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[m][n]

#每种编辑操作的次数分别是多少次
def minDistance_count(word1: str, word2: str) -> int:
    """
    解题思路：不同操作的时候记录下来，而后分别记录每种操作的次数；
    替换操作： dp[i][j]=dp[i-1][j-1]+1
    插入操作： dp[i][j]=dp[i][j-1]+1
    删除操作： dp[i][j]=dp[i-1][j]+1
    只需要在上题代码中加入操作的计数代码即可：
    """
    m = len(word1)
    n = len(word2)
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    # 初始化
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i
    del_num, repalce_num, insert_num = 0, 0, 0
    # 状态转移
    # i , j 代表 word1, word2 对应位置的 index
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 如果word1[:i][-1]==word2[:j][-1]
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 否则从三种状态中选一个最小的然后 +1
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                # if dp[i][j] == dp[i][j-1]: repalce_num += 1
                # elif dp[i][j] == dp[i-1][j]: del_num += 1
                # elif dp[i][j] == dp[i-1][j-1]: insert_num += 1
                if dp[i][j] == dp[i-1][j]+1: del_num += 1
                if dp[i][j] == dp[i][j-1]+1: insert_num += 1
                if dp[i][j] == dp[i-1][j-1]+1: repalce_num += 1
    return repalce_num, del_num, insert_num


if __name__ == '__main__':
    str1 = 'abcdefg'
    str2 = 'adjbckf'
    print(minDistance(str1, str2))
    print(minDistance_count(str1, str2))