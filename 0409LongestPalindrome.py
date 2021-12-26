class Solution:
    def longestPalindrome(self, s: str) -> int:
        visited = set()
        result = 0

        for letter in s:
            if letter not in visited:
                visited.add(letter)
            else:
                result += 2
                visited.remove(letter)

        return result + 1 if len(visited) > 0 else result

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("abcbc"))

