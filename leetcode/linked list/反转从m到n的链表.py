# 92. Reverse Linked List II


class Solution:

    # t1   t2       pre  cur  lat
    # 1 -> 2 <- 3 <- 4    5 -> null
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
