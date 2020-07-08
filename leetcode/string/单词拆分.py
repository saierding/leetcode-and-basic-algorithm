# 139. Word Break


class Solution:

    # i遍历s，j标记断点
    def wordBreak(self, s, wordDict):
        result = [False]*(len(s)+1)
        result[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if result[i] and s[i:j+1] in wordDict:
                    result[j+1] = True
        return result[-1]


s = "applepenapple"
word = ["apple", "pen"]
so = Solution()
print(so.wordBreak(s, word))