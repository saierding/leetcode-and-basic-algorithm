# 83. Remove Duplicates from Sorted List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head):
        temp = head
        while temp:
            while temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next
            temp = temp.next
        return head.next.val


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
print(s.deleteDuplicates(node1))
