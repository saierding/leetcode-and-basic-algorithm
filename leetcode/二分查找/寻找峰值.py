# 162. Find Peak Element


class Solution:

    # 这个题是用数学定理，如果mid比相邻的左边的小，峰值在左边，
    # 如果mid比相邻的右边的小，峰值在右边。
    def findPeakElement(self, nums):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid - 1]:
                r = mid
            elif nums[mid] < nums[mid + 1]:
                l = mid
            else:
                return mid
        mid = l if nums[l] > nums[r] else r
        return mid


nums = [1, 2, 1, 3, 5, 6, 4]
s = Solution()
print(s.findPeakElement(nums))