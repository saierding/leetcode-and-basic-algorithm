# 93. Restore IP Addresses
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
class Solution:

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = list()
        if not s or 4 > len(s) or len(s) > 12:
            return result

        self._restoreIpAddresses(s, 4, 0, "", result)
        return result

    def _restoreIpAddresses(self, s, n, index, ip, result):
        # 判断是否走完了len(s)
        if n == 0:
            if index == len(s):
                result.append(ip)
            return
        # 判断是否符合规则
        def isNum(num):
            if 0 <= int(num) <= 255 and str(int(num)) == num:
                return True
            return False
        # 递归一直往下走
        for i in range(index + 1, len(s) + 1):
            if isNum(s[index:i]):
                self._restoreIpAddresses(s, n - 1, i, s[index:i] if ip == "" else ip + '.' + s[index:i], result)
            else:
                break

s = Solution()
print(s.restoreIpAddresses("25525511135"))



