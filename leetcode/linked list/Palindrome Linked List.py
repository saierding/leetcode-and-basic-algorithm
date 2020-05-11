# 234. Palindrome Linked List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 快慢指针找到中点，栈弹出判断
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        fast, slow = head, head
        reverse_node = []
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            cur = slow.next
            slow.next = None
            while cur:
                reverse_node.append(cur.val)
                cur = cur.next
        else:
            cur = slow.next
            slow.next = None
            while cur:
                reverse_node.append(cur.val)
                cur = cur.next
        while head and len(reverse_node) > 0:
            if head.val != reverse_node.pop():
                return False
            head = head.next
        return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)

node1.next = node2
node2.next = node3
s = Solution()
print(s.isPalindrome(node1))