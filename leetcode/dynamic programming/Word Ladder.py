# 127. Word Ladder


class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0

        q, visited = [(beginWord, 1)], set()
        while q:
            word, step = q.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i] + j + word[i + 1:]
                        if tmp in wordDict and tmp not in visited:  # difference
                            q.append((tmp, step + 1))

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))