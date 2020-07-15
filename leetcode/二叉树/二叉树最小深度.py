# 111. Minimum Depth of Binary Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 还是层次遍历的方法
    def minDepth(self, root: TreeNode) -> int:
        result = float('inf')
        if not root:
            return 0
        # 队列保存节点还有深度
        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            # 到了叶子节点的话，记录当前最小的深度
            if not node.left and not node.right:
                result = min(result, depth)

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

        return result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3
s = Solution()
print(s.minDepth(node1))