class Solution:
    def simplifyPath(self, path: str) -> str:
        fullPath = path.split("/")
        pathStack = []

        for cur in fullPath:
            if cur == "..":
                if pathStack:
                    pathStack.pop()
            elif cur == "." or cur == "":
                continue
            else:
                cur = "/" + cur
                pathStack.append(cur)

        canonical = "".join(pathStack)
        return canonical if len(canonical) > 1 else "/"


