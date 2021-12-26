class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        bracket_map = {"}":"{", "]":"[", ")":"("}
        bracket_stack = []
        
        for ch in s:
            if ch in bracket_map:
                if not bracket_stack or bracket_stack.pop() != bracket_map[ch]:
                    return False
            elif ch in bracket_map.values():
                bracket_stack.append(ch)
            else:
                return False
                
        return len(bracket_stack) == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))
