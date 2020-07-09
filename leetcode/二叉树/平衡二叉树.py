# 110. Balanced Binary Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归即可
    # 当root为空的时候，我们将None也看成是一棵二叉树，所以返回True。
    # 接着我们判断左子树高度和右子树高度差是不是大于1，如果是，那么我们返回False就好啦。
    # 如果不是接着递归判断左子树和右子树是不是一棵平衡二叉树。
    def isBalanced(self, root):
        if not root:
            return True

        def height(node):
            if not node:
                return 0

            return max(height(node.left), height(node.right)) + 1

        if abs(height(root.left) - height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 改进后
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        return height(root) != -1