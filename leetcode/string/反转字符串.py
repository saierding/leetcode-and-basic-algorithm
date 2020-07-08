# 344. Reverse String


class Solution:

    def reverseString(self, s):

        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)


s = Solution()
print(s.reverseString(["h","e","l","l","o"]))