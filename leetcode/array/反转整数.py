# 7. Reverse Integer


class Solution:
    # Input: 123
    # Output: 321
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x > 0:
            neg = 1
        else:
            neg = -1
        nums = 0
        # 全部变成正数
        x *= neg

        while x:
            nums = nums * 10 + x % 10
            x //= 10
        nums *= neg
        if nums > (2 ** 31) - 1 or nums < -1 * (2 ** 31):
            return 0
        return nums


s = Solution()
print(s.reverse(123))
