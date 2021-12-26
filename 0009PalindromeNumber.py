class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverseNumber = 0
        original = x
        while x:
            lastDigit = x % 10
            reverseNumber = reverseNumber * 10 + lastDigit
            x = x // 10
            
        return original == reverseNumber


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(2121))
