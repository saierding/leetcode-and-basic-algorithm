# 45. Jump Game II


class Solution():

    # curReach表示当前能跳到的最远距离，lastReach表示上次最远可以跳到的距离。
    # 那么，对于每次lastReach < i 时，说明跳上一次不到i，需要cnt++
    def jump(self, nums):
        curReach, lastReach, cnt, Len = 0, 0, 0, len(nums)
        for i in range(0, Len):
            if lastReach < i:
                lastReach = curReach
                cnt += 1
            curReach = max(curReach, nums[i]+i)
        return cnt


s = Solution()
print(s.jump([1, 1, 1, 1, 1]))