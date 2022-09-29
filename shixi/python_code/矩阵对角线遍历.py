import numpy as np

def findDiagonalOrder(mat): # 按照左上角打印，S型遍历
    ans = []
    m, n = len(mat), len(mat[0])
    for i in range(m + n - 1):
        if i % 2: #奇数列
            x = 0 if i < n else i - n + 1   #行从小到大
            y = i if i < n else n - 1       #列从大到小
            while x < m and y >= 0:
                ans.append(mat[x][y])
                x += 1
                y -= 1
        else:   #偶数列
            x = i if i < m else m - 1      #行从大到小
            y = 0 if i < m else i - m + 1  #列从小到大
            while x >= 0 and y < n:
                ans.append(mat[x][y])
                x -= 1
                y += 1
    return ans

#方法二 思路较为简单
def findDiagonalOrder_1(arr): # 按照右上角打印，S型遍历
    m, n = arr.shape
    ret = []
    for row in list(range(m+n-1)):
        # 反转元素的开始位置
        ret_count = len(ret)
        # i, j 每个对角线的开始位置
        i = row if row < m else m-1
        j = n-1 if row < m else (m+n-1) -row -1
        # 获取每条对角线上的元素
        while i>= 0 and j>=0:
            ret.append(arr[i][j])
            i -= 1
            j -= 1
        # 偶数行顺序反转 注释掉下面的if语句就是同一方向遍历
        if row % 2 == 0:
            ret = ret[: ret_count] + ret[ret_count:][: : -1]
    return ret

#方法二 思路较为简单
def findDiagonalOrder_2(arr): # 按照左上角打印，S型遍历
    m, n = arr.shape
    ret = []
    for row in list(range(m+n-1)):
        # 反转元素的开始位置
        ret_count = len(ret)
        # i, j 每个对角线的开始位置
        i = row if row < m else m-1
        j = 0 if row < m else n - ((m+n-1) - row)
        # 获取每条对角线上的元素
        while i>= 0 and j<=n-1:
            ret.append(arr[i][j])
            i -= 1
            j += 1
        # 偶数行顺序反转 注释掉下面的if语句就是同一方向遍历
        if row % 2 == 0:
            ret = ret[: ret_count] + ret[ret_count:][: : -1]
    return ret

if __name__ == '__main__':
    mat = [
        [1, 2, 3, 9],
        [4, 5, 6, 6],
        [7, 8, 9, 9]
    ]
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    print(findDiagonalOrder(mat))
    print(findDiagonalOrder(mat1))
    arr = np.array([
        [1, 2, 3, 9],
        [4, 5, 6, 6],
        [7, 8, 9, 9]
    ])
    arr1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])
    print(findDiagonalOrder_1(arr))
    print(findDiagonalOrder_2(arr1))
