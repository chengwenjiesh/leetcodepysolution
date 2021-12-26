class Solution:
    def decodeString(self, s: str) -> str:
        strStack = [""]
        numStack = []
        size = len(s)

        i = 0
        while i < size:
            if s[i] >= 'a' and s[i] <= 'z':
                strStack[-1] += s[i]

            elif s[i] >= '0' and s[i] <= '9':
                startIdx = i
                while i < size - 1 and s[i + 1] >= '0' and s[i + 1] <= '9':
                    i += 1
                numStack.append(int(s[startIdx : i + 1]))

            elif s[i] == '[':
                strStack.append("")

            elif s[i] == ']':
                curr = strStack.pop()
                strStack[-1] += curr * numStack.pop()

            i += 1
        return "".join(strStack)

