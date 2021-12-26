class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        idx1, idx2 = len(a) - 1, len(b) - 1
        carry = 0

        while idx1 >= 0 or idx2 >= 0 or carry:
            numA = int(a[idx1]) if idx1 >= 0 else 0
            numB = int(b[idx2]) if idx2 >= 0 else 0

            digit = (numA + numB + carry) % 2
            carry = (numA + numB + carry) // 2
            result += str(digit)

            idx1 -= 1
            idx2 -= 1

        return result[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("111", "10"))

