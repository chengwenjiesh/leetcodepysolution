class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited, count = [False] * 26, [0] * 26
        for letter in s:
            count[ord(letter) - ord('a')] += 1
            
        letterStack = []
        for letter in s:
            if visited[ord(letter) - ord('a')]:
                count[ord(letter) - ord('a')] -= 1
                continue
                
            while letterStack and letterStack[-1] > letter \
                              and count[ord(letterStack[-1]) - ord('a')] > 0:
                visited[ord(letterStack[-1]) - ord('a')] = False
                letterStack.pop()
                
            letterStack.append(letter)
            count[ord(letter) - ord('a')] -= 1
            visited[ord(letter) - ord('a')] = True

        return ''.join([letter for letter in letterStack])


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters("bbaaac"))
