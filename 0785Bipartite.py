from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # can we paint each node with either blue or red
        # so that for each edge, we will have different color on two sides
        visited = [0] * len(graph)
        nodeColor = {}
        for i in range(len(graph)):
            if not visited[i]:
                if not self.findNodes(i, graph, visited, nodeColor, 0):
                    return False

        return True


    def findNodes(self, curr, graph, visited, nodeColor, flag):
        visited[curr] = 1
        nodeColor[curr] = flag

        for nextNode in graph[curr]:
            if visited[nextNode] == 1:
                if nodeColor[nextNode] == flag:
                    return False
                else:
                    continue
            if not self.findNodes(nextNode, graph, visited, nodeColor, 1 - flag):
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

