# 53. Maximum Subarray


class Solution:

    # 可以固定起始位置，可以直接动态规划。

    # def maxSubArray(self, nums):
    #     maxnum = float('-inf')
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             sumnum = sum(nums[i:j+1])
    #             maxnum = max(sumnum, maxnum)
    #     return maxnum

    def maxSubArray(self, nums):
        curnum = 0
        maxnum = float('-inf')
        for i in nums:
            curnum = max(curnum+i, i)
            maxnum = max(maxnum, curnum)
        return maxnum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))