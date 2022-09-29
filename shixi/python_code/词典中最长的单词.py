from typing import List

#哈希集合+排序
def longestWord1(words: List[str]) -> str:
    words.sort(key=lambda x: (-len(x), x), reverse=True)
    longest = ""
    candidates = {""}
    for word in words:
        if word[:-1] in candidates:
            longest = word
            candidates.add(word)
    return longest

#字典树,前缀树
class Trie:
    def __init__(self):
        self.child = {} #字典的实现方式
    
    def insert(self, word: str) -> None: #lc208题目答案
        nownode = self.child
        for s in word:
            if s not in nownode.keys():
                nownode[s] = {}  #创建下一个节点
            nownode = nownode[s]
        nownode['#']='#'         #有一定的局限性 前提是单词里不能有结束符

    def search(self, word: str) -> bool:
        nownode = self.child
        for s in word:
            if '#' in nownode[s].keys():
                nownode = nownode[s]
            else:
                return False
        return True

def longestWord2(words: List[str]) -> str:
    t = Trie()
    for word in words:
        t.insert(word)
    longest = ""
    for word in words:
        if t.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
            longest = word
    return longest


if __name__ == "__main__":
    words = ["w","wo","wor","worl", "world"]
    print(longestWord1(words))
    print(longestWord2(words))
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(longestWord1(words))
    print(longestWord2(words))