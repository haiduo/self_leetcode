
import collections
from typing import List

#广度优先搜索
def floodFill1(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    currColor = image[sr][sc]
    if currColor == newColor:
        return image
    n, m = len(image), len(image[0])
    que = collections.deque([(sr, sc)])
    image[sr][sc] = newColor
    while que:
        x, y = que.popleft()
        for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                que.append((mx, my))
                image[mx][my] = newColor
    return image

#深度优先搜索
def floodFill2(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    n, m = len(image), len(image[0])
    currColor = image[sr][sc]
    def dfs(x: int, y: int):
        if image[x][y] == currColor:
            image[x][y] = newColor
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                    dfs(mx, my)
    if currColor == newColor:
        return image
    else:
        dfs(sr, sc)
    return image

if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(floodFill1(image, sr, sc, newColor))
    print(floodFill2(image, sr, sc, newColor))