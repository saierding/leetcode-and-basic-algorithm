# 242. Valid Anagram


class Solution:

    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False


so = Solution()
s = "anagram"
t = "nagaram"
print(so.isAnagram(s, t))