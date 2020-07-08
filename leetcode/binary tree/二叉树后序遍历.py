# 145. Binary Tree Postorder Traversal


class Solution:

    def __init__(self):
        self.ret = []

    def postorderTraversal(self, root):

        if root != None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ret.append(root.val)

        return self.ret