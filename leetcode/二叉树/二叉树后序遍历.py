# 145. Binary Tree Postorder Traversal


class Solution:

    def __init__(self):
        self.ret = []

    # 递归先进去2，然后3，最后进1
    def postorderTraversal(self, root):

        if root != None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ret.append(root.val)

        return self.ret