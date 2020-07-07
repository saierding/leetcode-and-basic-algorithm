# 328. Odd Even Linked List


class ListNode:

    def __init__(self, x):
        self.val =  x
        self.next = None


class Solution:
    # 1->2->3->4->5->NULL => 1->3->5->2->4->NULL
    # 把奇偶链表分别标注下来，奇的下一个是偶的下一个，偶的下一个是奇的下一个即可
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        t = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = t
        return head


