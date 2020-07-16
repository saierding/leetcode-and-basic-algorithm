# 20. Valid Parentheses

# Input: "()[]{}"
# Output: true
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
            elif char == ')':
                temp = '('
            elif char == '}':
                temp = '{'
            elif char == ']':
                temp = '['
            else:
                return False
            # print(stack,temp)
            if stack:
                if stack[-1] == temp:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) != 0:
            return False
        return True

s = Solution()
print(s.isValid("()[]{}"))
