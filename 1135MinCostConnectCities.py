from typing import List

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for edge in connections:
            if edge[0] not in graph:
                graph[edge[0]] = [(edge[1], edge[2])]
            else:
                graph[edge[0]].append((edge[1], edge[2]))
            if edge[1] not in graph:
                graph[edge[1]] = [(edge[0], edge[2])]
            else:
                graph[edge[1]].append((edge[0], edge[2]))

        # minpq (cost, city)
        minpq = [(0, n)]
        visited = set()
        total = 0

        while minpq and len(visited) < n:
            cost, city = heapq.heappop(minpq)
            if city not in visited:
                visited.add(city)
                total += cost
                if city not in graph:
                    return -1
                for nxtCity, nxtCost in graph[city]:
                    heapq.heappush(minpq, (nxtCost, nxtCity))

        return total if len(visited) == n else -1
