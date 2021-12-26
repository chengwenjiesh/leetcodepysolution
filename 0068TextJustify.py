from typing import List

class Solution:
    def partialJustify(self, words: List[str], maxWidth: int) -> List[str]:
        fullSen = ""
        for w in words:
            w += " "
            fullSen += w
        idx, size = 0, len(fullSen)

        result = []
        while idx < size:
            prev = idx
            idx += maxWidth

            if idx < size:
                if fullSen[idx] == " ":
                    idx += 1
                else:
                    while idx > 0 and fullSen[idx - 1] != " ":
                        idx -= 1
            else:
                idx = size

            padSize = maxWidth - (idx - prev)
            pad = " " * padSize
            result.append(fullSen[prev : idx] + pad)

        return result


    def fullJustify(self, words, maxWidth):
        return []

