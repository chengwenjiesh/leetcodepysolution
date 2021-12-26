from typing import List

class Solution:
    def longestStrChain1(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x), reverse = True)
        chainLen = {}

        for i, w in enumerate(words):
            self.findChain(w, words, chainLen, 1)

        return max(chainLen.values())

    def findChain(self, w, words, chainLen, l):
        if w in chainLen:
            return

        chainLen[w] = l

        for i in range(len(w)):
            candidate = w[0 : i] + w[i + 1:]
            if candidate in words:
                self.findChain(candidate, words, chainLen, l + 1)

    def longestStrChain(self, words):
        words.sort(key = len)
        chainLen = {}
        result = 1

        for w in words:
            chainLen[w] = 1

        for w in words:
            for i in range(len(w)):
                candidate = w[0 : i] + w[i + 1:]
                if candidate in chainLen:
                    chainLen[w] = max(chainLen[w], chainLen[candidate] + 1)
            result = max(result, chainLen[w])

        return result


if __name__ == '__main__':
    sol = Solution()
    w = 'abcdea'
    for i in range(len(w)):
        candidate = w.replace(w[i], '')
        print(candidate)
    print(sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))

