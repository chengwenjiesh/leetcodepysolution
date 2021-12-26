class Solution:
    def canIWin(self, maxBound: int, target: int) -> bool:
        if maxBound >= target:
            return True
        if (1 + maxBound) * maxBound // 2 < target:
            return False

        candidate = [x for x in range(1, maxBound + 1)]
        prevPath = {}
        return self.buildPath(candidate, target, prevPath)


    def buildPath(self, candidate, target, prevPath):
        if target <= 0:
            return False

        if tuple(candidate) in prevPath:
            return prevPath[tuple(candidate)]

        for i, num in enumerate(candidate):
            if target <= num or not self.buildPath(candidate[:i] + candidate[i + 1:],\
                                                   target - num, prevPath):
                prevPath[tuple(candidate)] = True
                return True

        prevPath[tuple(candidate)] = False
        return False



if __name__ == '__main__':
    sol = Solution()
    print(sol.canIWin(10, 40))

