class Solution:
    def evalRPN(self, tokens) -> int:
        # tokens will be valid
        numbers = []

        for i in range(len(tokens)):
            if tokens[i] not in {'+', '-', '*', '/'}:
                numbers.append(int(tokens[i]))

            else:
                a = numbers.pop()
                b = numbers.pop()
                if tokens[i] == '+':
                    numbers.append(a + b)

                elif tokens[i] == '-':
                    numbers.append(b - a)

                elif tokens[i] == '*':
                    numbers.append(a * b)

                elif tokens[i] == '/':
                    flag = -1 if a * b < 0 else 1
                    numbers.append(abs(b) // abs(a) * flag)

        return numbers[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

