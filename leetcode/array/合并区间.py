# 56. Merge Intervals


class Solution:

    # Input: [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果不存在list或者新的list与之前的最后一个没重合
            # 直接加上新的list
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
