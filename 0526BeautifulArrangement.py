class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [0 for _ in range(n)]
        cached = {}

        def formArrangement(used, visited):
            if used == n:
                return 1

            currState = "".join([str(v) for v in visited])
            if currState in cached:
                return cached[currState]

            cnt = 0
            for i in range(n, 0, -1):
                if not visited[i - 1] and (max(i, used + 1) % min(i, used + 1) == 0):
                    visited[i - 1] = 1
                    used += 1
                    cnt += formArrangement(used, visited)
                    visited[i - 1] = 0
                    used -= 1
            cached[currState] = cnt
            return cnt

        return formArrangement(0, visited)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countArrangement(8))

