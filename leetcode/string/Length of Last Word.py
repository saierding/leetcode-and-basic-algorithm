# 58. Length of Last Word


class Solution:

    def lengthOfLastWord(self, str):
        # if not str:
        #     return 0
        # str_list = str.split(' ')
        # for i in range(len(str_list)-1, -1, -1):
        #     if str_list[i] == '':
        #         continue
        #     else:
        #         return len(str_list[i])
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