# 141. Linked List Cycle


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 快慢指针解法
    def hasCycle(self, head):
        if head == None:
            return False
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2
node2.next = node1
s = Solution()
print(s.hasCycle(node1))