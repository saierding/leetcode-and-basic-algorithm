# 240. Search a 2D Matrix II


class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        length = len(matrix[0])
        height = len(matrix)
        m, n = 0, length-1
        while m < height and n >= 0:
            if target == matrix[m][n]:
                return True
            elif target > matrix[m][n]:
                m += 1
            else:
                n -= 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
s = Solution()
print(s.searchMatrix(matrix, 20))