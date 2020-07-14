# 144. Binary Tree Preorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)

    # 迭代是栈存储并循环栈，root进栈然后出栈存储val
    # 到result。接着如果有右子树先进栈右子树，然后进栈左子树。这样顺序就是中左右了
    # 例子：1，2，3
    # stack:[1,出栈 3,2 出栈]
    # result:[1, 2, 3]
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result