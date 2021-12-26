class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start, end = 0, 1
        used = {s[0]}
        result = 1

        while end < len(s):
            if s[end] not in used:
                used.add(s[end])
                result = max(result, end - start + 1)
                end += 1
            else:
                used.remove(s[start])
                start += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))
