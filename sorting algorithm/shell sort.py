# 希尔排序

class Solution:

    def shellsort(self, alist):
        if alist == None or len(alist) <= 0:
            return
        n = len(alist)
        gap = n//2

        while gap > 0:

            for i in range(gap, n):
                temp = alist[i]
                j = i
                while j > gap and alist[j-gap] > temp:
                    alist[j] = alist[j-gap]
                    j -= gap
                alist[j] = temp
            gap = gap//2
        return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
s = Solution()
print(s.shellsort(unsorted_list))