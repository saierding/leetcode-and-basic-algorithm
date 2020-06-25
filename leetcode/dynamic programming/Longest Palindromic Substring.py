# 5. Longest Palindromic Substring(最大回文子序列)


class Solution:

    # 笨办法穷举所有子字符串
    # def longestPalindrome(self, s):
    #     if not s:
    #         return ''
    #     substring = []
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             substring.append(s[i:j+1])
    #     longest = 0
    #     result = []
    #     for i in range(len(substring)):
    #         if self.ispalindrome(substring[i]) and len(substring[i]) >= longest:
    #             longest = len(substring[i])
    #             result.append(substring[i])
    #     output = []
    #     for i in result:
    #         if len(i) == longest:
    #             output.append(i)
    #     return output
    #
    # def ispalindrome(self, s):
    #     if not s:
    #         return False
    #     return s == s[::-1]

    def longestPalindrome(self, s):

        if len(s) < 2 or s == s[::-1]:
            return s
        start, maxlength = 0, 1
        for i in range(len(s)):
            # 在发现一个新的回文时，比如'aca'，这是遍历到了下一个'b'就插'bacab'和'acab'这两个新的就可以了
            # 即下面的odd 和 even
            odd = s[i - maxlength - 1:i + 1]
            even = s[i - maxlength:i + 1]
            if i - maxlength - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlength - 1
                maxlength += 2
            elif i - maxlength >= 0 and even == even[::-1]:
                start = i - maxlength
                maxlength += 1
        return s[start:start + maxlength]


string = 'bacabd'
s = Solution()
print(s.longestPalindrome(string))