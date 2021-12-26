from typing import List

class Solution:
    def subarrayBitwiseORs2(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        sz = len(arr)
        result = set()
        dp = [[0] * len(arr) for _ in range(len(arr))]

        for i in range(sz - 1, -1, -1):
            dp[i][i] = arr[i]
            result.add(dp[i][i])
            for j in range(i + 1, sz):
                dp[i][j] = dp[i][j - 1] | arr[j]
                result.add(dp[i][j])

        return len(result)

    def subarrayBitwiseORs(self, arr):
        sz = len(arr)
        if sz < 2:
            return sz

        prev = set()
        result = set()
        for i in range(sz):
            curr = set()
            curr.add(arr[i])
            if i > 0:
                for num in prev:
                    curr.add(num | arr[i])

            prev = curr
            for num in curr:
                result.add(num)

        return len(result)

if __name__ == '__main__':
    sol = Solution()
    print(1 or 2)
    print(sol.subarrayBitwiseORs([1,1,2]))

