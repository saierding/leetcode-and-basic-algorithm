# a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

class Solution:
    # 做法是把对字符串中的每个元素都当做起始位置，
    # 把其他元素当做以后的位置，然后再同样的进行操作。这样就会得到全排列。
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i+1:], res, path + ss[i])


s = Solution()
print(s.Permutation('abc'))
