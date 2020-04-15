# 插入排序

class Solution:

    def insertionsort(self, alist):
        if alist == None or len(alist) <= 0:
            return
        for i, val in enumerate(alist):
            while i > 0 and val < alist[i-1]:
                alist[i] = alist[i-1]
                i -= 1
            alist[i] = val
        return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
s = Solution()
print(s.insertionsort(unsorted_list))