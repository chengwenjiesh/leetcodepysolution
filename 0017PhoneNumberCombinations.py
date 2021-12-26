
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        result2 = []

        self.findCombination(0, digits, "", letters, result)
        self.findCombination2(0, digits, "", letters, result2)
        return result

    def findCombination(self, idx, digits, prefix, letters, result):
        if idx == len(digits):
            result.append(prefix)
            return

        for letter in letters[int(digits[idx]) - 0]:
            self.findCombination(idx + 1, digits, prefix + letter, letters, result)

    def findCombination2(self, idx, digits, prefix, letters, result):
        if idx == len(digits):
            result.append(prefix)
            return

        for letter in letters[int(digits[idx]) - 0]:
            prefix += letter
            self.findCombination2(idx + 1, digits, prefix, letters, result)
            prefix = prefix[:-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
