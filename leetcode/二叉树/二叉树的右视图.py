# 199. Binary Tree Right Side View


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 和层次遍历差不多，先层次遍历，再然后将每一层的最后一个值添加到结果中。
    def rightSideView(self, root):
        if not root:
            return []
        q, res = [root], list()
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


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
print(s.rightSideView(node1))