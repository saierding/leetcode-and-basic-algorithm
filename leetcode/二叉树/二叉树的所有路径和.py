# 113. Path Sum II


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 用dfs的方法，先从左边往下，找到是叶子结点又是和等于target的就存起来，继续递归
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return []
        res = []
        self.dfs(root, sum, res, [root.val])
        return res

    def dfs(self, root, target, res, path):
        if not root:
            return
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, target, res, path+[root.left.val])
        if root.right:
            self.dfs(root.right, target, res, path+[root.right.val])


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

s = Solution()
print(s.pathSum(node1, 22))