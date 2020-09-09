# 150. Evaluate Reverse Polish Notation


class Solution(object):

    # 从前往后遍历数组，遇到数字则压入栈中，遇到符号，
    # 则把栈顶的两个数字拿出来运算，把结果再压入栈中，
    # 直到遍历完整个数组，栈顶数字即为最终答案。
    # Python计算-1//2结果为-1，而在这里应该为0，所以要进行特殊的处理。

    def evalRPN(self, tokens):

        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                else:
                    if num1*num2 < 0:
                        res = -(abs(num1)//abs(num2))
                    else:
                        res = num1 // num2
                stack.append(res)
        return stack[0]