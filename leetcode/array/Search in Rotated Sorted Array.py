# 33. Search in Rotated Sorted Array


class Solution:

    # 旋转过的array找val存在的位置，还是用二分法找，注意这道题的边界值
    def search(self, nums, target):
        if target not in nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid-1
        return -1


nums = [3, 1]
nums1 = [4, 5, 6, 7, 0, 1, 2]
target = 0
s = Solution()
print(s.search(nums1, target))