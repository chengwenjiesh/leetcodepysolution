from typing import List
from typing import Dict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        inDegree = [-1] * 26
        self.buildGraph(words, graph, inDegree)
        curr, nxt = [], []
        result = []

        for i in range(26):
            if inDegree[i] == 0:
                curr.append(chr(ord('a') + i))
            if inDegree[i] == -2:
                return ""

        while curr:
            result += curr[:]
            for ch in curr:
                candidates = graph.get(ch, [])
                for nxtCh in candidates:
                    inDegree[ord(nxtCh) - ord('a')] -= 1
                    if inDegree[ord(nxtCh) - ord('a')] == 0:
                        nxt.append(nxtCh)
            curr, nxt = nxt, []

        allVisited = True
        for d in inDegree:
            if d > 0:
                allVisited = False

        return "".join(result) if allVisited else ""

    def buildGraph(self, words: List[str], graph: Dict, inDegree: List[int]) -> None:
        for word in words:
            for c in word:
                if inDegree[ord(c) - ord('a')] == -1:
                    inDegree[ord(c) - ord('a')] = 0

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            if len(words[i - 1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                inDegree[0] = -2
                break

            l1, l2, idx1, idx2 = len(w1), len(w2), 0, 0
            while idx1 < l1 and idx2 < l2:
                if w1[idx1] != w2[idx2]:
                    if w1[idx1] in graph:
                        if w2[idx2] not in graph[w1[idx1]]:
                            graph[w1[idx1]].append(w2[idx2])
                            inDegree[ord(w2[idx2]) - ord('a')] += 1
                    else:
                        graph[w1[idx1]] = [w2[idx2]]
                        inDegree[ord(w2[idx2]) - ord('a')] += 1
                    break
                idx1 += 1
                idx2 += 1

if __name__ == '__main__':
    sol = Solution()
    words = ["ac","ab","zc","zb"]
    # words = ["er","ett"]
    print(sol.alienOrder(words))

