class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                b_row, b_col = r//3, c//3
                box = (b_row) * 3 + (b_col)
                val = board[r][c]

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)
        return True