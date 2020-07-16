# 27. Remove Element


class Solution:

    # 这个题是把值为val的去掉，重新排列nums,nums前面为去掉val后的nums。
    # 与上面思路相似双指针，一个遍历，一个left计数，遇到不同的left++并
    # 改写nums[left]。
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