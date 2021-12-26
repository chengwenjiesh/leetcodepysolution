from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        visited = [False] * (2 ** n)
        visited[start] = True
        result = []
        self.dfs(n, visited, [start], result)
        return result


    def dfs(self, n, visited, curr, result):
        if len(result) == 0:
            if all(visited):
                diff = curr[0] ^ curr[-1]
                if diff & (diff - 1) == 0:
                    result.append(curr[:])
                    return

            for nextNum in self.findNextNum(n, curr[-1]):
                if not visited[nextNum]:
                    visited[nextNum] = True
                    self.dfs(n, visited, curr + [nextNum], result)
                    visited[nextNum] = False


    def findNextNum(self, n, num):
        result = []
        for i in range(n):
            if num & (1 << i) == 0:
                result.append(num + (1 << i))
            else:
                result.append(num - (1 << i))
        print(str(num) + str(result))
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.circularPermutation(2, 3))

