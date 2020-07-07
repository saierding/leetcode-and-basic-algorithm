# 24. Swap Nodes in Pairs

class ListNode:

    def __init__(self, x):
        self.val =  x
        self.next = None


class Solution:

    # 很简单，就直接画个图解释while里面的即可
    # 1->2->3->4 => 2->1->4->3
    def swapPairs(self, head):
        h = ListNode(-1)
        h.next = head
        pre = h
        while pre.next != None and pre.next.next != None:
            node1 = pre.next
            node2 = node1.next
            lat = node2.next

            pre.next = node2
            node2.next = node1
            node1.next = lat

            pre = node1

        return h.next