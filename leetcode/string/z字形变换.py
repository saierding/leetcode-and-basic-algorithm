# 6. ZigZag Conversion


class Solution:
    # LEETCODEISHIRING
    # ↑
    # l1: L
    # l2: E T
    # l3: E
    # 我们就将L添加到第一行。接着我们碰到E，我们将它添加到第二行。
    # 接着我们碰到第二个E，我们将它添加到第三行。此时我们已经完成一次操作了，我们要折返回去，
    # 也就是回到第二行了（我们可以通过一个变量实现这个功能）。我们将T添加到第二行。以此类推

    def convert(self, s, numRows):

        if numRows == 1:
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)