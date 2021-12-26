class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s

        vowels = set(list('aeiouAEIOU'))
        ch = [ch for ch in s]

        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and s[l] not in vowels:
                l += 1
            while r >= 0 and s[r] not in vowels:
                r -= 1
            if l < r:
                ch[l], ch[r] = ch[r], ch[l]
                l += 1
                r -= 1

        return ''.join(ch)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels("bqq"))
    print(sol.reverseVowels("boa"))
    print(sol.reverseVowels("oasdhshlau"))

