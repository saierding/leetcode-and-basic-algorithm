# 82. Remove Duplicates from Sorted List II


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 两个指针来存储位置, 两个指针，一个一直找到next不重复的然后另一个直接next到这个下面。
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        while cur:
            while cur.next and cur.next.val == pre.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
print(s.deleteDuplicates(node1))