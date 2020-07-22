# 13. Roman to Integer
# Input: "IV"
# Output: 4


class Solution:

    def romanToInt(self, s):
        s_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, pre = 0, 0
        for i in s:
            cur = s_dict[i]
            # 如果cur>pre，减去两个pre用来弥补
            if pre < cur:
                res += (cur - 2*pre)
            else:
                res += cur
            pre = cur
        return res

