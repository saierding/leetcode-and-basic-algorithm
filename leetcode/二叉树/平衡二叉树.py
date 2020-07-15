# 110. Balanced Binary Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归即可
    # 当root为空的时候，我们将None也看成是一棵二叉树，所以返回True。
    # 接着我们判断左子树高度和右子树高度差是不是大于1，如果是，那么我们返回False就好。
    # 如果不是接着递归判断左子树和右子树是不是一棵平衡二叉树。
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            # 这里对每一个子节点判断，存在不平衡就设为-1
            # 最终返回也是-1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        # 如果返回值是-1，说明不平衡
        return height(root) != -1


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
print(s.isBalanced(node1))