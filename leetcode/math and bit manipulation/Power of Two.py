# 231. Power of Two

class Solution:

    # 笨办法直接循环到这个数，用2的n次方去判断。
    def isPowerOfTwo1(self, n):
        i = 0
        while i < n:
            if 2 ** i == n:
                return True
            elif 2 ** i > n:
                return False
            i += 1
        return False

    # bit, 位方法，2的次方有特性，和比他小一个的数
    # 位与得到0。n和n-1位与得到的就是0
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        if n & n-1 == 0:
            return True
        return False


s = Solution()
print(s.isPowerOfTwo(32))