import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numList = []
        self.numMap = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.numMap:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
            return True

        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.numMap:
            idx = self.numMap[val]
            self.numList[idx], self.numList[-1] = self.numList[-1], self.numList[idx]
            self.numMap[self.numList[idx]] = idx
            del self.numMap[val]
            self.numList.pop()
            return True

        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.numList:
            randIdx = random.randint(0, len(self.numList) - 1)
            return self.numList[randIdx]

if __name__ == '__main__':
    randSet = RandomizedSet()
    randSet.insert(1)
    randSet.insert(0)
    randSet.remove(1)
    randSet.insert(2)
    randSet.remove(0)
    print(randSet.getRandom())

