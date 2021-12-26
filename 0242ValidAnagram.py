class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # only lowercase char
        if not len(s) == len(t):
            return False
        
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        return not any(counts)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("abcde", "badce"))
