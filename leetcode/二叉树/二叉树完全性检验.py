# 958. Check Completeness of a Binary Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 自左向右寻找第一个空的节点，然后判断是否还有节点即可
    # [1, 2, 3, 4, 5, null, 6....] i这时候走到5后面的null
    # 从6开始还存在一个6说明any(node[i:])为true，not any为false
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [root]
        i = 0
        while nodes[i]:
            nodes.append(nodes[i].left)
            nodes.append(nodes[i].right)
            i += 1
        return not any(nodes[i:])


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
s = Solution()
print(s.isCompleteTree(node1))
