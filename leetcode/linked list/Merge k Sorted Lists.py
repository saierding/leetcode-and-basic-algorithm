# 23. Merge k Sorted Lists


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
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
                # (i.val存储val值，x存储整个链表的第几个元素，i存储第几个链表)
                heapq.heappush(p, (i.val, x, i))
                i = i.next
                x += 1
        while p:
            cur.next = heapq.heappop(p)[2]
            cur = cur.next

        return result.next


node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(2)
node8 = ListNode(6)

node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
node7.next = node8
s = Solution()
print(s.mergeKLists([node1, node4, node7]))


