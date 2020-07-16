# 92. Reverse Linked List II


class ListNode:

    def __init__(self, x):
        self.val =  x
        self.next = None


class Solution:
    # Input: 1->2->3->4->5->NULL, m = 2, n = 4
    # Output: 1->4->3->2->5->NULL
    # pre,cur一直往后移动
    # t1   t2       pre  cur  lat
    # 1 <- 2 <- 3 <- 4    5 -> null
    # t1.next = pre, t2.next = cur
    # 首先把pre和cur移动到指定位置，然后反转链表
    # t1和t2记录pre和cur反转前的位置
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m >= n or m < 0 or n < 0:
            return head
        pre = None
        cur = head
        i = 1
        while i < m and cur != None:
            pre = cur
            cur = cur.next
            i += 1
        t1 = pre
        t2 = cur

        while i <= n and cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat
            i += 1

        if m == 1:
            t2.next = cur
            return pre

        t1.next = pre
        t2.next = cur
        return head


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
print(s.reverseBetween(node1, 2, 4))