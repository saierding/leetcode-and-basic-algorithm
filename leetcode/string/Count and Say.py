# 38. Count and Say


class Solution:

    def countAndSay(self, n):
        if n <= 0:
            return ''
        if n == 1:
            return '1'
        seq = self.countAndSay(n - 1)
        next_seq = ''
        cnt = 1
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] == seq[i + 1]:
                cnt += 1
            else:
                next_seq += str(cnt)
                next_seq += seq[i]
                cnt = 1

        return next_seq


s = Solution()
print(s.countAndSay(5))