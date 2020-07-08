# 143. Reorder List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 1->2->3->4->5, reorder it to 1->5->2->4->3.
    # head1: 1->2->null
    # head2: 5->4->3->null

    def reorderList(self, head):
        if head and head.next and head.next.next:
            # find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None

            # reverse linked list head2
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next

            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2

