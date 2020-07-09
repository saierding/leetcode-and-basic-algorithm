# 263. Ugly Number


class Solution:

    # 对每一个丑数循环，循环里面如果余这个丑数为0
    # 就一直除以这个丑数，最后得到1就说明是丑数
    def isUgly(self, num):
        for p in [2, 3, 5]:
            while num and num % p == 0:
                num //= p
        return num == 1


s = Solution()
print(s.isUgly(7))