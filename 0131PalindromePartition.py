from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, 0, [], result)
        return result

    def dfs(self, s, idx, curr, result):
        if idx == len(s):
            result.append(curr[:])
            return

        for i in range(idx, len(s)):
            if self.checkPalindrome(s[idx : i + 1]):
                curr.append(s[idx : i + 1])
                self.dfs(s, i + 1, curr, result)
                curr.pop()

    def checkPalindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.partition('aabbc'))

