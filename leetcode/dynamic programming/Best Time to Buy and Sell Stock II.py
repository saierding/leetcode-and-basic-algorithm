# 122. Best Time to Buy and Sell Stock II


class Solution:

    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))







