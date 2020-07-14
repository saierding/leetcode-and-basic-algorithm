# 100. Same Tree


class Solution:

    # 二叉树的层次遍历改编
    def isSameTree(self, p, q):

        q = [(p, q)]
        while q:
            node1, node2 = q.pop(0)
            if node1 and node2 and node1.val == node2.val:
                q.append((node1.left, node2.left))
                q.append((node1.right, node2.right))
            else:
                # node1 == None and node2 != None  node1 != None and node2 == None
                if node1 != node2:
                    return False

        return True
