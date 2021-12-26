class Solution:
    def countVowelStrings(self, n: int) -> int:
        # break each level of solution to a,b,c,d,e
        # f(1) = (5,4,3,2,1)
        # f(2) = (15, 10, 6, 3, 1)
        # f(3) = (35, .......)
        currCnt, nextCnt = [5, 4, 3, 2, 1], [0] * 5
        for i in range(n - 1):
            for j in range(4, -1, -1):
                nextCnt[j] = currCnt[j] if j == 4 else currCnt[j] + nextCnt[j + 1]
            currCnt, nextCnt = nextCnt, [0] * 5

        return currCnt[0]


