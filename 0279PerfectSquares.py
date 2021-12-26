from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return -1

        cnt = [i for i in range(n + 1)]

        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                cnt[i] = min(cnt[i], cnt[i - j ** 2] + 1)
                j += 1

        return cnt[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(10))

