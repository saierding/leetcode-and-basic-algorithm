# 69. Sqrt(x)


class Solution:

    def mySqrt(self, x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        l, r = 1, x
        while l+1 < r:
            mid = (l+r)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid
            else:
                l = mid
        return l


s = Solution()
print(s.mySqrt(8))