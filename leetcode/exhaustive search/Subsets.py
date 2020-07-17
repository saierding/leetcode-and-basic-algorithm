# 78. Subsets


class Solution:

    # 迭代
    # def subsets1(self, nums):
    #     result = [[]]
    #     for num in nums:
    #         result += [[num]+item for item in result]
    #     return result

    # 递归：[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    def subsets1(self, nums):
        if not nums:
            return [[]]
        result = self.subsets1(nums[1:])
        result += [[nums[0]] + item for item in result]
        return result


    # dfs
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    # 就是在当前index元素使用的情况下，从nums的index后面抽取0个或者全部数字放入path的后面，
    # 注意这个for循环，意义是当前元素如果使用，后面的那个元素从哪里开始，也就决定了后面的数字选择多少个。
    def subsets(self, nums):
        res = []
        tmp = []
        index = 0
        self.dfs(nums, tmp, index, res)
        return res

    def dfs(self, nums, tmp, index, res):
        res.append(tmp[:])
        for index in range(index, len(nums)):
            tmp.append(nums[index])
            self.dfs(nums, tmp, index+1, res)
            tmp.pop()


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))