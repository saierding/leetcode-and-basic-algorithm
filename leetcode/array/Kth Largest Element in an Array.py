# 215. Kth Largest Element in an Array


class Solution:

    # def findKthLargest(self, nums, k):
    #     nums = sorted(nums)
    #
    #     return nums[-k]
    def findKthLargest(self, nums, k):
        import heapq
        output = []
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