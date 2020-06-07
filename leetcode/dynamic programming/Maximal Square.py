# 221. Maximal Square


class Solution:

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*cols for row in range(rows)]

        for row in range(rows):
            dp[row][0] = int(matrix[row][0])

        for col in range(cols):
            dp[0][col] = int(matrix[0][col])

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == '0':
                    dp[row][col] = int(matrix[row][col])
                else:
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
        return max(map(max, dp)) ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
print(s.maximalSquare(matrix))










