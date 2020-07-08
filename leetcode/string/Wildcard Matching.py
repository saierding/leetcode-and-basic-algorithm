# 44. Wildcard Matching


class Solution:

    # 如果string[i]和pattern[i]一样或者pattern[i]
    # 为？那么往下走即可，如果出现了*符号，记住当前的i，j状态并让pattern继续往下走,走错了返回来
    # j往下走i也往下走以此类推。
    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        i, j, star, i_index = 0, 0, -1, 0
        while i < s_len:
            if j < p_len and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                j += 1
                i_index = i
            elif star != -1:
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False

        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len


s = "acdcb"
p = "a*c?b"
so = Solution()
print(so.isMatch(s, p))