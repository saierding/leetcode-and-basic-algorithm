# 543. Diameter of Binary Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def maxDiameter(root):
            nonlocal res
            if not root:
                return 0

            l = maxDiameter(root.left)
            r = maxDiameter(root.right)
            res = max(res, l + r)
            return max(l, r) + 1

        maxDiameter(root)
        return res
