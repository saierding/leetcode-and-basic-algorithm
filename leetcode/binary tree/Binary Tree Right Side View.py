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
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res