# 14 Longest Common Prefix


class Solution:

    def longestCommonPrefix(self, strs):
        if not strs or len(strs) <= 0:
            return ''
        result = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return result
                else:
                    continue
            result += strs[0][i]
        return result


strs = ["flower", "flow", "flight"]
strs1 = ["c", "c"]
s = Solution()
print(s.longestCommonPrefix(strs1))