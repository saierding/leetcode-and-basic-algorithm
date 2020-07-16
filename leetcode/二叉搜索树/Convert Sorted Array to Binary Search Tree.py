# 108. Convert Sorted Array to Binary Search Tree


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归，找好中间的，然后递归即可
    def sortedArrayToBST(self, nums):
        return self._sortedArrayToBST(nums, 0, len(nums)-1)

    def _sortedArrayToBST(self, nums, left, right):
        if left > right:
            return None
        mid = (left+right)//2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, left, mid-1)
        root.right = self._sortedArrayToBST(nums, mid+1, right)
        return root

    # 迭代
    def sortedArrayToBST1(self, nums):
        root, stack = None, [(0, len(nums) - 1, None, None)]
        while stack:
            start, end, l_parent, r_parent = stack.pop()
            if start > end:
                continue

            mid = start + (end - start) // 2
            node = TreeNode(nums[mid])
            root = root or node
            if l_parent:
                l_parent.right = node
            if r_parent:
                r_parent.left = node
            stack.append((start, mid - 1, None, node))
            stack.append((mid + 1, end, node, None))

        return root


nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
print(s.sortedArrayToBST1(nums))


