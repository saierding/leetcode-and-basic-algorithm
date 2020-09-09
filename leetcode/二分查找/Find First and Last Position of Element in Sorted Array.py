# 34. Find First and Last Position of Element in Sorted Array


class Solution:

    def searchRange(self, nums, target):
        l, r = 0, len(nums)
        result = [-1, -1]
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    result[0] = mid
                r = mid
            else:
                l = mid + 1

        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    result[1] = mid
                l = mid + 1
            else:
                r = mid
        return result


nums = [5, 7, 7, 7, 8, 8, 10]
s = Solution()
print(s.searchRange(nums, 8))