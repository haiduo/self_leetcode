from collections import Counter
from functools import reduce
from operator import xor

def findTheDifference1(s: str, t: str) -> str: #xor（异或运算）思想
    return chr(reduce(xor, map(ord, s + t))) 
    # map将连接后的字符串使用ord转换为ascii码列表
    # reduce对列表所有元素使用xor得到最后剩余的值
    # 使用chr将值转换回字符并返回

def findTheDifference2(s: str, t: str) -> str: #求和相减思想
    return chr(sum(map(ord, t)) - sum(map(ord, s)))

def findTheDifference3(s: str, t: str) -> str: #计数法，生成一个26字母的数组
        str_count = [0] * 26
        for ch in s:
            str_count[ord(ch) - ord('a')] += 1
        for ch in t:
            str_count[ord(ch) - ord('a')] -= 1
            if str_count[ord(ch) - ord('a')] < 0:
                return ch

#与上述方法3相似
def findTheDifference4(s: str, t: str) -> str: #构建一个出现字母的字典，返回字典值最后存续的那个字母即可
    return list(Counter(t) - Counter(s))[0] #Counter用于计算可哈希项的Dict子类。

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(findTheDifference1(s, t))
    print(findTheDifference2(s, t))
    print(findTheDifference3(s, t))
    print(findTheDifference4(s, t))
    s = ""
    t = "y"
    print(findTheDifference1(s, t))
    print(findTheDifference2(s, t))
    print(findTheDifference3(s, t))
    print(findTheDifference4(s, t))
