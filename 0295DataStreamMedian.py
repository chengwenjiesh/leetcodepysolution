import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallHalf = [] # max heap
        self.largeHalf = [] # min heap


    def addNum(self, num: int) -> None:
        # large half size should be equal or +1 of small half
        if len(self.smallHalf) == len(self.largeHalf):
            heapq.heappush(self.smallHalf, -num)
            top = heapq.heappop(self.smallHalf)
            heapq.heappush(self.largeHalf, -top)
        else:
            heapq.heappush(self.largeHalf, num)
            top = heapq.heappop(self.largeHalf)
            heapq.heappush(self.smallHalf, -top)

    def findMedian(self) -> float:
        # no need to -re-heapify
        if len(self.smallHalf) == len(self.largeHalf):
            return (self.largeHalf[0] - self.smallHalf[0]) / 2.0
        else:
            return float(self.largeHalf[0])


if __name__ == '__main__':
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    print(finder.findMedian())
    finder.addNum(3)
    print(finder.findMedian())

