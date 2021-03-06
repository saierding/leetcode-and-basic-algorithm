# 快速排序


def quicksort(alist):
    if len(alist) < 2:
        return alist
    else:
        pivot = alist[0]
        less, more = [], []
        for i in alist[1:]:
            if i > pivot:
                more.append(i)
            else:
                less.append(i)
        return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([1, 5, 7, 8, 0, 1]))



# class Solution:

#     def quicksort(self, alist, i, j):
#         if i >= j:
#             return alist
#         low, high = i, j
#         pivot = alist[i]
#         while i < j:
#
#             while i < j and alist[j] > pivot:
#                 j -= 1
#             alist[i] = alist[j]
#
#             while i < j and alist[i] <= pivot:
#                 i += 1
#             alist[j] = alist[i]
#         alist[i] = pivot
#         self.quicksort(alist, low, i-1)
#         self.quicksort(alist, i+1, high)
#         return alist
#
#
# unsorted_list = [3, 6, 9, 11, 6, 7, 5]
# s = Solution()
# print(s.quicksort(unsorted_list, 0, len(unsorted_list)-1))