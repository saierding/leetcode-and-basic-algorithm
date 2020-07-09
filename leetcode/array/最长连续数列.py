# 128. Longest Consecutive Sequence


class Solution:

    # 先找到最小的数，然后递增到不存在
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


nums = [100, 4, 200, 1, 3, 2]
s = Solution()
print(s.longestConsecutive(nums))