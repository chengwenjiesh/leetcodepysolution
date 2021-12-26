class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.size = 0
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.end] = value
        self.end = (self.end + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.q[self.start] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.q[(self.end - 1) % self.capacity] if not self.isEmpty() else -1


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
