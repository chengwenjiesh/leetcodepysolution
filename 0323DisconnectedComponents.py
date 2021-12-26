from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        component = 0
        visited = [0] * n
        graph = {i : [] for i in range(n)}

        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)

        for i in range(n):
            if visited[i] == 0:
                component += 1
                self.findConnectedNodes(i,visited, graph)

        return component

    def findConnectedNodes(self, n, visited, graph):
        visited[n] = 1
        for nextNode in graph[n]:
            if visited[nextNode] == 0:
                self.findConnectedNodes(nextNode, visited, graph)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))

