# 1299. Replace Elements with Greatest Element on Right Side


class Solution:

    def replaceElements(self, arr):
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_right = max_right, max(max_right, arr[i])
        return arr


arr = [17,18,5,4,6,1]
s = Solution()
print(s.replaceElements(arr))