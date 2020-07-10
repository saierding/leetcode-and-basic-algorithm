# 42. Trapping Rain Water


class Solution:

    # 建立left和right两个指针。判断height[left]<height[right]，
    # 如果成立的话，left+=1，否则的话，我们right-=1。
    # 挪动left和right的同时需要记录左右的最大值maxLeft和maxRight。
    # 如果height[left]<height[right]并且height[left]<maxLeft的话，
    # 那么说明此时的left处于较低位置，增加水量maxLeft-height[left]
    # 如果height[left]>=height[right]并且height[right]<maxRight的话，
    # 那么说明此时的right处于较低位置，增加maxRight-height[right]水量。
    def trap(self, height):

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1

        return res
