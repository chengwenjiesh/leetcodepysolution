class Solution:
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        # two-dimensional dp
        m, n = len(text1), len(text2)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
                    
        return lcs[m][n]
    
    def longestCommonSubsequence(self, text1, text2):
        # save more space usage
        # only maintain 2 * (n + 1) grid
        m, n = len(text1), len(text2)
        lcs = [[0] * (n + 1) for _ in range(2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i % 2][j] = lcs[(i - 1) % 2][j - 1] + 1
                else:
                    lcs[i % 2][j] = max(lcs[(i - 1) % 2][j], lcs[i % 2][j - 1])

        return lcs[m % 2][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))
    print(sol.longestCommonSubsequence("abcde", "fgh"))
