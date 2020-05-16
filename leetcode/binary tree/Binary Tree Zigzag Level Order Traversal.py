# 103. Binary Tree Zigzag Level Order Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root):
        if not root:
            return
        result = []
        i = 1
        queue = [root]
        while queue:
            layer = []
            for j in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if i % 2 == 1:
                result.append(layer)
            else:
                result.append(layer[::-1])
            i += 1
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
print(s.zigzagLevelOrder(node1))