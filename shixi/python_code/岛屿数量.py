from typing import List


class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:  # 深度优先搜索
        def dfs(i, j):
            grid[i][j] = '0'

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == '1':
                    dfs(x, y)

        n, m = len(grid), len(grid[0])  # 行列数
        count = 0
        for i in range(n):
            for j in range(m):
                # 深搜的次数就是岛屿的个数
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

    def numIslands_bfs(self, grid: List[List[str]]) -> int:  # 广度优先搜索：
        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = "0"
            while queue:
                x, y = queue.pop(0)
                for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == "1":
                        queue.append((x, y))
                        grid[x][y] = "0"

        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count

    def numIslands_uf(self, grid: List[List[str]]) -> int:  # 并查集
        # 使用横坐标*列数+纵坐标作为元素在并查集中的唯一标识
        # 岛屿数量 = （总元素个数 - 水的个数）中的连通块的个数 = 矩阵的大小 - 水的大小 - union的次数
        class UnionFind:
            def __init__(self, n):
                # 总数
                self.rank = [0]*n  # quick union优化（权重思想)
                self.size = n
                self.p = [i for i in range(n)]
            def find(self, x):
                # 查找根节点，即当前元素所属的集合
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])  # quick find 优化
                return self.p[x]
            def union(self, a, b):
                ar, br = self.find(a), self.find(b)
                # 两个元素位于同一个集合，跳过
                if ar == br:
                    return
                # 不在同一个集合，合并
                else:
                    ###优化的###
                    if self.rank[ar] > self.rank[br]:
                        self.p[br] = ar
                    elif self.rank[ar] < self.rank[br]:
                        self.p[ar] = br
                    else:
                        self.p[ar] = br
                        self.rank[br] += 1
                    self.size -= 1  # 每合并一次，size减一次
                    ###没优化的###
                    # self.p[ar] = br
                    # self.size -= 1 #每合并一次，size减一次
        n, m = len(grid), len(grid[0])
        ocean = 0   # 统计水的个数
        uf = UnionFind(n*m)
        for i in range(n):
            for j in range(m):
                # 统计水的个数
                if grid[i][j] == "0":
                    ocean += 1
                else:
                    # 只需向右和向下查看
                    if i+1 < n and grid[i+1][j] == "1":
                        uf.union(i*m+j, (i+1)*m+j)  # 二维坐标转化为一维坐标
                    if j+1 < m and grid[i][j+1] == "1":
                        uf.union(i*m+j, i*m+(j+1))
        return uf.size - ocean

if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print('DFS：', sol.numIslands_dfs(grid))
    print('DFS：', sol.numIslands_dfs(grid1))
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print('BFS：', sol.numIslands_dfs(grid))
    print('BFS：', sol.numIslands_dfs(grid1))
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print('并查集：', sol.numIslands_dfs(grid))
    print('并查集：', sol.numIslands_dfs(grid1))
