# 16. 3Sum Closest


class Solution:

    # 这个题要写出最接近target的三个数的和。这里先对nums遍历，然后对i+1到len-1左右夹击，i+left+
    # right-target小于0则left++要不right--,用closest作为寄存器保存当前最接近值。
    def threeSumClosest(self, nums, target):
        nums_len = len(nums)
        nums.sort()
        closest_num = float('inf')
        for i in range(nums_len-2):
            left, right = i+1, nums_len-1
            while left < right:
                min_num = nums[i] + nums[left] + nums[right] - target
                if abs(min_num) < abs(closest_num):
                    closest_num = min_num
                if abs(min_num) == 0:
                    return target
                elif min_num < 0:
                    left += 1
                elif min_num > 0:
                    right -= 1
        return closest_num + target


nums = [-1, 2, 1, -4]
s = Solution()
print(s.threeSumClosest(nums, 1))