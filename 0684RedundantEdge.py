from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        for e in edges:
            nodeA, nodeB = e[0], e[1]
            if not self.isConnected(nodeA, nodeB, graph, set()):
                if nodeA not in graph:
                    graph[nodeA] = [nodeB]
                else:
                    graph[nodeA].append(nodeB)
                if nodeB not in graph:
                    graph[nodeB] = [nodeA]
                else:
                    graph[nodeB].append(nodeA)
            else:
                return e

        return []


    def isConnected(self, nodeA, nodeB, graph, visited) -> bool:
        if nodeA not in graph or nodeB not in graph:
            return False

        if nodeA == nodeB:
            return True

        visited.add(nodeA)
        for nxtNode in graph[nodeA]:
            if nxtNode not in visited and self.isConnected(nxtNode, nodeB, graph, visited):
                return True

        return False

