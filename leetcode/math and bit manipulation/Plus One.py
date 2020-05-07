# 66. Plus One


class Solution:

    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1

        digits.insert(0, 1)
        return digits


nums = [9, 9]
s = Solution()
print(s.plusOne(nums))





