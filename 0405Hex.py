class Solution:
    def toHex(self, num: int) -> str:
        hexBit = '0123456789abcdef'
        if num == 0:
            return '0'
        elif num < 0:
            num += (2 ** 32)

        result = ''
        while num:
            bit = hexBit[num & (16 - 1)]
            result += bit
            num >>= 4

        return result[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.toHex(-1))

