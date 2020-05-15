# 142. Linked List Cycle II


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 快慢指针解法,第一次相遇后，慢继续迭代，pre节点从头出发，相遇节点为入口
    def detectCycle(self, head):
        if head == None:
            return 'no cycle'
        fast, slow, pre = head, head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != pre:
                    slow = slow.next
                    pre = pre.next
                return pre.val
        return 'no cycle'


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

s = Solution()
print(s.detectCycle(node1))