# 124. Binary Tree Maximum Path Sum


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxPathSum(self, root):
        res = float('-inf')

        def maxPath(node):
            nonlocal res
            if not node:
                return 0

            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val

        maxPath(root)
        return res


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.maxPathSum(node1))