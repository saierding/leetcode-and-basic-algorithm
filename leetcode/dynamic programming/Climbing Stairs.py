# 70. Climbing Stairs


class Solution:

    def climbStairs(self, n):
        fib_front = 1
        fib_rear = 1
        if n < 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            ans = fib_front + fib_rear
            fib_front = fib_rear
            fib_rear = ans
        return ans


s = Solution()
print(s.climbStairs(4))