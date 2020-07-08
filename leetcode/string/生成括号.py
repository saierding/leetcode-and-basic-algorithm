# 22. Generate Parentheses


class Solution:

    # n = 3
    # f(i-1即2): ["()()", "(())"]
    # f(1): ["()"]
    # 我们现在要做的就是将f(1)插入到f(i-1)的所有元素中去。例如对于第一个元素结果就是
    # "()()()" "(())()" "()(())"
    def generateParenthesis(self, n):
        if n == 0:
            return list()
        if n == 1:
            return ["()"]
        res = set()
        tmp = self.generateParenthesis(n - 1)
        for s in tmp:
            for i in range(len(s)):
                tmp = s[:i] + "()" + s[i:]
                res.add(tmp)

        return list(res)


s = Solution()
print(s.generateParenthesis(2))