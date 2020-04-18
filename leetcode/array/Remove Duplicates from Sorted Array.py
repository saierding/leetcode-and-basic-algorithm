# 26. Remove Duplicates from Sorted Array


class Solution:

    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                nums[i+1] = nums[j]
                i += 1
        return i+1


nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))