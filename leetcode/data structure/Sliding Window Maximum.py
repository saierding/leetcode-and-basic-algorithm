# 239. Sliding Window Maximum


class Solution:

    def maxSlidingWindow(self, nums, k):
        if not nums:
            return
        stack, res = [], []
        for i, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            stack.append(i)

            if i - stack[0] >= k:
                stack.pop(0)

            if i >= k-1:
                res.append(nums[stack[0]])

        return res
