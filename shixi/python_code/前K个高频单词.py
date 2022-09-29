import collections
import heapq
from typing import List

'''哈希+排序'''
def topKFrequent1(words: List[str], k: int) -> List[str]: 

    #记录每个单词出现的次数
    hash = collections.Counter(words) 
    #词频倒序排列，若词频相同，按字母顺序排序 正序排列
    res = sorted(hash, key=lambda key:(-hash[key], key)) #（reverse=True 即将sorted方法修改为倒序排列）
    return res[:k]

'''哈希+优先队列（小顶堆） O(nlogk)'''
class Node:
    def __init__(self, key, val):
        self.key = key #单词
        self.val = val #频率
    def __lt__(self, other):
        return self.key>other.key if self.val == other.val else self.val < other.val

def topKFrequent2(words: List[str], k: int) -> List[str]:
    # cnt = {} #实现mapping
    # for word in words:
    #     if word not in cnt: 
    #         cnt[word] = 0 
    #     cnt[word] = cnt[word]+1

    cnt = collections.Counter(words)
    heap = []
    # print(cnt)
    for key, val in cnt.items():
        heapq.heappush(heap, Node(key, val)) #添加元素自动调用__lt__()函数比较
        if len(heap) > k:
            heapq.heappop(heap)

    heap.sort(reverse=True)
    return [x.key for x in heap]


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(topKFrequent1(words, k))
    print(topKFrequent2(words, k))
