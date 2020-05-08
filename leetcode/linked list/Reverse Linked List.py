# 206. Reverse Linked List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head):
        if head == None:
            return None
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
    

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
print(s.reverseList(node1))