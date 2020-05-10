# 23. Merge k Sorted Lists


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 二次遍历存为一个排序的最小堆[val, id, listnode]
    def mergeKLists(self, lists):
        import heapq
        result = ListNode(-1)
        cur = result
        p = list()
        x = 0
        for i in lists:
            while i:
                heapq.heappush(p, (i.val, x, i))
                i = i.next
                x += 1

        while p:
            cur.next = heapq.heappop(p)[2]
            cur = cur.next

        return result.next

