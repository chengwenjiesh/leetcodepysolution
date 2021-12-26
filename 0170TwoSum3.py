class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numDict = {}


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # O(1)
        if number in self.numDict:
            self.numDict[number] += 1
        else:
            self.numDict[number] = 1


    def find(self, target: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # O(n)
        for num in self.numDict:
            if target - num in self.numDict:
                if target - num != num:
                    return True
                if self.numDict[num] > 1:
                    return True

        return False

if __name__ == '__main__':
    obj = TwoSum()
    obj.add(-1)
    obj.add(0)
    obj.add(1)
    print(obj.find(0))
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
