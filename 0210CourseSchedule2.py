from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # at least 1 course
        if not prerequisites:
            return [i for i in range(numCourses)]

        inLevel = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for [c2, c1] in prerequisites:
            inLevel[c2] += 1
            graph[c1].append(c2)

        curr_crs, next_crs, result = [], [], []

        for i in range(numCourses):
            if not inLevel[i]:
                curr_crs.append(i)

        while curr_crs:
            result.extend(curr_crs[:])
            for c1 in curr_crs:
                for c2 in graph[c1]:
                    inLevel[c2] -= 1
                    if inLevel[c2] == 0: # no other prerequisite
                        next_crs.append(c2)

            curr_crs, next_crs = next_crs, []

        return result if not any(inLevel) else []


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
