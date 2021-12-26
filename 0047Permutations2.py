class Solution:
    def permuteUnique(self, nums):
        result = []
        nums.sort()
        self.formPermutations([], nums, result)
        return result

    def formPermutations(self, permutation, candidate, result):
        # for each level, one ch from candidate if picked
        # in each level, no ch should be same
        if not candidate:
            result.append(permutation)
            return

        for i in range(len(candidate)):
            if i == 0 or candidate[i] != candidate[i - 1]:
                c = candidate[i]
                self.formPermutations(permutation + [c], candidate[:i] + candidate[i+1:], result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([2,2,1,1]))

