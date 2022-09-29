#中心扩散
def longestPalindrome_1(s: str) -> str:
    res = ''
    def expandAroundCenter(s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    for i in range(len(s)):
        s1 = expandAroundCenter(s, i, i) #奇数列
        s2 = expandAroundCenter(s, i, i + 1) #偶数列
        if len(s1) > len(res):
            res = s1
        if len(s2) > len(res):
            res = s2
    return res

#动态规划--容易超时
def longestPalindrome_2(s):
    n = len(s)
    if n < 2:
        return s
    dp = [[None for _ in range(n)] for _ in range(n)]
    max_len = 1
    begin = 0
    # length === 1
    for i in range(n) :
        dp[i][i] = True
    # length === 2
    for i in range(n-1) :
        if s[i] == s[i+1]: 
            dp[i][i+1] = True
            max_len = 2
            begin = i
        else: 
            dp[i][i+1] = False
    # length > 2
    for sub_len in range(3, n+1): 
        for i in range(n+1-sub_len):
            if i+sub_len > n:
                break
            front, end = s[i], s[i+sub_len-1]
            if front == end:
                dp[i][i+sub_len-1] = dp[i+1][i+sub_len-2]
            else: 
                dp[i][i+sub_len-1] = False
            if dp[i][i+sub_len-1] and sub_len > max_len:
                max_len = sub_len
                begin = i
    return s[begin:begin+max_len]

#动态规划——改进
def longestPalindrome_3(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    # 递推开始
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 枚举左边界，左边界的上限设置可以宽松一些
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False 
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return s[begin:begin + max_len]

if __name__ == "__main__":
    s1 = "babad"
    s2 = 'ccc'
    s3 = 'cbbd'
    print(longestPalindrome_1(s1))
    print(longestPalindrome_2(s1))
    print(longestPalindrome_3(s1))
    print(longestPalindrome_1(s2))
    print(longestPalindrome_2(s2))
    print(longestPalindrome_3(s2))
    print(longestPalindrome_1(s3))
    print(longestPalindrome_2(s3))
    print(longestPalindrome_3(s3))
    