# 560. Subarray Sum Equals K

# Input:nums = [1,1,1], k = 2
# Output: 2
class Solution:

    # 每次计算[i,len(nums)]这个区间内以i开始的每个小区间的和，
    # 记录所有和为k的区间个数。通过遍历nums每个元素i，
    # 我们就可以求解出每个以i开始并且和为k的区间个数，最后加在一起即可。
    # O(n2)
    def subarraySum(self, nums, k):
        nums_len, result = len(nums), 0
        for i in range(nums_len):
            cur_sum = 0
            for j in range(i, nums_len):
                cur_sum += nums[j]
                if cur_sum == k:
                    result += 1

        return result

    # O(n)
    # 使用一个字典保存数组某个位置之前的数组和，然后遍历数组求和，
    # 这样当我们求到一个位置的和的时候，向前找sum-k是否在数组中，
    # 如果在的话，更新结果为之前的结果+(sum-k出现的次数)。同时，当前这个sum出现的次数就多了一次。
    def subarraySum1(self, nums, k: int) -> int:
        import collections
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res,d


nums = [1,1,1]
s = Solution()
print(s.subarraySum1(nums, 2))