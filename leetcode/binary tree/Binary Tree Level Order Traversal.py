# 102. Binary Tree Level Order Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    # def _levelOrder(self, level, result, node):
    #     if node:
    #         if level == len(result):
    #             result.append([])
    #
    #         result[level].append(node.val)
    #         self._levelOrder(level + 1, result, node.left)
    #         self._levelOrder(level + 1, result, node.right)
    #
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     level, result = 0, list()
    #     self._levelOrder(level, result, root)
    #     return result

    # 迭代使用队列存每一层的节点，最后全部添加到result
    def levelOrder(self, root):
        if not root:
            return
        queue = [root]
        result = []
        while queue:
            layer = []
            for i in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layer)
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
print(s.levelOrder(node1))
