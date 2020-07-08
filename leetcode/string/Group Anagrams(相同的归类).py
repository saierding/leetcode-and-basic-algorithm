# 49. Group Anagrams


class Solution:

    # 用dict存相同的字符，key存不同的类，value
    # 来分别记每一类里不同的字符串。
    def groupAnagrams(self, strs):
        str_dict = {}
        result = []
        for i in strs:
            new_strs = ''.join(sorted(i))
            if new_strs not in str_dict.keys():
                str_dict[new_strs] = [i]
            else:
                str_dict[new_strs].append(i)
        for i in str_dict.values():
            result.append(i)
        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))