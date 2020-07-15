# 105. Construct Binary Tree from Preorder and Inorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def buildTree1(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

    # 一直往左边进栈，相等时说明到头了，这时候遍历stack和相等的条件，满足时出栈并且i+1,最后把右子树进栈并且加进树。
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return
        root = TreeNode(preorder[0])
        stack = [root]
        i = 0
        # 循环preorder，当pre和inorder[i]不相等时说明还有左子树
        for node in preorder[1:]:
            # parent用来保存当前所处的preorder的node,也就是构造的树的node
            parent = stack[-1]
            # 当pre和inorder[i]不相等时说明还有左子树,一直进栈保存
            if parent.val != inorder[i]:
                parent.left = TreeNode(node)
                stack.append(parent.left)
            else:
                # 相等了就开始出栈并且用parent记录父节点的位置
                while stack and stack[-1].val == inorder[i]:
                    parent = stack.pop()
                    i += 1
                # 右子树进栈即可
                parent.right = TreeNode(node)
                stack.append(parent.right)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
print(s.buildTree(preorder, inorder))