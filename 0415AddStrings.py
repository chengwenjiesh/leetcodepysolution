class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # negative number?
        if not num1 or not num2:
            return num1 or num2

        result = ''
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        carry = 0

        while idx1 >= 0 or idx2 >= 0 or carry:
            n1 = int(num1[idx1]) if idx1 >= 0 else 0
            n2 = int(num2[idx2]) if idx2 >= 0 else 0

            result += str((n1 + n2 + carry) % 10)
            carry = (n1 + n2 + carry) // 10

            idx1 -= 1
            idx2 -= 1

        return result[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.addStrings("17", "177"))

