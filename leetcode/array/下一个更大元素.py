# 503. Next Greater Element II
# 输入: [1,2,1]
# 输出: [2,-1,2]


class Solution:
    def nextGreaterElements(self, nums):
        # 对于循环数组的问题一个常见的处理手段就是通过余数，
        # 然后将数组的长度扩大两倍即可
        stack, nums_len = list(), len(nums)
        res = [-1] * nums_len
        for i in range(nums_len * 2):
            while stack and nums[stack[-1]] < nums[i % nums_len]:
                res[stack.pop()] = nums[i % nums_len]
            stack.append(i % nums_len)

        return res

s = Solution()
print(s.nextGreaterElements([1,2,1]))