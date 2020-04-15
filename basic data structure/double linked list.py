# 双向链表的反转

class Solution:

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class Solution:

    def reveresedlinkedlist(self, node):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt