# 80. Remove Duplicates from Sorted Array II


class Solution:

    def removeDuplicates(self, nums):
        i = 0
        index = 1
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                index += 1
                if index > 2:
                    continue
                else:
                    nums[i+1] = nums[j]
                    i += 1
            else:
                index = 1
                nums[i+1] = nums[j]
                i += 1
        return i+1


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
s = Solution()
print(s.removeDuplicates(nums))