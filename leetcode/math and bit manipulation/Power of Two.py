# 231. Power of Two

class Solution:

    # 笨办法
    def isPowerOfTwo1(self, n):
        i = 0
        while i < n:
            if 2 ** i == n:
                return True
            elif 2 ** i > n:
                return False
            i += 1
        return False

    # bit, n和n-1位与得到的就是0
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        if n & n-1 == 0:
            return True
        return False


s = Solution()
print(s.isPowerOfTwo(32))