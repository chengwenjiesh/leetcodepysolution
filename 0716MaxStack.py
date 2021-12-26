class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxStack = []

    def push(self, x: int) -> None:
        if not self.maxStack:
            self.maxStack.append((x, x))
        else:
            self.maxStack.append((x, max(x, self.maxStack[-1][1])))

    def pop(self) -> int:
        # stack not empty
        return self.maxStack.pop()[0]

    def top(self) -> int:
        # stack not empty
        return self.maxStack[-1][0]

    def peekMax(self) -> int:
        # stack not empty
        return self.maxStack[-1][1]

    def popMax(self) -> int:
        # pop all element to buffer until we find max
        # remove max and pop back previous elements
        buf = []
        currMax = self.maxStack[-1][1]
        while self.maxStack and self.maxStack[-1][0] != currMax:
            buf.append(self.maxStack.pop())

        if self.maxStack:
            self.maxStack.pop()

        while buf:
            self.push(buf.pop()[0])

        return currMax


