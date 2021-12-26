class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s and t not empty
        letterMap = [0] * 128
        for letter in t:
            letterMap[ord(letter) - ord('A')] += 1

        start = end = 0
        span = float('inf')
        minIdx = 0
        count = len(t)

        while end < len(s):
            if letterMap[ord(s[end]) - ord('A')] > 0:
                count -= 1
            letterMap[ord(s[end]) - ord('A')] -= 1
            end += 1

            while count == 0:
                if end - start < span:
                    span = end - start
                    minIdx = start

                if letterMap[ord(s[start]) - ord('A')] == 0:
                    count += 1
                letterMap[ord(s[start]) - ord('A')] += 1
                start += 1

        return "" if span == float('inf') else s[minIdx : minIdx + span]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("cabwefgewcwaefgcf", "cae"))

