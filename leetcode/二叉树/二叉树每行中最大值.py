# 515. Find Largest Value in Each Tree Row


class Solution:

    # 还是先层序遍历二叉树，把每一行的所有元素找出来，然后把它们中的最大值添加到到result里。
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        next_layer = [root]
        result = []
        while (next_layer):
            temp_next_layer = []
            layer_value = []
            for node in next_layer:
                if not node:
                    continue
                layer_value.append(node.val)
                # print layer_value
                if node.left:
                    temp_next_layer.append(node.left)
                if node.right:
                    temp_next_layer.append(node.right)

            # print temp_next_layer[0].val
            next_layer = temp_next_layer
            result.append(max(layer_value))

        return result
