# 230. Kth Smallest Element in a BST


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 直接中序遍历然后存进数组就是排好序的
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = list()
        stack = list()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result[k-1]


node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(5)
node4 = TreeNode(4)
node5 = TreeNode(6)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.kthSmallest(node1, 2))