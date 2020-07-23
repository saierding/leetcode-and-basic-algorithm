def Knapsack(num, weight, value, res, cap):
    dp = [[0 for i in range(cap + 1)] for j in range(cap + 1)]
    for i in range(0, num+1):
        dp[i][0] = 0
    for j in range(0, cap+1):
        dp[0][j] = 0
    for i in range(1, num):
        for j in range(1, cap+1):
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
    print(dp)
    j = cap
    for i in range(num-1, 0, -1):
        if dp[i][j] > dp[i-1][j]:
            res[i] = 1
            j = j-weight[i]
        else:
            res[i] = 0
    return res



weight = [-1, 8, 11, 17]
value = [-1, 8, 11, 17]
num = len(weight)
cap = sum(value[1:])//2
res = [0]*num
maxval = Knapsack(num, weight, value, res, cap)
sum1 = 0
sum2 = 0
for i in range(1, len(maxval)):
    if maxval[i] == 1:
        sum1 += value[i]
    else:
        sum2 += value[i]
print(max(sum1, sum2))

