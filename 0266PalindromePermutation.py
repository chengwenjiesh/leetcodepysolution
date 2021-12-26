class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        singleLetter = set()
        for ch in s:
            if ch in singleLetter:
                singleLetter.remove(ch)
            else:
                singleLetter.add(ch)

        return len(singleLetter) <= 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPermutePalindrome("abcde"))

