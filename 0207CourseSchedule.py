from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        inLevel = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for [c1, c2] in prerequisites:
            inLevel[c1] += 1
            graph[c2].append(c1)

        curr_crs, next_crs = [], []
        for i in range(numCourses):
            if inLevel[i] == 0: # no prerequi needed
                curr_crs.append(i)

        # expand course layer by layer
        while curr_crs:
            for c1 in curr_crs:
                for c2 in graph[c1]:
                    inLevel[c2] -= 1
                    if inLevel[c2] == 0: # no other prerequi
                        next_crs.append(c2)

            curr_crs, next_crs = next_crs, []

        # all inorder should be 0 since all courses are expanded
        return not any(inLevel)

if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1,0],[0,1]]))
