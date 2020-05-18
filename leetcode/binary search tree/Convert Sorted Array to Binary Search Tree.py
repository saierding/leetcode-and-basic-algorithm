# 108. Convert Sorted Array to Binary Search Tree


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

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


nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
print(s.sortedArrayToBST(nums))


