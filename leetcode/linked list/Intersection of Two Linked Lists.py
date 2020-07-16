# 160. Intersection of Two Linked Lists


class ListNode:

    def __init__(self, x):
        self.val =  x
        self.next = None


class Solution:

    # 最简单的做法就是先将A中的节点添加到set中，然后遍历B中的节点，
    # 判断遍历到的节点是不是在set中已经存在了，如果存在的话，那么这个就是交点。O(n)
    def getIntersectionNode(self, headA, headB):
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next
        while headB:
            if headB in nodes:
                return headB

            headB = headB.next
        return None

    # 循环着走，走完了a走b，最后就相遇了,O(1)
    def getIntersectionNode1(self, headA, headB):
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1.val


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node4
node3.next = node4
node4.next = node5
s = Solution()
print(s.getIntersectionNode1(node1, node3))

