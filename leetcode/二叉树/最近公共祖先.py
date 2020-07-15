# 236. Lowest Common Ancestor of a Binary Tree


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # p在左子树中，q在右子树中
    # q在左子树中，p在右子树中
    # p和q都在左子树中
    # p和q都在右子树中
    # 对于第一种和第二种情况很简单，p和q的最近公共祖先就是root。
    # 对于第三种情况我们只需递归向左子树找，第四种情况我们只需递归向右子树找。接着思考边界情况。
    # 当p==root or q==root的时候，我们返回root即可（因为要找最近公共祖先，继续遍历的话，就不可能是其祖先了）。
    # 那么这里就有一个迷惑人的地方了，请认真思考第一种和第二种情况下，左右子树的递归返回结果是什么？就是p和q。

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        # 查左子树是否有目标，没有返回none
        left = self.lowestCommonAncestor(root.left, p, q)
        # 查右子树是否有目标，没有返回none
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左右子树分别是目标返回当前根节点
        if left and right:
            return root
        # 只有一边有目标返回一边的节点，都没有返回none
        return left if left else right

    # 迭代
    # 先通过层序遍历得到p和q的祖先节点。然后将p的所有祖先放到集合ans中去。
    # 接着判断q的父亲节点是不是在ans中，如果不在，继续判断q父亲的父亲，不断向上，
    # 知道其中一个祖先在ans中出现。那么这个出现的节点即为p和q的最近公共祖先。
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s, parent = [root], {root: None}
        while p not in parent or q not in parent:
            node = s.pop()
            if node.left:
                parent[node.left] = node
                s.append(node.left)
            if node.right:
                parent[node.right] = node
                s.append(node.right)
        ans = set()
        while p:
            ans.add(p)
            p = parent[p]
        while q not in ans:
            q = parent[q]
        return q


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
s = Solution()
print(s.lowestCommonAncestor1(node1, node4, node5))
