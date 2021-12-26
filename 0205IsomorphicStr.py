class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}
        for i in range(len(s)):
            # both of them in map
            # one of them in map
            # neither of them in map
            if s[i] not in sMap and t[i] not in tMap:
                sMap[s[i]], tMap[t[i]] = t[i], s[i]
            elif s[i] not in sMap or t[i] not in tMap:
                return False
            elif sMap[s[i]] != t[i] or tMap[t[i]] != s[i]:
                    return False

        return True

    def groupIsomorphic(self, sList):
        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic("apple", "bqqoa"))

