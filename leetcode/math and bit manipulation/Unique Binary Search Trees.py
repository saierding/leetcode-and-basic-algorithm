# 96. Unique Binary Search Trees


class Solution:

    def numTrees(self, n):
        count = [1, 1, 2]
        if n < 3:
            return count[n]
        else:
            for i in range(n - 2):
                count += [0]
            #print(count)
            for i in range(3, n + 1):
                for j in range(0, i):
                    count[i] += count[j] * count[i - j - 1]
                #print(count)
            return count[n]


s = Solution()
print(s.numTrees(4))