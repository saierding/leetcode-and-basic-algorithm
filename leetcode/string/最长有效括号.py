# 32. Longest Valid Parentheses


class Solution:

    # 首先遍历一遍s，判断遍历到的字符ch是不是(，如果是的话，我们就将此时c的位置加入到栈中
    # 如果遍历到的元素是)，栈不为空且栈顶元素是(，我们就出栈。
    # 这样扫描完一轮，我们的栈里面存放的就是没有匹配到的位置。
    # 最后还需考虑如果栈为空，那么当前的最长匹配就是当前指针位置+1；
    # 如果不为空，那么最长匹配就是当前指针位置减去栈顶元素位置。
    def longestValidParentheses(self, s: str) -> int:
        res, st = 0, []
        for i, c in enumerate(s):
            if st:
                if s[st[-1]] == '(' and c == ')':
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)

            if st:
                res = max(res, i - st[-1])
            else:
                res = max(res, i + 1)
        return res
