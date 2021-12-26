from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # arrange 
        if n == 0:
            return len(tasks)

        maxNum, maxCount = -1, 0
        letterCount = [0 for _ in range(26)]

        for task in tasks:
            idx = ord(task) - ord('A')
            letterCount[idx] += 1
            if letterCount[idx] > maxNum:
                maxNum = letterCount[idx]
                maxCount = 1
            elif letterCount[idx] == maxNum:
                maxCount += 1

        freeSlots = (maxNum - 1) * (n + 1 - maxCount)
        idleSlots = max(freeSlots - (len(tasks) - maxCount * maxNum), 0)
        return len(tasks) + idleSlots


if __name__ == '__main__':
    sol = Solution()
    print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

