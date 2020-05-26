# 55. Jump Game


class Solution:

    # 自底向上贪心算法
    def canJump(self, nums):
        m = 0
        for i, num in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+num)
        return True


s = Solution()
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))