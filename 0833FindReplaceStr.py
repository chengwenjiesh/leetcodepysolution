class Solution:
    def findReplaceString(self, s, indices, sources, targets) -> str:
        size = len(indices)

        indexSorted = []
        for i in range(size):
            indexSorted.append((indices[i], i))
        indexSorted.sort()

        for i in range(size - 1, -1, -1):
            idx = indexSorted[i][1]
            length = len(sources[idx])
            if s[indices[idx] : indices[idx] + length] == sources[idx]:
                s = s[: indices[idx]] + targets[idx] + s[indices[idx] + length :]

        return s

