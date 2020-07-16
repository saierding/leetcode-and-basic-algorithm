# 8. String to Integer (atoi)

# Input: "   -42"
# Output: -42
class Solution:

    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        length = len(s)
        if length == 0 or s[0] not in '0123456789+-':
            return 0
        index = 1
        while index < length and s[index].isdigit():
            index += 1
        if index == 1 and s[0] in '+-':
            return 0
        result = int(s[:index])
        if result < 0:
            return max(-2147483648, result)
        else:
            return min(2147483647, result)