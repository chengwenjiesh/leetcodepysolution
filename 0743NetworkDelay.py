from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for t in times:
            try:
                graph[t[0]].append((t[1], t[2]))
            except KeyError as e:
                graph[t[0]] = [(t[1], t[2])]

        visited = set()
        minheap = [(0, k)]
        minTime = [float('inf')] * n

        while minheap and len(visited) < n:
            cost, node = heapq.heappop(minheap)
            minTime[node - 1] = cost
            visited.add(node)

            for nxtNode, nxtCost in graph.get(node, []):
                if cost + nxtCost < minTime[nxtNode - 1]:
                    heapq.heappush(minheap, (cost + nxtCost, nxtNode))

        return max(minTime) if len(visited) == n else -1


if __name__ == '__main__':
    sol = Solution()
    times = [[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
    n = 5
    k = 1
    print(sol.networkDelayTime(times, n, k))

