# 125. Valid Palindrome（回文字符串）


class Solution:

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