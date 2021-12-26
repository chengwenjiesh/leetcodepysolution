import bisect

class MyCalendar:

    def __init__(self):
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        # start < end
        idx = bisect.bisect_right(self.slots, start)
        if idx % 2 == 1:
            return False

        idx2 = bisect.bisect_left(self.slots, end)
        if idx2 != idx:
            return False

        self.slots.insert(idx, start)
        self.slots.insert(idx + 1, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    obj = MyCalendar()
    print(obj.book(0,10))
    print(obj.book(10,20))
    print(obj.book(15,25))
    print(obj.book(20,30))

