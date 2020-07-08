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
                if len(result) >= k:
                    break
                root = root.right

        return result[k - 1]
