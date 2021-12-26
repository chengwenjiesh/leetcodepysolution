class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        left = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            else:
                if left and s[left[-1]] == '(':
                    left.pop()
                else:
                    left.append(i)

        if not left:
            return len(s)

        result = max(0, left[0] - 0, len(s) - 1 - left[-1])
        for i in range(1, len(left)):
            result = max(result, left[i] - left[i - 1] - 1)

        return result


