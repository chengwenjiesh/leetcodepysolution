from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cached = {}
        return self.findBreak(s, cached, wordSet)


    def findBreak(self, s, cached, wordSet):
        if s in cached:
            return cached[s]

        if s in wordSet:
            return True

        for i in range(len(s)):
            left = s[0:i + 1]
            right = s[i + 1:]
            if right in wordSet and self.findBreak(left, cached, wordSet):
                cached[s] = True
                return True

        cached[s] = False
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak('leetcode', ['leet', 'code']))
    print(sol.wordBreak('leetcodee', ['leet', 'code']))
