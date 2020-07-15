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
            # 以当前结点为root，最大路径就是左加右
            res = max(res, l + r)
            # 不以当前结点为root，
            # 最大路径就是左右最大值加一往上递归
            return max(l, r) + 1
        maxDiameter(root)
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
print(s.diameterOfBinaryTree(node1))