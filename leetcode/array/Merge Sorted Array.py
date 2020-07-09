# 88. Merge Sorted Array


class Solution:

    # 这个题给了两个array，要求将nums2加到nums1中排序。这里从后往前排序变动少，
    # 从后往前记为nums1[index]
    # 然后谁大将谁填入其中，如果最后nums2没填完，就把它从后往前继续填进去。
    def merge(self, nums1, m, nums2, n):
        index = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[index] = nums1[m-1]
                m -= 1
            else:
                nums1[index] = nums2[n-1]
                n -= 1
            index -= 1

        while n > 0:
            nums1[index] = nums2[n-1]
            n -= 1
            index -= 1
        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
s = Solution()
print(s.merge(nums1, m, nums2, n))
