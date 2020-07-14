# 515. Find Largest Value in Each Tree Row


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 还是先层序遍历二叉树，把每一行的所有元素找出来，然后把它们中的最大值添加到到result里。
    def largestValues(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            # 每一层存进layer
            layer = []
            for i in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # result统计总的每一层最大的
            result.append(max(layer))

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
print(s.largestValues(node1))