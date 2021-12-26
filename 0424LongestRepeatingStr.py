class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0] * 26
        l, r = 0, 0
        cnt = 0

        result = 0
        while r < len(s):
            if k >= sum(char) - max(char):
                char[ord(s[r]) - ord("A")] += 1
                r += 1
            else:
                char[ord(s[l]) - ord("A")] -= 1
                l += 1
            if k >= sum(char) - max(char):
                result = max(result, r - l)

        return result

