class Solution:
    def generatePalindromes(self, s: str):
        if len(s) < 2:
            return list(s)

        candidates = []

        singleLetter = set()
        for ch in s:
            if ch in singleLetter:
                singleLetter.remove(ch)
                candidates.append(ch)
            else:
                singleLetter.add(ch)

        if len(singleLetter) > 1:
            return []

        # generate permutations for first half
        candidates.sort()
        result = []
        self.generatePermutations("", candidates, result)

        singleCh = list(singleLetter)[0] if singleLetter else ""
        return [s + singleCh + s[::-1] for s in result]


    def generatePermutations(self, permutation, candidates, result):
        if not candidates:
            result.append(permutation)
            return

        for i in range(len(candidates)):
            if i == 0 or candidates[i] != candidates[i - 1]:
                c = candidates[i]
                self.generatePermutations(permutation + c,
                                          candidates[:i] + candidates[i + 1:], result)

if __name__ == '__main__':
    sol = Solution()
    print(sol.generatePalindromes("aabbddc"))

