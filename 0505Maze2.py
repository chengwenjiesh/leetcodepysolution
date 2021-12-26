import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        minheap = [(0, start[0], start[1])]
        visited = set()

        while minheap:
            d, x, y = heapq.heappop(minheap)
            if [x, y] == destination:
                return d
            visited.add((x, y))

            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y, next_d = x, y, d
                while 0 <= next_x + i < m and 0 <= next_y + j < n \
                                          and maze[next_x + i][next_y + j] == 0:
                    next_x += i
                    next_y += j
                    next_d += 1

                if (next_x, next_y) not in visited:
                    heapq.heappush(minheap, (next_d, next_x, next_y))

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestDistance([[0,0,1,0,0],
                                [0,0,0,0,0],
                                [0,0,0,1,0],
                                [1,1,0,1,1],
                                [0,0,0,0,0]], [0,4], [4,4]))
