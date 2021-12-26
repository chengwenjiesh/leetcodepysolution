from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shiftMap = {}
        for s in strings:
            shifted = self.shiftStr(s)
            if shifted in shiftMap:
                shiftMap[shifted].append(s)
            else:
                shiftMap[shifted] = [s]

        result = []
        for key in shiftMap:
            result.append(shiftMap[key])

        return result

    def shiftStr(self, s):
        # s is not empty
        # bcd -> abc
        # ba -> az
        chList = [c for c in s]
        offset = ord(chList[0]) - ord('a')
        result = []

        for c in chList:
            if ord(c) - offset >= ord('a'):
                uni = ord(c) - offset
            else:
                uni = ord(c) - offset + 26
            result.append(chr(uni))

        return str(result)

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))

