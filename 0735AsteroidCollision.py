from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aStack = []
        for a in asteroids:
            if not aStack or a * aStack[-1] > 0 or aStack[-1] < 0:
                aStack.append(a)
            else:
                while aStack and aStack[-1] * a < 0 and aStack[-1] + a < 0:
                    aStack.pop()
                if not aStack or aStack[-1] * a > 0:
                    aStack.append(a)
                elif aStack[-1] + a == 0:
                    aStack.pop()

        return aStack

if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([-1,2,3,-4]))

