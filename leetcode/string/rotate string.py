# 796. Rotate String


class Solution:

    # 如果b由a旋转而得，b就一定是a+a的
    # 子字符串，通过判断b in a+a判断而得。
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A + A


a = "bbbacddceeb"
b = "ceebbbbacdd"
A = 'abcde'
B = 'cdeab'
s = Solution()
print(s.rotateString(a, b))
