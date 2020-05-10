# 138. Copy List with Random Pointer


class Node:
    def __init__(self, x):
        self.val = int(x)
        self.next = None
        self.random = None


class Solution:

    # 先正常拷贝next，把老node和新node的random存成字典，从过key找到新的random
    def copyRandomList(self, head):
        dummy = Node(0)
        cur = dummy
        random_dict = {}
        while head:
            new_node = Node(head.val)
            cur.next = new_node

            random_dict[head] = new_node
            new_node.random = head.random

            head = head.next
            cur = cur.next

        curNode = dummy.next
        while curNode is not None:
            if curNode.random is not None:
                curNode.random = random_dict[curNode.random]
            curNode = curNode.next

        return dummy.next


