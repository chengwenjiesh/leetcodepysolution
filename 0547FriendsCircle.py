from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0
        n = len(isConnected)
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                result += 1
                self.findNeighbor(isConnected, i, visited)

        return result

    def findNeighbor(self, isConnected, i, visited):
        visited[i] = True

        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.findNeighbor(isConnected, j, visited)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

