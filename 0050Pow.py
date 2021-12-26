class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n == -1:
            return 1 / x
        
        half_pow = self.myPow(x, n // 2)
        if n % 2 == 1:
            return half_pow * half_pow * x
        else:
            return half_pow * half_pow


if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(-1, -1))
    print(sol.myPow(5, -1))
    print(sol.myPow(2, 9))
    print(sol.myPow(2, 4))
