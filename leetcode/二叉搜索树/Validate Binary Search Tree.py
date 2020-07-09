# 98. Validate Binary Search Tree


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 中序遍历的迭代算法
    def isValidBST(self, root):
        if not root:
            return True
        pre = None
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and root.val <= pre.val:
                    return False
                pre = root
                root = root.right
        return True


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(15)
node4 = TreeNode(3)
node5 = TreeNode(21)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.isValidBST(node1))