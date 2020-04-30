# 4. Median of Two Sorted Arrays


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        result = []
        i, j = 0, 0
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result += nums1[i:]
        result += nums2[j:]
        num = result
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