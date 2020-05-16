# 105. Construct Binary Tree from Preorder and Inorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def buildTree1(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

    # 迭代
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return
        root = TreeNode(preorder[0])
        stack = [root]
        i = 0
        for node in preorder[1:]:
            parent = stack[-1]
            if parent.val != inorder[i]:
                parent.left = TreeNode(node)
                stack.append(parent.left)
            else:
                while stack and stack[-1].val == inorder[i]:
                    parent = stack.pop()
                    i += 1
                parent.right = TreeNode(node)
                stack.append(parent.right)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
print(s.buildTree(preorder, inorder))