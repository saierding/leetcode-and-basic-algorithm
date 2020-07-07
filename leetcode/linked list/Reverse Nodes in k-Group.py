# 25. Reverse Nodes in k-Group

class ListNode:

    def __init__(self, x):
        self.val =  x
        self.next = None


class Solution:

    # 分开成小块，每一块执行反转，画图解释for循环里面的
    # 1->2->3->4->5 k = 3举这个例子,先变成2->1->3->4->5,再变成3->2->1->4->5
    def reverseKGroup(self, head, k):
        h = ListNode(-1)
        h.next = head
        cur = pre = h

        n = -1
        while cur != None:
            n += 1
            cur = cur.next

        while n >= k:
            cur = pre.next
            for _ in range(k - 1):
                lat = cur.next
                cur.next = lat.next
                lat.next = pre.next
                pre.next = lat

            pre = cur
            n -= k

        return h.next


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
print(s.reverseKGroup(node1, 3))