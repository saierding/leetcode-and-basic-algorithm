# 4. Median of Two Sorted Arrays


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        num = sorted(nums1+nums2)
        odd = float(num[(0+len(num))//2])
        even = (num[len(num)//2]+num[len(num)//2-1])/2
        if len(num) % 2 == 1:
            return odd
        else:
            return even


nums1 = [1, 2, 5]
nums2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))