class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        prev = -1
        result = float('inf')

        for idx, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if prev != -1 and wordsDict[idx] != wordsDict[prev]:
                    result = min(result, idx - prev)
                prev = idx

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestDistance(["practice","makes","perfect","coding","makes"],"coding","makes"))

