# 1. Two Sum


class Solution:

    # 这里用dict，key存数，value存位置，如果target-key在key里
    # 那么返回value即可。
    def twoSum(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[nums[i]] = i
        return []


nums = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(nums, 9))