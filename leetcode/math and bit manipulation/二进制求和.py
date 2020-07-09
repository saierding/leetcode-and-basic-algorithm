# 67. Add Binary


class Solution:

    def addBinary(self, a, b):

        res = list()
        add, l1, l2 = 0, len(a), len(b)
        while add or l1 or l2:
            if l1:
                l1 -= 1
                add += int(a[l1])
            if l2:
                l2 -= 1
                add += int(b[l2])
            res.append(str(add & 1))
            add >>= 1

        return ''.join(reversed(res))


a = "11"
b = "1"
s = Solution()
print(s.addBinary(a,b))