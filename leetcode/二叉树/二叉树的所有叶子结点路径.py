# 257. Binary Tree Paths


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归, path作为字符串保存路径，res作为数组保存字符串，
    # 如果是叶子结点就把路径保存下来，不是就把结点加到path里继续调用
    def binaryTreePaths(self, root: TreeNode):
        if root == None:
            return []
        res = []
        self.dfs(root, res, str(root.val))
        return res

    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res.append(path)
        if root.left != None:
            self.dfs(root.left, res, path+'->'+str(root.left.val))
        if root.right!= None:
            self.dfs(root.right, res, path+'->'+str(root.right.val))

    # 迭代,和上面基本一样,层次遍历的思路
    def binaryTreePaths1(self, root: TreeNode):
        if not root:
            return []
        stack = []
        res = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node4

s = Solution()
print(s.binaryTreePaths1(node1))
