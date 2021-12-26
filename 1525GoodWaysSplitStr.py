class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0

        left, right = set(), set()
        leftPart = []
        result = 0

        for i in range(len(s)):
            left.add(s[i])
            leftPart.append(len(left))

        for i in range(len(s) - 1, 0, -1):
            right.add(s[i])
            if len(right) == leftPart[i - 1]:
                result += 1

        return result

