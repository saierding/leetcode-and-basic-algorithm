# 112. Path Sum


class Solution:

    # 递归找到叶子结点即可
    # 当node.left==None and node.right==None的时候，node就是叶子节点
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not (root.left or root.right):
            return sum == root.val

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 迭代，前序遍历解决
    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while len(stack) > 0:
            node, tmp_sum = stack.pop()
            if node:
                if not node.left and not node.right and node.val == tmp_sum:
                    return True
                stack.append((node.right, tmp_sum - node.val))
                stack.append((node.left, tmp_sum - node.val))
        return False



