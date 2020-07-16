# 347. Top K Frequent Elements


class Solution:

    def topKFrequent(self, nums, k):
        import collections
        counter = collections.Counter(nums)
        # print(counter)
        return [item[0] for item in counter.most_common(k)]

    # dict
    # 通过(频率, 元素)
    # 形式存储,对排序解决
    def topKFrequent1(self, nums, k):
        import heapq
        count_list = dict()
        for i in nums:
            count_list[i] = count_list.get(i, 0) + 1
        # count_list:{1:4, 2:2, 3:1}
        p = list()
        for i in count_list.items():
            heapq.heappush(p, (i[1], i[0]))
        # p:[(4,1),(2,2),(1,3)]
        return [i[1] for i in heapq.nlargest(k, p)]


s = Solution()
nums = [1,1,1,1,2,2,3]
print(s.topKFrequent1(nums, 2))