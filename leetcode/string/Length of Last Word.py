# 58. Length of Last Word


class Solution:

    def lengthOfLastWord(self, str):
        if str is None:
            return 0
        last_word = str.split()
        if last_word:
            return len(last_word[-1])
        else:
            return 0


string = " "
str2 = "Hello World"
s = Solution()
print(s.lengthOfLastWord(str2))