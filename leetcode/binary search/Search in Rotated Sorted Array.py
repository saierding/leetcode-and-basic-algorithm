# 33. Search in Rotated Sorted Array


class Solution:

    def search(self, nums, target):
        if target not in nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


nums = [3, 1]
s = Solution()
print(s.search(nums, 1))