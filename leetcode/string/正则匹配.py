# 10. Regular Expression Matching


class Solution:

    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        if p_len == 0:
            return s_len == 0
        # 首先判断len(p)>1 and p[1]=="*"，如果是的话，说明*在p的第二位，
        # 判断s[0]和p[0]能否匹配，如果可以匹配的话，继续判断isMatch(s[1:], p)
        # （也就是*匹配了一次，我们会继续使用.*或者?*去参与比较），
        # 同时需要判断isMatch(s,p[2:])是不是成立（也就是*表示匹配0次）
        if p_len > 1 and p[1] == "*":
            if s_len != 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            # 如果上述条件不成立，需判断isMatch(s, p[2:])
            # 是不是成立（也就是 * 表示匹配0次），因为此时也可能匹配0次
            else:
                return self.isMatch(s, p[2:])
        # 如果*不在p的第二位，就要判断s[0]和p[0]能否匹配。
        else:
            return s_len != 0 and (s[0] == p[0] or p[0] == '.') \
                   and self.isMatch(s[1:], p[1:])


ss = "aab"
p = "c*a*b"
s = Solution()
print(s.isMatch(ss,p))


