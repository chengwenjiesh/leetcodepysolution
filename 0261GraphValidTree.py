from DataStructures import TreeNode
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # len(edges) >= n -> cycle in tree
        # len(edges) < n - 1 -> separate tree
        if n - 1 != len(edges):
            return False

        graph = {i : [] for i in range(n)}
        visited = [0] * n

        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)

        self.findNodes(0, graph, visited)
        return sum(visited) == n

    def findNodes(self, currNode, graph, visited):
        visited[currNode] = 1
        for nextNode in graph[currNode]:
            if visited[nextNode] == 0:
                self.findNodes(nextNode, graph, visited)



if __name__ == '__main__':
    sol = Solution()
    print(sol.validTree(4,[[0,1],[0,2],[0,3],[1,4]]))
    print(sol.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))

