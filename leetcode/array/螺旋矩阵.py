# 54. Spiral Matrix


class Solution:

    # 向下表示y正方向，向右表示x正方向。我们再定义两个点，
    # 分别是左上x1,y1和右下x2,y2，这样我们每循环一次将x1++,
    # y1++并且x2--,y2--。我们每次循环的策略采用下面的这种
    def spiralOrder(self, matrix):
        result = list()
        if not matrix:
            return result
        r, c = len(matrix), len(matrix[0])
        x1, y1, x2, y2 = 0, 0, c - 1, r - 1
        while x1 <= x2 and y1 <= y2:
            for i in range(x1, x2 + 1):
                result.append(matrix[y1][i])

            for j in range(y1 + 1, y2 + 1):
                result.append(matrix[j][x2])
            if x1 < x2 and y1 < y2:
                for i in range(x2 - 1, x1, -1):
                    result.append(matrix[y2][i])

                for j in range(y2, y1, -1):
                    result.append(matrix[j][x1])

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1

        return result
