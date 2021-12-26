from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letterMap = [[] for _ in range(26)]
        for i, c in enumerate(s):
            letterMap[ord(c) - ord('a')].append(i)

        result = 0
        for word in words:
            result += self.isSubsequence(letterMap, word)
        return result

    def isSubsequence(self, letterMap, word):
        position = -1
        for c in word:
            idx = bisect.bisect_left(letterMap[ord(c) - ord('a')], position)
            if idx >= len(letterMap[ord(c) - ord('a')]):
                return 0
            position = letterMap[ord(c) - ord('a')][idx] + 1
        return 1


