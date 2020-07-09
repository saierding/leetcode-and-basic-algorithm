# 66. Plus One


class Solution:

    # 从后往前判断，如果是9，变0。否则直接加1返回。
    # 9进一的话在nums[0]insert一个1
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





