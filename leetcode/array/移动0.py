# 283. Move Zeroes


class Solution:

    def moveZeroes(self, nums):
        k = 0
        for i, num in enumerate(nums):
            # 往下找num不为0的
            if num != 0:
                # 把不为0的按照顺序往前提，和0换
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                    k += 1
                else: #i == k
                    k += 1
        return nums


arr = [0, 1, 0, 3, 12]
s = Solution()
print(s.moveZeroes(arr))