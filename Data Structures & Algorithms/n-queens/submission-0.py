from typing import List

class Solution:
    def is_legal(self, board: List[int], x: int) -> bool:
        for x_other in range(x):
            if (board[x] == board[x_other])\
                or (x - x_other == abs(board[x] - board[x_other])):
                    return False
        return True
    
    def recNQueens(
        self, 
        boards: List[List[int]], 
        x: int, 
        board: List[int], 
        size: int) -> bool:
        if x == size:
            boards.append(board.copy())
            return True
        else:
            for y in range(size):
                board[x] = y
                if self.is_legal(board, x):
                    self.recNQueens(boards, x+1, board, size)
            return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        board = [-1] * n
        self.recNQueens(boards, 0, board, n)

        ans = []
        for board in boards:
            tmp = [['.'] * n for _ in range(n)]
            for x in range(n):
                y = board[x]
                tmp[x][y] = 'Q'
            ans.append([''.join(row) for row in tmp])
        return ans