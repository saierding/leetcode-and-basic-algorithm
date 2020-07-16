# 26. Remove Duplicates from Sorted Array


class Solution:

    # 这个题是要将nums重新排序，重复的不要，前k个数位不重复的返回k。两个指针同时走，
    # 当j=i时就把nums[i]填为j并且i往后走，要不然i不动。
    # 最后返回有多少个不重复的
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                nums[i+1] = nums[j]
                i += 1
        return i+1


nums = [1, 1, 2, 4, 4, 5]
s = Solution()
print(s.removeDuplicates(nums))