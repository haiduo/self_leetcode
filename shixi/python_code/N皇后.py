from typing import List

#基于集合的回溯
def solveNQueens(n: int) -> List[List[str]]:
    solutions = list() #结果列表
    queens = [-1] * n  #皇后的位置
    columns = set()
    diagonal1 = set() #右斜
    diagonal2 = set() #左斜
    row = ["."] * n  #空白位置
    def generateBoard(): #生成最后的结果
        board = list()
        for i in range(n):
            row[queens[i]] = "Q"
            board.append("".join(row))
            row[queens[i]] = "."
        return board
    def backtrack(row: int):
        if row == n:
            board = generateBoard()
            solutions.append(board)
        else:
            for i in range(n):
                if i in columns or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i #当前皇后(行)的所在列
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                backtrack(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i) 
    backtrack(0)
    return solutions

if __name__ == '__main__':
    n = 4
    print(solveNQueens(n))
