import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Dijkstra
        if src == dst:
            return 0

        graph = self.buildGraph(flights)
        minpq = [(0, src, 0)]

        while minpq:
            cost, city, stop = heapq.heappop(minpq)
            print(cost, city, stop)
            if city == dst:
                return cost
            if stop <= k and city in graph:
                for nextCity, nextCost in graph[city].items():
                    heapq.heappush(minpq, (cost + nextCost, nextCity, stop + 1))

        return -1

    def buildGraph(self, flights):
        graph = {}
        for f in flights:
            start, end, cost = f[0], f[1], f[2]
            if start not in graph:
                graph[start] = {end : cost}
            else:
                graph[start][end] = cost

        return graph


    def findCheapestPrice2(self, n: int, flights, src: int, dst: int, k: int):
        # Bellman-Ford
        cost = [float('inf')] * n
        cost[src] = 0

        for i in range(k + 1):
            temp = cost[:]
            for flight in flights:
                curr, next, price = flight[0], flight[1], flight[2]
                if cost[curr] == float('inf'): # haven't been reached
                    continue
                temp[next] = min(temp[next], cost[curr] + price)
            cost = temp
        return cost[dst] if cost[dst] != float('inf') else -1



if __name__ == '__main__':
    sol = Solution()
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    print(sol.findCheapestPrice(3, flights, 0, 2, 1))

