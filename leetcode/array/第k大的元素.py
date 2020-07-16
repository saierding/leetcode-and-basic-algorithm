# 215. Kth Largest Element in an Array


# 这个题要找出数组里第k大的数。可以先排序然后nums[-k]即可。
# 大数据的情况可以用最小堆排序来做，先整一个len=k的最小堆然后有比他大的就进去再排序，最后输出
# output[0]即可。[4,5,5,6]

class Solution:

    # def findKthLargest(self, nums, k):
    #     nums = sorted(nums)
    #
    #     return nums[-k]
    def findKthLargest(self, nums, k):
        import heapq
        output = []
        # output = [4,5,5,6]
        for i in range(len(nums)):
            if len(output) < k:
                output.append(nums[i])
                output = heapq.nsmallest(len(output), output)
            else:
                if nums[i] > output[0]:
                    output[0] = nums[i]
                    output = heapq.nsmallest(k, output)
        return output[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
s = Solution()
print(s.findKthLargest(nums, 4))