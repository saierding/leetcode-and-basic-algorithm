# 14 Longest Common Prefix


class Solution:

    # 用一个二维数组解决，str[i][j]，i用来存第几个字母，j用来存
    # 字母的第几个数，以第一个字母为基准开始循环即可。
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
print(s.longestCommonPrefix(strs))