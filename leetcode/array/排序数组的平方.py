# 977. Squares of a Sorted Array


class Solution:
    # Input: [-4, -1, 0, 3, 10]
    # Output: [0, 1, 9, 16, 100]
    def sortedSquares(self, A):
        N = len(A)
        j = 0  # i, j，表示两个指针，分别从正负界限，指向负数部分，和正数部分
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        res = []
        while 0 <= i and j < N:  # 归并操作, 谁的平方小，谁先输出
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1

        while i >= 0:  # 如果，负数部分没有输出完，则直接输出
            res.append(A[i]**2)
            i -= 1
        while j < N:  # 如果，正数部分没有输出完，则直接输出
            res.append(A[j]**2)
            j += 1

        return res