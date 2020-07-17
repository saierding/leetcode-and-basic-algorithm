# 518. Coin Change 2
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

class Solution(object):
    # dp[i]代表了生成总价值为i有多少方案
    # dp[i] += dp[i - coin]，价值为i的解决方案应该加上价值为i - coin的解决方案。
    def change(self, amount, coins):

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[amount]

s = Solution()
print(s.change(5,[1,2,5]))
