#超大的数组:通过空间换时间
class MyHashSet1:
    def __init__(self):
        self.hashset = [False]*1000001

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key]

# 定长拉链数组；就是把 HashSet 设计成一个 M * NM∗N 的二维数组
class MyHashSet2:
    def __init__(self):
        self.buckets = 1000 #计算hash分桶
        self.itemsPerBucket = 1001 #key存放具体的位置
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def pos(self, key):
        return key // self.buckets
    
    def add(self, key):
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1
        
    def remove(self, key):
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key) -> bool:
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)

# 不定长拉链数组:根据分桶中的 key 动态增长，更类似于真正的链表
class MyHashSet3:
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)
        
    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]


if __name__ == "__main__":
    obj = MyHashSet1()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.remove(1)
    print(obj.contains(1))
    print(obj.contains(2))
    obj = MyHashSet2()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.remove(1)
    print(obj.contains(1))
    print(obj.contains(2))
    obj = MyHashSet3()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.remove(1)
    print(obj.contains(1))
    print(obj.contains(2))