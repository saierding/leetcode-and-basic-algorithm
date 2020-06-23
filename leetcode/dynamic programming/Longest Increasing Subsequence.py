# 300. Longest Increasing Subsequence


class Solution:

    # [1, 1, 1, 1, 1]然后每次迭代增加
    # [1, 2, 2, 1, 2]
    # [1, 2, 3, 1, 3]
    # [1, 2, 3, 1, 4]
    # [1, 2, 3, 1, 4] max(2, 4)
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        result = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    result[j] = max(result[i]+1, result[j])
        return max(result)


nums = [1, 2, 3, 0, 4]
s = Solution()
print(s.lengthOfLIS(nums))