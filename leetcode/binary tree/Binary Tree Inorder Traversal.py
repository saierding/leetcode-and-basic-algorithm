# 94. Binary Tree Inorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

    # 迭代
    def inorderTraversall(self, root):
        if not root:
            return []
        stack = []
        result = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result