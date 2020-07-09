# 136. Single Number


class Solution:

    # 老办法就是dict得出所有的数和对应的个数。然后遍历找到个数为1的
    def singleNumber1(self, nums):
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict.keys():
                dict[nums[i]] = 0
            dict[nums[i]] += 1
        for i in dict:
            if dict[i] == 1:
                return i

    # 这里用位方法，特性是两个相同的数异或得0，
    # 0异或任何数得任何数本身，所以直接全部异或即可。
    def singleNumber(self, nums):
        x = 0
        for i in nums:
            x ^= i
        return x


nums = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))