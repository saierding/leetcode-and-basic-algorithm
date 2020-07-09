# 131. Palindrome Partitioning


class Solution:

    # 首先传入s="aab" pal=[] res = [], 首先切割出"a"（然后是"aa" "aab" ...），然后判读它是不是回文串：
    # 如果不是，直接跳过
    # 如果是，则此时剩余的 s="ab"， pal += ["a"]
    # 写入res的判断是，当s=""时，记录结果

    def partition(self, s):
        result = []
        if not s:
            return result

        palindromes = []
        self.dfs(s, 0, palindromes, result)
        return result

    def dfs(self, s, pos, palindromes, ret):
        if pos == len(s):
            ret.append([] + palindromes)
            return

        for i in range(pos + 1, len(s) + 1):
            if not self.isPalindrome(s[pos:i]):
                continue

            palindromes.append(s[pos:i])
            self.dfs(s, i, palindromes, ret)
            palindromes.pop()

    def isPalindrome(self, s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1]


string = 'aab'
s = Solution()
print(s.partition(string))