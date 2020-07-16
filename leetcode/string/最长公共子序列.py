# 1143. Longest Common Subsequence

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
class Solution:

    # dp[i][j]代表着text1的前i 个字符和text2的前j 个字符可以计算得出的最长子字符串，需要注意的是这里的i和j并不包括在内。
    # 所以动态规划的原则可以写出：
    # if text1[i-1]==text2[j-1]:
    # dp[i][j]=dp[i-1][j-1]+1
    # 否则
    # dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # 画表格很直观

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
