# 297. Serialize and Deserialize Binary Tree

# 先考虑前序遍历的解法，我们可以对空节点存储为'#'，那么例子中的树就可以存储为1 2 # # 3 4 # # 5 # #
# 1
# / \
#     2
# 3
# / \
#     4
# 5
def serialize(self, root):

    res = ""

    def preOrder(root):
        nonlocal res
        if not root:
            res += '# '
            return
        res += str(root.val) + ' '
        preOrder(root.left)
        preOrder(root.right)

    preOrder(root)
    return res


def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    datas = data.split()

    def deOrder():
        val = datas.pop(0)
        if val == '#':
            return
        root = TreeNode(int(val))
        root.left = deOrder()
        root.right = deOrder()
        return root

    return deOrder()

