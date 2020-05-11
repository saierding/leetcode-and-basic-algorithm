# 148. Sort List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 归并排序，快慢指针找中间点
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(fast)
        return self.mergesort(left, right)

    def mergesort(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            v1 = left.val
            v2 = right.val
            if v1 < v2:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return dummy.next


node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
print(s.sortList(node1))

