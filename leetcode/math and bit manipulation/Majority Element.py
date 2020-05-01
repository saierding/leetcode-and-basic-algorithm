# 169. Majority Element


class Solution:

    # 老方法
    def majorityElement1(self, nums):
        nums.sort()
        mid = len(nums)//2
        return nums[mid]

    # 两两抵消
    def majorityElement(self, nums):
        net_count = 0
        cur = 0
        for i in nums:
            if net_count == 0:
                net_count += 1
                cur = i
            elif cur == i:
                net_count += 1
            else:
                net_count -= 1
        return cur


nums = [6, 5, 5]
s = Solution()
print(s.majorityElement(nums))