# 125. Valid Palindrome（回文字符串）


class Solution:

    # 因为牵扯大小写和非数字字母输入，while判断左右，两边同
    # 时往中间靠，这里学习到s.isalnum()判断是否为数字字母，s.islower()判断左右是否相同。
    def isPalindrome(self, s):
        if not s:
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


str = 'A man, a plan, a canal: Panama'
s = Solution()
print(s.isPalindrome(str))