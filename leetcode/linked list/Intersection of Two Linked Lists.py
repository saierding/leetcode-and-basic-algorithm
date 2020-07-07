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
    def getIntersectionNode(self, headA, headB):
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA

        return n1


