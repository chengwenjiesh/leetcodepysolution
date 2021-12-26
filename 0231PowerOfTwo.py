class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2
        return n == 1
    
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(100))

