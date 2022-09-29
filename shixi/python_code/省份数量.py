import collections
from typing import List

#深度优先搜索
def findCircleNum1(isConnected: List[List[int]]) -> int:
    def dfs(i: int):
        for j in range(cities):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                dfs(j)
    cities = len(isConnected)
    visited = set()
    provinces = 0
    for i in range(cities):
        if i not in visited:
            dfs(i)
            provinces += 1
    return provinces

#广度优先搜索
def findCircleNum2(isConnected: List[List[int]]) -> int:
    cities = len(isConnected)
    visited = set()
    provinces = 0
    for i in range(cities):
        if i not in visited:
            Q = collections.deque([i])
            while Q:
                j = Q.popleft()
                visited.add(j)
                for k in range(cities):
                    if isConnected[j][k] == 1 and k not in visited:
                        Q.append(k)
            provinces += 1
    return provinces

#并查集-父亲节点数组实现
def findCircleNum3(isConnected: List[List[int]]) -> int:
    cities = len(isConnected)
    parent = list(range(cities))

    def find(index: int) -> int:         #查找
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]

    def union(index1: int, index2: int): #合并
        parent[find(index1)] = find(index2)

    for i in range(cities):
        for j in range(i + 1, cities):
            if isConnected[i][j] == 1:
                union(i, j)
    provinces = sum(parent[i] == i for i in range(cities))
    return provinces

#并查集-字典-树结构的实现
class UnionFind:
    def __init__(self):
        self.father = {}  #记录每个节点的父节点
        self.num_of_sets = 0  #记录集合的数量

    def find(self,x):#查找根节点
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root: #路径压缩，把树的深度固定为二
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def union(self,x,y):#合并两个节点
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1  #集合的数量-1
    
    def add(self,x):#添加新节点
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1  #集合的数量+1

def findCircleNum4(isConnected: List[List[int]]) -> int:
    uf = UnionFind()
    for i in range(len(isConnected)):
        uf.add(i)
        for j in range(i):
            if isConnected[i][j]:
                uf.union(i,j)
    return uf.num_of_sets

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(findCircleNum1(isConnected))
    print(findCircleNum2(isConnected))
    print(findCircleNum3(isConnected))
    print(findCircleNum4(isConnected))