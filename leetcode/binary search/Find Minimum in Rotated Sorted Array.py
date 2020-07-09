# 153. Find Minimum in Rotated Sorted Array


class Solution:

    # 这个题求反转后的有序数列的最小值。如果mid比right小的话，最小值肯定在左边（包含mid），要不然肯定在右边（不包含mid),
    # 最后剩下了left和right，哪个大返回哪个。
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