# 88. Merge Sorted Array


class Solution:

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
