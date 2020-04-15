# 151. Reverse Words in a String


class Solution:

    def reverseWords(self, str):
        if not str:
            return ''
        str_reverse = []
        str_list = str.split()
        for i in str_list:
            str_reverse.append(i)
        str_reverse = str_reverse[::-1]
        return ' '.join(str_reverse)


str = "  hello world!  "
s = Solution()
print(s.reverseWords(str))