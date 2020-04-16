# 189. Rotate Array


class Solution:

    def rotate(self, nums, k):
        length = len(nums)
        nums = nums[length-k:]+nums[:length-k]
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
print(s.rotate(nums, k))