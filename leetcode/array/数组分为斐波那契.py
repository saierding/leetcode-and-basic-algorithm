# 842. Split Array into Fibonacci Sequence


class Solution(object):

    def splitIntoFibonacci(self, S):

        res = []
        self.dfs(S, [], res)
        return res
    # (1,2,3)->(1,2,34)->..(1,2,345..)
    # ->(1,23,4..)->(123,456,579)
    def dfs(self, num_str, path, res):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            res.extend(path)
            return True
        for i in range(len(num_str)):
            curr = num_str[:i + 1]
            if (curr[0] == '0' and len(curr) != 1) or int(curr) >= 2 ** 31:
                continue
            if self.dfs(num_str[i + 1:], path + [int(curr)], res):
                return True
        return False


s = Solution()
print(s.splitIntoFibonacci('123456579'))