class Solution:
    def twodistinct(self, s: str) -> int:
        used = {s[0]:1}
        l, r = 0, 1
        result = 1

        while r < len(s):
            if len(used) < 3:
                used[s[r]] = 1 if s[r] not in used else used[s[r]] + 1
                result = max(result, r - l)
                r += 1
            else:
                if used[s[l]] == 1:
                    del used[s[l]]
                else:
                    used[s[l]] -= 1
                l += 1

        return max(result, r - l) if len(used) < 3 else result

if __name__ == '__main__':
    sol = Solution()
    print(sol.twodistinct("ccaabbb"))

