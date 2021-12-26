class Solution:
    def shortestWordDistance(self, wordsDict, word1: str, word2: str) -> int:
        sameWord = word1 == word2
        prev = -1
        result = float('inf')

        for idx, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if prev != -1 and (sameWord or wordsDict[idx] != wordsDict[prev]):
                    result = min(result, idx - prev)
                prev = idx

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestWordDistance(["practice","makes","perfect","coding","makes"],"makes","makes"))


