# 15. 3Sum


class Solution:

    # 遍历数组，在每个循环中target就是-nums[i], 然后转化为two sum
    def threeSum(self, nums):
        results = []
        nums_len = len(nums)
        if nums_len < 3:
            return results
        nums.sort()
        for i in range(nums_len):
            target = 0 - nums[i]
            nums_dict = {}
            for j in range(i+1, nums_len):
                diff = target - nums[j]
                if diff in nums_dict:
                    result = [nums[i], diff, nums[j]]
                    if result not in results:
                        results.append(result)
                nums_dict[nums[j]] = j
        return results


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))