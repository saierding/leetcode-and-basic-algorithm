# 958. Check Completeness of a Binary Tree

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 自左向右寻找第一个空的节点，然后判断是否还有节点即可
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [root]
        i = 0

        while nodes[i]:
            nodes.append(nodes[i].left)
            nodes.append(nodes[i].right)
            i += 1

        return not any(nodes[i:])