# 二分查找


class Solution:

    # 递归
    def binarysearch(self, alist, first, last, value):
        if not alist:
            return -1
        if first < last:
            mid = (first+last)//2
            if alist[mid] == value:
                return mid
            elif alist[mid] > value:
                return self.binarysearch(alist, first, mid, value)
            elif alist[mid] < value:
                return self.binarysearch(alist, mid+1, last, value)
        else:
            return -1

    # 迭代
    def binarysearch2(self, alist, first, last, value):
        if not alist:
            return -1
        while first < last:
            mid = (first+last)//2
            if alist[mid] > value:
                last = mid
            elif alist[mid] < value:
                first = mid+1
            else:
                return mid
        return -1


alist = [1, 4, 5, 6, 7, 9, 10]
s = Solution()
print(s.binarysearch2(alist, 0, len(alist), 10))


