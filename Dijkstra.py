import heapq

class Solution:
    def findShortestPath(self, graph, start):
        n = len(graph)
        d = [float('inf')] * n
        visited = [False] * n
        minpq = [(0, start)]

        while minpq:
            distance, node = heapq.heappop(minpq)
            d[node] = min(d[node], distance)
            for i in range(n):
                if not visited[i] and graph[node][i] > 0:
                    heapq.heappush(minpq, (distance + graph[node][i], i))
            visited[node] = True
        print(visited)
        return d


if __name__ == '__main__':
    graph1 = [[0,6,0,1,0],
              [6,0,5,2,2],
              [0,5,0,0,5],
              [1,2,0,0,1],
              [0,2,5,1,0]]
    sol = Solution()
    print(sol.findShortestPath(graph1, 0))


