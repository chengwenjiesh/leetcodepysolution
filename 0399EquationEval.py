from typing import List

class Solution:
    def calcEquation(self, equations, values, queries) -> List[float]:
        graph = self.buildGraph(equations, values)
        result = []

        for qry in queries:
            result.append(self.findValue(graph, set(), qry[0], qry[1], 1.0))
        return result

    def findValue(self, graph, visited, src, dst, prev):
        if src not in graph or dst not in graph:
            return -1.0

        if src == dst:
            return prev

        for node, value in graph[src].items():
            if node not in visited:
                visited.add(node)
                result = self.findValue(graph, visited, node, dst, prev * value)
                if result > 0:
                    return result

        return -1.0

    def buildGraph(self, equations, values):
        size = len(equations)
        graph = {}

        for i in range(size):
            src, dst, val = equations[i][0], equations[i][1], values[i]
            if src not in graph:
                graph[src] = {dst : val}
            else:
                graph[src][dst] = val
            if dst not in graph:
                graph[dst] = {src : 1 / val}
            else:
                graph[dst][src] = 1 / val

        return graph


