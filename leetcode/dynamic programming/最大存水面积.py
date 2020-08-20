# 11. Container With Most Water


class Solution(object):
    # 一个比较好的解决的方法是，使用双指针方法，一个从最左边开始，
    # 一个从最右边开始，计算两个挡板之间的面积，然后在向中间移动。
    # 移动的规则是这样的，如果哪个挡板比较矮，就舍弃掉这个挡板，
    # 把指向这个挡板的指针向中间移动。 这样的移动方式是我们每次都保留了
    # 比较长的哪个挡板，也就能获得更多的水。当两个挡板的高度一样的话，
    # 移动任意一个即可，因为这两个是高度一样的挡板，如果中间有更高的挡板，
    # 那么当前的挡板决定了以后的挡板的最低值，
    # 也就是说以其中任意一个为边界的容器面积不可能超过当前的当前的值。
    def maxArea(self, height):

        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans