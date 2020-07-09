# 101. Symmetric Tree


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # left == None and right == None
    # left == None or right == None
    # left.val != right.val
    # 如果是第一种的话，我们直接返回True。对于第二种和第三种的话，我们返回False。
    # 接着就是left.val == right.val，此时我们只需要递归下去，
    # 判断left.left and right.right和left.right and right.left是不是同样成立即可。

    def isSymmetric(self, root):
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    # 迭代
    # 建立一个栈，每次将left.left,right.right,left.right,right.left依次入栈即可。
    def isSymmetric(self, root):

        if not root:
            return True

        stack = list()
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if left == None and right == None:
                continue

            if (left == None or right == None) or (left.val != right.val):
                return False

            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)

        return True


