from typing import List

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        lenLow, lenHigh = len(low), len(high)
        result = []

        for i in range(lenLow, lenHigh + 1):
            strobo = self.buildStroboStr(i)
            for num in strobo:
                if not (len(num) > 1 and num[0] == "0"):
                    result.append(num)
        print(result)
        cnt = 0
        for num in result:
            if int(num) >= int(low) and int(num) <= int(high):
                cnt += 1

        return cnt


    def buildStroboStr(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        result = []
        for num in self.buildStroboStr(n - 2):
            result.append("0" + num + "0")
            result.append("1" + num + "1")
            result.append("6" + num + "9")
            result.append("8" + num + "8")
            result.append("9" + num + "6")
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.strobogrammaticInRange("50", "100"))

