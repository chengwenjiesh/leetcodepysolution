# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0

        q = deque([n for n in nestedList])
        total, unweight = 0, 0

        while q:
            qSize = len(q)
            levelSum = 0
            for i in range(qSize):
                nestedInt = q.popleft()
                if nestedInt.isInteger():
                    levelSum += nestedInt.getInteger()
                else:
                    for nextLevel in nestedInt.getList():
                        q.append(nextLevel)

            unweight += levelSum
            total += unweight

        return total

