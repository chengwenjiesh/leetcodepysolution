import bisect

class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        if not t:
            return False
        
        idxS, idxT = 0, 0
        while idxS < len(s) and idxT < len(t):
            if s[idxS] == t[idxT]:
                idxS += 1
            idxT += 1
            
        return idxS == len(s)
    
    def isSubsequence(self, s, t):
        dictT = [[] for _ in range(26)]
        for i, letter in enumerate(t):
            dictT[ord(letter) - ord('a')].append(i)
            
        curr = 0
        for letter in s:
            idx = bisect.bisect_left(dictT[ord(letter) - ord('a')], curr)
            if idx >= len(dictT[ord(letter) - ord('a')]):
                return False
            curr = dictT[ord(letter) - ord('a')][idx] + 1
            
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("abc", "annbsdjixc"))
    print(sol.isSubsequence1("abc", "annbsdjixc"))
