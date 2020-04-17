# 16. 3Sum Closest


class Solution:

    def threeSumClosest(self, nums, target):
        nums_len = len(nums)
        nums.sort()
        closest_num = 1000000
        for i in range(nums_len-2):
            left, right = i+1, nums_len-1
            while left < right:
                min_num = nums[i] + nums[left] + nums[right] - target
                if abs(min_num) < abs(closest_num):
                    closest_num = min_num
                if abs(min_num) == 0:
                    return target
                elif min_num < 0:
                    left += 1
                elif min_num > 0:
                    right -= 1
        return closest_num + target


nums = [-1, 2, 1, -4]
s = Solution()
print(s.threeSumClosest(nums, 1))