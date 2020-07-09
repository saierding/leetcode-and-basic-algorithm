# 34. Find First and Last Position of Element in Sorted Array


class Solution:

    # 二分算法找到mid后如果target在前面再继续往前找，中间值存储为
    # result0即可，如果target在后面再继续往后找，中间值存储为result1.
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