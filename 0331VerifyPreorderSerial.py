class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        visited = []
        curr = 0

        while curr < len(nodes) - 1:
            if nodes[curr] != "#":
                visited.append(curr)
            else:
                if not visited:
                    return False
                visited.pop()
            curr += 1

        return len(visited) == 0 and curr == len(nodes) - 1 and nodes[curr] == "#"


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

