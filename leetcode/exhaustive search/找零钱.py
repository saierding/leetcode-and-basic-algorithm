# 322. Coin Change
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
import math


class Solution:
    # 这里我们首先将coins从大到小进行排序，这是因为我们希望硬币数量尽可能的少，
    # 那么就需要尽量将面值大的硬币加入结果中。
    # 每次递归中判断剩余的amount%nums[index]是不是为0，如果是的话，
    # 表示当前的coins[index]可以将amount塞满，那么此时就是最优解了，记录下来；
    # 如果不是的话，那么我们只需要递归判断需要多少个coins[index]即可。
    # 如果遍历到最后一个coins[-1]且无法塞满amount的话，那么无解。
    # 最后还有一个非常重要的剪枝，如果当前硬币coins[index]（放满amount）放入后，
    # 硬币数比之前的结果都大的话，那么就不用继续判断后面的硬币了（因为硬币是排序过的）。

    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        n, res = len(coins), amount + 1

        def dfs(index, target, cnt):
            nonlocal res
            # 最后还有一个非常重要的剪枝，如果当前硬币coins[index]（放满amount）放入后，
            # 硬币数比之前的结果都大的话，那么就不用继续判断后面的硬币了（因为硬币是排序过的）
            if cnt + math.ceil(target / coins[index]) >= res:
                return
            # 每次递归中判断剩余的amount%nums[index]是不是为0，如果是的话，
            # 表示当前的coins[index]可以将amount塞满，那么此时就是最优解了，记录下来；
            if target % coins[index] == 0:
                res = cnt + target // coins[index]
                return
            # 如果遍历到最后一个coins[-1]且无法塞满amount的话，那么无解。
            if index == n - 1:
                return

            for i in range(target // coins[index], -1, -1):
                dfs(index + 1, target - coins[index] * i, cnt + i)

        dfs(0, amount, 0)
        return -1 if res > amount else res


s = Solution()
print(s.coinChange([1, 2, 5], 11))