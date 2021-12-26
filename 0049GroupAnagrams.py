from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            t = ''.join(sorted(s))
            anagrams[t] = anagrams.get(t, []) + [s]
            
        return [anagrams[t] for t in anagrams]


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(['abc', 'bac', 'cab', 'ddd']))
