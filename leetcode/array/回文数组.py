# 9. Palindrome Number


class Solution:

    # int 转 string解决
    # def isPalindrome1(self, x):
    #     strx = str(x)
    #     return strx == strx[::-1]

    # 将数字倒过来比较
    # 每次把数除以10，取10的余数然后
    # 加上temp，然后temp每次乘10加余数
    def isPalindrome(self, x):
        temp = x
        ans = 0
        while temp > 0:
            ans = ans * 10 + temp % 10
            temp //= 10
        return ans == x


s = Solution()
print(s.isPalindrome(121))