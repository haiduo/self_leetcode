from typing import List

#用map和set
def isValidSudoku1(board: List[List[str]]) -> bool:
    row,col,area  = {}, {}, {}
    for i in range(9):
        row[i] = set()
        col[i] = set()
        area[i] = set() #假设一共有9个block
    for i in range(9):
        for j in range(9):
            c = board[i][j]
            if (c == '.'): continue
            u = int(c)
            k = i//3*3 + j//3 #计算当前(i,j)落在哪个block里
            if(u in row[i] or u in col[j] or u in area[k]):
                return False
            row[i].add(u)
            col[j].add(u)
            area[k].add(u)
    return True

#数组
def isValidSudoku2(board: List[List[str]]) -> bool:
    row = [[False] * 9 for _ in range(9)]
    col = [[False] * 9 for _ in range(9)]
    area = [[False] * 9 for _ in range(9)] #假设一共有9个block
    for i in range(9):
        for j in range(9):
            c = board[i][j]
            if (c == '.'): continue
            u = int(c)-1
            k = i//3*3 + j//3 #计算当前(i,j)落在哪个block里
            if (row[i][u] or col[j][u] or area[k][u]):
                return False
            row[i][u] = col[j][u] = area[k][u] = True
    return True

#位运算-类似多位独热编码
def isValidSudoku3(board: List[List[str]]) -> bool:
    row = [False]*9
    col = [False]*9
    area = [False]*9
    for i in range(9):
        for j in range(9):
            if (board[i][j] == '.'): continue
            num = 1 << int(board[i][j])
            k = i//3*3 + j//3 #计算当前(i,j)落在哪个block里
            #一旦遇到曾经遇到过的数，则该位为1，求并后还为1.转换成整数不为0
            if ((row[i] & num) != 0 or (col[j] & num) != 0 or (area[k] & num) != 0): return False
            row[i] |= num
            col[j] |= num
            area[k] |= num
    return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku1(board))
    print(isValidSudoku2(board))
    print(isValidSudoku3(board))
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku1(board))
    print(isValidSudoku2(board))
    print(isValidSudoku3(board))


