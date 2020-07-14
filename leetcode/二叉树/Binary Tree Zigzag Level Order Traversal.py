# 103. Binary Tree Zigzag Level Order Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 和广度遍历一样的思路，就是在判断一下是否是奇数层或者偶数层即可
    # 迭代就是将每一层的node存储进一个队列。
    # 当还存在queue时，循环这个队列，将上一层的node出队列并且将这一层的左子树右子树进队列。
    def zigzagLevelOrder(self, root):
        if not root:
            return
        result = []
        i = 1
        queue = [root]
        while queue:
            # 每一层存进layer
            layer = []
            for j in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 用i来统计在哪一层
            # 对每一层进行判断，奇数直接输出，偶数输出倒序的
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