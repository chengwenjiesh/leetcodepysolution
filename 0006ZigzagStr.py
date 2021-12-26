class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        circle = numRows * 2 - 2
        zigzag = [[] for _ in range(numRows)]

        for i, ch in enumerate(s):
            idx = i % circle
            if idx < numRows:
                zigzag[idx].append(ch)
            else:
                zigzag[circle - idx].append(ch)

        result = []
        for row in zigzag:
            result.append("".join(row))
        return "".join(result)


