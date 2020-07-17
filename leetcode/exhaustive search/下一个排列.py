# 31. Next Permutation
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    # 1  5  6  4  3  2  1
    # 1  6  1  2  3  4  5
    def nextPermutation(self, nums):
        i = j = r = len(nums) - 1
        # 定义一个右指针i，向左移，找到第一个数下降位置
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        if i >= 0:
            # 定义一个右指针j，从j向i找第一个大于nums[i]的位置
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            # 交换nums[i]和nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        # 接着将nums[i+1:]的元素reverse即可
        while i < r:
            nums[i], nums[r] = nums[r], nums[i]
            i += 1
            r -= 1


