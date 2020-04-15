# 796. Rotate String


class Solution:

    def rotateString(self, A, B):
        return len(A) == len(B) and B in A + A


a = "bbbacddceeb"
b = "ceebbbbacdd"
A = 'abcde'
B = 'cdeab'
s = Solution()
print(s.rotateString(a, b))
