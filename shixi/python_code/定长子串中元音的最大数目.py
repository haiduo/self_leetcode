# 滑动窗口
def maxVowels(s: str, k: int) -> int:
    def isVowel(ch):
        return int(ch in "aeiou")
    
    n = len(s)
    vowel_count = sum(1 for i in range(k) if isVowel(s[i]))
    ans = vowel_count
    for i in range(k, n):
        vowel_count += isVowel(s[i]) - isVowel(s[i - k])
        ans = max(ans, vowel_count)
    return ans

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print(maxVowels(s,k))