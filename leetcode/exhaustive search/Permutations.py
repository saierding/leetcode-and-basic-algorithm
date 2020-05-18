# 46. Permutations


class Solution:

    # 递归
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