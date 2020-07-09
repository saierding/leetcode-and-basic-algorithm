# 35. Search Insert Position


class Solution:

    # 有target输出位置，没有输出插入位置。
    # 和二分写法一样，如果没有返回left即可
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1
        return left


nums = [1, 3, 5, 6]
s = Solution()
print(s.searchInsert(nums, 2))