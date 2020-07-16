# 572. Subtree of Another Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = ''

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s1 = self.preOrder(s)
        self.res = ''
        s2 = self.preOrder(t)
        if s2 in s1:
            return True
        else:
            return False

    def preOrder(self, root):
        if not root:
            self.res += '# '
            return
        self.res += str(root.val) + ' '
        self.preOrder(root.left)
        self.preOrder(root.right)
        return self.res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.isSubtree(node1, node3))
