class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        if values[0][0] > timestamp:
            return ""

        l, r = 0, len(values) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid
        return values[r][1] if values[r][0] <= timestamp else values[l][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
