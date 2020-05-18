# 78. Subsets


class Solution:

    # 迭代
    def subsets1(self, nums):
        result = [[]]
        for num in nums:
            result += [[num]+item for item in result]
        return result

    # 递归
    def subsets(self, nums):
        if not nums:
            return [[]]
        result = self.subsets(nums[1:])
        result += [[nums[0]] + item for item in result]
        return result


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))