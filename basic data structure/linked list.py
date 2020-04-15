# 反转链表

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverselist(self, node):
        if node == None:
            return None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

s = Solution()
print(s.reverselist(node1))

