class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        distance = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            distance[i + 1][0] = i + 1
        for j in range(n):
            distance[0][j + 1] = j + 1

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    distance[i + 1][j + 1] = distance[i][j]
                else:
                    distance[i + 1][j + 1] = min(distance[i + 1][j], distance[i][j + 1], \
                                                 distance[i][j]) + 1

        return distance[m][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance("intention", "execution"))
