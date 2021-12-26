class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.rle = encoding
        self.idx = 0
        self.cnt = 0


    def next(self, n: int) -> int:
        while n > 0:
            if self.idx >= len(self.rle):
                return -1

            remain = self.rle[self.idx] - self.cnt
            if remain >= n:
                self.cnt += n
                return self.rle[self.idx + 1]
            else:
                n -= remain
                self.idx += 2
                self.cnt = 0


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
