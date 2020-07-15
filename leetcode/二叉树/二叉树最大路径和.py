# 124. Binary Tree Maximum Path Sum


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归，返回条件就是
    # 如果是路径的root，此时的最大值来自于node.left+node.right
    # 不是路径的root，此时的最大值来自于node.left或node.right
    def maxPathSum(self, root):
        res = float('-inf')

        def maxPath(node):
            # 记录当前最大值res
            nonlocal res
            if not node:
                return 0
            # 记录左子树最大值
            left = max(0, maxPath(node.left))
            # 记录右子树最大值
            right = max(0, maxPath(node.right))
            # 比较以当前节点为root的树的最大值和不以当前结点节点为root的树的最大值
            res = max(res, left + right + node.val)
            # 不以当前结点为root，最大值来自左右子树最大值加节点值
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