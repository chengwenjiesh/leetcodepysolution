from typing import List
from collections import deque

class Solution:
    def killProcess1(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # pid and ppid should have same len
        # skip sanity check for time's sake
        # assume process to kill is in the pid
        processTree = {}
        for i in range(len(pid)):
            if ppid[i] not in processTree:
                processTree[ppid[i]] = [pid[i]]
            else:
                processTree[ppid[i]].append(pid[i])

        result = []
        processQueue = deque([kill])

        # bfs
        while processQueue:
            currProc = processQueue.popleft()
            result.append(currProc)
            if currProc in processTree:
                for subProc in processTree[currProc]:
                    processQueue.append(subProc)

        return result

    def killProcess(self, pid, ppid, kill):
        processTree = {}
        for i in range(len(pid)):
            if ppid[i] not in processTree:
                processTree[ppid[i]] = [pid[i]]
            else:
                processTree[ppid[i]].append(pid[i])

        result = []
        self.findSubProcess(kill, result, processTree)
        return result

    def findSubProcess(self, curr, result, processTree):
        if curr not in processTree:
            result.append(curr)
            return

        result.append(curr)
        for subProcess in processTree[curr]:
            self.findSubProcess(subProcess, result, processTree)

if __name__ == '__main__':
    sol = Solution()
    print(sol.killProcess([1,3,10,5], [3,0,5,3], 5))
    print(sol.killProcess1([1,3,10,5], [3,0,5,3], 5))
