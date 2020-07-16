# 32. Longest Valid Parentheses

# Input: "(()"
# Output: 2
class Solution:

    # 首先遍历一遍s，判断遍历到的字符ch是不是(，如果是的话，我们就将此时ch的位置加入到栈中
    # 如果遍历到的元素是)，栈不为空且栈顶元素是(，我们就出栈。
    # 这样扫描完一轮，我们的栈里面存放的就是没有匹配到的位置。
    # 最后还需考虑如果栈为空，那么当前的最长匹配就是当前指针位置+1；
    # 如果不为空，那么最长匹配就是当前指针位置减去栈顶元素位置。
    def longestValidParentheses(self, s: str) -> int:
        s_len, stack = len(s), list()
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        if not stack:
            return s_len
        print(stack)
        stack = [-1] + stack + [s_len]
        for i, val in enumerate(stack[1:]):
            stack[i] = val - stack[i] - 1
        return max(stack[:-1])


s = Solution()
print(s.longestValidParentheses("()(()"))