# 136. Single Number


class Solution:

    # old approach
    def singleNumber1(self, nums):
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict.keys():
                dict[nums[i]] = 0
            dict[nums[i]] += 1
        for i in dict:
            if dict[i] == 1:
                return i

    # bit
    def singleNumber(self, nums):
        x = 0
        for i in nums:
            x ^= i
        return x


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))