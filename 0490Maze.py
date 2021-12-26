from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        return self.searchPath(maze, start, destination, visited)
        
    def searchPath(self, maze, curr, desti, visited):
        if (curr[0], curr[1]) in visited:
            return False
        visited.add((curr[0], curr[1]))
        
        if curr == desti:
            return True
        
        # search in 4 direction
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = curr[0], curr[1]
            while 0 <= x + i < len(maze) and 0 <= y + j < len(maze[0]) \
                                         and maze[x + i][y + j] == 0:
                x += i
                y += j
            # next place found
            if self.searchPath(maze, [x, y], desti, visited):
                return True
        
        # exhausted all possible next places
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[3,2]))
