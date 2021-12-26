class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = [int(s) for s in str(num)]
        buckets = [-1 for _ in range(10)]

        for i in range(len(numList)):
            buckets[numList[i]] = i

        for i in range(len(numList)):
            for digit in range(9, -1, -1):
                if digit > numList[i] and buckets[digit] > i:
                    numList[i], numList[buckets[digit]] = numList[buckets[digit]], numList[i]
                    return int("".join(str(i) for i in numList))

        return num

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSwap(47736))

