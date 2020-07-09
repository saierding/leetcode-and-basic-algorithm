# 4. Median of Two Sorted Arrays


class Solution:

    # 将两个array加起来排序然后直接求中位数。
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