# 415. Add Strings


class Solution(object):

    # 从末尾开始向前以次相加，注意进位，两个数的相加最多只能进1，因此只要一个boolean 型的量表示是否进位即可。
    # 提前进行补零，这样能够使得两个数字长度一样，方便了计算。
    def addStrings(self, num1, num2):

        res = ""
        carry = 0
        M, N = len(num1), len(num2)
        if M < N:
            num1 = "0" * (N - M) + num1
        else:
            num2 = "0" * (M - N) + num2
        N = max(M, N)
        for i in range(N - 1, -1, -1):
            add = int(num1[i]) + int(num2[i]) + carry
            if add >= 10:
                carry = 1
                add -= 10
            else:
                carry = 0
            res = str(add) + res
        if carry:
            res = "1" + res
        return res
