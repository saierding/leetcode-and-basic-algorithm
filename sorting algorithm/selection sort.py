# 选择排序


class Solution:

    def selectionsort(self, alist):
        if alist == None or len(alist) <= 0:
            return
        for i in range(len(alist)):
            minval = i
            for j in range(i+1, len(alist)):
                if alist[minval] < alist[j]:
                    pass
                else:
                    minval = j
            alist[i], alist[minval] = alist[minval], alist[i]
        return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
s = Solution()
print(s.selectionsort(unsorted_list))