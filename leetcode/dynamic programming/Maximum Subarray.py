# 53. Maximum Subarray


class Solution:

    # 固定起始位置
    def maxSubArray1(self, nums):
        max_sum = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur_sum = sum(nums[i:j+1])
                max_sum = max((max_sum, cur_sum))
        return max_sum

    # 动态规划
    def maxSubArray(self, nums):
        cur_sum = 0
        max_sum = float('-inf')
        for i in nums:
            # 当前的值和当前值加上之前的cur_sum的最大值
            cur_sum = max(i, cur_sum+i)
            # 当前值cur_sum和最大值max_sum的最大值
            max_sum = max(max_sum, cur_sum)
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(nums))