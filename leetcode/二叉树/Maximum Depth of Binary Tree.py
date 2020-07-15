# 104. Maximum Depth of Binary Tree


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 二叉树的层次遍历的方法
    # 队列存储每一行的节点
    # 当还存在queue时，循环这个队列，将上一层的node出队列并且将这一层的左子树右子树进队列。
    # 最后统计行数即可
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        layer = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            layer += 1
        return layer


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
print(s.maxDepth(node1))