from typing import List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source, desti):
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        # dfs to all all potential desti
        # if loop found, return false
        # else, check if only desti is in candidate
        dstCandidate = set()
        return self.findAllPath(graph, source, desti, [], dstCandidate)


    def findAllPath(self, graph, src, dst, prevPath, dstCandidate):
        if len(graph[src]) == 0:
            if src != dst:
                return False
            dstCandidate.add(src)
            if len(dstCandidate) > 1:
                return False
            return True

        if src in prevPath:
            return False

        prevPath.append(src)
        for nextNode in graph[src]:
            if not self.findAllPath(graph, nextNode, dst, prevPath, dstCandidate):
                return False

        prevPath.pop()
        return True


if __name__ == '__main__':
    sol = Solution()
    #edges = [[0,1],[0,2],[1,3],[2,3]]
    edges = []
    print(sol.leadsToDestination(1, edges, 0, 0))

