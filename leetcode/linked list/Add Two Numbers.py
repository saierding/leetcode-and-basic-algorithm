# 2. Add Two Numbers


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 用carry记进位，当前值是%10，进位值是//10
    def addTwoNumbers(self, l1, l2):
        # 进位
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node3
node3.next = node2
node5.next = node6
node6.next = node4
s = Solution()
print(s.addTwoNumbers(node1, node5))