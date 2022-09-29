from typing import List

#bool的二维数组
def solveSudoku(board: List[List[str]]) -> None:
    if not board:
        return []
    row = [[False] * 9 for _ in range(len(board))] #构造行的可能性
    column = [[False] * 9 for _ in range(len(board[0]))] #构造列的可能性
    block = [[[False] * 9 for _a in range(3)] for _b in range(3)] #构造九宫格
    valid = False
    spaces = list() #存储空白格位置
    for i in range(len(board)): #对整个数独数组进行遍历
        for j in range(len(board[0])):
            if board[i][j] == ".":
                spaces.append((i, j))
            else:
                digit = int(board[i][j]) - 1
                row[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
    def dfs(pos: int):
        nonlocal valid
        if pos == len(spaces): #当空白都填充完则结束
            valid = True
            return
        i, j = spaces[pos]
        for digit in range(9):
            if row[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                row[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                row[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
            if valid: #填充玩后就提前结束
                return
    dfs(0)
    return board

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
    print(solveSudoku(board))

