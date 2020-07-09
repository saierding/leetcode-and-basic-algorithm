# 46. Permutations


class Solution:

    # 递归遍历谁把谁拿出来然后剩下的继续递归
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            extra = nums[:i] + nums[i+1:]
            for j in self.permute(extra):
                ans.append([num]+j)

        return ans


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))