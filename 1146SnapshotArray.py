class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = [[[-1, 0]] for _ in range(length)]
        self.v = 0

    def set(self, index: int, val: int) -> None:
        if self.snapshot[index][-1][0] == self.v:
            self.snapshot[index][-1][1] = val
        else:
            self.snapshot[index].append([self.v, val])

    def snap(self) -> int:
        self.v += 1
        return self.v - 1

    def get(self, index: int, snap_id: int) -> int:
        versions = self.snapshot[index]
        l, r = 0, len(versions) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if versions[mid][0] == snap_id:
                return versions[mid][1]
            elif versions[mid][0] < snap_id:
                l = mid
            else:
                r = mid - 1
        return versions[l][1] if versions[r][0] > snap_id else versions[r][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
