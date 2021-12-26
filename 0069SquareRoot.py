class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x
        
        while left + 1 < right: # what's the ending status
            mid = left + (right - left) // 2
            if mid ** 2 < x:
                left = mid
            elif mid ** 2 > x:
                right = mid
            else:
                return mid

        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.mySqrt(50))
