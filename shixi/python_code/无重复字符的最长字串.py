
def lengthOfLongestSubstring(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，开始移动
    right, count = 0, 0
    begin = None
    for left in range(n):
        if left != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[left - 1])
        while right < n and s[right] not in occ:
            # 不断地移动右指针
            occ.add(s[right])
            right += 1
        # 第 left 到 right 个字符是一个极长的无重复字符子串
        if right-left > count:
            count = right-left
            begin = left
    return s[begin: begin+count]

if __name__ == "__main__":
    s1 = "babad"
    s2 = 'ccc'
    s3 = 'cbbd'
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))
    print(lengthOfLongestSubstring(s3))
