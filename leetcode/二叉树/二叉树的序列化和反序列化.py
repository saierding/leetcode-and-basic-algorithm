# 297. Serialize and Deserialize Binary Tree


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 前序遍历的解法，我们可以对空节点存储为'#'，那么例子中的树就可以存储为1 2 # # 3 4 # # 5 # #
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

    # 将上面的前序遍历转化为二叉树
    def deserialize(self, data):
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


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.serialize(node1))
#print(s.deserialize('1 2 # # 3 4 # # 5 # #'))

