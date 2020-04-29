# 74. Search a 2D Matrix


class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        length = len(matrix[0])
        height = len(matrix)
        left, right = 0, length*height
        while left < right:
            mid = (left+right)//2
            m, n = mid//length, mid%length
            if target == matrix[m][n]:
                return True
            elif target > matrix[m][n]:
                left = mid + 1
            else:
                right = mid
        return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
s = Solution()
print(s.searchMatrix(matrix, 3))