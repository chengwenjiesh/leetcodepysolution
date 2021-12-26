from typing import List

class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        result = []
        self.buildParentheses(n, n, '', result)
        return result

    def buildParentheses(self, left, right, curr, result):
        if not right:
            result.append(curr)
            return

        if left > 0:
            self.buildParentheses(left - 1, right, curr + '(', result)

        if right > left:
            self.buildParentheses(left, right - 1, curr + ')', result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParentheses(3))
