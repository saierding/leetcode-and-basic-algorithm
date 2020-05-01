# 263. Ugly Number


class Solution:

    def isUgly(self, num):
        for p in [2, 3, 5]:
            while num and num % p == 0:
                num //= p
        return num == 1


s = Solution()
print(s.isUgly(7))