# 94. Binary Tree Inorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def inorderTraversal(self, root):
        if not root:
            return []
        ans = self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        return ans

    # 迭代
    # 迭代就是栈存储并循环root和栈，先一直往左走并
    # 进栈，走完了root以后开始出栈并且存储val到result，最后root变为右子树。
    # 例子：1，2，3
    # stack:[1,2,出栈  3]
    # result:[2,1, 3]
    def inorderTraversall(self, root):
        if not root:
            return []
        stack = []
        result = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result


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
print(s.inorderTraversal(node1))