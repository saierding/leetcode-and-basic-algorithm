# 55. Jump Game


class Solution:

    # 自底向上贪心算法
    def canJump(self, nums):
        m = 0
        for i, num in enumerate(nums):
            # 如果到i不了m的位置那就直接false因为就停在i不能继续往下走了
            # 全部轮一遍过了就true了
            if i > m:
                return False
            m = max(m, i+num)
        return True


s = Solution()
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))