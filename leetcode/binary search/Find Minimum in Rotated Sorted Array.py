# 153. Find Minimum in Rotated Sorted Array


class Solution:

    def findMin(self, nums):
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]


nums = [2, 1]
s = Solution()
print(s.findMin(nums))