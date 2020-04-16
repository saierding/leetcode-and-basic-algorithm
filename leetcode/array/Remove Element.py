# 27. Remove Element


class Solution:

    def removeElement(self, nums, val):
        left = 0
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1

        return left


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))