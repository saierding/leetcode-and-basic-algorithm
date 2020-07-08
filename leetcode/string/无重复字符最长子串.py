# 3. Longest Substring Without Repeating Characters


class Solution:

    # 先遍历整个字符串，然后对遍历到的每个字符后的字符做处理（检查是否有重复元素），
    # 我们通过建立一个空的字符串，如果检查的字符在这个空的字符串中没有的话，
    # 我们将他加入这个空字符串中，并且记录这个空字符串的长度
    # O(n2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i, _ in enumerate(s):  # 这里没有使用range函数
            count = 0
            usedChar = str()
            for j in s[i:]:
                if j not in usedChar:
                    usedChar += j
                    count += 1
                    if maxLength < count:  # 这里没有使用max函数
                        maxLength = count
                else:
                    break
        return maxLength

    # O(n)
    # 用字典记录位置，重复的话left更新到前一个right的下一个
    def lengthOfLongestSubstring1(self, s):
        left, right = 0, 0
        res = 0
        chars = dict()
        for right in range(len(s)):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            res = max(res, right - left + 1)
        return res


s = Solution()
print(s.lengthOfLongestSubstring1('dvdf'))