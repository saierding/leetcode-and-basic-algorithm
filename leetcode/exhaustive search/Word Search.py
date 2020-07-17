# 79. Word Search


class Solution:

    # 全局找起始点和调用dfs
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(i, j, board, word, 0):
                    return True
        return False

    # dfs,前后左右分别找是否满足
    def helper(self, i, j, board, word, index):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
            return False

        board[i][j] = 'visited'

        dfs = self.helper(i-1, j, board, word, index+1) or self.helper(i, j-1, board, word, index+1) \
              or self.helper(i+1, j, board, word, index+1) or self.helper(i, j+1, board, word, index+1)

        board[i][j] = word[index]
        return dfs

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.