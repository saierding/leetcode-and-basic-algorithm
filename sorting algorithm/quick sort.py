# 快速排序


class Solution:

    def quicksort(self, alist, i, j):
        if i >= j:
            return alist
        low, high = i, j
        pivot = alist[i]
        while i < j:

            while i < j and alist[j] > pivot:
                j -= 1
            alist[i] = alist[j]

            while i < j and alist[i] <= pivot:
                i += 1
            alist[j] = alist[i]
        alist[i] = pivot
        self.quicksort(alist, low, i-1)
        self.quicksort(alist, i+1, high)
        return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4, 9, 6]
s = Solution()
print(s.quicksort(unsorted_list, 0, len(unsorted_list)-1))