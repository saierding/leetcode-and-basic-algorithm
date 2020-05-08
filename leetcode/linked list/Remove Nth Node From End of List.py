# 19. Remove Nth Node From End of List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        cur, pre = dummy,  dummy
        while n > 0:
            cur = cur.next
            n -= 1
        while cur.next:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
print(s.removeNthFromEnd(node1, 2))