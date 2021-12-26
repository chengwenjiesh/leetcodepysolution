from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        visited = [0] * len(wordList)
        q = deque([(beginWord, 1)])

        while q:
            word, l = q.popleft()
            # find next possible words
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    #s = list(word)
                    #s[i] = j
                    #newWord = ''.join(s)
                    newWord = word[:i] + j + word[i + 1:]
                    if newWord in wordSet:
                        if newWord == endWord:
                            return l + 1
                        else:
                            wordSet.remove(newWord)
                            q.append((newWord, l + 1))

        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))

