from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(speed)
        time = [(target - position[i]) / speed[i] for i in range(size)]
        cars = [(position[i], time[i]) for i in range(size)]

        result = 1
        cars.sort()

        slowest = cars[-1][1]
        for i in range(size - 1, -1, -1):
            if slowest < cars[i][1]:
                result += 1
                slowest = cars[i][1]

        return result

