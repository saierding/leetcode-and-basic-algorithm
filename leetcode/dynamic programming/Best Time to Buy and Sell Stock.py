# 121. Best Time to Buy and Sell Stock


class Solution:

    # 慢方法
    def maxProfit(self, prices):
        if not prices:
            return 0
        result = [0]*len(prices)
        for i in range(len(prices)-1):
            next = max(prices[i+1:])
            if next > prices[i]:
                result[i] = next-prices[i]
        return max(result)

    # 快方法
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))