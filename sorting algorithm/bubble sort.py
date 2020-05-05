# 冒泡排序


class Solution:

    def bubblesort(self, alist):
        if alist == None or len(alist) <= 0:
            return
        for i in range(0, len(alist)):
            for j in range(0, len(alist)-i-1):
                if alist[j] < alist[j+1]:
                    pass
                else:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist


unsorted_list = []
s = Solution()
print(s.bubblesort(unsorted_list))