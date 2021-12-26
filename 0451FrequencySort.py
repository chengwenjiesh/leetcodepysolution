class Solution:
    def frequencySort1(self, s: str) -> str:
        cnt = Counter(s)
        freq = [[] for _ in range(len(s) + 1)]

        for letter in cnt:
            freq[cnt[letter]].append(letter)

        result = ""
        for i in range(len(s), 0, -1):
            if freq[i]:
                for ch in freq[i]:
                    result += (ch * i)

        return result

    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        minpq = [(cnt[i], i) for i in cnt]
        heapq.heapify(minpq)

        result = ""
        while minpq:
            freq, ch = heapq.heappop(minpq)
            result += (ch * freq)

        return result[::-1]


