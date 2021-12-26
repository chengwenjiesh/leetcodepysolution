class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []


    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, val))
        else:
            self.minStack.append((val, min(val, self.minStack[-1][1])))

    def pop(self) -> None:
        # minStack is not empty
        self.minStack.pop()


    def top(self) -> int:
        # minStack is not empty
        return self.minStack[-1][0]


    def getMin(self) -> int:
        # minStack is not empty
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(2)
    minStack.push(1)
    minStack.push(-1)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())

