# 36. Valid Sudoku


class Solution:

    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    seen.append((i, digit))
                    seen.append((digit, j))
                    seen.append((i//3, j//3, digit))
        return len(seen) == len(set(seen))
