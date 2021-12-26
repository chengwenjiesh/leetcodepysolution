from typing import List

class Solution:
    def wordsTyping(self, words: List[str], rows: int, cols: int) -> int:
        fullSen = ""
        for w in words:
            w += " "
            fullSen += w
        fullIdx, size = 0, len(fullSen)

        for i in range(rows):
            fullIdx += cols
            if fullSen[fullIdx % size] == " ":
                fullIdx += 1
            else:
                while fullIdx > 0 and fullSen[(fullIdx - 1) % size] != " ":
                    fullIdx -= 1

        return fullIdx // size


if __name__ == '__main__':
    sol = Solution()
    sentence = ["hello","world"]
    print(sol.wordsTyping(sentence, 4, 8))

