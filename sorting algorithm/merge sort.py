# 归并排序(分治法)


class Solution:

    def mergesort(self, alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist)//2
        left = self.mergesort(alist[:mid])
        right = self.mergesort(alist[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4, 9]
s = Solution()
print(s.mergesort(unsorted_list))